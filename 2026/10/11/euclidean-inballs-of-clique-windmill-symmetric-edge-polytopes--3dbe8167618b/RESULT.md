# Euclidean inballs of clique-windmill symmetric edge polytopes

## Finding

For integers \(m\ge2\) and \(q\ge1\), let \(G_{m,q}=K_1\vee(mK_q)\) be the graph formed from \(m\) disjoint \(q\)-cliques by adjoining one hub adjacent to every other vertex. Put \(N=mq+1\), and in the intrinsic Euclidean zero-sum space \(H=\{z\in\mathbb R^N:\sum_v z_v=0\}\) define its symmetric edge polytope
\[
P_{m,q}=\operatorname{conv}\{\pm(e_v-e_w):vw\in E(G_{m,q})\}.
\]
Write \(\delta_m=0\) for even \(m\) and \(\delta_m=1\) for odd \(m\). The radius of a largest Euclidean ball contained in \(P_{m,q}\) is exactly
\[
\boxed{r_{m,q}=\left(mq-\frac{\delta_m q^2}{mq+1}\right)^{-1/2}.}
\]
The origin-centered ball of this radius is tangent to precisely
\[
\boxed{T_m=\begin{cases}
\binom m{m/2},&m\text{ even},\\
2\binom m{(m-1)/2},&m\text{ odd}
\end{cases}}
\]
distinct facets. Their polar normals, normalized by making the hub potential zero, are exactly those that assign one constant sign \(\sigma_i\in\{-1,1\}\) to all \(q\) leaves of blade \(i\), with \(\left|\sum_{i=1}^m\sigma_i\right|=\delta_m\).

The set \(\mathcal C_{m,q}\) of **all centers** of maximum-radius Euclidean balls has affine dimension
\[
\boxed{\dim\mathcal C_{m,q}=m(q-1)+\begin{cases}1,&m\text{ even},\\0,&m\text{ odd}.\end{cases}}
\]
It is a convex set containing the origin in its relative interior. Hence the inball center is unique exactly when \(q=1\) and \(m\) is odd. The entire polytope has \((2^{q+1}-2)^m\) facets (the known one-sum factorization), so the number of tangent facets, remarkably, does not depend on \(q\).

## Assumptions and scope

All roots \(e_v-e_w\) have ordinary ambient Euclidean length \(\sqrt2\). The metric is the restriction of the standard Euclidean metric of \(\mathbb R^N\) to \(H\), **not** the different metric obtained by deleting the hub coordinate. The hub is labelled \(0\); the other vertices are \((i,j)\) for \(1\le i\le m\), \(1\le j\le q\). There are all edges within each \(\{0,(i,1),\ldots,(i,q)\}\), but no edges between different blades away from the hub. Both parameter bounds are part of the statement: \(m\ge2\), \(q\ge1\). A center means the center of a ball of the stated maximum radius, without an a priori centering requirement.

## Proof

**Polar potentials and the exact facet labels.** Since the connected edge roots span \(H\), the polytope is full-dimensional there and contains the origin in its interior. Its polar is
\[
Q_{m,q}=P_{m,q}^{\circ}=\{u\in H:|u_v-u_w|\le1\text{ for every }vw\in E(G_{m,q})\}.
\]
Write each potential modulo additive constants by fixing the hub value to zero. Thus a vector in \(Q_{m,q}\) is encoded by \(mq\) real leaf values \(x_{ij}\) satisfying \(|x_{ij}|\le1\) and \(|x_{ij}-x_{ik}|\le1\) within each blade. Its corresponding vector \(u\in H\) is obtained by subtracting the mean from the \(N\) hub-and-leaf entries \((0,x_{11},\ldots,x_{mq})\).

For any feasible potential, form the **tight-edge graph** by retaining the edges whose potential difference has absolute value one. A feasible potential is a vertex of \(Q_{m,q}\) if and only if this tight-edge graph is connected. Indeed the active equalities have edge-incidence normals; on \(H\) they span the dual space precisely when their graph is connected. If disconnected, one can vary an entire non-hub component slightly in either direction while preserving all strict inequalities, showing that the potential is not a vertex. If connected, fixing the hub value zero and following tight edges makes all leaf values integral; the hub-leaf bounds then force each leaf value into \(\{-1,0,1\}\). No blade can contain both \(+1\) and \(-1\), because every pair of leaves in a blade is adjacent. A blade of all zeros would be disconnected from the hub in the tight-edge graph. Conversely, any blade containing at least one leaf with value \(+1\) and otherwise only \(0\)'s and \(+1\)'s, or at least one leaf with value \(-1\) and otherwise only \(0\)'s and \(-1\)'s, is entirely connected to the hub by tight edges. Therefore the polar vertices are **exactly** the independent choices of a nonempty signed binary pattern on each blade. There are \(2(2^q-1)\) such patterns per blade and \((2^{q+1}-2)^m\) polar vertices, equivalently facets of the original polytope.

