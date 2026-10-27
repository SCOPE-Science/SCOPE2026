# A sharp flip law and singular sign-cycle selection for a two-floor spectral surrogate

## Finding

Consider the fixed-step scalar iteration obtained from a fourth-power soft-sign preconditioner **with a preceding gradient normalization floor**, as in the deterministic specialization of equation (30) of [1]. Two distinct floors are essential. For every \(\lambda,\gamma,\varepsilon,\delta>0\), let
\[
L(r)=\left[\varepsilon^4(\lambda r+\delta)^4+(\lambda r)^4\right]^{1/4},\qquad
F(x)=x\left(1-\frac{\gamma\lambda}{L(|x|)}\right),\quad r\geq0.
\]
Here \(F\) is the actual scalar update when the objective is \(f(x)=\lambda x^2/2\), the direction is its deterministic gradient, the normalization uses \(d/(|d|+\delta)\), and the soft-sign surrogate is \(z/(\varepsilon^4+|z|^4)^{1/4}\).

Write \(C=\gamma\lambda\). The following statements hold.

**(i) Global convergence frontier.** If \(0<C\leq2\varepsilon\delta\), every real orbit converges to zero. If \(0<C<2\varepsilon\delta\), the fixed point is linearly attracting with multiplier \(1-C/(\varepsilon\delta)\). At the exact matched value \(C=\varepsilon\delta\), its first nonzero local term is quadratic:
\[
F(x)=\frac{\lambda}{\delta}x|x|+O(|x|^3).
\]

**(ii) Critical law.** If \(C=2\varepsilon\delta\), any orbit that never hits zero obeys the sharp limit
\[
\lim_{n\to\infty}n|x_n|=\frac{\delta}{2\lambda}.
\]
Some exceptional starting points reach zero in finitely many steps; they are excluded from this asymptotic assertion.

**(iii) The supercritical symmetric cycle.** If \(C>2\varepsilon\delta\), zero is linearly unstable. There exists exactly one positive number \(a\) for which \(\{a,-a\}\) is a symmetric nonzero two-cycle, characterized by
\[
L(a)=\frac{C}{2}.
\]
This two-cycle is locally asymptotically attracting. With \(A=\lambda a\), its two-step multiplier is
\[
\left(-1+2q\right)^2,\quad
q=\frac{A[\varepsilon^4(A+\delta)^3+A^3]}{\varepsilon^4(A+\delta)^4+A^4},\qquad 0<q<1.
\]
As the supercritical gap \(C-2\varepsilon\delta\) decreases to zero with \(\lambda,\varepsilon,\delta\) fixed,
\[
a=\frac{C-2\varepsilon\delta}{2\varepsilon\lambda}+O\!\left((C-2\varepsilon\delta)^2\right).
\]
Thus the cycle amplitude emerges **linearly** rather than with the fourth-root critical scaling of the same soft sign without pre-normalization.

**(iv) Singular removal of the normalization floor.** Holding \(\gamma,\lambda,\varepsilon>0\) fixed while \(\delta\downarrow0\), the attracting symmetric cycle satisfies
\[
\lim_{\delta\downarrow0}a=\frac{\gamma}{2(1+\varepsilon^4)^{1/4}},
\qquad
\lim_{\delta\downarrow0}\left(-1+2q\right)^2=1.
\]
At \(\delta=0\), define \(F_0(0)=0\) and \(F_0(x)=x-t\operatorname{sgn}(x)\) for \(x\ne0\), where \(t=\gamma/(1+\varepsilon^4)^{1/4}\). Every \(\{u,u-t\}\) with \(0<u<t\) is then a neutral period-two orbit. Positive normalization selects the symmetric midpoint of this continuum and turns it into a locally attracting cycle, with attraction degenerating as the floor vanishes.

## Assumptions and scope

Everything is in exact real arithmetic, for a deterministic one-dimensional quadratic, one preconditioned update per iteration, a constant learning rate, and strictly positive independent floors \(\varepsilon\) (intrinsic) and \(\delta\) (pre-normalization). No stochastic noise, matrix Newton–Schulz polynomial, momentum state, or decreasing stepsize is included. Local attraction of the supercritical cycle is not a claim of global convergence to that cycle.

## Proof

**Derivation.** For \(d=\lambda x\), insert \(z=d/(|d|+\delta)\) into \(z/(\varepsilon^4+|z|^4)^{1/4}\) and multiply numerator and denominator by \(|d|+\delta\). This gives \(d/L(|x|)\). Thus \(F\) is exactly the stated composition, including both floors. The denominator \(L\) is positive, continuous and strictly increasing from \(L(0)=\varepsilon\delta\) to infinity; moreover, \(F\) is odd.

