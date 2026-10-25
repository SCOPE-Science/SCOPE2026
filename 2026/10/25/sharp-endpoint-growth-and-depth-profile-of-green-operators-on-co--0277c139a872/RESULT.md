# Sharp endpoint growth and depth profile of Green operators on complete branching trees

## Finding
For every integer \(b\ge2\), the sharp endpoint operator norm of the unweighted graph Poisson inverse on the complete rooted \(b\)-ary tree grows linearly with the number of vertices, with limiting coefficient \(2/b\). More precisely, at height \(h\) and order \(N=(b^{h+1}-1)/(b-1)\),
\[
\|L_{b,h}^{\dagger}\|_{\ell^1\to\ell^1}=\|L_{b,h}^{\dagger}\|_{\ell^\infty\to\ell^\infty}=\frac{2}{b}N+O_b(h).
\]
The depth-\(k\) absolute Green row sum divided by \(N\) converges to \(\frac2b(1-b^{-k})\) for fixed depth \(k\). An explicit finite-height error estimate, exact Green kernel, and exact leaf row sum accompany the asymptotics.

## Assumptions and scope
Let \(b\ge2\) and \(h\ge1\) be integers. Identify vertices of the complete rooted \(b\)-ary tree \(T_{b,h}\) with words of length at most \(h\) over an alphabet of \(b\) letters. Words are adjacent when one extends the other by one letter. The root is the empty word; \(|x|\) is the depth of vertex \(x\); \(t(x,y)\) is the length of their longest common prefix. Write
\[
N=\frac{b^{h+1}-1}{b-1},\quad D=b^{h+1}-1,\quad
q_l=\frac{b^{h-l+1}-1}{D}\ (1\le l\le h),\quad
F_h(k)=\sum_{l=1}^{k}q_l,\quad
H_h=\frac1N\sum_{j=0}^{h}b^jF_h(j),\quad
\delta_h=F_h(h)-H_h.
\]
Here \(q_l\) is the fraction of vertices below a specified vertex at depth \(l\), including that vertex. The combinatorial Laplacian is \((Lf)(x)=\sum_{y\sim x}(f(x)-f(y))\). Its Moore--Penrose inverse \(G=L^{\dagger}\) is characterized by \(LG=GL=I-\mathbf1\mathbf1^{\mathsf T}/N\), symmetry, and zero row sums. Endpoint operator norms act on all vertex functions with counting-measure \(\ell^1\) and \(\ell^\infty\) norms; no normalization is imposed on input functions.

## Proof
**Step 1: Exact kernel.** Fix a column \(y\). Sum the equation \(LG(\cdot,y)=\mathbf1_{\{y\}}-\mathbf1/N\) over the descendant subtree \(S\) of a child vertex at depth \(l\). All interior edge terms cancel, leaving
\[
G(\operatorname{child},y)-G(\operatorname{parent},y)=\mathbf1_{\{y\in S\}}-q_l.
\]
Summing these increments along the path from the root to \(x\) shows that \(G(x,y)=G(\varnothing,y)+t(x,y)-F_h(|x|)\). The zero-column-sum normalization implies
\[
G(\varnothing,y)=H_h-F_h(|y|),\qquad
\boxed{G(x,y)=t(x,y)+H_h-F_h(|x|)-F_h(|y|)}.
\]
The resulting expression is symmetric and satisfies the Poisson and centering identities, hence equals the Moore--Penrose inverse.

**Step 2: Absolute row estimates.** Let \(Y\) be uniform on all \(N\) vertices and fix a vertex \(x\) at depth \(k\). Then
\[
\mathbb E\,t(x,Y)=F_h(k),\qquad \mathbb P\{t(x,Y)=0\}=1-q_1\quad(k\ge1).
\]
Moreover \(0\le F_h(k)<\sum_{l=1}^{\infty}b^{-l}\le1\). Thus, because the positive integer values of \(t(x,Y)\) are all greater than its mean,
\[
\mathbb E\bigl|t(x,Y)-F_h(k)\bigr|=2F_h(k)(1-q_1).
\]
For \(k=0\) both sides vanish. The perturbation from this variable to the exact kernel is \(H_h-F_h(|Y|)\). It has mean zero and is bounded below by \(-\delta_h\), hence
\[
\mathbb E\bigl|H_h-F_h(|Y|)\bigr|\le2\delta_h.
\]
The reverse triangle inequality therefore proves, for all \(0\le k\le h\),
\[
\boxed{\left|R_h(k)-2(1-q_1)F_h(k)\right|\le2\delta_h},\qquad
R_h(k)=\frac1N\sum_y|G(x,y)|.
\]
The row value depends only on depth by rooted-tree automorphisms.

