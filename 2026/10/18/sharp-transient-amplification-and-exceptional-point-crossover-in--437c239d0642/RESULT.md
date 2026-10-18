# Sharp transient amplification and exceptional-point crossover in a two-population nonreciprocal flow

## Finding

Consider the real two-component linear system
\[
\frac{d m}{dt}=(\mu I_2+pA_\eta)m,\qquad
A_\eta=\begin{pmatrix}-\eta&1+\eta\\\eta-1&\eta\end{pmatrix},
\]
where \(p>0\), \(\mu<0\), and \(|\eta|\le1/\sqrt2\). Define the dimensionless damping \(r=-\mu/p>0\), nonnormality \(h=\sqrt2|\eta|\), and frequency parameter \(k=\sqrt{1-h^2}\). The operator norm is the standard Euclidean induced norm.

The full transient norm profile is
\[
\left\|e^{t(\mu I_2+pA_\eta)}\right\|_2
=\exp\!\left[-r\tau+\operatorname{arsinh}\!\left(
\frac{h|\sin(k\tau)|}{k}\right)\right],\qquad\tau=pt,
\]
with the continuous convention \(\sin(k\tau)/k=\tau\) at \(k=0\).

If \(r\ge h\), then the global maximum is exactly \(G=1\), attained at \(t=0\). If \(0<r<h\), put \(v=\sqrt{h^2-r^2}\). There is a **unique** global maximizer at positive time,
\[
\boxed{\displaystyle
 t_*=\frac{1}{pk}\arctan\!\frac{kv}{r},\qquad
 G=\frac{1+v}{\sqrt{k^2+r^2}}\exp\!\left[-\frac r k\arctan\!\frac{kv}{r}\right].}
\]
Both expressions have their continuous \(k=0\) limits: \(t_*=v/(pr)\) and \(G=(1+v)e^{-v}/r\). Thus the distinction between asymptotic stability and actual transient amplification is characterized exactly, not merely by the numerical-abscissa threshold.

A sharper singular regime occurs while approaching an exceptional point from the complex-eigenvalue side. Fix \(s>0\), set \(r=sk\), and let \(k\downarrow0\) (so \(h=\sqrt{1-k^2}\)). The unique maximizing time and gain satisfy
\[
\boxed{\displaystyle
 \lim_{k\downarrow0}kp t_*=\arctan(1/s),\qquad
 \lim_{k\downarrow0}kG=\Psi(s):=
 \frac{2e^{-s\arctan(1/s)}}{\sqrt{1+s^2}}.}
\]
The profile is strictly decreasing, with \(\Psi(s)\to2\) as \(s\downarrow0\) and \(s\Psi(s)\to2/e\) as \(s\to\infty\). The limits quantify a crossover between weakly damped oscillatory amplification and the damped Jordan-block regime. They hold for either sign of \(\eta\).

## Assumptions and scope

The theorem concerns exactly the **linearized** two-population magnetization equation about the disordered equilibrium in the nonreciprocal coupling model of Rippa, Garofalo and Lippiello [1]. In that model \(\mu=(1-p)a(q)-p\) and \(p\in(0,1]\); our statement uses only the resulting linear system and so holds whenever its parameters satisfy \(p>0\), \(\mu<0\), and \(|\eta|\le1/\sqrt2\). The borderline \(|\eta|=1/\sqrt2\) is admitted even though the eigenvalues and eigenvectors coalesce. No nonlinear, stochastic, or finite-amplitude prediction is inferred from the linear theorem.

The gain \(G\) means \(\sup_{t\ge0}\sup_{\|m(0)\|_2=1}\|m(t)\|_2\). It is not the maximum over one chosen initial perturbation. The parameter \(k\) is dimensionless and approaches zero through positive values in the crossover statement.

## Proof

**Step 1: Matrix exponential and exact singular values.** A direct multiplication gives \(\operatorname{tr}A_\eta=0\) and \(A_\eta^2=-k^2I_2\). For \(k>0\),
\[
 e^{\tau A_\eta}=\cos(k\tau)I_2+\frac{\sin(k\tau)}{k}A_\eta=:B(\tau).
\]
When \(k=0\), this reads \(B(\tau)=I_2+\tau A_\eta\). In every case \(\det B=1\) and
\[
 \operatorname{tr}(B^{\mathsf T}B)=2+4h^2\left(\frac{\sin(k\tau)}{k}\right)^2.
\]
For a real \(2\times2\) determinant-one matrix with Frobenius square \(2+4y^2\), the two singular values are \(\sqrt{1+y^2}\pm |y|\), as follows by solving their product-one and squared-sum constraints. Taking \(y=h\sin(k\tau)/k\) yields
\[
 \|B(\tau)\|_2=\sqrt{1+y^2}+|y|=e^{\operatorname{arsinh}|y|}.
\]
Multiplication by \(e^{-r\tau}\) establishes the asserted exact norm for all \(\tau\ge0\).

