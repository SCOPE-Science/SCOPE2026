# FedAvgM has a sharp two-period workload resonance
## Finding

FedAvgM was introduced by adding server momentum to Federated Averaging. Its original update is
\[
v_{t+1}=\beta v_t+\Delta_t,
\qquad
x_{t+1}=x_t-v_{t+1},
\qquad
0\le \beta<1,
\]
where \(\Delta_t\) is the aggregated client model difference.

Consider identical scalar quadratic client objectives
\[
f_i(x)=\frac a2x^2,
\qquad a>0.
\]
Let one local gradient step use learning rate \(\eta_l\) and define
\[
q=1-\eta_l a,
\qquad
|q|<1.
\]
Thus every individual local gradient step is contractive.

If each participating client performs \(K_t\ge1\) local steps during round \(t\), then its returned model is
\[
q^{K_t}x_t,
\]
so the aggregate model difference is
\[
\Delta_t=(1-q^{K_t})x_t.
\]
Eliminating the momentum variable gives
\[
x_{t+1}
=
(\beta+q^{K_t})x_t-\beta x_{t-1}.
\]
Hence
\[
\begin{bmatrix}
x_{t+1}\\
x_t
\end{bmatrix}
=
M_{K_t}
\begin{bmatrix}
x_t\\
x_{t-1}
\end{bmatrix},
\qquad
M_K=
\begin{bmatrix}
\beta+q^K&-\beta\\
1&0
\end{bmatrix}.
\]

For every fixed workload \(K\), this matrix is Schur stable. Indeed its characteristic polynomial is
\[
z^2-(\beta+q^K)z+\beta,
\]
and the three second-order Jury inequalities reduce to
\[
1-q^K>0,
\qquad
1+2\beta+q^K>0,
\qquad
1-\beta>0.
\]

Now alternate two workloads:
\[
K_1,K_2,K_1,K_2,\ldots.
\]
The two-round monodromy matrix is
\[
P=M_{K_2}M_{K_1}.
\]
It has
\[
\det P=\beta^2
\]
and
\[
\operatorname{tr}P
=
(\beta+q^{K_1})(\beta+q^{K_2})-2\beta.
\]
The Jury conditions for \(P\) simplify to
\[
(1+\beta)^2-(\beta+q^{K_1})(\beta+q^{K_2})>0,
\]
\[
(1-\beta)^2+(\beta+q^{K_1})(\beta+q^{K_2})>0,
\]
and
\[
1-\beta^2>0.
\]
The first and third inequalities hold automatically because
\[
|q|<1
\]
and
\[
0\le\beta<1.
\]
Therefore the exact two-period stability criterion is
\[
\boxed{
(\beta+q^{K_1})(\beta+q^{K_2})
>
-(1-\beta)^2.
}
\]

Equality is the sharp boundary where the two-round monodromy has eigenvalue
\[
-1.
\]

For the particularly natural alternation
\[
K_1=1,
\qquad
K_2=2,
\]
the boundary is
\[
q^3+\beta q^2+\beta q+1-2\beta+2\beta^2=0.
\]
For every
\[
0<\beta<1,
\]
this cubic is strictly increasing in \(q\), because its derivative
\[
3q^2+2\beta q+\beta
\]
has negative discriminant. Its value at \(q=-1\) is
\[
-2\beta(1-\beta)<0,
\]
whereas its value at \(q=0\) is positive. Thus there is a unique
\[
q_\beta\in(-1,0)
\]
such that alternating one and two local steps is unstable for
\[
-1<q<q_\beta.
\]
So every positive amount of server momentum admits a locally contractive overshoot regime in which periodic local work destabilizes the global iteration.

An exact witness is
\[
\beta=\frac12,
\qquad
q=-\frac45,
\qquad
K_1=1,
\qquad
K_2=2.
\]
For the one-step workload,
\[
\beta+q=-\frac3{10},
\]
and for the two-step workload,
\[
\beta+q^2=\frac{57}{50}.
\]
Each frozen-workload characteristic polynomial has complex roots of modulus
\[
\sqrt{\beta}=\frac1{\sqrt2}<1.
\]

But
\[
(\beta+q)(\beta+q^2)
=
-\frac{171}{500}
<
-\frac14
=
-(1-\beta)^2,
\]
so the alternating system is unstable. Its two-round monodromy has
\[
\operatorname{tr}P=-\frac{671}{500},
\qquad
\det P=\frac14,
\]
and eigenvalues
\[
\frac{-671\pm\sqrt{200241}}{1000}.
\]
Thus its spectral radius is
\[
\boxed{
\frac{671+\sqrt{200241}}{1000}>1.
}
\]

In contrast, with no server momentum,
\[
\beta=0,
\]
the same local-work sequence is simply FedAvg, whose two-round multiplier is
\[
q^{K_1+K_2}
=
\left(-\frac45\right)^3
=
-\frac{64}{125},
\]
so it is strictly stable.

## Assumptions and scope

The result uses the original FedAvgM heavy-ball server rule with server learning rate one.

All participating clients have the same scalar quadratic objective, so the effect is caused by temporal variation in local work rather than data heterogeneity.

Each round uses a common local-step count across participating clients. The count alternates periodically between two positive integers.

