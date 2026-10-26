# Two sharp extremizer phase curves for endpoint Hodge norms of bipartite prisms

## Finding
Let integers \(2\le p\le q\) be given, write \(N=p+q\), and form the unweighted Cartesian-product graph \(G=K_{p,q}\square K_2\). Let \(Q\) be the Euclidean-orthogonal projection of the real edge space onto the cut space and \(C=I-Q\) the complementary cycle projection. The edge space carries the unweighted \(\ell_1\) norm. Define
\[
A=1+\frac{2q(2p+q)}{(q+2)(N+2)},\qquad B=1+\frac{2p(p+2q)}{(p+2)(N+2)},
\]
\[
U=\frac{2q(3p+2q+1)}{(q+2)(N+2)},\qquad V=\frac{2p(2p+3q+1)}{(p+2)(N+2)}.
\]
For all \(2\le p\le q\), the exact endpoint cut-projection norm is
\[
\boxed{\|Q\|_{1\to1}=\|Q\|_{\infty\to\infty}=\max\{A,B\}.}
\]
The exact cycle-projection norm is
\[
\boxed{\|C\|_{1\to1}=\|C\|_{\infty\to\infty}=\begin{cases}73/30,&p=q=3,\\ \max\{U,V\},&\text{otherwise}.\end{cases}}
\]
In the exceptional case \(p=q=3\), a horizontal edge attains the cycle norm; its vertical-edge values are only \(12/5\). For \(p=q=2\), horizontal and vertical edge columns all tie (the cube case).

For \(p<q\), the cut-norm maximizing vertical edge class switches at \(pq=2(p+q)\), whereas the cycle-norm maximizing vertical class switches at the distinct curve \(pq=4(p+q)+2\). Below each curve the vertical edges in the part of size \(p\) maximize; above it the vertical edges in the part of size \(q\) maximize; equality gives a tie. More exactly,
\[
 B-A=\frac{2(q-p)(pq-2N)}{(p+2)(q+2)(N+2)},\qquad
 V-U=\frac{2(q-p)(pq-4N-2)}{(p+2)(q+2)(N+2)}.
\]
The two transitions therefore occur in genuinely different regions. For example, at \((p,q)=(3,7)\) the cut norm equals \(B=27/10\), attained on the larger-part vertical edges, while the cycle norm equals \(U=28/9\), attained on the smaller-part vertical edges. On the diagonal \(p=q=m\ge4\), the cut and cycle norms tend respectively to \(4\) and \(5\) as \(m\to\infty\).

## Assumptions and scope
All graphs are finite, connected, simple and unweighted. The two parts of \(K_{p,q}\) have \(p\) and \(q\) vertices, respectively. Horizontal edges lie within the two copies of \(K_{p,q}\); vertical edges join corresponding vertices across the copies. The orientation of edges is arbitrary. For the incidence matrix \(D\), the cut projection is \(Q=D^{\mathsf T}(DD^{\mathsf T})^+D\), and the cycle projection is \(C=I-Q\), with Moore--Penrose pseudoinverse denoted \((\cdot)^+\). This is an exact calculation for the **canonical orthogonal** projections, not a minimum over all linear projections. The \(\ell_1\) operator norm of a finite matrix is its largest absolute column sum. Since both projections are symmetric, their \(\ell_\infty\) operator norms agree with the \(\ell_1\) norms.

## Proof
**1. Spectral separation.** Let \(L\) be the vertex Laplacian of \(K_{p,q}\), let \(F=L^+\), and let \(T=(L+2I)^{-1}\). Write \(P_\pm=\frac12\begin{psmallmatrix}1&\pm1\\\pm1&1\end{psmallmatrix}\) on the two layers. The product Laplacian pseudoinverse is
\[
 \mathcal L^+=F\otimes P_+ +T\otimes P_- .
\]
The base Laplacian has eigenvalues \(0,q,p,N\), on the constant, part-\(p\) zero-sum, part-\(q\) zero-sum, and between-part contrast spaces. Consequently the entries of \(F\) and \(T\) follow by their four orthogonal spectral projectors. In particular \(T\) is entrywise nonnegative and every column has sum \(1/2\).

**2. Vertical-edge columns.** A unit source on the vertical edge at vertex \(a\) in the size-\(p\) part has opposite layer potentials \(\pm T\mathbf e_a\). Its vertical current absolute sum is \(2\sum_v T_{va}=1\). The base-edge gradients of \(T\mathbf e_a\) are \((N+1)/[(q+2)(N+2)]\) for the \(q\) edges incident to \(a\), and \(-1/[(q+2)(N+2)]\) for the \((p-1)q\) other base edges. Accounting for both layers yields total cut-column norm \(A\). Interchanging \(p,q\) yields \(B\). The corresponding effective resistances are
\[
 R_A=\frac{2p+3q+4}{(q+2)(N+2)},\qquad R_B=\frac{3p+2q+4}{(p+2)(N+2)}.
\]
For any edge \(e\), if its cut column has absolute sum \(S_e\) and diagonal \(R_e=Q_{ee}\), then the complementary column has absolute sum \(1+S_e-2R_e\), because \(0<R_e\le1\). This gives precisely \(U=1+A-2R_A\) and \(V=1+B-2R_B\).

