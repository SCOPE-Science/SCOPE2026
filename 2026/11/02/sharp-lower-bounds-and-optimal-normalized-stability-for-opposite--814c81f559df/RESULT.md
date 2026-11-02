# Sharp lower bounds and optimal normalized stability for opposite Cauchy poles

## Finding

For each real \(a>0\) and \(c>0\), let
\[
g_{a,c}(t)=\frac1{t-ia}+\frac{c}{t+ia},\qquad t\in\mathbb R.
\]
Consider the critical Gabor family \(\{e^{2\pi i m t}g_{a,c}(t-n):m,n\in\mathbb Z\}\) on \(L^2(\mathbb R)\). Its **optimal squared lower frame bound** \(A(a,c)\) (zero when the family is not a frame) is as follows. Set \(p=\pi a\), \(H=\sinh p\) and \(J=\cosh p\):
\[
A(a,c)=\begin{cases}
\dfrac{\pi^2e^{-2p}(1+ce^{2p})^2}{J^2},&0<c\le e^{-4p},\\[5pt]
\dfrac{\pi^2e^{-2p}(1-ce^{2p})^2}{H^2},&e^{-4p}\le c\le e^{-2p},\\[5pt]
0,&e^{-2p}\le c\le e^{2p},\\[5pt]
\dfrac{\pi^2e^{2p}(ce^{-2p}-1)^2}{H^2},&e^{2p}\le c\le e^{4p},\\[5pt]
\dfrac{\pi^2e^{2p}(ce^{-2p}+1)^2}{J^2},&c\ge e^{4p}.
\end{cases}
\]
The formulas agree at shared endpoints. In particular, this Gabor family is a frame exactly for \(0<c<e^{-2\pi a}\) or \(c>e^{2\pi a}\).

The two switches at \(c=e^{-4\pi a}\) and \(c=e^{4\pi a}\) are changes of the location of the exact minimizing Zak fiber; they are distinct from the intervening frame/nonframe thresholds. With energy-normalized lower bound \(\mathcal A(a,c)=A(a,c)/\|g_{a,c}\|_2^2\), the unique global maximizers over positive \(c\) are
\[
\boxed{c=e^{-4\pi a}\quad\text{or}\quad c=e^{4\pi a}},\qquad
\boxed{\max_{c>0}\mathcal A(a,c)=\frac{2\pi a}{\cosh(4\pi a)}}.
\]
The word unique here means exactly these two coefficients for each fixed \(a>0\).

## Assumptions and scope

The parameter \(a\) is any strictly positive real number, and the coefficient \(c\) is any strictly positive real number. The time and frequency lattice steps are both exactly one, with modulations \(e^{2\pi i mt}\), and the unnormalized window is exactly as displayed. Frame bounds use the squared norm convention
\[
A\|f\|_2^2\le\sum_{m,n\in\mathbb Z}|\langle f,e^{2\pi i m\cdot}g_{a,c}(\cdot-n)\rangle|^2\le B\|f\|_2^2.
\]
No assertion about noncritical lattices, unequal pole heights, arbitrary complex residues or optimal upper frame bounds is made. Although earlier literature discusses the frame-set question for general two-pole rational windows, the quantitative sharp lower bound and its energy-normalized optimum are the assertions assessed here.

## Proof

