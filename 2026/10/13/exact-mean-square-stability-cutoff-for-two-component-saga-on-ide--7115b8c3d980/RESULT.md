# Exact mean-square stability cutoff for two-component SAGA on identical quadratics

## Finding
The smallest nontrivial SAGA memory table already imposes a sharp stochastic stability limitation even when the underlying finite-sum components are **identical**.

Fix \(L>0\) and minimize
\[
F(x)=\frac12(f_1(x)+f_2(x)),\qquad
f_1(x)=f_2(x)=\frac L2x^2
\]
using standard nonproximal SAGA, one uniformly sampled index per iteration, and a constant stepsize \(\eta>0\). The index samples are mutually independent. Initialize the iterate \(x_0\) and both stored gradient-evaluation points \(y_{1,0},y_{2,0}\) arbitrarily in \(\mathbb R\).

The exact global mean-square stability range is
\[
\boxed{
\mathbb E[x_k^2]\to0\text{ for every deterministic initialization}
\quad\Longleftrightarrow\quad
0<\eta L<\frac2{\sqrt3}.
}
\]
At and beyond the threshold, **every nonzero deterministic full-state initialization** fails to converge in mean square, including the canonical initialization with equal stored points and nonzero iterate.

The proof exhibits a positive-definite quadratic energy with exactly zero conditional drift at the critical learning rate. The same classification applies to joint mean-square convergence of the iterate and both cached points.

## Assumptions and scope
The SAGA step is explicitly
\[
x_{k+1}=x_k-\eta\left[
 f_{i_k}'(x_k)-f_{i_k}'(y_{i_k,k})
 +\frac12\bigl(f_1'(y_{1,k})+f_2'(y_{2,k})\bigr)
\right],
\]
followed by setting \(y_{i_k,k+1}=x_k\) and retaining the other cached point. Gradient-table memory is updated **after** the iterate step. The two indices have sampling probability \(1/2\) independently at each iteration.

The objective is a one-dimensional, nondegenerate, strongly convex quadratic with two equal component functions and exact gradients. Arbitrary deterministic cached points are permitted. Canonical SAGA initialization is a special case. Mean square means expectation with respect to the index samples only.

No conclusion is asserted for other sampling schemes, minibatches, nonidentical component functions, dimensions above one, nonquadratic functions, or almost-sure stability at and above the cutoff.

## Proof
Write the dimensionless stepsize
\[
s=\eta L>0,
\]
and the mean and half-difference of the stored points as
\[
u=\frac{y_1+y_2}{2},\qquad
v=\frac{y_1-y_2}{2}.
\]
Let \(\sigma\in\{-1,1\}\) be the fresh independent Rademacher variable, positive if the first component is selected. Since each component gradient is \(Lx\), the SAGA update simplifies exactly to
\[
\begin{aligned}
x'&=(1-s)x+s\sigma v,\\
u'&=\frac{x+u-\sigma v}{2},\\
v'&=\frac{v+\sigma(x-u)}{2}.
\end{aligned}
\]
The half-difference variable is essential: even identical component functions can produce different cached gradients because their stored points need not agree.

Define
\[
V_s(x,u,v)=\frac{s+2}{s}x^2+s(s+1)u^2
 +3s(s+1)v^2-2sx u.
\]
This is positive definite for every \(s>0\). Indeed its \(x,u\) block has upper-left entry \((s+2)/s>0\) and determinant
\[
\frac{s+2}{s}s(s+1)-s^2=3s+2>0,
\]
while the remaining coefficient \(3s(s+1)\) is positive.

