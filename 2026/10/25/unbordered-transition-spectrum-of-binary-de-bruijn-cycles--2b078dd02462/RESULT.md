# Unbordered transition spectrum of binary de Bruijn cycles

## Finding

A binary circular de Bruijn word of order \(k\) is a circular binary word of length \(2^k\) in which every binary length-\(k\) word occurs exactly once as a circular factor. An ordinary finite binary word is *unbordered* if no nonempty proper prefix is also a suffix. Let \(U_k(B)\) be the number of distinct unbordered circular length-\(k+1\) factors of such a cycle \(B\).

For every integer \(k\ge2\), each \((k-1)\)-bit word \(v\) has a uniquely determined **crossing bit** \(\epsilon_v\in\{0,1\}\) for which the cyclic successor of the length-\(k\) factor \(av\) is \(v(a\oplus\epsilon_v)\), for \(a\in\{0,1\}\), where \(\oplus\) denotes addition modulo two. Define
\[
c_k(v)=\mathbf1_{\{0v1\text{ is unbordered}\}}+\mathbf1_{\{1v0\text{ is unbordered}\}}.
\]
Then the all-order weighted-feedback identity is
\[
\boxed{U_k(B)=\sum_{v\in\{0,1\}^{k-1}}c_k(v)\epsilon_v.}
\]
For the number \(T_k(B)=\sum_v\epsilon_v\) of crossing vertices, there is also a universal constraint
\[
\boxed{T_k(B)\ge N_k-1,\qquad T_k(B)\equiv N_k-1\pmod2,}
\]
where \(N_k\) is the number of binary necklaces of length \(k\), equivalently the number of orbits of length-\(k\) binary words under cyclic rotation.

At order \(k=5\), the weights are \(c_5(v)=2\) exactly for
\[
v\in\{0000,0110,1001,1111\},
\]
and \(c_5(v)=1\) for each of the other twelve \(4\)-bit words. Hence
\[
U_5(B)=T_5(B)+\epsilon_{0000}+\epsilon_{0110}+\epsilon_{1001}+\epsilon_{1111}.
\]
Across all \(2048\) binary de Bruijn cycles of order five, counted up to rotation only, the **complete distribution** of \(U_5\) is:

| Number of unbordered length-six factors | Number of cycles |
| ---: | ---: |
| 9 | 192 |
| 10 | 288 |
| 11 | 160 |
| 12 | 576 |
| 13 | 320 |
| 14 | 160 |
| 15 | 288 |
| 17 | 64 |

There are no other attainable values (in particular, \(16\) does not occur). The uniform average and variance are
\[
\boxed{\mathbb E[U_5]=\tfrac{49}{4},\qquad\operatorname{Var}(U_5)=\tfrac{63}{16}.}
\]

## Assumptions and scope

Cycles are identified under rotation, **not** under bit complementation or reversal. Each circular factor may wrap around the displayed end of a representative. Distinctness concerns factor strings rather than starting indices. Since distinct circular length-\(k+1\) factors have distinct length-\(k\) prefixes, all \(2^k\) circular length-\(k+1\) factors in an order-\(k\) cycle are themselves distinct. The all-order identities hold for every integer \(k\ge2\). The exact distribution and moment claims concern order five only.

## Proof

**1. Local transition representation.** In an order-\(k\) cycle, each length-\(k\) state \(av\), with \(a\in\{0,1\}\) and \(|v|=k-1\), occurs once. Its successor is necessarily \(vb\) for some \(b\in\{0,1\}\). For fixed \(v\), the two states \(0v\) and \(1v\) have different successors, since each length-\(k\) state must occur once. Thus the two possible successor last bits form a bijection of \(\{0,1\}\), which is necessarily \(b=a\oplus\epsilon_v\) for a unique \(\epsilon_v\in\{0,1\}\). Conversely, any assignment of the crossing bits defines the permutation
\[
P_\epsilon(av)=v(a\oplus\epsilon_v)
\]
on all \(2^k\) length-\(k\) binary states: for each target \(vb\), its unique predecessor is \((b\oplus\epsilon_v)v\). The assignment represents a circular de Bruijn word precisely when \(P_\epsilon\) is one cycle containing all \(2^k\) states. Each such single-cycle permutation gives one cyclic word up to rotation, and conversely. This proves the bijection used below.

**2. Unbordered-factor identity.** The length-\(k+1\) circular word contributed at \(av\) is \(av(a\oplus\epsilon_v)\). If \(\epsilon_v=0\), its first and last letters are equal, so it has a border of length one. If \(\epsilon_v=1\), its two possible words are precisely \(0v1\) and \(1v0\), contributing \(c_k(v)\) unbordered factors. Summing across the partition by \(v\) proves the boxed weighted-feedback identity. No independence assumption on the crossing bits is made.

