# Self-review

## Correctness
PASS. The first direct BFGS update acts only on the two-dimensional space
\[
\operatorname{span}\{s,Hs\}.
\]
Its active block has determinant
\[
q=s^{\mathsf T}Hs
\]
and trace
\[
q+1+\frac{m^2}{q},
\qquad
m^2=s^{\mathsf T}H^2s-q^2.
\]
The sharp endpoint spectral inequality gives
\[
m^2\le(q-1)(\kappa-q).
\]
This reduces the full problem to a one-variable maximization with unique optimizer
\[
q_*=\frac{3\kappa}{\kappa+2}.
\]
Endpoint eigenspace support realizes equality, and solving the resulting trace-determinant relation gives the stated closed form. The strict comparison with \(\kappa\) follows from an exact positive factorization. The packaged checker replays the algebra and the \(\kappa=4\) witness.

## Originality
PASS with stated residual risks. Conditioning of quasi-Newton approximations, sizing, and self-scaling are established literature and are explicitly treated as prior work. The closest full conditioning source notes that low-rank updates can become ill-conditioned and develops scaling remedies. Powell's full two-dimensional study analyzes the complementary regime of identity true Hessian with a poor current Hessian approximation.

The final statement instead starts from the identity approximation and optimizes the condition number of the first ordinary BFGS update over true SPD Hessians of fixed condition number. Targeted statement-level searches and the inspected full texts did not expose the function
\[
\Gamma(\kappa)
\]
or the theorem that it strictly exceeds \(\kappa\) for every \(\kappa>1\).

A specific residual risk remains because the full body of Shanno's 1970 conditioning paper was not retrievable in this run.

## Value
PASS. The result quantifies a concrete conditioning cost of an exact BFGS curvature update before asymptotic recovery. It shows that positive definiteness and exact secant information do not prevent the approximate Hessian from becoming less well conditioned than the true one, and that the worst first-update conditioning grows quadratically with the problem condition number. This directly motivates the historical emphasis on scaling and conditioning safeguards.

## Closest literature and limitations
The closest sources are the classical quasi-Newton conditioning and sizing literature, Powell's two-dimensional quadratic BFGS analysis, and a full archive-era review of the standard BFGS matrix update. The theorem is one-step and assumes minimum-curvature scalar normalization of the initial identity; later BFGS updates and other initial scalings are not classified.

Self-review: passed. Independent audit: not yet performed.
