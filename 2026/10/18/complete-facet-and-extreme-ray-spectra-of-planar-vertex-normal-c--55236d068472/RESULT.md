# Complete facet and extreme-ray spectra of planar vertex-normal cones

## Finding
Let \(n\ge3\) and let \(a_0,\ldots,a_{n-1}\) be distinct unit vectors in \(\mathbb R^2\), listed in counterclockwise order, with every successive cyclic angular gap strictly between \(0\) and \(\pi\). The planar vertex-normal cone is
\[
 C(a)=\{(x_0,\ldots,x_{n-1})\in(\mathbb R^2)^n:\ a_i\cdot(x_i-x_j)\ge0\text{ for all }i\ne j\}.
\]
Here and below indices are cyclic. Its translation lineality consists exactly of the configurations with all \(x_i\) equal and has dimension two. The cone has dimension \(2n\) and exactly \(2n\) facets. A simultaneously irredundant inequality description consists of only
\[
 a_i\cdot(x_i-x_{i+1})\ge0,\qquad
 a_{i+1}\cdot(x_{i+1}-x_i)\ge0,\qquad 0\le i<n.
\]
There is a complete classification of the extreme rays modulo translation. Define \(t_i=J a_i\), where \(J\) rotates counterclockwise by \(\pi/2\). For every antipodal pair \(t_i=-t_j\), four extreme rays are obtained by selecting either of the two occurrences of each direction, with equal positive coefficients. For every unordered triple \(t_i,t_j,t_k\) whose successive counterclockwise angular gaps are each less than \(\pi\), eight extreme rays are obtained by independently selecting one of the two occurrences of each direction. For a triple in cyclic order with consecutive gaps \(\alpha,\beta,\gamma\), their three coefficients are respectively \(\sin\beta,\sin\gamma,\sin\alpha\). There are no other extreme rays in the translation quotient.

In particular, for equally spaced directions, the exact number \(r_n\) of extreme rays in the translation quotient is
\[
 r_n=\begin{cases}
 \dfrac{n(n^2-1)}3,&n\text{ odd},\\
 \dfrac{n(n-2)(n-4)}3+2n,&n\text{ even}.
 \end{cases}
\]
For \(n=3,4,5,6,7,8\), the respective numbers are \(8,8,40,28,112,80\), whereas the corresponding facet counts are \(6,8,10,12,14,16\).

## Assumptions and scope
The cyclic order and strict upper gap bound \(\Delta_i<\pi\) are essential: each consecutive tangent pair must be linearly independent and span a pointed planar sector of aperture less than \(\pi\). No regularity, symmetry, rationality, or generic-position condition beyond these angular assumptions is imposed. The original cone includes translations and is therefore not pointed; all extreme-ray statements concern its quotient by the two-dimensional translation subspace. For regular directions we set \(a_i=(\cos(2\pi i/n),\sin(2\pi i/n))\). A zero-dimensional polygonal configuration is permitted by the inequalities; no positivity of individual side lengths is assumed.

## Proof
**1. Locality of support inequalities.** Put \(\theta_n=\theta_0+2\pi\) and \(\Delta_i=\theta_{i+1}-\theta_i\in(0,\pi)\). Write \(e_i=x_{i+1}-x_i\). The two displayed adjacent inequalities say \(a_i\cdot e_i\le0\) and \(a_{i+1}\cdot e_i\ge0\), precisely when \(e_i\) is a nonnegative linear combination of the counterclockwise tangents \(t_i=Ja_i\) and \(t_{i+1}=Ja_{i+1}\):
\[
 e_i=\lambda_i t_i+\mu_i t_{i+1},\qquad\lambda_i,\mu_i\ge0.
\]
Indeed, \(a_i\cdot t_{i+1}=-\sin\Delta_i<0\) and \(a_{i+1}\cdot t_i=\sin\Delta_i>0\), so the unique coefficients are \(\mu_i=-a_i\cdot e_i/\sin\Delta_i\) and \(\lambda_i=a_{i+1}\cdot e_i/\sin\Delta_i\). Each nonzero \(e_i\) has argument in the closed counterclockwise interval \([\theta_i+\pi/2,\theta_{i+1}+\pi/2]\). These edge-angle intervals are disjoint in their interiors and traverse one full turn in cyclic order.

Fix a support index \(i\) and traverse the closed edge chain beginning at \(x_i\). Its scalar increments \(a_i\cdot e_j\) are initially nonpositive, then eventually nonnegative; there is at most one boundary interval intersecting the sign-change direction of the scalar projection, whose increment can have either sign. Hence the sequence \(a_i\cdot x_i,a_i\cdot x_{i+1},\ldots,a_i\cdot x_i\) cannot exceed its common initial/final value: before the ambiguous edge it is nonincreasing, while after that edge it is nondecreasing toward the final value. This proves every original inequality, including nonadjacent pairs. The converse is immediate. (Alternatively, a closed polygonal chain with weakly rotating edge arguments through one turn is the oriented boundary of a convex polygon, allowing coincident vertices.)

**2. Orthant-section normal form.** Closure of the polygonal chain is equivalent to
\[
 \sum_{i=0}^{n-1}(\lambda_i t_i+\mu_i t_{i+1})=0.
\]
Conversely, any nonnegative \((\lambda,\mu)\) satisfying this vector equation uniquely reconstructs the edge sequence and hence \((x_i)\) up to a common translation. Consequently the translation quotient is linearly isomorphic to the pointed cone
\[
 B(a)=\{(\lambda,\mu)\in\mathbb R_{\ge0}^{2n}:\sum_i(\lambda_i t_i+\mu_i t_{i+1})=0\}.
\]
Thus each \(t_i\) occurs twice, in coordinates \(\lambda_i\) and \(\mu_{i-1}\). The closure matrix has rank two, and the original cone has a strict feasible point \(x_i=a_i\): for \(i\ne j\), \(a_i\cdot(x_i-x_j)=1-a_i\cdot a_j>0\). Hence \(B(a)\) has dimension \(2n-2\), and \(C(a)\) has dimension \(2n\).

