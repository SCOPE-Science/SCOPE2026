# Six-cell orbit-closure periodicity for exact clusters in Z^2

**Run:** SCOPE-20260917-001  
**Status of this note:** research proof draft; same-model reviewed, not peer reviewed.

## Main theorem

Let \(F\subset \mathbb Z^2\) be an exact cluster of full affine span with \(|F|=6\), and let \(T\) be any \(F\)-tiling. Then the orbit closure \(\overline{\mathbb Z^2\cdot T}\) contains a 1-periodic \(F\)-tiling.

Combined with Khetan's eight-cell counterexample and the already-known cases of cardinality <8, this would make 8 the sharp minimum cardinality for failure of orbit-closure 1-periodicity under the full-affine-span hypothesis.

The proof reuses Khetan's general spectral/dilation setup and his cardinality-independent “at most one infinite-zero direction” argument, but replaces the prime-square section argument in the other case by a six-point classification.

## Lemma 1: unequal-prime product tiles are axis-periodic

Let \(p,q\) be primes and let \(A,B\subset\mathbb Z\) satisfy \(|A|=p\), \(|B|=q\), \(\gcd(A-A)=\gcd(B-B)=1\). If \(T\) is an \((A\times B)\)-tiling of \(\mathbb Z^2\), then either
\[
(p,0)+T=T\qquad\text{or}\qquad(0,q)+T=T.
\]

### Proof

For row fibres \(S_y=\{x:(x,y)\in T\}\), Khetan's fibre decomposition gives, for every \(n\),
\[
R_n=\bigsqcup_{b\in B}S_{n-b},\qquad A\oplus R_n=\mathbb Z.
\]
The prime-cardinality one-dimensional rigidity theorem, together with \(\gcd(A-A)=1\), implies that \(A\) is a complete residue system modulo \(p\) and
\[
R_n=p\mathbb Z+r_n
\]
for a residue \(r_n\in\mathbb Z/p\mathbb Z\). Symmetrically, with column fibres \(V_x=\{y:(x,y)\in T\}\),
\[
C_m=\bigsqcup_{a\in A}V_{m-a}=q\mathbb Z+s_m,
\]
where \(B\) is a complete residue system modulo \(q\) and \(s_m\in\mathbb Z/q\mathbb Z\).

Let
\[
U=(x^p-1)T(x,y),\qquad W=(y^q-1)T(x,y).
\]
The fibre identities imply
\[
B(y)U=0,\qquad A(x)W=0.
\]
If \(r_n\) is constant, translate horizontally so that \(r_n=0\). Then every anchor has x-coordinate divisible by \(p\), hence \(W\) is supported on \(p\mathbb Z\times\mathbb Z\). Write
\[
W=\sum_{k\in\mathbb Z}x^{pk}w_k(y).
\]
Since \(A\) is a complete residue system modulo \(p\), the exponents \(a+pk\) are pairwise distinct; therefore \(A(x)W=0\) forces every \(w_k=0\). Thus \(W=0\) and \((0,q)\) is a period. The symmetric argument shows that constant \(s_m\) gives period \((p,0)\).

Assume now that \(s\) is nonconstant and put \(I=\operatorname{Im}(s)\subset\mathbb Z/q\mathbb Z\), so \(|I|\ge2\). A row \(y\) is nonempty iff \(y\bmod q\in I\): one direction follows from \(V_x\subset C_{x+a}\), and the converse from \(y\in C_m=\bigsqcup_aV_{m-a}\). For a nonempty row and any \(b,c\in B\),
\[
S_y\subset R_{y+b}\cap R_{y+c}.
\]
A nonempty intersection of two cosets of \(p\mathbb Z\) forces equality, so
\[
r_{y+b}=r_{y+c}
\]
for all \(b,c\in B\) whenever \(y\bmod q\in I\). Khetan's Lemma 3.7 applies with prime \(q\), the complete residue system \(B\), and the function \(r:\mathbb Z\to\mathbb Z/p\mathbb Z\) (its codomain may be any set). It forces \(r\) to be constant, hence the previous paragraph gives period \((0,q)\). ∎

