# Exact off-diagonal curvature leakage in AdaHessian's Hessian RMS
## Finding

AdaHessian combines a Hutchinson diagonal estimator with a root-mean-square exponential moving average of the estimated Hessian diagonal. On a fixed quadratic, those two operations have an exact interaction: the RMS converts diagonal-estimation variance into a persistent off-diagonal curvature term.

Let
\[
f(x)=\frac12x^\top Hx
\]
with a fixed real symmetric Hessian
\[
H\in\mathbb R^{d\times d}.
\]
Consider paper-form AdaHessian with no spatial averaging, so each coordinate uses its own Hutchinson estimate.

For one Rademacher probe
\[
z\in\{-1,+1\}^d,
\]
the diagonal estimator is
\[
D_i=z_i(Hz)_i.
\]
For \(m\ge1\) independent probes in one iteration, average them before the Hessian RMS:
\[
\widetilde D_i
=
\frac1m\sum_{q=1}^m D_i^{(q)}.
\]

Then
\[
\mathbb E[\widetilde D_i]=H_{ii},
\]
but its second moment is
\[
\mathbb E[\widetilde D_i^2]
=
H_{ii}^2
+
\frac1m\sum_{j\ne i}H_{ij}^2.
\]

Now apply the bias-corrected AdaHessian Hessian RMS:
\[
\overline D_{t,i}^{\,2}
=
\frac{1-\beta_2}{1-\beta_2^t}
\sum_{s=1}^t
\beta_2^{t-s}\widetilde D_{s,i}^{\,2},
\qquad
0<\beta_2<1.
\]
On a deterministic quadratic the Hessian is constant, and fresh probes have the same distribution at every iteration. Therefore, for every
\[
t\ge1,
\]
\[
\mathbb E[\overline D_{t,i}^{\,2}]
=
H_{ii}^2
+
\frac1m\sum_{j\ne i}H_{ij}^2.
\]

For the single-probe source default,
\[
m=1,
\]
this becomes
\[
\mathbb E[\overline D_{t,i}^{\,2}]
=
\sum_jH_{ij}^2
=
\|H_{i:}\|_2^2.
\]

Thus the RMS state does not target the squared diagonal curvature in expectation. Its exact excess is
\[
\mathbb E[\overline D_{t,i}^{\,2}]-H_{ii}^2
=
\frac1m
\sum_{j\ne i}H_{ij}^2.
\]
This is precisely the Hutchinson diagonal-estimation variance divided by the number of probes.

The exponential-momentum coefficient affects temporal fluctuations and correlation, but it does not alter this mean-square target. By contrast, increasing the number of probes reduces the leakage exactly at the rate
\[
1/m.
\]

There is also a sharp condition-number interpretation in two dimensions. Let
\[
H\succ0
\]
have eigenvalues
\[
0<\mu\le L,
\qquad
\kappa=\frac L\mu.
\]
For a single probe, the RMS target at coordinate \(i\) is
\[
\|H_{i:}\|_2,
\]
while the true diagonal curvature is
\[
H_{ii}>0.
\]
Over every orientation of a two-dimensional SPD Hessian with condition number \(\kappa\),
\[
\sup
\frac{\|H_{i:}\|_2}{H_{ii}}
=
\frac{\kappa+1}{2\sqrt\kappa}.
\]
This bound is sharp.

With \(m\) independent probes averaged before squaring, the sharp two-dimensional inflation factor becomes
\[
\sqrt{
1+
\frac{(\kappa-1)^2}{4\kappa m}
}.
\]

For example, at
\[
\kappa=100,
\]
one probe permits a sharp RMS inflation factor
\[
\frac{101}{20}=5.05.
\]
Using
\[
m=100
\]
probes reduces the sharp factor to about
\[
1.117.
\]

The conclusion is structural: an unbiased stochastic diagonal estimate need not remain unbiased after a root-mean-square transformation. In AdaHessian, off-diagonal Hessian energy is exactly what survives that nonlinearity in mean square.

## Assumptions and scope

The theorem analyzes the paper-form Hutchinson estimator
\[
D=z\odot Hz
\]
and the paper-form bias-corrected RMS Hessian momentum.

The main theorem uses no spatial averaging, equivalently block size one. This configuration isolates the interaction between Hutchinson variance and Hessian RMS. The public reference implementation takes absolute Hessian-vector entries before its spatial block averaging; for block size one, squaring removes that distinction, but larger blocks require a separate analysis.

The Hessian is fixed across iterations, as it is for a deterministic quadratic. The result does not claim the same exact target when the Hessian changes with the iterate or mini-batch.

The identity concerns
\[
\mathbb E[\overline D_{t,i}^{\,2}],
\]
not
\[
\mathbb E[\overline D_{t,i}].
\]
A fixed exponential moving average remains random, so the theorem does not claim almost-sure convergence of the RMS state to the row norm.

The multi-probe formula assumes independent Rademacher probes are averaged before the RMS square. The defining paper explicitly notes that more Hutchinson steps can be used for a more accurate diagonal approximation; the source default uses one probe per iteration.

## Proof

For one probe,
\[
D_i
=
z_i\sum_jH_{ij}z_j
=
H_{ii}
+
\sum_{j\ne i}H_{ij}z_iz_j.
\]
Since the Rademacher coordinates are independent and centered,
\[
\mathbb E[z_iz_j]=0
\]
for
\[
i\ne j.
\]
Hence
\[
\mathbb E[D_i]=H_{ii}.
\]

For the second moment, distinct Rademacher pair monomials are orthogonal in expectation:
\[
\mathbb E[(z_iz_j)(z_iz_k)]=0
\]
when
\[
j\ne k.
\]
Therefore
\[
\mathbb E[D_i^2]
=
H_{ii}^2
+
\sum_{j\ne i}H_{ij}^2.
\]
Equivalently,
\[
\operatorname{Var}(D_i)
=
\sum_{j\ne i}H_{ij}^2.
\]

