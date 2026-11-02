# Sharp near-identity Ritt power defects for two-dimensional contractions

## Finding
For a bounded operator \(T\) on complex Euclidean two-space define its power-difference Ritt quantity by
\[
\mathcal D(T)=\sup_{n\ge1}n\,\|T^n(I-T)\|_2.
\]
For \(0<r<1\), let \(\mathcal C_r\) be the collection of all \(2\times2\) complex contractions whose only eigenvalue is \(r\). Then
\[
\boxed{\lim_{r\uparrow1}\ \max_{T\in\mathcal C_r}\mathcal D(T)=\mathfrak R(2)=0.6794006077854641\ldots.}
\]
Here \(y_2=1.395336994467\ldots\) is the unique positive solution of \(y^4-2y-1=0\), and
\[
\mathfrak R(2)=(1+y_2)e^{-1-y_2}\big(\sqrt{1+y_2^2}+y_2\big).
\]
The maximum for each \(r\) is achieved by the Schur-form contraction \(T_r=rI+(1-r^2)N\), where \(N=\begin{psmallmatrix}0&1\\0&0\end{psmallmatrix}\). If \(n_r\) is any maximizing power for this extremal contraction, then
\[
\boxed{\lim_{r\uparrow1}(1-r)n_r=1+y_2=2.395336994467\ldots.}
\]
For comparison, the scalar contraction \(rI\) has limiting Ritt quantity \(e^{-1}\). Thus the extreme permitted nonnormal coupling produces a sharp, substantially larger value.

More generally, for each fixed \(c\ge0\), put \(T_{\varepsilon,c}=(1-\varepsilon)I+c\varepsilon N\) for \(0<\varepsilon<1\). Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\mathcal D(T_{\varepsilon,c})=\mathfrak R(c).}
\]
The complete profile has \(\mathfrak R(0)=e^{-1}\). For \(c>0\), let \(y_c>0\) be the unique solution of
\[
\frac{c}{\sqrt{4+c^2y_c^2}}=\frac{y_c}{1+y_c}.
\]
Then
\[
\mathfrak R(c)=(1+y_c)e^{-1-y_c}\left(\sqrt{1+\frac{c^2y_c^2}{4}}+\frac{cy_c}{2}\right),
\qquad
\lim_{\varepsilon\downarrow0}\varepsilon n_{\varepsilon,c}=1+y_c
\]
for any maximizing integers \(n_{\varepsilon,c}\). The function \(\mathfrak R\) is strictly increasing on \([0,\infty)\) and has the asymptotic descriptions
\[
\mathfrak R(c)=e^{-1}\left(1+\frac{c^2}{8}+\frac{c^3}{24}+O(c^4)\right)\quad(c\downarrow0),
\qquad
\lim_{c\to\infty}\frac{\mathfrak R(c)}c=\varphi^3 e^{-\varphi^2},
\]
where \(\varphi=(1+\sqrt5)/2\).

## Assumptions and scope
All operator norms are the standard complex Euclidean induced (largest-singular-value) norm. The contraction class consists of matrices \(T\) with \(\|T\|_2\le1\), repeated real eigenvalue \(r\in(0,1)\), and no restriction on diagonalizability. Powers are positive integers. The quantity studied is the *power-difference Ritt quantity* \(\mathcal D(T)\), not the distinct resolvent-based Ritt constant.

## Proof
**1. Schur normal form and the exact contraction boundary.** By unitary Schur triangularization and phase conjugation, every matrix in \(\mathcal C_r\) is unitarily equivalent to \(T=rI+aN\), with \(a\ge0\) and \(N^2=0\). The determinant of \(I-T^*T\) is \((1-r^2)^2-a^2\). Since its first diagonal entry is \(1-r^2>0\), positivity of \(I-T^*T\) is equivalent to \(0\le a\le1-r^2\). Therefore the entire contraction class is parametrized by a single bounded off-diagonal magnitude.

**2. Exact power difference.** With \(\varepsilon=1-r\), \(a=c\varepsilon\), and \(x=n\varepsilon\), the nilpotent binomial identity gives
\[
 nT^n(I-T)=n\varepsilon r^n\left[I+c\left(\frac{x}{r}-1\right)N\right].
\]
The largest singular value of \(I+uN\) is exactly
\[
 h(|u|):=\sqrt{1+|u|^2/4}+|u|/2.
\]
Thus
\[
\boxed{n\|T^n(I-T)\|_2=xr^n h\left(c\left|\frac xr-1\right|\right).}
\]
For each fixed \(r\), this expression is nondecreasing in \(a\), so the supremum over contractions is achieved by \(a=1-r^2\), equivalently \(c=1+r=2-\varepsilon\).