**3. All-order switch constraint.** When all crossing bits vanish, \(P_0(av)=va\) rotates each length-\(k\) word one place. Its disjoint orbits are the binary necklaces, so it has \(N_k\) cycles. Changing the crossing bit at one \(v\) interchanges the images of \(0v\) and \(1v\); in permutation language this composes with a single transposition, thereby splitting one permutation cycle into two or joining two into one. Starting with \(N_k\) cycles, reaching the single-cycle de Bruijn permutation by performing \(T_k\) switches thus requires \(T_k\ge N_k-1\) and \(T_k\equiv N_k-1\pmod2\).

**4. Order-five weights and exhaustive finite classification.** For each of the sixteen binary length-four strings \(v\), check the proper prefix/suffix equalities of the two length-six words \(0v1\) and \(1v0\). Exactly \(v=0000,0110,1001,1111\) makes both unbordered; each other \(v\) makes exactly one unbordered. This gives the displayed order-five formula, independently checked in the accompanying program.

There are exactly \(2^{16}=65536\) crossing-bit masks. The checker visits **every** mask. For each mask it starts at the all-zero length-five state, applies the explicitly defined permutation \(P_\epsilon\) at most \(32\) times, and accepts the mask if and only if it returns to that state after visiting all \(32\) distinct states. Because \(P_\epsilon\) is a permutation, this condition is equivalent to having one cycle. For an accepted mask, the checker computes the integer statistic directly from the sixteen weights. The exhaustive loop produces the eight rows in the table and exactly \(2048\) accepted masks.

A second, independent enumeration generates binary strings beginning with \(00000\), successively rejecting repeated length-five windows, and tests the cyclic wraparound windows on completion. Every order-five cycle has a **unique** circular occurrence of \(00000\), so this procedure generates each cyclic cycle once. It independently produces exactly \(2048\) cycles and the identical table by directly testing all circular length-six factors for borders. The two fully specified generators, with assertions for orders two through five, are in `verify.py`. These finite exhaustive algorithms establish the **order-five** distribution, while Steps 1–3 prove the structural statements at **all** orders.

Finally, summing the table gives \(2048\) and the exact first and second moments
\[
\frac{1}{2048}\sum_B U_5(B)=\frac{49}{4},\qquad
\frac{1}{2048}\sum_B U_5(B)^2=154.
\]
Subtracting the squared mean gives the variance \(63/16\), as claimed.

## Verification

Run `python3 verify.py` with the standard Python library. The script checks two logically separate complete enumerations for orders \(2,3,4,5\), exact weight classification, order-five crossing-count totals, the eight-cell distribution, and rational moments. It prints `PASS: two independent complete enumerators and weight table` on success. The algorithms search precisely specified finite spaces, and the accompanying proof establishes exhaustiveness; there is no extrapolation from finitely many cases to the all-order identity.

## Relationship to prior work

The 2015 work on maximal unbordered factors studies longest unbordered substrings and random-word length bounds. Standard work on de Bruijn sequences establishes counting and Hamiltonian/Eulerian representations but not, in the material inspected, the distribution of their unbordered length-\(k+1\) factors. Later work on locally constrained de Bruijn codes addresses repeated windows and code sizes rather than the full border-free motif spectrum. This result studies the **first factor length beyond the universally present length-\(k\) words** and refines basic de Bruijn enumeration by a border-sensitive statistic and a local feedback identity.

## Limitations

The distribution and moments are proved only for binary order five, not all orders or larger alphabets. The general feedback identity does not give a closed-form count of admissible crossing masks for arbitrary order. The computational certificate is finite and does not assert additional asymptotic results. Literature searches do not establish absolute priority; no independent audit was performed.

## References

1. A. Loptev, G. Kucherov, and T. Starikovskaya, *On Maximal Unbordered Factors*, arXiv:1504.07406, first public version 2015-04-28; CPM 2015.
2. L. Kari and Z. Xu, *De Bruijn Sequences Revisited*, *International Journal of Foundations of Computer Science* 23 (2012), 1307–1321, DOI: 10.1142/S0129054112400540. Public author manuscript was inspected.
3. Y. M. Chee, T. Etzion, H. M. Kiah, S. Marcovich, A. Vardy, V. K. Vu, and E. Yaakobi, *Locally-Constrained de Bruijn Codes: Properties, Enumeration, Code Constructions, and Applications*, *IEEE Transactions on Information Theory* 67 (2021), 7857–7876, DOI: 10.1109/TIT.2021.3112300.
4. N. G. de Bruijn, *A combinatorial problem*, *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen* 49 (1946), 758–764.
