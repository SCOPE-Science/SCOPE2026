# Sharp anisotropic amplification for bilinear Lipschitz-free \(p\)-interpolation

## Finding
For every \(0<p\leq1\), let \(V_{a,b}=\{(0,0),(a,0),(0,b),(a,b)\}\) carry its inherited Manhattan metric, where \(a,b>0\). On \([0,1]^2\) equip the source with \(d_{a,b}((s,t),(u,v))=a|s-u|+b|t-v|\). Let the canonical bilinear vertex interpolation map into the real Lipschitz-free \(p\)-space \(\mathcal F_p(V_{a,b})\) be
\[
r_{a,b}(s,t)=(1-s)(1-t)\delta_{00}+(1-s)t\delta_{01}+s(1-t)\delta_{10}+st\delta_{11}.
\]
The coefficients sum to one, and the expression is interpreted modulo the basepoint. Its Lipschitz constant \(\kappa_p(a,b)\) satisfies
\[
\kappa_p(a,b)\leq3^{1/p-1},\qquad
\lim_{b/a\to\infty}\kappa_p(a,b)=\lim_{b/a\to0}\kappa_p(a,b)=3^{1/p-1}.
\]
Consequently \(\sup_{a,b>0}\kappa_p(a,b)=3^{1/p-1}\). At \(p=1\), all aspect ratios have \(\kappa_1(a,b)=1\). For \(0<p<1\), the sharp anisotropic supremum strictly exceeds the previously determined unit-square constant \(\kappa_p(1,1)=(2+2^p)^{1/p}/4\).

## Assumptions and scope
All spaces and coefficients are real, \(0<p\le1\), and both edge lengths are strictly positive. The \(p\)-free norm is the usual infimum of \(\ell_p\)-molecular costs \((\sum_j |c_j|^p d(x_j,y_j)^p)^{1/p}\) among representations \(\mu=\sum_j c_j(\delta_{x_j}-\delta_{y_j})\) of a zero-total-mass measure. The claim is a sharp *uniform-over-aspect-ratio* bound and its asymptotic attainment, not a closed formula for every finite unequal aspect ratio. The number three is the number of edges in a spanning tree of four vertices.

## Proof
**A finite-flow lemma.** On any finite metric space with four vertices, the \(p\)-free norm of a zero-total-mass signed measure \(\mu\) is
\[
\|\mu\|_{\mathcal F_p}^p=\min_{T}\sum_{e\in T}d(e)^p|f_e(T,\mu)|^p,
\]
where \(T\) runs through the spanning trees of the complete four-vertex graph and \(f_e\) is the unique signed flow with divergence \(\mu\) along the edges of \(T\). Indeed, molecular representations correspond to edge flows, with parallel copies consolidated using \(|x+y|^p\le|x|^p+|y|^p\). On a nonzero undirected cycle, adding a multiple of a circulation leaves the divergence unchanged. Between successive edge-zero crossings, the sum of absolute \(p\)-powers of affine edge flows is concave, so it cannot have a strict interior minimum; replacing the flow by an endpoint eliminates an edge without raising its cost. Repeating leaves a forest, which may be augmented by zero-flow edges to a spanning tree. Conversely each tree gives an admissible molecular representation. The same argument at \(p=1\) gives an optimal transport flow on at most three edges.

**Universal bound.** Given any \(\mu\), take a minimum-cost \(p=1\) tree flow with at most three nonzero edges and set \(z_e=d(e)|f_e|\). The concavity inequality \(\sum_{e=1}^3 z_e^p\le3^{1-p}(\sum_{e=1}^3z_e)^p\) shows
\[
\|\mu\|_{\mathcal F_p}\le3^{1/p-1}\|\mu\|_{\mathcal F_1}.
\]
The weights in \(r_{a,b}(s,t)\) form a product Bernoulli distribution at the four vertices. Couple the two Bernoulli factors monotonically for each coordinate. Its expected Manhattan transport cost is exactly \(a|s-u|+b|t-v|\). The ordinary free-space norm is no larger than that cost. Together these yield \(\operatorname{Lip}(r_{a,b})\le3^{1/p-1}\). For \(p=1\), two distinct vertices realize ratio one, proving equality.