**1. Exact Zak fiber.** Define the unitary Zak map on \([0,1)^2\) by
\[
(Zf)(x,\omega)=\sum_{n\in\mathbb Z}f(x+n)e^{2\pi i n\omega},
\]
where the series is interpreted in \(L^2\) and, where applicable, by its conditional pointwise sum. For \(z\notin\mathbb Z\) and \(0<\omega<1\), the classical partial-fraction identity is
\[
\sum_{n\in\mathbb Z}\frac{e^{2\pi i n\omega}}{n+z}
=\frac{\pi e^{i\pi z(1-2\omega)}}{\sin(\pi z)}.
\]
For completeness, the function on the right on \(0<\omega<1\), extended periodically, has Fourier coefficient \(1/(n+z)\): directly integrating against \(e^{-2\pi i n\omega}\) yields \(\pi e^{i\pi z}(1-e^{-2\pi iz})/[2\pi i(n+z)\sin\pi z]=1/(n+z)\). Its interior Fourier series converges to the displayed smooth expression, while the endpoint values need not match.
Taking \(z=x-ia\) and \(z=x+ia\) yields, for \(0<x,\omega<1\),
\[
Zg_{a,c}(x,\omega)=\pi e^{i\pi x(1-2\omega)}
\left(\frac{y}{\sin\pi(x-ia)}+\frac{c/y}{\sin\pi(x+ia)}\right),
\quad y=e^{p(1-2\omega)}\in(e^{-p},e^p).
\]
The critical-density Gabor frame operator is unitarily equivalent under this map to multiplication by \(|Zg_{a,c}|^2\). Thus its squared optimal lower frame bound is the essential infimum of that multiplier. The displayed rational-trigonometric expression is bounded; consequently the upper Bessel bound is always finite. Endpoints in the following minimization represent limits from the open unit square, so their values belong to the essential range closure even though a conditional Fourier series can have different boundary representatives.

**2. A one-variable extremum reduction.** Put \(s=\sin^2(\pi x)\in[0,1]\), \(H=\sinh p\), and \(J=\cosh p\). Since
\[
|\sin\pi(x+ia)|^2=H^2+s,
\]
a direct numerator expansion gives
\[
|Zg_{a,c}|^2=\pi^2\frac{H^2(1-s)(y-c/y)^2+J^2s(y+c/y)^2}{(H^2+s)^2}.
\]
For each fixed \(y\), write its numerator as \(n_0+n_1s\), where \(n_0=H^2(y-c/y)^2\) and
\[
n_1=J^2(y+c/y)^2-H^2(y-c/y)^2=(y+c/y)^2+4cH^2>0.
\]
The derivative of \((n_0+n_1s)/(H^2+s)^2\) has the sign of \(n_1H^2-2n_0-n_1s\). This is strictly decreasing in \(s\); hence an interior critical point, if present, is a maximum, never a minimum. Therefore
\[
\operatorname*{ess\,inf}_{x,\omega}|Zg_{a,c}|^2
=\pi^2\inf_{e^{-p}<y<e^p}\min\left\{
\frac{(y-c/y)^2}{H^2},\frac{(y+c/y)^2}{J^2}\right\}.
\]
(The closed-interval infimum is identical.) The two terms correspond respectively to \(x=0\) and \(x=1/2\).

**3. Complete minimization in the positive residue.** If \(e^{-2p}\le c\le e^{2p}\), the choice \(y=\sqrt c\) makes the first term zero (or approaches zero at an endpoint), so the lower bound is zero. If \(c<e^{-2p}\), then \(y>\sqrt c\) throughout the range, and both \((y-c/y)^2\) and \((y+c/y)^2\) increase with \(y\); their infima occur at \(y=e^{-p}\). This gives
\[
A(a,c)=\pi^2e^{-2p}\min\left\{
\frac{(1-ce^{2p})^2}{H^2},\frac{(1+ce^{2p})^2}{J^2}\right\}.
\]
The second choice is smaller exactly when \(c\le e^{-4p}\), because \((J-H)/(J+H)=e^{-2p}\). Conversely, if \(c>e^{2p}\), both relevant squares decrease with \(y\), so their infima occur at \(y=e^p\). One obtains
\[
A(a,c)=\pi^2e^{2p}\min\left\{
\frac{(ce^{-2p}-1)^2}{H^2},\frac{(ce^{-2p}+1)^2}{J^2}\right\},
\]
whose first term is smaller exactly when \(c\le e^{4p}\). This proves every branch, including all boundary values. It also proves the asserted frame criterion, since the multiplier remains bounded above and has positive essential infimum precisely outside the intervening interval.

