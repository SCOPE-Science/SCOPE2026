# An exact zero-entry staircase for jet-penalized Bergman kernels

## Finding
Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), let \(m\ge1\) be any integer, and let \(0\le\tau<\infty\). Equip the analytic Bergman space with
\[
\|f\|_{m,\tau}^{2}=\frac1\pi\int_{\mathbb D}|f(z)|^2\,dA(z)+\tau|f^{(m)}(0)|^2.
\]
For \(t=z\overline w\), its reproducing kernel is
\[
K_{m,\tau}(z,w)=\frac1{(1-t)^2}-q t^m,\qquad
q=\frac{\tau(m+1)^2(m!)^2}{1+\tau(m+1)(m!)^2},\qquad 0\le q<m+1.
\]
The complete number of distinct kernel-zero products \(t\in\mathbb D\), with multiplicities, is
\[
\boxed{N_m(q)=\#\left\{0\le j\le m:\;
q>\frac1{4\sin^2\!\left(\frac{(2j+1)\pi}{2(m+1)}\right)}\right\}.}
\]
All such interior zeros are simple for every finite penalty. The strict inequality is essential: equality places corresponding roots on \(|t|=1\), which is not attainable by two interior disk points.

The kernel is zero-free for all pairs of interior points if and only if
\[
q\le q_m^\mathrm{first}=\begin{cases}
\frac14,&m\text{ even},\\[2pt]
\bigl[4\cos^2(\pi/(2(m+1)))\bigr]^{-1},&m\text{ odd}.
\end{cases}
\]
A threshold \(Q<m+1\) corresponds exactly to the physical penalty
\[
\tau_Q=\frac{Q}{(m+1)(m!)^2((m+1)-Q)}.
\]
The formula counts repeated threshold values separately, as required for conjugate pairs. Some formal thresholds \(Q\ge m+1\) are unreachable at finite \(\tau\); the census automatically excludes them. For example, the first transitions occur at \(\tau=1/6\) when \(m=1\) and \(\tau=1/132\) when \(m=2\).

## Assumptions and scope
The domain is the open complex unit disk with normalized area measure \(dA/\pi\). The Hilbert space consists of all analytic square-integrable functions, equipped with one positive point-derivative penalty of exact order \(m\) at the origin. The parameter \(\tau\) is real, nonnegative and finite; \(q\in[0,m+1)\) is the equivalent spectral coordinate. A scalar root \(t\in\mathbb D\) corresponds to an actual pair \(z,w\in\mathbb D\) with \(z\overline w=t\); no roots on the unit circle are counted. The zero count refers to distinct scalar products \(t\), not the infinitely many corresponding pairs \((z,w)\).

## Proof
**Kernel computation.** The monomials are orthogonal, since the area form is radial and the derivative term vanishes except in degree \(m\). For \(f(z)=\sum_{k\ge0}a_kz^k\),
\[
\|f\|_{m,\tau}^2=\sum_{k\ne m}\frac{|a_k|^2}{k+1}
+\left[\frac1{m+1}+\tau(m!)^2\right]|a_m|^2.
\]
Reciprocating these diagonal squared norms yields the displayed kernel and the stated formula for \(q\). In particular \(q\in[0,m+1)\).

**Boundary crossings.** Multiplication by \((1-t)^2\), which is nowhere zero in the disk, reduces the zero question to the degree-\((m+2)\) polynomial
\[
P_q(t)=1-qF_m(t),\qquad F_m(t)=t^m(1-t)^2.
\]
For \(0<q<1/4\), the bound \(|F_m(t)|\le4\) on \(|t|\le1\) rules out all roots in the closed disk. On the unit circle \(t=e^{i\theta}\),
\[
F_m(e^{i\theta})=-4\sin^2(\theta/2)e^{i(m+1)\theta}.
\]
Thus for positive \(q\) a boundary root occurs exactly at \(\theta=(2j+1)\pi/(m+1)\), \(j=0,\ldots,m\), and at the listed \(q_{m,j}\). None is \(t=1\), since \(F_m(1)=0\).

