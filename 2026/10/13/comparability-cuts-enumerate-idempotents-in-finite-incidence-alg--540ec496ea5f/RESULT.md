# Comparability cuts enumerate idempotents in finite incidence algebras
## Finding
Let \(P\) be a nonempty finite poset and let \(I(P,\mathbb F_q)\) be its incidence algebra over the finite field \(\mathbb F_q\). Let \(G_P\) be the comparability graph of \(P\): its vertices are the elements of \(P\), and distinct vertices are adjacent exactly when they are comparable in \(P\). For a subset \(S\subseteq P\), write \(c_P(S)\) for the number of edges of \(G_P\) having exactly one endpoint in \(S\).

Then
\[
|\operatorname{Idem} I(P,\mathbb F_q)|=\sum_{S\subseteq P} q^{c_P(S)}.
\]
Equivalently, the field-size polynomial
\[
E_P(Q)=\sum_{S\subseteq P}Q^{c_P(S)}
\]
is exactly the subset cut-size enumerator of the comparability graph. Consequently \(E_P\) depends only on \(G_P\),
\[
\deg E_P=\operatorname{MaxCut}(G_P),
\]
and the leading coefficient of \(E_P\) is the number of subsets producing a maximum cut.

For a chain on \(n\) points, \(G_P=K_n\), so
\[
|\operatorname{Idem} T_n(\mathbb F_q)|=\sum_{r=0}^n \binom{n}{r}q^{r(n-r)}.
\]
For an antichain on \(n\) points, the count is \(2^n\).

## Assumptions and scope
The poset is finite and nonempty, and the coefficient ring is a finite field. The incidence algebra consists of functions \(a(x,y)\) on comparable pairs \(x\le y\), with convolution
\[
(ab)(x,y)=\sum_{x\le z\le y}a(x,z)b(z,y).
\]
Let \(J\) be its Jacobson radical. For a finite incidence algebra, \(J\) consists exactly of the functions with zero diagonal, and it has one basis vector \(e_{xy}\) for each strict comparable pair \(x<y\). Thus \(\dim_{\mathbb F_q}J=|E(G_P)|\).

The result counts all idempotents, not conjugacy classes of idempotents and not generating sets of idempotents. No assertion is made for arbitrary finite coefficient rings with nontrivial scalar idempotents.

## Proof
Fix a subset \(S\subseteq P\) and let \(\varepsilon_S\) be the diagonal idempotent whose diagonal entry is \(1\) on \(S\) and \(0\) on \(P\setminus S\).

Khripchenko and Novikov prove that every idempotent in a finitary incidence algebra over a field is conjugate to the diagonal idempotent with the same diagonal. In their proof, if \(\alpha\) is an idempotent and \(\rho=\alpha-\varepsilon_S\in J\), the conjugating unit has the form
\[
\beta=1+(2\varepsilon_S-1)\rho.
\]
Hence \(\beta\in 1+J\). Therefore the algebra group \(U=1+J\) acts transitively, by conjugation, on the idempotents having diagonal \(\varepsilon_S\).

The stabilizer of \(\varepsilon_S\) in \(U\) is
\[
1+C_J(\varepsilon_S),
\]
where \(C_J(\varepsilon_S)\) is the centralizer of \(\varepsilon_S\) inside \(J\). For a radical basis vector \(e_{xy}\) with \(x<y\),
\[
\varepsilon_S e_{xy}=\varepsilon_S(x,x)e_{xy},
\qquad
e_{xy}\varepsilon_S=\varepsilon_S(y,y)e_{xy}.
\]
Thus \(e_{xy}\) centralizes \(\varepsilon_S\) exactly when \(x\) and \(y\) lie on the same side of the cut \(S\mid P\setminus S\). It follows that
\[
\dim J-\dim C_J(\varepsilon_S)=c_P(S).
\]
Because the additive map \(j\mapsto1+j\) is a bijection from \(J\) onto \(U\),
\[
|U|=q^{\dim J},
\qquad
|\operatorname{Stab}_U(\varepsilon_S)|=q^{\dim C_J(\varepsilon_S)}.
\]
Orbit-stabilizer therefore gives exactly
\[
q^{c_P(S)}
\]
idempotents with diagonal \(\varepsilon_S\). Distinct subsets give distinct diagonals, so summing over all \(S\subseteq P\) proves the formula.

The graph consequences are immediate: the exponent attached to \(S\) is its cut size in \(G_P\). For a chain, a subset of size \(r\) cuts exactly \(r(n-r)\) edges of \(K_n\), and there are \(\binom{n}{r}\) such subsets.

## Verification
A standalone verifier enumerates every transitive relation contained in the natural order on \(1,\ldots,n\), directly enumerates every incidence-algebra element, and tests the convolution equation \(a^2=a\). It checks all such relations for \(1\le n\le4\) over \(\mathbb F_2\) and for \(1\le n\le3\) over \(\mathbb F_3\), for a total of \(60\) poset-field cases. Every direct count agrees with the cut formula. It also checks the chain specialization independently for \(1\le n\le8\) and \(q\in\{2,3,5}\).

These finite computations are consistency checks only. The theorem for every finite poset and finite field follows from the conjugacy theorem and the orbit-stabilizer argument above.

## Relationship to prior work
Khripchenko and Novikov's 2008 preprint proves the decisive structural statement: every idempotent of a finitary incidence algebra over a field is conjugate to its diagonal idempotent, and their explicit conjugator lies in \(1+J\). That source does not state the finite-field orbit sizes, the sum \(\sum_S q^{c_P(S)}\), or the comparability-cut interpretation.

For full upper-triangular matrix rings, later work of Hou describes triangular idempotents and, over finite coefficient rings, counts them. This is the chain case of the present setting, so the chain specialization is not treated here as the originality-bearing part. The new statement is the arbitrary finite-poset formula and its exact identification with the cut-size enumerator of the comparability graph.

Kolegov's 2024 incidence-algebra paper computes the minimum number of idempotent generators using the Hasse diagram and hypercube embeddings. Its invariant is the minimum size of a generating family, not the cardinality of the full idempotent set. Searches under incidence-algebra, structural-matrix, triangular-matrix, cut-enumerator, and idempotent-count formulations did not locate a source stating or implying the arbitrary-poset cut formula.

## Limitations
The proof uses that the coefficient ring is a field, so diagonal idempotents are exactly \(0\)-\(1\) choices and \(1+J\) has the simple cardinality \(q^{\dim J}\). The result does not count idempotents over general finite rings, where diagonal scalar idempotents and stabilizers can behave differently.

The exact arbitrary-poset formula was not found in the sources and database searches performed, but an unindexed structural-matrix enumeration could contain an equivalent statement. The full text of some triangular-matrix counting papers was not accessible; their published abstracts establish coverage of the chain case but do not provide evidence of coverage for general incidence algebras.

## References
1. N. S. Khripchenko and B. V. Novikov, “Finitary incidence algebras,” arXiv:0803.0069, first posted 2008-03-01; later *Communications in Algebra* 37 (2009), 1670–1676.
2. X. Hou, “Idempotents in triangular matrix rings,” *Linear and Multilinear Algebra* 69 (2021), 296–304, published online 2019-03-22, DOI 10.1080/03081087.2019.1596223.
3. N. A. Kolegov, “Idempotent generators of incidence algebras,” *Bulletin of the Australian Mathematical Society* 110 (2024), 488–497, DOI 10.1017/S0004972724000078.
