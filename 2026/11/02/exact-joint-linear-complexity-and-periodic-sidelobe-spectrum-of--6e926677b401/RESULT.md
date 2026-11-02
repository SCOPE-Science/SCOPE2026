# Exact joint linear-complexity and periodic-sidelobe spectrum of binary order-five de Bruijn cycles

## Finding

There are exactly \(2,048\) binary de Bruijn cycles of order five, counted up to rotation but **not** up to reversal or symbol complement. Each such cycle is a binary periodic word \(W=(w_i)_{i\in\mathbb Z/32\mathbb Z}\) in which every binary length-five word occurs exactly once as a cyclic factor.

For each cycle, define its periodic linear complexity \(L(W)\) as the minimum order of a homogeneous linear feedback recurrence over \(\mathbb F_2\) generating the bi-infinite periodic word. Define its largest absolute nontrivial periodic autocorrelation sidelobe as
\[
P(W)=\max_{1\le t\le31}\left|\sum_{i=0}^{31}(-1)^{w_i+w_{i+t}}\right|.
\]
The complete number of cycles at each \((L,P)\) is as follows (unlisted cells are zero).

| \(L\) | \(P=4\) | \(P=8\) | \(P=12\) | \(P=16\) | \(P=20\) | \(P=24\) | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 21 | 0 | 0 | 0 | 8 | 0 | 0 | 8 |
| 23 | 0 | 0 | 0 | 4 | 0 | 8 | 12 |
| 24 | 0 | 0 | 12 | 0 | 8 | 0 | 20 |
| 25 | 0 | 4 | 24 | 0 | 4 | 0 | 32 |
| 26 | 0 | 20 | 16 | 0 | 0 | 0 | 36 |
| 27 | 4 | 18 | 28 | 14 | 0 | 0 | 64 |
| 28 | 0 | 84 | 60 | 28 | 8 | 0 | 180 |
| 29 | 0 | 72 | 110 | 38 | 4 | 0 | 224 |
| 30 | 0 | 148 | 212 | 56 | 28 | 4 | 448 |
| 31 | 8 | 426 | 420 | 134 | 36 | 0 | 1024 |
| **Total** | **12** | **772** | **882** | **282** | **88** | **12** | **2048** |

Exactly eight cycles attain both the maximum linear complexity \(L=31\) and the minimum possible peak sidelobe \(P=4\). The twelve cycles with \(P=4\) are three four-element orbits under reversal and bitwise complement. Rooting each cycle at its unique occurrence of `00000`, the lexicographically least representatives and their linear complexities are:

| Representative | \(L\) | Orbit size |
|---|---:|---:|
| `00000100011101001010110011011111` | 31 | 4 |
| `00000100011111010011011100101011` | 31 | 4 |
| `00000100101100110111000111110101` | 27 | 4 |

## Assumptions and scope

The alphabet is \(\{0,1\}\), indices are cyclic modulo \(32\), and each cycle is considered once under cyclic rotation only. The usual degree of a linear recurrence is its order over \(\mathbb F_2\); it is not the nonlinear shift-register stage count, which equals five for every cycle here. The sidelobe definition uses absolute values and excludes shift zero. No normalization by \(32\) is used.

The result is an exact finite computation of a natural two-invariant distribution. It does not assert any corresponding distribution, or optimized tradeoff, for higher orders.

## Proof

**1. Exhaustive and nonredundant enumeration.** A cycle determines a cyclic permutation of all \(32\) five-bit states: the successor of a window is the window shifted one place and appended with the next symbol. Write each state as \((a,u)\), where \(a\in\{0,1\}\) and \(u\in\{0,1\}^{4}\). Because every state occurs once, the successor map must be bijective. The two states \((0,u)\), \((1,u)\) can only have successors \((u,0)\), \((u,1)\), in one order or the other. Thus a unique Boolean function \(g:\{0,1\}^4\to\{0,1\}\) determines the successor as
\[
T_g(a,u)=(u,a\mathbin{\oplus}g(u)).
\]
Conversely, if the orbit of `00000` under \(T_g\) has length \(32\), it visits each five-bit state once and describes a de Bruijn cycle. Each cycle contains exactly one `00000`, so this starting point is canonical, and each valid cycle corresponds to exactly one of the \(2^{16}=65,536\) truth tables for \(g\). The `feedback_cycles` procedure in `verify.py` checks each truth table, exactly enumerating all valid cycles. It finds \(2,048\), with no duplicates. For a second enumeration, the `eulerian_cycles` procedure traverses every Euler tour of the order-four binary de Bruijn graph, rooted at the unique edge `00000`, and obtains exactly the same set of \(2,048\) rooted cycles. Every order-five cycle is exactly one such Euler tour, so these two constructions prove exhaustion, not sampling.

