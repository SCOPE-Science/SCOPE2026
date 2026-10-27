# Complete-graph dichotomy for consistent-mass backward Euler positivity on equilateral metric networks

## Finding

For every finite connected simple graph \(G=(V,E)\) with \(|V|\ge2\), realize each edge as a segment of common physical length \(\ell>0\), equip the graph with Kirchhoff–Neumann heat diffusion of diffusivity one, discretize with continuous piecewise-linear finite elements retaining all vertices and the consistent mass, and advance by one backward Euler step of size \(t\ge0\). Its nodal update matrix \(P(t)\) has **entrywise nonnegative coefficients exactly** as follows:

\[
P(t)\ge0\quad\Longleftrightarrow\quad
\begin{cases}
 t\ge0,&G\text{ is complete},\\
 t=0\ \text{or}\ t\ge\ell^2/6,&G\text{ is not complete}.
\end{cases}
\]

For every connected noncomplete graph and every \(0<t<\ell^2/6\), an off-diagonal entry of \(P(t)\) is strictly negative. For every graph and \(t>\ell^2/6\), every matrix entry is strictly positive; the complete-graph case is strictly positive for all \(t>0\).

## Assumptions and scope

The graph is finite, connected, undirected, simple and has at least two vertices. Edges all have the same length \(\ell>0\). Diffusivity is one; no Dirichlet vertices or forcing are present. Every graph vertex is one retained nodal unknown, with continuous piecewise-linear interpolation on each edge. The mass is *consistent*, not diagonally lumped. Matrix inequalities compare all entries; they do not denote positive semidefiniteness. Time step \(t\) ranges over all nonnegative real numbers. The claim is for one completed backward Euler step. It therefore also guarantees nonnegativity at all iterated steps whenever that one-step map is nonnegative.

Write \(A\) for the graph adjacency matrix, \(D=\operatorname{diag}(d_v:v\in V)\) for its degree matrix, and \(I\) for identity. Connectedness and at least two vertices imply \(d_v>0\).

## Proof

**Exact assembly.** On a physical edge the consistent local mass and stiffness matrices are respectively \(\frac{\ell}{6}\begin{pmatrix}2&1\\1&2\end{pmatrix}\) and \(\frac1\ell\begin{pmatrix}1&-1\\-1&1\end{pmatrix}\). Summing over edges gives
\[
M=\frac{\ell}{6}(2D+A),\qquad K=\frac1\ell(D-A).
\]
The matrix \(M\) is symmetric positive definite and \(K\) is positive semidefinite. Thus \(S(t)=M+tK\) is symmetric positive definite for every \(t\ge0\), and \(P(t)=S(t)^{-1}M\) is well-defined. Since \(K\mathbf1=0\), every \(P(t)\) has row sums one. At \(t=0\), \(P(0)=I\).

**Sufficiency above the threshold.** Put \(h=t/\ell^2\). Then
\[
S(t)=\frac\ell6\left((2+6h)D+(1-6h)A\right).
\]
For \(h\ge1/6\), this is a symmetric positive definite matrix with nonpositive off-diagonal entries (a Stieltjes matrix). Consequently \(S(t)^{-1}\ge0\); since \(M\ge0\), the update \(P(t)\ge0\). At \(h=1/6\), direct substitution gives
\[
P(t)=\frac23I+\frac13D^{-1}A.
\]
For \(h>1/6\), \(S(t)\) is irreducible as a Stieltjes matrix because the graph is connected. The standard inverse-positivity lemma below gives \(S(t)^{-1}>0\). As every diagonal element of \(M\) is positive, \(P(t)>0\).

**Necessity for every noncomplete graph.** Suppose \(0<h<1/6\). Set \(b=1-6h>0\), so that the exact identity \(S(t)=bM+3\ell hD\) yields
\[
P(t)=\frac1b I-\frac{3\ell h}{b}S(t)^{-1}D.
\]
If \(P(t)\) were entrywise nonnegative, every off-diagonal entry of \(S(t)^{-1}\) would have to be nonpositive, because \(D\) has strictly positive diagonal. Thus \(H=S(t)^{-1}\) would itself be symmetric positive definite with nonpositive off-diagonal entries. It is irreducible: otherwise, simultaneously permuting rows and columns would make \(H\), and therefore its inverse \(S(t)\), block diagonal, contradicting the connected positive-edge pattern of \(S(t)\). By the strict inverse-positivity lemma, \(H^{-1}=S(t)\) would have *every* entry strictly positive. But a noncomplete graph has two nonadjacent vertices, and the formula for \(S(t)\) shows its corresponding off-diagonal entry is zero. Contradiction. Therefore at least one off-diagonal entry of \(P(t)\) is negative for every \(0<h<1/6\).

