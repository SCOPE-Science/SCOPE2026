# Degree rigidity and ring reconstruction from finite-field idempotent annihilation graphs

## Finding

For every prime power \(q\) and integer \(n\ge 2\), let \(R=M_n(\mathbb F_q)\). Its **one-sided idempotent annihilation graph** \(\Gamma_{n,q}\) has as vertices all \(E\in R\) satisfying \(E^2=E\) and \(E\notin\{0,I\}\); two distinct vertices \(E,F\) are adjacent when \(EF=0\) **or** \(FE=0\). Write \({a\brack b}_q\) for the Gaussian binomial coefficient, with value zero when \(b\notin\{0,\ldots,a\}\).

**Rank-resolved degrees.** For an arbitrary vertex \(E\) of rank \(r\in\{1,\ldots,n-1\}\), the exact number of neighbors of rank \(s\in\{1,\ldots,n-1\}\) is
\[
D_{n,q}(r,s)=\begin{cases}
{n-r\brack s}_q\bigl(2q^{s(n-s)}-q^{s(n-r-s)}\bigr),&s\le n-r,\\
0,&s>n-r.
\end{cases}
\]
In particular its degree depends only on \(r\), and equals \(d_{n,q}(r)=\sum_{s=1}^{n-r}D_{n,q}(r,s)\). There are exactly \(m_r={n\brack r}_qq^{r(n-r)}\) vertices of rank \(r\).

**Degree rigidity.** For \(n\ge3\), the degrees satisfy
\[
d_{n,q}(1)>d_{n,q}(2)>\cdots>d_{n,q}(n-1).
\]
Thus the abstract graph degree of a vertex uniquely identifies its algebraic matrix rank, and the graph has exactly \(n-1\) degree values. In dimension \(n=2\), the graph is regular of degree \(2q-1\), as already proved by Patil–Momale–Jadhav.

**Ring reconstruction.** Let \(\delta\) be the minimum graph degree and \(M\) its multiplicity in the ordinary (unlabeled) graph-degree multiset. Then
\[
Q=\frac{\delta+1}{2}=q^{n-1},\qquad A=\frac{M}{Q}=\frac{q^n-1}{q-1},
\qquad \boxed{q=\frac{A-1}{A-Q}.}
\]
The dimension \(n\) is the unique integer \(\ge2\) satisfying \(Q=q^{n-1}\). Consequently, among finite fields and matrix sizes at least two,
\[
\boxed{\Gamma_{n,q}\cong\Gamma_{m,t}\ \Longleftrightarrow\ n=m\text{ and }q=t.}
\]
This reconstructs the isomorphism type of the full matrix ring from two elementary graph-degree statistics.

For example, when \(n=3\) and \(q=2\), the 56 vertices split into 28 rank-one vertices of degree 25 and 28 rank-two vertices of degree 7. For \(n=4,q=2\), the rank strata have multiplicities \((120,560,120)\) and degrees \((295,73,15)\).

## Assumptions and scope

All rings are full associative unital matrix rings \(M_n(\mathbb F_q)\) over finite fields; \(q\) may be any prime power and the characteristic may be two. Matrix rank is ordinary linear rank. The graph is simple and undirected, but its adjacency is an **OR** of the two ordered zero-product conditions; replacing OR by AND changes the graph and theorem. Neither the zero matrix nor the identity is a vertex. The zero-dimensional and one-dimensional matrix-ring cases are excluded since their graphs have no vertices. A finite-field order is determined only up to field isomorphism, which is enough for the ring classification.

Define \({a\brack b}_q=\prod_{i=0}^{b-1}(q^{a-i}-1)/(q^{b-i}-1)\) for \(0\le b\le a\). All terms in the degree formulas have nonnegative exponents because the first branch imposes \(s\le n-r\). The vertex count \(m_r\) is for labeled matrices rather than similarity classes.

## Proof

**1. Idempotents are ordered decompositions.** An idempotent \(F\) of rank \(s\) is precisely the projection associated with \(V=W\oplus L\), where \(V=\mathbb F_q^n\), \(W=\operatorname{im}F\) is an \(s\)-plane, and \(L=\ker F\) is a complementary \((n-s)\)-plane. There are \({n\brack s}_q\) choices for \(W\) and \(q^{s(n-s)}\) complements \(L\) (graphs of arbitrary linear maps from a fixed complement into \(W\)). Hence \(m_s={n\brack s}_qq^{s(n-s)}\).

**2. Directed and mutual annihilation counts.** Fix a rank-\(r\) idempotent \(E\), and put \(U=\operatorname{im}E\), \(T=\ker E\), so \(V=U\oplus T\) with \(\dim T=n-r\). The equation \(EF=0\) is equivalent to \(W\subseteq T\). For \(s\le n-r\), there are \({n-r\brack s}_q\) choices of \(W\subseteq T\), and for each \(W\), \(q^{s(n-s)}\) kernels complementary to \(W\). Thus
\[
\#\{F: \operatorname{rank}F=s,\ EF=0\}={n-r\brack s}_qq^{s(n-s)}.
\]
Transposing \(E,F\), a bijection of idempotents preserving rank and conjugacy class, shows the same count for \(FE=0\). Alternatively, the latter requires \(U\subseteq\ker F\).

Both equations hold exactly when \(W\subseteq T\) and \(U\subseteq L\). For fixed \(W\subseteq T\), such a complement \(L\) has the form \(U\oplus C\) where \(T=W\oplus C\). The number of complements \(C\) to \(W\) inside \(T\) is \(q^{s(n-r-s)}\). Hence
\[
\#\{F: \operatorname{rank}F=s,\ EF=FE=0\}={n-r\brack s}_qq^{s(n-r-s)}.
\]
Inclusion–exclusion gives \(D_{n,q}(r,s)\). If \(s>n-r\), neither ordered zero product can occur. Because a nonzero idempotent has \(E^2=E\ne0\), there is no self-loop to subtract.

