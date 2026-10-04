# Exact Fuglede census for \(\mathbb Z_4\times\mathbb Z_2^2\)
## Finding
Let \(G=\mathbb Z/4\mathbb Z\times(\mathbb Z/2\mathbb Z)^2\). Every nonempty subset \(A\subseteq G\) is spectral if and only if it tiles \(G\) by translations. Exactly \(3147\) nonempty subsets have these equivalent properties. By cardinality \(|A|=1,2,4,8,16\), the exact counts are \(16,120,1436,1574,1\), and no other size occurs. Under the full affine automorphism group of \(G\), these sets form respectively \(1,3,10,12,1\) orbits, hence exactly \(27\) affine classes.

## Assumptions and scope
The group is the additive finite abelian group
\[
G=\mathbb Z/4\mathbb Z\times\mathbb Z/2\mathbb Z\times\mathbb Z/2\mathbb Z.
\]
Its dual is identified with \(G\) through
\[
\chi_k(x)=i^{k_1x_1+2k_2x_2+2k_3x_3}.
\]
A set \(A\subseteq G\) is spectral when the restrictions to \(A\) of \(|A|\) characters form an orthogonal basis of the complex functions on \(A\). It tiles when there is a set \(T\subseteq G\) for which every element of \(G\) has a unique representation \(a+t\) with \(a\in A\) and \(t\in T\). The statement concerns all nonempty subsets of this one group and does not extrapolate to larger \(2\)-groups.

## Proof
For \(A\subseteq G\), put
\[
\widehat{1_A}(k)=\sum_{x\in A}\chi_k(x),
\qquad
Z(A)=\{k\in G:\widehat{1_A}(k)=0\}.
\]
If \(B\subseteq G\), then the characters indexed by \(B\) are pairwise orthogonal on \(A\) exactly when
\[
(B-B)\setminus\{0\}\subseteq Z(A).
\]
Thus \(B\) is a spectrum exactly when \(|B|=|A|\) and the displayed inclusion holds. Translation of \(B\) preserves this condition, so a candidate spectrum may be normalized to contain \(0\).

Similarly, \(A\) and \(T\) tile \(G\) exactly when
\[
|A||T|=16
\quad\text{and}\quad
(A-A)\cap(T-T)=\{0\}.
\]
Indeed, the second condition makes the addition map \(A\times T\to G\) injective, while the first condition gives equal finite cardinalities and hence bijectivity. Translation again allows \(0\in T\).

The Fourier-zero test is exact without floating point. Every character value is one of \(1,i,-1,-i\). For fixed \(k\), let \(n_r\) be the number of points \(x\in A\) for which
\[
k_1x_1+2k_2x_2+2k_3x_3\equiv r\pmod 4.
\]
Then
\[
\widehat{1_A}(k)=(n_0-n_2)+i(n_1-n_3),
\]
so
\[
\widehat{1_A}(k)=0
\quad\Longleftrightarrow\quad
n_0=n_2\ \text{and}\ n_1=n_3.
\]

The bundled verifier enumerates every one of the \(2^{16}-1=65535\) nonempty subsets \(A\). For each \(A\), it constructs the Cayley compatibility graph on \(G\) whose distinct vertices \(b,b'\) are adjacent exactly when \(b-b'\in Z(A)\). A spectrum exists exactly when the neighborhood search contains a clique of size \(|A|\) after the translation normalization \(0\in B\). Independently, for tiling it constructs the compatibility graph in which \(t,t'\) are adjacent exactly when \(t-t'\notin(A-A)\setminus\{0\}\), and it searches for a clique of size \(16/|A|\) after normalizing \(0\in T\). These tests are the two exact criteria above, so the finite search is exhaustive rather than heuristic.

No mismatch occurs. The common positive counts are
\[
\begin{array}{c|ccccc}
|A|&1&2&4&8&16\\\hline
\#A&16&120&1436&1574&1.
\end{array}
\]
Their sum is \(3147\), and all other cardinalities have zero spectral and tiling sets.

