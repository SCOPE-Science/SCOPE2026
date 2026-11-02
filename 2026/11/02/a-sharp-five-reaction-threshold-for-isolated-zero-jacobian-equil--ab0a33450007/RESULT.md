# A sharp five-reaction threshold for isolated zero-Jacobian equilibria in planar quadratic kinetics

## Finding
**Theorem (four-support line obstruction; sharp five-reaction threshold).** Let \(F=(P,Q):\mathbb R^2\to\mathbb R^2\) be a polynomial vector field of total degree at most two, and let \(z_*=(x_*,y_*)\) with \(x_*y_*\ne0\). Suppose \(F(z_*)=0\) and the entire Jacobian \(DF(z_*)\) is zero. If, among the six possible monomials
\[
1,\quad x,\quad y,\quad x^2,\quad xy,\quad y^2,
\]
at most four have a nonzero coefficient in at least one component of \(F\), then **a whole affine line of equilibria passes through \(z_*\)**. Thus such a point is never an isolated equilibrium.

Consequently, for a two-species mass-action network whose *reactant* complexes contain at most two molecules, if there is an **isolated positive equilibrium** where the full \(2\times2\) Jacobian vanishes, there must be at least **five distinct active reactant complexes**, and hence at least **five reaction channels**. This is sharp without an upper restriction on product molecularity: a five-reaction network realizing such an isolated equilibrium is displayed below, as already supplied by Yeung and Erban (2026).

This is a statement about the complete Jacobian being the **zero matrix**, not merely having two zero eigenvalues. It does not claim a lower bound for nonzero-nilpotent Jacobians, for nonisolated equilibria, or for networks with reactant molecularity above two.

## Assumptions and scope
A reaction \(\sum_i a_iX_i\to\sum_i b_iX_i\), with rate \(k>0\), contributes \(k(b-a)x_1^{a_1}x_2^{a_2}\) to the vector field. An *active reactant complex* means a distinct source monomial with a nonzero aggregate vector coefficient; there may be several reaction channels with the same source, and cancellations can occur. Counting channels always bounds the number of active complexes from above. Products may have any finite molecularity.

The lower-bound theorem assumes a positive equilibrium \((x_*,y_*)\in(0,\infty)^2\) and vanishing of all four partial derivatives there. The algebraic four-support statement is slightly stronger, requiring only nonzero coordinates and imposing no chemical sign conditions. Isolation is in the ordinary Euclidean topology; since the equilibrium is positive, any nearby equilibrium line also contains positive points.

## Proof
**Step 1: normalize the point and the first jet.** Change coordinates by \(X=x/x_*\), \(Y=y/y_*\). This preserves the set of monomials that occur (every scaling multiplier is nonzero) and the zero-Jacobian condition. We may therefore assume \(z_*=(1,1)\). For either scalar component \(R\in\{P,Q\}\), the equations \(R(1,1)=R_x(1,1)=R_y(1,1)=0\) imply
\[
R(1+u,1+v)=a_Ru^2+b_Ruv+c_Rv^2.
\]
Indeed, after translation a degree-at-most-two polynomial has only these homogeneous quadratic terms if its constant and linear terms vanish.

**Step 2: four monomials give a common scalar factor.** Label the six monomials \(1,x,y,x^2,xy,y^2\) by their exponents
\[
(0,0),\ (1,0),\ (0,1),\ (2,0),\ (1,1),\ (0,2).
\]
Any four distinct exponent vectors in this set affinely span the plane: a straight line contains at most three of these six triangular-lattice points. Hence, for any four chosen monomials the \(3\times4\) matrix whose columns are \((1,i,j)^{\mathsf T}\) has rank three. Its kernel is one-dimensional.

Choose a four-monomial set containing the union of supports of \(P\) and \(Q\) (supplement a smaller support if necessary). The three first-jet equations for each component say that its four coefficients lie in the same one-dimensional kernel. Thus there are a real vector \(w=(w_1,w_2)\) and a single scalar degree-at-most-two polynomial \(G\) such that
\[
F(x,y)=w\,G(x,y),\qquad G(1,1)=G_x(1,1)=G_y(1,1)=0.
\]
If \(F\equiv0\), every point is an equilibrium. Otherwise it suffices to show that this unique (up to nonzero scalar multiple) \(G\) vanishes along a real line through \((1,1)\).

**Step 3: exhaustive *symbolic* two-missing-monomial classification.** Write \(G(1+u,1+v)=au^2+buv+cv^2\). In the original monomial coordinates its coefficients, in the order \(1,x,y,x^2,xy,y^2\), are
\[
(a+b+c,\,-2a-b,\,-b-2c,\,a,\,b,\,c).
\]
Exactly two monomials are absent from the chosen four-monomial superset. Solving the corresponding two linear coefficient equations gives the following exhaustive list; each displayed form is the unique generator up to nonzero scalar multiplication:

