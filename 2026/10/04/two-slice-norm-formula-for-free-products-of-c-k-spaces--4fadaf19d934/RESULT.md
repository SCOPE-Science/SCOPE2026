# Two-slice norm formula for free products of \\(C(K)\\)-spaces

## Finding
Let \\(K_1,K_2\\) be nonempty compact Hausdorff spaces and let \\(J=K_1*K_2\\) be their topological join. Under the canonical lattice identification of \\(C(K_1)*C(K_2)\\) with \\(C(J)\\), define for \\(f\\in C(J)\\)
\\[
m_f(t)=\\max_{x\\in K_1,\\,y\\in K_2}|f([x,y,t])|,\\qquad 0\\le t\\le1.
\\]
Let \\(\\operatorname{conc}m_f\\) denote the least concave majorant of \\(m_f\\) on \\([0,1]\\). Then
\\[
\\boxed{\\ \\|f\\|_*=2(\\operatorname{conc}m_f)(1/2)\\ }.
\\]
Equivalently, if the value at \\(s=t=1/2\\) is defined to be \\(2m_f(1/2)\\), then
\\[
\\boxed{\\ \\|f\\|_*=\\max_{0\\le s\\le1/2\\le t\\le1}
\\frac{(2t-1)m_f(s)+(1-2s)m_f(t)}{t-s}\\ }.
\\]
Hence the free-product norm depends only on the one-dimensional slice-maximal profile \\(m_f\\), and every norm value has an exact certificate involving at most two join-parameter slices.

As immediate checks, for a canonical first-factor element \\(L(g,0)\\), one has \\(m(t)=(1-t)\\|g\\|_\\infty\\), so the formula gives \\(\\|L(g,0)\\|_*=\\|g\\|_\\infty\\). For the constant function \\(1\\), one has \\(m(t)=1\\), hence \\(\\|1\\|_*=2\\); therefore the standard comparison \\(\\|f\\|_\\infty\\le\\|f\\|_*\\le2\\|f\\|_\\infty\\) has sharp upper constant.

## Assumptions and scope
The spaces \\(K_1\\) and \\(K_2\\) are nonempty compact Hausdorff spaces. The join parameter is written \\(t\\in[0,1]\\), with points represented by \\([x,y,t]\\). The norm \\(\\|\\cdot\\|_*\\) is the Banach-lattice free-product norm from the canonical representation in the cited 2026 paper. No metrizability or separability assumption is used.

The conclusion is specific to two \\(C(K)\\)-factors. It does not assert an analogous midpoint formula for arbitrary Banach-lattice free products.

## Proof
The map
\\[
(x,y,t)\\longmapsto |f([x,y,t])|
\\]
is continuous on the compact space \\(K_1\\times K_2\\times[0,1]\\) after passage to the quotient defining the join. Therefore the maximum over \\(K_1\\times K_2\\) exists for every \\(t\\), and the maximum theorem gives continuity of \\(m_f\\).

Theorem 6.2 of Martínez-Fernández--Tradacete gives
\\[
\\|f\\|_*=\\inf\\left\\{a+b:
 a,b\\ge0,\\ |f([x,y,t])|\\le(1-t)a+tb
 \\text{ for all }[x,y,t]\\in J\\right\\}.
\\]
Taking the maximum over \\(x,y\\) at each fixed \\(t\\) shows that this is exactly
\\[
\\|f\\|_*=\\inf\\left\\{a+b:
 m_f(t)\\le(1-t)a+tb\\ \\text{ for every }t\\in[0,1]\\right\\}.
\\]
The endpoint constraints already imply \\(a\\ge m_f(0)\\ge0\\) and \\(b\\ge m_f(1)\\ge0\\), so the explicit nonnegativity conditions add nothing.

