# Sharp subunit \(p\)-Bures quasi-triangle constant for pure-state projections

## Finding
Let \(H\) be any complex Hilbert space with \(\dim H\ge 2\), and let \(\mathcal P_1(H)\) denote its rank-one orthogonal projections. For \(p>0\), define on this set the restriction of the \(p\)-Bures expression
\[
D_p(P,Q)=\left(\operatorname{tr}P^p+\operatorname{tr}Q^p-2\|P^{1/2}Q^{1/2}\|_p^p\right)^{1/2}.
\]
For every \(0<p\le 2/3\), the **smallest possible** constant \(K\) such that
\[
D_p(P,R)\le K\bigl(D_p(P,Q)+D_p(Q,R)\bigr)
\]
for all \(P,Q,R\in\mathcal P_1(H)\) is
\[
\boxed{K_p=\frac{1}{2\sqrt{1-2^{-p/2}}}}.
\]
Equality for three distinct rays occurs precisely when the endpoint rays are orthogonal and the intermediate ray is an equal-angle projective midpoint (angles \(\pi/4\) to both). The sharp constant is dimension-independent and satisfies
\[
K_p\sim\frac{1}{\sqrt{2p\log 2}}\quad(p\downarrow0).
\]
The exponent \(2/3\) is also the **exact convexity threshold** for the pure-state angular profile: within \(0<p<1\), the function \(\theta\mapsto\sqrt{1-\cos^p\theta}\), \(0\le\theta\le\pi/2\), is convex if and only if \(p\le2/3\). No sharp quasi-triangle constant is asserted here for \(2/3<p<1\).

## Assumptions and scope
The trace and Schatten expression are evaluated on rank-one projections, so they are finite even in infinite-dimensional \(H\). For a unit vector \(u\), write \(P_u x=\langle x,u\rangle u\) with the inner-product convention chosen consistently. If \(P=P_u\) and \(Q=P_v\), the sole nonzero singular value of \(P_uP_v\) is \(|\langle u,v\rangle|\); hence
\[
D_p(P_u,P_v)=\sqrt{2}\,F_p\bigl(\vartheta(u,v)\bigr),\qquad
F_p(t)=\sqrt{1-\cos^p t},\quad
\vartheta(u,v)=\arccos|\langle u,v\rangle|\in[0,\pi/2].
\]
The Fubini–Study angle \(\vartheta\) is a metric on projective Hilbert space. The formula is an assertion about the **rank-one projector subspace only**, not arbitrary positive operators.

## Proof
**1. The angular convexity boundary.** Put \(r=\cos t\) and \(g_p(t)=1-r^p\). Differentiating \(F_p=\sqrt{g_p}\) gives
\[
F_p''(t)=\frac{p r^{p-2}}{4(1-r^p)^{3/2}}\,B_p(r),\quad
B_p(r)=2(1-p)+2pr^2-r^p\bigl((2-p)+pr^2\bigr)
\]
for \(0<t<\pi/2\). At \(p=2/3\), set \(z=r^{2/3}\); then
\[
B_{2/3}(r)=\frac23(1-z)^3(1+z)>0\quad(0<r<1).
\]
Thus \(F_{2/3}\) is strictly increasing and strictly convex.

For \(0<s\le1\), let \(h_s(x)=\sqrt{1-(1-x^2)^s}\) on \([0,1]\). The exact identity
\[
h_s(x)=\sqrt{s}\left(\int_0^1\bigl[x(1-tx^2)^{-(1-s)/2}\bigr]^2\,dt\right)^{1/2}
\]
shows that \(h_s\) is convex: for each \(0\le t<1\), the integrand's positive square-root factor \(x(1-tx^2)^{-(1-s)/2}\) is increasing and convex (its power series in \(x\) has nonnegative coefficients), and the \(L^2[0,1]\) norm preserves convexity of this nonnegative pointwise-convex family by monotonicity and Minkowski. The endpoint follows by continuity. Moreover, \(h_s\) is increasing. Since
\[
F_p(t)=h_{3p/2}\bigl(F_{2/3}(t)\bigr),\qquad 0<p\le2/3,
\]
composition proves strict convexity for the entire claimed range. Conversely, Taylor expansion gives
\[
F_p(t)=\sqrt{p/2}\,t\left(1+\frac{2-3p}{24}t^2+O(t^4)\right),\quad t\downarrow0.
\]
For \(2/3<p<1\), the first nonzero curvature near zero is negative, excluding convexity. This proves the exact threshold within \(0<p<1\).

