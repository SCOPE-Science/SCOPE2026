# A sharp complete envelope of fully discrete upwind entropy fluxes beyond the half-cell criterion

## Finding

For first-order upwind advection with quadratic entropy, every shared two-point numerical entropy flux satisfying the *fully discrete* cell entropy inequality for **all** real initial states is characterized by an explicit sharp pointwise interval. Beyond physical consistency, the characterization does not assume that the entropy flux is continuous, differentiable, or polynomial. It shows that the commonly used half-cell sufficient interval is strictly conservative, and that it can be empty at Courant numbers where a whole nonempty family of universally valid cell entropy fluxes still exists.

For \(0<\nu\le1\), the complete interval is

\[
\boxed{\frac{a^2}{2}-\frac{1-\nu}{2}(a-b)^2\ \le H(a,b)\ \le\frac{a^2}{2}}.
\]

For \(\nu>1\), no shared two-point function satisfies the universal cell inequality. The two extremal fluxes, and every selection of values between them, are admitted as far as this one-step cell inequality is concerned.

## Assumptions and scope

On a periodic uniform one-dimensional mesh with an arbitrary fixed number \(N\ge3\) of cells, let \(u_i\in\mathbb R\) be unrestricted old states with cyclic indices. Apply the explicit first-order upwind method for the advection equation \(u_t+u_x=0\):

\[
 v_i=(1-\nu)u_i+\nu u_{i-1},\qquad \nu=\Delta t/\Delta x>0.
\]

The convex mathematical entropy and its physical flux are both \(U(z)=F(z)=z^2/2\). An entropy flux is an arbitrary single **physically consistent** function \(H:\mathbb R^2\to\mathbb R\), with \(H(a,a)=U(a)\) for all \(a\), used at interface \(i+1/2\) as \(H(u_i,u_{i+1})\). Require, simultaneously for every state vector and every cell,

\[
 U(v_i)\le U(u_i)-\nu\bigl(H(u_i,u_{i+1})-H(u_{i-1},u_i)\bigr). \tag{1}
\]

There are no boundary fluxes and no restrictions on the sign of the states. The assertion concerns one full forward-Euler step, not internal stages or higher-order DG updates. Physical consistency is necessary for a canonical gauge: adding a constant to any entropy flux leaves (1) unchanged.

## Proof

**Necessity, upper envelope.** Fix arbitrary \(a,b\in\mathbb R\) and choose one cell with \(u_{i-1}=u_i=a\), \(u_{i+1}=b\). Its updated value is exactly \(a\). Equation (1), with \(\nu>0\), forces

\[
 H(a,b)\le H(a,a). \tag{2}
\]

The physical consistency hypothesis is \(H(a,a)=U(a)\), so (2) gives the stated upper envelope.

**Necessity, lower envelope.** Choose \(u_{i-1}=a\), \(u_i=u_{i+1}=b\). Then \(v_i=b+\nu(a-b)\), and (1) together with consistency gives

\[
 H(a,b)\ge U(b)+\frac{U(b+\nu(a-b))-U(b)}{\nu}
 =U(a)-\frac{1-\nu}{2}(a-b)^2. \tag{3}
\]

The neighbors can be chosen independently because \(N\ge3\). If \(\nu>1\), the right side of (3) exceeds \(U(a)\) whenever \(a\ne b\), contradicting (2).

**Sufficiency.** For \(0<\nu\le1\), define \(J(a,b)=U(a)-H(a,b)\). The envelope (2)--(3) is equivalent to

\[
 0\le J(a,b)\le\frac{1-\nu}{2}(a-b)^2. \tag{4}
\]

With \(\ell=u_{i-1}\), \(a=u_i\), and \(b=u_{i+1}\), direct expansion gives the exact identity

\[
 U(a)-\nu[H(a,b)-H(\ell,a)]-U((1-\nu)a+\nu\ell)
 =\nu\left[\frac{1-\nu}{2}(a-\ell)^2+J(a,b)-J(\ell,a)\right]. \tag{5}
\]

The right side is nonnegative by (4), proving the inequality for every cell, state vector, and mesh size. The envelope (4) forces \(J(a,a)=0\), in agreement with the independently assumed physical consistency. Both pointwise bounds are attained by \(H_0(a,b)=U(a)\) and \(H_{(1-\nu)/2}(a,b)=U(a)-(1-\nu)(a-b)^2/2\), respectively, so neither can be tightened.

**All quadratic polynomial specializations.** Every consistent polynomial \(H\) of total degree at most two has the form \(U(a)+(b-a)[c_0+c_1a+c_2(b-a)]\). The global upper bound in (2), valid for all \(a,b\in\mathbb R\), forces \(c_0=c_1=0\) and \(c_2\le0\). Writing \(k=-c_2\), (3) gives exactly

