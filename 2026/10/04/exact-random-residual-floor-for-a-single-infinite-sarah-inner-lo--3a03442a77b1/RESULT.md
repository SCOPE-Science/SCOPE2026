# Exact random residual floor for a single infinite SARAH inner loop
## Finding

Consider a finite sum of two scalar quadratics
\[
f_\sigma(x)=\frac{\mu(1+\sigma h)}{2}x^2,
\qquad
\sigma\in\{-1,+1\},
\]
sampled uniformly, where
\[
\mu>0,
\qquad
0<h<1.
\]
Their average is
\[
f(x)=\frac{\mu}{2}x^2,
\]
so the unique minimizer is \(x^\star=0\).

Start one SARAH inner loop from a deterministic \(x_0\ne0\) using the exact full gradient
\[
v_0=\nabla f(x_0)=\mu x_0
\]
and the standard first step
\[
x_1=x_0-\eta v_0.
\]
For \(t\ge1\), sample \(\sigma_t\) uniformly and independently and use
\[
v_t
=
\nabla f_{\sigma_t}(x_t)
-
\nabla f_{\sigma_t}(x_{t-1})
+
v_{t-1},
\]
\[
x_{t+1}=x_t-\eta v_t.
\]
Put
\[
\alpha=\eta\mu.
\]

Then
\[
v_t
=
\mu x_0
\prod_{j=1}^t R_j,
\qquad
R_j=1-\alpha(1+\sigma_jh),
\]
and therefore
\[
\mathbb E[v_t^2]
=
\mu^2x_0^2
\left[
(1-\alpha)^2+\alpha^2h^2
\right]^t.
\]
The recursive direction converges to zero in mean square exactly when
\[
0<\alpha<
\frac{2}{1+h^2}.
\]

The iterate behaves differently. Throughout that same range, \(x_t\) converges almost surely and in \(L^2\) to a random limit \(x_\infty\) satisfying
\[
\mathbb E[x_\infty]=0
\]
but
\[
\mathbb E[x_\infty^2]
=
x_0^2
\frac{\alpha h^2}
{2-\alpha(1+h^2)}.
\]
For every heterogeneous pair \(h>0\) and every positive stable step \(\alpha>0\), this residual is strictly positive. Thus a single indefinitely long SARAH inner loop can have a linearly vanishing recursive direction without converging to the minimizer in mean square.

The residual floor is strictly increasing in \(\alpha\):
\[
\frac{\mathrm d}{\mathrm d\alpha}
\left[
\frac{\alpha h^2}
{2-\alpha(1+h^2)}
\right]
=
\frac{2h^2}
{\left[2-\alpha(1+h^2)\right]^2}>0.
\]

There is also an explicit distributional slice. At
\[
\alpha=1,
\]
the component multipliers are \(+h\) and \(-h\) with equal probability, and
\[
x_\infty
=
-x_0
\sum_{j=1}^{\infty}h^jY_j,
\]
where the \(Y_j\) are iid Rademacher signs.

For
\[
h=\frac12,
\]
this Bernoulli convolution is exactly uniform:
\[
x_\infty
\sim
\operatorname{Unif}[-|x_0|,|x_0|].
\]
At the same parameter values,
\[
|v_t|
=
\mu|x_0|\,2^{-t}
\]
holds deterministically. Thus the stochastic direction shrinks perfectly geometrically while the limiting iterate remains spread over the entire interval between \(-|x_0|\) and \(|x_0|\).

## Assumptions and scope

The result concerns one SARAH inner loop with no outer restart after time zero. It uses the original SARAH recursion, uniform component sampling, a constant stepsize, and two positive scalar quadratic components sharing the same minimizer.

The initialization includes the exact full-gradient SARAH snapshot step. The result is not a statement about the full multi-outer-loop SARAH method, which periodically recomputes a full gradient and can converge linearly under standard assumptions.

The mean-square stability range above is exact for the recursive direction on this two-component family. Outside that range, the theorem does not classify every possible almost-sure behavior of the iterate.

## Proof

The average gradient is
\[
\nabla f(x)=\mu x.
\]
Because
\[
x_t-x_{t-1}=-\eta v_{t-1},
\]
the SARAH recursion gives
\[
v_t
=
\mu(1+\sigma_th)(x_t-x_{t-1})+v_{t-1}
=
\left[
1-\alpha(1+\sigma_th)
\right]v_{t-1}.
\]
Thus
\[
v_t=v_0\prod_{j=1}^tR_j
\]
with
\[
R_j=1-\alpha(1+\sigma_jh).
\]

The iid multiplier has first and second moments
\[
r=\mathbb E[R_j]=1-\alpha
\]
and
\[
q=\mathbb E[R_j^2]
=
(1-\alpha)^2+\alpha^2h^2.
\]
Therefore
\[
\mathbb E[v_t^2]
=
v_0^2q^t.
\]
The condition \(q<1\) is exactly
\[
0<\alpha<\frac{2}{1+h^2}.
\]

Define
\[
P_0=1,
\qquad
P_j=\prod_{\ell=1}^jR_\ell.
\]
Since
\[
x_t
=
x_0-\eta\sum_{j=0}^{t-1}v_j,
\]
one has
\[
x_t
=
x_0
\left[
1-\alpha\sum_{j=0}^{t-1}P_j
\right].
\]
When \(q<1\),
\[
\sum_{j\ge0}\mathbb E[|P_j|]
\le
\sum_{j\ge0}
\sqrt{\mathbb E[P_j^2]}
=
\sum_{j\ge0}q^{j/2}
<\infty.
\]
Hence
\[
S=\sum_{j\ge0}P_j
\]
converges absolutely almost surely and in \(L^2\), and
\[
x_\infty=x_0(1-\alpha S).
\]

