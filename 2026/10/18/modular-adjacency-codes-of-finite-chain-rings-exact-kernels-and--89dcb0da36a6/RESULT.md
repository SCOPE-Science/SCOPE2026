# Modular adjacency codes of finite chain rings: exact kernels and weight-one socle words

## Finding

Let \(R\) be any finite commutative chain ring with maximal ideal \(\mathfrak m=(\pi)\), residue-field order \(q=p^f\), and nilpotency length \(m\geq3\), meaning \(\mathfrak m^m=0\ne\mathfrak m^{m-1}\). Let \(A\) be the **loopless** adjacency matrix of the ordinary zero-divisor graph on the nonzero zero divisors of \(R\), with \(A_{xy}=1\) if \(x\ne y\) and \(xy=0\), and zero otherwise. Regard \(A\) as a matrix over the prime field \(\mathbb F_p\). Define the row-space code \(C=\operatorname{rowsp}_{\mathbb F_p}(A)\).

Then its exact parameters, dual parameters, and Euclidean hull are

\[
\boxed{C:\ [q^{m-1}-1,\ q^{\lfloor m/2\rfloor},\ 1]_p,\qquad
C^\perp:\ [q^{m-1}-1,\ q^{m-1}-1-q^{\lfloor m/2\rfloor},\ 2]_p,\qquad
\dim_{\mathbb F_p}(C\cap C^\perp)=1.}
\]

In fact every unit coordinate vector supported on a vertex from the nonzero socle \(\mathfrak m^{m-1}\setminus\{0\}\) belongs to \(C\). The dual code admits the explicit parametrization given below, valid for **all** lengths and all residue-field sizes, including mixed-characteristic chain rings. The stated minimum distance of \(1\) differs from the minimum distance \(2\) reported for the length-four odd-prime truncated-polynomial subfamily in [1, Theorem 4.6]; an explicit row combination proves the distance-one assertion in the same conventional code definition.

## Assumptions and scope

Write \(V_i=\mathfrak m^i\setminus\mathfrak m^{i+1}\) for \(1\leq i\leq m-1\), and let \(\nu(x)=i\) for \(x\in V_i\). These disjoint valuation classes are precisely the graph vertices, with

\[
|V_i|=(q-1)q^{m-i-1},\qquad
|V|=q^{m-1}-1,\qquad
x\sim y\ \Longleftrightarrow\ x\ne y\text{ and }\nu(x)+\nu(y)\geq m.
\]

Here \(\mathbb F_p\) is the coefficient field of the graph code and need not be a coefficient subfield of \(R\). Set \(t=\lceil m/2\rceil\), \(P=\bigcup_{i=1}^{t-1}V_i\), and, for a vector \(z\in\mathbb F_p^{V}\), set \(s_j(z)=\sum_{x\in V_j}z_x\). The cardinality of the low-valuation part is

\[
|P|=q^{m-1}-q^{\lfloor m/2\rfloor}.
\]

The theorem concerns **ordinary adjacency row codes**, not the binary vertex-edge incidence code, the graph Laplacian code, the real matrix minimum-rank invariant, or the adjacency matrix with self-loops retained.

## Proof

**1. Exact kernel.** Let \(z\in\ker_{\mathbb F_p}A\). For \(x\in V_i\), the adjacency equation is

\[
(Az)_x=\sum_{j=m-i}^{m-1}s_j(z)-\boldsymbol 1_{2i\geq m}\,z_x,
\]

where the subtraction accounts exactly for a forbidden diagonal edge when \(x^2=0\). Thus, for every \(i\geq t\), all entries of \(z\) in \(V_i\) equal one common scalar \(c_i\). Since

\[
|V_i|\equiv0\pmod p\quad(1\leq i\leq m-2),\qquad |V_{m-1}|=q-1\equiv-1\pmod p,
\]

we have \(s_i(z)=0\) on these nonsocle high layers and \(s_{m-1}(z)=-c_{m-1}\). The equation at any low-valuation vertex \(x\in V_i\), \(i<t\), therefore gives \(c_{m-1}=0\). The equation in \(V_{m-1}\) then gives \(\sum_{j=1}^{t-1}s_j(z)=0\). For each \(t\leq i\leq m-2\), the remaining equation uniquely determines

\[
\boxed{z_x=c_i=\sum_{j=m-i}^{t-1}s_j(z)\quad\text{for every }x\in V_i,}
\]

where an empty sum is zero. Conversely, any vector on \(P\) whose total coordinate sum is zero extends uniquely by this formula and by setting its socle coordinates to zero; substituting into the adjacency equations verifies \(Az=0\). Consequently the kernel is naturally isomorphic to

\[
\boxed{\ker A\ \cong\ \bigl\{z\in\mathbb F_p^P:\sum_{x\in P}z_x=0\bigr\},}
\]

with the high-coordinate extension described explicitly above. This is a statement about the whole kernel, not merely its dimension. Its dimension is \(|P|-1\), and rank-nullity gives

\[
\operatorname{rank}_{\mathbb F_p} A
=(q^{m-1}-1)-(|P|-1)=q^{\lfloor m/2\rfloor}.
\]

**2. Socle words of weight one.** Fix any vertex \(u\in V_1\). Its row in \(A\) is precisely the characteristic vector \(\mathbf1_{V_{m-1}}\) of the nonzero socle. For distinct \(a,b\in V_{m-1}\), their adjacency rows satisfy \(r_b-r_a=e_a-e_b\), since each socle vertex is adjacent to every other vertex. Writing \(h=|V_{m-1}|=q-1\), for any fixed \(a\in V_{m-1}\),

