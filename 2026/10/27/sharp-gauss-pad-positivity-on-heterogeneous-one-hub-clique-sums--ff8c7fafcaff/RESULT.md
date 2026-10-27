# Sharp Gauss–Padé positivity on heterogeneous one-hub clique sums

## Finding

**Theorem.** Let \(t\ge 2\) and let \(s_1,\ldots,s_t\) be arbitrary positive integers. Form the finite, simple, unit-conductance graph
\[
G=K_1\vee\bigl(K_{s_1}\sqcup\cdots\sqcup K_{s_t}\bigr),
\qquad n=1+\sum_{i=1}^t s_i.
\]
Thus one hub is joined to every other vertex, and the non-hub vertices form disjoint cliques. Write \(L\) for the combinatorial Laplacian and, for \(h\ge0\), let
\[
T_G(h)=(12I-6hL+h^2L^2)(12I+6hL+h^2L^2)^{-1},
\]
the completed two-stage, order-four Gauss–Legendre diffusion step (diagonal \([2/2]\) Padé map). Put \(d(z)=z^2+6z+12\). For each integer \(k\ge2\) define
\[
\begin{aligned}
P_{n,k}(h)={}&(k+1)(kn+k-n^2+n+1)h^4\\
&+6(k+1)(k+2)h^3\\
&+12(2k+n^2+n+3)h^2\\
&+72(n+1)h+144.
\end{aligned}
\]
Whenever \(k=s_i\ge2\), the polynomial \(P_{n,k}\) has **exactly one positive real zero** \(H_{n,k}\). Set
\[
H_G=\begin{cases}
+\infty,&s_1=\cdots=s_t=1,\\
\min_{\{i:s_i\ge2\}}H_{n,s_i},&\text{otherwise}.
\end{cases}
\]
Then, for every real \(h\ge0\),
\[
\boxed{\quad T_G(h)\text{ is entrywise nonnegative}\quad\Longleftrightarrow\quad 0\le h\le H_G.\quad}
\]
All hub-to-leaf entries, all entries connecting different petals, and all diagonal entries are strictly positive for \(h>0\). Only transitions between distinct vertices of the *same* petal can become negative. A petal attaining the minimum defining \(H_G\) has strictly negative within-petal transitions for **every** \(h>H_G\); positivity cannot return. Consequently, among these one-hub clique sums, **exactly the stars** (every petal of size one) preserve positivity for every timestep. Nevertheless \(\|T_G(h)\|_{2\to2}=1\) for all \(h\ge0\), including those beyond a finite positivity horizon.

## Assumptions and scope

Graphs are undirected, connected, finite, simple and unweighted. The Laplacian is \(L=D-A\), not the normalized Laplacian; time is dimensionless for unit edge rates. The assertion concerns **the completed Runge–Kutta end-step**, not nonnegativity of intermediate stages. Every \(t\ge2\) and every vector of positive integer petal sizes is included, without a balance assumption. Spectral nonexpansiveness is in the Euclidean operator norm.

## Proof

**1. Eigenspaces.** Write \(m=n-1\). Label the hub by \(o\). The orthogonal eigenspaces of \(L\) are: the constants (eigenvalue \(0\)); the line spanned by \((-m,1,\ldots,1)\) (eigenvalue \(n\)); the \(t-1\)-dimensional space of vectors zero at the hub and constant on each petal whose total leaf sum is zero (eigenvalue \(1\)); and, for each petal of size \(s_i\), the subspace supported there with coordinate sum zero (eigenvalue \(s_i+1\)). This follows directly by applying \(L\) to each indicated vector. Their dimensions add to \(n\), so no eigenspaces are missing.

Let the projectors onto these spaces be \(E_0,E_n,E_1,E_{s_i+1}^{(i)}\). For two distinct leaves \(u,v\) in different petals,
\[
(E_0)_{uv}=\frac1n,\quad(E_n)_{uv}=\frac1{n(n-1)},\quad(E_1)_{uv}=-\frac1{n-1},
\]
and the other projectors vanish in this position. For distinct leaves in the same petal of size \(k\), these three entries remain the same except \((E_1)_{uv}=1/k-1/(n-1)\), while \((E_{k+1}^{(i)})_{uv}=-1/k\). For a hub–leaf pair the only nonzero projector entries are \((E_0)_{ou}=1/n\) and \((E_n)_{ou}=-1/n\).

**2. Scalar stability.** For a nonnegative Laplacian eigenvalue \(\lambda\), the rational map has scalar value
\[
r(h\lambda)=\frac{(h\lambda)^2-6h\lambda+12}{(h\lambda)^2+6h\lambda+12}.
\]
Its numerator is \((h\lambda-3)^2+3>0\), its denominator is positive, and \(0<r(z)\le1\) for \(z\ge0\). Thus \(T_G(h)\) is positive definite for every finite \(h\ge0\); all diagonal entries are strictly positive. Since \(r(0)=1\), the zero Laplacian eigenvalue gives the spectral operator norm exactly one and every row sum exactly one.

**3. All off-diagonal entry classes.** The spectral projectors yield three formulas, valid for \(h>0\). For hub–leaf pairs,
\[
T_G(h)_{ou}=\frac{1-r(nh)}n=\frac{12h}{d(nh)}>0.
\]
For leaves in different petals,
\[
\begin{aligned}
T_G(h)_{uv}&=\frac{n-1+r(nh)-n r(h)}{n(n-1)}\\
&=\frac{12h^2((n+1)h+6)}{d(h)d(nh)}>0.
\end{aligned}
\]
For two distinct leaves in one petal of size \(k\ge2\), the same formula gains \((r(h)-r((k+1)h))/k\). Reduction to a common denominator gives **exactly**
\[
\boxed{\quad T_G(h)_{uv}=\frac{12hP_{n,k}(h)}{d(h)d(nh)d((k+1)h)}.\quad}
\]
The denominators are strictly positive. The three identities can also be checked by symbolic rational arithmetic in the accompanying verifier.

