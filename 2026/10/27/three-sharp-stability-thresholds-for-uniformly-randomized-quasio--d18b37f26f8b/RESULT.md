# Three sharp stability thresholds for uniformly randomized quasioptimal alternating projections

## Finding

Let \(A\) and \(B\) be two distinct lines through the origin in the real Euclidean plane, with acute angle \(\theta\in(0,\pi/2]\). Put \(c=\cos\theta\in[0,1)\) and \(s=\sin\theta>0\). At every step, choose **independently and uniformly by arclength** a point in the entire \(\sigma\)-quasioptimal projection interval on the next line: its distance from the current point must not exceed \(\sigma\) times the minimum distance, where \(\sigma\ge1\). Write \(r=\sqrt{\sigma^2-1}\).

For every nonzero initial point in \(A\), three different notions of convergence have **sharp** boundaries:

1. **Adversarial/all-selection convergence:** every sequence of admissible choices converges to the intersection if and only if \(0\le r<r_{\rm rob}(c):=(1-c)/s\). At equality a stationary nonzero sequence of sweeps is admissible; above it an exponentially divergent sequence is admissible.
2. **Mean-square convergence under uniform sampling:** \(\mathbb E\|a_n\|^2\to0\) if and only if \(r<\sqrt3\), independently of the angle. Precisely, \(\mathbb E\|a_n\|^2=\|a_0\|^2(c^2+s^2r^2/3)^{2n}\).
3. **Almost-sure convergence under uniform sampling:** \(a_n\to0\) almost surely if and only if \(0\le r<R(c)\), where \(R(c)\) is the unique positive solution of
   \[
   \mathcal L_c(R)=\frac{1}{2}\int_{-1}^1\log|c+sR u|\,du=0.
   \]
   For \(c=0\), \(R(0)=e\). For \(0<c<1\), this is an explicit one-variable equation as described below. At the critical value \(r=R(c)\), the nonzero sweep coefficients have almost-sure logarithmic limsup \(+\infty\) and liminf \(-\infty\), hence they do not converge. For \(r>R(c)\) their magnitudes diverge exponentially almost surely.

The three boundaries are strictly ordered for every angle:
\[
0<r_{\rm rob}(c)<\sqrt3<R(c).
\]
Thus an unconditionally stable deterministic quasioptimality tolerance, a universally angle-independent second-moment tolerance \(\sigma=2\), and an appreciably larger pathwise tolerance are genuinely different. For perpendicular lines the three critical tolerances are \(\sqrt2\), \(2\), and \(\sqrt{1+e^2}\), respectively.

More generally, for any \(p>0\) and any \(r>0\), the exact \(p\)-moment law is
\[
\mathbb E\|a_n\|^p=\|a_0\|^p\mathcal M_p(c,r)^{2n},\qquad
\mathcal M_p(c,r)=\frac{(c+sr)|c+sr|^p-(c-sr)|c-sr|^p}{2sr(p+1)}.
\]
The law at \(r=0\) is the continuous limit \(\mathcal M_p(c,0)=c^p\). For fixed \(p>0\), \(p\)-moment convergence holds exactly when \(\mathcal M_p(c,r)<1\).

## Assumptions and scope

All spaces are real and two-dimensional. Both lines are complete, closed, distinct, and intersect only at the origin. Their unoriented acute angle satisfies \(0<\theta\le\pi/2\). The same finite quasioptimality ratio \(\sigma\ge1\) is used at every projection. The random choice is conditionally uniform in the **whole feasible interval** on the target line, with independent choices between steps; it is not a uniformly chosen direction, nor an independent additive perturbation of fixed size. No assumption about a typical numerical implementation realizing this distribution is made.