**Subcritical and critical contraction.** For \(r>0\), \(L(r)>\varepsilon\delta\). If \(0<C\leq2\varepsilon\delta\), then \(0<C/L(r)<2\), hence \(|F(x)|<|x|\) for each nonzero \(x\). The monotone magnitude sequence converges to some \(\ell\geq0\); continuity and the strict inequality at every positive \(\ell\) force \(\ell=0\). At zero the derivative is \(F'(0)=1-C/(\varepsilon\delta)\). Expanding the strictly positive denominator for \(r\to0+\) yields
\[
L(r)=\varepsilon\delta+\varepsilon\lambda r+O(r^2),\qquad
\frac{C}{L(r)}=\frac{C}{\varepsilon\delta}\left(1-\frac{\lambda}{\delta}r+O(r^2)\right).
\]
With \(C=\varepsilon\delta\), this gives \(F(x)=(\lambda/\delta)x|x|+O(|x|^3)\). With \(C=2\varepsilon\delta\), near zero \(F(x)=x[-1+(2\lambda/\delta)|x|+O(x^2)]\). Since all nonterminating critical orbits converge to zero, their magnitudes eventually satisfy
\[
r_{n+1}=r_n-\frac{2\lambda}{\delta}r_n^2+O(r_n^3).
\]
For a positive sequence with this expansion, \(r_{n+1}/r_n\to1\) and \(r_{n+1}^{-1}-r_n^{-1}\to2\lambda/\delta\). Cesàro averaging therefore yields \(1/(nr_n)\to2\lambda/\delta\), proving the critical limit. The possibility of finitely hitting zero is expressly excluded.

**Supercritical existence, uniqueness and attraction.** The positive symmetric orbit equation is \(F(a)=-a\), equivalent to \(L(a)=C/2\). Strict monotonicity and \(C/2>L(0)\) give a unique positive root. The local fixed-point multiplier \(F'(0)=1-C/(\varepsilon\delta)<-1\) establishes instability. Let \(D(A)=\varepsilon^4(A+\delta)^4+A^4\), so \(L(a)=D(A)^{1/4}\). For \(r>0\), \(rL'(r)/L(r)=A[\varepsilon^4(A+\delta)^3+A^3]/D(A)=q\). The exact identity
\[
D(A)-A[\varepsilon^4(A+\delta)^3+A^3]
=\varepsilon^4\delta(A+\delta)^3>0
\]
proves \(0<q<1\). At the cycle, \(F'(a)=-1+2q\); oddness gives \(F'(-a)=F'(a)\). Consequently the period-two multiplier \((F'(a))^2=(-1+2q)^2<1\), proving local attraction. The expansion \(L(a)=\varepsilon\delta+\varepsilon\lambda a+O(a^2)\) and the implicit-function theorem prove the linear amplitude law.

**Singular limit.** For every fixed \(r>0\), as \(\delta\to0+\), \(L(r)\to \lambda r(1+\varepsilon^4)^{1/4}\). The unique positive root of \(L(a)=C/2\) therefore converges to \(a=\gamma/[2(1+\varepsilon^4)^{1/4}]\). The exact formula for \(q\) gives \(q\to1\), hence the squared multiplier tends to one. With \(\delta=0\), the update simplifies to the fixed-length sign step stated above. For any \(0<u<t\), the step alternates \(u\mapsto u-t\mapsto u\), and the two-step derivative along either nonzero branch equals one. This proves neutrality and selection. No assertion is made about arbitrarily switching limits \(n\to\infty\) and \(\delta\to0\).

## Verification

Run the standalone Python 3 standard-library script `VERIFY.py`. It checks the strict algebraic derivative gap with exact rational arithmetic, the two-cycle equation and multiplier numerically across 300 seeded parameter settings, the predicted critical \(1/n\) asymptotic, local quadratic coefficient, and the singular midpoint selection. The script prints `VERIFY_OK 2207 checks`. These finitely many checks are reproducibility diagnostics; all quantified claims above follow from the proof.

## Relationship to prior work

Equation (30) of [1] explicitly includes the additional pre-normalization floor distinct from the intrinsic fourth-power surrogate parameter; its Section F proves other convergence bounds and does not provide this fixed-step scalar phase classification. The unnormalized soft-sign fixed-step iteration has a different local normal form and therefore different critical exponents: removing pre-normalization changes the map itself, not merely its parameter names. [2] studies momentum soft-sign and algebraic spectral relaxations rather than this fourth-power two-floor composition. [3] treats actual Newton–Schulz or Polar-Express polynomials and stochastic nonconvergence, not this smooth surrogate's exact deterministic two-floor flip classification. Standard sign-update two-cycle phenomena explain the limiting continuum but not its unique regularized midpoint selection with a sharp multiplier.

## Limitations

The result does not establish behavior for the complete matrix optimizer, stochastic or momentum updates, variable stepsizes, or arbitrary objectives. The sole symmetric 2-cycle is locally attracting when supercritical; other asymmetric higher-period orbits and their basins are not classified. The singular sign map is discontinuous at zero. Other independent published analyses of this exact scalar two-floor map may exist.

## References

[1] K. Oikonomidis, J. Quan, K. Antonakopoulos, A. Silveti-Falls, V. Cevher, and P. Patrinos, *Constrained Stochastic Spectral Preconditioning Converges for Nonconvex Objectives*, arXiv:2605.11850v1 (2026-05-12), Section F, especially equation (30). https://arxiv.org/html/2605.11850v1

[2] *Softsign: Smooth Sign in Your Optimizer For Better Parameter Heterogeneity Handling*, arXiv:2605.31371v1 (2026). https://arxiv.org/html/2605.31371v1

[3] *On MUON optimization: From non-convergence to an error analysis with Polar Express and the Newton-Schulz polynomial from implementations*, arXiv:2608.04607v1 (2026). https://arxiv.org/abs/2608.04607
