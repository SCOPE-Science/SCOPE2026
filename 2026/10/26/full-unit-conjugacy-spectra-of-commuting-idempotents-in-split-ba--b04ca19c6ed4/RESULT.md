# Full-unit conjugacy spectra of commuting idempotents in split basic algebras
## Finding
Let \(A\) be a finite-dimensional unital split basic algebra over the finite field \(k=\mathbb F_q\), with Jacobson radical \(J\) and \(A/J\cong k^n\). Choose a complete primitive orthogonal idempotent system \(e_1,\dots,e_n\), indexed compatibly with the factors of \(A/J\). Set
\[
w_{ij}=\dim_k(e_iJe_j)+\dim_k(e_jJe_i)\quad(i<j),\qquad
Q=2^r,\quad d(c)=\sum_{i<j}w_{ij}\mathbf1_{c_i\ne c_j}.
\]
For every \(r\ge1\), a quotient-coloring \(c:\{1,\dots,n\}\to\{0,1\}^r\) specifies precisely **one** orbit under simultaneous conjugation by \(A^\times\) of ordered pairwise-commuting idempotent \(r\)-tuples. Its cardinality is exactly \(q^{d(c)}\). Consequently the **conjugacy-orbit size spectrum**, with one term per class, is
\[
\mathcal C_{A,r}(X)=\sum_{c:\{1,\ldots,n\}\to[Q]}X^{d(c)},\qquad
\#\{\text{ordered commuting idempotent tuples}\}=\mathcal C_{A,r}(q),\qquad
\#\{\text{conjugacy classes}\}=Q^n.
\]
If \(G_A\) is the loopless multigraph with \(w_{ij}\) edges between \(i\) and \(j\), \(m=|E(G_A)|\), and \(k(F)\) is the number of components of a spanning edge subgraph, then
\[
\mathcal C_{A,r}(X)=\sum_{F\subseteq E(G_A)}X^{m-|F|}(1-X)^{|F|}Q^{k(F)}.
\]
In particular, this complete class-size spectrum is insensitive to the radical's internal multiplication and to dimensions \(\dim(e_iJe_i)\) at fixed off-diagonal Peirce weights.

A natural, infinite nonreconstruction family is provided by the directed two-cycle with arrow ideal \(\mathfrak a\). For every integer \(s\ge1\), the nonisomorphic algebras \(A_{2s}=kQ/\mathfrak a^{2s}\) and \(A_{2s+1}=kQ/\mathfrak a^{2s+1}\) have different Loewy lengths but, for **every** \(r\ge1\) and every finite field \(k\), identical complete full-unit orbit-size polynomials
\[
\mathcal C_{A_{2s},r}(X)=\mathcal C_{A_{2s+1},r}(X)
=Q+Q(Q-1)X^{2s}.
\]
The formula is for the multiset of orbit cardinalities, not an isomorphism of the two unit groups or equality of their stabilizer orders.

## Assumptions and scope
All fields are finite \(k=\mathbb F_q\), of arbitrary characteristic. The algebra is associative, unital, finite-dimensional and split basic: its semisimple quotient is a direct product of copies of \(k\), each once. The integer \(r\ge1\) is arbitrary but finite. The group is the **full unit group** \(A^\times\), acting by simultaneous inner conjugation on ordered pairwise-commuting idempotents; neither coordinate permutations nor algebra automorphisms are divided out. An idempotent means \(x^2=x\). A Peirce corner \(e_iJe_j\) is a \(k\)-vector space; \(J\) is a nilpotent ideal. The polynomial \(\mathcal C\) has one monomial per conjugacy class, not one per tuple.

## Proof
**1. Spectral colors.** Given commuting idempotents \((b_1,\dots,b_r)\), for each bit-vector \(\alpha\in\{0,1\}^r\) define the polynomial expression
\[
f_\alpha=\prod_{h=1}^r\left(\alpha_hb_h+(1-\alpha_h)(1-b_h)\right).
\]
Then the \(f_\alpha\) are pairwise orthogonal idempotents summing to \(1\), and \(b_h=\sum_{\alpha:\alpha_h=1}f_\alpha\). Their images in \(A/J\cong k^n\) give a **unique** labeling \(c_i\in\{0,1\}^r\) of the \(n\) primitive semisimple coordinates. This works in characteristic two as well.

**2. Transitivity in a quotient-color fiber.** For a coloring \(c\), put \(d_\alpha=\sum_{i:c_i=\alpha}e_i\), an orthogonal family summing to \(1\). Suppose \((f_\alpha)_\alpha\) is any other complete orthogonal family with the same quotient images. The element
\[
u=\sum_\alpha f_\alpha d_\alpha
\]
is congruent to \(1\) modulo \(J\), hence is invertible because \(J\) is nilpotent. Furthermore \(u d_\beta=f_\beta u\) for every \(\beta\), by pairwise orthogonality. Therefore \(f_\beta=ud_\beta u^{-1}\) simultaneously. Thus the subgroup \(1+J\le A^\times\) already acts transitively on each color fiber. Distinct fibers cannot be conjugate because the semisimple quotient is commutative, so conjugation acts trivially there. Hence there is exactly one **full-unit** orbit per coloring.

