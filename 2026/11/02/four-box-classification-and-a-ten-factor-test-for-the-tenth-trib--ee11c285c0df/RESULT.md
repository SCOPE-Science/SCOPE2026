# Four-box classification and a ten-factor test for the tenth Tribonacci word

## Finding

Let \(\tau\) be the morphism \(\tau(0)=01\), \(\tau(1)=02\), \(\tau(2)=0\). Define \(T_j=\tau^j(0)\), with letters \(0,1,2\), and index positions from \(0\). The tenth word \(T_{10}\) has length \(504\). A string attractor is a set \(\Gamma\) of positions such that every nonempty factor has **some** occurrence whose position interval intersects \(\Gamma\).

**Theorem.** All the smallest attractors of \(T_{10}\) are the following four disjoint families of increasing position triples:

\[
\mathcal A(T_{10})=(A\times B\times D)\,\dot\cup\,(B\times C\times D)\,\dot\cup\,(B\times D\times E)\,\dot\cup\,(\{229\}\times D\times F),
\]

where the coordinate sets are

\[
\begin{aligned}
A&=\{80,82,93,95\},\\
B&=\{148,152,172,176\},\\
C&=\{229,231,242,244\},\\
D&=\{273,274,280,281,317,318,324,325\},\\
E&=\{354,356,367,369\},\\
F&=\{422,426,446,450\}.
\end{aligned}
\]

In particular, the total number of smallest attractors is

\[4\cdot4\cdot8+4\cdot4\cdot8+4\cdot8\cdot4+1\cdot8\cdot4=416.\]

**Ten-factor certificate.** A particular family of ten distinct nonempty factors \(f_0,\ldots,f_9\), explicitly embedded as `EXPECTED_MINIMAL_FACTORS[:10]` in `certify.py`, suffices: a three-position set is a string attractor if and only if it crosses an occurrence of every \(f_i\). Ten is optimal in the strongest sense that **no nine factors of \(T_{10}\)** can give an equivalent test on triples.

For context, the preceding ninth word \(T_9\) has length \(274\) and exactly \(224\) smallest attractors. Thus the next-stage count is \(416\), not \(448\); doubling the preceding finite count is not a valid stage-to-stage rule at this boundary.

## Assumptions and scope

The alphabet is exactly \(\{0,1,2\}\), with the morphism above, the iterate is exactly \(10\), and all intervals and positions are zero-based. A factor is a *contiguous* nonempty substring; crossing means the chosen position belongs to the closed occurrence interval. The factor test concerns sets of exactly three distinct positions, not arbitrary-size attractors. The theorem makes no statement about all later Tribonacci iterates.

## Proof

**Step 1: exact reduction to factor supports.** For each distinct nonempty factor \(u\) of \(T_{10}\), define its occurrence-support set
\[
I(u)=\bigcup_{[a,b)\,:\,T_{10}[a:b]=u}\{a,a+1,\ldots,b-1\}.
\]
An increasing triple \(P\) is an attractor if and only if \(P\cap I(u)\ne\varnothing\) for every factor \(u\). This is exactly the definition, with the existential choice of an occurrence evaluated by the union. The program `certify.py` enumerates all \(\binom{505}{2}=127260\) nonempty substring occurrences, builds all support sets as exact \(504\)-bit integers and finds \(80559\) distinct factors and \(79983\) different supports.

**Step 2: irredundant support antichain.** Sort the distinct supports by size, breaking ties numerically, and retain a support exactly if no previously retained support is contained in it. As every subset has no more elements than its superset, this algorithm returns *all* inclusion-minimal supports. The verified result is an antichain of exactly \(12\) supports, represented by the twelve explicit factors in `EXPECTED_MINIMAL_FACTORS`. Every factor support contains at least one of them. The first ten representatives are denoted \(f_0,\ldots,f_9\).

**Step 3: exhaustive triple count from signatures.** For a family \(I_0,\ldots,I_{r-1}\) of support sets, give each position \(p\) the \(r\)-bit signature with bit \(j\) set precisely when \(p\in I_j\). A triple hits every support if and only if the bitwise OR of its signatures has all \(r\) bits. Group the \(504\) positions by signature. For three *different* classes of sizes \(a,b,c\), the number of triples is \(abc\); for two coincident classes it is \(\binom a2c\); for three coincident classes it is \(\binom a3\). Summing only class multisets whose bitwise OR is complete is an exact, exhaustive count—each unordered position triple is counted once. The twelve-support system has \(133\) signature classes and exactly \(416\) solutions; the first ten supports have \(65\) classes and also exactly \(416\) solutions. Since the twelve-support solutions are a subset of the ten-support solutions, equality proves that all ten factors suffice for every original factor.

