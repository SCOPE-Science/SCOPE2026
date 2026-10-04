# Yogi has an exact arithmetic locking law under constant-magnitude gradients
## Finding

Yogi replaces Adam's multiplicative second-moment update by an additive sign-controlled update. Under a constant gradient, that rule has an exact arithmetic phase distinction: finite exact locking or a permanent two-cycle.

For one coordinate of source-form Yogi Algorithm 2,
\[
m_t=eta_1m_{t-1}+(1-eta_1)g_t,
\]
\[
v_t=v_{t-1}-(1-eta_2)\operatorname{sign}(v_{t-1}-g_t^2)g_t^2,
\]
\[
x_{t+1}=x_t-\etarac{m_t}{\sqrt{v_t}+arepsilon}.
\]
Assume \(v_0=0\), \(0\leeta_1<1\), \(0<eta_2<1\), \(\eta>0\), \(arepsilon>0\), \(\operatorname{sign}(0)=0\), and \(g_t=G
e0\) for every \(t\).

Set
\[
s=1-eta_2,\qquad q=rac1s.
\]

If \(q=N\in\mathbb N\), then
\[
v_t=t\,sG^2\quad(0\le t\le N),
\]
and
\[
v_t=G^2\quad(t\ge N).
\]
Thus the second moment reaches the target exactly in \(N\) steps.

If \(q
otin\mathbb N\), write
\[
N=\lfloor qfloor,\qquad \phi=q-N\in(0,1).
\]
Then
\[
v_N=G^2[1-\phi s]=:v_-<G^2,
\]
\[
v_{N+1}=G^2[1+(1-\phi)s]=:v_+>G^2,
\]
and \(v_-,v_+,v_-,v_+,\ldots\) repeat forever. The exact cycle width is
\[
v_+-v_-=(1-eta_2)G^2.
\]

The first moment is
\[
m_t=(1-eta_1^t)G.
\]
Hence in the locking case the update magnitude tends to
\[
rac{\eta|G|}{|G|+arepsilon},
\]
whereas in the nonlocking case it approaches the two values
\[
rac{\eta|G|}{\sqrt{v_-}+arepsilon}
\quad	ext{and}\quad
rac{\eta|G|}{\sqrt{v_+}+arepsilon}.
\]

The source reports successful choices
\[
eta_2\in\{0.9,0.99,0.999\}.
\]
These satisfy
\[
(1-eta_2)^{-1}\in\{10,100,1000\},
\]
so each lies exactly on the finite-locking family.

For Adam under the same constant gradient,
\[
v_t^{m Adam}=eta_2v_{t-1}^{m Adam}+(1-eta_2)G^2,
\]
so
\[
v_t^{m Adam}=G^2(1-eta_2^t),
\]
which converges geometrically for every \(0<eta_2<1\). The arithmetic locking-versus-cycle distinction is therefore specific to Yogi's fixed-magnitude sign update.

## Assumptions and scope

The theorem concerns the displayed source Yogi Algorithm 2 recurrence.

The constant gradient is an optimizer input-response diagnostic; it is not asserted to be the gradient trajectory of a coercive objective with a minimizer.

The standard convention \(\operatorname{sign}(0)=0\) is used.

The source form omits Adam-style debiasing in the displayed algorithm; the theorem analyzes that recurrence exactly.

No global optimization convergence claim is made.

## Proof

Normalize \(y_t=v_t/G^2\). Then
\[
y_0=0,\qquad
y_t=y_{t-1}-s\operatorname{sign}(y_{t-1}-1).
\]

While \(y_{t-1}<1\), the state increases by exactly \(s\), so \(y_t=ts\) until it reaches or first crosses \(1\).

If \(q=1/s=N\in\mathbb N\), then \(y_N=1\). Since the sign vanishes there, the state remains exactly \(1\).

If \(q=N+\phi\) with \(0<\phi<1\), then
\[
y_N=Ns=1-\phi s<1.
\]
The next step adds \(s\):
\[
y_{N+1}=1+(1-\phi)s>1.
\]
The following step subtracts exactly \(s\), returning to \(y_N\). Determinism then forces the two-cycle forever.

The first-moment recurrence with constant forcing solves to \(m_t=(1-eta_1^t)G\), giving the update-magnitude limits.

Adam's comparison follows by solving its scalar linear second-moment recurrence.

## Verification

The accompanying `verify.py` directly replays the scalar Yogi and Adam recurrences. It checks finite locking, nonlocking two-cycles, the exact cycle width, the reported \(eta_2\) grid, and the asymptotic update magnitudes.

These numerical checks are transcription guards; the complete classification is proved analytically above.

## Relationship to prior work

Zaheer, Reddi, Sachan, Kale, and Kumar introduced Yogi as an additive alternative to Adam. Their paper emphasizes that the magnitude of Yogi's second-moment change depends only on the current squared gradient, in contrast with Adam's multiplicative relaxation, and motivates this as a way to control effective-learning-rate changes.

The defining full text does not state the constant-gradient arithmetic classification, the finite exact-lock criterion
\[
(1-eta_2)^{-1}\in\mathbb N,
\]
or the persistent two-cycle for all other values. Focused published-record and web searches for Yogi constant-gradient cycles, second-moment oscillation, and equivalent locking conditions did not identify an implication-equivalent result.

The paper's practical discussion reports \(eta_2\in\{0.9,0.99,0.999\}\) as useful values; all three happen to lie on the exact-locking set.

## Limitations

The input is deliberately simple and isolates second-moment mechanics.

The result does not imply a parameter-space limit cycle on a fixed nonlinear objective.

Finite-precision arithmetic can perturb exact locking.

The practical grid lying on the locking family is an arithmetic observation, not a claim of deliberate design.

## References

1. Manzil Zaheer, Sashank J. Reddi, Devendra Singh Sachan, Satyen Kale, and Sanjiv Kumar, “Adaptive Methods for Nonconvex Optimization,” Advances in Neural Information Processing Systems 31, 2018.
