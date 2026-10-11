# Sharp four-point self-disjoint Fourier supports on \(\mathbb F_p^2\) for \(p\equiv3\pmod8\)

## Finding
For an odd prime \(p\), let \(G=\mathbb F_p^2\) with its standard dot product and the unitary finite Fourier transform described below. Define the self-disjoint-support invariant
\[
\sigma_p=\min\left\{\left|\operatorname{supp}f\right|:\;0\ne f:G\to\mathbb C,\ \operatorname{supp}f\cap\operatorname{supp}\widehat f=\varnothing\right\}.
\]
For every prime \(p\equiv3\pmod8\), the exact value is
\[
\boxed{\sigma_p=4.}
\]
Every such prime admits an explicit four-point signal; every nonzero signal with one, two, or three support points intersects its own Fourier support. In particular, the exact minimum remains four along arbitrarily large primes in this congruence class.

## Assumptions and scope
The group is \(G=\mathbb F_p^2\), and the Fourier identification of \(G\) with its character group is fixed by the *standard coordinate dot product*, not an arbitrary nondegenerate bilinear form. Put \(\zeta=\exp(2\pi i/p)\), and normalize
\[
\widehat f(\xi)=\frac1p\sum_{x\in G}f(x)\zeta^{x\cdot\xi},\qquad \xi\in G.
\]
Support means the set of points with nonzero complex coefficient. The theorem concerns all nonzero complex-valued functions on \(G\) and all primes \(p\equiv3\pmod8\), including \(p=3\). The use of complex coefficients is essential to the stated explicit witness; no real-valued restriction is asserted.

## Proof
**Step 1: a four-point support and explicit signal.** For \(p\equiv3\pmod8\), the supplementary quadratic-reciprocity formula gives
\[
\left(\frac{-2}{p}\right)=\left(\frac{-1}{p}\right)\left(\frac2p\right)=(-1)(-1)=1.
\]
Thus choose \(a\in\mathbb F_p^\times\) with \(a^2=-2\). Set \(u=(0,1)\), \(v=(a,0)\), and
\[
S=\{0,u,v,v-u\}=\{(0,0),(0,1),(a,0),(a,-1)\}.
\]
These are four distinct points. Define
\[
f(0)=1,\quad f(u)=-1,\quad f(v)=\zeta,\quad f(v-u)=-\zeta,\quad f(x)=0\ \text{otherwise}.
\]
All four displayed values are nonzero. For any \(\xi\in G\),
\[
p\widehat f(\xi)=1-\zeta^{u\cdot\xi}+\zeta^{1+v\cdot\xi}-\zeta^{1+(v-u)\cdot\xi}.
\]
Using \(u\cdot u=1\), \(u\cdot v=0\), \(v\cdot v=a^2=-2\), and \((v-u)\cdot(v-u)=-1\) in \(\mathbb F_p\), its values at \(0,u,v,v-u\) are respectively
\[
1-1+\zeta-\zeta,\quad
1-\zeta+\zeta-1,\quad
1-1+\zeta^{-1}-\zeta^{-1},\quad
1-\zeta^{-1}+\zeta^{-1}-1.
\]
All are zero. Hence \(\operatorname{supp}f\cap\operatorname{supp}\widehat f=\varnothing\) and \(\sigma_p\le4\).

**Step 2: no one- or two-point support for \(p\equiv3\pmod4\).** When \(p\equiv3\pmod4\), the quadratic form
\[
Q(w)=w_1^2+w_2^2
\]
is anisotropic: \(Q(w)=0\) implies \(w=0\), because \(-1\) is not a square modulo \(p\). A signal with support \(S\) and Fourier transform vanishing at all points of \(S\) supplies a nonzero kernel vector for the principal Fourier matrix indexed by \(S\). Every one-by-one principal matrix is nonzero. For \(S=\{x,y\}\), write \(w=y-x\ne0\). Multiplication by invertible row and column characters reduces its determinant, up to a nonzero factor, to
\[
\det\begin{pmatrix}1&1\\1&\zeta^{Q(w)}\end{pmatrix}=\zeta^{Q(w)}-1\ne0.
\]
Thus two-point supports are also impossible.

