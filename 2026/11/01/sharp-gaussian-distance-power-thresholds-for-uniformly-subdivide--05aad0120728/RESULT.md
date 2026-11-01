# Sharp Gaussian distance-power thresholds for uniformly subdivided stars

## Finding

For each integer \(m\ge 3\), let \(T_m\) be the unit-edge tree with one central vertex \(o\) and \(m\) branches \(o-a_i-b_i\), each of length two. Its graph distance is \(d_m\). Permuting the arms gives a natural \(S_m\)-symmetry, and the question is positivity of the resulting invariant distance kernels. Put
\[
\begin{aligned}
 A_m(p)&=m-(m-1)2^{p-1},\\
 B_m(p)&=2^{p-1}-\frac{m-1}{2}(3^p-1-2^p),\\
 F_m(p)&=2^{p/2}A_m(p)+B_m(p),\\
 s_m&=\log_2\!\left(\frac{2m}{m-1}\right).
\end{aligned}
\]
There is exactly one solution \(p_m\in(1,s_m)\) of \(F_m(p_m)=0\). For every \(t>0\), the Gaussian distance-power matrix
\[
 K_{t,p}(x,y)=\exp\!\left(-t\,d_m(x,y)^p\right),\qquad x,y\in V(T_m),
\]
is positive semidefinite **for every \(t>0\)** if and only if \(0\le p\le p_m\). Here \(d_m(x,y)^0\) at \(p=0\) means \(1\) for distinct vertices and \(0\) on the diagonal. For \(p>p_m\), some positive scale \(t\) violates positive semidefiniteness.

The thresholds are strictly decreasing: \(p_{m+1}<p_m\), and are strictly smaller than the corresponding unsubdivided-star threshold \(s_m\). As \(m\to\infty\),
\[
 p_m=1+\frac{c}{m}+O(m^{-2}),\qquad
 c=\frac{1+\sqrt2}{\sqrt2\log2+\frac12(3\log3-2\log2)}
 =1.247636634086\ldots.
\]
For the squared-Euclidean metric \(d_m^{p_m}\), the least possible affine dimension of a Hilbert-space realization is exactly \(2m-1\), whereas for every \(0\le p<p_m\) it is \(2m\). The unique endpoint zero-energy direction, up to scale, puts coefficient \(2^{p_m/2}\) on every \(a_i\), coefficient \(1\) on every \(b_i\), and coefficient \(-m(1+2^{p_m/2})\) on \(o\). The exception \(m=2\) is the five-vertex path: its critical exponent is \(2\) and its endpoint Euclidean dimension is \(1\).

## Assumptions and scope

All graphs are finite, undirected, and equipped with their unit-edge shortest-path metric. Throughout the nondegenerate theorem \(m\) is an integer at least three, \(p\ge0\), and the all-scales quantifier in the Gaussian criterion is essential. The endpoint embedding dimension refers to squared Euclidean distances \(\|z_x-z_y\|^2=d_m(x,y)^p\), not to realizing the original graph metric itself as Euclidean distance. Positive semidefiniteness is asserted for **all** positive scales at the admitted exponents, not for an arbitrarily chosen fixed scale.

## Proof

**Step 1: Schoenberg reduction and arm blocks.** A symmetric zero-diagonal kernel \(d^p\) is conditionally negative semidefinite exactly when \(\exp(-t d^p)\) is positive semidefinite at every \(t>0\). Fix \(o\) as the basepoint. The corresponding Schoenberg Gram matrix on the remaining \(2m\) vertices has entries
\[
 G_p(x,y)=\frac{d_m(o,x)^p+d_m(o,y)^p-d_m(x,y)^p}{2}.
\]
Writing the two coordinates of branch \(i\) as \((a_i,b_i)\), the diagonal and off-diagonal branch blocks, respectively, are
\[
 D_p=\begin{pmatrix}1&u\\u&v\end{pmatrix},\qquad
 O_p=\begin{pmatrix}1-u&(1+v-w)/2\\(1+v-w)/2&v-v^2/2\end{pmatrix},
\]
where \(u=2^{p-1}\), \(v=2^p\), and \(w=3^p\). The harmonic decomposition for the arm-permutation action splits branch labels into the trivial representation and the \((m-1)\)-dimensional standard representation. Orthogonal decomposition of the branch-label space into its constant vector and its \((m-1)\)-dimensional zero-sum space shows that \(G_p\) is orthogonally congruent to the direct sum of \(m-1\) copies of \(Q_p=D_p-O_p\) and one copy of \(P_{m,p}=D_p+(m-1)O_p\).