## Lemma 2: section profiles forced by an infinite common-zero direction when |F|=6

Assume \(0\in F\), \(|F|=6\), and \(g_0=nh\ne0\) with \(h\) primitive. Suppose infinitely many \(\xi\in\ker\chi_{g_0}\) satisfy the common vanishing equations
\[
\sum_{g\in F}\chi_{\alpha g}(\xi)=0\qquad\text{for every }\gcd(\alpha,6)=1.
\]
Then the nonempty sections of \(F\) by lines parallel to \(h\) have one of the profiles
\[
(3,3),\qquad(2,4),\qquad(2,2,2).
\]
Moreover, there is one root of unity \(\omega\ne1\), common to all nonempty sections in this direction, such that
\[
\sum_{g\in F_\ell}\omega^{\langle g,h\rangle}=0
\]
for every such section \(F_\ell\).

### Proof

Follow the first half of Khetan's Lemma 3.15. Infinitely many common zeros lie on one component \(rh+tv\) of the kernel, with \(v=h^\perp\) and \(r=c/d\) reduced. For each admissible dilation \(\alpha\), the corresponding Laurent polynomial in \(z=e^{2\pi it}\) has infinitely many roots and is therefore identically zero.

Write
\[
d=\beta D,
\]
where \(D=2^a3^b\) is the maximal divisor of \(d\) whose prime factors are only 2 and 3. Then \(\gcd(\beta,6)=1\), so \(\alpha=\beta\) is among the dilation equations. Grouping the resulting zero Laurent polynomial by the value of \(\langle g,v\rangle\) gives, for every nonempty section,
\[
\sum_{g\in F_\ell}e^{2\pi i c\langle g,h\rangle/D}=0.
\]
Thus take \(\omega=e^{2\pi ic/D}\). If \(D=1\), each displayed sum is the positive integer \(|F_\ell|\), impossible. Hence \(\omega\ne1\). A one-point section also cannot vanish. Therefore every nonempty section has size at least 2. Full affine span rules out a single six-point line. The only partitions of 6 into at least two parts, every part at least 2, are precisely \((3,3),(2,4),(2,2,2)\). ∎

Call \((3,3)\) a **3-profile**, and the other two **even-profiles**.

## Main proof

Use Khetan's dynamical formulation. Let \(X=\overline{\mathbb Z^2\cdot T}\), choose an ergodic invariant probability measure \(\mu\) on \(X\), let \(f\) be the origin-anchor cylinder indicator, and let \(\nu\) be its spectral measure. Khetan's Theorem 3.16 (from Bhattacharya) gives a minimal finite set \(\Delta\subset\mathbb Z^2\setminus\{0\}\) such that
\[
\operatorname{supp}\nu\subseteq\bigcup_{g\in\Delta}\ker\chi_g,
\]
and minimality makes the directions in \(\Delta\) pairwise nonparallel.

### Case I: at least two directions carry infinitely many common zeros

By Lemma 2, each such direction has either a 3-profile or an even-profile.

**Two 3-profiles are impossible.** Each uses two support lines. Two transverse families of two lines have at most four intersection points, but \(|F|=6\).

**A 3-profile and an even-profile.** The even-profile cannot be \((2,4)\), since two-by-two transverse line families again give at most four intersections. Therefore it is \((2,2,2)\). We have two lines in one direction and three in the other, hence at most six intersections; all six points of \(F\) force every intersection to be occupied. Thus \(F\) is a full 2-by-3 grid. Using primitive direction vectors \(u,v\), the standard grid-coordinate argument shows
\[
F=\{au+bv:a\in A,\ b\in B\},\qquad |A|=3,\ |B|=2.
\]
Full affine span forces \(|\det(u,v)|=1\) and \(\gcd(A-A)=\gcd(B-B)=1\). In these unimodular coordinates, \(F=A\times B\). Since it tiles \(\mathbb Z^2\), Lemma 1 applies and the original tiling \(T\) is already 1-periodic.