A sweep starts at \(a_n\in A\), selects \(b_{n+1}\in B\), then selects \(a_{n+1}\in A\). The convergence assertions concern all sweeps and also imply the corresponding conclusions for intermediate \(b_n\) whenever convergence to zero occurs. At a zero iterate the only quasioptimal projection is zero and it remains zero. For nonzero initial points, uniform continuous sampling hits an exactly zero multiplier with probability zero when \(r>0\).

## Proof

Choose unit coordinates \(e_A=(1,0)\), \(e_B=(c,s)\). If the present point is \(x e_A\), its orthogonal projection onto \(B\) is \(cx e_B\) and its distance to \(B\) is \(s|x|\). By the Pythagorean theorem, a point \(y e_B\) is \(\sigma\)-quasioptimal precisely when
\[
|y-cx|\le s|x|\sqrt{\sigma^2-1}=sr|x|.
\]
Uniform arclength selection therefore has the exact conditional representation \(y=x(c+sU)\) with \(U\sim\operatorname{Unif}[-r,r]\), regardless of the sign of \(x\). Projection back onto \(A\) has the same form with a fresh independent \(V\). Hence, for \(a_n=X_n e_A\),
\[
X_{n+1}=X_n(c+sU_n)(c+sV_n),
\]
where all \(U_n,V_n\) are mutually independent and uniform on \([-r,r]\). This is an identity for the specified algorithm, not an approximation.

For arbitrary admissible selections, each scalar factor has maximum absolute magnitude \(c+sr\), so every sweep contracts by at most \((c+sr)^2\). If this is less than one, every selection converges geometrically. At equality, selecting \(U_n=V_n=r\) preserves the nonzero coefficient, and for greater values the same endpoint rule grows geometrically. Solving \(c+sr<1\) gives \(r<r_{\rm rob}(c)\).

Since \(\mathbb E U=0\), \(\mathbb E U^2=r^2/3\), independence gives
\[
\mathbb E X_n^2=X_0^2\left(c^2+\frac{s^2r^2}{3}\right)^{2n}.
\]
The identity \(c^2+s^2=1\) makes the condition for strict decay exactly \(r<\sqrt3\), with an unchanged positive second moment at equality and exponential growth above. Likewise, integration of \(|c+su|^p\) over \([-r,r]\) produces the stated general \(p\)-moment formula.

For \(r>0\), define \(Z_j=\log|c+sU_j|\). Its first two absolute moments are finite, including if the interval crosses zero, because logarithmic singularities are integrable. Its variance is strictly positive. The strong law of large numbers gives, almost surely,
\[
\lim_{n\to\infty}\frac{\log|X_n/X_0|}{n}=2\mathcal L_c(r),\qquad
\mathcal L_c(r)=\mathbb E Z_1.
\]
Thus a negative exponent implies exponential decay and a positive exponent implies exponential divergence. At an exponent of zero, the ordinary law of the iterated logarithm for the independent centered variables \(Z_j\) gives unbounded positive and negative excursions of \(\log|X_n/X_0|\); in particular there is no convergence to zero. The deterministic case \(r=0\) contracts by \(c^2<1\), and at \(c=r=0\) reaches the intersection immediately.

It remains to prove that the exponent changes sign exactly once. If \(0<c<1\) and \(0<r<c/s\), Jensen's inequality gives \(\mathcal L_c(r)<\log c<0\); at \(r=c/s\), direct integration gives \(\mathcal L_c(r)=\log(2c)-1<0\). For \(r>c/s\), write \(t=c/(sr)\in(0,1)\), and let
\[
G(t)=\frac{(1+t)\log(1+t)+(1-t)\log(1-t)}{2}.
\]
Then direct integration yields
\[
\mathcal L_c(r)=\log(sr)-1+G(t),\qquad
\frac{d}{dr}\mathcal L_c(r)=\frac{1-t\operatorname{artanh}(t)}{r}.
\]
Because \(t\operatorname{artanh}(t)\) strictly increases from zero to infinity on \((0,1)\), the exponent first strictly decreases and then strictly increases as \(r\) grows beyond \(c/s\). It tends to \(+\infty\) with \(\log(sr)-1\), so it has exactly one positive root \(R(c)\). At \(c=0\), integration directly gives \(\mathcal L_0(r)=\log r-1\), yielding \(R(0)=e\).