**Step 3: no three-point support for \(p\equiv3\pmod4\).** By translating and rescaling rows and columns, any three-point principal Fourier minor has the same singularity as the matrix associated with \(S=\{0,u,v\}\), where \(u,v\ne0\) and \(u\ne v\). Put
\[
A\equiv Q(u),\quad B\equiv Q(v),\quad C\equiv u\cdot v\pmod p,
\]
using representatives \(A,B\in\{1,\ldots,p-1\}\) and \(C\in\{0,\ldots,p-1\}\). Anisotropy ensures \(A,B\ne0\). The determinant equals
\[
D=(\zeta^A-1)(\zeta^B-1)-(\zeta^C-1)^2.
\]
If \(C=0\), both factors in the first product are nonzero, so \(D\ne0\). If \(C\ne0\) and \(D=0\), the identity
\[
\zeta^j-1=2i\exp(\pi i j/p)\sin(\pi j/p)
\]
for \(1\le j<p\) yields
\[
\exp\!\left(\frac{\pi i(A+B-2C)}p\right)
=\frac{\sin^2(\pi C/p)}{\sin(\pi A/p)\sin(\pi B/p)}.
\]
The right side is strictly positive and the left side has modulus one, so both equal one. Because \(|A+B-2C|<2p\), this forces \(A+B=2C\) as ordinary integers. Consequently \(\sin(\pi C/p)=\sin(\pi(A+B)/(2p))\), and the identity
\[
\sin\frac{\pi A}p\sin\frac{\pi B}p=
\sin^2\frac{\pi(A+B)}{2p}-\sin^2\frac{\pi(A-B)}{2p}
\]
forces \(\sin(\pi(A-B)/(2p))=0\). Since \(|A-B|<p\), we get \(A=B\) and then \(C=A=B\). Therefore
\[
Q(u-v)=Q(u)+Q(v)-2u\cdot v=A+B-2C=0\pmod p.
\]
Anisotropy forces \(u=v\), contradicting distinctness. Thus \(D\ne0\), and no three-point support works.

Steps 1–3 prove \(\sigma_p=4\) for all primes \(p\equiv3\pmod8\).

## Verification
`artifacts/verify.py` is a dependency-free, deterministic exact-arithmetic corroboration. For every prime \(p\equiv3\pmod8\) below \(800\), it verifies the two roots of \(a^2=-2\), the distinct four-point support, and the four Fourier cancellations in the integral group ring, without floating-point tolerances. For \(p\in\{3,11,19\}\) it exhausts all normalized two- and three-point principal minors, using the exact cyclotomic relation \(1+\zeta+\cdots+\zeta^{p-1}=0\). The successful replay reports \(37\) witness primes, \(488\) nonzero two-point determinants, and \(143576\) nonzero three-point determinants.

The infinite theorem is proved by the algebraic and trigonometric argument above; the finite program is not an infinite proof.

## Relationship to prior work
W. Zhou, *On number of cyclic \(n\)-roots and disjointness of Fourier supports* (arXiv:2608.06335, Proposition 3), shows the existence of self-disjoint Fourier supports on \(\mathbb F_p^2\). In the case \(p\equiv3\pmod4\), the paper explicitly leaves the minimal support size undetermined and gives a construction with support \(2p-2\). The present theorem determines the exact minimum for the infinite subclass \(p\equiv3\pmod8\), reducing that bound to \(4\) for every \(p\ge11\) in the subclass.

Delvaux and Van Barel describe rank-deficient submatrices of Kronecker Fourier matrices and Hamming-number uncertainty bounds, but their theorems concern unconstrained placements of row and column sets and do not determine the smallest *principal* rank defect in this congruence class. Earlier principal-minor criteria for cyclic Fourier matrices concern \(\mathbb Z_N\), not the noncyclic group \(\mathbb F_p^2\). Published exact three-sparse Fourier-support spectra on elementary Abelian groups classify transform-support cardinalities, rather than the coincidence condition that the transform vanish at each time-support point.

## Limitations
The theorem uses the standard coordinate identification of \(G\) with its dual. It does not determine the corresponding minimum for primes \(p\equiv7\pmod8\), does not classify all minimal supports or coefficients, and does not claim the analogous minimum for arbitrary symmetric bilinear pairings. The finite checks are supplementary and independent external validation has not occurred.

## References
1. W. Zhou, *On number of cyclic \(n\)-roots and disjointness of Fourier supports*, arXiv:2608.06335, first posted 2026-08-06, Proposition 3; https://arxiv.org/abs/2608.06335 .
2. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Kronecker products of Fourier matrices*, KU Leuven technical report TW477 (2006), subsequently Linear Algebra and its Applications 426 (2007), 349–367; https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW477.pdf .
3. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793, first posted 2024-09-15; https://arxiv.org/abs/2409.09793 .
4. W. Zhou, *Principal non-singularity of Fourier matrices on \(\mathbb Z_p\times\mathbb Z_q\) and \(\mathbb Z_2^k\times\mathbb Z_q\)*, arXiv:2505.01189, first posted 2025-05-02; https://arxiv.org/abs/2505.01189 .