**Step 4: identification with four boxes.** Every triple in the four displayed Cartesian boxes hits the ten supports; the four boxes are disjoint and contain \(128,128,128,32\) triples. Their union therefore equals the entire \(416\)-element family found in Step 3. The independent `independent_replay.py` also enumerates all \(\binom{504}{3}=21210504\) candidate triples using distinct factor identifiers and checks exact equality with the four-box union. There can be no two-position attractor because \(T_{10}\) contains all three different one-letter factors, each requiring a position carrying its own letter. Thus all \(416\) are smallest.

**Step 5: optimality of the ten-factor certificate.** For each of the first ten minimal supports \(I(f_i)\), `certify.py` gives an explicit three-position witness \(W_i\), listed in `WITNESSES`, which misses \(I(f_i)\) and hits all other eleven minimal supports. Take any original factor \(u\). Because \(I(u)\) contains one of the twelve minimal supports, it cannot be missed by two distinct witnesses: if \(W_i\) misses \(I(u)\), every minimal support contained in \(I(u)\) must be \(I(f_i)\); the analogous statement for \(W_j\) with \(j\ne i\) is contradictory. Any family of factor tests equivalent to the attractor condition must reject every one of the ten distinct invalid triples \(W_i\). Since one factor can reject at most one, at least ten factors are necessary. The supplied ten achieve this bound.

## Verification

Run `python3 certify.py` and `python3 independent_replay.py` with Python 3.10 or newer and no nonstandard packages. Both terminate with `PASS`; their exact recorded output appears in `certify_output.txt` and `replay_output.txt`. The first program independently checks the factor-support antichain, the compressed signature count, four-box membership, and the ten exclusive invalid witnesses. The second reconstructs a distinct factor-ID coverage representation, tests every increasing triple directly for both \(T_9\) and \(T_{10}\), and compares the resulting attractor set with the displayed four-box formula. The word's ASCII SHA-256 is `b791afd79668cf46a43a74bf97563e159fc146b8902a13763ee0fe4191d9049e`.

## Relationship to prior work

Schaeffer and Shallit [1, Theorem 6] established that **every sufficiently long prefix** of the infinite Tribonacci word has minimum attractor size three and gave an explicit optimal triple. That result supplies the known size-three baseline, not the enumeration of all size-three attractors at this iterate or a minimal factor-test basis. Gheeraert, Romana and Stipulanti [2] construct attractors in families generalizing the Tribonacci word and discuss optimal sizes; their constructions do not state the four-box, \(416\)-triple classification. Banbara et al. [3] enumerate all minimum attractors of Fibonacci, period-doubling, and Thue–Morse words, motivating the analogous exact Tribonacci question; they do not enumerate Tribonacci attractors. General decision procedures could in principle compute these finite data, but the exact count, boxes and ten-factor minimality are not immediate stated corollaries. Unindexed computations remain a publication-priority risk.

## Limitations

This is a finite exact classification at one naturally distinguished morphism stage, not an infinite-stage theorem. Its factor-test optimality is for deciding the attractor property of *triples*, not arbitrary subsets. The numerical certificate exhausts the finite domain; the exact results and all dependencies are provided for reproducibility. Published-literature priority is not certified to be exhaustive.

## References

[1] L. Schaeffer and J. Shallit, *String Attractors for Automatic Sequences*, arXiv:2012.06840, first public 2020-12-12; Theorem 6 (Tribonacci), https://arxiv.org/pdf/2012.06840.

[2] F. Gheeraert, G. Romana and M. Stipulanti, *String attractors of some simple-Parry automatic sequences*, arXiv:2302.13647, first public 2023-02-27, https://arxiv.org/pdf/2302.13647; MSC2020 68R15.

[3] M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno and Y. Okamoto, *The Smallest String Attractors of Fibonacci, Period-Doubling, and Thue–Morse Words*, arXiv:2602.16152, first public 2026-02-18, https://arxiv.org/html/2602.16152 (current version extends an earlier paper).
