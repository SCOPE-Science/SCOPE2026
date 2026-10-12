# Leaf sibling multiplicities determine Levi factors in functional-square nilpotent evolution algebras
## Finding
Let \(E\) be a finite-dimensional evolution algebra over a field \(K\) of characteristic zero with natural basis \(\{e_v:v\in V\}\). Suppose every square is either zero or \(e_v^2=c_v e_{\sigma(v)}\) with \(c_v\in K^\times\), the resulting directed graph is acyclic, and no vertex is isolated. Direct each edge from \(v\) to \(\sigma(v)\). Let \(S\) be the sinks, let \(L\) be the leaves (vertices with no incoming children), and put
\[
L_p=\{v\in L:\sigma(v)=p\},\qquad \lambda_p=|L_p|,\qquad C_p=\operatorname{diag}(c_v:v\in L_p).
\]
Then
\[
\operatorname{Der}(E)=T\oplus B\oplus\bigoplus_p\mathfrak{so}(C_p)
\]
as a vector space, with brackets described below. Here \(T\cong K^{|S|}\) consists of componentwise depth-scalings, \(B\cong\operatorname{Mat}_{|S|\times|L|}(K)\) consists of arbitrary maps from leaves into the sink span and is an abelian ideal, and
\[
\mathfrak{so}(C_p)=\{X:C_pX+X^{\mathsf T}C_p=0\}
\]
acts on the leaf children of \(p\). Consequently
\[
\dim\operatorname{Der}(E)=|S|(1+|L|)+\sum_p\binom{\lambda_p}{2}.
\]
The Levi factor is exactly \(\bigoplus_{\lambda_p\ge3}\mathfrak{so}(C_p)\). In particular, \(\operatorname{Der}(E)\) is solvable if and only if every vertex has at most two leaf children.

## Assumptions and scope
An evolution algebra has a natural basis with \(e_ue_v=0\) for distinct basis vectors. The functional-square assumption means every nonzero basis square points to a single basis vector. Acyclicity makes the attached graph a disjoint union of rooted in-trees. The no-isolated-vertex assumption excludes zero-algebra direct summands; without it, arbitrary endomorphisms of the isolated sink subspace add further Lie factors. Characteristic zero is used both to divide by \(2\) along edges and to identify the orthogonal factors of dimension at least three as semisimple Lie algebras.

For a vertex \(v\), write \(\rho(v)\in S\) for its sink and \(d(v)\) for its directed distance to that sink. If \(D(e_v)=\sum_u d_{uv}e_u\), the diagonal part is determined by one scalar \(a_r\) for each sink \(r\):
\[
d_{vv}=2^{-d(v)}a_{\rho(v)}.
\]

## Proof
For every non-sink \(v\), applying a derivation to \(e_v^2=c_ve_{\sigma(v)}\) gives
\[
D(e_{\sigma(v)})=2d_{vv}e_{\sigma(v)}.
\]
Thus every vertex having a child has a purely diagonal derivation column, and along each edge \(v\to p\) one has \(d_{pp}=2d_{vv}\). Since every sink has a child under the no-isolated hypothesis, the diagonal coefficients are exactly the componentwise depth-scalings above, giving \(T\cong K^{|S|}\).

For distinct non-sinks \(u,v\), the identity \(D(e_ue_v)=0\) becomes
\[
c_vd_{vu}e_{\sigma(v)}+c_ud_{uv}e_{\sigma(u)}=0.
\]
If \(\sigma(u)\ne\sigma(v)\), both coefficients vanish. If \(\sigma(u)=\sigma(v)=p\), the only possible off-diagonal entries occur when both \(u\) and \(v\) are leaves, because a non-leaf column is already diagonal. On \(L_p\) the remaining relation is
\[
c_vd_{vu}+c_ud_{uv}=0,
\]
which is precisely \(C_pX+X^{\mathsf T}C_p=0\). This gives the factor \(\mathfrak{so}(C_p)\), of dimension \(\binom{\lambda_p}{2}\).

