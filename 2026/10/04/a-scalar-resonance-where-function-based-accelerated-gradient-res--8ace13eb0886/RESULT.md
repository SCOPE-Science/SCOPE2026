# A scalar resonance where function-based accelerated-gradient restart never fires

## Finding
Consider the scalar quadratic
\[
f(x)=\frac{5L}{16}x^2,\qquad L>0,
\]
so its curvature is \(\lambda=5L/8\). Apply the fixed-step, fixed-momentum accelerated-gradient model used in the quadratic analysis of O'Donoghue and Candes, with step \(1/L\), momentum \(\beta=1/3\), and initialization \(y^0=x^0\neq0\). Then the mode is genuinely under-damped, but the strict function-based restart rule never activates. In contrast, the gradient-based restart rule activates on the third computed point.

More precisely,
\[
x^1=\frac38x^0,\qquad
x^{k+1}=\frac12x^k-\frac18x^{k-1}\quad(k\ge1),
\]
and
\[
x^{k+4}=-\frac1{64}x^k\quad(k\ge0).
\]
The consecutive magnitude ratios therefore repeat
\[
\frac38,\quad\frac16,\quad\frac14,\quad1.
\]
Hence \(f(x^{k+1})\le f(x^k)\) for every \(k\), with equality once per four updates, so the strict function-restart condition \(f(x^{k+1})>f(x^k)\) is never satisfied. The gradient-restart quantity is already positive for the update producing \(x^3\).

## Assumptions and scope
The claim concerns the exact constant-momentum scalar quadratic model analyzed in Section 4 of O'Donoghue--Candes, not the full varying-momentum FISTA/Nesterov sequence. Their analysis explicitly fixes the step at \(1/L\) and then treats \(\beta_k\) as a constant \(\beta\) to study high- and low-momentum modes.

The function restart is interpreted with the strict inequality proposed in that work: restart after computing \(x^{k+1}\) if \(f(x^{k+1})>f(x^k)\). The gradient restart is the scalar specialization of \(\nabla f(y^k)^\top(x^{k+1}-x^k)>0\).

## Proof
Because \(\lambda/L=5/8\), one gradient step from \(y^k\) gives
\[
x^{k+1}=\left(1-\frac{\lambda}{L}\right)y^k=\frac38y^k.
\]
With \(\beta=1/3\),
\[
y^k=x^k+\frac13(x^k-x^{k-1})=\frac43x^k-\frac13x^{k-1},
\]
so
\[
x^{k+1}=\frac12x^k-\frac18x^{k-1}.
\]
The initial step has no momentum, hence \(x^1=3x^0/8\). Direct substitution gives
\[
x^2=\frac1{16}x^0,\qquad
x^3=-\frac1{64}x^0,\qquad
x^4=-\frac1{64}x^0.
\]

The characteristic polynomial is
\[
r^2-\frac12r+\frac18,
\]
with roots
\[
r_\pm=\frac{1\pm i}4=\frac1{2\sqrt2}e^{\pm i\pi/4}.
\]
Thus \(r_\pm^4=-1/64\), and every solution obeys
\[
x^{k+4}=-\frac1{64}x^k.
\]
Combining this four-step scaling with the first block yields the repeating magnitude ratios
\[
\left|\frac{x^1}{x^0}\right|=\frac38,\quad
\left|\frac{x^2}{x^1}\right|=\frac16,\quad
\left|\frac{x^3}{x^2}\right|=\frac14,\quad
\left|\frac{x^4}{x^3}\right|=1.
\]
Since \(f\) is a positive multiple of \(x^2\), its value never increases. Therefore the strict function restart never occurs.

The roots are nonreal, so this is exactly the under-damped/high-momentum regime of the source analysis. Equivalently, the critical momentum for \(\lambda/L=5/8\) is
\[
\beta^\star=\frac{1-\sqrt{5/8}}{1+\sqrt{5/8}}<\frac13.
\]

For the gradient restart, \(x^{k+1}=(3/8)y^k\) implies
\[
\nabla f(y^k)=\frac{5L}8y^k=\frac{5L}3x^{k+1},
\]
so the restart quantity has the sign of
\[
x^{k+1}(x^{k+1}-x^k).
\]
It is negative for the first two updates, while for the third,
\[
x^3(x^3-x^2)=\left(-\frac1{64}x^0\right)\left(-\frac5{64}x^0\right)>0.
\]
Thus the gradient criterion first triggers at \(k=2\), after \(x^3\) is computed.

## Verification
The accompanying `check.py` uses exact rational arithmetic to generate the recurrence, verifies the first block and the identity \(x^{k+4}=-x^k/64\) over many blocks, checks that no objective increase occurs, and checks that the first positive gradient-restart sign occurs at the update producing \(x^3\). It also verifies that the characteristic discriminant is negative.

## Relationship to prior work
O'Donoghue and Candes (arXiv:1204.3982; later Foundations of Computational Mathematics) introduce the function and gradient adaptive-restart rules and analyze exactly the constant-\(\beta\) quadratic mode used here. Their high-momentum analysis replaces exact phase information by approximations and states that under either rule one expects a restart after roughly a quarter oscillation period. The scalar resonance above keeps the objective nonincreasing forever, so it is an exact exception to that heuristic timing statement, while the gradient rule still detects the oscillation promptly.

Fercoq and Qu (arXiv:1609.07358) subsequently emphasize that the original adaptive condition is heuristic and report an accelerated-proximal-gradient experiment in which an adaptive restart condition did not occur within the first 10,000 iterations. Their work develops forced/periodic safeguards and does not provide this scalar exact mechanism. The present calculation therefore supplies a minimal closed-form explanation of how a strict objective-increase detector can be blind despite an under-damped mode.

Targeted published-finding corpus searches for adaptive-restart blind spots, scalar quadratic objective-monotonic under-damped modes, and function-versus-gradient restart equivalence returned no implication-equivalent published finding. The closest indexed results concern objective spikes in multi-mode Nesterov acceleration and unrelated monotonicity frontiers.

## Limitations
This is a sharp counterexample inside the constant-momentum model used for the source paper's quadratic heuristic; it is not a claim that the varying-momentum accelerated scheme with \(q=0\) will never function-restart on this same scalar quadratic. The no-trigger phenomenon also relies on the strict inequality in the function test: replacing the trigger by a non-strict comparison would restart at the equality transitions, though such a rule can be sensitive to floating-point noise. The result does not by itself quantify how long a nearby nonresonant parameter choice can delay a function restart.

## References
1. B. O'Donoghue and E. Candes, *Adaptive Restart for Accelerated Gradient Schemes*, arXiv:1204.3982, first submitted 2012-04-18; DOI 10.1007/s10208-013-9150-3.
2. O. Fercoq and Z. Qu, *Restarting accelerated gradient methods with a rough strong convexity estimate*, arXiv:1609.07358, first submitted 2016-09-23.
