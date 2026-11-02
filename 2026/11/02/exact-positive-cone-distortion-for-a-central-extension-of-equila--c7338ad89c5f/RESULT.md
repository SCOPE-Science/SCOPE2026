# Exact positive-cone distortion for a central extension of equilateral metrics

## Finding
Let \(k\ge2\) be an integer, \(0<p\le1\), and \(1/2\le r\le1\). Take the equilateral pointed metric \(N=\{o,x_1,\ldots,x_k\}\) with all nonzero distances equal to \(1\). Adjoin a point \(c\) to form \(M=N\cup\{c\}\), with \(d(c,y)=r\) for every \(y\in N\). Write \(J:\mathcal F_p(N)\to\mathcal F_p(M)\) for the canonical linear embedding and \(C=\{\sum_{i=1}^k a_i\delta_N(x_i):a_i\ge0\}\) for the nonnegative Dirac-coordinate cone. Then the exact inverse distortion restricted to \(C\) is
\[
\boxed{\sup_{v\in C\setminus\{0\}}\frac{\|v\|_{\mathcal F_p(N)}}{\|Jv\|_{\mathcal F_p(M)}}=\max\!\left\{1,\frac{1}{r(1+k^{p-1})^{1/p}}\right\}.}
\]
More precisely, every \(a_1,\ldots,a_k\ge0\) satisfies the complete positive-charge formula
\[
\boxed{\left\|\sum_{i=1}^ka_i\delta_M(x_i)\right\|_{\mathcal F_p(M)}^p=\min_{S\subseteq\{1,\ldots,k\}}\left\{\sum_{i\notin S}a_i^p+r^p\left(\sum_{i\in S}a_i^p+\left(\sum_{i\in S}a_i\right)^p\right)\right\}.}
\]
The corresponding norm in \(\mathcal F_p(N)\) has \(p\)-th power \(\sum_{i=1}^ka_i^p\). For \(p<1\), the cone distortion is greater than \(1\) exactly when \(r<(1+k^{p-1})^{-1/p}\); in that region equal positive coefficients are extremal. At the tight metric midpoint \(r=1/2\), this happens exactly when \(k>(2^p-1)^{-1/(1-p)}\). For fixed \(0<p<1\) and \(1/2\le r<1\), the distortion tends to \(1/r\) as \(k\to\infty\). For \(p=1\), it is identically one.

## Assumptions and scope
All scalars are real. The free \(p\)-spaces use the standard pointed Dirac convention \(\delta(o)=0\) and their maximal \(p\)-norms linearizing the metric. The distance table is a metric because \(r\ge1/2\), and \(r\le1\) is the range in which the center edges are no longer than the equilateral edges. The supremum is **only over nonnegative Dirac coefficients**, not over the whole linear span: this is a cone-restricted distortion and furnishes a lower bound, not an exact formula, for the full inverse operator norm \(\|J^{-1}\|\). No signed-coefficient assertion is made.

## Proof
We use the spanning-tree norm formula of Cúth and Raunig [1, Theorem 2.2]. For a positive vector \(a=(a_1,\ldots,a_k)\), root a spanning tree of the finite metric at \(o\); every edge directed toward the root carries the sum of the nonnegative charges in its descendant subtree. Its \(p\)-cost is the sum over nonroot edges of the edge length raised to \(p\), multiplied by the corresponding subtree mass raised to \(p\). The free \(p\)-norm to the \(p\)-th power is the minimum of these tree costs. The new vertex \(c\) has charge zero.

First, any tree on \(M\) can be transformed without increasing its cost so that the parent of \(c\) is the root \(o\). If \(c\) is not already rooted directly at \(o\), delete its parent edge and attach \(c\) to \(o\). Both center edges have length \(r\), the mass of the entire \(c\)-subtree and the cost of its new edge are unchanged, and every old ancestor edge between its former parent and \(o\) now transports a smaller nonnegative charge. No other edge changes cost. Thus the transformation is nonexpansive.

Second, whenever a vertex \(x_i\) is the parent of another leaf vertex \(x_j\), reattach the subtree rooted at \(x_j\) directly to the parent of \(x_i\). This is still a tree. The replaced edge had length one; the new edge has length either one or \(r\le1\). The descendant mass of \(x_j\) is unchanged; the mass carried by the edge from \(x_i\) to its parent weakly decreases, and all ancestor flows are unchanged. Therefore cost again does not increase. Repeating (each move strictly shortens an offending leaf-to-leaf root path) eventually yields a tree consisting of \(o\! -\! c\) and, for each \(i\), exactly one edge joining \(x_i\) either to \(o\) or to \(c\).

