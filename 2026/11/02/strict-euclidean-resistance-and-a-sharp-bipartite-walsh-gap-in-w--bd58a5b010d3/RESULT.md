# Strict Euclidean resistance and a sharp bipartite Walsh gap in weighted cubelike networks

## Finding

For every finite, connected, positively weighted Boolean Cayley network, effective resistance \(R\) itself is a strict Euclidean metric: all \(N=2^d\) vertex images form an affinely independent Euclidean simplex of minimal dimension \(N-1\). The nonzero eigenvalues of its centered squared-resistance Gram matrix satisfy the sharp bound
\[
b_\tau\ge\frac4{N\lambda_\tau^2}>0,
\qquad\lambda_\tau=2\sum_{s:\tau(s)=-1}c_s,
\]
with equality exactly in the uniquely determined bipartition Walsh mode when the network is bipartite. Its supremal negative-type exponent is strictly larger than \(2\).

## Assumptions and scope

Fix \(d\ge1\) and the additive Boolean group \(G=(\mathbb F_2)^d\), with \(N=2^d\) elements. Let \(S\subset G\setminus\{0\}\) be a nonempty generating set, with arbitrary **positive** real conductance \(c_s\) at every undirected edge \(\{x,x+s\}\) for each \(x\in G\) and \(s\in S\). The weighted Laplacian is \((Lf)(x)=\sum_{s\in S}c_s(f(x)-f(x+s))\); each undirected edge is counted once. Let \(L^+\) be its pseudoinverse and \(R(x,y)=(e_x-e_y)^\mathsf{T}L^+(e_x-e_y)\). This is electrical effective resistance, **not** shortest-path distance. Strict \(p\)-negative type means \(\sum_{x,y}\alpha_x\alpha_yR(x,y)^p<0\) for all nonzero real zero-sum \(\alpha\).

## Proof

**Electrical Fourier diagonalization.** The Boolean characters \(\chi:G\to\{\pm1\}\) diagonalize \(L\). For nonconstant \(\chi\), \(\lambda_\chi=\sum_sc_s(1-\chi(s))=2\sum_{s:\chi(s)=-1}c_s>0\), since \(S\) spans \(G\). Their orthogonality and the spectral pseudoinverse give
\[
R(x,y)=r(x-y),\quad r(z)=\frac2N\sum_{\chi\ne1}\frac{1-\chi(z)}{\lambda_\chi}.
\]
Set \(a_1=0\), \(a_\chi=\lambda_\chi^{-1}\) for \(\chi\ne1\), and \(A=\sum_\chi a_\chi\). With the unnormalized transform \(\widehat f(\tau)=\sum_{z\in G}f(z)\tau(z)\), one has \(\widehat r(1)=2A\) and \(\widehat r(\chi)=-2a_\chi\) for nontrivial \(\chi\). The Fourier product-convolution identity gives
\[
\widehat{r^2}(\tau)=\frac4N\left[\sum_\chi a_\chi a_{\chi\tau}-2Aa_\tau\right]
\qquad(\tau\ne1).
\]
The matrix \(D_2=(R(x,y)^2)_{x,y}\) is a convolution matrix, and \(H=I-N^{-1}J\) removes its constant mode. Thus the Gram eigenvalue for every nonconstant \(\tau\) is \(b_\tau=-\widehat{r^2}(\tau)/2\).

**The sharp sign inequality.** At every generator \(s\), Boolean signs imply \(1-\tau(s)\le(1-\chi(s))+(1-(\chi\tau)(s))\). Multiply by \(c_s\) and sum to obtain \(\lambda_\tau\le\lambda_\chi+\lambda_{\chi\tau}\). For \(\chi\notin\{1,\tau\}\) all three symbols are strictly positive, and division gives \(a_\chi a_{\chi\tau}\le a_\tau(a_\chi+a_{\chi\tau})\). Sum over \(\chi\notin\{1,\tau\}\), use \(a_1=0\), and simplify:
\[
\sum_\chi a_\chi a_{\chi\tau}\le2Aa_\tau-2a_\tau^2.
\]
Therefore \(\widehat{r^2}(\tau)\le-8a_\tau^2/N\) and
\[
b_\tau\ge\frac4{N\lambda_\tau^2}>0.
\]
This positivity on all nonconstant Walsh modes proves strict \(2\)-negative type. By the finite Euclidean-distance Gram criterion, \((G,R)\) embeds isometrically in dimension exactly \(\operatorname{rank}B=N-1\); it cannot embed in a lower-dimensional Euclidean space.

