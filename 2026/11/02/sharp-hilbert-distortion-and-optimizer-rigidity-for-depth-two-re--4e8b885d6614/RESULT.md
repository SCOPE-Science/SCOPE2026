# Sharp Hilbert distortion and optimizer rigidity for depth-two regular trees

## Finding

For integers \(r,s\ge2\), let \(T_{r,s}\) be the tree with root \(o\), intermediate vertices \(c_1,\ldots,c_r\), and leaves \(\ell_{ij}\) for \(1\le i\le r\), \(1\le j\le s\). Its edges are \(oc_i\) and \(c_i\ell_{ij}\), each of unit length. All vertices, not merely leaves, carry the shortest-path metric \(d\).

Set
\[
 a=\frac{r-1}{r},\quad u=\frac{s-1}{s},\quad t=2u,\quad
 L=8-t,\quad B=aL+t.
\]
The least real-Hilbert bi-Lipschitz distortion, with arbitrary target dimension, is exactly
\[
 \boxed{c_2(T_{r,s})=\frac{B}{2\sqrt{aL}}},\qquad
 \boxed{c_2(T_{r,s})^2=\frac{[a(8-2u)+2u]^2}{4a(8-2u)}}.
\]
All optimal embeddings, normalized to \(d(p,q)\le\|f(p)-f(q)\|\le c_2d(p,q)\), are congruent. Every such embedding has affine dimension exactly \(rs-1\). Moreover \(c_2\) increases strictly with either \(r\) or \(s\), and
\[
 \lim_{r,s\to\infty}c_2(T_{r,s})=\sqrt{8/3}.
\]
For the seven-vertex binary tree, \(r=s=2\), one obtains \(c_2^2=81/56\) and affine dimension three.

## Assumptions and scope

All Hilbert spaces are real. Distortion is the infimum of \(L/l\) over injective maps \(f\) having \(l d(p,q)\le\|f(p)-f(q)\|\le Ld(p,q)\) for all distinct vertices. Rescaling allows \(l=1\). The result concerns exactly \(1+r+rs\) vertices, not their edge continua. Both integer parameters are at least two. No assertion is made for weighted edges, other depths, nonregular branching, or a prescribed target dimension smaller than \(rs-1\).

## Proof

**1. An obstruction valid for every embedding.** Suppose \(f\) is noncontracting with expansion at most \(D\); translate so that \(f(o)=0\). Write \(x_i=f(c_i)\) and \(z_{ij}=f(\ell_{ij})\). Define their branch means \(b_i=s^{-1}\sum_jz_{ij}\) and global means \(\bar x=r^{-1}\sum_i x_i\), \(\bar b=r^{-1}\sum_i b_i\). Define nonnegative variances
\[
 X=\frac1r\sum_i\|x_i-\bar x\|^2,\quad
 Y=\frac1r\sum_i\|b_i-\bar b\|^2,\quad
 W=\frac1{rs}\sum_{i,j}\|z_{ij}-b_i\|^2,
\]
and \(Z=r^{-1}\sum_i\langle x_i-\bar x,b_i-\bar b\rangle\). Cauchy--Schwarz gives \(Z\le\sqrt{XY}\).

The average squared root-to-child distance equals \(\|\bar x\|^2+X\le D^2\), hence \(X\le D^2\). The average squared child-to-own-leaf distance equals
\[
 \|\bar x-\bar b\|^2+X+Y-2Z+W\le D^2.
\]
Consequently
\[
 W\le D^2,\qquad
 \sqrt Y\le\sqrt X+\sqrt{D^2-W}\le D+\sqrt{D^2-W}. \tag{1}
\]
The mean squared distance of distinct leaves in the *same* branch is \(2W/u\); since every such tree distance equals two, \(W\ge2u=t\). The mean squared distance of leaves in *different* branches is \(2Y/a+2W\); since every such tree distance equals four, \(Y/a+W\ge8\). Combining with (1) gives
\[
 8a\le aW+\big(D+\sqrt{D^2-W}\big)^2. \tag{2}
\]
For fixed \(D\), the function \(w\mapsto aw+(D+\sqrt{D^2-w})^2\) is strictly decreasing on \([0,D^2]\): its interior derivative is \(a-1-D/\sqrt{D^2-w}<0\). As \(W\ge t\), (2) therefore implies
\[
 a(8-t)\le\big(D+\sqrt{D^2-t}\big)^2. \tag{3}
\]
Here \(a(8-t)>t\), since \(a\ge1/2\), \(1\le t<2\), so the left side is at least three whereas \(t<2\). As \(D^2\ge t\), the right side of (3) increases strictly with \(D\). Solving equality yields \(D=[a(8-t)+t]/[2\sqrt{a(8-t)}]\). Thus (3) proves the stated universal lower bound, without symmetry assumptions on \(f\).

