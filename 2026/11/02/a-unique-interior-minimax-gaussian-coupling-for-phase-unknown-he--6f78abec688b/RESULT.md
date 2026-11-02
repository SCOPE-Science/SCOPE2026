# A unique interior minimax Gaussian coupling for phase-unknown heat Fourier modes

## Finding

For every diffusion-time/frequency parameter \(q>0\), a Gaussian pair can estimate a real heat Fourier mode with any unknown phase using two marginally correct Brownian displacements. Among **all jointly Gaussian couplings** of those displacements, there is a unique correlation that minimizes the largest variance over phases. It is strictly between perfect antithesis and independence:

\[
 r_*(q)=-\frac{\log(2-e^{-q})}{q}\in(-1,0),\qquad
 \min_{-1\le r\le1}\max_{\phi\in\mathbb R}\operatorname{Var}H_{q,r,\phi}
 =\frac{(1-e^{-q})^2}{2(2-e^{-q})}.
\]

The minimizer balances the cosine and sine phase variances exactly, and is the only minimizing correlation. This worst-phase variance is strictly below that of either independent Gaussian displacements or a perfectly reflected pair, at every finite \(q>0\). In the small-\(q\) limit it is asymptotic to \(q^2/2\), whereas independent sampling has worst-phase variance asymptotic to \(q/2\). Perfect antithesis has a smaller worst-phase variance than independence exactly for \(0<q<\log 3\), ties at \(q=\log 3\), and is worse when \(q>\log 3\).

## Assumptions and scope

Take the periodic one-dimensional heat equation \(\partial_tu=\nu\partial_{xx}u\) with \(\nu,t>0\), and a fixed nonzero integer spatial frequency \(k\). Let \(\sigma^2=2\nu t\) and \(q=k^2\sigma^2>0\). For each \(r\in[-1,1]\), let \((Z_1,Z_2)\) be a centered jointly Gaussian vector with marginal variances \(\sigma^2\) and covariance \(r\sigma^2\). Degenerate endpoint couplings are included. Define, for arbitrary unknown phase \(\phi\in\mathbb R\),

\[
 H_{q,r,\phi}=\tfrac12\bigl(\cos(kZ_1+\phi)+\cos(kZ_2+\phi)\bigr).
\]

Its expectation is \(e^{-q/2}\cos\phi\), independently of \(r\); thus every admissible coupling is unbiased for the heat semigroup acting on \(\cos(kx+\phi)\) at \(x=0\). The performance criterion is the maximum **absolute variance** over all phases, not a phase-normalized relative variance. The optimization concerns correlations of a jointly Gaussian pair, not arbitrary couplings or adaptive estimators. The cost comparison fixes two function evaluations; generating a nondegenerate Gaussian pair uses an additional independent normal draw compared with exact reflection.

## Proof

Put \(z=e^{-q}\in(0,1)\), and define \(U=kZ_1\), \(V=kZ_2\). The Gaussian characteristic function gives

\[
 \mathbb E\cos U=\sqrt z,\quad
 \operatorname{Var}(\cos U)=\tfrac12(1-z)^2,\quad
 \operatorname{Var}(\sin U)=\tfrac12(1-z^2).
\]

Using \(\cos U\cos V=[\cos(U-V)+\cos(U+V)]/2\) and the analogous sine identity, the cross covariances are

\[
 \operatorname{Cov}(\cos U,\cos V)=z(\cosh(qr)-1),\quad
 \operatorname{Cov}(\sin U,\sin V)=z\sinh(qr).
\]

The mixed cosine-sine covariances vanish by joint reflection symmetry \((U,V)\mapsto(-U,-V)\). Define

\[
 C_q(r)=\tfrac12(1-z)^2+z(\cosh(qr)-1),\qquad
 S_q(r)=\tfrac12(1-z^2)+z\sinh(qr).
\]

Consequently, for every phase,

\[
 \operatorname{Var}H_{q,r,\phi}=\tfrac12\bigl(C_q(r)\cos^2\phi+S_q(r)\sin^2\phi\bigr),
 \qquad
 \max_\phi\operatorname{Var}H_{q,r,\phi}=\tfrac12\max\{C_q(r),S_q(r)\}.
\]

The exact difference simplifies to

\[
 C_q(r)-S_q(r)=z\bigl(e^{-qr}-(2-z)\bigr).
\]

On \([-1,0]\), \(C_q\) strictly decreases toward zero correlation and \(S_q\) strictly increases, because \(C_q'(r)=qz\sinh(qr)<0\) for \(r<0\) and \(S_q'(r)=qz\cosh(qr)>0\). At \(r=-1\), \(S_q(-1)=0<C_q(-1)=(1-z)^2\); at \(r=0\), \(C_q(0)=(1-z)^2/2<S_q(0)=(1-z^2)/2\). Hence the maximum of these two curves has exactly one minimizer on \([-1,0]\), their crossing. The difference identity gives \(e^{-qr_*}=2-z\), so

