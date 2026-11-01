# Gaussian positivity on the generalized Petersen graphs \(GP(n,2)\): exactly four surviving orders

## Finding

For each integer \(n\ge5\), let \(G_n=GP(n,2)\) have vertices \(u_i,v_i\), \(i\in\mathbb Z/n\mathbb Z\), and undirected unit edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+2}\). Write \(d_n\) for shortest-path distance. The translation action of the cyclic group \(\mathbb Z/n\mathbb Z\) preserves both vertex layers; the two-layer matrix-valued function \(e^{-t d_n}\) is consequently a natural positive-definiteness problem in finite-group harmonic analysis.

**Theorem.** For every integer \(n\ge5\), the following are equivalent:

1. \(\big(e^{-t d_n(x,y)}\big)_{x,y\in G_n}\) is positive semidefinite for every \(t>0\).
2. \(d_n\) is conditionally negative semidefinite, meaning that \(\sum_{x,y}c_xc_yd_n(x,y)\le0\) for every real vector \(c\) with \(\sum_x c_x=0\).
3. \(n\in\{5,6,9,10\}\).

In these four cases the kernel is **strictly** positive definite for every \(t>0\). The least Euclidean dimensions of a realization \(d_n(x,y)=\|\Phi(x)-\Phi(y)\|^2\) are, respectively, \(5,7,9,10\) for \(n=5,6,9,10\). For every other integer \(n\ge5\), the exponential-distance kernel is not positive semidefinite for all sufficiently small positive \(t\).

This is a classification at the fixed exponent \(1\); it does **not** evaluate supremal fractional negative-type exponents for the excluded graphs.

## Assumptions and scope

The graphs are finite, simple, and undirected, and all edges have unit length. The conclusion concerns the complete \(2n\)-vertex metric, not an induced-graph metric. Coefficients in negative-type inequalities are real; the equivalent kernel statement allows arbitrary complex test vectors. Indices are interpreted modulo \(n\). The restriction \(n\ge5\) ensures that \(GP(n,2)\) is the standard cubic generalized Petersen graph with two distinct inner neighbors at each vertex.

For a distance matrix \(D\) on vertices \(x_0,x_1,\ldots,x_{2n-1}\), define the integer anchored matrix \(B\), indexed by \(1\le i,j<2n\), by
\[
B_{ij}=d(x_0,x_i)+d(x_0,x_j)-d(x_i,x_j).
\]
For \(c_0=-\sum_{i\ge1}c_i\), the exact identity \(c^{\mathsf T}Dc=-\sum_{i,j\ge1}c_iB_{ij}c_j\) proves that conditional negative semidefiniteness of \(D\) is equivalent to ordinary positive semidefiniteness of \(B\). The minimal squared-Euclidean embedding dimension equals \(\operatorname{rank}(B)\): its Gram matrix is \(B/2\).

## Proof

**1. Exact distance formula on the cyclic two-layer cover.** Consider the infinite graph with outer vertices \(u_i\), inner vertices \(v_i\), for \(i\in\mathbb Z\), and the same three kinds of edges. For an integer displacement \(s\), put \(h(s)=\lceil |s|/2\rceil\). Its shortest-path distances, by endpoint-layer types, are
\[
 f_{uu}(s)=\min\{|s|,2+h(s)\},\qquad
 f_{uv}(s)=1+h(s),\qquad
 f_{vv}(s)=\begin{cases}|s|/2,&s\text{ even},\\2+h(s),&s\text{ odd}.\end{cases}
\]
To prove the formulas, note that outer steps change the index by \(\pm1\), inner steps by \(\pm2\), and a spoke preserves it. In any path, the index increments commute, so grouping all inner steps and all outer steps cannot increase length and needs at most two spokes when both endpoint layers agree and at most one when they differ. The minimum number of steps needed to realize a displacement with inner and outer moves is \(h(s)\): use inner steps for the even part and at most one outer step for odd parity. An entirely inner path between inner endpoints exists exactly for even displacement, yielding the stated alternative. An entirely outer path costs \(|s|\). This proves the infinite-cover formulas.

Every finite path lifts to the infinite graph, and any infinite path between a fixed lift of its start and an appropriate lift of its finish projects to a finite path. Thus the **exact finite-graph formula** is
\[
 d_n(a_i,b_j)=\min_{m\in\mathbb Z} f_{ab}(j-i+mn),\qquad a,b\in\{u,v\}.
\]
Here the minimization includes all integer windings; it is not restricted to a local neighborhood.