**3. Exact orbit size.** For the standard family \((d_\alpha)\), the centralizer inside \(J\) is precisely
\[
J_c=\bigoplus_{i,j:\,c_i=c_j}e_iJe_j.
\]
Indeed, \(x\in e_iJe_j\) commutes with all \(d_\alpha\) exactly when \(i,j\) have the same color. The stabilizer under \(1+J\) is the group \(1+J_c\); therefore
\[
\#(1+J)\cdot(d_\alpha)=\frac{q^{\dim J}}{q^{\dim J_c}}=q^{\sum_{i,j:\,c_i\ne c_j}\dim(e_iJe_j)}=q^{d(c)}.
\]
Since the full-unit orbit is exactly that \(1+J\)-orbit, this is also the desired full-unit orbit size. Alternatively, the stabilizer in \(A^\times\) has size \((q-1)^nq^{\dim J_c}\), while \(\# A^\times=(q-1)^nq^{\dim J}\). In particular the calculation applies even when \(J^2\ne0\): only its **additive Peirce dimensions**, not the radical multiplication, enter.

**4. Graph expansion.** Give each of the \(w_{ij}\) undirected multiedges weight \(X\) if its endpoint colors differ, and \(1\) otherwise. Multiplication over all edges yields \(X^{d(c)}\). The factor on any edge is \(X+(1-X)\mathbf1_{c_i=c_j}\); expanding and summing over the \(Q^n\) colorings gives the spanning-subgraph formula, since each selected edge subset forces constant color on each of its \(k(F)\) connected components. Substituting \(X=q\) weights each unit orbit by its size, producing the tuple count.

**5. Infinite Loewy-length ambiguity.** In the quiver with vertices \(1,2\) and one arrow in each direction, an off-diagonal path necessarily has odd length. For the quotient \(A_\ell=kQ/\mathfrak a^\ell\), the two off-diagonal corner dimensions count oriented odd-length paths shorter than \(\ell\). For \(\ell=2s\) and \(2s+1\), these are precisely lengths \(1,3,\dots,2s-1\), with one path of each length in each direction, so \(w_{12}=2s\) in both algebras. With \(n=2\) vertices, there are \(Q\) equal-color colorings and \(Q(Q-1)\) unequal-color colorings. This proves the displayed polynomial. Their radical nilpotency indices are respectively \(2s\) and \(2s+1\), so the algebras are nonisomorphic. There is no field-characteristic exception.

## Verification
The attached `verify.py` uses only the Python standard library. It enumerates every element and every commuting idempotent pair in the two-cycle path-algebra quotients of radical cutoffs two and three over \(\mathbb F_2\) and \(\mathbb F_3\), checks the formulas for \(r=1,2\), verifies each pair's full-unit orbit index directly from the unit centralizer size, and cross-checks the coloring sum against the Fortuin–Kasteleyn subset expansion. Additional three-chain incidence-algebra cases are exhaustively checked for the counts of single and pairwise commuting idempotents. Run `python3 verify.py`; the last output line must be `COMMUTING_IDEMPOTENT_POTTS_OK`. Finite examples are not proofs of the all-parameter statement; the argument above supplies that proof.

## Relationship to prior work
The basic lifting/conjugacy of idempotents modulo nilpotent radicals is classical, and the simultaneous diagonalization lemma for incidence algebras is explicitly provided by Santulo–Souza–Yasumura (2019), Lemma 8. Earlier work by Gargate–Gargate (2020) counts single polynomial-potent elements of triangular and selected incidence algebras; Sokal (2005) develops the Fortuin–Kasteleyn/Tutte identity. Related published work by Mazurek–Nielsen–Ziembowski (2015) studies lifts of commuting idempotents modulo Jacobson radicals. Those premises are not claimed as new. A previously recorded incidence-algebra result already contains the incidence-only all-arity affine component and Tutte count, so the incidence specialization is also **not** claimed new. The present asserted advance is the universal **full-unit conjugacy class-size spectrum** for arbitrary split basic algebras, including algebras with loops, oriented cycles, arbitrary relations and high Loewy length, and the resulting infinite family of distinct Loewy lengths that no such all-arity orbit-size data distinguish.

## Limitations
The result requires split basic algebras; semisimple matrix blocks and nonsplit division-field factors are excluded. The polynomial records orbit **cardinalities**, not abstract stabilizer groups or isomorphisms of unit groups. The classification of every arbitrary subalgebra or idempotent over a nonfield base is not asserted. A general theorem on nilpotent radical conjugacy could imply much of the orbit enumeration indirectly; the literature search is bounded and does not prove world-wide priority. The full 2015 comparison article could not be accessed through the available noninteractive route, so possible stronger coverage remains a residual risk. No independent mathematical audit has been performed.

## References
- A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, arXiv:math/0503607, first publicly submitted 2005-03-25. https://arxiv.org/abs/math/0503607
- R. Mazurek, P. P. Nielsen and M. Ziembowski, *Commuting idempotents, square-free modules, and the exchange property*, *Journal of Algebra* 444 (2015), 52–80, DOI:10.1016/j.jalgebra.2015.07.015. https://doi.org/10.1016/j.jalgebra.2015.07.015
- E. A. Santulo Jr., J. P. Souza and F. Y. Yasumura, *Group gradings on finite dimensional incidence algebras*, arXiv:1905.08391, Lemma 8. https://arxiv.org/abs/1905.08391
- I. Gargate and M. Gargate, *\((k+1)\)-potent Matrices in triangular matrix Groups and Incidence Algebras of Finite Posets*, arXiv:2009.04243. https://arxiv.org/abs/2009.04243
