# Exact two-spectral-point Cartesian radius and its cubic-to-linear angular transition

## Finding

Let \(T\) be a bounded normal operator on a nonzero complex Hilbert space. Audeh, Moradi and Sahoo's \(L^2\)-Cartesian numerical radius is
\[
\omega_2(T)^2=\frac{1}{2\pi}\int_0^{2\pi}\left\|\operatorname{Re}(e^{-i\theta}T)\right\|^2\,d\theta.
\]
For any spectral points \(\lambda,\mu\in\sigma(T)\), define
\[
a=|\lambda|^2,\quad b=|\mu|^2,\quad
h=\frac{|a-b|}{2},\quad c=|\operatorname{Im}(\overline\lambda\mu)|,
\]
and the continuous correction function
\[
\mathcal D_h(c)=
\begin{cases}
c-h\arctan(c/h),&h>0,\\
c,&h=0.
\end{cases}
\]
Then the **sharp spectral-pair certificate** is
\[
\boxed{\omega_2(T)^2\ge
\frac{\max\{a,b\}}{2}+\frac{\mathcal D_h(c)}{\pi}.}
\tag{1}
\]
For the normal operator \(T=\operatorname{diag}(\lambda,\mu)\), equality always holds, with no restriction on its two spectral moduli or phases. Thus (1) exactly determines the new radius for every normal operator with at most two distinct spectral points, including those with infinite-dimensional eigenspaces.

For fixed nonzero spectral moduli \(|\lambda|=R\ge r=|\mu|>0\), the exact squared radius is strictly increasing with \(|\sin(\arg\mu-\arg\lambda)|\). The least value \(R^2/2\) occurs precisely for collinear spectral points; the greatest is attained precisely for perpendicular spectral points and equals
\[
\boxed{\frac{R^2}{2}+\frac1\pi\left[Rr-
\frac{R^2-r^2}{2}\arctan\left(\frac{2Rr}{R^2-r^2}\right)\right]}
\tag{2}
\]
when \(R>r\); its continuous \(R=r\) value is \(R^2(1/2+1/\pi)\).

Most importantly, take \(T_\phi=\operatorname{diag}(R,re^{i\phi})\) with \(R>r>0\) fixed. As the spectral rays become collinear,
\[
\boxed{\omega_2(T_\phi)^2-\frac{R^2}{2}
=\frac{4R^3r^3}{3\pi(R^2-r^2)^2}\,|\phi|^3+O_{R,r}(|\phi|^5).}
\tag{3}
\]
In contrast, on the equal-modulus boundary \(R=r>0\), the **exact** deficit is
\[
\boxed{\omega_2(T_\phi)^2-\frac{R^2}{2}
=\frac{R^2}{\pi}|\sin\phi|,}
\tag{4}
\]
which grows linearly near alignment. The change from cubic to linear is a sharp radial-degeneracy transition for the first nontrivial normal spectral class.

## Assumptions and scope

The spectral theorem is used for complex normal bounded operators. The eigenvalues of the displayed diagonal operator may be repeated in an arbitrary nonzero multiplicity; only the spectrum matters. The two-point certificate applies to *any* two spectral points of an arbitrary normal operator (whether or not they are eigenvalues). Formulae (2)--(4) concern normal operators whose entire spectra consist of the two displayed points. The asymptotic (3) holds with \(R>r>0\) fixed and \(\phi\to0\) through real values. The maximum condition refers to angle modulo \(\pi\). When \(R=r\), the formula in (2) is interpreted by continuity. If one spectral point is zero, the correction vanishes and \(\omega_2(T)^2=R^2/2\) in the exactly two-spectral-point setting.

## Proof

**Spectral reduction.** For a normal \(T\), continuous functional calculus gives
\[
\left\|\operatorname{Re}(e^{-i\theta}T)\right\|
=\max_{z\in\sigma(T)}|\operatorname{Re}(e^{-i\theta}z)|.
\]
For any two \(\lambda,\mu\in\sigma(T)\), the squared integrand is therefore at least
\[
\max\{\operatorname{Re}(e^{-i\theta}\lambda)^2,
\operatorname{Re}(e^{-i\theta}\mu)^2\}.
\]
Equality holds pointwise when the spectrum consists only of \(\lambda,\mu\).

**Exact angular integration.** Regard \(\lambda,\mu\) as vectors \(v,w\in\mathbb R^2\), and put \(e_\theta=(\cos\theta,\sin\theta)\). Let \(D=vv^{\mathsf T}-ww^{\mathsf T}\). The scalar identity
\[
\max\{x,y\}=\tfrac12(x+y+|x-y|)
\]
with \(x=(v\cdot e_\theta)^2\), \(y=(w\cdot e_\theta)^2\) shows that the desired average is
\[
I=\frac{a+b}{4}+\frac12\frac1{2\pi}\int_0^{2\pi}
|e_\theta^{\mathsf T}De_\theta|\,d\theta.
\]
Since \(\operatorname{tr}D=a-b\) and \(\det D=-c^2\), some angle \(\alpha\) satisfies
\[
e_\theta^{\mathsf T}De_\theta=t+s\cos(2\theta-\alpha),\quad
t=\frac{a-b}{2},\quad s=\sqrt{t^2+c^2}.
\]
For \(s\ge |t|\), direct integration, splitting at the two zeros, yields
\[
\frac1{2\pi}\int_0^{2\pi}|t+s\cos u|\,du
=\frac2\pi\left[\sqrt{s^2-t^2}+t\arcsin(t/s)\right],
\]
with the right side interpreted continuously when \(s=0\). Therefore
\[
I=\frac{a+b}{4}+\frac1\pi\left[c+t\arcsin(t/s)\right].
\]
Writing \(h=|t|\), for \(h>0\) we have
\[
t\arcsin(t/s)=h\left[\frac\pi2-\arctan(c/h)\right],
\]
including \(c=0\). Since \((a+b)/4+h/2=\max(a,b)/2\), we obtain
\[
I=\frac{\max(a,b)}2+\frac{c-h\arctan(c/h)}\pi.
\]
The case \(h=0\) follows from the displayed integral (or its limit). This proves (1) and its exactness assertion.

