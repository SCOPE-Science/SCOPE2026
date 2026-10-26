# The five-vertex onset of a precision-sign reversal for isolation indicators

## Finding

For a finite connected simple graph \(H=(V,E)\) on at least three vertices, retain each edge independently with a common probability \(p\in(0,1)\). Let \(I_v\) indicate that vertex \(v\) is isolated in the retained subgraph, and let \(\Sigma(p)=\operatorname{Cov}((I_v)_{v\in V})\). Define the *linear partial correlation*, with all other indicators linearly adjusted for, by
\[
\rho_{uv\cdot V\setminus\{u,v\}}(p)=
-\frac{[\Sigma(p)^{-1}]_{uv}}{\sqrt{[\Sigma(p)^{-1}]_{uu}[\Sigma(p)^{-1}]_{vv}}}.
\]
The covariance matrix is positive definite. The following give a sharp qualitative classification.

1. If \(H\) is bipartite and connected, then for every distinct \(u,v\), the partial correlation is nonzero with sign \((-1)^{\operatorname{dist}_H(u,v)+1}\), independently of \(p\).
2. For every connected graph of order three or four, each pair's partial correlation has a fixed nonzero sign throughout \(0<p<1\), whether or not the graph is bipartite.
3. The lower bound of five vertices is sharp. Let \(H_r\) consist of adjacent hubs \(a,b\) and \(r\ge1\) other vertices, each joined to both hubs but with no edges among themselves. Set \(t=(1-p)^{-1}\) and \([m]_t=\sum_{j=0}^{m-1}t^j\). Then
\[
\rho_{ab\cdot V\setminus\{a,b\}}(p)
=\frac{t+1-r}{(t+1)[r+1]_t-r}.
\]
For every \(r\ge3\), this has exactly one zero and reverses from negative to positive as \(p\) increases through \(p_r=(r-2)/(r-1)\). For the five-vertex graph \(H_3\), the transition is exactly \(p_3=1/2\). Nonetheless the *marginal* covariance of the hubs is positive for every \(p\in(0,1)\).

The claim concerns population linear partial correlations of binary variables. A zero does **not** assert conditional independence of the two isolation events given the others.

## Assumptions and scope

The base graph is finite, undirected, connected, and simple; it has at least three vertices. Each existing edge is retained independently with the same parameter strictly between zero and one, while nonedges remain absent. An isolation indicator takes value one if no retained edge touches its vertex. Linear partial correlations use residuals from least-squares linear projection onto the remaining isolation indicators; no Gaussian law is assumed. The graph \(H_r\) has \(r+2\) vertices and \(2r+1\) edges.

## Proof

**Exact covariance and positivity.** Write \(q=1-p\), \(d_v=\deg_H(v)\), and \(a_v=q^{d_v}\). Independence of edge retentions gives \(\mathbb E I_v=a_v\). For distinct vertices \(u,v\), their incident edge sets are disjoint unless \(uv\in E\). If \(uv\in E\), exactly one absent edge is counted twice in \(a_u a_v\), and hence
\[
\Sigma_{uv}=a_u a_v\frac{p}{q}\mathbf1_{\{uv\in E\}},\qquad
\Sigma_{vv}=a_v(1-a_v).
\]
With \(t=1/q>1\), \(D=\operatorname{diag}(a_v)\), and the adjacency matrix \(A\), define
\[
B(t)=A+\operatorname{diag}([d_v]_t:v\in V),\qquad [d]_t=\sum_{j=0}^{d-1}t^j.
\]
Then exactly
\[
\Sigma(p)=\frac{p}{q}D B(t)D.
\]
The quadratic form \(x^\top B(t)x=\sum_{uv\in E}(x_u+x_v)^2+\sum_v([d_v]_t-d_v)x_v^2\) is strictly positive for nonzero \(x\). Indeed, a connected graph on at least three vertices has a vertex of degree at least two, whose last coefficient is strictly positive for \(t>1\); if the form vanished, that coordinate would vanish and the edge equations would propagate zero across the connected graph. Thus \(B\) and \(\Sigma\) are positive definite. Because the diagonal congruence is positive, the sign of the partial correlation is the opposite of the sign of \((B^{-1})_{uv}\).

**Bipartite rigidity.** Give each vertex its bipartition sign \(s_v\in\{-1,1\}\) and put \(S=\operatorname{diag}(s_v)\). The matrix \(T=S B S\) is positive definite, has nonpositive off-diagonal entries, and is irreducible. Choose \(c\) greater than every diagonal entry of \(T\). Then \(N=cI-T\) is an irreducible nonnegative matrix. Its Perron eigenvalue is \(c-\lambda_{\min}(T)<c\), whence
\[
T^{-1}=c^{-1}\sum_{k=0}^{\infty}(N/c)^k
\]
converges and has strictly positive entries. It follows that \(\operatorname{sgn}(B^{-1}_{uv})=s_us_v=(-1)^{\operatorname{dist}(u,v)}\), proving assertion 1.