**2. A matching explicit embedding.** In \(\mathbb R^r\), take centered coordinate-simplex vectors \(h_i=e_i-r^{-1}\sum_ke_k\), so \(\langle h_i,h_k\rangle=\mathbf1_{i=k}-1/r\). For each \(i\), take a mutually orthogonal copy of \(\mathbb R^s\) with centered vectors \(g_{ij}=e_{ij}-s^{-1}\sum_le_{il}\). All the \(g\)-spaces are orthogonal to the \(h\)-space. Set
\[
 y=\sqrt{L},\quad x=\frac{B}{2a\sqrt L},\quad
 f(o)=0,\qquad f(c_i)=xh_i,\qquad
 f(\ell_{ij})=yh_i+\sqrt2\,g_{ij}. \tag{4}
\]
Let \(Q=B^2/(4aL)\). Since \(a x^2=Q\), \(2axy=B\), and \(ay^2+t=B\), direct inner products give the following **complete list** of squared image distances:
\[
\begin{array}{c|c|c}
\text{pair type}&d^2&\|f(p)-f(q)\|^2\\\hline
(o,c_i)&1&Q\\
(o,\ell_{ij})&4&B\\
(c_i,c_k),\ i\ne k&4&2Q/a\\
(c_i,\ell_{ij})&1&Q\\
(c_i,\ell_{kj}),\ i\ne k&9&Q+B/a\\
(\ell_{ij},\ell_{il}),\ j\ne l&4&4\\
(\ell_{ij},\ell_{kl}),\ i\ne k&16&16
\end{array} \tag{5}
\]
All entries lie between \(d^2\) and \(Qd^2\). Indeed, \(Q\ge t\ge1\), \(B\ge8a\ge4\), and \(B\le4Q\) because \(B\ge aL\). The bound \(2a\le Q\) follows from \(Q=aL/4+t/2+t^2/(4aL)\ge2a+t(2-a)/4\); also \(a\ge1/2\) gives \(2Q/a\le4Q\). Finally, \(B/a=L+t/a\ge8\), so \(Q+B/a\ge9\), while \(L\le2(aL+t)=2B\) gives \(B/a\le8Q\), hence \(Q+B/a\le9Q\). Both the lower and upper distortion extrema in (5) are attained, so \(c_2^2=Q\).

**3. Rigidity and optimal affine dimension.** Suppose an embedding attains the lower bound. Strict monotonicity in (2) forces \(W=t\); equality through (1)--(3) forces \(X=Q\), \(Y=aL\), \(Z=\sqrt{XY}\), \(\bar x=\bar b=0\), and equality in the root-child and child-own-leaf distance upper bounds. Equality in Cauchy--Schwarz on the \(r\)-tuples means \(x_i=\sqrt{X/Y}\,b_i\) for every \(i\). Equality of the two *averaged* leaf noncontraction inequalities forces every within-branch leaf pair to have image distance exactly two and every different-branch leaf pair to have image distance exactly four. Every root-child and child-own-leaf pair likewise has image distance \(\sqrt Q\).

