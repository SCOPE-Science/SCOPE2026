# Parity-controlled nonlocal precision in uniformly colored cycles

## Finding
Let \(n\ge3\) and \(q\ge3\) be integers. Color the vertices of the cycle \(C_n\) uniformly from its proper \(q\)-colorings and fix one distinguished color. Put \(X_i=\mathbf1\{\text{vertex }i\text{ has the distinguished color}\}\), \(\Sigma=\operatorname{Cov}(X_1,\ldots,X_n)\), and, whenever it exists, \(Q=\Sigma^{-1}\).

**Complete precision sign law.** The only singular case is \((n,q)=(3,3)\), where \(\Sigma\) has rank two. In all other cases \(\Sigma\) is positive definite, and for distinct vertices \(i,j\),
\[
Q_{ij}>0\quad\text{if }i,j\text{ are adjacent},
\]
\[
\operatorname{sgn}(Q_{ij})=(-1)^{n+1}\quad\text{if }i,j\text{ are nonadjacent}.
\]
Thus every full-order **linear** partial correlation \(-Q_{ij}/\sqrt{Q_{ii}Q_{jj}}\) is negative when \(n\) is odd; when \(n\) is even, it is negative for neighbors and positive for every nonneighbor. The parity law applies to every admissible number of colors, not only to a large-cycle limit.

The full matrices have explicit closed forms. Define
\[
b=q-1,\quad r=-\frac1b,\quad t=r^n,\quad
 a=\frac{b}{q^2(1+bt)},\quad c=(b-1)t,
\]
\[
g=\frac{(1-t)(1+r)}{1-r},\qquad h=(1-t)(1-r^2).
\]
For \(d\in\{0,\ldots,n-1\}\) congruent to \(j-i\pmod n\),
\[
\Sigma_{ij}=a\bigl(r^d+r^{n-d}+c\bigr).
\]
Let \(S\) be the cyclic shift on \(\mathbb R^n\), \(I\) the identity, and \(J\) the all-ones matrix. Except at \((n,q)=(3,3)\),
\[
\boxed{\displaystyle
Q=\frac1a\left[\frac{(1+r^2)I-r(S+S^{\mathsf T})}{h}
-\frac{c}{g(g+nc)}J\right].}
\]
Consequently, for all nonneighbor pairs the precision entry is identical and nonzero. For fixed \(q\ge3\), its magnitude as \(n\to\infty\) is
\[
\lvert Q_{ij}\rvert\sim
\frac{q^4}{(q-1)(q-2)}(q-1)^{-n},
\]
independent of the separation provided it is at least two along both arcs.

## Assumptions and scope
The probability space consists of all color maps \(\sigma:V(C_n)\to\{1,\ldots,q\}\) satisfying \(\sigma(i)\ne\sigma(i+1)\) at every cyclic edge, each map equally likely. Vertex indices are read modulo \(n\). No randomness of the underlying graph and no independence of vertex colors is assumed. The word *precision* refers only to the inverse of the finite covariance matrix; a zero precision entry would not by itself characterize nonlinear conditional independence for this non-Gaussian distribution.

## Proof
**1. Transfer-matrix covariance.** The proper-coloring transfer matrix is \(T=J_q-I_q\), acting on the \(q\) color labels. Its eigenvalues are \(b=q-1\) on constant vectors and \(-1\) on their orthogonal complement, so its cyclic partition function is
\[
Z=\operatorname{tr}(T^n)=b^n+b(-1)^n>0.
\]
Fixing the distinguished color at two vertices separated by \(d\in\{1,\ldots,n-1\}\) gives
\[
\mathbb E(X_iX_j)=\frac{(T^d)_{11}(T^{n-d})_{11}}{Z},\qquad
(T^k)_{11}=\frac{b^k+b(-1)^k}{q}.
\]
Color symmetry yields \(\mathbb E X_i=1/q\). Expansion of the last product and subtraction of \(1/q^2\) produce \(\Sigma_{ij}=a(r^d+r^{n-d}+c)\). The same formula at \(d=0\) equals \(b/q^2=\operatorname{Var}(X_i)\).

**2. Exact inverse.** Define \(G_{ij}=r^d+r^{n-d}\). An entrywise finite-geometric-series calculation, or direct multiplication of the cyclic second-difference operator, gives
\[
\bigl[(1+r^2)I-r(S+S^{\mathsf T})\bigr]G=hI,
\qquad G\mathbf1=g\mathbf1.
\]
As \(\lvert r\rvert<1\), the matrix in square brackets is positive definite: its Fourier eigenvalues are \(1+r^2-2r\cos(2\pi k/n)>0\). Hence \(G\) is positive definite, with \(G^{-1}=((1+r^2)I-r(S+S^{\mathsf T}))/h\). Since \(\Sigma=a(G+cJ)\), the rank-one inverse identity gives the displayed formula for \(Q\) if \(g+nc\ne0\).