For the affine classification, every endomorphism is determined by the images of the three standard generators. The order-two generators must map into the \(2\)-torsion subgroup; exhaustively retaining exactly the bijective maps yields \(192\) automorphisms. Combining them with the \(16\) translations gives \(3072\) affine automorphisms. Exact orbit closure of the \(3147\) accepted subsets gives
\[
1,3,10,12,1
\]
orbits in sizes \(1,2,4,8,16\), respectively, totaling \(27\).

## Verification
Running `python verify.py` uses only the Python standard library and exact integer arithmetic. It re-enumerates all \(65535\) nonempty subsets, independently applies the spectral and tiling predicates, checks equality subset by subset, checks the exact size census, enumerates all \(192\) automorphisms and all \(3072\) affine maps, and verifies the full affine-orbit census. The reviewed output is:

`VERIFY_OK subsets=65535 accepted=3147 sizes=16,120,1436,1574,1 aut=192 affine=3072 orbits=1,3,10,12,1`

The computation is a finite exhaustive proof of this finite classification. It does not certify any statement about groups of larger order.

## Relationship to prior work
Malikiosis surveys the finite-abelian Fuglede problem and records positive two-generator families including \(\mathbb Z_p\times\mathbb Z_p\), \(\mathbb Z_p\times\mathbb Z_{p^2}\), and \(\mathbb Z_p\times\mathbb Z_{p^n}\). The group treated here has three generators and invariant factors \(4,2,2\), so those theorems do not contain it. Shi's theorem for \(\mathbb Z_{p^2}\times\mathbb Z_p\) specializes at \(p=2\) to the order-eight group \(\mathbb Z_4\times\mathbb Z_2\), not to the present order-sixteen group. Zhang's theorem for \(\mathbb Z_p\times\mathbb Z_{p^n}\) is likewise a two-generator result. Kiss--Somlai treat \(\mathbb Z_p^2\times\mathbb Z_q\) for distinct primes \(p,q\), which also does not specialize to \(\mathbb Z_4\times\mathbb Z_2^2\).

The closest exact small-group result found in the literature concerns different group structures, while targeted searches under the aliases \(\mathbb Z_4\times\mathbb Z_2\times\mathbb Z_2\), \(\mathbb Z_4\times\mathbb Z_2^2\), order-sixteen finite abelian Fuglede, spectral-set census, and affine classification did not locate a statement implying the present census. An obscure small-group computation or differently indexed classification remains a residual priority risk.

## Limitations
The result is a complete finite classification only for \(\mathbb Z_4\times\mathbb Z_2^2\). It gives no inductive theorem for \(\mathbb Z_4\times\mathbb Z_2^m\), no general rank-three \(2\)-group theorem, and no asymptotic statement. The exact counts and orbit numbers depend on exhaustive finite enumeration. Literature searches cannot exclude an unindexed or differently phrased earlier census.

## References
1. R. D. Malikiosis, *On the structure of spectral and tiling subsets of cyclic groups*, arXiv:2005.05800, first public version 2020-05-12; *Forum of Mathematics, Sigma* 10 (2022), e23, DOI: 10.1017/fms.2022.14. Primary MSC 43A46.
2. R. Shi, *Equi-distributed property and spectral set conjecture on \(\mathbb Z_{p^2}\times\mathbb Z_p\)*, arXiv:1906.11717; *Journal of the London Mathematical Society* 102 (2020), 1030--1046, DOI: 10.1112/jlms.12346.
3. T. Zhang, *Fuglede's Conjecture Holds in \(\mathbb Z_p\times\mathbb Z_{p^n}\)*, arXiv:2109.08400; *SIAM Journal on Discrete Mathematics* 37 (2023), 1180--1197, DOI: 10.1137/22M1493598.
4. G. Kiss and G. Somlai, *Fuglede's conjecture holds on \(\mathbb Z_p^2\times\mathbb Z_q\)*, *Proceedings of the American Mathematical Society* 149 (2021), 4181--4188, DOI: 10.1090/proc/15541.
