# Grassmann distance degrees of all rational-normal-scroll ruling curves

## Finding

For every integer \(d\ge 2\) and every sequence \(n_1,\ldots,n_d\ge 2\), let \(\mathcal S\) be the one-dimensional family of ruling \((d-1)\)-planes of the complex rational normal scroll \(S(n_1,\ldots,n_d)\), represented in the projection Grassmannian \(\mathrm{pGr}(d,M)\), where \(M=\sum_i(n_i+1)\). Define \(s_i(t)=\sum_{j=0}^{n_i}t^{2j}\), \(L(t)=\operatorname{lcm}_i s_i(t)\), and \(\delta=\deg L\). Then the Grassmann distance degree with **rank-\(d\) orthogonal-projection data** is

\[
\operatorname{GDdeg}(\mathcal S)=2\delta-2
=2\!\sum_{\substack{e>2\\ \exists i:\,e\mid 2(n_i+1)}}\varphi(e)-2
=\operatorname{EDdeg}(\mathcal S).
\]

Thus the cyclotomic ED-degree formula of Friedman–Hoşten–Rosana remains unchanged under the nonlinear requirement that the data matrix itself be a rank-\(d\) orthogonal projector. In particular, on surface scrolls \(S(2,m)\), \(m\ge2\), the GD degree is \(4m+10-4\gcd(3,m+1)\); the first values at \(m=2,3,4,5\) are \(6,18,22,18\).

## Assumptions and scope

Work over \(\mathbb C\) with the standard nonconjugate bilinear form \(v\cdot w=\sum_jv_jw_j\). The affine projection Grassmannian consists of symmetric idempotent matrices of trace \(d\). Let \(v_i(t)=(1,t,\ldots,t^{n_i})\) in the \(i\)-th of \(d\) pairwise orthogonal coordinate blocks. On the open set \(\prod_i s_i(t)\ne0\), the curve is parametrized by

\[
P(t)=\operatorname{diag}\left(\frac{v_1(t)^\top v_1(t)}{s_1(t)},\ldots,\frac{v_d(t)^\top v_d(t)}{s_d(t)}\right).
\]

The parameter map has degree one and is an immersion: a block rank-one image recovers the parameter \(t\) from the first two coordinate ratios, and its differential has nonzero first-ratio derivative. The projective completion adds \(t=\infty\), where the projector has a finite limit; roots of any \(s_i\) lie outside this projection-Grassmannian affine chart. A GD-critical point means a critical point of \(P\mapsto\operatorname{tr}(PQ)\) along the smooth affine curve **outside the algebraic cut locus** \(\operatorname{rank}(PQ)<d\), for generic \(Q\in\mathrm{pGr}(d,M)\), counted without multiplicity. The cut-locus restriction follows the GD definition of Friedman–Hoşten–Rosana. The underlying optimization is equivalent to squared Frobenius distance because the ranks are fixed.

## Proof

**1. A legitimate constrained-data family.** Consider the irreducible parameter space \(W=\prod_{i=1}^d\{[w_i]\in\mathbb P^{n_i}:q_i:=w_i\cdot w_i\ne0\}\). Every tuple gives an actual rank-\(d\) symmetric idempotent

\[
Q_w=\operatorname{diag}\left(\frac{w_1w_1^\top}{q_1},\ldots,\frac{w_dw_d^\top}{q_d}\right).
\]

Put \(g_i(t)=\sum_{j=0}^{n_i}w_{ij}t^j\). The objective restricted to the ruling curve is the rational map

\[
F_w(t)=\operatorname{tr}(P(t)Q_w)=\sum_{i=1}^d\frac{g_i(t)^2}{q_i s_i(t)}=\frac{R_w(t)}{L(t)},\qquad R_w=\sum_i\frac{g_i^2}{q_i}\frac{L}{s_i}.
\]

**2. Generic reduced poles.** Each \(s_i=(t^{2(n_i+1)}-1)/(t^2-1)\) is squarefree and has no zero at \(t=\pm1\); hence \(L\) is squarefree of degree \(\delta\), with the cyclotomic formula in the statement. For a root \(\alpha\) of \(L\), the possible pole residue is

