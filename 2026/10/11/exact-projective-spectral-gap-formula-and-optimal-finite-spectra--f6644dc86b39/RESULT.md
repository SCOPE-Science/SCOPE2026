# Exact projective spectral-gap formula and optimal finite spectra for the \(L^2\)-Cartesian radius of unitaries

## Finding

**Theorem.** Let \(\mathcal H\ne\{0\}\) be any complex Hilbert space and \(U\) a unitary operator on \(\mathcal H\). Define its Cartesian parts and the angular quadratic numerical radius by
\[
H=\tfrac12(U+U^*),\qquad K=\tfrac1{2i}(U-U^*),\qquad
\omega_2(U)^2=\frac1{2\pi}\int_0^{2\pi}\|\cos(t)H+\sin(t)K\|^2\,dt.
\]
Take the antipodal image \(S\) of \(\sigma(U)\) on the projective circle \(\mathbb R/\pi\mathbb Z\). Write \((\ell_j)_{j\in J}\) for the lengths of all connected complementary open arcs of \(S\); there are at most countably many, and the empty list is allowed. Then
\[
\boxed{\omega_2(U)^2=1-\frac{1}{2\pi}\sum_{j\in J}(\ell_j-\sin\ell_j).} \tag{1}
\]
In particular, \(\tfrac12\le\omega_2(U)^2\le1\); equality on the left holds exactly when \(U^2\) is scalar, and equality on the right holds exactly when \(\sigma(U)\cup[-\sigma(U)]\) is the unit circle.

If the projective spectrum consists of exactly \(q\ge1\) distinct points, then
\[
\boxed{\omega_2(U)^2\le\tfrac12+\frac{q}{2\pi}\sin\frac\pi q,} \tag{2}
\]
with equality if and only if the \(q\) points are equally spaced on the projective circle. Consequently, for each integer \(n\ge1\), every \(n\)-dimensional unitary matrix satisfies the optimal inequality
\[
\boxed{\omega_2(U)^2\le\tfrac12+\frac{n}{2\pi}\sin\frac\pi n.} \tag{3}
\]
Equality in (3) holds precisely for matrices whose \(n\) eigenvalues project to \(n\) equally spaced distinct projective classes. Equivalently, after a common rotation, their eigenvalue multiset is \(\{\epsilon_k e^{ik\pi/n}:0\le k<n\}\), with arbitrary signs \(\epsilon_k\in\{-1,1\}\). In particular, the extremal squared radius approaches \(1\) as \(1-\pi^2/(12n^2)+O(n^{-4})\).

## Assumptions and scope

All operator norms are usual complex-Hilbert-space operator norms. The spectrum \(\sigma(U)\) is compact and nonempty because \(\mathcal H\ne\{0\}\), and it lies on the unit circle. The projective circle \(\mathbb R/\pi\mathbb Z\) has total arclength \(\pi\). The image \(S\) is nonempty and compact. The open gaps are the connected components of its complement, with lengths in \((0,\pi]\). A singleton \(S\) gives one gap of length \(\pi\); a full projective circle gives no gaps. The complement may be countably infinite or have zero total length. No finite-spectrum or finite-dimensional hypothesis is required for (1). Formulae (2)--(3) count *distinct antipodal spectral classes*, not individual eigenvectors or multiplicities.

## Proof

**Spectral reduction.** The Cartesian identity gives
\[
\cos(t)H+\sin(t)K=\operatorname{Re}(e^{-it}U).
\]
By the continuous functional calculus for the normal operator \(U\), its norm is
\[
\|\operatorname{Re}(e^{-it}U)\|=\max_{\zeta\in\sigma(U)}|\operatorname{Re}(e^{-it}\zeta)|
=\max_{\alpha\in S}|\cos(t-\alpha)|
=\cos d(t,S),
\]
where \(d\) is shortest arclength distance on the projective circle, necessarily in \([0,\pi/2]\). Thus the integrand is \(\pi\)-periodic and
\[
\omega_2(U)^2=\frac1\pi\int_0^\pi\cos^2 d(t,S)\,dt.
\]

**Gap integration, including infinite spectra.** At a point of \(S\) the integrand equals \(1\). On a complementary open gap of length \(\ell\), parametrized by distance \(x\) from one endpoint, the nearest point in \(S\) is one of the two endpoints. This remains true for a gap of full length \(\pi\), whose endpoints coincide as points of the circle. Hence the distance is \(\min\{x,\ell-x\}\). Integrating the deficit over that gap gives exactly
\[
\int_0^\ell\bigl(1-\cos^2\min\{x,\ell-x\}\bigr)\,dx
=2\int_0^{\ell/2}\sin^2x\,dx
=\frac{\ell-\sin\ell}{2}.
\]
The gaps are disjoint, with \(\sum_j\ell_j\le\pi\). Since \(0\le\ell_j-\sin\ell_j\le\ell_j\), the series is absolutely convergent. Countable additivity and the zero deficit on \(S\) prove (1) without any discreteness assumption.