Let
\[
D_i^{(1)},\ldots,D_i^{(m)}
\]
be independent copies and
\[
\widetilde D_i
=
\frac1m\sum_{q=1}^mD_i^{(q)}.
\]
Then
\[
\mathbb E[\widetilde D_i]=H_{ii}
\]
and
\[
\operatorname{Var}(\widetilde D_i)
=
\frac1m
\sum_{j\ne i}H_{ij}^2.
\]
Thus
\[
\mathbb E[\widetilde D_i^2]
=
H_{ii}^2
+
\frac1m
\sum_{j\ne i}H_{ij}^2.
\]

The bias-corrected RMS weights are
\[
w_{t,s}
=
\frac{(1-\beta_2)\beta_2^{t-s}}
{1-\beta_2^t},
\]
and they satisfy
\[
\sum_{s=1}^tw_{t,s}=1.
\]
Therefore
\[
\mathbb E[\overline D_{t,i}^{\,2}]
=
\sum_{s=1}^tw_{t,s}
\mathbb E[\widetilde D_{s,i}^2]
=
H_{ii}^2
+
\frac1m
\sum_{j\ne i}H_{ij}^2.
\]
This proves the exact leakage law and its independence from \(\beta_2\).

It remains to prove the sharp two-dimensional condition-number formula.

Scale
\[
\mu=1,
\qquad
L=\kappa.
\]
For one coordinate direction, let
\[
p\in[0,1]
\]
be its squared projection onto the eigenvector of eigenvalue \(1\). Then
\[
H_{ii}
=
p+(1-p)\kappa,
\]
while
\[
\|H_{i:}\|_2^2
=
(H^2)_{ii}
=
p+(1-p)\kappa^2.
\]
Hence the squared single-probe inflation is
\[
R(p)
=
\frac{
p+(1-p)\kappa^2
}{
[p+(1-p)\kappa]^2
}.
\]
Differentiation gives a unique interior maximizer
\[
p=\frac{\kappa}{\kappa+1}.
\]
At that point,
\[
R_{\max}
=
\frac{(\kappa+1)^2}{4\kappa}.
\]
Taking square roots proves
\[
\sup
\frac{\|H_{i:}\|_2}{H_{ii}}
=
\frac{\kappa+1}{2\sqrt\kappa}.
\]

For \(m\) probes,
\[
\frac{
\mathbb E[\widetilde D_i^2]
}{
H_{ii}^2
}
=
1+
\frac1m
\left(
\frac{\|H_{i:}\|_2^2}{H_{ii}^2}
-1
\right).
\]
Substituting the sharp single-probe maximum gives
\[
1+
\frac{(\kappa-1)^2}{4\kappa m}.
\]
Taking square roots proves the multi-probe factor.

## Verification

The accompanying `verify.py` enumerates all Rademacher vectors for small symmetric matrices and checks the exact first and second moments, simulates the bias-corrected Hessian RMS across time, verifies the \(1/m\) multi-probe law, and numerically maximizes the two-dimensional orientation formula against its closed form.

The computations are finite transcription guards. The expectation identities and sharp condition-number maximization are proved analytically above.

## Relationship to prior work

Yao, Gholami, Shen, Mustafa, Keutzer, and Mahoney introduced AdaHessian using a Hutchinson-based Hessian diagonal approximation, a root-mean-square exponential moving average of the approximated diagonal, and spatial averaging. Their paper states that one Hutchinson step is used per iteration by default and that more steps may improve the approximation.

Bekas, Kokiopoulou, and Saad developed stochastic matrix-diagonal estimation from matrix-vector products. Later analyses of Hutchinson diagonal estimation quantify its error through the off-diagonal part of the matrix. In particular, modern diagonal-estimation theory makes clear that off-diagonal matrix energy controls estimator variance.

Those diagonal-estimation results establish the stochastic error of the estimator itself. The present finding identifies what happens after the estimator is fed into AdaHessian's RMS momentum: on a fixed Hessian, the variance becomes an exact additive curvature-scale term in the expected squared RMS state. The same calculation yields a sharp condition-number-dependent inflation factor and an exact \(1/m\) mitigation law for probe averaging.

The inspected AdaHessian paper does not state this mean-square target, the row-norm identity for its RMS state, or the sharp two-dimensional condition-number factor.

## Limitations

The result does not analyze full AdaHessian convergence or the later Hessian-power nonlinearity applied to the random RMS state.

Spatial block averaging larger than one is outside the main theorem.

For nonquadratic or stochastic objectives, the Hessian itself changes over time, so estimator variance and genuine curvature variation are mixed.

The sharp condition-number formula is two-dimensional. Higher-dimensional orientation effects can be larger and require separate extremal analysis.

## References

1. Zhewei Yao, Amir Gholami, Sheng Shen, Mustafa Mustafa, Kurt Keutzer, and Michael W. Mahoney, “AdaHessian: An Adaptive Second Order Optimizer for Machine Learning,” arXiv:2006.00719v1, 2020.
2. Costas Bekas, Effrosyni Kokiopoulou, and Yousef Saad, “An Estimator for the Diagonal of a Matrix,” Applied Numerical Mathematics 57 (2007), 1214–1229, DOI `10.1016/j.apnum.2007.01.003`.
3. Prathamesh Dharangutte and Christopher Musco, “A Tight Analysis of Hutchinson's Diagonal Estimator,” Symposium on Simplicity in Algorithms, 2023, DOI `10.1137/1.9781611977585.ch32`.