**Anisotropic sharpness.** Uniform common scaling of \(a,b\) preserves the Lipschitz ratio; assume \(a=1\), \(b=B\). At \((s,t)=(1/2,1/2)\) take a directional derivative along \(h_B=(2/3,1/(3B))\); its weighted source norm is exactly one. In vertex order \((00,01,10,11)\), the derivative measure is
\[
\mu_B=\bigl(-\tfrac13-\tfrac1{6B},-\tfrac13+\tfrac1{6B},\tfrac13-\tfrac1{6B},\tfrac13+\tfrac1{6B}\bigr).
\]
Thus \(\kappa_p(1,B)\ge\|\mu_B\|_{\mathcal F_p}\). Apply the finite-flow lemma over the sixteen spanning trees. The horizontal edges \(00\!\leftrightarrow\!10\) and \(01\!\leftrightarrow\!11\) both have length one; all four other edges have length at least \(B\). A tree including both horizontal edges has one connecting long edge. Its long-edge flow equals the total mass on one horizontal pair, \(\pm1/(3B)\), and the two horizontal flows each tend in absolute value to \(1/3\). Hence its \(p\)-cost tends to \(3(1/3)^p=3^{1-p}\). For a tree omitting a horizontal edge, suppose its \(p\)-cost remained bounded on a sequence \(B\to\infty\). Every long-edge flow would tend to zero; the limiting nonzero masses \((-1/3,-1/3,1/3,1/3)\) would then have to be balanced using only the remaining horizontal edges. Both horizontal edges are necessary for this, a contradiction. Thus all trees omitting a horizontal edge have divergent cost. The minimum of the finitely many tree costs therefore converges to \(3^{1-p}\), and
\[
\lim_{B\to\infty}\|\mu_B\|_{\mathcal F_p}=3^{1/p-1}.
\]
The universal upper bound finishes the limit. Swapping coordinates proves the reciprocal-aspect limit.

**Comparison with the square.** For \(0<p<1\), the three positive loads \((1/2,1/4,1/4)\) of the known unit-square extremizer are unequal. Strict concavity implies \((2+2^p)^{1/p}/4<3^{1/p-1}\), establishing genuine anisotropic amplification relative to the previously known square constant.

## Verification
The included standalone `CHECKER.py` enumerates all 16 labelled spanning trees, computes the exact tree flows from vertex cuts and evaluates the directional lower bound for \(B=1,2,4,8,32,128,512\) and \(p\in\{1/2,3/4,1\}\). Every value respects the bound; values approach it as \(B\) increases. The script is a finite diagnostic only. The claims for all aspect ratios and the limit rely on the preceding proof, especially the flow-cycle elimination lemma and the finite-tree limiting argument.

## Relationship to prior work
Bíma [1] studies canonical coordinatewise-affine retractions onto vertices of unions of equal-edge-length cubes, and establishes dimension/exponent-dependent bounds. The later exact unit-square result [2] gives \((2+2^p)^{1/p}/4\) at equal side lengths. The present result instead optimizes across arbitrary rectangular aspect ratios and identifies the sharp singular aspect-ratio limit; neither cited equal-side-length statement gives this anisotropic supremum. This is a comparison of claims, not a claim of exhaustive bibliographic uniqueness.

## Limitations
No closed formula, optimizer classification, or strict nonattainment assertion is made for an arbitrary finite aspect ratio. The proof is restricted to four real vertices with the Manhattan product metric and the canonical bilinear interpolation map. Relevant unpublished or poorly indexed generalizations may remain undiscovered; independent scientific audit has not occurred.

## References
[1] Jan Bíma, *Lipschitz Free Spaces and Subsets of Finite-Dimensional Spaces*, arXiv:2303.03265v1 (first public 2023-03-06), https://arxiv.org/abs/2303.03265.

[2] *The sharp square-cell constant for Lipschitz-free \(p\)-interpolation*, published-finding corpus research record, 2026-10-11, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-the-sharp-square-cell-constant-for-lipschitz-free-p-interpolatio--23ae4bb01450. Relevant indexed claim: exact unweighted square constant. Full underlying proof was not available during this comparison.