**2. Positive semidefiniteness for exactly four orders.** Order the vertices as \(u_0,\ldots,u_{n-1},v_0,\ldots,v_{n-1}\), anchor at \(x_0=u_0\), form \(B\) as above, and let \(z\) be an indeterminate. Exact integer determinant evaluation gives the following **complete factorizations** of \(\det(zI-B)\):

\[
\begin{aligned}
 n=5:\quad &z^4(z-18)(z-3)^4,\\
 n=6:\quad &z^4(z^2-6z+4)(z^5-36z^4+314z^3-780z^2+688z-192),\\
 n=9:\quad &z^8(z-1)(z^3-18z^2+87z-73)\\
 &\hspace{1.2em}\cdot(z^5-63z^4+669z^3-2380z^2+3309z-1548),\\
 n=10:\quad &z^9(z-2)^3(z^2-14z+4)^2(z^3-66z^2+252z-88).
\end{aligned}
\]

Each displayed nonzero factor is monic and has **strictly alternating coefficient signs**. Therefore none has a negative real root, because evaluating at a negative argument produces nonzero terms of a common sign. As \(B\) is real symmetric, all its eigenvalues are real; thus every root is nonnegative. The multiplicities of the factor \(z\) are exactly \(4,4,8,9\), respectively. Since \(B\) has size \((2n-1)\times(2n-1)\), the ranks are exactly \(5,7,9,10\). This simultaneously proves conditional negative semidefiniteness and the asserted minimal squared-Euclidean dimensions. The determinant identities are reproducibly checked with integer arithmetic by `verify.py`, using the graph edges and Newton identities for characteristic polynomials, without numerical eigensolvers.

**3. Finite obstructions for all remaining orders through \(17\).** For \(n\notin\{5,6,9,10\}\), we construct a real zero-sum coefficient vector \(c\) with \(c^{\mathsf T}D_nc>0\). Denote by \(\delta_{u_i}\) and \(\delta_{v_i}\) the coordinate vectors and write \(w_i=\delta_{v_i}-\delta_{u_i}\). The following list gives complete certificates. Each claimed quadratic value is a direct integer distance calculation via the formula in Step 1.

- \(n=7\): \(c=\delta_{u_0}+\delta_{v_2}+\delta_{v_3}-\delta_{u_2}-\delta_{v_0}-\delta_{v_6}\), with \(c^{\mathsf T}D_7c=2\).
- \(n=8\): coefficients \(c(u_i)=3(-1)^i\), \(c(v_i)=-(-1)^i\), for all \(0\le i<8\), with \(c^{\mathsf T}D_8c=16\).
- \(n=11\): \(c=w_0-w_1-w_2+w_3-w_5-w_9\), with value \(2\).
- \(n=12,14,16\): \(c=w_0+w_2+w_5+w_7\), with value \(2\) in each case.
- \(n=13\): \(c=w_0-w_1+w_3-w_4+w_8-w_9\), with value \(2\).
- \(n=15\): \(c=w_0+w_5+w_{10}\), with value \(6\).
- \(n=17\): \(c=w_0+w_5+w_{10}\), with value \(4\).

Every listed vector has zero coordinate sum. Thus none of those nine graph metrics has conditional negative type.

**4. A universal eight-vertex obstruction for every \(n\ge18\).** In each of the four indices \(i\in S=\{0,2,5,7\}\), set \(c(v_i)=1\), \(c(u_i)=-1\), and give every other vertex coefficient zero. For \(n\ge18\), the four-by-four distance blocks on these vertices, with rows and columns indexed by \(0,2,5,7\), are
\[
D_{uu}=\begin{pmatrix}0&2&5&6\\2&0&3&5\\5&3&0&2\\6&5&2&0\end{pmatrix},\quad
D_{uv}=\begin{pmatrix}1&2&4&5\\2&1&3&4\\4&3&1&2\\5&4&2&1\end{pmatrix},\quad
D_{vv}=\begin{pmatrix}0&1&5&6\\1&0&4&5\\5&4&0&1\\6&5&1&0\end{pmatrix}.
\]
Indeed, two indices in \(S\) differ in absolute value by at most \(7\). Every nonzero winding in Step 1 then has displacement magnitude at least \(n-7\ge11\). Its candidate distances in the \(uu\), \(uv\), and \(vv\) blocks are respectively at least \(8,7,6\), while the displayed zero-winding distances are at most \(6,5,6\). Thus no winding can shorten a displayed distance. Direct summation yields
\[
 c^{\mathsf T}D_nc=\mathbf1^{\mathsf T}D_{uu}\mathbf1+\mathbf1^{\mathsf T}D_{vv}\mathbf1-2\mathbf1^{\mathsf T}D_{uv}\mathbf1
 =46+44-88=2>0.
\]
This single certificate excludes **every** remaining integer \(n\ge18\), not merely those checked computationally.