**3. Singular boundary.** Writing \(b=q-1\),
\[
g+nc=\frac{b-1}{b+1}\left[1+\bigl(n(b+1)-1\bigr)(-1/b)^n\right].
\]
For even \(n\), this is strictly positive. For odd \(n\), it is nonnegative exactly when \(b^n\ge n(b+1)-1\). At \(n=3\) the difference is \((b-2)(b+1)^2\); its increment when \(n\) rises by one is \((b-1)b^n-(b+1)>0\) for \(b\ge2,n\ge3\). Thus the sole zero is \((n,b)=(3,2)\). The other Fourier eigenvalues are strictly positive, proving positive definiteness otherwise and rank exactly two at the exceptional triangle.

**4. Strict precision signs.** In the inverse formula, nonneighbor entries are exactly
\[
Q_{ij}=-\frac{c}{a g(g+nc)}.
\]
All other factors in the denominator are positive; \(c=(b-1)(-1)^n b^{-n}\), giving the required parity sign. For neighbors, the bracketed off-diagonal entry is \(-r/h-c/[g(g+nc)]\). When \(n\) is odd, \(c<0\), so this is positive. For even \(n\ge4\), set \(t=b^{-n}>0\) and note
\[
\frac{-r}{h}\,g=\frac{b}{(b+1)^2},\qquad
0<\frac{c}{g+nc}<\frac{c}{g}=\frac{(b+1)t}{1-t}
\le\frac{b+1}{b^4-1}<\frac{b}{(b+1)^2}.
\]
The last strict inequality follows by multiplying out and using \(b(b-1)\ge2\) and \(b^2+1\ge (b+1)^2/2\), with at least one strict inequality. Therefore every neighbor precision entry is strictly positive.

**5. Long-cycle coefficient.** For fixed \(b\ge2\), as \(n\to\infty\), \(a\to b/q^2\) and \(g\to(b-1)/(b+1)\), while \(nc\to0\). Substitution into the exact nonneighbor formula yields the stated coefficient \(q^4/[b(b-1)]\) and exponential decay.

## Verification
The standalone standard-library program `verify.py` enumerates proper colorings directly for \(3\le q\le5\) and \(3\le n\le7\), comparing all rational first and mixed moments to the transfer-matrix formulas. It then multiplies the proposed precision by the covariance matrix exactly and checks every predicted sign for \(3\le q\le7\) and \(3\le n\le12\), including the singular triangle. Running `python3 verify.py` produced `VERIFIED_EXACT_ASSERTIONS 6605`. This is a finite independent check; the proof above establishes the all-size statements.

## Relationship to prior work
Uniform proper colorings are the zero-temperature antiferromagnetic Potts model. Standard transfer matrices, cycle chromatic polynomials, Potts two-point functions, and spatial-mixing/influence methods are prior mathematics. The specific contribution asserted here is the **complete inverse covariance formula for one distinguished-color indicator family**, including the strict parity classification of all nonneighbor full-order linear partial correlations and the unique singularity. Standard two-point formulas supply the covariance but do not alone state or classify the signs of its inverse.

The related primary literature includes Turban's exact correlation calculations for a different one-dimensional Potts interaction, Chang–Shrock's cyclic-strip transfer matrices and chromatic partition functions, and Chen–Liu–Mani–Moitra's spectral-independence theory for uniformly random colorings. These establish relevant machinery or different correlation questions; they are not claimed to provide the present classification. Historical priority for an implicit equivalent inversion in older Potts or graphical-model literature remains uncertain.

## Limitations
These results concern one marked color, uniform proper colorings on a simple cycle, and full-order **linear** partial correlations. They do not imply statements about actual conditional independence, color-specific heterogeneous fugacities, general graphs, or finite-temperature interactions. The result does not claim a new transfer-matrix identity or an independent mathematical audit.

## References
1. Z. Chen, K. Liu, N. Mani, A. Moitra, *Strong spatial mixing for colorings on trees and its algorithmic applications*, arXiv:2304.01954, first posted 2023-04-04, https://arxiv.org/abs/2304.01954.
2. L. Turban, *One-dimensional q-state Potts model with multi-site interactions*, arXiv:1701.09058, first posted 2017-01-31, https://arxiv.org/abs/1701.09058.
3. S.-C. Chang, R. Shrock, *Transfer matrices for the zero-temperature Potts antiferromagnet on cyclic and Möbius lattice strips*, arXiv:cond-mat/0404373, first posted 2004-04-16, https://arxiv.org/abs/cond-mat/0404373.