**2. Two independent exact linear-complexity evaluations.** For a cycle define \(S_W(x)=\sum_{i=0}^{31}w_i x^i\) over \(\mathbb F_2\). The generating series of its one-sided periodic expansion is \(S_W(x)/(1-x^{32})\). Because \(1-x^{32}=(1+x)^{32}\) in characteristic two, cancellation shows that its minimal recurrence degree is
\[
L(W)=32-v_{x+1}\bigl(S_W(x)\bigr),
\]
where \(v_{x+1}\) is the number of factors \((x+1)\) in the polynomial, counted with multiplicity. Every de Bruijn cycle has exactly \(16\) ones, so \(S_W(1)=0\) and \(L(W)\le31\); the displayed table exhibits cycles attaining this bound. The numerator is nonzero for a de Bruijn cycle. The checker computes this multiplicity by exact \(\mathbb F_2\) polynomial division and independently computes linear complexity by the recursive Games–Chan half-block XOR algorithm. Both agree on all cycles.

**3. Two independent exact sidelobe evaluations.** Put \(s_i=(-1)^{w_i}\). The periodic autocorrelation is \(\sum_i s_i s_{i+t}\). Equivalently, if \(d_t\) is the Hamming distance between \(W\) and its rotation by \(t\), then \(R_W(t)=32-2d_t\). The checker separately evaluates every signed inner product and every bitwise XOR/Hamming distance, for all \(31\) nonzero shifts, and verifies agreement on all \(2,048\) cycles.

**4. Certificate and counting.** The bundled standalone program `verify.py` uses the two full enumerators and both independent evaluations of each invariant. It checks every cell in the displayed table, every row/column sum, the total \(2,048\), the set of \(12\) smallest-peak cycles, and the sizes and exact canonical representatives of their reversal-complement orbits. All tests complete with the exact output `VERIFY_OK cycles=2048 joint_cells=32 optimal=8 best_orbits=3 independent_enumerations=2 independent_invariant_checks=2`. Together with the enumeration-exhaustiveness arguments above, this certifies the finite classification without an assumption that a finite sample represents a larger population.

## Verification

Run `python3 verify.py` using Python 3.8 or later; the standard library suffices. Every numerical cell is reproduced from the truth-table construction rather than read from an external table. The independent Euler-tour enumeration, polynomial/Games–Chan comparison, signed-dot-product/XOR comparison, and orbit tests provide separate cross-checks. The program's running time and memory needs are small at this fixed order.

## Relationship to prior work

Holdahl's 1983 thesis gives the marginal complexity distribution at order five, with counts \((8,12,20,32,36,64,180,224,448,1024)\) for the ten occurring degrees. Etzion and Lempel (1984) and Etzion (1985, 1999) analyze distributions and bounds for linear complexity; their inspected statements do not give a joint classification with periodic sidelobes. Spinsante, Andrenacci and Gambi (2011) enumerate length-32 de Bruijn correlation behavior and obtain \(12\) cycles with largest absolute sidelobe \(4\), and \(784\) with largest sidelobe at most \(8\). Fujisaki and Nabeshima (2011) examine autocorrelation bounds and extremal behavior. Neither inspected correlation study gives the linear-complexity intersection counts. Marginal distributions alone do not mathematically determine the joint counts, and no such inference is made.

The distinctive fact here is the simultaneous count: exactly eight of the twelve minimum-sidelobe cycles also have maximum binary linear complexity. These are two distinct reversal-complement orbits. This classification refines known **separate** finite-order invariants. It is not a claim to have discovered the known individual extrema.

## Limitations

The assertion is restricted to order-five binary de Bruijn cycles, with absolute *periodic* autocorrelation. It does not concern aperiodic sidelobes, cross-correlation between different cycles, higher de Bruijn orders, or actual communications-system error rates. Exhaustive computational verification certifies this fixed finite collection through the proved exhaustive enumeration; it is not an infinite-family proof. Historically unindexed computations may contain an equivalent table, so precedence should be independently checked.

## References

1. R. L. Holdahl, *On the Distribution of Complexity for de Bruijn Sequences*, Naval Postgraduate School thesis (June 1983), esp. Chapter III, Table 3.2. https://commons.wikimedia.org/wiki/File:On_the_distribution_of_complexity_for_de_Bruijn_sequences._(IA_ondistributionof00hold).pdf
2. T. Etzion and A. Lempel, *On the Distribution of de Bruijn Sequences of Given Complexity*, IEEE Transactions on Information Theory (1984), DOI: 10.1109/TIT.1984.1056933; author-open text: https://etzion.net.technion.ac.il/files/2016/02/P3.pdf
3. T. Etzion, *On the Distribution of de Bruijn Sequences of Low Complexity* (1985), author-open text: https://etzion.net.technion.ac.il/files/2016/02/P5.pdf
4. T. Etzion, *Linear Complexity of de Bruijn Sequences—Old and New Results*, IEEE Transactions on Information Theory (1999); author-open text: https://etzion.net.technion.ac.il/files/2016/02/P51.pdf
5. S. Spinsante, S. Andrenacci, and E. Gambi, *Binary De Bruijn Sequences for DS-CDMA Systems: Analysis and Results*, EURASIP Journal on Wireless Communications and Networking 2011, article 4 (published June 6, 2011). DOI: 10.1186/1687-1499-2011-4. https://link.springer.com/article/10.1186/1687-1499-2011-4
6. H. Fujisaki and Y. Nabeshima, *On Auto-correlation Values of de Bruijn Sequences*, NOLTA 2(4), 400–408 (2011). https://www.jstage.jst.go.jp/article/nolta/2/4/2_4_400/_pdf/-char/en