**Step 2: positivity of the nonconstant-label sectors.** For \(1<p<2\), the matrix \(H_p=-O_p\) is strictly positive definite. Indeed, for any \(r,s>0\),
\[
 (r+s)^p-r^p-s^p
 =\frac{p(p-1)}{\Gamma(2-p)}
 \int_0^\infty(1-e^{-rt})(1-e^{-st})t^{-p-1}\,dt.
\]
Apply this to \(r,s\in\{1,2\}\). The two functions \(1-e^{-t}\) and \(1-e^{-2t}\) are linearly independent, so the displayed integral is strictly positive definite as a two-by-two Gram kernel. On the other hand \(D_p\succ0\) for \(p<2\), since \(\det D_p=2^p(1-2^{p-2})>0\). Thus \(Q_p=D_p+H_p\succ0\), so all possible critical degeneracy is in the branch-constant two-dimensional sector.

**Step 3: the one-dimensional sharp equation.** Directly,
\[
 P_{m,p}=\begin{pmatrix}A_m(p)&B_m(p)\\B_m(p)&2^p A_m(p)\end{pmatrix},\qquad
 \det P_{m,p}=[2^{p/2}A_m(p)-B_m(p)]F_m(p).
\]
At \(p=1\), \(A_m(1)=B_m(1)=1\), so \(F_m(1)=1+\sqrt2>0\). At \(p=s_m\), \(A_m(s_m)=0\). Since
\[
 g(p)=\log(3^p-1)-p\log4+\log2
\]
has \(g(1)=g(2)=0\) and strictly negative second derivative
\[
 g''(p)=-\frac{(\log3)^2 3^p}{(3^p-1)^2}<0,
\]
it follows that \(3^p-1>4^p/2\) whenever \(1<p<2\). At \(p=s_m\), this makes \(B_m(s_m)<0\) and hence \(F_m(s_m)<0\). Finally, on \([1,s_m]\),
\[
 \frac{d}{dp}\bigl[2^{p/2}A_m(p)\bigr]
 =\frac{2^{p/2}\log2}{2}\left[m-3(m-1)2^{p-1}\right]<0
\]
and
\[
 B_m'(p)=2^{p-1}\left[m\log2-(m-1)(3/2)^p\log3\right]<0.
\]
The inequalities hold for every \(m\ge3\) and \(p\ge1\). Thus \(F_m\) has exactly one root \(p_m\in(1,s_m)\).

At that root, \(A_m(p_m)>0\) and \(B_m(p_m)=-2^{p_m/2}A_m(p_m)\). Therefore \(P_{m,p_m}\) is positive semidefinite of rank one, with null vector \((2^{p_m/2},1)\). Along with \(Q_{p_m}\succ0\), this proves that \(d_m^{p_m}\) is conditionally negative semidefinite. Since a positive power at most one of a conditionally negative semidefinite nonnegative kernel is again conditionally negative semidefinite, all \(0<p\le p_m\) are admissible; \(p=0\) follows from the discrete metric.