**Endpoint cases.** The upper bound \(1\) is attained if and only if all deficits vanish. Each nonempty gap has \(\ell-\sin\ell>0\), so this is equivalent to no gaps, i.e. \(S\) is the full projective circle. The lower bound follows from \(\sum_j(\ell_j-\sin\ell_j)\le\sum_j\ell_j\le\pi\). Equality at \(\tfrac12\) demands full complementary measure and \(\sin\ell_j=0\) for every gap, hence one gap of length \(\pi\) and \(S\) a singleton. A singleton antipodal image of \(\sigma(U)\) means \(\sigma(U)\subset\{\zeta,-\zeta\}\), which by normal functional calculus is equivalent to \(U^2=\zeta^2I\).

**Finite projective spectra.** If \(S\) comprises \(q\) distinct points, its \(q\) cyclic gaps have lengths \(\ell_1,\ldots,\ell_q>0\) summing to \(\pi\). Expanding (1) gives
\[
\omega_2(U)^2=\frac12+\frac1{2\pi}\sum_{j=1}^q\sin\ell_j.
\]
The sine function is strictly concave on \((0,\pi)\), so Jensen's inequality bounds the last sum by \(q\sin(\pi/q)\). Equality for \(q\ge2\) holds precisely when every \(\ell_j=\pi/q\); the one-point case is immediate. This proves (2).

**Dimension bound and equality.** An \(n\)-dimensional unitary has at most \(n\) projective spectral points. The function \(f(q)=q\sin(\pi/q)\) is strictly increasing for real \(q\ge1\): writing \(x=\pi/q\), its derivative is \(\sin x-x\cos x>0\) for \(0<x\le\pi\) because its derivative as a function of \(x\) is \(x\sin x>0\) and its value at zero is zero. Hence (2) implies (3), with equality exactly for \(q=n\) and equally spaced gaps. The explicit diagonal matrix with entries \(e^{ik\pi/n}\) attains equality. Taylor expansion of \(\sin(\pi/n)\) gives the asserted asymptotic. \(\square\)

## Verification

The spectral-calculus identity, nearest-endpoint geometry, absolute convergence, and Jensen equality conditions provide an analytic proof for all Hilbert spaces and all nonempty compact spectral sets. A standalone reproducibility script, `verify_phase_gaps.py`, numerically evaluates angular midpoint quadrature against the gap formula for a range of equally spaced and nonuniform finite spectra and checks strict improvement under equidistribution. The numerical script is supplementary and is not used in any step establishing the infinite-spectrum identity or sharpness theorem.

## Relationship to prior work

Audeh, Moradi, and Sahoo introduced the \(L^2\)-Cartesian numerical radius, including the defining integral, and proved universal comparison bounds. Their Theorem 17 for commuting Cartesian parts (in particular, normal operators) gives \(\tfrac12\|H^2+K^2\|\le\omega_2(U)^2\le\|H^2+K^2\|\). For a unitary, these reduce to \(\tfrac12\le\omega_2(U)^2\le1\). The new formulas (1)--(3) distinguish arbitrary compact projective spectral configurations, give an exact gap-by-gap invariant, and classify all finite-dimensional maximizers; neither the general integral definition nor the universal bounds are claimed as new. The source's full text, including Theorem 17, was inspected. Earlier operator-radius literature chiefly treats supremum-based angular functionals or bounds and does not by those statements imply this integrated projective-spectrum classification.

## Limitations

This theorem concerns unitary operators, not arbitrary normal contractions, nonnormal operators, or other angular averaging exponents. It classifies maximizers at fixed number of distinct projective spectral points; it does not impose spacing constraints on an arbitrary continuous spectrum. The originality comparison is limited by indexing and access: an equivalent angular-gap formula could occur in historical convex/support-function integral literature under another name. No independent audit has been performed, and no computational test is a substitute for the analytic argument.

## References

1. W. Audeh, H. R. Moradi, and S. Sahoo, *The \(L^2\)-Cartesian Numerical Radius of Hilbert Space Operators*, arXiv:2610.04844v1 (first public version: 2026-10-04), especially Definition and Theorem 17, https://arxiv.org/html/2610.04844v1 .
2. Standard spectral theorem/continuous functional calculus for bounded normal operators; standard concavity of the sine function and Jensen's inequality.