Write \\(\\ell(t)=(1-t)a+tb\\). Since \\(\\ell(1/2)=(a+b)/2\\), the preceding infimum is twice the smallest possible value at \\(1/2\\) of an affine majorant of \\(m_f\\). Every affine majorant is concave, so it majorizes \\(\\operatorname{conc}m_f\\), giving
\\[
\\|f\\|_*\\ge2(\\operatorname{conc}m_f)(1/2).
\\]
Conversely, a concave function on an interval has a supporting affine majorant at every interior point. Applying this at \\(1/2\\) to \\(\\operatorname{conc}m_f\\) produces an affine function \\(\\ell\\) satisfying
\\[
\\ell\\ge\\operatorname{conc}m_f\\ge m_f,
\\qquad
\\ell(1/2)=(\\operatorname{conc}m_f)(1/2).
\\]
Its endpoint values are nonnegative because \\(\\ell\\ge m_f\\ge0\\). Thus it is admissible in the published norm formula and yields the reverse inequality. This proves
\\[
\\|f\\|_*=2(\\operatorname{conc}m_f)(1/2).
\\]

For the two-slice formula, the value of the least concave majorant at a point is the supremum of barycentric averages of the original function with that barycenter. In one dimension, two support points suffice. Hence
\\[
(\\operatorname{conc}m_f)(1/2)
=\\max_{0\\le s\\le1/2\\le t\\le1}
\\left(
\\frac{t-1/2}{t-s}m_f(s)+
\\frac{1/2-s}{t-s}m_f(t)
\\right),
\\]
with the diagonal value interpreted as \\(m_f(1/2)\\). Multiplication by \\(2\\) gives the displayed formula. Continuity of \\(m_f\\) makes the extended two-point expression continuous on the compact parameter region, so the maximum is attained. At each active slice, compactness of \\(K_1\\times K_2\\) also gives points where \\(m_f\\) is attained. Thus at most two slices give an exact certificate for the norm.

Finally, since \\(m_f\\le\\|f\\|_\\infty\\), one has \\(\\operatorname{conc}m_f\\le\\|f\\|_\\infty\\), so \\(\\|f\\|_*\\le2\\|f\\|_\\infty\\). The reverse comparison follows already from the published formula, or directly because any admissible affine majorant has value at least \\(m_f(t)\\) on every slice. The constant function \\(1\\) has constant profile \\(m_f=1\\), proving sharpness of the factor \\(2\\).

## Verification
The proof was replayed from the published norm formula without changing its hypotheses. Three boundary tests were checked symbolically: canonical first-factor functions have affine profile \\((1-t)\\|g\\|_\\infty\\) and recover their original norm; canonical second-factor functions have profile \\(t\\|h\\|_\\infty\\) and recover their original norm; the constant function has profile \\(1\\) and free-product norm \\(2\\). These tests probe both endpoint behavior and the midpoint factor.

The two-slice expression is exactly twice a convex combination of \\(m_f(s)\\) and \\(m_f(t)\\) whose barycenter is \\(1/2\\); the coefficients are nonnegative and sum to \\(2\\) after the final scaling. No finite numerical experiment is used as proof.

## Relationship to prior work
Martínez-Fernández and Tradacete introduced Banach-lattice free products and proved in Theorem 6.2 that \\(C(K_1)*C(K_2)\\) is lattice isomorphic to \\(C(K_1*K_2)\\), with the exact infimum formula over endpoint parameters \\(a,b\\). The present finding converts that two-variable infinite-constraint minimization into a one-dimensional concavification identity and then into an attained maximum over at most two join slices.

Targeted searches of the open-access paper for “concave”, “least concave”, and “majorant” found no such reformulation, and targeted literature searches for a concave-envelope or two-slice formula for this free-product norm found only the original theorem and summaries reproducing its \\(a,b\\)-infimum formula. This supports, but does not prove, originality.

## Limitations
The result is a sharpening and convex-geometric reformulation of a norm formula already proved in the 2026 source; it does not introduce a new free-product construction. Because the reduction from an affine-majorant problem to a least-concave-majorant value is classical convex analysis, an equivalent observation may exist under different terminology or may have been regarded as implicit by the original authors. The statement has only been checked for the two-factor \\(C(K)\\) representation, not for general free products or more than two factors.

## References
1. Gonzalo Martínez-Fernández and Pedro Tradacete, “Free Products of Banach Lattices,” arXiv:2605.28988, first submitted 2026-05-27. In particular, Theorem 6.2 gives the \\(C(K_1*K_2)\\) representation and the endpoint-affine norm formula.