**2. A monotone halving ratio.** For \(0<s\le\pi/2\), set \(r=\cos(s/2)\in[1/\sqrt2,1)\). Then
\[
\left(\frac{F_p(s)}{F_p(s/2)}\right)^2
=\frac{1-(2r^2-1)^p}{1-r^p}.
\]
Let the numerator and denominator be \(A(r)\) and \(B(r)\). Both vanish at \(r=1\). Their derivative ratio is
\[
\frac{A'(r)}{B'(r)}=4r^{2-p}(2r^2-1)^{p-1}.
\]
Its logarithmic derivative has the sign of
\[
2pr^2-(2-p)<0\quad\text{for}\quad 0<p\le2/3,\quad 1/\sqrt2<r<1.
\]
Therefore \(A'/B'\) strictly decreases with \(r\). Since \(A(r)/B(r)\) is its average over \([r,1]\) with the positive weight \(-B'(r)\), the ratio \(A/B\) strictly decreases with \(r\). Equivalently, \(F_p(s)/(2F_p(s/2))\) strictly increases with \(s\) and attains its maximum at \(s=\pi/2\), where it equals \(K_p\).

**3. The global three-projector inequality.** Let \(x=\vartheta(P,Q)\), \(y=\vartheta(Q,R)\), and \(z=\vartheta(P,R)\). If \(x+y\le\pi/2\), the projective-angle triangle inequality and monotonicity give
\[
F_p(z)\le F_p(x+y)\le K_p\bigl(F_p(x)+F_p(y)\bigr).
\]
Indeed, strict convexity yields \(F_p(x)+F_p(y)\ge2F_p((x+y)/2)\), and Step 2 bounds the resulting quotient. If \(x+y>\pi/2\), choose \(0\le x'\le x\) and \(0\le y'\le y\) with \(x'+y'=\pi/2\), and use monotonicity to obtain
\[
F_p(z)\le F_p(\pi/2)\le K_p\bigl(F_p(x')+F_p(y')\bigr)
\le K_p\bigl(F_p(x)+F_p(y)\bigr).
\]
Multiplication by \(\sqrt2\) proves the quasi-triangle inequality.

**4. Sharpness, extremizers, and asymptotics.** Take orthonormal vectors \(e_1,e_2\) and the three rays represented by \(e_1\), \((e_1+e_2)/\sqrt2\), and \(e_2\). Their projective angles are respectively \(\pi/4,\pi/4,\pi/2\), and their ratio is exactly \(K_p\). Equality for a nondegenerate triple forces \(x=y\) by strict convexity and \(x+y=\pi/2\) by Step 2, hence the stated geometry. Finally, \(1-2^{-p/2}\sim p\log2/2\) yields the displayed small-exponent law.

## Verification
Run `python3 CHECK.py` alongside this file. The standalone deterministic checker tests angular inequalities, sharp midpoint equality, direct complex-projector triples, and the factorization of the critical curvature numerator. Its finite diagnostics cannot prove the infinite collection of inequalities; Steps 1–4 provide the proof.

## Relationship to prior work
Sra's 2026 \(p\)-Bures–Wasserstein work proves a genuine metric for \(1\le p\le2\); its source does not state a sharp quasi-triangle constant below one. Under rank-one restriction, the parameter \(t\) of Komálovics–Molnár and of Vuong–Osaka is related by \(t=2/p\), up to a harmless overall distance normalization. Komálovics–Molnár establish that metricity fails for \(t>2\); Vuong–Osaka extend the metricity classification to noncommutative cones. Neither statement determines the optimal multiplicative quasi-triangle distortion for \(t\ge3\). Vuong's related quantitative study addresses spectral/local quasi-metric estimates, not the exact, dimension-free rank-one constant here.

## Limitations
The theorem does not determine the sharp constant for \(2/3<p<1\), for general positive semidefinite matrices, or for general trace-class operators. The established convexity threshold is about the auxiliary angular profile, not a claim that quasi-triangle bounds stop beyond that threshold. Source comparison cannot exclude all older equivalent formulations in projective or quantum-state geometry; an independent priority audit remains to be performed.

## References
1. Suvrit Sra, *The \(p\)-Bures–Wasserstein distance via \(3\times3\) block matrices*, arXiv:2610.15889v1, public 2026-10-11; https://arxiv.org/html/2610.15889v1.
2. Ábel Komálovics and Lajos Molnár, *On a parametric family of distance measures that includes the Hellinger and the Bures distances*, J. Math. Anal. Appl. 529 (2024), 127226, online 2023-03-24; https://publicatio.bibl.u-szeged.hu/37355/1/OnaparametricfamilyofdistancemeasuresthatincludestheHellingerandtheBuresdistances_ML.pdf.
3. Trung Dung Vuong and Hiroyuki Osaka, *Three-Point Trace Positivity: Schatten Norm Compression and Interpolating Metrics*, arXiv:2610.11021, public 2026-10-08; https://arxiv.org/pdf/2610.11021.
4. Trung Dung Vuong, *Quantitative geometry of the symmetric \(\alpha\)-\(z\) Bures–Wasserstein divergence*, Filomat (2026), author manuscript publicly posted April 2026; https://www.researchgate.net/publication/403374888_Quantitative_geometry_of_the_symmetric_a-z_Bures-Wasserstein_divergence.