**3. Uniform passage from discrete to continuous time.** For \(\varepsilon\le1/2\), \(r^n\le e^{-n\varepsilon}=e^{-x}\) and \(h(u)\le1+u\) for \(u\ge0\). Uniformly for \(0\le c\le C\),
\[
 n\|T_{\varepsilon,c}^n(I-T_{\varepsilon,c})\|_2
 \le xe^{-x}\,[1+C(2x+1)].
\]
This is uniformly small for sufficiently large \(x\). On each compact interval in \(x\), the exact expression converges uniformly for \(c\in[0,C]\) to
\[
 F_c(x)=xe^{-x}\,h(c|x-1|).
\]
The mesh \(x=n\varepsilon\) becomes dense. Hence \(\mathcal D(T_{\varepsilon,c})\to\max_{x\ge0}F_c(x)\), uniformly on compact sets of coupling values. The same tightness and compact uniform convergence imply that rescaled maximizing integers converge to the unique maximizer of \(F_c\) whenever it is unique.

**4. Unique nonnormal maximum.** For \(0<x<1\), writing \(y=1-x\), the corresponding point \(x'=1+y\) has the same shear norm and strictly larger scalar factor because \(\log\frac{1+y}{1-y}>2y\) for \(0<y<1\). Thus no maximum occurs below one. At \(c>0\), the right derivative at \(x=1\) is positive. On \(x=1+y>1\), differentiation gives
\[
\frac{d}{dy}\log F_c(1+y)
= -\frac{y}{1+y}+\frac{c}{\sqrt{4+c^2y^2}}.
\]
The first term decreases strictly from zero, while the positive second term decreases strictly to zero; equivalently, \(y/(1+y)\) rises strictly from zero to one whereas \(c/\sqrt{4+c^2y^2}\) falls to zero. Therefore there is exactly one critical point \(y_c>0\), it is the unique global maximum, and it obeys the displayed equation. For \(c=0\), the unique maximum of \(xe^{-x}\) is \(x=1\).

**5. Contractive sharp constant and maximizing times.** As \(c\) increases, \(h(cy)\) increases strictly for each \(y>0\), and the maximizing \(y_c\) is strictly positive. Thus \(\mathfrak R(c)\) increases strictly. Since the exact finite-\(r\) maximizing contraction has \(c=2-\varepsilon\), Step 3 gives the stated sharp limit \(\mathfrak R(2)\). At \(c=2\) the unique maximizing equation simplifies, after squaring positive quantities, to \(y^4-2y-1=0\); this polynomial is strictly increasing after its unique positive minimum and crosses zero exactly once on \((0,\infty)\). The uniqueness from Step 4 also proves this root characterization. Tightness and uniqueness yield the power-location limit.

**6. Parameter endpoints.** Expanding the uniquely determined stationary equation at zero gives \(y_c=c/2+c^2/4+c^3/8+O(c^4)\), which inserted into the exact profile yields the small-coupling expansion. Dividing the stationary equation by \(c\), and using its monotonicity, shows \(y_c\uparrow\varphi\), the positive root of \(y^2-y-1=0\). Since \(h(cy_c)/(c)\to\varphi\) and \(1+\varphi=\varphi^2\), the strong-coupling slope is \(\varphi^3 e^{-\varphi^2}\).

## Verification
The accompanying standalone `check_ritt.py` uses only the Python standard library. It compares the exact matrix product against the shear-norm expression across multiple couplings, spectral gaps and power indices; numerically checks the stationary condition, the global envelope on a fine bounded grid, the contractive boundary value, and endpoint asymptotics. It reports `CHECK_OK 154820 finite assertions`. These numerical experiments are not substitutes for the analytic supremum, uniqueness and limiting arguments above.

## Relationship to prior work
General characterizations of Ritt operators in terms of power differences and resolvent conditions are established operator theory. Borichev, Gomilko and Tomilov study new global Beurling–Kato criteria and Hardy–Sobolev calculi; Arnold analyzes rates of \(\|T^n(I-T)^k\|\); Badea studies displacement bounds and associated resolvent constants. The result here is a different exact, near-unit asymptotic optimization: the sharp value of \(\sup_n n\|T^n(I-T)\|\) among repeated-eigenvalue two-dimensional contractions, with its complete coupling and maximizing-time profile. Standard Jordan power formulas are used as elementary inputs; they do not, by themselves, specify the constrained global Ritt-envelope or its time localization.

## Limitations
No general-dimensional or arbitrary-spectrum universal Ritt constant is claimed. The eigenvalue is restricted to a real scalar approaching one and the space has complex Hilbert dimension two. The general profile for \(c>2\) covers matrices not necessarily contractive. Badea's closely timed paper was accessible only by abstract and secondary summaries, not complete primary text; an equivalent specialization there or in older semigroup literature remains a priority risk.

## References
- L. Arnold, *Rates of Decay for (alpha, beta)-Ritt-Kreiss Operators*, arXiv:2606.14323, first version 2026-06-12. Relevant introduction, power-difference estimates, and Section 6 examples inspected in the accessible manuscript text.
- A. Borichev, A. Gomilko, Yu. Tomilov, *Beurling--Kato theory, Hardy--Sobolev calculus and Ritt operators*, arXiv:2607.10507, first version 2026-07-11. Relevant Sections 2 and 6 inspected in the accessible preprint text.
- C. Badea, *Iterates of Ritt operators close to the identity*, arXiv:2609.27458, first version 2026-09-23. Abstract inspected; full manuscript inaccessible in this review.