| Absent monomials | Generator at \((1+u,1+v)\) |
|:--|:--|
| \(1,x\); \(1,y\); \(x,y\) | \((u-v)^2\) |
| \(1,x^2\) | \(v(v-u)\) |
| \(1,xy\) | \(v^2-u^2\) |
| \(1,y^2\) | \(u(v-u)\) |
| \(x,x^2\); \(x,xy\); \(x^2,xy\) | \(v^2\) |
| \(y,xy\); \(y,y^2\); \(xy,y^2\) | \(u^2\) |
| \(x,y^2\) | \(u(2v-u)\) |
| \(y,x^2\) | \(v(v-2u)\) |
| \(x^2,y^2\) | \(uv\) |

These nine rows exhaust all \(\binom{6}{2}=15\) missing pairs, and each generator has a nonzero real linear factor. Consequently \(G\), hence both components of \(F\), vanish along a line through \((1,1)\). Rescaling gives the asserted line through \(z_*\). That line contains a nontrivial open segment inside the positive quadrant when \(z_*\) is positive.

**Step 4: apply to mass-action systems and attain equality.** A quadratic two-species mass-action field uses at most six source monomials listed above. If a network has at most four reaction channels, its aggregate vector field has at most four monomial supports. By the theorem, a positive zero-Jacobian equilibrium cannot be isolated. In fact the same reasoning shows that five **distinct active reactant complexes** are necessary.

For sharpness, take the following five channels (all rates are written over the arrows):
\[
\varnothing\xrightarrow{1}Y,\qquad
Y\xrightarrow{2}\varnothing,\qquad
2X\xrightarrow{1}3X,\qquad
X+Y\xrightarrow{2}Y,\qquad
2Y\xrightarrow{1}X+3Y.
\]
The exact mass-action ODE, reproduced from Yeung–Erban (2026, Section 4), is
\[
\dot x=x^2-2xy+y^2=(x-y)^2,\qquad
\dot y=1-2y+y^2=(y-1)^2.
\]
Its entire equilibrium set is the singleton \(\{(1,1)\}\), and its Jacobian vanishes at that point. All five sources \(\varnothing,Y,2X,X+Y,2Y\) are distinct and active. Therefore the lower bound is attained. \(\square\)

## Verification
The standalone Python file `verify.py` uses exact symbolic arithmetic to check that all fifteen four-source exponent matrices have rank three, that the fifteen missing-pair generators factor into real linear factors, and that the listed five channels give exactly the displayed ODE and unique equilibrium with zero Jacobian. Run from this directory with `python3 verify.py` (SymPy required). A successfully checked local execution reported `FOUR_SUPPORT_AFFINE_RANK_PASS 15`, `ALL_15_SPARSE_CASES_REAL_LINEAR_FACTOR_PASS 15`, and `MASS_ACTION_FIVE_REACTION_IDENTITIES_PASS`.

The finiteness of the list of missing pairs is what makes this exact exhaustive algebraic check meaningful; it is not a numerical proxy for infinitely many networks. The written rank and factorization proof independently establishes the universal statement.

## Relationship to prior work
Yeung and Erban's 2026 preprint classifies possible local phase portraits at positive zero-matrix equilibria of planar second-order mass-action systems and explicitly supplies the five-channel example used here. The present result supplies a matching **universal minimum**, independent of phase-portrait class, through a source-support obstruction not established in the inspected portions of that work.

Banaji, Boros, and Hofbauer (2024) classify generic bifurcations for small planar quadratic networks, and their Theorem 36 excludes **parameter-unfoldable cusp bifurcations** for \((n,n+2,n)\) networks. A cusp with a simple zero eigenvalue is not a full zero-matrix singularity; their result does not give this source-support factorization, nor does it directly exclude an isolated zero-matrix equilibrium with four arbitrary product complexes.

The 2026 paper *Positive equilibria in mass action networks: geometry and bounds*, particularly Theorem 4.24, concerns uniqueness/nondegeneracy or continua of equilibria under restricted source-count and partition hypotheses; its general bound in the full-rank, one-partition, two-species case concerns at most three distinct sources. The present sharp four-source exclusion covers the remaining sparse quadratic support and is independent of network partition or product molecularity.

## Limitations
This theorem does not classify degenerate equilibria with a nonzero nilpotent Jacobian, does not bound the number of reactions needed to realize **each** of the nine phase-portrait classes, and does not address networks with cubic or higher source complexes. It also does not assert stability or convergence for the sharpness witness. The five-channel witness is credited to the motivating paper, not presented as a new network. The new lower bound is algebraic and may also follow from broader fewnomial-support results not found in the inspected literature; a comprehensive historical-priority determination and independent validation remain outstanding.

## References
1. N. Yeung and R. Erban, *Classification of strongly non-hyperbolic critical points of planar second-order chemical reaction systems*, arXiv:2610.06130v1, publicly available 5 October 2026, Sections 3 and 4. https://arxiv.org/html/2610.06130v1
2. M. Banaji, B. Boros and J. Hofbauer, *Bifurcations in planar, quadratic mass-action networks with few reactions and low molecularity*, Nonlinear Dynamics 112 (2024), 21425–21448, Theorems 12 and 36. https://doi.org/10.1007/s11071-024-10068-1
3. *Positive equilibria in mass action networks: geometry and bounds*, Journal of Mathematical Biology 93 (2026), article 37, Section 4.3 and Theorem 4.24. https://doi.org/10.1007/s00285-026-02429-8