For \(p_m<p<s_m\), strict decrease of both \(F_m\) and \(B_m\) gives \(F_m(p)<0\) and \(B_m(p)<0\). Then \(2^{p/2}A_m(p)-B_m(p)>0\), so \(\det P_{m,p}<0\). At \(p=s_m\), the diagonal entry \(A_m=0\) but \(B_m<0\), again excluding positive semidefiniteness. For \(p>s_m\), \(A_m(p)<0\), which is already impossible for a positive semidefinite Gram matrix. This proves the claimed **exact** interval, not just a local threshold.

**Step 4: endpoint geometry and monotonicity.** The multiplicity of the positive \(Q\)-sector is \(m-1\), and the single \(P\)-sector has rank one at the threshold. Thus \(\operatorname{rank}G_{p_m}=2(m-1)+1=2m-1\), with null direction constant across branches as specified. By the standard strict-negative-type theorem for finite metrics, strict conditional negative definiteness holds for every \(0\le p<p_m\); equivalently, \(G_p\succ0\) and its rank is \(2m\). At fixed \(1<p<2\), \(P_{m+1,p}=P_{m,p}-H_p\) with \(H_p\succ0\). Evaluating the new matrix on the endpoint null vector for \(m\) yields a negative value, hence \(p_{m+1}<p_m\). The special \(m=2\) tree is a five-point subset of the real line, giving the stated exponent and dimension.

**Step 5: sharp large-branch asymptotic.** Since \(1<p_m<s_m\) and \(s_m=1+1/(m\log2)+O(m^{-2})\), write \(p_m=1+x_m/m\) with \((x_m)\) bounded. Uniform Taylor expansion for bounded \(x\) gives
\[
 F_m(1+x/m)=1+\sqrt2-x\left(\sqrt2\log2+\frac12(3\log3-2\log2)\right)+O(m^{-1}).
\]
Using \(F_m(p_m)=0\) implies \(x_m=c+O(m^{-1})\), proving the stated asymptotic with its explicit coefficient.

## Verification

Run `python3 verification/check_subdivided_star.py` with Python 3 and no nonstandard dependencies. The direct-distance Gram matrix, derived block matrices, endpoint ranks, and exact root interval are checked for multiple branch counts; a second numerical path independently computes tree distances, and fixed-power tests check both sides of each threshold. The included execution passed 443 deterministic assertions, with representative roots \(p_3\approx1.553978601036\), \(p_4\approx1.383482745300\), \(p_8\approx1.171976965867\), and \(p_{100}\approx1.012569973724\). These are finite corroborations; the proof above supplies the universal quantifiers.

## Relationship to prior work

Doust and Weston (arXiv:0705.0411) established strict negative type estimates for finite trees and the exact one-level star exponent \(s_m\). Their special-case star contains no intermediate degree-two vertices, whereas the present tree has \(m\) intermediate vertices and distinct distances from one to four. Li and Weston (arXiv:0901.0695) established interval and strictness principles, used in the full-rank conclusion. Sánchez (arXiv:1108.0451) supplied a general finite-metric distance-matrix criterion and a complete-bipartite graph formula; applying that criterion alone does not state the present scalar threshold, rank direction, strict subdivision comparison, or asymptotic coefficient. These foundational facts are not claimed as new. The claimed contribution is the complete closed scalar and geometric classification for **uniform two-edge subdivisions of stars**, together with its strict arm-count law and sharp coefficient.

## Limitations

The theorem is for equal unit-length two-edge arms and does not classify arbitrary branch lengths, irregular subdivided stars, or a single fixed Gaussian scale. A finite numerical checker is not an independent proof or a substitute for the analytic inequalities. Searches of accessible literature do not rule out an unindexed historically equivalent negative-type calculation, and no independent mathematical validation has been performed.

## References

1. I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, arXiv:0705.0411, first publicly posted 2007-05-03; corrected full text: https://arxiv.org/html/0705.0411v2 .
2. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695, first publicly posted 2009-01-06; full text: https://arxiv.org/html/0901.0695v3 .
3. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first publicly posted 2011-08-02; full text: https://arxiv.org/html/1108.0451v1 .
