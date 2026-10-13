# Self-review

## Correctness
PASS. The diagonal quadratic decouples into scalar heavy-ball modes. With Polyak's classical optimal parameters, the normalized modal error has the exact form
\[
e_k=-q^k\left(U_k(t)-qU_{k-1}(t)\right),
\]
where \(t\in[-1,1]\). The standard inequality \(|U_k(t)|\le k+1\) gives, for \(q\le1/2\) and \(k\ge2\),
\[
|e_k|\le\frac{3k+2}{2^{k+1}}\le1.
\]
The first iterate is directly nonnegative. At the largest-curvature endpoint,
\[
\frac{x_2}{x^\star}=(1+q)^2(1-2q),
\]
so \(q=1/2\), equivalently \(\kappa=9\), is both necessary and sufficient. The embedded rational verifier reproduces the threshold and strict-failure examples.

## Originality
PASS. The closest archive-era primary papers establish the heavy-ball recurrence, classical optimal quadratic tuning, and rate/stability analyses. Later work explicitly studies peak effects and quadratic oscillations. None of the inspected statements implies an all-iterate componentwise positivity classification for positive diagonal quadratics, and targeted searches for positivity, orthant invariance, sign change, and the condition-number-nine threshold found no implication-equivalent result.

The strongest residual risk is terminology mismatch with older momentum or stationary two-step literature, plus incomplete full-text access to one peak-effect paper.

## Value
PASS. Whole-trajectory positivity is a natural requirement when the variables themselves represent nonnegative quantities. The result gives an exact feasibility frontier for the canonical optimally tuned momentum method, not merely a numerical overshoot example: \(\kappa\le9\) is sufficient for every iterate, and \(\kappa>9\) fails immediately in an active largest-curvature coordinate.

## Closest literature and limitations
Ghadimi--Feyzmahdavian--Johansson provide the archive-era method definition and classical optimal quadratic context. Lessard--Recht--Packard provide a broader heavy-ball stability analysis. Danilova--Malinovskiy and Orvieto make transient oscillation and peak effects explicit motivations. The present claim is restricted to positive diagonal Hessians, zero initial velocity, exact optimal quadratic parameters, and exact arithmetic.

Self-review: passed. Independent audit: not yet performed.
