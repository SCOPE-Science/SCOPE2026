# Arithmetic finite-size gap law for a dissipative SSH ring

## Finding

For the bond-dissipated fermionic Su–Schrieffer–Heeger ring of Yang, Jiang and Bergholtz, fix hopping amplitudes \(0<a<b\), intracell dissipation \(g>0\), zero intercell and on-site dissipation, and \(N\ge2\) unit cells. Put
\[
\theta=\frac{1}{2\pi}\arccos(-a/b)\in(1/4,1/2),\qquad
C=\frac{4\pi^2g(b^2-a^2)}{b^2-a^2+g^2}>0,
\]
where \(\|x\|=\min_{m\in\mathbb Z}|x-m|\). For the rapidity-gap convention of the cited source, the finite-ring gap obeys the *uniform relative law*
\[
\boxed{\displaystyle
\Delta_N=C\frac{\|N\theta\|^2}{N^2}
\bigl(1+O_{a,b,g}(N^{-1})\bigr).}
\]
The formula includes exact zeros, since \(\Delta_N=0\) precisely when \(N\theta\in\mathbb Z\); equivalently the absolute error is at most \(K\|N\theta\|^2/N^3\) for all sufficiently large integers \(N\), for a constant \(K\) depending only on the fixed amplitudes. It therefore remains valid uniformly along arbitrarily close resonances.

If \(\theta=p/r\) in lowest terms, the gap vanishes for exactly the sizes divisible by \(r\). If \(\theta\) is irrational, the gap is strictly positive at **every** finite size, but satisfies
\[
\liminf_{N\to\infty}N^2\Delta_N=0,\qquad
\limsup_{N\to\infty}N^2\Delta_N=C/4.
\]
For rational \(\theta=p/r\), the corresponding upper limit is \(C\lfloor r/2\rfloor^2/r^2\) and the lower limit is zero. Every irrational angle has infinitely many near-resonant sizes at which \(\Delta_N=O(N^{-4})\). If the irrational angle is badly approximable, these near-resonant gaps have order \(N^{-4}\) along a subsequence, while an \(N^{-4}\) lower bound holds at all sufficiently large sizes. Thus the exact finite-ring relaxation scale is arithmetic even at fixed physical parameters.

## Assumptions and scope

The object is the **periodic** quadratic Lindblad model, with the source notation \(t_1=a\), \(t_2=b\), \(\gamma_1=g\), \(\gamma_2=0\), and no additional on-site gain or loss. No magnetic flux, disorder, or driving is included. The periodic allowed Bloch momenta are \(q_j=2\pi j/N\) for \(j=0,\ldots,N-1\). In the exact spectral solution of the source (Eq. (2.23)), the two rapidities are
\[
\beta_\pm(q)=g\pm i\sqrt{a^2+b^2-g^2+2ab\cos q+2ibg\sin q}.
\]
The branch choice of the square root only interchanges the two signs. Define the **rapidity gap** as in Eq. (2.5) of the source,
\[
\Delta_N=2\min_{0\le j<N,\ \sigma\in\{+,-\}}\operatorname{Re}\beta_\sigma(q_j).
\]
In particular, the zero-mode convention here is *not* the smallest strictly positive decay rate after removing additional stationary modes when extra zero modes exist. All large-size limits keep \(a,b,g\) fixed and take \(N\) through positive integers.

## Proof

**1. Exact positivity and zeros.** Set \(u(q)=a+b\cos q\) and \(v(q)=b\sin q\). The discriminant factors as
\[
D(q)=u(q)^2+(v(q)+ig)^2.
\]
Write \(R(q)=|D(q)|\), \(S(q)=u(q)^2+v(q)^2+g^2\), and \(Y(q)=|\operatorname{Im}\sqrt{D(q)}|\). The elementary complex square-root identity gives
\[
Y^2=\tfrac12\bigl(R-u^2-v^2+g^2\bigr),\qquad
S^2-R^2=4g^2u^2.
\]
Since \(R\le S\), one has \(Y\le g\) and the branch-minimized mode gap is
\[
F(q)=2\bigl(g-Y(q)\bigr)
=\frac{4g^2u(q)^2}{\bigl(S(q)+R(q)\bigr)\bigl(g+Y(q)\bigr)}.
\]
All denominators are strictly positive because \(g>0\), so \(F(q)=0\) if and only if \(u(q)=0\). As \(0<a<b\), the only zeros modulo \(2\pi\) occur at \(q=\pm q_*\), where \(q_*=\arccos(-a/b)=2\pi\theta\). A discrete grid meets either zero exactly if and only if \(N\theta\) is an integer. This proves the zero criterion and strict positivity otherwise.