Finally \(r_{\rm rob}(c)=(1-c)/s=s/(1+c)\le1<\sqrt3\). At \(r=\sqrt3\), strict Jensen inequality for the nonconstant positive random variable \(|c+sU|^2\) shows
\[
2\mathcal L_c(\sqrt3)=\mathbb E\log|c+sU|^2<\log\mathbb E|c+sU|^2=0,
\]
so \(R(c)>\sqrt3\). All inequalities are strict, including for \(c=0\).

## Verification

The accompanying `verify.py` uses only the Python standard library. It verifies the Pythagorean-admissibility identity numerically on bounded rational-parameter samples, checks the second- and fourth-moment expansions using exact rational arithmetic, confirms the angle-independent second-moment threshold, and independently evaluates the logarithmic exponent and its unique root at several angles. Run `python verify.py` from the package directory. These finite tests are consistency checks; the infinite-time conclusions follow from the proof, not from numerical experiments.

## Relationship to prior work

Budzinskiy, *Quasioptimal alternating projections and their use in low-rank approximation of matrices and tensors* (first public preprint 2023), defines the same multiplicative quasioptimality ratio and proves deterministic local linear convergence under transversality and regularity assumptions. Its Theorem 5.6 gives a sufficient two-tolerance contraction criterion. Specializing that sufficient criterion to two lines recovers the adversarial safe region above; the published article also explicitly gives the perpendicular-coordinate-axis divergence example. Neither fact is asserted as a previously unknown deterministic result. The present contribution is the **exact uniform-random-selection model and its three non-equivalent sharp stability notions**, notably the angle-independent \(\sigma=2\) mean-square boundary, the explicit pathwise boundary, and their strict separation.

Diaconis, Khare, and Saloff-Coste, *Stochastic alternating projections* (2010), analyze iterated conditional expectations and Gibbs-sampler relationships, which use exact Hilbert projections rather than a uniform choice among quasioptimal Euclidean projection outputs. The standard strong law and law of the iterated logarithm supply the probability tools after the new finite-dimensional reduction; they are not claimed as new theorems.

## Limitations

Uniform arclength selection is a specified model, not a universal characterization of randomized approximate projection solvers. The sharp random thresholds can change under biased, dependent, state-dependent, or unequal-tolerance sampling, or in higher-dimensional/nonlinear target sets. The assertion of worst-case robustness concerns **all** admissible choices, while the probabilistic assertions concern only the stated independent uniform oracle. No finite-time optimality, computational-complexity claim, or application guarantee for specific low-rank algorithms follows. At the almost-sure critical point the logarithmic random walk oscillates; no positive deterministic convergence rate exists there. Related work not surfaced in the literature searches could have an equivalent specialized result.

## References

1. Stanislav Budzinskiy, *Quasioptimal alternating projections and their use in low-rank approximation of matrices and tensors*, arXiv:2308.16097 (first posted 2023-08-30; full-text version v3 inspected), especially Definition of quasioptimal projections, Section 4, Theorems 5.3 and 5.6, and their proofs. https://arxiv.org/abs/2308.16097
2. Persi Diaconis, Kshitij Khare, and Laurent Saloff-Coste, *Stochastic alternating projections*, Illinois Journal of Mathematics 54 (2010), 963–979, DOI:10.1215/ijm/1336568522. https://doi.org/10.1215/ijm/1336568522
3. Heinz H. Bauschke, D. Russell Luke, Hung M. Phan, and Xianfu Wang, *Restricted normal cones and the method of alternating projections: theory*, Set-Valued and Variational Analysis 21 (2013), 431–473, arXiv:1205.0318. https://arxiv.org/abs/1205.0318
