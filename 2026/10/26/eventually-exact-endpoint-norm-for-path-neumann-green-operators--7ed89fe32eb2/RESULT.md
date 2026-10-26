# Eventually exact endpoint norm for path Neumann Green operators

## Finding
For the unweighted path on \(n\ge2\) vertices, let \(L_n\) be its combinatorial Laplacian and \(G_n=L_n^\dagger\) the zero-mean inverse. The sharp \(\ell^1\)- and \(\ell^\infty\)-operator norms agree, and for all sufficiently large \(n\), the only maximizing rows are the two endpoint rows. In that eventual range put
\[
 m_n=\left\lfloor n\left(1-\sqrt{\tfrac13-\tfrac{1}{12n^2}}\right)-\tfrac12\right\rfloor.
\]
Then their common sharp norm is exactly
\[
 \|G_n\|_{1\to1}=\|G_n\|_{\infty\to\infty}
 =\frac{m_n+1}{3n}\left[m_n(m_n-3n+2)+2n^2-3n+1\right].
\]
For every \(n\ge2\), irrespective of the eventual-row theorem, the following explicit error bound holds:
\[
 \left|\|G_n\|_{\infty\to\infty}-\frac{2n^2}{9\sqrt3}\right|
 \le\frac78+\frac{1}{4\sqrt3}.
\]
For each fixed nonnegative integer \(k\), the difference between the endpoint row absolute sum and the row \(k\) absolute sum tends to \(k(k+1)/\sqrt3\). Thus the eventual endpoint maximizers are strict. The norm is attained in \(\ell^\infty\) by the signs of an endpoint kernel row, and in \(\ell^1\) by unit masses at endpoint columns.

## Assumptions and scope
Vertices are \(0,\ldots,n-1\); edges join successive vertices with unit conductance. The Laplacian has diagonal degree and off-diagonal minus adjacency. Its Moore–Penrose inverse acts on all inputs by subtracting the input mean, then returning the solution of zero vertex mean. Both operator norms are for the counting-measure spaces, not degree-normalized graph measures. The unspecified finite onset of strict endpoint optimality is not claimed to be effective.

## Proof
**Discrete Green kernel.** Put \(s_i=i^2+(1-n)i+n(n-1)/2\). Direct summation and endpoint/interior second differences give
\[
 (G_n)_{ij}=-\frac{|i-j|}{2}+\frac{s_i+s_j}{2n}-\frac{n^2-1}{6n}.
\]
Each row sums to zero, and \(L_nG_n=I-\mathbf1\mathbf1^\mathsf T/n\), uniquely identifying the Moore–Penrose inverse. Symmetry gives equality of the \(\ell^1\) and \(\ell^\infty\) norms. For any fixed row \(i\), its \(\ell^\infty\)-evaluation norm is exactly \(F_{n,i}=\sum_j |(G_n)_{ij}|\).

**Exact midpoint identity.** Define \(x_i=(i+1/2)/n\) and
\[
 K(x,y)=-\frac{|x-y|}{2}+\frac{x^2-x+y^2-y}{2}+\frac13.
\]
Substitution, not an asymptotic approximation, gives
\[
 (G_n)_{ij}/n=K(x_i,x_j)-1/(12n^2).
\]
For fixed \(x\), \(y\mapsto|K(x,y)|\) is one-Lipschitz, has second derivative of absolute magnitude one away from at most three exceptional points (at most two zeros and \(y=x\)), and has zero integral mean only *before* taking absolute values. A midpoint cell without an exceptional point contributes at most \(1/(24n^3)\) integration error. Each of at most three exceptional cells contributes at most \(1/(4n^2)\). Removing the \(1/(12n^2)\) kernel shift changes the normalized absolute row sum by at most \(1/(12n^2)\). Consequently, uniformly over all rows,
\[
 \left|F_{n,i}/n^2-J(x_i)\right|\le\frac{7}{8n^2},\qquad J(x)=\int_0^1|K(x,y)|\,dy.
\]

