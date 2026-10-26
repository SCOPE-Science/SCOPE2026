# Near-neutral interaction scaling of the first phase threshold

## Finding

For the symmetric three-colour interacting nonlinear urn with matrix entries \(A(a)_{ii}=1\) and \(A(a)_{ij}=a\in(0,1)\) for \(i\ne j\), let
\[
P_{a,\beta}(z)=az^{\beta+1}-z^\beta+(1+a)z-2a
\]
and let \(\beta_1(a)\) be the lower phase threshold in Proposition 3.3 of Costa and Jordan, where two additional stationary-point roots greater than \(1\) first appear. Then
\[
\lim_{a\uparrow1}(1-a)\beta_1(a)=\lambda_*,\qquad
\lambda_* = \min_{0<s<1}\frac{1}{s}\log\frac{1+2s}{1-s}=2.745643576732724\ldots.
\]
The minimizer \(s_*\in(1/4,1)\) is the unique solution of
\[
\log\frac{1+2s_*}{1-s_*}=\frac{3s_*}{(1+2s_*)(1-s_*)},
\]
and \(\lambda_*=3/((1+2s_*)(1-s_*))\).

## Assumptions and scope

The model has three colours and symmetric interaction matrix with diagonal entries \(1\) and common off-diagonal entry \(a\in(0,1)\). The reinforcement exponent is \(\beta>0\). The claim concerns the first threshold for additional stationary points in the associated mean-field vector field, not a new almost-sure convergence theorem for the urn trajectories. The first public version of the source paper appeared on 2020-06-04.

## Proof

Write \(\delta=1-a\), so \(\delta\downarrow0\). Costa and Jordan define \(\beta_1(a)\) through the appearance of additional roots of \(P_{a,\beta}\); their Proposition 3.3 also gives \(\beta_1(a)<(1+2a)/(1-a)\). For \(1<z<1/a\),
\[
\frac{\partial P_{a,\beta}(z)}{\partial\beta}=(az-1)(\log z)z^\beta<0.
\]
Consequently, the first appearance of roots in this interval is the infimum of the exponents obtained by solving \(P_{a,\beta}(z)=0\) for each fixed \(z\in(1,1/a)\). Rearranging gives
\[
z^\beta=\frac{(1+a)z-2a}{1-az}.
\]
Put \(z=1+\delta s\), so \(0<s<1/a=1/(1-\delta)\). The last equation becomes
\[
(1+\delta s)^\beta=\frac{1+(2-\delta)s}{1-(1-\delta)s}.
\]
Thus, defining
\[
G_\delta(s)=\frac{\delta}{\log(1+\delta s)}
\log\frac{1+(2-\delta)s}{1-(1-\delta)s},
\]
we have the exact variational identity
\[
\delta\beta_1(1-\delta)=\inf_{0<s<1/(1-\delta)}G_\delta(s).
\]
On every compact subinterval of \((0,1)\), \(G_\delta\) converges uniformly to
\[
L(s)=\frac1s\log\frac{1+2s}{1-s}.
\]
The boundary regimes cannot minimize in the limit: jointly as \(\delta\downarrow0\) and \(s\downarrow0\), \(G_\delta(s)\to3\); as \(s\) approaches \(1\) from within its varying domain, \(G_\delta(s)\to\infty\). Since, for example, \(L(2/5)<3\), minimizers stay in a compact subset of \((0,1)\) for all sufficiently small \(\delta\). Uniform convergence there therefore implies
\[
\lim_{\delta\downarrow0}\delta\beta_1(1-\delta)=\min_{0<s<1}L(s).
\]

It remains to identify the minimum. Let
\[
f(s)=\log\frac{1+2s}{1-s},\qquad
f'(s)=\frac{3}{(1+2s)(1-s)},\qquad
f''(s)=\frac{3(4s-1)}{(1+2s)^2(1-s)^2}.
\]
The sign of \(L'(s)\) is the sign of \(h(s)=sf'(s)-f(s)\). Since \(h'(s)=sf''(s)\), the function \(h\) decreases on \((0,1/4)\) from \(h(0)=0\), then increases strictly on \((1/4,1)\) to \(+\infty\). It therefore has exactly one zero \(s_*\in(1/4,1)\), which is the unique minimizer of \(L\). At this zero, \(f(s_*)=s_*f'(s_*)\), yielding the stated equation and \(\lambda_*=f'(s_*)\). The accompanying standard-library script reproduces the numerical value of \(s_*\) and \(\lambda_*\); the limit itself follows from the analytic argument, not from numerical sampling.

## Verification

The polynomial is rearranged exactly, with no approximation, before the rescaling \(z=1+(1-a)s\). The rescaled threshold identity follows from the sign of \(\partial_\beta P_{a,\beta}\) on \((1,1/a)\) and the definition of the first root-appearance threshold. Uniform convergence on compact subsets plus the explicit endpoint limits justifies passing the infimum to the limit. The derivative calculation proves uniqueness of the limiting minimizer. Run `python verify.py` to reproduce the displayed decimal root and constant; this script checks only the numerical evaluation, not the infinite-parameter limit. No finite simulation is used as proof.

## Relationship to prior work

Costa and Jordan, Proposition 3.3, establish the existence and monotonicity of \(\beta_1(a)\), prove that it diverges as \(a\uparrow1\), and bound it between a lower bound exceeding \(2/(1-a)-1\) and the upper threshold \((1+2a)/(1-a)\). Those explicit coarse bounds put the scaled threshold between the limiting endpoints \(2\) and \(3\). The same proof defines an auxiliary lower bound \(\beta_0(a)\) by equation (25); taking logarithms shows \((1-a)\beta_0(a)\to2+\log2\approx2.693147\), which is still below \(\lambda_*\) and is only a lower bound for \(\beta_1(a)\). Thus it does not identify the threshold's sharp leading coefficient. It does not claim the urn model, its phase diagram, or the polynomial as new. Nakayama and Mori study a binary feedback urn and critical autocorrelation scaling; their state space and order parameter differ from the three-colour symmetric-interaction root threshold treated here.

## Limitations

Only the leading-order limit of the lower threshold is established; no second-order expansion or closed form for \(\beta_1(a)\) at fixed \(a\) is claimed. The argument concerns the symmetric three-colour stationary-point polynomial and does not extend the phase classification to more colours or alter the source paper's trajectory-level conclusions. The numerical constant is given by a unique transcendental minimizer, not an elementary closed form. Unindexed literature on asymptotics of bifurcation thresholds remains a residual priority risk.

## References

1. M. Costa and J. Jordan, “Phase transitions in non-linear urns with interacting types,” *Bernoulli* 28(4) (2022), 2546–2562. First public version: 2020-06-04. arXiv:2006.02685; DOI: 10.3150/21-BEJ1428.
2. K. Nakayama and S. Mori, “Universal function of the nonequilibrium phase transition of a nonlinear Pólya urn,” *Physical Review E* 104 (2021), 014109. DOI: 10.1103/PhysRevE.104.014109.