**Every crossing is inward.** At a boundary root, logarithmic differentiation gives
\[
\frac{tF'_m(t)}{F_m(t)}=m-\frac{2t}{1-t},
\qquad \Re\frac{tF'_m(t)}{F_m(t)}=m+1>0,
\]
so every boundary root is simple. Along the local root trajectory \(qF_m(t(q))=1\),
\[
\frac{d\log|t(q)|}{d\log q}
=-\Re\left(\frac{1}{tF'_m(t)/F_m(t)}\right)<0
\]
at each crossing. Hence all boundary crossings point strictly into \(\mathbb D\) as \(q\) increases. Roots vary continuously as a multiset, and the argument principle makes their number constant away from these finitely many parameters; starting at zero roots for \(q<1/4\) and summing the inward crossings proves the exact counting formula, including coincident crossings.

**No multiple physical zeros.** A multiple root of \(P_q\) for \(q>0\) requires \(F'_m(t)=0\), hence \(t=m/(m+2)\), since \(t=0\) never solves \(P_q=0\). The corresponding exceptional parameter is
\[
q_*=\frac{(m+2)^{m+2}}{4m^m}>
\frac{(m+2)^2}{4}>m+1,
\]
for every integer \(m\ge1\). Thus no multiple root occurs in the permitted range. Every \(t\in\mathbb D\) is realized as \(z\overline w\) with \(|z|=|w|=\sqrt{|t|}<1\), so the scalar census is exactly the kernel-zero census.

**First threshold.** The largest among \(\sin^2((2j+1)\pi/(2(m+1)))\) equals \(1\) if \(m\) is even and equals \(\cos^2(\pi/(2(m+1)))\) if \(m\) is odd. Taking its reciprocal times \(1/4\) proves the displayed sharp zero-free boundary. Finally, solving the expression for \(q\) for \(\tau\) proves the physical threshold formula.

## Verification
The identities for the monomial norm, numerator, boundary phase, logarithmic crossing direction, and discriminant exceptional parameter are exact. A supplementary independent numerical root census was performed for integer orders \(1\le m\le14\) and admissible noncritical sample strengths, using polynomial companion roots; all computed counts matched the formula. Numerical roots are not invoked to prove the infinite-order statement. A standalone reproducibility checker `check.py` illustrates the polynomial coefficients, threshold count, and finite sample tests; the analytic argument above is the proof.

## Relationship to prior work
Zeytuncu (2010, arXiv:1009.2806), Section 2, studies zeros of kernels arising from radial changes in an area weight. The present norm instead adds a discrete derivative penalty at one interior point and changes exactly one monomial norm; the former construction does not imply this all-order crossing classification. Marcellán and Xu (2014, arXiv:1403.6249), Sections 7 and 9, survey Sobolev inner products with point-derivative terms and zeros of the resulting *finite-degree orthogonal polynomials*, not zeros of the full analytic-disk reproducing kernel.

Other nearby work on Gram kernels of derivative evaluation forms concerns different RKHS kernels. In particular, a pure-jet evaluation Gram kernel with a Jacobi-polynomial numerator cannot be substituted for the positive-definite inverse-norm kernel computed here. The classical Bergman kernel and rank-one coefficient identity are standard tools; the additional result is the complete all-order zero-entry phase classification with exact boundary multiplicities and physical penalty restrictions.

## Limitations
The theorem covers one pure derivative penalty at the center of the unit disk. It does not address several simultaneous jet orders, off-center penalties, negative or complex penalties, weighted disk Bergman backgrounds, or domain deformation. The result is a mathematical derivation with supplementary finite checks, not an independent external audit. An undiscovered equivalent presentation in the large literature on Sobolev-type analytic spaces remains a research-priority risk.

## References
1. Y. E. Zeytuncu, *Weighted Bergman Projections and Kernels: Lp Regularity and Zeros*, arXiv:1009.2806v1 (first public 2010-09-14), especially Section 2. https://arxiv.org/abs/1009.2806
2. F. Marcellán and Y. Xu, *On Sobolev Orthogonal Polynomials*, arXiv:1403.6249v1 (first public 2014-03-25), especially Sections 7 and 9. https://arxiv.org/abs/1403.6249
3. H. P. Boas, *Lu Qi-Keng's Problem*, arXiv:math/0001036 (2000), for the general problem of kernel zeros. https://arxiv.org/abs/math/0001036