**Sharpness and bipartiteness.** If \(\tau(s)=-1\) for all \(s\in S\), then for each generator exactly one of \(\chi(s)\), \((\chi\tau)(s)\) equals \(-1\). Every generatorwise inequality above is equality, hence the Gram bound is equality. Conversely, if \(\tau(s)=1\) at some generator \(s\), choose a character \(\chi\) with \(\chi(s)=-1\). Then \(\chi\notin\{1,\tau\}\) and that generator gives a strict contribution to \(\lambda_\chi+\lambda_{\chi\tau}-\lambda_\tau\), so the Gram bound is strict. A character taking all generators to \(-1\) two-colors the Cayley network. Conversely, in a connected bipartite Cayley graph, path parity defines a character taking all generators to \(-1\); it is unique because \(S\) spans \(G\).

**Exponents above two.** For a fixed finite network, the restriction of \(-\frac12H(R(x,y)^2)H\) to the zero-sum space is positive definite. The entries of \(R(x,y)^p\) depend continuously on \(p>0\), hence some \(\epsilon>0\) retains strict \(p\)-negative type on \([2,2+\epsilon)\). Standard monotonicity of negative type for lower powers gives strict \(p\)-negative type for all \(0<p<2\). No exact supremal exponent is asserted.

The conclusion does not hold for all electrical graphs: the unit-edge three-leaf star has resistance distances \(1\) from center to leaf and \(2\) between leaves. Its zero-sum coefficient vector \((3,-1,-1,-1)\) has positive squared-resistance quadratic form \(6\), contradicting \(2\)-negative type.

## Verification

Run the bundled `verify_cubelike_resistance.py` using Python 3 with no third-party dependencies. It independently constructs physical weighted Laplacians, exactly inverts a grounded principal submatrix over rational arithmetic, checks all \(980\) ordered pair resistances in eight cases of sizes \(2,4,8,16\), and verifies the Walsh squared-resistance eigenvalues, strict Gram inequality, and precise bipartite equality criterion. The finite computations are corroboration only, not an exhaustive proof of every real conductance or dimension.

## Relationship to prior work

Jorgensen--Pearse (2009) construct a general Hilbert realization for **\(\sqrt R\)**. That does not imply the stronger assertion that \(R\) is Euclidean: the star example disproves it in general. Gao--Luo--Liu (2011) study resistance distances and Kirchhoff indices in Cayley graphs. Their resistance formulas overlap the spectral starting point; their **full text was not accessible**, so whether a statement equivalent to the new strict squared-resistance Gram inequality occurs there remains a serious stated priority risk. Liu and coauthors (2013) calculate hypercube Kirchhoff indices (aggregate resistance), not the complete powered-distance Gram matrix in the inspected full text. Robertson (2023) studies the Boolean cube with the **Hamming shortest-path metric**, not electrical resistance. No inspected accessible statement implies the all-weights, sharp-inequality and iff-equality claim by itself. Unindexed equivalent work remains possible.

## Limitations

Only finite connected, translation-invariant electrical networks on Boolean groups with strictly positive generator conductances are covered. No assertion concerns vertex-dependent conductances, non-Boolean groups, arbitrary electrical networks, or the exact sharp exponent beyond \(2\). The inaccessible 2011 Cayley resistance article leaves a residual publication-priority risk. Independent scientific auditing is not claimed.

## References

1. P. E. T. Jorgensen and E. P. J. Pearse, *A Hilbert Space Approach to Effective Resistance Metric* (public arXiv version 2009-06-14), https://arxiv.org/abs/0906.2535 ; full primary work inspected, including the square-root-resistance embedding.
2. X. Gao, Y. Luo and W. Liu, *Resistance distances and the Kirchhoff index in Cayley graphs*, Discrete Applied Mathematics 159 (2011), 2050–2057, https://doi.org/10.1016/j.dam.2011.06.027 ; bibliography and citing discussion inspected; full primary text unavailable.
3. *The Kirchhoff Index of Hypercubes and Related Complex Networks* (2013), https://doi.org/10.1155/2013/543189 ; full text and hypercube results inspected.
4. G. Robertson, *Negative type and bi-Lipschitz embeddings into Hilbert space* (2023), https://arxiv.org/abs/2309.16070 ; full primary paper and Hamming-cube example inspected.