Since \(|r|<1\),
\[
\mathbb E[S]
=
\sum_{j\ge0}r^j
=
\frac{1}{1-r}
=
\frac{1}{\alpha}.
\]
Therefore
\[
\mathbb E[x_\infty]=0.
\]

To compute the second moment, split off the first multiplier:
\[
S\overset{d}{=}1+RS',
\]
where \(S'\) is an independent copy of \(S\). Put
\[
m=\mathbb E[S]=\frac1\alpha
\]
and
\[
Q=\mathbb E[S^2].
\]
Then
\[
Q=1+2rm+qQ,
\]
so
\[
Q
=
\frac{2-\alpha}
{\alpha^2[2-\alpha(1+h^2)]}.
\]
Consequently
\[
\operatorname{Var}(S)
=
\frac{h^2}
{\alpha[2-\alpha(1+h^2)]},
\]
and
\[
\mathbb E[x_\infty^2]
=
x_0^2
\frac{\alpha h^2}
{2-\alpha(1+h^2)}.
\]

At \(\alpha=1\),
\[
R_j=-\sigma_jh.
\]
Writing
\[
Y_j=\prod_{\ell=1}^j(-\sigma_\ell),
\]
the finite-dimensional map from the sampled signs to \((Y_1,\ldots,Y_j)\) is bijective on the sign cube, so the \(Y_j\) are iid Rademacher variables. Since the initial full-gradient step gives \(x_1=0\),
\[
x_\infty
=
-x_0
\sum_{j\ge1}h^jY_j.
\]

For \(h=1/2\), set
\[
B_j=\frac{Y_j+1}{2}.
\]
Then
\[
\sum_{j\ge1}2^{-j}Y_j
=
2\sum_{j\ge1}2^{-j}B_j-1.
\]
The binary expansion on the right is uniform on \([0,1]\), apart from the null set of dyadic double representations. Hence the signed series is uniform on \([-1,1]\).

## Verification

The accompanying `verify.py` reconstructs the SARAH recursion directly. It enumerates all sample paths through finite depths using exact rational arithmetic, verifies the multiplier formula and the exact second moment of \(v_t\), checks finite partial sums against the perpetuity moment recursion, and verifies the dyadic uniform-grid structure of the \(h=1/2,\alpha=1\) finite approximants.

The finite enumeration is not used as an infinite proof. Almost-sure and \(L^2\) convergence, the residual floor, and the limiting uniform law follow analytically from the product representation and perpetuity calculation above.

## Relationship to prior work

Nguyen et al. introduced SARAH and emphasized a distinctive property of a single inner loop: the recursive stochastic direction \(v_t\) converges linearly in expectation under strong convexity. Their experiments also show a much more stable inner-loop trajectory than SVRG. The inspected full text proves decay of the recursive direction and analyzes finite inner loops, but it does not state the infinite-inner-loop random residual law above.

Li, Ma, and Giannakis later established linear convergence for using the last iterate of a finite SARAH inner loop across repeated outer loops. Their result still relies on periodic restart structure: the endpoint of one finite inner loop seeds a new outer loop with a newly computed reference gradient. It therefore does not imply that one inner loop run forever converges to the optimizer.

Li, Wang, and Giannakis further studied weighted averaging for SARAH and explicitly note that estimator bias creates a nonzero correction in their estimate-sequence analysis. Their inspected results optimize finite-loop averaging and restart choices rather than the almost-sure limit of one infinite recursive loop.

The present calculation isolates that distinction sharply. On the two-curvature family, the direction can decay exactly geometrically while the iterate converges to a nondegenerate random limit. Focused searches for SARAH random limits, residual floors, scalar quadratics, multiplicative recursions, infinite inner loops, and Bernoulli convolutions did not identify the closed residual formula or the uniform limiting example.

## Limitations

The finding is for two scalar quadratic components with a common minimizer. Unequal minimizers introduce additive noise into the recursive-gradient multiplier equation and require a different analysis.

The result concerns a deliberately infinite inner loop. Standard SARAH uses finite inner loops and outer full-gradient resets, so the residual floor is not a claim that the complete algorithm fails to converge.

The special uniform law uses the exact values \(\alpha=1\) and \(h=1/2\). Other \(h\) values give different Bernoulli-convolution laws.

The formula optimizes no practical compute budget by itself. It identifies a structural reason that shrinking \(v_t\) alone is not a certificate that the current inner-loop iterate is near the optimizer.

## References

1. Lam M. Nguyen, Jie Liu, Katya Scheinberg, and Martin Takáč, “SARAH: A Novel Method for Machine Learning Problems Using Stochastic Recursive Gradient,” arXiv:1703.00102v1, 2017.
2. Bingcong Li, Meng Ma, and Georgios B. Giannakis, “On the Convergence of SARAH and Beyond,” arXiv:1906.02351v1, 2019.
3. Bingcong Li, Lingda Wang, and Georgios B. Giannakis, “Almost Tune-Free Variance Reduction,” arXiv:1908.09345v1, 2019.