Substitute the three update formulas into the quadratic and average the two choices of \(\sigma\). The cross terms odd in \(\sigma\) cancel, and the remaining coefficients simplify to the exact identity
\[
\boxed{
\mathbb E[V_s(x',u',v')\mid x,u,v]-V_s(x,u,v)
=(3s^2-4)x^2.
}
\]
This is an algebraic identity, not an asymptotic or numerical approximation.

Suppose first that \(0<s<2/\sqrt3\). Put \(c_s=4-3s^2>0\). Taking expectations and summing the drift relation from \(k=0\) to \(N-1\) gives
\[
\mathbb E[V_s(z_N)]
+c_s\sum_{k=0}^{N-1}\mathbb E[x_k^2]
=V_s(z_0),
\]
where \(z_k=(x_k,u_k,v_k)\) and \(z_0\) is deterministic. Since the energy is nonnegative,
\[
\sum_{k=0}^{\infty}\mathbb E[x_k^2]
\le\frac{V_s(z_0)}{c_s}<\infty.
\]
Thus \(\mathbb E[x_k^2]\to0\).

Each original table entry satisfies its own exact second-moment recurrence,
\[
\mathbb E[y_{i,k+1}^2]
=\frac12\mathbb E[x_k^2]
+\frac12\mathbb E[y_{i,k}^2],
\qquad i\in\{1,2\},
\]
because the freshly sampled index is independent of the current state. If a nonnegative sequence is updated by averaging its preceding value with a sequence tending to zero, it tends to zero. Consequently both cached second moments tend to zero. This proves joint mean-square convergence.

Now take \(s\ge2/\sqrt3\). The drift identity implies
\[
\mathbb E[V_s(z_k)]\ge V_s(z_0)
\]
for all \(k\). If the initial triple is nonzero, positive definiteness ensures \(V_s(z_0)>0\). Suppose for contradiction that \(\mathbb E[x_k^2]\to0\). The just-displayed memory recurrences then force both \(\mathbb E[y_{i,k}^2]\to0\). Since \(V_s\) is a fixed finite quadratic form in \(x,y_1,y_2\), Cauchy–Schwarz implies \(\mathbb E[V_s(z_k)]\to0\), contradicting its positive lower bound. This rules out mean-square convergence at and above the threshold for *every* nonzero initialization. In particular, at equality the energy is a nonnegative martingale with constant positive expectation and cannot decay in mean square.

Finally, gradient descent without the SAGA cache obeys
\[
x_{k+1}=(1-s)x_k,
\]
which converges for all initial iterates precisely when \(0<s<2\). Hence SAGA has a strictly smaller stability interval here despite zero heterogeneity in the component functions.

## Verification
The standalone `verify.py` establishes the quadratic drift identity by exact rational polynomial interpolation in the stepsize and state: after clearing the single denominator \(s\), each coefficient is a polynomial of degree at most five in \(s\). Six distinct exact rational stepsizes determine each such coefficient. Six independent quadratic-form evaluation states determine all six coefficients of a quadratic in three state variables. The code checks all thirty-six combinations for both index outcomes using only standard-library `fractions.Fraction` arithmetic.

The checker separately verifies exact positivity of the stated principal minors at representative positive rational steps and checks the normalized drift values
\[
3s^2-4=-1\quad\text{at}\quad s=1,
\]
and
\[
3s^2-4=\frac8{25}>0\quad\text{at}\quad s=\frac65.
\]
The universal correctness proof does not depend on sampling, approximate eigenvalues, or a finite simulation.

## Relationship to prior work
Defazio, Bach, and Lacoste-Julien introduced SAGA and analyzed its convergence for finite-sum optimization; their 2014 paper supplies the precise algorithm and a conservative guaranteed stepsize. Its general convergence statements do not establish the exact all-initialization mean-square stability threshold for two *identical* quadratic components, nor the above closed positive-definite drift identity.

Gazagnadou, Gower, and Salmon later investigated SAGA stepsizes through expected smoothness and minibatch optimization. Their full discussion, convergence bounds, and step-size recommendations concern general sufficient guarantees, not this explicit necessary-and-sufficient stochastic memory-table cutoff. The related paper by Taylor, Van Scoy, and Lessard shows that constructing tight Lyapunov functions is a recognized route for studying first-order algorithms, but the two-component SAGA identity is a specialized new calculation.

Targeted searches for SAGA, identical component quadratics, two-sample cached gradients, exact mean-square thresholds, and equivalent stochastic-recursion formulations did not identify a published statement implying the theorem. This negative search alone is not proof of novelty; the claimed gap concerns the specific objective, state, exact threshold, and conserved critical energy.

## Limitations
The result addresses mean-square stability rather than pathwise stability or arbitrary nonlinear objective behavior. At and above the threshold, nonconvergence in mean square does **not** by itself imply divergence almost surely.

Although the components are equal as functions, their stored evaluation points are allowed to differ. If one artificially resets both cached points to the *current* iterate after every step, the iteration is no longer standard SAGA, and the theorem does not apply.

The exact boundary need not persist for more than two components, nonuniform sampling, nonidentical Hessians, or mini-batches. A different initialization does not rescue mean-square convergence at or above the boundary, provided its full initial state is nonzero.

## References
1. A. Defazio, F. Bach, and S. Lacoste-Julien, “SAGA: A Fast Incremental Gradient Method With Support for Non-Strongly Convex Composite Objectives,” arXiv:1407.0202v1, first submitted 2014-07-01. https://arxiv.org/abs/1407.0202
2. N. Gazagnadou, R. M. Gower, and J. Salmon, “Optimal Mini-Batch and Step Sizes for SAGA,” arXiv:1902.00071v1, first submitted 2019-01-31. https://arxiv.org/abs/1902.00071
3. A. Taylor, B. Van Scoy, and L. Lessard, “Lyapunov Functions for First-Order Methods: Tight Automated Convergence Guarantees,” Proceedings of Machine Learning Research 80 (2018), 4897–4906. https://proceedings.mlr.press/v80/taylor18a.html