**Inverse-positivity lemma.** If a real symmetric positive definite matrix \(H\) has nonpositive off-diagonal entries and is irreducible, choose \(\alpha\) at least as large as its largest eigenvalue. The matrix \(B=\alpha I-H\) is entrywise nonnegative, symmetric and irreducible; its spectral radius is \(\alpha-\lambda_{\min}(H)<\alpha\). Hence
\[
H^{-1}=\frac1\alpha\sum_{k=0}^{\infty}(B/\alpha)^k>0
\]
entrywise: for any two indices, irreducibility supplies a nonzero nonnegative walk term in the series. This also proves all uses of the lemma above.

**The complete-graph exception.** For \(G=K_n\), the constant vector and its orthogonal complement diagonalize both \(M\) and \(K\). The update eigenvalue is one on constants and \(r(h)=(2n-3)/(2n-3+6nh)\) on their orthogonal complement. Thus
\[
P(t)=r(h)I+\frac{1-r(h)}n\mathbf1\mathbf1^{\mathsf T}.
\]
Since \(0<r(h)\le1\) for \(h\ge0\), this is entrywise nonnegative for all times and strictly positive for \(h>0\). The two cases exhaust all connected simple graphs with at least two vertices.

## Verification

Run `python verification/check.py` with Python 3, NumPy, SymPy and NetworkX installed. The checker assembles the dimensionless exact matrix formula and compares entrywise signs and row sums over every connected unlabeled graph in the NetworkX graph atlas with two through seven vertices, at steps on both sides of and exactly on the sharp boundary. For connected atlas graphs on two through five vertices, it independently recomputes those signs and conservation identities with rational SymPy arithmetic. It also checks the complete-graph spectral formula symbolically in orders two through five. Reproduced output: 995 connected graphs, 10,945 floating-point checks; 30 graphs and 330 exact rational checks; four symbolic complete-graph cases. These finite checks are supplementary: the proof covers all graph orders and all real step sizes.

## Relationship to prior work

Li and Huang, arXiv:1209.5657 (first public September 25, 2012), analyze discrete maximum-principle sufficient mesh/step conditions for spatial finite elements and temporal \(\theta\)-methods in anisotropic diffusion; they do not classify all connected metric-network graph topologies by necessity and sufficiency. Jin, Lazarov, Thomée, and Zhou, arXiv:1510.02825 (first public October 9, 2015), prove positivity-threshold sufficient bounds for standard Galerkin fully discrete methods, as well as small-step negativity under mesh assumptions. Their Stieltjes argument supplies the known sufficient side at this graph specialization but does not establish the missing-edge necessity for **every** intermediate positive step or the unconditional complete-graph exception. The structural ingredient used here is the standard inverse-positivity theorem for irreducible Stieltjes matrices; the finite-network dichotomy arises from combining it with the exact consistent-mass update identity. Existing periodic-chain, tree and bipartite special-family formulas are subsumed, not counted as additional findings.

## Limitations

This result assumes equilateral edges, unit diffusivity, all vertices retained and Kirchhoff–Neumann coupling. It is not asserted for unequal lengths, altered vertex coupling, Dirichlet elimination, mass lumping, higher-order spatial elements, or other time integrators. The graph-theoretic necessity is a completed-step statement; individual negative entries need not occur at any specified fixed pair of vertices. Literature search and inspection cannot exclude specialized work not indexed or accessible; independent audit has not been performed.

## References

1. X. Li and W. Huang, *Maximum principle for the finite element solution of time dependent anisotropic diffusion problems*, arXiv:1209.5657 (first submitted September 25, 2012), https://arxiv.org/abs/1209.5657.
2. B. Jin, R. Lazarov, V. Thomée and Z. Zhou, *On nonnegativity preservation in finite element methods for subdiffusion equations*, arXiv:1510.02825 (first submitted October 9, 2015), https://arxiv.org/abs/1510.02825.
3. V. Thomée and L. B. Wahlbin, *On the existence of maximum principles in parabolic finite element equations*, Mathematics of Computation 77 (2008), 11–19, DOI: 10.1090/S0025-5718-07-02021-2 (abstract accessed, full paper not inspected).