**4. Exact energy normalization and optimum.** By contour integration, or Hardy half-plane orthogonality,
\[
\int_{\mathbb R}\frac{dt}{t^2+a^2}=\frac\pi a,
\qquad \int_{\mathbb R}\frac{dt}{(t-ia)^2}=0,
\qquad \|g_{a,c}\|_2^2=\frac\pi a(1+c^2).
\]
For \(0<c<e^{-4p}\), the normalized lower bound is proportional to \((1+ce^{2p})^2/(1+c^2)\), whose derivative is positive, since \(e^{2p}>c\). For \(e^{-4p}<c<e^{-2p}\), it is proportional to \((1-ce^{2p})^2/(1+c^2)\), whose derivative is negative. It vanishes in the nonframe interval. Finally, time reversal yields \(g_{a,c}(-t)=-c\,g_{a,1/c}(t)\); hence \(A(a,c)=c^2A(a,1/c)\), and the normalized bound is invariant under \(c\mapsto1/c\). Its only maxima are therefore \(c=e^{-4p}\) and \(c=e^{4p}\). At either point the unnormalized bound is \(4\pi^2e^{-4p}\) on the low branch (or its reciprocal equivalent), and division by \(\pi(1+e^{-8p})/a\) gives \(2\pi a/\cosh(4p)\), as claimed.

## Verification

The complete independent mathematical argument is the preceding partial-fraction identity, derivative-sign reduction and one-dimensional endpoint optimization. The standard-library script `checker.py` evaluates the closed-form Zak expression against its real algebraic form, checks random interior lower-bound inequalities, constructs minimizing endpoints and exact zeros, tests reciprocity and the normalized optimum, checks conditional Fourier sums and checks cancellation at complex coefficients outside the claim. Run `python3 checker.py` in the same directory. A successful run prints `PASS 14508 supplementary checks; finite checks do not prove the theorem`. All identities needed for the infinite statement are proved analytically; finite checks alone are not the proof.

## Relationship to prior work

Belov, Kulikov and Lyubarskii's 2021 work introduced a general rational-window Gabor framework, established Herglotz-window frame properties and **announced** a complete two-Cauchy-kernel frame-set description without the detailed proof in the inspected article (Section 1.7.2). Thus the **qualitative frame/nonframe classification is not asserted to be novel independently**. The distinctive claim here is the exact optimal squared lower frame bound for every positive residue, including the two internal minimizer transitions, and the unique energy-normalized maximizing residues. Neither an existence-only frame-set theorem nor a single-Cauchy-kernel estimate supplies this quantitative formula without additional optimization.

The 2022 preprint on the frame operator of a single Cauchy kernel provides a natural one-pole comparison; its accessible abstract does not establish mixed opposite-pole bounds, but its complete text was not reviewed. Related 2026 work on rational windows with symmetric poles addresses a different multi-pole family and rational-density frame behavior; its abstract was inspected, not its full manuscript. The novelty comparison therefore has a stated historical-priority risk and is not independent certification.

## Limitations

The theorem concerns the positive coefficient family and the unit critical Gabor lattice. It does not give a new full two-kernel frame-set theory, arbitrary-complex-coefficient sharp bounds, all lattice densities, a sharp upper frame bound or a noise-dependent reconstruction algorithm. The qualitative frame set was previously announced. The full text of the single-pole 2022 preprint and the 2026 symmetric-pole paper was not inspected, leaving a residual possibility of indirect or earlier quantitative coverage. No independent mathematical validation has been performed.

## References

1. Y. Belov, A. Kulikov and Y. Lyubarskii, *Gabor frames for rational functions*, arXiv:2103.08959 (first submitted March 16, 2021), *Inventiones mathematicae* 231 (2023), 431–466, DOI: 10.1007/s00222-022-01151-8. Full text of the open journal article inspected, especially Sections 1, 2 and 5.
2. Y. Belov, A. Kulikov and Y. Lyubarskii, *Gabor frame operator for the Cauchy kernel*, arXiv:2212.08915 (first submitted December 17, 2022). Accessible abstract inspected.
3. R. Ghosh, *Gabor Frames for Rational Windows with Symmetric Poles*, arXiv:2608.10568 (first submitted August 11, 2026). Abstract inspected for potential later indirect coverage.
4. K. Gröchenig, *Foundations of Time-Frequency Analysis*, Birkhäuser, 2001, Chapter 8 (classical Zak criterion; cited by Reference 1).
