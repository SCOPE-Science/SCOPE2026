# Balanced ternary classification of facets of even prism Lipschitz-free balls

## Finding
For every even integer \(n\ge4\), let \(G_n=C_n\square K_2\) be the circular ladder (an \(n\)-gonal prism graph), with its unweighted shortest-path metric on the \(2n\) vertices. The real Lipschitz-free space \(\mathcal F(G_n)\) has unit ball with precisely
\[
 F_n=2[z^0](z^{-1}+1+z)^n
    =2\sum_{j=0}^{n/2}\binom n{2j}\binom{2j}j
\]
facets. These facets are classified bijectively by a cyclic initial sign \(\epsilon\in\{-1,1\}\) and a balanced ternary word \(x\in\{-1,0,1\}^n\) satisfying \(\sum_i x_i=0\). Along even integers,
\[
 F_n\sim \sqrt{\frac{3}{\pi n}}\,3^n.
\]
The counts at \(n=4,6,8,10,12,14\) are \(38,282,2214,17906,147578,1232454\).

## Assumptions and scope
The vertex set is \(\{(i,j):i\in\mathbb Z/n\mathbb Z,\ j\in\{0,1\}\}\); adjacent vertices lie in the same layer at consecutive cycle positions, or form a rung at the same position. All graph edges have length one; distances are shortest-path distances. The scalar field is real. Fixing any base vertex, the unit ball of the Lipschitz-free (Arens–Eells) space is the convex hull of the molecules \((\delta_u-\delta_v)/d(u,v)\) over distinct vertices. For a graph shortest-path metric, every molecule across a nonedge is a convex combination of oriented edge molecules along a geodesic. Consequently this unit ball equals the symmetric edge polytope \(\operatorname{conv}\{\pm(\delta_u-\delta_v):uv\in E(G_n)\}\). The latter lies in the \((2n-1)\)-dimensional zero-sum coordinate hyperplane. No result is asserted for odd \(n\), where the graph is not bipartite, or for weighted edges.

## Proof
**1. Reduce facets to integral flows.** The graph \(G_n\) is connected, planar and bipartite for even \(n\). Proposition 4.33 of D’Alì–Delucchi–Michałek [1] provides a bijection from facets of its symmetric edge polytope to nowhere-zero integer \(2\)-flows on the planar dual. A nowhere-zero integer \(2\)-flow assigns each edge a signed value \(\pm1\) relative to an arbitrarily fixed reference orientation, conserving flow at every vertex. Equivalently, it is an orientation of every undirected edge such that indegree equals outdegree at every vertex. This equivalence counts an orientation and its simultaneous reversal separately, as required for antipodal facets.

**2. The planar dual.** Embed the two \(n\)-cycles as inner and outer rims of a planar annulus, joined by the \(n\) rungs. The dual graph has one vertex per quadrilateral face and one vertex for each of the two complementary faces. Each quadrilateral-face vertex is linked to its two cyclic neighbors and both complementary-face vertices. Hence the dual is the \(n\)-gonal bipyramid graph, namely an \(n\)-cycle together with two apices adjacent to every cycle vertex (the two apices are not adjacent to each other).

**3. Conservation relations.** Orient the reference cycle edges from \(i\) to \(i+1\), and both reference apex spokes from rim vertex \(i\) outward toward their respective apices. Write their signed flows \(c_i,a_i,b_i\in\{-1,1\}\). Kirchhoff conservation at rim vertex \(i\) is
\[
 a_i+b_i=c_{i-1}-c_i, \qquad i\in\mathbb Z/n\mathbb Z.
\]
If \(c_i=c_{i-1}\), this forces \(a_i=-b_i\); set \(x_i=a_i\in\{-1,1\}\). If \(c_i=-c_{i-1}\), it forces \(a_i=b_i=c_{i-1}\); set \(x_i=0\). Equivalently, \(x_i=(a_i-b_i)/2\). In either case,
\[
 a_i=x_i+\frac{c_{i-1}-c_i}{2},\qquad
 b_i=-x_i+\frac{c_{i-1}-c_i}{2}.
\]
Summing around the rim yields \(\sum_i a_i=\sum_i x_i\) and \(\sum_i b_i=-\sum_i x_i\), because the cyclic differences telescope. The two apex conservation conditions are therefore equivalent to \(\sum_i x_i=0\).