\[
\rho_\alpha(w)=\sum_{i:\,s_i(\alpha)=0}\frac{g_i(\alpha)^2}{q_i s_i'(\alpha)}.
\]

This is not identically zero on \(W\): take a block \(i\) with \(s_i(\alpha)=0\), choose \(g_i(\alpha)\ne0\), and for all other blocks vanishing at \(\alpha\) choose \(g_j(\alpha)=0\) and \(q_j\ne0\). Such choices exist: a hyperplane \(g_j(\alpha)=0\) in \(\mathbb C^{n_j+1}\), dimension at least two, is not contained in the nondegenerate quadric \(q_j=0\). Consequently, for generic \(w\), \(R_w\) and \(L\) are coprime. The map \(F_w:\mathbb P^1\to\mathbb P^1\) then has degree \(\delta\), and exactly \(\delta\) simple finite poles, none of them ramification points.

**3. Uniform generic simplicity of non-pole critical points.** Fix a finite \(t\in\mathbb C\) with \(\prod_i s_i(t)\ne0\), and write

\[
A_i(w_i;t)=\frac{g_i(t)\,[2s_i(t)g_i'(t)-s_i'(t)g_i(t)]}{s_i(t)^2}.
\]

As a quadratic form in \(w_i\), \(A_i\) is a product of two independent linear forms because \(n_i\ge2\) and \(s_i(t)\ne0\). The critical equation is \(F_w'(t)=\sum_i A_i/q_i=0\). This cuts an irreducible divisor \(D_t\) in \(W\). Indeed, fixing the last \(d-1\) block parameters, the equation on \([w_1]\) is the quadric \(A_1+\lambda q_1=0\), where \(\lambda=\sum_{i=2}^d A_i/q_i\) is a nonconstant rational function of those remaining parameters. In the rational-function field of these parameters, \(\lambda\) is transcendental over \(\mathbb C\); the determinant polynomial \(\det(A_1+zq_1)\) is nonzero with leading coefficient \(\det q_1\ne0\). Hence the generic quadric is nondegenerate and geometrically irreducible because \(n_1+1\ge3\). Over all remaining parameter values the quadratic polynomial is never identically zero, as \(A_1\) is not proportional to \(q_1\), so there are no vertical divisorial components. This proves irreducibility of \(D_t\).

The second derivative does not vanish identically on \(D_t\). To see it, choose \(w_i\) with \(g_i(t)=0\) and \(q_i\ne0\) for every \(i\). Such tuples lie on \(D_t\), but there

\[
F_w''(t)=\sum_{i=1}^d\frac{2g_i'(t)^2}{q_i s_i(t)}.
\]

On the hyperplane \(g_1(t)=0\), the restriction of \(q_1\) has rank \(n_1\ge2\) (because \(s_1(t)=v_1(t)\cdot v_1(t)\ne0\)), whereas \(g_1'(t)^2\) has rank one and is nonzero. Thus the first summand is nonconstant and can be chosen not to cancel the fixed other summands. Consequently \(F_w'=F_w''=0\) has codimension at least two in \(W\) for *every* finite regular parameter \(t\).

The global incidence of tuples \((w,t)\) satisfying these two equations over the one-dimensional regular-parameter locus has dimension at most \(\dim W-1\). Its projection cannot contain a Zariski-open subset of \(W\). Therefore, for generic \(w\), every critical point at finite non-poles is simple.

**4. No cut-locus critical points for generic data.** GD degree requires discarding the algebraic cut locus \(\operatorname{rank}(P(t)Q)<d\), not just counting all critical points of the rational trace. For the block-diagonal data \(Q_w\) above, the rank condition is equivalent on the regular curve to \(g_i(t)=0\) for **some** \(i\). Fix any regular finite parameter \(t\) and any index \(i\). On the hypersurface \(g_i(t)=0\), the derivative of its own summand vanishes, but the derivative of the remaining summands is \(\sum_{j\ne i}A_j/q_j\). This is not identically zero, since at least one other block exists (\(d\ge2\)) and each \(A_j/q_j\) is nonconstant. Thus \(g_i(t)=F_w'(t)=0\) has codimension at least two in \(W\), for every regular \(t\). A one-dimensional incidence argument and the finite union over indices show that a generic \(w\) has **no critical point in the cut locus**.

For arbitrary rank-\(d\) data \(Q\), let \(A(t)\) be the unsquared block row matrix defining the scroll and put \(D_Q(t)=\det(A(t)QA(t)^\top)\). On the regular parametrized curve, \(D_Q(t)=0\) is exactly the cut-locus condition. Both \(D_Q\) and the derivative numerator \(H_Q\) are polynomials in \(t\) and in the entries of \(Q\). For generic special data \(Q_w\), the two polynomials have no common root (poles are not critical), hence the resultant \(\operatorname{Res}_t(D_Q,H_Q)\) is nonzero at one actual data projector. This supplies an additional nonempty Zariski-open condition on the full data Grassmannian, so none of the critical points counted below is discarded by the GD cut-locus restriction.

**5. No ramification at infinity.** In the local coordinate \(u=1/t\),

\[
F_w(1/u)=\sum_i\frac{(w_{i,n_i}+w_{i,n_i-1}u+\cdots+w_{i,0}u^{n_i})^2}{q_i(1+u^2+\cdots+u^{2n_i})}.
\]

Its coefficient of \(u\) is \(2\sum_iw_{i,n_i}w_{i,n_i-1}/q_i\), nonzero on a Zariski-open subset of \(W\). Thus infinity is unramified generically. Riemann–Hurwitz for the degree-\(\delta\) map \(F_w\) now gives exactly \(2\delta-2\) finite, non-pole, simple ramification points. These are precisely the GD-critical points of the scroll ruling curve.

**6. Extension to generic unrestricted projectors.** For an arbitrary symmetric data matrix \(Q\), the same denominator \(L\) gives a numerator \(R_Q\) *linear in \(Q\)*, and its derivative numerator is \(H_Q=R_Q'L-R_QL'\). The conditions \(\gcd(R_Q,L)=1\), \(\deg H_Q=2\delta-2\), \(\operatorname{disc}(H_Q)\ne0\), and \(\operatorname{Res}(H_Q,D_Q)\ne0\) are Zariski open. Steps 1–5 exhibit a point of their intersection *inside the actual data Grassmannian* \(\mathrm{pGr}(d,M)\). Since this projection Grassmannian is irreducible over \(\mathbb C\), their common nonempty open is dense therein. The generic GD count therefore equals \(2\delta-2\). The ED degree is the same number by Friedman–Hoşten–Rosana, Theorem 2.2. This completes the proof.

## Verification

Run `python verify_scroll.py` with Python 3 and SymPy installed. It constructs genuine rank-one projectors in each coordinate block, checks that their direct sum is legal rank-\(d\) data, reconstructs the rational trace objective exactly, verifies every possible cyclotomic pole persists, computes the squarefree critical polynomial, and verifies that no critical point lies on the algebraic cut locus. Five independent degree patterns test equal blocks, coprime block lengths, shared cyclotomic poles, three blocks, and larger blocks. These finite examples are consistency checks only; Steps 2–5 establish the theorem for all allowed \(d,n_i\).

## Relationship to prior work

Friedman, Hoşten, and Rosana, arXiv:2610.02018v1, Example 2.1 and Theorem 2.2, calculate the **ED** degree \(2\delta-2\) for this exact ruling curve with a generic unconstrained symmetric data matrix. Their Theorem 4.5 discusses conditions and dimension heuristics under which GD and ED may agree but does not assert GD equality for these ruling curves. The present proof treats rank-\(d\) projection-matrix data directly and proves the necessary noncollision, cut-locus avoidance, and full-degree assertions. Earlier Friedman–Rosana–Sturmfels, arXiv:2601.22843v1, studies GD for other curves and generic complete-intersection models, but does not state this ruling-curve formula. The distinction matters because GD can be strictly smaller than ED on other Grassmann subvarieties.

## Limitations

The conclusion concerns the indicated ruling curves with all \(n_i\ge2\), \(d\ge2\), over characteristic zero, in the symmetric-bilinear projection model. It does not prove ED–GD equality for arbitrary Grassmannian curves or model classes. The proof establishes generic complex critical-point counts and does not claim the number of *real* critical points for every real data projector. The originality comparison cannot exclude unindexed equivalent work.

## References

1. H. Friedman, S. Hoşten, A. Rosana, *Euclidean Distance Optimization Within the Grassmannian*, arXiv:2610.02018v1 (2026-10-01), especially Example 2.1, Theorems 2.2 and 4.5. https://arxiv.org/html/2610.02018v1
2. H. Friedman, A. Rosana, B. Sturmfels, *Distance Optimization in the Grassmannian of Lines*, arXiv:2601.22843v1 (2026-01-30), especially Sections 4–5. https://arxiv.org/html/2601.22843v1