**Polar circumradius.** At a polar vertex let \(k\) denote the number of nonzero leaves, and let \(s=\sum_{i,j}x_{ij}\) be their signed sum. Mean subtraction yields the exact Euclidean norm identity
\[
\|u\|_2^2=k-\frac{s^2}{N}.
\tag{1}
\]
Every blade is one-signed; write \(t_i\in\{1,\ldots,q\}\) for its number of nonzero leaves and \(\sigma_i\in\{-1,1\}\) for their sign. Then \(k=\sum_i t_i\) and \(s=\sum_i\sigma_i t_i\).

At any maximizing polar vertex, necessarily \(|s|\le q\). Otherwise choose any nonzero blade whose sign agrees with that of \(s\) and reverse all its signs. Its size \(t_i\) satisfies \(0<t_i\le q<|s|\); thus the signed sum changes by \(-2\operatorname{sgn}(s)t_i\), strictly reducing its absolute value, while \(k\) stays fixed. Identity (1) gives a strictly larger norm, a contradiction.

Suppose first that \(m\ge3\). If a maximizing vertex had \(k<mq\), a zero leaf in one of its blades could be made equal to that blade's existing sign, preserving all graph inequalities and the vertex property. The new count is \(k+1\), and its sum is \(s+\varepsilon\), where \(\varepsilon\in\{-1,1\}\). By \(|s|\le q\), the squared-norm increment obeys
\[
1-\frac{2\varepsilon s+1}{mq+1}
\ge 1-\frac{2q+1}{mq+1}
=\frac{(m-2)q}{mq+1}>0.
\]
This contradicts maximality. Therefore **every leaf is nonzero**. When \(m=2\), identity (1) gives \(\|u\|^2\le k\le2q\), and equality is attained by opposite full-blade signs; any equality case must have all leaves nonzero and \(s=0\). Thus for every \(m\ge2\), each maximizer has \(k=mq\) and a single sign on every blade. Now \(s=q\sum_i\sigma_i\), whose minimum possible absolute value is zero if \(m\) is even and \(q\) if \(m\) is odd. Substitution into (1) shows that
\[
R^2:=\max_{u\in Q_{m,q}}\|u\|_2^2=mq-\frac{\delta_m q^2}{mq+1},
\]
with precisely the listed maximizing normals. This completes the characterization of the polar circumradius and of all polar farthest vertices.

**Inradius and tangent facets.** The polar identity \(P_{m,q}=\{z\in H:u\cdot z\le1\text{ for all }u\in Q_{m,q}\}\) shows that an origin-centered ball of radius \(r\) lies in \(P_{m,q}\) if and only if \(r\|u\|\le1\) for every polar vertex. Its largest such radius is \(r=1/R\). Because \(P_{m,q}=-P_{m,q}\), any contained ball of radius \(r\) centered at \(c\) has its reflection, centered at \(-c\), contained as well. Taking midpoints of points of those two balls proves that the ball of radius \(r\) centered at the origin is contained. Thus no translated ball can have a larger radius. A facet is tangent to the central maximum ball precisely when its polar vertex has norm \(R\); the balanced full-blade sign choices therefore yield exactly the stated binomial count.

**Dimension of the full center set.** For \(r=1/R\), the set of allowed ball centers is
\[
\mathcal C_{m,q}=\{c\in H:u\cdot c+r\|u\|\le1\text{ for every vertex }u\text{ of }Q_{m,q}\}.
\]
Each farthest vertex \(u\), along with \(-u\), forces \(u\cdot c=0\) for every \(c\in\mathcal C_{m,q}\). Let \(L\) be the orthogonal complement in \(H\) of the span of those farthest vertices. Thus \(\mathcal C_{m,q}\subseteq L\). Every other polar vertex has \(r\|u\|<1\); there are only finitely many. Consequently, all centers in a sufficiently small relative neighborhood of zero in \(L\) satisfy every remaining inequality, and \(\mathcal C_{m,q}\) has affine hull exactly \(L\) and zero in its relative interior.