**4. Exact reconstruction and the two-to-one factor.** Every balanced ternary word has the same number of positive and negative entries, so its nonzero count is even. As \(n\) is even, the number of zeros is also even. Choose \(c_{n-1}=\epsilon\in\{-1,1\}\) freely. Traverse the word cyclically and **preserve** the rim sign across position \(i\) when \(x_i\ne0\), but **flip** it when \(x_i=0\). Since the number of flips is even, the rim signs close consistently. At each position choose \(a_i,b_i\) by the rules in Step 3. The local and apex conservation equations all hold, and every value is \(\pm1\). Conversely any flow has precisely this word and is uniquely recovered from it and one initial rim sign. Thus the announced map \((\epsilon,x)\mapsto\text{facet}\) is a bijection, including the all-zero word, whose \(n\) flips close because \(n\) is even.

**5. Exact enumeration.** A word with \(j\) positive coordinates and \(j\) negative coordinates can be formed in \(\binom n{2j}\binom{2j}j\) ways. Sum for \(0\le j\le n/2\), then multiply by the two initial signs. Equivalently, the balanced words are counted by the constant coefficient of \((z^{-1}+1+z)^n\). This completes the exact finite-dimensional assertion.

**6. Growth.** By Fourier inversion, the central coefficient is
\[
 [z^0](z^{-1}+1+z)^n
 =\frac1{2\pi}\int_{-\pi}^{\pi}(1+2\cos\theta)^n\,d\theta.
\]
Near its unique point of maximal absolute value \(\theta=0\), the base has expansion \(3-\theta^2+O(\theta^4)\). A standard Gaussian Laplace estimate gives
\[
 [z^0](z^{-1}+1+z)^n
 \sim\frac{\sqrt3}{2\sqrt{\pi n}}\,3^n.
\]
Every compact subset away from zero has strictly smaller absolute base than three, so it contributes exponentially less. Multiplication by two gives the stated asymptotic.

## Verification
The included Python 3 standard-library file `verify.py` performs independent exact enumerations of signed flows on the bipyramid for \(n=4,6,8,10\), and independently enumerates all integral anchored Lipschitz potentials on the primal prism for \(n=4,6\), checking the connectedness of their saturated-edge graphs. A third exact Laurent-transfer calculation checks the coefficient identity for \(2\le n\le20\). All \(25\) programmed top-level assertions pass. These checks establish finite consistency, not the infinite theorem; Steps 1–6 supply the infinite proof.

## Relationship to prior work
D’Alì, Delucchi and Michałek [1], Proposition 4.33, establish the general correspondence between facets for *all* planar connected bipartite graphs and nowhere-zero integer \(2\)-flows on their duals. Their Proposition 4.29 explicitly evaluates the outerplanar case, including open ladders, but an even circular ladder is not outerplanar. The present contribution is an **explicit evaluation of the bipyramid flow count** and a sharp two-to-one classification by balanced ternary words, not a claim that the underlying flow correspondence is new. Chen, Davis and Korchevskaia [2] give a general facet-subgraph correspondence, without the even-prism evaluation in the material inspected. The polytope/metric-space identification is also classical [1].

## Limitations
The result addresses facet counts of real Lipschitz-free unit balls for even, unweighted prism graph metrics only. It does not give the complete face vector, odd-prism facet enumeration, or results for weighted prisms. The finite checks do not certify all dimensions. The bibliography comparison does not exclude unindexed or inaccessible equivalent evaluations, and no independent scientific audit has occurred.

## References
[1] A. D’Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193 (first public version 2019-10-11), Sections 2.3, 4.4 and Proposition 4.33. https://arxiv.org/html/1910.05193v1

[2] T. Chen, R. Davis, E. Korchevskaia, *Facets and facet subgraphs of symmetric edge polytopes*, arXiv:2107.12315 (first public version 2021-07-26). https://arxiv.org/abs/2107.12315