If \(r\in S\) and \(v\) is a non-sink, then \(D(e_re_v)=0\) forces the coefficient of \(e_v\) in \(D(e_r)\) to vanish. The reverse coefficient, from \(e_v\) into \(e_r\), is unrestricted exactly when \(v\) is a leaf; otherwise the column of \(v\) is diagonal. Hence the remaining free entries form \(B\cong\operatorname{Mat}_{|S|\times|L|}(K)\). Since \(S\cap L=\varnothing\), products of two such matrices vanish, so \(B\) is abelian.

The depth-scaling diagonal is constant on each sibling leaf set, so \([T,\mathfrak{so}(C_p)]=0\). Different sibling blocks commute, while \([T,B]\subseteq B\) and \([\mathfrak{so}(C_p),B]\subseteq B\). Therefore the displayed vector-space decomposition is a Lie-algebra semidirect decomposition. In characteristic zero, \(\mathfrak{so}(C_p)\) is semisimple for \(\lambda_p\ge3\), is one-dimensional abelian for \(\lambda_p=2\), and is zero for \(\lambda_p\le1\). The sum of \(T\), \(B\), and the two-leaf orthogonal factors is a solvable ideal with semisimple quotient \(\bigoplus_{\lambda_p\ge3}\mathfrak{so}(C_p)\), proving the Levi-factor and solvability statements.

## Verification
The accompanying `verify.py` independently constructs the linear derivation equations for every labeled acyclic partial functional graph on \(2\) through \(5\) vertices having no isolated vertices. For deterministic nonzero edge weights it compares the nullity of that linear system with the closed formula above modulo two large primes. This covers \(892\) labeled forests and returns `VERIFY_OK cases=892 primes=2`. These finite checks are sanity checks only; the proof above establishes the claim in characteristic zero for arbitrary finite dimension.

## Relationship to prior work
Camacho, Gómez, Omirov and Turdibaev analyze derivations through the rank of the structure matrix and completely treat the nonsingular and rank-
\(n-1\) cases. Their rank-
\(n-1\) theorem includes path-like members of the present family but does not cover arbitrary branching forests or identify graph-controlled Levi factors. Cabrera Casado, Cadavid, Rodiño Montoya and Rodriguez develop graph/twin-partition constraints for derivations, explicitly focusing on non-degenerate evolution algebras; the present nilpotent family necessarily has sinks and is therefore degenerate. Mukhamedov, Khakimov, Omirov and Qaralleh determine derivations for nilpotent algebras of maximal nilindex, again a narrow chain-type regime. Later rank-
\(n-2\) work treats several specified low-corank conditions, whereas a rooted forest here can have arbitrary structure-matrix rank. None of the inspected sources states the leaf-sibling orthogonal decomposition, its dimension formula, or the exact solvability boundary.

## Limitations
The result excludes isolated vertices and positive characteristic. Adding isolated vertices introduces a full endomorphism block on the isolated zero-algebra summand, so the stated Levi factor is no longer complete. Characteristic \(2\) changes both the edge scaling equations and the orthogonal factors; small positive characteristics also require separate Lie-theoretic treatment. The literature search did not establish an absolute novelty theorem: specialized low-rank papers could contain equivalent formulas for particular forest shapes. The claim is limited to the stated functional-square class and does not address general nilpotent evolution algebras whose basis squares have support larger than one.

## References
1. L. M. Camacho, J. R. Gómez, B. A. Omirov, R. M. Turdibaev, *The derivations of some evolution algebras*, arXiv:1004.1936, first public 2010-04-12; Linear and Multilinear Algebra 61 (2013), 309–322. MR3003426 lists MSC 17A36 and 17D92.
2. A. Elduque, A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685, first public 2013-12-17.
3. F. Mukhamedov, O. Khakimov, B. Omirov, I. Qaralleh, *Derivations and automorphisms of nilpotent evolution algebras with maximal nilindex*, arXiv:1805.10285, first public 2018-05-25.
4. Y. Cabrera Casado, P. Cadavid, M. L. Rodiño Montoya, P. M. Rodriguez, *On the characterization of the space of derivations in evolution algebras*, arXiv:1912.06925, first public 2019-12-14.
5. H. Abd El-Qader, A. T. Ab Ghani, I. Qaralleh, *On evolution algebras and their derivations*, Journal of Mathematics and Computer Science 21 (2020), 213–230, DOI 10.22436/jmcs.021.03.05.