**Angular optimization.** At fixed \(R,r>0\), \(h\) is fixed and \(c=Rr|\sin\phi|\in[0,Rr]\). For \(h>0\),
\[
\frac{d}{dc}\mathcal D_h(c)
=1-\frac{h^2}{h^2+c^2}=\frac{c^2}{h^2+c^2};
\]
for \(h=0\) the derivative is one. Therefore \(\mathcal D_h\) is strictly increasing on nonnegative arguments, with unique minimum at collinearity and maximum at perpendicularity. Evaluating at \(c=Rr\) gives (2).

**Critical angular asymptotics.** When \(h=(R^2-r^2)/2>0\), Taylor's theorem gives
\[
\mathcal D_h(c)
=c-h\arctan(c/h)=\frac{c^3}{3h^2}+O_h(c^5).
\]
Because \(c=Rr|\sin\phi|=Rr|\phi|+O_{R,r}(|\phi|^3)\), the coefficient in (3) follows. If \(R=r\), then \(h=0\), so \(\mathcal D_0(c)=c\), proving (4). The coefficients are positive, so both asymptotic exponents are exact. \(\square\)

## Verification

All infinite-dimensional assertions follow from the spectral theorem and the elementary scalar integral proved above; no finite search is treated as a proof. The standalone, dependency-free `verify_pair.py` checks 12 deterministic complex spectral pairs against a 32768-node midpoint quadrature, three strict angular-monotonicity chains, and six cubic-asymptotic ratios for two small angles and three radii. Every test passed. Its role is to detect transcription or branch mistakes, not certify the infinite-dimensional spectral reduction.

## Relationship to prior work

Audeh--Moradi--Sahoo [1, Theorems 4 and 17] introduced the angular squared-mean radius and gave sharp universal bounds, including the commuting-Cartesian-parts (normal) case. Their inspected full text does not evaluate the unequal-modulus, nonorthogonal two-spectral-point problem or its angular transition.

A published unitary spectral-gap theorem [2] exactly determines the equal-modulus subfamily and the optimal finite-dimensional unitary arrangements. A published rank-one overlap theorem [3] treats a different rank-one operator family, covering the diagonal \(\{\lambda,0\}\) boundary. A published cubic operator-norm stability theorem [4] gives a general qualitative cubic exponent and already computes the *orthogonal* unequal-modulus slice \(\{1,i\varepsilon\}\); those statements are **not claimed new** here. None of these inspected results determines the entire two-parameter, unequal-modulus and nonorthogonal spectral-pair formula (1), its phase monotonicity, or the fixed-modulus cubic coefficient in (3). The distinction is one of exact claims and implications, not of paper titles.

## Limitations

The exact formula applies to normal operators with at most two spectral points; the inequality applies to arbitrary normal operators but need not be sharp for a given spectrum with three or more points. It makes no assertion for nonnormal operators. General cubic stability, endpoint equality characterization, unitary finite-spectrum optimization, the orthogonal unequal-modulus example, and rank-one specializations are prior results rather than contributions of this theorem. The two-point angular integration is elementary; the value lies in a full, exact parameter classification of the newly introduced invariant and its radial-degeneracy behavior. Earlier convex-geometric angular averages could hide an equivalent integral under different terminology; priority remains open to specialist review.

## References

1. W. Audeh, H. R. Moradi and S. Sahoo, *The \(L^2\)-Cartesian Numerical Radius of Hilbert Space Operators*, arXiv:2610.04844v1, first available 2026-10-04, https://arxiv.org/html/2610.04844v1 .
2. *Exact projective spectral-gap formula and optimal finite spectra for the \(L^2\)-Cartesian radius of unitaries*, published mathematical record f6644dc86b39, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-projective-spectral-gap-formula-and-optimal-finite-spectra--f6644dc86b39 .
3. *Exact rank-one overlap profile for the \(L^2\)-Cartesian numerical radius*, published mathematical record 846b702b24b7, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-rank-one-overlap-profile-for-the-l-2-cartesian-numerical-r--846b702b24b7 .
4. *Cubic operator-norm stability for the \(L^2\)-Cartesian numerical radius*, published mathematical record ffd07fee0727, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-cubic-operator-norm-stability-for-the-l-2-cartesian-numerical-ra--ffd07fee0727 .