\[
h e_a=r_u+\sum_{b\in V_{m-1}\setminus\{a\}}(r_b-r_a).
\]

Because \(h\equiv-1\ne0\pmod p\), this is an explicit row-span representation of \(e_a\), valid even when the socle has a single vertex. Hence \(d(C)=1\). This argument also gives a concrete checkable witness for the length-four case in [1].

**3. Dual distance.** Since \(A\) is symmetric, \(C^\perp=\ker A\). The kernel parametrization prohibits a nonzero vector supported on a single coordinate. On the other hand, \(V_1\) has at least two vertices, and \(e_a-e_b\in\ker A\) for distinct \(a,b\in V_1\), by its zero layer-sums and zero high extension. Therefore \(d(C^\perp)=2\).

**4. Hull.** On two kernel vectors \(z,w\), the contributions to their standard Euclidean inner product from high layers \(V_i\) with \(t\leq i\leq m-2\) are products of block constants multiplied by \(|V_i|\equiv0\pmod p\); the socle contributions vanish. Thus the inner product on \(\ker A\) is exactly the standard dot product on the low-coordinate zero-sum hyperplane \(H\subset\mathbb F_p^P\). The radical of that restricted form is \(H\cap\langle\mathbf1_P\rangle\). Because \(p\mid |P|\), it is one-dimensional. Also each \(|V_i|\) for \(i<t\) is divisible by \(p\), so the high extension of \(\mathbf1_P\) is zero. Since \(C=(\ker A)^\perp\), the radical is exactly

\[
\boxed{C\cap C^\perp=\operatorname{span}_{\mathbb F_p}(\mathbf1_P),}
\]

where \(\mathbf1_P\) is zero outside \(P\). This completes all assertions.

## Verification

The standalone, dependency-free program `verify.py` constructs the **loopless** adjacency matrix from valuation classes, applies modular Gaussian elimination without using the rank formula, tests a full basis of the proposed dual, verifies that every socle coordinate vector lies in the row space, and computes the kernel Gram rank to check the hull. It also checks the dual weight-two witness and the absence of zero columns.

The 16 tested triples \((q,m,p)\) were \((2,3,2)\), \((2,4,2)\), \((2,5,2)\), \((2,6,2)\), \((2,7,2)\), \((2,8,2)\), \((3,3,3)\), \((3,4,3)\), \((3,5,3)\), \((3,6,3)\), \((4,3,2)\), \((4,4,2)\), \((4,5,2)\), \((5,3,5)\), \((5,4,5)\), and \((9,3,3)\). All passed (`VERIFY_OK 16 independent finite configurations`). In particular, the \(q=3,m=4\) case has length \(26\), dimension \(9\), and a socle-supported weight-one codeword. These finite tests corroborate but do not replace the universal proof above.

## Relationship to prior work

Sarkar–Hansda–Maji [1], publicly posted October 6, 2026, treats adjacency codes of the length-four truncated polynomial ring over odd prime fields. Its Theorem 4.6 determines the dimension and dual zero-sum subspace in that restricted case and states a primal minimum distance of \(2\); its Theorem 4.7 determines a one-dimensional hull. The present result explicitly **includes** that special case in its dimension, dual, and hull assertions, but the weight-one socle row combination shows that its primal minimum-distance assertion is not valid for the conventional row-space definition given there. The new calculation covers arbitrary nilpotency lengths, extension residue fields, and mixed-characteristic chain rings, with higher-valuation dual-coordinate lifts that appear only at longer lengths.

Tirop–Oduor–Olwamba [2] study real-linear adjacency matrices of Galois rings and state a different rank expression; those results are neither modular row-space-code classifications nor a covering implication for the present theorem. Rather [3] treats ordinary adjacency spectra of truncated polynomial rings; a real spectrum does not determine rank after reduction modulo \(p\). Published indexed results on **real symmetric minimum rank** of chain-ring zero-divisor graphs concern a minimization over all admissible matrix entries, which is a different invariant from the rank of this fixed adjacency matrix over \(\mathbb F_p\).

## Limitations

The ring must be a finite **commutative chain ring** and the nilpotency length at least three. No statement is made about arbitrary Artinian local rings with nonprincipal maximal ideal, about graphs with loops, incidence-code parameters, or Euclidean codes over an unrelated characteristic. The theorem treats the row-space code over the residue characteristic \(p\), not arbitrary auxiliary characteristics. The result does **not** claim a new asymptotically good family of error-correcting codes: their primal minimum distance is one. Equivalent earlier formulations or unindexed modular-rank calculations cannot be absolutely excluded by literature searches. Independent mathematical validation has not been performed.

## References

[1] A. Sarkar, K. Hansda and M. Maji, *Graph-Based Linear Codes Associated with the Finite Ring \(\mathbb F_p[x]/\langle x^4\rangle\)*, arXiv:2610.08480v1 (October 6, 2026), Sections 3 and 4.2, Theorems 4.6–4.7. https://arxiv.org/abs/2610.08480

[2] R. G. Tirop, M. O. Oduor and L. O. Olwamba, *On the Adjacency Matrices of the Anderson-Livingston Zero Divisor Graphs of Galois Rings*, International Journal of Algebra **13** (2019), 153–160, Section 3.3 and Propositions 6–7. https://doi.org/10.12988/ija.2019.9211

[3] B. A. Rather, *Spectral Properties of Zero-Divisor Graphs of Truncated Polynomial Rings*, arXiv:2604.03101 (April 2026). https://arxiv.org/abs/2604.03101

[4] D. F. Anderson and P. S. Livingston, *The zero-divisor graph of a commutative ring*, Journal of Algebra **217** (1999), 434–447. https://doi.org/10.1006/jabr.1998.7840
