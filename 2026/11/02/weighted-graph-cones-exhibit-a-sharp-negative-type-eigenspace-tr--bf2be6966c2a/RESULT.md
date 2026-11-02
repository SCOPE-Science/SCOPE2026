# Weighted graph cones exhibit a sharp negative-type eigenspace transition

## Finding

Let \(G\) be any finite simple \(k\)-regular graph on \(N\ge4\) vertices with \(1\le k\le N-2\). Write \(-s\) for the smallest eigenvalue of its real adjacency matrix \(A\), assume \(s\ge2\), and let \(m\) be the multiplicity of \(-s\). For every \(h\in[1/2,1]\), form the **weighted graph cone** \(X_{G,h}\) by adjoining an apex \(o\), assigning length \(h\) to each apex edge and length \(1\) to every base edge, and taking the shortest-path metric. Hence distinct base vertices have distance \(1\) when adjacent in \(G\) and \(2h\) otherwise, while every apex--base distance is \(h\).

Let \(p_0(h)>1\) be the unique positive solution of
\[
 k+(N-1-k)(2h)^p=2Nh^p.
\]
For \(h>1/2\), define
\[
 p_1(h)=\frac{\log(s/(s-1))}{\log(2h)},
\]
with \(p_1(1/2)=+\infty\). Then the **exact supremal negative-type exponent** is
\[
 \boxed{\wp(X_{G,h})=\min\{p_0(h),p_1(h)\}.}
\]
There is exactly one transition weight \(h_*\in(1/2,1)\). Writing
\[
 p_*=\log_2\frac{2Ns}{s(N-1)-k},\qquad
 h_*=\frac12\left(\frac{s}{s-1}\right)^{1/p_*},
\]
we have \(p_0(h)<p_1(h)\) when \(h<h_*\), equality \(p_0(h_*)=p_1(h_*)=p_*\), and \(p_1(h)<p_0(h)\) when \(h>h_*\). Both branches are continuous, with \(p_0\) strictly increasing and \(p_1\) strictly decreasing.

At each \(0<p<\wp(X_{G,h})\) the snowflake \((X_{G,h},d^{p/2})\) embeds isometrically in real Hilbert space with **minimum affine dimension \(N\)**. At the endpoint \(p=\wp(X_{G,h})\), the minimum dimension is exactly
\[
 \boxed{\begin{cases}
 N-1,&h<h_*,\\
 N-m-1,&h=h_*,\\
 N-m,&h>h_*.
 \end{cases}}
\]
For \(p>\wp(X_{G,h})\), no such isometric embedding exists.

**Concrete infinite family.** For the \(q\)-ary Hamming graph \(G=H(d,q)\), with integers \(d,q\ge2\), put \(N=q^d\). Here \(k=d(q-1)\), \(s=d\), \(m=(q-1)^d\), so the formulas above yield the entire weighted-cone phase diagram with
\[
 p_*=\log_2\frac{2q^d}{q^d-q},\qquad
 h_*=\frac12\left(\frac d{d-1}\right)^{1/p_*}.
\]
At fixed \(d\), as \(q\to\infty\), the crossover exponent tends to \(1\) and \(h_*\to d/[2(d-1)]\). The minimum affine embedding dimension on the adjacency-controlled side drops by \((q-1)^d\) relative to subcritical powers.

## Assumptions and scope

All metrics, exponents, operators and Hilbert targets are real. The graph need not be connected, bipartite, distance-regular or vertex-transitive; only finite simplicity, regularity, noncompleteness, positive degree and \(s\ge2\) are used. The apex edge length is exactly \(h\in[1/2,1]\). At \(h=1/2\), adjacent and nonadjacent base pairs both have distance \(1\). For \(h>1/2\), the weighted shortest-path formula follows since any base nonedge has a path of length \(2h\) via the apex, any other path uses at least two base edges or apex edges, and \(1\le2h\le2\). The metric has \(N+1\) points. Negative type means that for all real coefficients \((c_x)_{x\in X}\) with \(\sum_xc_x=0\),
\[
\sum_{x,y\in X}c_xc_y d(x,y)^p\le0.
\]
The critical exponent is the supremum of \(p\ge0\) satisfying this inequality. The minimum affine embedding dimension refers to the affine span of images in an arbitrary real Hilbert space.