**4. One sharp zero per nontrivial petal.** A petal size \(k\ge2\) is accompanied by at least one other petal, so \(n\ge k+2\). Write \(j=n-k-2\ge0\). Then
\[
kn+k-n^2+n+1=-\bigl(1+j(k+3)+j^2\bigr)<0.
\]
Therefore the leading coefficient of \(P_{n,k}\) is strictly negative, and its other four coefficients are strictly positive. In descending degree order there is precisely one sign change. By Descartes' rule of signs it has at most one positive root, counted with multiplicity; \(P_{n,k}(0)=144>0\) and \(P_{n,k}(h)\to-\infty\) as \(h\to+\infty\), so a positive root exists. It is the unique positive root, the polynomial is positive strictly before it and negative strictly after it. Taking the minimum over present nontrivial petals proves the theorem, including the nonreentrance assertion. If no petal is nontrivial, the first two positive off-diagonal formulas and positive definiteness establish unconditional positivity.

**5. Sharp structural illustrations.** The star \(K_{1,3}\) is unconditionally positivity-preserving. Adding one edge between its leaves yields the four-vertex paw graph with petal sizes \((2,1)\). Its positivity threshold is the unique positive zero of
\[
h^4-24h^3-108h^2-120h-48=0,
\]
namely \(28.0107851613\ldots\); an added edge therefore destroys unconditional positivity, despite unconditional spectral stability. The heterogeneous size vector \((4,5,6)\), with \(n=16\), has three distinct root enclosures:
\[
\begin{array}{lll}
2.261<H_{16,4}<2.262, &2.221<H_{16,5}<2.222,&2.230<H_{16,6}<2.231.
\end{array}
\]
Thus the *intermediate-size* petal, not necessarily the smallest or largest, determines the first negative transition. The displayed enclosures follow by exact rational substitution in the quartics and their proved unique-root property.

## Verification

Run \(\texttt{python verify.py}\) with the dependency in \(\texttt{requirements.txt}\). The verifier uses independent combinatorial construction of graph Laplacians and exact matrix rational arithmetic; it checks three symbolic projector-to-entry identities and the symbolic leading-sign reduction. For 23 graph specifications and six rational timesteps each, it compares 2,322 distinct off-diagonal entries of the full matrix rational function to the derived orbit formulas; it also checks symmetry, row sums and positive diagonals, and tests the paw transition and exact isolated intervals for three petal thresholds. These computations are checks on the formulas, **not** a substitute for the all-parameter proof in the preceding section.

## Relationship to prior work

Gottlieb, Shu and Tadmor [1] formulate the role of strong-stability preservation in high-order time stepping and limitations of method-wide monotonicity. Zappavigna, Colaneri, Kirkland and Shorten [2] study diagonal Padé approximants for positive linear systems; their second-order diagonal Padé theorem provides a sufficient step condition for Hurwitz Metzler matrices, not the exact graph-specific endpoint positivity threshold for a conservative Laplacian. Blanes, Iserles and Macnamara [3] examine positivity-preserving integrators for graph-Laplacian-structured ODEs and identify positivity under Padé approximation as a challenge. Spectral research on windmill graphs, e.g. [4], concerns eigenvalues and graph energy rather than numerical-step entry signs. The formulas here make a stronger, sharp, all-size statement for this particular graph family. Earlier results for classical **explicit** RK4 on one-hub clique sums or for Gauss–Legendre on complete multipartite graphs do not imply the present implicit-method behavior on nonstar clique sums. This is a literature assessment, not a proof of uniqueness among all publications.

## Limitations

The classification does not apply without further work to weighted petals, overlapping hub sets, arbitrary block graphs, or arbitrary Laplacian generators. Positivity of the completed step does not certify positivity at intermediate Gauss stages. The exact zero is defined algebraically, not asserted to have a simpler radical formula for every parameter choice. The survey cannot exclude unpublished or incompletely indexed exact-equivalent results. This document reports an analytical proof with supporting computational checks, not independent certification.

## References

[1] S. Gottlieb, C.-W. Shu and E. Tadmor, *Strong Stability-Preserving High-Order Time Discretization Methods*, SIAM Review 43 (2001), 89–112; first electronically public 2001-02-02. DOI: 10.1137/S003614450036757X; lawful full text: https://www.math.umd.edu/~tadmor/pub/linear-stability/Gottlieb-Shu-Tadmor.SIREV-01.pdf

[2] A. Zappavigna, P. Colaneri, S. Kirkland and R. N. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS (2010), repository full text: https://mural.maynoothuniversity.ie/id/eprint/2195/1/SK-pade_MTNS10_long.pdf

[3] S. Blanes, A. Iserles and S. Macnamara, *Positivity-preserving methods for ordinary differential equations*, ESAIM: M2AN 56 (2022), 1843–1870. DOI: 10.1051/m2an/2022042; author full text: https://personales.upv.es/serblaza/2022_M2AN.pdf

[4] W. Li, Y. Zhang and Y. Wang, *On the characteristic polynomials of Dutch windmill graphs and their applications*, AIMS Mathematics 11 (2026), 16697–16711, DOI: 10.3934/math.2026685 (abstract and bibliography compared; exact full content not fully accessible in the consulted HTML rendering).
