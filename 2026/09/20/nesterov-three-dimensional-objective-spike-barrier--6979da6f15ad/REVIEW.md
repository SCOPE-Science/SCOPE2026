# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** In an eigenbasis, the stated Nesterov iteration reduces exactly to
\[
p_{k+1}(t)=(1-t)((1+\beta)p_k(t)-\beta p_{k-1}(t)),
\]
with \(p_0=1\) and \(p_1=1-t\). For exact spectral calibration,
\(q=\sqrt{\mu/L}\) and \(\beta=(1-q)/(1+q)\). At \(t=q^2\), substitution
reduces the characteristic polynomial to a double root at \(1-q\), giving
\(p_k(q^2)=(1+kq)(1-q)^k\). Its consecutive ratio is strictly below one.
At \(t=1\), all components vanish after the first step. Hence an endpoint-only
spectrum is objective-monotone, and this covers every two-dimensional SPD matrix
when \(\mu,L\) are the exact endpoints.

The step-two polynomial factors as
\[
p_2(t)=(1-t)(1-(1+\beta)t),
\]
so its interior zero is \(t_*=(1+q)/2\). Substitution in the recurrence gives
\(p_3(t_*)=-(1-q)^3/[4(1+q)]\), proving exact annihilation at step two and
revival at step three. Combining this middle mode with an \(\varepsilon\)-sized
low-curvature endpoint component yields a strictly positive step-two objective
of order \(\varepsilon^2\), while the revived step-three component has a
nonzero limit. The displayed exact formulas therefore imply
\(f(x_3)/f(x_2)=\Theta(\varepsilon^{-2})\). This also neutralizes the possible
objection that an exact hit of the minimizer would trigger termination.

Boundary cases were checked. When \(\kappa=1\), the method reduces to a single
gradient step to the minimizer, so the dimension-three construction correctly
requires \(\kappa>1\). The witness has exact eigenvalues \(\mu\),
\((L+\sqrt{\mu L})/2\), and \(L\), hence exact condition number \(\kappa\).
The claim is a local relative-objective statement and does not conflict with
global accelerated convergence. Deterministic numerical checks reproduced all
closed forms and found no endpoint-spectrum monotonicity violation in rotated
tests. Numerical evidence is supporting evidence only; the proof is analytic.

## Originality

**PASS, to the best of our knowledge.** Nesterov's classical work gives the
accelerated method and global rate. O'Donoghue and Candes establish the practical
importance of oscillation and restart criteria, including function-based restart.
Hagedorn and Jarre provide an accessible theorem-level spectral treatment of
fixed-step Nesterov acceleration on strongly convex quadratics and explicitly
study nonmonotone low-dimensional momentum behavior. Their Nesterov analysis
contains the modal recurrence framework relevant to the present proof but does
not state a sharp minimum dimension for objective increase, the step-two interior
annihilation node, or an unbounded positive-denominator local objective ratio.

Current-status checks included Bach's 2026 z-transform analysis of Nesterov-type
quadratic acceleration and recent 2025-2026 acceleration/restart literature.
Searches used synonymous formulations involving function-value monotonicity,
objective overshoot, spectral polynomials, modal roots, low-dimensional examples,
and restart. No checked source states the combined result proved here.

Residual originality risk remains because the literature on semi-iterative
methods, polynomial acceleration, and momentum is extensive, and some older
sources were not inspected theorem by theorem. The interior-root identity is
elementary once the recurrence is written down, so historical equivalence under
different terminology cannot be excluded.

## Value

**PASS.** The result refines the broad statement that acceleration can oscillate
into an exact structural threshold. Under perfect spectral calibration, two
curvature endpoints alone cannot make the objective rise, while one additional
interior curvature mode can do so for every nontrivial condition number. The
same three-dimensional construction shows that no condition-number-only bound
on the local relative objective spike exists. This sharply separates global
accelerated convergence from stepwise descent and gives a concrete spectral
mechanism for the usefulness of restart and monotonicity safeguards.

## Scientific limitations

The theorem assumes exact arithmetic, real SPD quadratics, exact spectral
endpoints, classical strongly-convex constant Nesterov momentum, and standard
zero-momentum initialization. Loose endpoint estimates, arbitrary initial
momentum states, alternate Nesterov formulations, convex time-varying coefficient rules,
FISTA, heavy-ball, composite objectives, adaptive or restarted schemes,
stochastic gradients, and finite precision are outside the claim. The unbounded
quantity is a local relative ratio caused by the previous objective becoming
arbitrarily small; no absolute blow-up or divergence is claimed. Historical
prior-coverage uncertainty remains as described above. Independent audit has
not been performed.
