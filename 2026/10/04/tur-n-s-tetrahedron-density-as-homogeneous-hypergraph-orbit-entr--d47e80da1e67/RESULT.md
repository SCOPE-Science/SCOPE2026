# Turán's tetrahedron density as homogeneous-hypergraph orbit entropy

Let \(M\) be the countable universal homogeneous tetrahedron-free \(3\)-uniform hypergraph, and let \(a_n\) be the number of \(\operatorname{Aut}(M)\)-orbits on injective ordered \(n\)-tuples.

## Exact orbit/counting identification

Siniora and Solecki explicitly list the universal homogeneous tetrahedron-free \(3\)-hypergraph as a free homogeneous structure. Its age is the class of finite \(K_4^{(3)}\)-free \(3\)-uniform hypergraphs. For an injective ordered tuple \((x_1,\ldots,x_n)\), the tuple positions label the induced finite hypergraph on \([n]\). Homogeneity says that two such tuples lie in the same automorphism orbit exactly when these labeled induced hypergraphs agree, while universality realizes every finite labeled tetrahedron-free \(3\)-graph. Therefore

\[
\boxed{a_n=\operatorname{forb}(n,K_4^{(3)})},
\]

where \(\operatorname{forb}(n,K_4^{(3)})\) denotes the number of labeled tetrahedron-free \(3\)-graphs on \([n]\).

Nagle and Rödl proved, for every fixed forbidden \(3\)-uniform hypergraph \(F\), that

\[
\log_2 \operatorname{forb}(n,F)=\operatorname{ex}(n,F)+o(n^3).
\]

Consequently,

\[
\boxed{\lim_{n\to\infty}\frac{\log_2 a_n}{\binom n3}=\pi(K_4^{(3)})}.
\]

This turns the classical tetrahedron Turán-density problem into an exact entropy statement about the automorphism group of one canonical countable homogeneous structure. In particular,

\[
\pi(K_4^{(3)})=\frac59
\quad\Longleftrightarrow\quad
\lim_{n\to\infty}\frac{\log_2 a_n}{\binom n3}=\frac59.
\]

The standard Turán construction gives the lower bound \(5/9\). A September 2026 flag-algebra computation of Jeong, Park, Im, Lee, and Yang gives

\[
\frac59\le
\lim_{n\to\infty}\frac{\log_2 a_n}{\binom n3}
\le
\frac{312372062889819}{560000000000000}
<0.557808.
\]

The upper bound is prior work; the contribution retained here is the model-theoretic identification that makes the Turán density itself an injective tuple-orbit entropy.

## Finite replay

Exhaustive enumeration through six vertices gives

\[
a_n=1,1,1,2,15,768,477965\qquad(n=0,\ldots,6),
\]

with corresponding extremal edge counts

\[
0,0,0,1,3,7,14.
\]

The bundled verifier independently enumerates all \(2^{\binom n3}\) labeled \(3\)-graphs for \(n\le6\), rejects exactly those containing a tetrahedron, checks the above counts and extremal numbers, and checks the published upper-bound fraction numerically. It terminates with `VERIFY_OK`.

## Sources

- Daoud Siniora and Sławomir Solecki, *Coherent extension of partial automorphisms, free amalgamation and automorphism groups*, arXiv:1705.01888; first submitted 2017-05-04; Journal of Symbolic Logic 85 (2020), 199–223. Example 4.3 explicitly lists the universal homogeneous tetrahedron-free \(3\)-hypergraph.
- Brendan Nagle and Vojtěch Rödl, *The asymptotic number of triple systems not containing a fixed one*, Discrete Mathematics 235 (2001), 271–290, DOI 10.1016/S0012-365X(00)00280-6.
- Gyeongwon Jeong, Seonghun Park, Seonghyuk Im, Joonkyung Lee, and Hongseok Yang, *A New Upper Bound for the Turán Density of the Tetrahedron*, arXiv:2609.27495 (2026). This is used only to state the current numerical upper bound, not for scope eligibility.