The local gradient map is itself contractive:
\[
|1-\eta_l a|<1.
\]
The instability requires the local step to overshoot the minimizer, so
\[
q<0.
\]
If
\[
q\ge0,
\]
then every factor
\[
\beta+q^K
\]
is nonnegative and the displayed two-period resonance cannot occur.

The result is a deterministic linear stability statement. It does not claim instability for the small client learning rates used in sufficient general convergence theorems.

## Proof

The local quadratic recursion is
\[
x_{k+1}^{\mathrm{loc}}
=
x_k^{\mathrm{loc}}-\eta_l a x_k^{\mathrm{loc}}
=
q x_k^{\mathrm{loc}},
\]
so after \(K_t\) local steps,
\[
x_t^{\mathrm{loc}}=q^{K_t}x_t.
\]
The model difference used by FedAvgM is therefore
\[
\Delta_t=x_t-x_t^{\mathrm{loc}}=(1-q^{K_t})x_t.
\]

Because
\[
x_t=x_{t-1}-v_t,
\]
we have
\[
v_t=x_{t-1}-x_t.
\]
Substituting this into
\[
x_{t+1}
=
x_t-\beta v_t-(1-q^{K_t})x_t
\]
gives
\[
x_{t+1}
=
(\beta+q^{K_t})x_t-\beta x_{t-1}.
\]

For a fixed workload, applying the complete quadratic Jury criterion to
\[
z^2-(\beta+q^K)z+\beta
\]
gives the three inequalities displayed in the finding. Since
\[
-1<q^K<1
\]
and
\[
0\le\beta<1,
\]
all three are strict.

For the period-two sequence, multiply the two state matrices. The determinant is
\[
\beta^2
\]
and the trace is
\[
(\beta+q^{K_1})(\beta+q^{K_2})-2\beta.
\]
Applying the same Jury criterion to the monodromy polynomial gives the three displayed inequalities. The only nonautomatic one is
\[
(1-\beta)^2+(\beta+q^{K_1})(\beta+q^{K_2})>0,
\]
which proves the exact criterion.

For
\[
K_1=1,
\qquad
K_2=2,
\]
substitution yields the cubic boundary. Its derivative has discriminant
\[
4\beta^2-12\beta<0
\]
for
\[
0<\beta<1,
\]
so it is strictly increasing and has the unique root claimed.

The rational witness follows by exact substitution.

## Verification

The accompanying `verify.py` reconstructs FedAvgM directly from the server momentum and local-gradient updates.

It verifies the fixed-workload Jury conditions, the exact two-period criterion over many random parameter choices, the unique one-versus-two-step transition, and the exact rational witness.

It also simulates the witness from zero initial server momentum and confirms growth along the unstable two-round mode. These finite calculations are transcription guards only; the stability classification is proved analytically above.

## Relationship to prior work

Hsu, Qi, and Brown introduced FedAvgM by accumulating the aggregated client update in a server momentum buffer. Their experiments use a fixed local-epoch count and note that the local epoch parameter changes the viable effective-learning-rate window. The inspected source does not analyze periodic local-work switching or a two-round monodromy.

Sun, Wu, Huang, and Zhang later identify system heterogeneity and time-varying local computation as an important missing dimension in server-momentum analysis. Their autonomous framework permits time-varying, device-dependent local-step counts, but it also normalizes each client update by its local-step count before aggregation. Its convergence theorem imposes a small client-step condition depending on the maximum local workload. Those choices exclude the raw FedAvgM recurrence and the locally stable overshoot regime analyzed here.

Adaptive federated optimization supplies a broader server-optimizer framework and studies data heterogeneity, but it does not state the exact periodic-workload stability criterion above.

Focused searches for FedAvgM with alternating local epochs, periodic workload switching, server-momentum parametric instability, and switched quadratic heavy-ball dynamics did not identify an implication-equivalent published result.

## Limitations

The theorem concerns identical scalar quadratics and a deterministic two-period workload.

It does not classify arbitrary nonperiodic local-work sequences or higher-dimensional noncommuting Hessians.

The explicit instability uses
\[
\eta_l a=\frac95,
\]
which is locally contractive but deliberately close to the local-gradient stability boundary. Small nonovershooting client steps
\[
0<\eta_l a\le1
\]
do not exhibit this two-period resonance.

Generic switched linear-system theory may contain equivalent matrix-product criteria under different terminology; no such source was identified in the focused searches.

## References

1. Tzu-Ming Harry Hsu, Hang Qi, and Matthew Brown, “Measuring the Effects of Non-Identical Data Distribution for Federated Visual Classification,” arXiv:1909.06335v1, first submitted 2019-09-13.
2. Jianhui Sun, Xidong Wu, Heng Huang, and Aidong Zhang, “On the Role of Server Momentum in Federated Learning,” arXiv:2312.12670v1, first submitted 2023-12-19; AAAI 2024.
3. Sashank Reddi, Zachary Charles, Manzil Zaheer, Zachary Garrett, Keith Rush, Jakub Konečný, Sanjiv Kumar, and H. Brendan McMahan, “Adaptive Federated Optimization,” arXiv:2003.00295v1, first submitted 2020-02-29; ICLR 2021.