## Proof

**Step 1: a complete decomposition.** Put \(c=(2h)^p\), \(b=h^p\), and let \(J\) denote the all-ones \(N\)-by-\(N\) matrix. The powered-distance matrix restricted to base vertices is
\[
 B=c(J-I)+(1-c)A.
\]
Because \(G\) is \(k\)-regular, its constant row sum is
\[
 S=k+(N-1-k)c.
\]
Every zero-sum coefficient vector on the \(N+1\) points has a **unique** representation \((t\mathbf1+x,-Nt)\), with \(x\perp\mathbf1\). Its powered-distance quadratic form is therefore exactly
\[
 \begin{aligned}
 Q_p(t\mathbf1+x,-Nt)
 &=x^TBx+Nt^2(S-2Nb),\\
 &=\sum_{\theta\in\mathrm{spec}(A|_{\mathbf1^\perp})}
 \bigl((1-c)\theta-c\bigr)\|x_\theta\|^2
 +Nt^2\bigl[k+(N-1-k)c-2Nb\bigr].
 \end{aligned}
\]
All terms are mutually orthogonal with respect to this decomposition. No higher graph distances or other adjacency eigenvalues enter.

**Step 2: the only two obstructions.** Since \(c\ge1\), the largest eigenvalue of \(B\) on \(\mathbf1^\perp\) is attained on the least adjacency eigenspace, \(\theta=-s\), and equals
\[
 \lambda_{\min\text{-mode}}(p,h)=(s-1)(2h)^p-s.
\]
For \(c>1\), this is the unique maximizing adjacency eigenvalue; at \(c=1\), all base eigenvalues equal \(-1\) and are strictly negative. Consequently the restriction of \(Q_p\) to \(\mathbf1^\perp\) is nonpositive exactly when \((2h)^p\le s/(s-1)\). The remaining one-dimensional condition is
\[
 F(p,h):=k+(N-1-k)(2h)^p-2Nh^p\le0.
\]
For every \(h\in[1/2,1]\), \(F(0,h)=-N-1<0\), \(F(1,h)=k-2h(k+1)<0\), and \(F(p,h)\to+\infty\) as \(p\to\infty\). Moreover, \(p\mapsto F(p,h)\) is strictly increasing: \(2h\ge1\), \(h\le1\), and \(N-1-k>0\); at least one of the two variable terms increases strictly. Thus a unique \(p_0(h)>1\) exists. When \(h>1/2\), the least-mode inequality holds precisely for \(p\le p_1(h)\); at \(h=1/2\) it holds for all \(p\). This proves the stated supremum and its strict/non-strict boundary.

**Step 3: uniqueness and value of the transition.** At \(p=p_0(h)\), the identity \(F(p,h)=0\) implies that the coefficient of \(h^p\) in the equivalent form
\[
 F(p,h)=k+h^p\bigl[(N-1-k)2^p-2N\bigr]
\]
 is negative. Hence increasing \(h\) makes \(F(p_0(h),h)\) strictly smaller, and \(p_0(h)\) is strictly increasing in \(h\). In contrast, \(p_1(h)\) strictly decreases from \(+\infty\) to \(\log_2(s/(s-1))\le1\). Since \(p_0(h)>1\), the two branches cross exactly once inside \((1/2,1)\). At their intersection, \((2h_*)^{p_*}=s/(s-1)\), while
\[
 h_*^{p_*}=\frac{s(N-1)-k}{2N(s-1)}.
\]
Dividing the first identity by the second gives \(2^{p_*}=2Ns/[s(N-1)-k]\), and then the displayed formula for \(h_*\). This also proves \(p_*>1\).

**Step 4: sharp affine dimensions.** Schoenberg's finite-distance criterion identifies isometric Hilbert realizability of \(d^{p/2}\) with nonpositivity of \(Q_p\) on zero-sum coefficients; its minimum affine embedding dimension is the rank of the corresponding centered Gram matrix, equivalently \(N\) minus the nullity of \(Q_p\) on that \(N\)-dimensional zero-sum space. Below the endpoint all \(N\) modes are strictly negative. At \(h<h_*\) only the constant-population mode \((\mathbf1,-N)\) vanishes. At \(h>h_*\), precisely the least adjacency eigenspace of dimension \(m\) vanishes. At the crossover, both mutually independent nullspaces vanish, giving nullity \(m+1\). These are the claimed minimum dimensions. A positive mode above the endpoint rules out an isometric embedding.