Let \(S\) denote the indices joined to \(c\). The direct edges to \(o\) contribute \(\sum_{i\notin S}a_i^p\); the edges \(x_i\! -\! c\) contribute \(r^p\sum_{i\in S}a_i^p\); and the edge \(c\! -\! o\) contributes \(r^p(\sum_{i\in S}a_i)^p\). Every subset \(S\) gives such a tree. Hence the boxed exact norm formula. The identical tree argument on the equilateral metric \(N\), without \(c\), collapses all parent-child chains to direct root edges and gives \(\|\sum_i a_i\delta_N(x_i)\|^p=\sum_i a_i^p\).

Put \(T=\sum_i a_i^p\). For a nonempty \(S\) of size \(m\), write \(t=\sum_{i\in S}a_i^p\), \(u=T-t\), and \(b=\sum_{i\in S}a_i\). The concavity of \(z\mapsto z^p\), or the finite power-mean inequality, yields \(b^p\ge m^{p-1}t\ge k^{p-1}t\). Therefore the cost of the subset \(S\) is at least \(u+\alpha t\), where \(\alpha=r^p(1+k^{p-1})\). The same bound is immediate when \(S\) is empty. In particular every tree cost is at least \(\min\{1,\alpha\}T\), proving that the distortion is at most \(\max\{1,\alpha^{-1/p}\}\).

For the matching lower bound, a vector supported on one leaf has norm exactly one in both free spaces: in \(M\), the direct edge has cost one, while the two-edge center path has cost \(2r^p\ge1\). Thus distortion one is attained. If \(\alpha<1\), take \(a_1=\cdots=a_k=1\). Its \(N\)-cost is \(k\), while the \(M\)-tree with all leaves attached to \(c\) has cost \(r^p(k+k^p)=\alpha k\). The universal lower cost bound forces equality and attains \(\alpha^{-1/p}\). This establishes both boxed formulas and the exact cone distortion.

Finally, \(\alpha<1\) is equivalent to \(r<(1+k^{p-1})^{-1/p}\). At \(r=1/2\) and \(0<p<1\), this is equivalent to \(k>(2^p-1)^{-1/(1-p)}\). With \(p<1\) fixed, \(k^{p-1}\to0\), proving the claimed limit. At \(p=1\), \(\alpha=2r\ge1\) and the distortion is one.

## Verification
The included standalone `CHECK.py` enumerates all \(7^5=16{,}807\) labeled spanning trees on the seven-point metric with five nonbase leaves and the additional center. For \(p=r=1/2\) and five different nonnegative charge vectors, it compares the minimum of their weighted descendant-flow costs against the exact subset formula, with discrepancies less than \(2\times10^{-14}\) in the performed floating-point run. This is a diagnostic consistency test, not an exhaustive proof for all coefficients, exponents or dimensions; the proof above provides the unrestricted statement.

## Relationship to prior work
Cúth and Raunig [1] derive the general finite spanning-tree formula and foundational inclusion bounds. That structural theorem supplies the key reduction, but the inspected tree theorem and embedding results do not explicitly specialize to the center-star positive-cone minimization or its threshold. Albiac, Ansorena, Cúth and Doucha [2] establish non-isometric inclusions for \(p<1\), without the stated uniform positive-charge family. A published result [3] computes the universal \(p\)-Banach **Lipschitz extension trace** for an equilateral boundary and its star center; that is a different variational problem, with the center image optimized over arbitrary targets. Neither its trace constant nor its barycentric extension optimizer determines the restricted inverse norm of a canonical map between two Lipschitz-free \(p\)-spaces. A later study [4] establishes general isomorphic inclusion; its broad bounds do not state this exact finite-cone formula.

## Limitations
The exact inverse distortion concerns only the nonnegative Dirac cone, so it is not an upper bound for the full inverse operator norm on signed vectors. The range \(r\in[1/2,1]\) is essential to the simple tree-shortening argument. The theorem does not address arbitrary one-point extensions or complex free spaces. Although inspected sources do not explicitly give this formula, a logically equivalent positive-cone statement in less indexed prior work cannot be excluded without independent bibliographic assessment.

## References
[1] Marek Cúth and Tomáš Raunig, *Canonical embedding of Lipschitz-free \(p\)-spaces*, arXiv:2311.02920v1, first posted 2023-11-06; especially Theorems 2.2 and 2.8 and Section 3. https://arxiv.org/abs/2311.02920

[2] Fernando Albiac, José L. Ansorena, Marek Cúth and Michal Doucha, *Lipschitz free \(p\)-spaces for \(0<p<1\)*, arXiv:1811.01265v1, 2018. https://arxiv.org/abs/1811.01265

[3] *Sharp leaf-count transitions in one-point \(p\)-Banach Lipschitz extensions*, published mathematical research record, 2026-10-11. https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-leaf-count-transitions-in-one-point-p-banach-lipschitz-ext--b03e5cc2b3f1

[4] Fernando Albiac and José L. Ansorena, *Lipschitz extensions into \(p\)-Banach spaces, and canonical embeddings of Lipschitz-free \(p\)-spaces for \(0<p<1\)*, arXiv:2603.28193v1, 2026. https://arxiv.org/abs/2603.28193