**3. Strict rank monotonicity.** For \(1\le r\le n-1\), choose the coordinate projections \(E_r=\operatorname{diag}(I_r,0)\) on one fixed vector space. Whenever \(E_rF=0\), also \(E_{r-1}F=0\), and whenever \(FE_r=0\), also \(FE_{r-1}=0\). Hence for \(r\ge2\), every graph neighbor of \(E_r\) is a neighbor of \(E_{r-1}\). This inclusion is strict: take \(F\) to be the rank-one projection whose image is \(\langle e_r\rangle\), with \(F(e_1)=e_r\), \(F(e_r)=e_r\), and \(F(e_j)=0\) for all other basis vectors. Then \(E_{r-1}F=0\), whereas \(E_rF\ne0\) and \(FE_r\ne0\). Thus \(d_{n,q}(r-1)>d_{n,q}(r)\). When \(n=2\) only rank one occurs, and its displayed degree is \(2q-1\).

**4. Recover \(q\) and \(n\).** The smallest degree belongs exactly to rank \(n-1\), including the singleton degree class when \(n=2\). The rank-\((n-1)\) vertex can only have rank-one neighbors, giving \(\delta=2q^{n-1}-1\). The number of rank-\((n-1)\) vertices is \(M=q^{n-1}{n\brack1}_q\). Therefore \(Q=q^{n-1}\) and \(A={n\brack1}_q=1+q+\cdots+q^{n-1}\). Since \(A-Q=1+q+\cdots+q^{n-2}>0\), the exact algebraic rearrangement \(q(A-Q)=A-1\) uniquely recovers \(q\). As \(q>1\), \(Q=q^{n-1}\) then uniquely recovers \(n\). Any graph isomorphism preserves its minimum degree and multiplicity, so it forces identical \((n,q)\). Conversely finite fields of the same order are isomorphic and induce graph isomorphisms between their matrix rings.

## Verification

The companion program `check_matrix_idempotent_annihilation.py` is a standalone Python finite-field and matrix enumerator with no third-party dependencies. It enumerates **all** matrices for the indicated small dimensions, identifies idempotents directly by matrix multiplication, computes their ranks using elimination over the actual finite field, and tests each ordered pair for \(EF=0\) and \(FE=0\). It compares every observed neighbor-rank coefficient against the formula, checks rank-stratum multiplicities, and verifies the reconstruction expressions. The independent implementation includes \(\mathbb F_4\cong\mathbb F_2[z]/(z^2+z+1)\), so the tests are not limited to prime fields.

The completed exhaustive cases are \((n,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(4,2)\), comprising **699,372 ordered vertex pairs**. It also checks an auxiliary orientation-sensitive reverse-product-rank identity as a consistency test, not as an additional novelty claim. The full recorded output is in `check_matrix_idempotent_annihilation.out`. These finite computations support but do not prove the general theorem; the proof is the four steps above.

## Relationship to prior work

Patil, Momale and Jadhav (arXiv:2402.11256v1, February 17, 2024), Sections 2–4, define **exactly the same OR-adjacency graph** for \(2\times2\) matrix rings and prove regularity with degree \(2q-1\) in that dimension. That case is therefore **prior work**, not part of the originality claim. The present contribution concerns every dimension, strict rank-dependent irregularity for all \(n\ge3\), and recovery of the matrix ring's parameters from the unlabeled degree multiset.

Ferraz, Polcino Milies and Taufer (arXiv:1711.09289v1, November 25, 2017) count left ideals and their idempotent generators over finite fields. Their Gaussian rank counts underlie the vertex stratification and are not claimed as new. Akbari and collaborators' older idempotent graph uses the stronger requirement \(EF=FE=0\) (**AND**, not OR). A related earlier finite-field count of directed zero-product **triangles** gives ordered counts for \(PQ=QR=RP=0\), and in particular yields one-sided pair information; that is also not claimed as new. The genuinely assessed graph conclusion here is exact **OR-adjacency** degree stratification, its strict rank rigidity and the graph-isomorphism reconstruction theorem. Separate work on full zero-divisor and trace graphs studies different vertex sets or adjacency predicates.

## Limitations

No claim is made about arbitrary finite rings, arbitrary division rings, spectral or diameter invariants, or non-idempotent matrices. The formula is proved over all finite fields, but computations only cover the seven finite parameter choices listed. The full text of some older specialist graph literature was not accessible; an independently established equivalent reconstruction theorem remains a residual priority risk. Originality here is a best-knowledge comparison with inspected publications and relevant prior algebraic results, not an exhaustive guarantee. No external independent mathematical audit has been performed.

## References

1. A. Patil, P. S. Momale and C. M. Jadhav, *On the Idempotent Graph of Matrix Ring*, arXiv:2402.11256v1 (2024-02-17). Full text: https://arxiv.org/html/2402.11256v1.
2. R. A. Ferraz, C. Polcino Milies and E. Taufer, *Left ideals in matrix rings over finite fields*, arXiv:1711.09289v1 (2017-11-25). Full text: https://arxiv.org/html/1711.09289v1.
3. Akbari et al., *On the idempotent graph of a ring*, Journal of Algebra and Its Applications, DOI:10.1142/S0219498813500035 (2013). Earlier AND-adjacency definition; full text not independently checked.