**Unique continuum endpoint maximizers.** Reflection gives \(J(1-x)=J(x)\). Set \(r=1-1/\sqrt3\). For \(0\le x\le r\) the positive kernel set is \([0,b(x)]\), with \(b(x)=1-\sqrt{1/3-x^2}\). Since \(\int K(x,y)\,dy=0\), differentiating the positive-part integral yields \(J'(x)=-2x\sqrt{1/3-x^2}<0\) for \(0<x\le r\). For \(r<x<1/2\), the positive set is \([a(x),b(x)]\), with \(a(x)=\sqrt{2x-x^2-2/3}\), and
\[
 J'(x)=2\left[(1-x)a(x)-x(1-b(x))\right]<0.
\]
The strict inequality follows by squaring the two nonnegative terms and using
\[
 x^2(1/3-x^2)-(1-x)^2(2x-x^2-2/3)
 =\frac23(1-2x)(3x^2-3x+1)>0.
\]
Thus \(J\) is strictly largest at \(0,1\). The endpoint kernel is \(K(0,y)=y^2/2-y+1/3\), which changes sign at \(r\), so
\[
 J(0)=2\int_0^r K(0,y)\,dy=\frac{2}{9\sqrt3}.
\]
For \(x\le r\), \(0\le J(0)-J(x)\le x^2/\sqrt3\). Comparing any discrete row with the first row now proves the displayed uniform absolute error bound.

**Eventual strict endpoint localization.** If \(i_n\) maximizes \(F_{n,i}\), the uniform midpoint estimate and first-row comparison imply \(J(0)-J(x_{i_n})=O(n^{-2})\). The strict continuum maximizers and the quadratic endpoint deficit \(J(0)-J(x)=x^2/\sqrt3+O(x^4)\) imply that the distance of \(i_n\) from the nearer endpoint is bounded independently of \(n\). Fix a nonnegative integer \(k\). The kernel identity yields, for every \(j\ge k\),
\[
 (G_n)_{kj}-(G_n)_{0j}=\frac{k(k+1)}{2n},
\]
whereas for \(j<k\) the difference is \(j-k+k(k+1)/(2n)\). The first \(k\) entries of row zero are eventually positive. The fraction of positive entries of row zero tends to \(r\), and its entries decrease through a unique zero with slope bounded away from zero. For fixed \(k\), the perturbation \(k(k+1)/(2n)\) changes the absolute-value linearization on at most a bounded number of near-zero entries, contributing \(o(1)\). Summing the signed differences therefore gives
\[
 F_{n,0}-F_{n,k}\longrightarrow k(k+1)(1-r)=\frac{k(k+1)}{\sqrt3}.
\]
By reflection and bounded localization, the only maximizing rows for all sufficiently large \(n\) are the two endpoints.

**Eventual finite formula and extremizers.** Row zero decreases strictly as a function of its column index, with
\[
 (G_n)_{0j}=\frac{3j^2-3(2n-1)j+2n^2-3n+1}{6n}.
\]
Its final nonnegative index is \(m_n\) as defined above, by the midpoint identity. Since the row sums to zero, \(F_{n,0}=2\sum_{j=0}^{m_n}(G_n)_{0j}\). Summing the quadratic polynomial gives the displayed floor-polynomial formula. Taking row signs supplies a sharp \(\ell^\infty\) input. A unit mass in an endpoint column supplies the equal sharp \(\ell^1\) norm.

## Verification
The companion `check_path_green.py` uses exact rational arithmetic to verify the finite Green kernel, Moore–Penrose identities, midpoint identity, endpoint sum formula and strict endpoint optimality for all integer \(2\le n\le80\). It also checks the uniform sharp-scale bound numerically in this finite range. These experiments are cross-checks, not proofs of the eventual statement or the infinite-parameter error bound.

## Relationship to prior work
Ellis, arXiv:math/0309080 (first public version 2003-09-04), provides discrete Green-function methodology for products of regular graphs and exact cycles/tori, rather than the sharp path inverse maximum norm. Franklin, arXiv:1201.6059 (2012-01-29), develops the one-dimensional Neumann Green-function normalization, not the sharp sequence of path inverse norms. Van Mieghem, Devriendt and Cetinay (2017) give a formula for the path graph Laplacian pseudoinverse and investigate diagonal entries and spreading; the present kernel itself is therefore not claimed as new. Their accessible abstract does not establish the sharp absolute-row norm, eventual endpoint localization, or uniform order-one error, but a decisive full-text comparison remains an access-related priority risk.

## Limitations
No explicit smallest endpoint-onset dimension is proved; endpoint optimality for every \(n\ge2\), though observed in exact finite tests, is not asserted. The value of the continuum constant is derived from a classical Neumann kernel, and any priority claim is limited to the joint sharp discrete norm, finite floor formula in the eventual regime, localization, and quantitative bound. General trees, weighted paths, degree-normalized Laplacians, and independent audit are outside scope.

## References
- R. B. Ellis, *Discrete Green's functions for products of regular graphs*, arXiv:math/0309080, first submitted 2003-09-04, https://arxiv.org/abs/math/0309080.
- J. Franklin, *Green's functions for Neumann boundary conditions*, arXiv:1201.6059, first submitted 2012-01-29, https://arxiv.org/abs/1201.6059.
- P. Van Mieghem, K. Devriendt and H. Cetinay, *Pseudoinverse of the Laplacian and best spreader node in a network*, Physical Review E 96 (2017), 032311, https://doi.org/10.1103/PhysRevE.96.032311.