\[
 H_k(a,b)=U(a)-k(a-b)^2,\qquad 0\le k\le\frac{1-\nu}{2}. \tag{6}
\]

Thus (6) completely classifies the total-degree-two subfamily, while (4) is the stronger unrestricted-function classification.

**Comparison with the half-cell sufficient interval.** In Section 3.2, equations (22)--(23), of Liu, Jiang, and Zhang (2026), insert \(f(z)=z\), the upwind state flux \(g(a,b)=a\), and quadratic \(U=F\). Their virtual states become \(Z^-=a\), \(Z^+=b+2\nu(a-b)\), and the half-cell bounds reduce exactly to

\[
 H^{\mathrm{half}}_{\mathrm{lo}}(a,b)=U(a)-(\tfrac12-\nu)(a-b)^2,
 \qquad H^{\mathrm{half}}_{\mathrm{hi}}(a,b)=U(a). \tag{7}
\]

For every nonconstant pair and \(0<\nu\le1/2\), the gap between the true and half-cell lower endpoints is \(\nu(a-b)^2/2>0\). For \(1/2<\nu\le1\), (7) has lower endpoint *strictly above* its upper endpoint whenever \(a\ne b\), while the exact envelope remains nonempty. For example, \(\nu=3/4\) and \(H(a,b)=U(a)-(a-b)^2/16\) satisfy (1) universally, but fail the sufficient half-cell bounds at every nonconstant pair. The example is fully within the first-order upwind setting; it does not contradict any sufficiency assertion in the source.

## Verification

The attached standalone script `verify.py` uses only the Python standard library and `fractions.Fraction`. Run `python3 verify.py` after extracting it from the package. It checks the exact dissipation identity and equivalent coefficient boundaries over 10,620 rational cases, then checks 1,452 additional rational instances for pair-dependent fluxes and deliberate violations of the sharp endpoints; the script reports 12,072 total exact-rational checks. These finite checks test the algebra; they are not a substitute for the unrestricted analytical argument above.

## Relationship to prior work

The forward-Euler upwind scheme and its quadratic entropy inequality are classical. The zero-penalty entropy flux \(H_0(a,b)=U(a)\), and the general principle that half-cell convex splitting provides *sufficient* entropy flux conditions, are established background rather than proposed discoveries.

Liu, Jiang, and Zhang, arXiv:2610.30535v1, Section 3.2, equations (20)--(23), construct sufficient shared numerical entropy-flux intervals. The present theorem proves a different, necessary-and-sufficient envelope in the first-order upwind quadratic model, quantifies the exact difference, and classifies even highly irregular admissible interface fluxes. Their general high-order theorem, limiting framework, and nonlinear entropies are not treated here. Published flux-correction approaches of Kuzmin--Hajduk--Rupp and Kivva address more general methods and limiter inequalities, but the inspected statements do not contain this exhaustive two-point envelope.

## Limitations

The result does not prove novelty over all older literature. Complete historical priority remains a risk, especially within classical numerical entropy-flux and flux-correction theory; no claim is made that the elementary algebra or classical upwind stability is new. It covers only scalar linear advection, a quadratic entropy, an exactly upwind conservative state flux, and a single forward-Euler step. It neither establishes high-order DG accuracy nor provides a replacement half-cell sufficient condition for general systems or nonlinear laws. The classification is pointwise over arbitrary real states; restricting data to a bounded physical state set can admit other fluxes. No independent mathematical audit has been performed.

## References

1. Y. Liu, Y. Jiang, and M. Zhang, *High-Order Fully Discrete Entropy-Stable DG Methods with Compact Explicit Single-Step Time Discretizations*, arXiv:2610.30535v1 (publicly submitted 2026-10-21), particularly Section 3.2, equations (20)--(23): https://arxiv.org/abs/2610.30535.
2. D. Kuzmin, H. Hajduk, and A. Rupp, *Limiter-based entropy stabilization of semi-discrete and fully discrete schemes for nonlinear hyperbolic problems*, arXiv:2107.11283 (2021): https://arxiv.org/abs/2107.11283.
3. S. Kivva, *Entropy stable flux correction for scalar hyperbolic conservation laws*, arXiv:2004.02258 (2020): https://arxiv.org/abs/2004.02258.
4. T. Chen and C.-W. Shu, *Review of entropy stable discontinuous Galerkin methods for systems of conservation laws on unstructured simplex meshes*, CSIAM Transactions on Applied Mathematics 1 (2020), 1--52.