\[
 r_*=-\log(2-z)/q.
\]

This lies strictly between \(-1\) and \(0\): \(2-z>1\), while \(2-z<1/z=e^q\) is equivalent to \((1-z)^2>0\). For \(r>0\), \(S_q(r)>S_q(0)>S_q(r_*)\), and thus the positive-correlation half interval cannot contain another minimizer. Substituting \(e^{-qr_*}=2-z\) yields

\[
 C_q(r_*)=S_q(r_*)=\frac{(1-z)^2}{2-z},
\]

which proves the stated exact minimax variance and uniqueness, including both endpoints in the domain.

For independent increments, \(\max_\phi\operatorname{Var}H_{q,0,\phi}=(1-z^2)/4\). For perfect reflection, \(\max_\phi\operatorname{Var}H_{q,-1,\phi}=(1-z)^2/2\). Both are strictly greater than \((1-z)^2/[2(2-z)]\) for \(0<z<1\). The reflected-to-optimal ratio is exactly \(2-z\), and reflected versus independent switches order at the unique root \(z=1/3\), namely \(q=\log3\). Finally, Taylor expansion at \(q=0\) gives

\[
 r_*(q)=-1+q-q^2+O(q^3),\quad
 \min_r\max_\phi\operatorname{Var}H_{q,r,\phi}=q^2/2+O(q^3),\quad
 \max_\phi\operatorname{Var}H_{q,0,\phi}=q/2+O(q^2).
\]

As \(q\to\infty\), \(r_*(q)\sim-(\log2)/q\), and the optimal and independent worst-phase variances both tend to \(1/4\), whereas reflected sampling tends to \(1/2\).

## Verification

Run `python verify_fourier.py` using Python 3.9 or later. The standard-library-only checker tests 6,611 grid dominance comparisons for a range of \(q\), analytically predicted endpoint and balancing identities, and 45 independently integrated two-dimensional Gaussian moments using tensor Gauss–Legendre quadrature. Its observed result was `PASS: 6611 grid dominance checks; 45 independent bivariate Gaussian quadratures; all limits and endpoint inequalities checked`. These numerical tests are supplementary; the proof above establishes the statements for every real \(q>0\), every \(r\in[-1,1]\), and every phase.

## Relationship to prior work

Abkin and Daripa (2026) motivate sign-dependent reflected/synchronous Brownian coupling in signed gradient-particle convection–diffusion solvers. Their reported optimality concerns contributions to a reconstructed spatial field \(U(x)\) at the last diffusion stage for a fixed particle matching. The present result instead minimizes the worst-phase variance of a *real Fourier-mode heat estimator* over the full Gaussian-correlation interval; the field-level pointwise sign rule does not by itself imply this Fourier-mode minimax formula. The source paper's full text was not obtainable for exhaustive priority comparison, so this distinction is made only to the extent supported by accessible primary metadata/abstract and a secondary analysis.

Classical antithetic variates explain why reflection reduces variance for monotone observables but may fail for even or oscillating observables; those general facts do not supply this exact unique interior correlation. Chattopadhyay, Liu and Panigrahi (2026) study antithetic Gaussian randomization for cross-validation in a different smooth-estimator asymptotic regime, and Singh (2019) studies correlated importance sampling in Fourier analysis. No inspected accessible statement gives the displayed finite-\(q\), unknown-phase minimax law. Historical priority remains provisional.

## Limitations

The estimator is for one real Fourier frequency at a single spatial point with two Gaussian heat displacements; superpositions, nonlinear particle dynamics, position matching, non-Gaussian couplings, phase-dependent choices of \(r\), and multidimensional or multistep effects are not covered. The result is a worst-phase variance design benchmark, not a claim that Monte Carlo is preferable to evaluating the explicitly known Fourier heat multiplier. The optimal interior correlation requires two Gaussian inputs instead of the single input sufficient for exact reflection. No full-text exclusion of equivalent older formulas or appendices of the motivating paper was possible; independent external mathematical audit has not been performed.

## References

1. S. Abkin and P. Daripa, *Sign-Switched Antithetic Coupling for Signed Gradient-Particle Methods*, arXiv:2610.01120, submitted 2026-10-01, https://arxiv.org/abs/2610.01120.
2. S. Chattopadhyay, S. Liu and S. Panigrahi, *On the optimality of antithetic randomization for cross-validation*, arXiv:2608.08089, 2026-08-08, https://arxiv.org/abs/2608.08089.
3. G. Singh et al., *Fourier Analysis of Correlated Monte Carlo Importance Sampling*, Computer Graphics Forum (2019), https://doi.org/10.1111/cgf.13613.
4. *Antithetic variates*, basic method and covariance identities, https://en.wikipedia.org/wiki/Antithetic_variates (background only).