**Step 3: Error and endpoint bounds.** The fraction of vertices at depth at least \(l\) equals \(1-(b^l-1)/D\); consequently
\[
\delta_h=\sum_{l=1}^{h}q_l\frac{b^l-1}{D}
=\frac{\sum_{l=1}^{h}(b^{h-l+1}-1)(b^l-1)}{D^2}
\le\frac{h b^{h+1}}{D^2}.
\]
The nonnegative approximant \(2(1-q_1)F_h(k)\) increases with \(k\). Maximizing over the finitely many depths, using the preceding uniform error, gives
\[
\boxed{\left|\frac{\|G\|_{\ell^\infty\to\ell^\infty}}N-2(1-q_1)F_h(h)\right|\le2\delta_h}.
\]
Symmetry yields equality of the induced \(\ell^1\) and \(\ell^\infty\) norms. Now \(q_1\to1/b\), \(F_h(h)\to1/(b-1)\), and \(N\delta_h=O_b(h)\), while \(N\bigl|F_h(h)-1/(b-1)\bigr|=O_b(h)\). Therefore \(\|G\|=(2/b)N+O_b(h)\). For fixed \(k\), \(F_h(k)\to\sum_{l=1}^{k}b^{-l}=(1-b^{-k})/(b-1)\), which gives \(R_h(k)\to(2/b)(1-b^{-k})\). Vertices of depth tending to infinity asymptotically attain the coefficient \(2/b\), as does the global norm.

**Step 4: Exact leaf response.** Fix a leaf \(x\). The kernel is negative exactly when \(t(x,y)=0\) and positive when \(t(x,y)\ge1\). Indeed, at \(t=0\) it is at most \(H_h-F_h(h)<0\); at \(t\ge1\) it is at least \(1+H_h-2F_h(h)>0\). For \(b\ge3\) the last inequality follows from \(F_h(h)<1/(b-1)\le1/2\). When \(b=2\), direct summation gives \(1+H_h-2F_h(h)=(3N-2h-2)/N^2>0\). The opposite-root branches and root comprise the negative set. The mean of \(F_h(|y|)\) is \(H_h\) and each root-child subtree carries exactly \(NH_h/b\) of the sum. The total kernel mass over the negative set is therefore \([H_h-((b-1)N+1)F_h(h)]/b\). Every row sums to zero, so twice the negative absolute mass yields
\[
\boxed{\sum_y|G(x,y)|=\frac2b\left(((b-1)N+1)F_h(h)-H_h\right)}.
\]
No assertion that a leaf maximizes the finite-height global norm is needed for the sharp limiting theorem.

## Verification
The independently evaluated rational test script `check.py` constructs complete rooted trees, computes the stated Green matrix entry-by-entry, and checks \(LG=I-\mathbf1\mathbf1^{\mathsf T}/N\), centering, symmetry, all depth rows, the finite-height estimate, the leaf sign partition, and the closed leaf sum. It passed 9,424 exact-rational assertions across eleven branching/height configurations. These finite tests check algebra and edge cases; the proof above, not finite testing, establishes the assertions for all \(b,h\).

## Relationship to prior work
Kirkland, Neumann and Shader (1997) derived broad generalized-inverse and distance identities for arbitrary weighted trees and studied extrema of diagonal entries. Ranjan, Zhang and Boley (2013) developed Laplacian pseudoinverse formulas and their relationship to effective resistance. These established identities provide the appropriate foundational setting; the new claim is the explicit sharp global \(\ell^1/\ell^\infty\) asymptotic coefficient, complete depth-dependent endpoint row profile, and closed leaf amplification for a growing family of regular rooted trees. The two primary sources' inspected statements do not supply those asymptotics or the depth profile. General tree Green formulas alone should not be confused with an already evaluated sharp endpoint asymptotic; further unknown equivalent results may exist.

## Limitations
The uniform error bounds do not determine the exact finite-height maximizing depth for every \(b,h\), and the height correction \(O_b(h)\) is not optimized. The statements are for complete unweighted rooted trees and the combinatorial Laplacian on counting measure, not arbitrary branching, weighted trees, or probability-normalized Laplacians. Literature priority is provisional pending independent verification, particularly under alternative Green-matrix or distance-matrix terminology. No independent audit is claimed.

## References
1. S. J. Kirkland, M. Neumann and B. L. Shader, *Distances in Weighted Trees and Group Inverse of Laplacian Matrices*, SIAM Journal on Matrix Analysis and Applications **18** (1997), 827–841. DOI: 10.1137/S0895479896298713. Lawful repository copy: https://pdfs.semanticscholar.org/6c13/6f0da4d44678c5251fe9b5a461f6ddbe1164.pdf.
2. G. Ranjan, Z.-L. Zhang and D. Boley, *Incremental Computation of Pseudo-Inverse of Laplacian: Theory and Applications*, first arXiv version 8 April 2013, arXiv:1304.2300, https://arxiv.org/abs/1304.2300.