**Step 5: Hamming family.** The adjacency matrix of \(H(d,q)\) is the sum of \(d\) commuting copies of \(J_q-I_q\). Tensor-product eigenvectors give eigenvalues \(d(q-1)-qj\) with multiplicities \(\binom dj(q-1)^j\), \(0\le j\le d\). The least is \(-d\), with multiplicity \((q-1)^d\). Substitution into the general theorem gives the stated corollary. Since \(q^{1-d}\to0\) at fixed \(d\ge2\), the limits of \(p_*\) and \(h_*\) follow directly.

## Verification

The companion script `check.py` independently constructs adjacency matrices for \(H(2,2)\), \(H(3,2)\), \(H(4,2)\), \(H(2,3)\), \(H(3,3)\), \(H(2,4)\), \(C_4\), \(C_6\), the Petersen graph, and the four-regular circulants with steps one and two on 7, 10 and 11 vertices. At each of five hub weights per graph (including \(1/2\), \(h_*\), and \(1\)) it builds the *full* powered-distance matrix and numerically diagonalizes its restriction to the zero-sum coefficient space. It checks the predicted number of zero modes at the critical exponent, strict negativity below, positivity above, and the two equal root formulas at the transition. Where the least adjacency eigenvalue is integral, it also reconstructs the crossover powered-distance matrix over the rationals and computes its rank *exactly*. The script prints the heading `CHECK_OK` after all cases pass. These finite computations test the decomposition and endpoint nullities; the proof above, not the computation, establishes the theorem for all graphs and parameters.

## Relationship to prior work

Schoenberg's negative-type/Hilbert-embedding criterion is classical. Sánchez's 2011 paper provides general determinant criteria for supremal negative type and an explicit complete-bipartite case. Deza and Laurent's 1992 survey (Theorem 4.6) records the earlier **unweighted** criterion for negative type of cones over regular diameter-two graphs at exponent one, in terms of the least adjacency eigenvalue; that boundary is not claimed as new. Robertson's 2023 paper develops negative-type/embedding theory and analyzes standard (untruncated, un-coned) Hamming cubes. Doust and Weston's 2024 work treats subsets of weighted Hamming cubes. Cardoso, Díaz and Rojo (2018) derive distance spectra for graph joins, not the present continuous apex-weight, variable-power phase diagram. The contribution here is the simultaneous exact parameter classification \((h,p)\) for every regular base graph with \(s\ge2\), the closed transition weight, the independent versus coincident endpoint obstructions, and the exact dimensional losses. A literature search cannot establish historical priority definitively.

## Limitations

The result applies only to graph bases satisfying the stated regularity and spectral hypotheses and to the given metric weighting. It does not handle irregular graphs, smallest adjacency eigenvalues above \(-2\), unequal apex weights, or apex lengths outside \([1/2,1]\). Full historical priority is not independently certified; earlier work on hypermetric two-distance spaces and graph joins remains a source of possible unrecognized equivalent formulations. No independent audit has been performed. Finite numerical reconstructions are neither an exhaustive search nor substitutes for the all-parameter proof.

## References

1. G. Robertson, *Negative type and bi-lipschitz embeddings into Hilbert space*, arXiv:2309.16070, first public 2023-09-27, https://arxiv.org/abs/2309.16070.
2. I. Doust and A. Weston, *Beyond trees: the metric geometry of subsets of weighted Hamming cubes*, arXiv:2404.06684, first public 2024-04-10, https://arxiv.org/abs/2404.06684.
3. S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451, 2011, https://arxiv.org/abs/1108.0451.
4. M. Deza and M. Laurent, *Applications of Cut Polyhedra*, September 1992, Theorem 4.6, https://micheldeza.altervista.org/papers/apl-cut-poly/applications-of-cut-polyhedra.pdf.
5. D. M. Cardoso, R. C. Díaz and O. Rojo, *Distance matrices on the H-join of graphs: A general result and applications*, Linear Algebra Appl. **559** (2018), 34–53, https://doi.org/10.1016/j.laa.2018.08.024.
