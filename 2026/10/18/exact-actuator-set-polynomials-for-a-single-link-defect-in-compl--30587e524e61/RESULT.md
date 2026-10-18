# Exact actuator-set polynomials for a single-link defect in complete bipartite networks

## Finding
Let \(p,q\ge3\) be integers and \(c\ge0\). Give every cross-edge of a complete bipartite graph \(K_{p,q}\) unit conductance except one distinguished edge \(a_0b_0\), whose conductance is \(c\). When \(c=0\) the exceptional edge is deleted. Let \(A'=A\setminus\{a_0\}\), \(B'=B\setminus\{b_0\}\), and \(N=p+q\). For a set \(S\) of independently actuated vertices, consider the real continuous-time system \(\dot x=-L_c x+B_Su\), where \(L_c\) is the weighted combinatorial Laplacian and the columns of \(B_S\) are the individual coordinate vectors indexed by \(S\).

**Complete controllability classification.** The pair \((-L_c,B_S)\) is controllable precisely in the following cases:

1. When \(c\ne1\) and \(p\ne q\), both \(|S\cap A'|\ge p-2\) and \(|S\cap B'|\ge q-2\).
2. When \(c\ne1\) and \(p=q=n\), those same two inequalities hold and additionally \(|S|\ge2n-3\).
3. When \(c=1\), both \(|S\cap A|\ge p-1\) and \(|S\cap B|\ge q-1\).

Consequently the **entire actuator-set generating polynomial** \(\mathcal C_{p,q,c}(z)=\sum_{S:\,(-L_c,B_S)\,\mathrm{controllable}}z^{|S|}\) is
\[
\mathcal C_{p,q,c}(z)=
\begin{cases}
z^{N-4}(z+p-1)(z+q-1)(1+z)^2,&c\ne1,\ p\ne q,\\[2pt]
z^{2n-4}\bigl((z+n-1)^2(1+z)^2-(n-1)^2\bigr),&c\ne1,\ p=q=n,\\[2pt]
z^{N-2}(z+p)(z+q),&c=1.
\end{cases}
\]
In particular the minimum number of independent inputs and the number of minimum input sets are, respectively,
\[
(\gamma,M_{\min})=
\begin{cases}
(N-4,(p-1)(q-1)),&c\ne1,\ p\ne q,\\
(2n-3,2n(n-1)),&c\ne1,\ p=q=n,\\
(N-2,pq),&c=1.
\end{cases}
\]
For a connected complete bipartite support (\(c>0\)), its known zero-forcing number is \(N-2\). Hence for any \(c>0\) with \(c\ne1\), the fixed weighted-Laplacian actuator minimum lies **two below** that structural sufficient bound when \(p\ne q\), and **one below** it when \(p=q\). This contrast does not assert strong structural controllability for arbitrary edge conductances.

## Assumptions and scope
All conductances other than the singled-out cross-edge equal one; the single exceptional conductance \(c\) is nonnegative and may be zero. The graph is connected for every \(p,q\ge3\), including \(c=0\). Each selected vertex receives a separate, independently adjustable input. The claim concerns exact algebraic controllability for a fixed weighted Laplacian; it does not bound control energy or condition numbers as \(c\to1\). The theorem covers *every* vertex subset and *every* \(p,q\ge3\), not just placements invariant under a graph automorphism.

## Proof
Write a vector in the four orbit coordinates \((u_0,u,v_0,v)\), where the coordinates on \(A'\) share value \(u\), those on \(B'\) share value \(v\), and the distinguished endpoints have values \(u_0,v_0\). The restriction of \(L_c\) to this four-dimensional orbit-constant space has matrix
\[
Q=\begin{pmatrix}
q-1+c&0&-c&-(q-1)\\
0&q&-1&-(q-1)\\
-c&-(p-1)&p-1+c&0\\
-1&-(p-1)&0&p
\end{pmatrix}.
\]
(The nonsymmetric display is simply the matrix in a nonorthonormal orbit basis; \(L_c\) itself is symmetric.) Orthogonally complementary to this space are the \(A'\)-supported vectors of sum zero, an eigenspace \(E_A\) of eigenvalue \(q\) and dimension \(p-2\), and the analogous \(B'\)-supported space \(E_B\) of eigenvalue \(p\) and dimension \(q-2\). In particular, unless at least \(p-2\) coordinates of \(A'\) and at least \(q-2\) coordinates of \(B'\) are actuated, a nonzero vector in one of these spaces vanishes on every input coordinate; the symmetric-matrix Popov--Belevitch--Hautus criterion then proves noncontrollability.

For \(p\ne q\), direct determinant expansion gives
\[
\det(pI-Q)=p(c-1)(p-q)(q-1),\qquad
\det(qI-Q)=-q(c-1)(p-1)(p-q).
\]
When \(c\ne1\), neither \(p\) nor \(q\) is an eigenvalue of the orbit-constant restriction. Thus an eigenvector with either eigenvalue lies wholly in \(E_A\) or \(E_B\); every other eigenvector is orbit-constant. If a nonzero orbit-constant eigenvector vanished on a leader in each of \(A'\) and \(B'\), its orbit values would satisfy \(u=v=0\). The \(A'\) row of \(Qw=\lambda w\) then forces \(v_0=0\), and its \(B'\) row forces \(u_0=0\), a contradiction. Because the two orbit-cardinality lower bounds each select at least one regular vertex, they are sufficient as well as necessary. This proves case 1 without assuming any simplicity of the remaining eigenvalues.