**5. Translation into kernel positivity.** The finite Schoenberg negative-type equivalence gives the equivalence between Steps 2–4 and positivity of \(e^{-t d_n}\) for all \(t>0\). More explicitly, in each surviving case the positive semidefinite Gram matrix \(B/2\) provides pairwise distinct Euclidean vectors with squared distances \(d_n\). Their Euclidean Gaussian kernel is strictly positive definite for each \(t>0\). In any excluded case, the zero-sum witness from Steps 3–4 gives \(c^{\mathsf T}e^{-tD_n}c=-t(c^{\mathsf T}D_nc)+O(t^2)<0\) as \(t\downarrow0\). This proves the theorem.

## Verification

Run `python3 verify.py` from the directory containing the standalone script. It requires only Python 3's standard library. The checker constructs adjacency lists independently from the stated edge definition; performs exact integer breadth-first shortest paths; verifies all four anchored characteristic-polynomial factorizations through Newton power sums; checks every finite obstruction and its exact positive quadratic value; compares the infinite-cover distance formula with **171580 individual finite-graph distance entries** over \(5\le n\le50\); and evaluates the eight-vertex universal cover certificate and the winding bounds. The successful terminal marker is `GP_GAUSSIAN_POSITIVITY_EXACT_CHECK_OK`.

The finite checks and determinant identities are exact, not floating-point approximations. The verification range for the cover formula is corroborative, while the all-\(n\) conclusions rest on the path-reordering proof and the explicit winding bound. Finite cross-checks are not treated as infinite proof.

## Relationship to prior work

Schoenberg's finite negative-type criterion, as described by Sánchez [2], supplies the general equivalence between squared-Euclidean distances and Gaussian positive definiteness. Sánchez's analysis of supremal negative type [2] does not provide this family classification. The original generalized Petersen construction and the cyclic two-layer adjacency decomposition are classical; the adjacency spectrum in Gera and Stănică [3] is not the shortest-path **distance** kernel spectrum or its conditional sign. Kutnar and collaborators [1] give a complete but different classification of **strong distance-balancedness** for \(GP(n,2)\), with the distinct surviving orders \(\{3,5,7,10\}\) in their broader small-order convention. Kratica and collaborators [4] determine strong metric dimensions, which are not the squared-Euclidean dimensions above. Shaheen and collaborators [5] calculate distance-counting polynomials and indices for the same graph family, but do not establish the signs of all centered distance quadratic forms or positive definiteness of the exponential kernel. No implication from those results to the current four-order classification was found in the inspected material.

## Limitations

The proof establishes precisely the fixed powered-distance exponent \(p=1\). It does not classify \(e^{-t d_n^p}\) for arbitrary \(p\), does not determine a positivity cutoff for the excluded graphs at large \(t\), and does not claim novelty against every historical treatment of distance-regular or two-layer circulant metrics. The original-literature comparison was bounded; an overlooked equivalent result remains possible. The finding has received no independent mathematical audit or validation.

## References

[1] K. Kutnar, A. Malnič, D. Marušič, Š. Miklavič, *Distance-balanced graphs: symmetry conditions*, arXiv:math/0510381v1, publicly posted 2005-10-18, especially Proposition 4.1. https://arxiv.org/abs/math/0510381

[2] S. Sánchez, *On the supremal \(p\)-negative type of a finite metric space*, arXiv:1108.0451v1, publicly posted 2011-08-02. https://arxiv.org/abs/1108.0451

[3] R. Gera and P. Stănică, *The Spectrum of Generalized Petersen Graphs*, *Australasian Journal of Combinatorics* **49** (2011), 39–45; openly available author manuscript. https://faculty.nps.edu/pstanica/research/SpectraGPG_AJC_r3.pdf

[4] J. Kratica, V. Kovačević-Vujčić, M. Čangalović, *The strong metric dimension of some generalized Petersen graphs*, arXiv:1507.00881v1, publicly posted 2015-07-03. https://arxiv.org/abs/1507.00881

[5] R. Shaheen, S. Mahfud, Q. Alhawat, *Hosoya, Schultz, and Gutman Polynomials of Generalized Petersen Graphs \(P(n,1)\) and \(P(n,2)\)*, *Journal of Mathematics* (2023), Article 7341285. https://doi.org/10.1155/2023/7341285