Write \(w_{ij}=z_{ij}-b_i\). The constant within-branch distances and \(\sum_jw_{ij}=0\) force a centered regular simplex of side two, with \(\|w_{ij}\|^2=t\), in each branch. Averaging cross-branch squared distances shows \(\|b_i-b_k\|^2=16-2t=2L\) for every \(i\ne k\), so the centered \(b_i\) form a regular simplex. Holding \(i\ne k\) fixed and averaging the individual cross-branch distance identities over one leaf index shows \(w_{ij}\perp(b_i-b_k)\) and \(w_{kl}\perp(b_i-b_k)\). The remaining cross terms give \(\langle w_{ij},w_{kl}\rangle=0\). Since the differences \(b_i-b_k\) span the center simplex, the residual-simplex spaces are mutually orthogonal and orthogonal to the centers. All Gram entries are therefore uniquely fixed. The rank is \((r-1)+r(s-1)=rs-1\). Thus every optimum is congruent to (4), and this is the precise affine dimension.

**4. Branching monotonicity and limit.** The squared distortion can be written
\[
 Q(a,u)=\frac{a(4-u)}2+u+\frac{u^2}{2a(4-u)}.
\]
For \(1/2\le a<1\), \(1/2\le u<1\),
\[
 \frac{\partial Q}{\partial a}=\frac{4-u}{2}-\frac{u^2}{2a^2(4-u)}>0,\quad
 \frac{\partial Q}{\partial u}=1-\frac a2+\frac{u(8-u)}{2a(4-u)^2}>0.
\]
Thus increasing either branching parameter strictly increases distortion. Substitution of \(a,u\uparrow1\) gives \(Q\to8/3\).

## Verification

The standalone file `verify.py` uses only Python's standard library and exact rational arithmetic. Run `python verify.py` from this package to reconstruct every pairwise graph and squared-image distance for integers \(2\le r,s\le17\), verify all lower/upper distortion inequalities and both attained extremal ratios, and independently check the Gram-factor identities. Its observed output was:

`TREE_DEPTH2_CHECK_OK cases=256 exact_pair_inequalities=1889536 binary_depth2_squared_distortion=81/56 limiting_squared_distortion=8/3`

The verification is finite, whereas the proof above establishes all indicated integer pairs. The construction in (4), or equivalently its rational Gram matrix, supplies an explicit certificate for every pair of parameters without numerical optimization.

## Relationship to prior work

The tree-embedding work of Linial--Magen--Saks provides general asymptotic bounds, and Linial--Saks develops a fork-based lower-bound method for complete binary trees; those results do not explicitly give the finite, two-parameter sharp value or the optimizer rigidity proved here. Babilon--Matoušek--Maxová--Valtr studies fixed-dimensional tree embeddings and subdivided-star fans, rather than unrestricted-dimensional distortion of a two-level branching tree. Robertson's distorted negative-type framework identifies exact Hilbert distortion with the relevant distortion threshold, but its explicit examples concern complete bipartite graphs and Hamming cubes. Existing results on the negative-type exponent of this same two-level tree concern *isometric snowflake embeddings* rather than the least distortion of its original shortest-path metric. This comparison does not establish absolute historical novelty under every possible terminology.

## Limitations

The conclusion is restricted to uniform unit edges, depth exactly two, integer \(r,s\ge2\), and the vertex metric. It does not solve embedding distortion for unbalanced children, larger depth, or fixed-dimensional targets. The published 1998 tree-embedding article was not accessible in full in the checked sources; its abstract states a general bound rather than this exact formula, but unseen content remains a priority risk. No independent mathematical review has been performed.

## References

1. G. Robertson, *Negative Type and Bi-lipschitz Embeddings into Hilbert Space*, arXiv:2309.16070v1, first public 2023-09-27, especially Theorems 2.3--2.4 and Section 4. https://arxiv.org/abs/2309.16070
2. N. Linial and M. Saks, *The Euclidean Distortion of Complete Binary Trees*, Discrete & Computational Geometry 29 (2003), 19--21, DOI:10.1007/s00454-002-2827-z. https://doi.org/10.1007/s00454-002-2827-z
3. R. Babilon, J. Matoušek, J. Maxová and P. Valtr, *Low-Distortion Embeddings of Trees*, Journal of Graph Algorithms and Applications 7 (2003), 399--409, DOI:10.7155/jgaa.00076. https://doi.org/10.7155/jgaa.00076
4. N. Linial, A. Magen and M. Saks, *Low distortion euclidean embeddings of trees*, Israel Journal of Mathematics 106 (1998), 339--348, DOI:10.1007/BF02773475. https://doi.org/10.1007/BF02773475
