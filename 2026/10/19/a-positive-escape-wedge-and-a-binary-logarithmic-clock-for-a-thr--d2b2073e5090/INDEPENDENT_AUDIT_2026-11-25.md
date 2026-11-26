# Independent mathematical audit

## correctness

PASS

PASS applies only to /workspace/repairs/1/RESULT.md. Frozen correctness FAIL: choose a=1/2, b=k=β=k1=1, k2=α=k0=c=0, Y=0, Φ=−2, R=3. Then K=1, B=9/4 and all frozen inequalities hold. But (4,−1,0) lies in the frozen wedge and maps to activation 16e^(−5)<3, violating forward invariance and growth. The repair expressly requires Φ>0. Now 3kβφ²>4 gives x'>3x, y'<Y by recovery and Kx≤φ'≤k1x<3Kx<Kx' by flux. This supplies Kx_{n−1}≤φ_n≤k1x_{n−1}, the delayed lower bound B x_n x_{n−1}², and hence x_n/x_{n−1}→∞. The shifted recovery is O(1+x_{n−2}), and the previous flux O(x_{n−2}); dividing their updates by x_{n−1} proves the two stated lag limits. Dividing the activation by x_n x_{n−1}² leaves precisely A in the limit, because y_n<Y suppresses the exponential. In the logarithmic recurrence the exact projection 2^(−n)(z_n+z_{n−1}) has summable increments; inversion on the other component is a contraction with signed coefficient −1/2 after normalization. The B-shifted lower comparison starts with two strictly positive values and the homogeneous roots are 2 and −1, giving H≥(log x0+log x1+log B)/3>0. Monotone two-sided bounds on log x_n then give the bounded-error hitting clock. The frozen code always chooses the positive square root for Φ, so its recorded 36 finite steps and nine lag-ratio triplets cannot address the original defect and are not a convergence proof. It was inspected, not executed.

## originality

PASS

The repaired finding concerns the full, quadratic-memductance three-coordinate map and establishes an explicit positive-flux invariant wedge with a binary logarithmic growth clock. Its recurrence is published and numerical escape was known. In the inspected primary and indexed statements, neither that escape region nor the orbitwise lag asymptotics are already covered. Priority beyond the bounded search is not established.

## value

PASS

For the repaired range this settles real divergence and its precise logarithmic scale on a natural explicit open set for a published model. It explains why the true live-flux lag has binary rather than instantaneous cubic scaling. This distinguishes mathematical escape from numerical overflow without purporting to classify the entire basin.

The dated certificate retains the supplied scientific assessment, sources and limitations.