**No smaller reversal.** There are exactly four connected labeled simple graphs on three vertices and 38 on four vertices. For each, form the integer-polynomial matrix \(B(1+z)\), \(z>0\). Its inverse numerator at \((u,v)\) is the cofactor \(C_{uv}(z)=(-1)^{u+v}\det B_{\widehat v,\widehat u}(1+z)\), and its denominator is positive. Exhaustive exact expansion for all 42 connected labeled graphs proves that every off-diagonal cofactor is a nonzero polynomial whose coefficients have a common weak sign. Therefore no cofactor vanishes or changes sign for \(z>0\). The complete symbolic expansions are reconstructed, rather than assumed, by the bundled standard-library checker `verify_isolation.py`; it checks all 12 pairs at order three and all 228 pairs at order four. This is an exhaustive *finite* proof because every labeled graph is visited. No assertion about larger order is inferred from the enumeration.

**The sharp family.** In \(H_r\), both hubs have degree \(r+1\); all other vertices have degree two. In the order hubs, then other vertices, the matrix \(B\) has upper-left block with diagonal \([r+1]_t\) and off-diagonal \(1\), hub-to-other block consisting of ones, and lower-right block \((1+t)I_r\). Eliminating that last block gives the positive-definite Schur complement
\[
\begin{pmatrix}
[r+1]_t-r/(t+1)&1-r/(t+1)\\
1-r/(t+1)&[r+1]_t-r/(t+1)
\end{pmatrix}.
\]
Because a pair's linear partial correlation is the off-diagonal residual covariance divided by the residual variance when the residual variances agree, the stated formula follows. Its denominator is positive by positive definiteness. Its numerator is \(t+1-r\): for \(r=1,2\) it is positive throughout \(t>1\); for \(r\ge3\) it has its unique zero at \(t=r-1\), equivalent to \(p=(r-2)/(r-1)\). At \(r=3\), this is \(p=1/2\), and the exact partial correlations are \(-27/491\), \(0\), and \(1/211\) at \(p=1/4,1/2,3/4\), respectively. Meanwhile, the marginal covariance is \(\operatorname{Cov}(I_a,I_b)=p q^{2r+1}>0\), as the hubs are adjacent.

## Verification

Run `python3 verify_isolation.py` in the extracted file directory. The checker requires only Python's standard library. It expands all 42 connected labeled graphs at orders three and four into exact cofactor polynomials in \(z=t-1\), tests their coefficient signs and nonvanishing, checks the Schur formula for ten family members and five rational parameters each, and independently enumerates all \(2^7=128\) edge configurations of the five-vertex witness at three rational parameters. The completed run passed 680 exact assertions. The infinite-family identity and bipartite theorem rest on the analytic arguments above; finite tests are not substitutes for them.

## Relationship to prior work

Multivariate Bernoulli distributions and the distinction between binary graphical dependence and Gaussian precision interpretations are discussed by Dai, Ding and Wahba [1]. Goldberg and Kirkland [2] study inverse-matrix and Schur-complement techniques for the (ordinary) signless Laplacian in a different eigenvector-sign problem. Penrose [3] studies isolated-vertex counts and Poisson approximation in random connection graphs, not the full-order partial-correlation signs of all vertex-isolation indicators on a fixed graph. The present covariance factorization produces a parameter-dependent *deformed* signless Laplacian and yields the exact first sign-change threshold and the full book-family law. These are not stated in the inspected cited results. General covariance, Schur-complement, and M-matrix methods are standard; historical priority for the particular percolation sign reversal remains open to independent assessment.

## Limitations

Uniform and independent edge retention is essential to the formulas; heterogeneous edge probabilities are not classified. Linear partial correlation is not nonlinear conditional covariance, conditional independence, or a Gaussian graphical model assertion. The minimality statement applies to connected graphs with nonsingular isolation covariance; one-edge components have identical isolation indicators and a singular covariance. The finite check covers orders three and four exhaustively but does not classify every five-vertex witness. No independent audit has been performed.

## References

[1] B. Dai, S. Ding and G. Wahba, *Multivariate Bernoulli distribution*, arXiv:1206.1874, first submitted 8 June 2012; Bernoulli 19 (2013), 1465–1483. https://arxiv.org/pdf/1206.1874

[2] F. Goldberg and S. Kirkland, *On the sign patterns of the smallest signless Laplacian eigenvector*, arXiv:1307.7749, first submitted 29 July 2013. https://arxiv.org/pdf/1307.7749

[3] M. D. Penrose, *Inhomogeneous random graphs, isolated vertices, and Poisson approximation*, arXiv:1507.07132, first submitted July 2015. https://arxiv.org/pdf/1507.07132