**3. Horizontal-edge columns.** Fix a base edge \(a b\), with \(a\) in the size-\(p\) part, \(b\) in the size-\(q\) part, and source in one layer. On a base edge whose endpoints have indicators \(\alpha=\mathbf 1_{\{a\}}\) and \(\beta=\mathbf 1_{\{b\}}\), the two relevant gradients are
\[
 f_{\alpha\beta}=\frac{\alpha}{q}+\frac{\beta}{p}-\frac1{pq},\qquad
 t_{\alpha\beta}=\frac{\alpha}{q+2}+\frac{\beta}{p+2}-\frac{N+4}{(p+2)(q+2)(N+2)}.
\]
The sum of absolute horizontal currents over both layers equals \(\max\{|f_{\alpha\beta}|,|t_{\alpha\beta}|\}\) for each base edge. The four indicator types \((1,1),(1,0),(0,1),(0,0)\) have multiplicities \(1,q-1,p-1,(p-1)(q-1)\). The vertical currents have total absolute sum
\[
 \frac{2p+q}{(q+2)(N+2)}+\frac{p+2q}{(p+2)(N+2)}.
\]
For \(2\le p\le q\), the signs of both gradients coincide for each indicator type, and \(|t_{\alpha\beta}|\le |f_{\alpha\beta}|\) for all types except possibly \((1,0)\). Thus the horizontal cut-column norm is \(H=\max\{H_0,H_1\}\), where
\[
 H_0=3-\frac2p-\frac2q+\frac2{pq}
      +\frac{2p+q}{(q+2)(N+2)}+\frac{p+2q}{(p+2)(N+2)},
\]
\[
 H_1=H_0+(q-1)\left[\frac1{q+2}-\frac{N+4}{(p+2)(q+2)(N+2)}-\frac{p-1}{pq}\right].
\]
Its effective resistance is
\[
 R_H=\frac12\left[\frac{N-1}{pq}+\frac1{p+2}+\frac1{q+2}
   -\frac{N+4}{(p+2)(q+2)(N+2)}\right],
\]
so the horizontal cycle-column norm is \(1+H-2R_H\).

**4. Exhaustive comparison over all parameters.** Every edge lies in one of the three automorphism orbits just analyzed. The following exact rational inequalities therefore settle the global maximum. For \(p=2\) and \(p=3\), both \(A-H_0\) and \(A-H_1\) are nonnegative for all \(q\ge p\). For \(p\ge4\), both \(B-H_0\) and \(B-H_1\) are positive for all \(q\ge p\). For the cycle columns, \(U-(1+H_i-2R_H)\) is nonnegative for \(p=2,q\ge2\), for \(p=3,q\ge4\), and for \(p=4,q\ge4\), for either \(i\in\{0,1\}\). If \(5\le p\le8\) and \(pq\le4N+2\), these same inequalities hold for each of the finite parameter ranges \(5\le q\le22\) when \(p=5\), \(6\le q\le13\) when \(p=6\), \(7\le q\le10\) when \(p=7\), and \(q=8\) when \(p=8\). In the complementary ranges \(p=5,q\ge23\), \(p=6,q\ge14\), \(p=7,q\ge11\), \(p=8,q\ge9\), or \(p\ge9,q\ge p\), both \(V-(1+H_i-2R_H)\) are nonnegative. These are finite polynomial-sign certificates: after clearing positive denominators and replacing \(q\) by its stated lower bound plus a nonnegative variable (and for \(p\ge4\) or \(p\ge9\), replacing \((p,q)\) by \((4+u,4+u+v)\) or \((9+u,9+u+v)\)), every numerator has nonnegative coefficients and a positive-denominator polynomial. The 31 finite middle-regime parameter pairs are directly checked by exact rational substitution. The complete coefficient and substitution checks are reproduced in `verify_prism.py`.

The only excluded case \(p=q=3\) has horizontal cycle-column norm \(73/30\), exceeding both vertical values \(12/5\); at \(p=q=2\), all three cut and cycle orbit norms tie. Hence the stated max formulas hold. Finally, subtraction of the explicit vertical formulas yields the two displayed switching curves, including the equality cases.

## Verification
Run `python verify_prism.py` with Python 3 and SymPy. It verifies the displayed rational identities; confirms nonnegative-coefficient certificates for every infinite parameter regime; checks all 31 finite parameter pairs and their two relevant horizontal comparisons; and independently reconstructs the incidence-matrix Laplacian and all its edge columns for ten small graphs using exact rational inverses (362 edge columns). The checks use no floating-point tests. The infinite assertion is justified by the preceding spectral formulas and symbolic polynomial inequalities, not by small-graph enumeration.

## Relationship to prior work
The graph cut/cycle projection framework and its relevance to transportation-cost spaces are developed by Dilworth, Kutzarova and Ostrovskii (2023); their explicit calculations focus on tori and Hamming graphs, not this asymmetric two-layer bipartite family. Ostrovska and Ostrovskii (2021) develop the quotient representation of finite transportation-cost spaces by graph cycle spaces, without the present endpoint-norm phase classification. The cube \(K_{2,2}\square K_2\) is already a known graph and the \((2,2)\) values are not presented as a new isolated result. The contribution here is a complete two-parameter calculation with two distinct sharp orbit-selection boundaries and an exceptional balanced parameter. Standard spectral separation and effective resistance are tools, not newly asserted identities.

## Limitations
Only the canonical Euclidean-orthogonal projections are studied; no unrestricted minimal-projection constant is determined. No general assertion is made for weighted edges or for additional Cartesian factors. The bibliographic comparison is not exhaustive; an equivalent presentation in electrical-transfer-current literature may exist. No independent mathematical validation is claimed.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first public version 2023-05-21), https://arxiv.org/abs/2305.12582.
2. S. Ostrovska and M. I. Ostrovskii, *Isometric structure of transportation cost spaces on finite metric spaces*, arXiv:2112.02689 (first public version 2021-12-05), https://arxiv.org/abs/2112.02689.
