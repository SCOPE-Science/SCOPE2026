# A scalar quadratic witness makes the trust-region radius lower bound indispensable
## Finding
Consider the basic trust-region framework with acceptance threshold \\(\\eta\\in(0,1)\\). On the scalar objective
\\[
f(x)=\\tfrac12 x^2,
\\]
use the exact quadratic model \\(m_k(s)=\\tfrac12(x_k+s)^2\\). Fix \\(q\\in(0,1)\\), \\(x_0>0\\), and \\(0<\\Delta_0<(1-q)x_0\\), and prescribe the radius update
\\[
\\Delta_{k+1}=q\\Delta_k.
\\]
Then every trial is successful with \\(\\rho_k=1\\), Conditions C.2 and C.3 of Rieussec--Bastin are satisfied, yet the iterates converge to a nonstationary point:
\\[
x_k=x_0-\\frac{\\Delta_0(1-q^k)}{1-q}
\\longrightarrow
x_\\infty=x_0-\\frac{\\Delta_0}{1-q}>0.
\\]
Consequently \\(\\|\\nabla f(x_k)\\|\\to x_\\infty>0\\). The missing structural ingredient is precisely their Condition C.1, the lower bound tying the radius to the running gradient scale.

## Assumptions and scope
The objective is the one-dimensional strongly convex quadratic \\(f:\\mathbb R\\to\\mathbb R\\), \\(f(x)=\\tfrac12x^2\\). The model is exact, so \\(H_k=1\\) and \\(g_k=x_k\\). The trust-region norm is the Euclidean norm. The trial step is an exact solution of the radius-constrained quadratic subproblem. The acceptance threshold may be any fixed \\(\\eta\\in(0,1)\\). The radius rule is deliberately chosen to be geometric on every iteration; it is a valid update rule within the generic framework but is not one of the five concrete mechanisms later proved to satisfy C.1 in the source.

## Proof
Because \\(\\Delta_0<(1-q)x_0\\), the total radius mass satisfies
\\[
\\sum_{j=0}^{\\infty}\\Delta_j=\\frac{\\Delta_0}{1-q}<x_0.
\\]
Suppose inductively that \\(x_k>\\Delta_k>0\\). The unconstrained model minimizer is \\(-x_k\\), which lies outside the trust region, so the exact constrained minimizer is \\(s_k=-\\Delta_k\\). Since the model equals the objective identically,
\\[
f(x_k)-f(x_k+s_k)=m_k(0)-m_k(s_k)>0,
\\]
and therefore the actual-to-predicted reduction ratio is exactly \\(\\rho_k=1\\). Thus the step is accepted for every \\(\\eta<1\\), giving
\\[
x_{k+1}=x_k-\\Delta_k.
\\]
With \\(\\Delta_k=q^k\\Delta_0\\), summation yields
\\[
x_k=x_0-\\Delta_0\\frac{1-q^k}{1-q}.
\\]
The assumed bound on \\(\\Delta_0\\) gives \\(x_k\\ge x_\\infty>0\\). Moreover \\(x_k>\\Delta_k\\) holds: indeed \\(x_k\\ge x_\\infty>0\\) while \\(\\Delta_k\\le\\Delta_0<(1-q)x_0<x_0\\), and directly
\\[
x_k-\\Delta_k=x_0-\\frac{\\Delta_0(1-q^{k+1})}{1-q}>x_\\infty>0.
\\]
Hence the induction is valid for all \\(k\\).

The Cauchy step in one dimension is the same boundary step, so the standard Cauchy-decrease requirement is satisfied. The objective is bounded below, its gradient is globally Lipschitz, and the exact model Hessian is uniformly bounded. Condition C.2 concerns unsuccessful iterations; there are none, so it is satisfied vacuously. For any controlled-growth constant \\(\\overline\\gamma_3>1\\), Condition C.3 holds because on every successful iteration
\\[
\\Delta_{k+1}=q\\Delta_k<\\overline\\gamma_3\\Delta_k.
\\]
However C.1 fails: \\(\\Delta_k\\to0\\), whereas \\(\\min_{0\\le j\\le k}|g_j|=x_k\\to x_\\infty>0\\) and the running Hessian bound is constant. Therefore no positive C.1 constant can hold.

## Verification
The standalone script `verify_scalar_tr.py` checks the exact geometric formulas using rational arithmetic for the representative choice \\(x_0=1\\), \\(q=1/2\\), \\(\\Delta_0=1/4\\). It verifies the exact ratio \\(\\rho_k=1\\), the constrained-step condition, the closed-form iterate, and the positive nonstationary limit \\(x_\\infty=1/2\\) for a finite replay; the proof above establishes the result for all admissible parameters and all iterations.

## Relationship to prior work
Rieussec and Bastin organize trust-region radius mechanisms around three structural conditions and explicitly elevate the radius lower bound C.1 to a named condition that is key for global convergence. Their generic algorithm accepts a step whenever its actual-to-predicted ratio exceeds a fixed threshold and otherwise leaves the radius update to a mechanism. They prove convergence after imposing C.1 together with contraction/growth controls, and verify C.1 for five concrete mechanism families. They do not state the scalar geometric-radius witness above.

The same survey cites Yuan's 1998 one-dimensional nonconvergence example to explain a different issue: when the acceptance threshold is zero, accepted steps with arbitrarily small decrease can permit nonstationary accumulation points. The present witness instead works for every strictly positive \\(\\eta<1\\), has a perfect model with \\(\\rho_k=1\\) at every iteration, and isolates failure of the radius-to-gradient lower bound itself.

Targeted published-finding corpus searches for summable trust-region radii, accepted exact-quadratic steps, and necessity of the radius lower bound returned no implication-equivalent record. The closest trust-region record concerns the fraction of optimal decrease achieved by the Cauchy point, not convergence under collapsing successful radii.

## Limitations
This is a necessity witness for the generic structural theory, not a counterexample to any of the five concrete update mechanisms that the source proves satisfy C.1. It shows that C.2 and C.3 cannot compensate for removing C.1; it does not claim C.1 is the weakest possible substitute in every specialized trust-region algorithm. The literature search cannot establish absolute novelty, and the historical trust-region literature is extensive.

## References
1. J. Rieussec and F. Bastin, “A survey of trust-region radius update mechanisms. Part I: First-order analysis,” arXiv:2606.30202v1, first public 2026-06-29. Primary MSC 90C30 and 65K05.
2. Y.-x. Yuan, “An example of non-convergence of trust region algorithms,” in *Advances in Nonlinear Programming*, 1998, pp. 205–215, DOI 10.1007/978-1-4613-3335-7_9.