Define the injective linear map \(\Phi:\mathbb R^m\to H\) by taking the hub value zero, placing a common value \(a_i\) on all \(q\) leaves of blade \(i\), and subtracting the mean. Injectivity follows because \(\Phi(a)=0\) would force each leaf-hub difference \(a_i\) to vanish. The contact normals are exactly \(\Phi(\sigma)\) for \(\sigma\in\{-1,1\}^m\) with \(|\sum_i\sigma_i|=\delta_m\). For even \(m\), their sign vectors span the \((m-1)\)-dimensional zero-sum hyperplane: swapping opposite signs produces all differences of coordinate unit vectors. For odd \(m\), those swaps still span the zero-sum hyperplane, and one contact sign vector has nonzero coordinate sum, giving rank \(m\). Since \(\dim H=mq\), subtracting these ranks gives \(\dim\mathcal C_{m,q}=mq-m+1\) for even \(m\) and \(mq-m\) for odd \(m\), exactly as claimed.

## Verification

Run `python3 verify.py` with Python 3 and no third-party dependencies. It enumerates the exact product of polar facet-label sets and calculates all norms as rational numbers. Across 18 parameter pairs it compared all 126,256 polar vertices with the stated radius, contact count, contact form, and rational rank of the contact span. Five additional tests constructed the full graph inequalities directly, enumerated all integer leaf assignments, and determined tight-constraint rank by graph connectivity; the resulting exact polar facet sets matched the product description. The reproducible summary is `ALL_EXACT_CHECKS_PASSED cases=18 polar_vertices=126256 direct_facets=5`. This finite verification is supplementary to the all-parameter proof above.

## Relationship to prior work

Chen, Davis and Korchevskaia describe facet subgraphs of symmetric edge polytopes in `arXiv:2107.12315`, Theorem 3, establishing the geometric setting and tight-edge viewpoint. Mori, Mori and Ohsugi, `arXiv:2312.11287`, Proposition 2.1 and the discussion of one-sums, supply the general integral facet-label criterion and the multiplicativity of the **total** facet number under 1-sums. The latter implies \((2^{q+1}-2)^m\) facets here but does not determine their distances from the origin, the maximally inscribed ball, which facets touch it, or the affine dimension of its center set. Ohsugi and Tsuchiya, `arXiv:2008.08621`, study normalized volumes and Ehrhart invariants for related suspension polytopes; these are not Euclidean ball invariants. In graph-theoretic language, the squared polar radius divided by \(N\) is the maximum variance of a 1-Lipschitz function on \(G_{m,q}\), sometimes called graph spread. The above evaluation and its Euclidean contact/center consequences require the displayed sign-balancing argument, not merely the definitions or known 1-sum facet counts.

## Limitations

The theorem uses equal clique sizes and a **single** shared hub; no conclusion is asserted for unequal blade sizes, multiple shared hubs, weighted roots, or an arbitrary affine coordinate projection with a changed Euclidean metric. The center dimension concerns the entire convex set of optimal centers; the formula does not claim to give all its bounding facets or its volume. The computer checks cover only the listed finite parameter pairs and cannot independently prove statements for unbounded \(m\) or \(q\). An equivalent result may conceivably appear in work using maximum Lipschitz variance rather than symmetric edge polytopes; the literature comparison below does not establish absence from all unpublished or differently indexed sources.

## References

1. Tianran Chen, Robert Davis and Evgeniia Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, first arXiv version 26 July 2021, `arXiv:2107.12315`, https://arxiv.org/abs/2107.12315.
2. Aki Mori, Kenta Mori and Hidefumi Ohsugi, *Number of facets of symmetric edge polytopes arising from join graphs*, first arXiv version 18 December 2023, `arXiv:2312.11287`, https://arxiv.org/abs/2312.11287.
3. Hidefumi Ohsugi and Akiyoshi Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, first arXiv version 19 August 2020, `arXiv:2008.08621`, https://arxiv.org/abs/2008.08621.
4. Louigi Addario-Berry, Svante Janson and Colin McDiarmid, *On the spread of random graphs*, `arXiv:0902.1156`, https://arxiv.org/abs/0902.1156. Included for the established terminology of Lipschitz variance, not as an assertion about windmill polytopes.
