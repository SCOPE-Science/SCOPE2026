# A sharp weighted two-charge collision cusp for planar Coulomb fields

## Finding

For fixed positive charge strengths \(\alpha,\beta>0\), write \(a_\delta=e^{i\delta}\), \(b_\delta=e^{-i\delta}\), and
\[
I_{\alpha,\beta}(\delta)=\int_{\mathbb D}\left|\frac{\alpha}{z-a_\delta}+\frac{\beta}{z-b_\delta}\right|\,dA(z).
\]
Here \(\mathbb D\) is the open unit disk and \(dA\) is ordinary, **unnormalized** planar Lebesgue area. The energy has the sharp, strictly linear collision law
\[
\boxed{I_{\alpha,\beta}(\delta)=4(\alpha+\beta)-\mathcal C(\alpha,\beta)|\sin\delta|+o(|\sin\delta|)}
\qquad(\delta\to0),
\]
where the finite positive coefficient is the explicit half-plane integral
\[
\boxed{\mathcal C(\alpha,\beta)=\int_{\operatorname{Re}w<0}\left[\frac{\alpha}{|w-i|}+\frac{\beta}{|w+i|}-\left|\frac{\alpha}{w-i}+\frac{\beta}{w+i}\right|\right]dA(w).}
\]
Thus the one-sided drop per unit chordal separation \(|a_\delta-b_\delta|=2|\sin\delta|\) is exactly \(\mathcal C(\alpha,\beta)/2\). In particular, the collision maximum is not differentiable as a function of signed angular displacement. For equal unit weights the coefficient has the exact positive series
\[
\boxed{\mathcal C(1,1)=\pi^2\sum_{m=1}^{\infty}\frac{b_m^2b_{m-1}}{2m-1},\quad b_m=\frac{\binom{2m}{m}}{4^m},\quad b_0=1,}
\]
with numerical value approximately \(2.87108004\). The series is an identity, not a fitted numerical constant.

## Assumptions and scope

The two coefficients are positive real constants. The poles lie on the unit circle, are symmetric about the positive real axis, and approach the common point \(1\). By rotational invariance this is any two-pole collision on the circle. The complex Cauchy field and the real planar Coulomb vector field have identical pointwise magnitudes (up to conjugation and a global sign), so the formula describes both. All normalizations of the area element are explicit: for normalized area \(dA/\pi\), divide the energy and the collision coefficient by \(\pi\). The theorem is a limit statement as \(\delta\to0\), not a finite-separation equality.

## Proof

**1. Exact triangle deficit and the collision scale.** For each \(a\in\partial\mathbb D\), polar coordinates centered at \(a\), with inward radial length between \(0\) and \(2\cos\theta\) for \(|\theta|<\pi/2\), give
\[
\int_{\mathbb D}\frac{dA(z)}{|z-a|}=\int_{-\pi/2}^{\pi/2}2\cos\theta\,d\theta=4.
\]
Define the nonnegative deficit
\[
D(\delta)=4(\alpha+\beta)-I_{\alpha,\beta}(\delta).
\]
For \(0<\delta<\pi/2\), put \(r=\sin\delta\) and \(m=\cos\delta\), and substitute \(z=m+rw\). Then the two poles become \(w=\pm i\), and the scale factors of kernel and area cancel to first order:
\[
D(\delta)=r\int_{\Omega_r}d_{\alpha,\beta}(w)\,dA(w),\quad
\Omega_r=\{w:|m+rw|<1\},
\]
\[
d_{\alpha,\beta}(w)=\frac{\alpha}{|w-i|}+\frac{\beta}{|w+i|}-\left|\frac{\alpha}{w-i}+\frac{\beta}{w+i}\right|.
\]
For each \(w\) outside the imaginary axis, the domain condition is exactly
\[
2m\operatorname{Re}w+r(|w|^2-1)<0.
\]
Hence the indicator \(1_{\Omega_r}(w)\) converges almost everywhere, as \(r\downarrow0\), to \(1_{\{\operatorname{Re}w<0\}}(w)\).

**2. A global integrable dominator.** Let \(U=\alpha/(w-i)\), \(V=\beta/(w+i)\). The elementary inequality
\[
0\le |U|+|V|-|U+V|\le2\min(|U|,|V|)
\]
shows that the deficit remains bounded in neighborhoods of the two poles, since the *other* summand stays bounded. On \(|w|>3\), the angle between \(U\) and \(V\) is \(O(|w|^{-1})\), while their moduli are each \(O(|w|^{-1})\). Rationalizing the triangle deficit,
\[
|U|+|V|-|U+V|=\frac{2\bigl(|U||V|-\operatorname{Re}(U\overline V)\bigr)}{|U|+|V|+|U+V|},
\]
gives \(d_{\alpha,\beta}(w)=O(|w|^{-3})\); the denominator is bounded below by a positive multiple of \(|w|^{-1}\). Thus \(d_{\alpha,\beta}\in L^1(\mathbb C)\). Dominated convergence yields
\[
\lim_{\delta\downarrow0}\frac{D(\delta)}{\sin\delta}
=\int_{\operatorname{Re}w<0}d_{\alpha,\beta}(w)\,dA(w)
=\mathcal C(\alpha,\beta).
\]
Strict positivity holds because the two complex vectors are not collinear in the same direction on a positive-area subset of \(\operatorname{Re}w<0\); for example, around every fixed negative real \(w\) they make distinct nonzero angles. Complex conjugation of the integration variable proves \(I_{\alpha,\beta}(-\delta)=I_{\alpha,\beta}(\delta)\), establishing the two-sided absolute-value cusp.