For \(p=q=n\), one has the exact factorization
\[
\det(\lambda I-Q)=\lambda(\lambda-n)\left[\lambda^2-(2c+3n-2)\lambda+2c(2n-1)+2(n-1)^2\right].
\]
The bracket evaluated at \(\lambda=n\) equals \(2(c-1)(n-1)\); its discriminant is \((2c-n)^2+4(n-1)>0\). If \(c\ne1\), therefore, \(n\) is a simple quotient eigenvalue, whose orbit eigenvector is proportional to \((-(n-1),1,-(n-1),1)\). Combining it with \(E_A,E_B\) gives the *entire* eigenspace
\[
E_n=\left\{x:\ x_{a_0}=x_{b_0}=-\sum_{a\in A'}x_a=-\sum_{b\in B'}x_b\right\},\qquad \dim E_n=2n-3.
\]
For such an eigenspace to be observed injectively, at least \(2n-3\) coordinates must be selected. Conversely, suppose \(|S\cap A'|\ge n-2\), \(|S\cap B'|\ge n-2\), and \(|S|\ge2n-3\). If a vector of \(E_n\) vanishes on \(S\), then each regular orbit has at most one potentially nonzero coordinate. If either distinguished endpoint belongs to \(S\), the two endpoint values are both zero, and the zero-sum equations force both remaining regular coordinates to vanish. If neither endpoint belongs to \(S\), the bound on \(|S|\) leaves at most one unselected regular vertex *in total*; one regular orbit is entirely zero, so the common endpoint value is zero and again the equations force all coordinates to vanish. The other eigenvalues lie only in the orbit-constant subspace and are observed by a selected regular vertex from each orbit, as proved above. This establishes case 2.

Finally if \(c=1\), the graph is the unit-weight \(K_{p,q}\). Its Laplacian eigenspaces comprise the constant vector, the bipartition-contrast vector, vectors supported in \(A\) summing to zero (eigenvalue \(q\)), and vectors supported in \(B\) summing to zero (eigenvalue \(p\)); when \(p=q\) the latter two belong to the same eigenspace. A zero-sum coordinate space is observed injectively exactly when all but at most one coordinate of that side are selected. This proves case 3; the constant and contrast eigenvectors cannot vanish on both selected sides.

In each case the Popov--Belevitch--Hautus criterion now gives the asserted if-and-only-if classification. To count sets, selecting at least \(p-2\) of the \(p-1\) vertices in \(A'\) contributes \(z^{p-2}(z+p-1)\), and similarly for \(B'\); either endpoint is independently optional and contributes \((1+z)^2\). In the balanced defective case, precisely the \((n-1)^2\) sets of size \(2n-4\), consisting of \(n-2\) regular vertices from each part and no endpoint, must be removed. In the homogeneous case, each part allows at most one unselected vertex, giving \(z^{p-1}(z+p)z^{q-1}(z+q)\). Reading the smallest positive-degree coefficient yields the minimum counts. For \(c>0\), the zero-forcing number of \(K_{p,q}\) is \(N-2\), because two uncolored vertices in one part can never be individually forced and all but one in each part suffice.

## Verification
A standalone Python 3 program `verify.py` constructs the weighted integer/rational Laplacian and, for each of two large primes, compares an independently computed finite-field Kalman rank for **every vertex subset** against the theorem. It tests \((p,q)=(3,3),(3,4),(4,4),(4,5),(5,5)\) and \(c\in\{0,1/2,1,2,5/2\}\). The actual run reported `VERIFY_OK 19840 individual truth-table entries over two primes`. This exhausts those finite instances but is not a proof for arbitrary part sizes or real conductances; the preceding eigenspace argument supplies the infinite-family proof. The computations do not assess numerical control energy near the exceptional parameter \(c=1\).

## Relationship to prior work
Yuan, Zhao, Di, Wang and Lai established the general exact-controllability framework using maximum eigenvalue geometric multiplicity and the PBH rank condition. Their result motivates the *problem*, but a maximum eigenvalue multiplicity concerns the minimum dimension of a sufficiently flexible input matrix and by itself need not give the minimum number of **coordinate-constrained** actuators. It does not state the three regimes or count all independently actuated vertex subsets for the one-exception weighted bipartite family. Monshizadeh, Zhang and Camlibel characterized strong structural controllability through zero forcing in a graph's qualitative matrix class. That is a different quantifier: the present claim fixes one Laplacian for each chosen conductance, and its inputs can be fewer than the structural zero-forcing upper bound. Klee and Stamps derived characteristic-polynomial identities and spectra for related bipartite families, including deleting a *whole* perfect matching; the inspected results are spectral, not all-input-set classification for a *single* edge defect. General spectral or PBH formulas are not presented as newly discovered here. The claimed contribution is the explicit full-parameter placement classification and generating polynomial, especially its simultaneous part-balance and link-homogeneity singularities.

## Limitations
The result uses equal background conductances and exactly one exceptional cross-edge, with independent coordinate inputs and \(p,q\ge3\). It does not address arbitrary heterogeneous backgrounds, joint-input constraints, exact minimum energy, or how ill-conditioned the reachable directions become as \(c\to1\). No independent mathematical audit has been performed. An equivalent specialized theorem could exist in literature not captured by the inspected sources.

## References
1. Z. Yuan, C. Zhao, Z. Di, W.-X. Wang and Y.-C. Lai, *Exact controllability of complex networks*, Nature Communications **4**, 2447 (first public 12 September 2013), DOI: 10.1038/ncomms3447. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC3945876/.
2. N. Monshizadeh, S. Zhang and M. K. Camlibel, *Zero forcing sets and controllability of dynamical systems defined on graphs*, arXiv:1403.4868 (first public 19 March 2014), https://arxiv.org/abs/1403.4868.
3. S. Klee and M. T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations*, arXiv:2008.01669 (4 August 2020), https://arxiv.org/abs/2008.01669.