**2. Curvature at the two soft modes.** At either zero, \(u=0\) and \(v^2=b^2-a^2=:s^2>0\). The exact quotient above, together with \(u(q_*+\delta)^2=s^2\delta^2+O(\delta^3)\), gives
\[
F(q_*+\delta)=\kappa\delta^2\bigl(1+O(\delta)\bigr),\qquad
\kappa=\frac{gs^2}{s^2+g^2}>0.
\]
The same expansion holds at \(-q_*\), with the same positive coefficient. These expansions are ordinary real-analytic local expansions (the discriminant is nonzero at both zeros).

**3. Uniform minimization over the Bloch grid.** Let \(d_N=(2\pi/N)\|N\theta\|\), the geodesic distance from either zero to the nearest grid momentum. Since \(d_N\le\pi/N\), testing a nearest grid point gives \(\Delta_N\le(\kappa+O(N^{-1}))d_N^2\). Conversely, away from any fixed small neighborhood of the two zeros, the continuous positive function \(F\) has a positive lower bound. The preceding upper bound therefore forces every minimizing momentum into such a neighborhood for all large \(N\). The local positive quadratic lower bound then forces its distance from a zero to be \(O(N^{-1})\). Applying the local Taylor bound there and using that this distance is at least \(d_N\) yields
\[
(\kappa-O(N^{-1}))d_N^2\le\Delta_N\le
(\kappa+O(N^{-1}))d_N^2.
\]
For \(d_N=0\) exact positivity gives \(\Delta_N=0\), so no division by a vanishing quantity is needed. Substituting \(d_N=2\pi\|N\theta\|/N\) gives the asserted uniform formula with \(C=4\pi^2\kappa\).

**4. Arithmetic limits.** If \(\theta=p/r\) reduced, \(N\theta\) is an integer exactly when \(r\mid N\), and the distances \(\|Np/r\|\) cycle through \(\|j/r\|\), \(0\le j<r\). Their maximum is \(\lfloor r/2\rfloor/r\). If \(\theta\) is irrational, the fractional parts \(\{N\theta\}\) are dense in \([0,1]\), whence \(\|N\theta\|\) approaches both \(0\) and \(1/2\) along subsequences. The uniform error in Step 3 proves both limit formulas. Continued-fraction convergent denominators \(N\) of any irrational \(\theta\) satisfy \(\|N\theta\|<1/N\) infinitely often; then \(\Delta_N=O(N^{-4})\). If \(\theta\) is badly approximable, there exists \(c>0\) with \(\|N\theta\|\ge c/N\) for all \(N\), giving the matching global lower bound and the claimed near-resonant order.

## Verification

The accompanying `verify_gap.py` evaluates the **finite** Bloch grid directly from the source's complex rapidities and compares against the predicted uniform leading term. It checks a rational angle with exact resonant multiples and a quadratic-irrational angle with pronounced small-divisor dips. This is a reproducibility check only: the statements for all sizes and every irrational angle are proved by the analytic and number-theoretic arguments above, not inferred from the samples.

## Relationship to prior work

Yang, Jiang and Bergholtz, arXiv:2203.01333 (first posted 2022-03-02), give the exact two-branch rapidity spectrum in Eq. (2.23), Bloch sampling in Appendix A, and the continuum periodic gap-closure regime in Eq. (2.45). Song, Yao and Wang, arXiv:1904.08432 (first posted 2019-04-17), establish the periodic/open damping contrast and the quartic *endpoint* momentum dispersion when \(a=b\). The present result concerns **interior** \(0<a<b\) and quantifies the size-dependent rational/irrational sampling of the two interior quadratic soft modes, including an exact zero-size classification and uniform small-divisor law. A full exact band formula determines any chosen finite case but does not itself state these arithmetic limit and subsequence results; the additional uniform minimization argument and Diophantine classification are supplied here. The earlier endpoint quartic mode law is not the mechanism for interior \(N^{-4}\) subsequences.

## Limitations

This theorem concerns the source's rapidity-gap convention under periodic boundaries, not the entire relaxation of every observable or uniqueness of a nonequilibrium steady state. At resonant sizes additional zero rapidities appear; removing all zero modes before defining a positive spectral gap is a different question. No estimates uniform when \(a\uparrow b\), \(a\downarrow0\), or \(g\to0\) are claimed. Constants may depend on fixed amplitudes. The \(N^{-4}\) bound is an infinite subsequence statement, **not** a generic all-size upper bound; rapidly approximable irrational angles may have much smaller rare gaps. The classification uses the exact solvable, translation-invariant, undriven linear-dissipation model and does not extend to interactions or disorder without further work.

## References

1. F. Yang, Q.-D. Jiang, and E. J. Bergholtz, *Liouvillian skin effect in an exactly solvable model*, arXiv:2203.01333, version 1 posted 2022-03-02, especially Eqs. (2.5), (2.23), (2.45), and Appendix A. https://arxiv.org/abs/2203.01333
2. F. Song, S. Yao, and Z. Wang, *Non-Hermitian skin effect and chiral damping in open quantum systems*, arXiv:1904.08432, version 1 posted 2019-04-17, especially Eqs. (11)–(12). https://arxiv.org/abs/1904.08432