**Step 2: Global optimality.** Write \(f(\tau)=\log\|e^{\tau(A_\eta-rI_2)}\|_2\). In the first half-wave \(0<\tau<\pi/k\) for \(k>0\),
\[
 f'(\tau)=-r+\frac{h\cos(k\tau)}{\sqrt{1+(h^2/k^2)\sin^2(k\tau)}}.
\]
The second summand is strictly decreasing from \(h\) to \(-h\) in that half-wave if \(h>0\) (differentiate, noting \(k^2+h^2=1\)). If \(r\ge h\), the norm cannot exceed one: alternatively \(\operatorname{arsinh}(h|\sin(k\tau)|/k)\le h\tau\) follows from \(|\sin u|\le |u|\) and \(\operatorname{arsinh}u\le u\). The same inequality and conclusion hold at \(k=0\). If \(0<r<h\), there is precisely one zero of \(f'\) in the first quarter-wave. It obeys
\[
 \tan(k\tau_*)=\frac{k\sqrt{h^2-r^2}}r.
\]
At this zero, \(h\sin(k\tau_*)/k=v/\sqrt{k^2+r^2}\) and therefore \(e^{\operatorname{arsinh}(h\sin(k\tau_*)/k)}=(1+v)/\sqrt{k^2+r^2}\). This proves both formulas in the interior case. Every subsequent half-wave is an exact translated copy of the first undamped envelope, multiplied by the strict damping factor \(e^{-r\pi/k}<1\). Hence no later time ties or exceeds the first positive maximizer. At \(k=0\), \(f=-r\tau+\operatorname{arsinh}(h\tau)\) has derivative \(-r+h/\sqrt{1+h^2\tau^2}\), which supplies the same formulas and uniqueness directly.

**Step 3: Singular crossover.** Set \(h=\sqrt{1-k^2}\) and \(r=sk\), with \(s>0\) fixed. For all sufficiently small \(k\), \(r<h\). The first formula becomes
\[
 kp t_*=\arctan\!\left(\frac{\sqrt{1-(1+s^2)k^2}}s\right)
 \longrightarrow\arctan(1/s).
\]
In the gain formula, \(v=\sqrt{1-(1+s^2)k^2}\), and thus
\[
 kG=\frac{1+\sqrt{1-(1+s^2)k^2}}{\sqrt{1+s^2}}
 \exp\!\left[-s\arctan\!\left(\frac{\sqrt{1-(1+s^2)k^2}}s\right)\right]
 \longrightarrow\Psi(s).
\]
For \(s>0\), direct differentiation gives \((\log\Psi)'(s)=-\arctan(1/s)<0\). The endpoint limits follow from \(s\arctan(1/s)\to0\) at zero and \(s\arctan(1/s)\to1\) at infinity.

## Verification

The accompanying `verification.py` uses only the Python standard library. It independently evaluates \(2\times2\) spectral norms through a stable closed formula for real matrices and compares them with the trigonometric semigroup profile, the global optimizer, the Jordan endpoint, and the scaling profile. Its reported finite checks are numerical corroboration; the analytic proof above carries the quantified all-parameter and limiting statements. Run with `python3 verification.py`.

## Relationship to prior work

Rippa, Garofalo and Lippiello [1, equations (3), (6), and (7)] introduced the coupling matrix, computed the linearization and eigenvalues, and identified a numerical-abscissa transient-growth regime. Their cited exceptional-point lines and stability thresholds are prior results and are not claimed as new here. Their inspected main text does not give the exact \(t\)-dependent Euclidean singular norm, the unique global peak gain and its time, or the nonconstant joint damping/frequency crossover derived above.

Transient amplification through nonnormality, singular-value analysis, and exceptional points is established physics and matrix analysis: see Makris [2] and Sornette and coauthors [3]. Those methods and qualitative observations are not claimed as new. The inspected full text of [3] provides a Kreiss-constant lower bound for a different network model, rather than the exact source-specific two-population peak. The accessible abstract of [2] addresses non-Hermitian waveguide systems and supplies no comparable explicit formula, but its full text was not available to check; equivalent methods or reductions in earlier literature remain a nontrivial bibliographic risk. No claim of an exhaustive literature uniqueness certificate is made.

## Limitations

The theorem is strictly local/linear: it neither guarantees that a perturbation of finite magnetization attains the operator norm nor predicts nonlinear basins, noise-driven excursions, or fluctuations. Only the complex-frequency sector and its exceptional-point boundary are covered; the real-eigenvalue side \(|\eta|>1/\sqrt2\) is excluded. The scaling law fixes \(s=r/k>0\) before the singular limit; it is not uniform in \(s\) on unbounded intervals. The cited primary work's supplemental analyses, and the complete text of [2], were not all accessible for comprehensive comparison.

## References

[1] F. Rippa, J. A. Garofalo, E. Lippiello, *From Equilibrium Criticality to Universal Collective Phases through Nonreciprocal Coupling of Ordered Systems*, arXiv:2610.04450 (first submitted 2026-10-03), https://arxiv.org/abs/2610.04450.

[2] K. G. Makris, *Transient growth and dissipative exceptional points*, Physical Review E 104, 054218 (2021), https://doi.org/10.1103/PhysRevE.104.054218.

[3] D. Sornette, S. C. Lera, J. Lin, K. Wu, *Non-normal interactions create socio-economic bubbles*, Communications Physics 6, 261 (2023), https://doi.org/10.1038/s42005-023-01379-7; preprint arXiv:2205.08661.