**3. Every local inequality is a facet.** At the same strict point, the coefficients on an edge are \(\lambda_i=\mu_i=\tan(\Delta_i/2)>0\), because \(a_{i+1}-a_i=\tan(\Delta_i/2)(t_i+t_{i+1})\). To make any particular coordinate of \(B(a)\) vanish, transfer its positive coefficient to the other occurrence of the identical tangent \(t_i\), preserving the vector closure and leaving every other coordinate strictly positive. Therefore each of the \(2n\) coordinate nonnegativity inequalities cuts out a codimension-one face in the \((2n-2)\)-dimensional linear hull of \(B(a)\). Their interiors distinguish the facets, so the local inequality system is irredundant and complete.

**4. All rays as minimal positive vector circuits.** For a nonzero \(z\in B(a)\), consider its positive support \(S\). If the kernel of the closure matrix restricted to \(S\) has dimension at least two, a nonzero tangent perturbation within that kernel makes \(z\) a nontrivial sum of two distinct nonnegative kernel vectors. Conversely, a positive vector with support-minimal kernel and one-dimensional restricted kernel spans an extreme ray. Since the closure matrix has rank two, the extreme supports contain two or three coordinates; a one-coordinate support is impossible because all \(t_i\ne0\). A two-coordinate positive dependence is necessarily a pair of opposite tangent vectors. A three-coordinate positive dependence consists of three distinct tangent directions strictly surrounding the origin, equivalently all three successive cyclic angular gaps being less than \(\pi\); it cannot include duplicate or antipodal directions. The sine rule for the unique positive dependence gives coefficients proportional to \((\sin\beta,\sin\gamma,\sin\alpha)\). Every tangent direction has exactly two coordinate occurrences, and selecting any one occurrence independently gives all \(4\) or \(8\) distinct positive supports. No other extreme rays exist.

**5. Regular-direction enumeration.** For odd \(n=2k+1\), the number of unordered three-direction sets with all cyclic gaps strictly less than \(\pi\) equals
\[
 T_n=\binom n3-n\binom k2=\frac{n(n^2-1)}{24}.
\]
Indeed, every excluded triple lies in a unique open semicircle beginning at one of its members, and the remaining two members can be selected in \(\binom k2\) ways. For even \(n=2k\), exclude first the \((n/2)(n-2)\) triples containing an antipodal pair, and then exclude the \(n\binom{k-1}2\) other triples contained in an open semicircle. This gives
\[
 T_n=\binom n3-\frac n2(n-2)-n\binom{k-1}2=\frac{n(n-2)(n-4)}{24}.
\]
For odd \(n\) there are no antipodal pairs, hence \(r_n=8T_n\). For even \(n\) there are \(n/2\) antipodal pairs, hence \(r_n=8T_n+4(n/2)\), giving the formulas asserted above.

## Verification
The standalone `verify.py` reproduces the regular-direction counts for every integer \(3\le n\le12\). It independently checks closure, all original nonlocal support inequalities, each of the \(2n\) explicit facet witnesses, and the rank of active original inequalities at every classified ray, requiring rank \(2n-3\) in the ambient \(2n\)-dimensional space. The program uses Python 3's standard library and prints its finite checks. These tests do not certify the formulas for arbitrary \(n\); arbitrary \(n\) is established by the preceding mathematical proof.

## Relationship to prior work
Rieger's 2026 paper introduces and studies cones of this vertex-normal type, including partial redundancy analysis for their defining inequalities. The adjacent-support reduction is consonant with that framework; the new point here is the complete simultaneous irredundant facet description, the classification of every extreme ray, and the parity-sensitive closed ray counts for regular direction grids. Prior work on deformation cones of planar normal fans, including Poullot's graphical-zonotope study, also uses nonnegative edge weights and closing relations, but controls a different geometry: deformation cones of fixed normal fans. In particular, a reported regular-hexagon deformation cone has six facets and five rays, in contrast to the twelve facets and twenty-eight rays here; identifying the two objects would be erroneous. General positive-circuit criteria for orthant sections are classical, and no novelty is claimed for those criteria alone.

## Limitations
The facet theorem assumes every successive angular gap is strictly less than \(\pi\); degenerate or widely separated normal sets may have a different face structure. The clean parity counts hold for equally spaced directions only; the general classification instead uses the actual antipodal pairs and origin-surrounding triples. The cone is considered modulo its unavoidable translation lineality when discussing rays. The standalone numerical rank tests use floating-point arithmetic and bounded sample sizes; the proof does not. Priority remains subject to possible equivalent formulations in older computational geometry and polyhedral cone literature; no claim of independent verification or formal certification is made.

## References
1. Janosch Rieger, *Galerkin approximations to the space of convex bodies by polytopes in nondegenerate V-representation*, arXiv:2608.26615v1, first public 27 August 2026. https://arxiv.org/abs/2608.26615
2. Germain Poullot, *Rays of the deformation cones of graphical zonotopes*, arXiv:2404.02669, first public April 2024. https://arxiv.org/abs/2404.02669
3. Arnau Padrol, Vincent Pilaud, and Germain Poullot, *Deformed Graphical Zonotopes*, Discrete & Computational Geometry, DOI: 10.1007/s00454-023-00586-x, publicly available 2023. https://doi.org/10.1007/s00454-023-00586-x