**3. Exact coefficient by confocal coordinates.** Rotate the half-plane with \(\zeta=-iw\), so \(\operatorname{Im}\zeta>0\) and the focal poles are \(\pm1\). Write
\[
\zeta=\cosh u\cos v+i\sinh u\sin v,
\qquad u>0,\quad0<v<\pi.
\]
Let \(R_{\pm}=|\zeta\mp1|=\cosh u\mp\cos v\). The Jacobian is \(R_+R_-=\sinh^2u+\sin^2v\). Set \(A=\alpha+\beta\) and \(q=(\alpha-\beta)/A\). Multiplication of the triangle deficit by this Jacobian gives the *exact*, nonnegative expression
\[
A\left[\cosh u+q\cos v-\sqrt{(\cosh u+q\cos v)^2-(1-q^2)\sin^2v}\right].
\]
Integration over \(u>0\), \(0<v<\pi\) gives the stated elliptic-coordinate formula for \(\mathcal C\). The bracket is positive in the interior because \(|q|<1\); it is integrable by Step 2 (or by rationalizing it and using exponential decay as \(u\to\infty\)).

**4. Equal-charge central-binomial series.** With \(\alpha=\beta=1\) (hence \(q=0\)), the coefficient becomes
\[
\mathcal C(1,1)=2\int_0^\infty\!\int_0^\pi \cosh u\left[1-\sqrt{1-\frac{\sin^2v}{\cosh^2u}}\right]dv\,du.
\]
For \(0\le t\le1\), the positive series
\[
1-\sqrt{1-t}=\sum_{m=1}^\infty\frac{b_m}{2m-1}t^m,\qquad b_m=\frac{\binom{2m}{m}}{4^m}
\]
allows Tonelli's theorem. The two classical beta integrals are
\[
\int_0^\pi\sin^{2m}v\,dv=\pi b_m,\qquad
\int_0^\infty\cosh^{1-2m}u\,du=\frac\pi2b_{m-1}.
\]
Multiplying the terms gives precisely \(\pi^2\sum_{m\ge1}b_m^2b_{m-1}/(2m-1)\). Since \(b_m=O(m^{-1/2})\), the summand is \(O(m^{-5/2})\), completing convergence. All steps concern ordinary finite integrals and convergent positive series, not a finite-data extrapolation.

## Verification

A standalone Python 3 standard-library checker is provided as `check_collision.py`. It verifies exact rational identities for the central-binomial coefficients and compares convergent-series partial sums against independent confocal-coordinate midpoint quadrature. Its output numerically reproduces \(\mathcal C(1,1)\approx2.87108004\), and checks weight-swap symmetry for two additional positive weight pairs. These computations test the formulae but are not used as evidence for the infinite-limit or literature-comparison conclusions; those rely on the analytic proof and the cited primary texts.

## Relationship to prior work

Doubtsov, Vasilyev, and Voinov (2026) determine optimal **global configuration scales** for positive weighted Coulomb fields on a sphere, with planar case governed by primary MSC 31B05. Doubtsov, Tselishchev, and Vasilyev (2026) give weighted Newman-type estimates and a nearby-pole estimate for a **signed difference** of two Cauchy kernels; that signed estimate does not give the positive-charge triangle deficit. Bezrukov (2026) proves global equispaced-pole minimization, and Nazarov's 2023 argument treats strict monotonicity for the equal-weight two-charge problem; neither inspected presentation supplies the sharp one-sided *collision coefficient* or the positive series above. Corbett (2026) and Abakumov–Borichev–Fedorovskiy (2020) study weighted **Hilbert Bergman norms**, not this \(L^1\) collision cusp. Thus the statement here quantifies a natural boundary degeneration distinct from the global minimization question.

## Limitations

The coefficient is obtained in the limit of two colliding poles; no general multi-pole collision law, finite-angle exact formula, or higher-dimensional analogue is asserted. Positive fixed weights are essential for the strictly positive coefficient. All numerical values are descriptive and are not proof of asymptotics or exhaustive searches. An unindexed equivalent derivation, particularly in older two-charge literature, remains a possible novelty risk. Independent validation has not been performed.

## References

1. E. Doubtsov, I. Vasilyev, G. Voinov, *Sharp weighted L¹ bounds for Coulomb fields on the sphere*, arXiv:2609.35123v1 (first publicly posted 2026-09-28). https://arxiv.org/abs/2609.35123
2. E. Doubtsov, A. Tselishchev, I. Vasilyev, *Weighted Chui's conjecture*, arXiv:2603.05233v1 (2026-03-05). https://arxiv.org/abs/2603.05233
3. E. Bezrukov, *Proof of the generalized Chui conjecture*, arXiv:2609.03134v1 (2026-09-02). https://arxiv.org/abs/2609.03134
4. F. Nazarov (as `fedja`), mathematical answer on the two-charge monotonicity problem, MathOverflow question 451203 (2023-07-25). https://mathoverflow.net/questions/451203/how-to-prove-that-phiz0-for-theta-in-0-pi
5. G. Corbett, *Two new proofs of Chui's Conjecture in Weighted Bergman Spaces*, arXiv:2609.21121v1 (2026-09-17). https://arxiv.org/abs/2609.21121
6. E. Abakumov, A. Borichev, K. Fedorovskiy, *Chui's conjecture in Bergman spaces*, arXiv:2009.01898 (2020). https://arxiv.org/abs/2009.01898