**Two even-profiles.** If either profile were \((2,4)\), it would use two lines. The other cannot also use two lines (only four intersections), so it would have to use three lines. Six points would then fill all intersections of a 2-by-3 grid, making each of the two first-family lines contain three points, contradicting its even profile. Hence both profiles must be \((2,2,2)\).

The six occupied intersections of the two 3-line families form a 2-regular bipartite graph on 3+3 vertices. Its complement in \(K_{3,3}\) is a perfect matching. Relabel the second family \(C_1,C_2,C_3\) so the occupied intersections are exactly \(i\ne j\). Fix the primitive vector \(h\) in the first direction and let \(q=\langle h,h\rangle\). Lemma 2 supplies a single common root \(\omega\) for all three first-direction sections.

For each pair \(C_j,C_k\), exactly one first-direction section contains their two intersections. Their difference is \(n_{jk}h\) for an integer \(n_{jk}\), and the two-term vanishing equation gives
\[
\omega^{q n_{jk}}=-1.
\]
Choose orientations so \(n_{13}=n_{12}+n_{23}\). Then
\[
\omega^{q n_{13}}=\omega^{q n_{12}}\omega^{q n_{23}}=(-1)(-1)=1,
\]
contradicting the same two-term equation for the pair \((1,3)\). Thus two even-profile directions are impossible.

Therefore the only possible instance of Case I is the mixed profile, and there \(T\) itself is periodic. If three or more infinite-zero directions existed, two would have the same one of the two profile types by pigeonhole, already impossible.

### Case II: at most one direction carries infinitely many common zeros

Khetan's Case (2) in the proof of Theorem 3.18 is cardinality-independent once the available dilations are indexed by integers coprime to \(|F|\). The needed dilation theorem (Theorem 3.12) is stated for every \(\alpha\) coprime to \(|F|\), and Lemma 3.13 likewise gives the common vanishing equations for all such \(\alpha\). Replacing “\(\alpha\) coprime to \(p\)” in that branch by “\(\alpha\) coprime to 6” leaves the proof unchanged: all but at most one spectral kernel contribute only finitely many common zeros; minimal finite exceptional support is isolated; the remaining character values are non-roots of unity; the integer-valued exponential-sum rigidity lemma forces \(g_0\cdot f=f\). Khetan's Theorem 3.11 then yields that \(\mu\)-almost every tiling in \(X\) is 1-periodic. Hence \(X\) contains a 1-periodic \(F\)-tiling.

The two cases exhaust all possibilities, proving the theorem. ∎

## Computational sanity check for Lemma 1

The attached script `scope_unequal_prime_axis_periodicity_check.py` exhaustively enumerates exact tilings of the 6-by-6 torus by
\[
A\times B,\quad A=\{0,1\},\ B=\{0,1,5\},
\]
with factor cardinalities 2 and 3. It enumerates 60 tilings; every one has period \((2,0)\) or \((0,3)\). This is only a finite sanity check, not part of the proof.

## Sources checked

- Abhishek Khetan, *A Counterexample to Nivat's Conjecture for a Non-Convex Window of Full Affine Span*, arXiv:2607.09830v2 (2026), especially Lemmas 3.6, 3.7, 3.13, 3.15; Proposition 3.9; Theorems 3.11, 3.12, 3.16, 3.18; §3.5.
- Hui Rao and Yu-Mei Xue, *Tiling Z^2 with translations of one set*, DMTCS 8 (2006), 129–140, DOI 10.46298/dmtcs.366.
- Current MathDB entry for the periodic orbit-closure conjecture, which at the time of this run recorded no solution to the six-cell gap.

## Audit caveat

This is a same-model review research draft, not independent verification or peer review. The main correctness risk is an unnoticed dependency on the prime-square hypothesis inside the imported spectral Case II; the cited proof was checked line-by-line for that dependency and none was found beyond the dilation index set, which is already available for \(|F|=6\). The main originality risk is equivalent coverage under different tiling/factorization terminology in older literature.
