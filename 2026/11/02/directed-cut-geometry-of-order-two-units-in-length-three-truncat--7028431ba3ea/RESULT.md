# Directed-cut geometry of order-two units in length-three truncated quiver algebras

## Finding

Let \(Q\) be any finite directed multiquiver, including loops and parallel arrows, and let \(k\) be any field of characteristic \(2\). Put \(A=kQ/J^3\), where \(J\) is the arrow ideal, and set \(G=1+J(A)\). Write \(m=|Q_1|\) and let \(p_2\) be the number of ordered pairs of composable arrows, including repeated arrows. Form a simple conflict graph \(\Gamma_Q\) whose vertices are the **nonloop** arrows; two distinct vertices are adjacent when the corresponding arrows can be concatenated in at least one order. Write \(I_{\Gamma_Q}(t)=\sum_{S\ \mathrm{independent}}t^{|S|}\).

**Complete algebraic-geometric classification.** The reduced \(k\)-scheme of normalized order-dividing-two units
\[
\mathcal T_Q=\{g\in G:g^2=1\}
\]
is the product of \(\mathbb A^{p_2}\) with the coordinate-subspace arrangement defined by the edge ideal of \(\Gamma_Q\). Its irreducible components are indexed by the inclusion-maximal independent sets \(S\) of \(\Gamma_Q\), with each component isomorphic to \(\mathbb A^{p_2+|S|}\). The **unreduced normalized involution scheme** is reduced if and only if \(Q\) has no loops; in the presence of a loop, the corresponding arrow-coordinate square vanishes scheme-theoretically and gives genuine nilpotents in the coordinate ring. This statement is about \(1+J(A)\), **not** the potentially thicker involution scheme of the full unit group.

The maximum component dimension has a direct graph-theoretic interpretation:
\[
\boxed{\dim(\mathcal T_Q)_{\mathrm{red}}=p_2+\operatorname{MaxDiCut}(Q)},
\]
where \(\operatorname{MaxDiCut}(Q)=\max_{U\subseteq Q_0}|\{a\in Q_1:s(a)\in U,\ t(a)\notin U\}|\). Computing this dimension from a variable quiver is NP-hard, already on loopless quivers obtained by doubling every edge of a simple undirected graph.

**Exact arithmetic.** For every finite field \(\mathbb F_q\) of characteristic \(2\), the number of elements of order dividing \(2\) in \(G\) is
\[
\boxed{N_Q(q)=q^{p_2}I_{\Gamma_Q}(q-1)}.
\]
Since \(|G|=q^{m+p_2}\) and all elements of \(G\) have order dividing \(4\), precisely \(N_Q(q)-1\) elements have exact order \(2\), and precisely \(q^{m+p_2}-N_Q(q)\) have exact order \(4\). The exponent is \(4\) if and only if \(Q\) has a length-two directed path, including repetitions of a loop. If there is no such path the exponent is at most \(2\); if \(Q\) has no arrows the group is trivial.

For the consistently oriented directed cycle with \(n\ge3\) arrows, \(p_2=n\), the conflict graph is the ordinary cycle graph, and
\[
N_Q(q)=q^n L_n(q),\quad L_0(q)=2,\quad L_1(q)=1,\quad
L_n(q)=L_{n-1}(q)+(q-1)L_{n-2}(q).
\]
In particular a directed triangle has \(N_Q(2)=32\) and \(N_Q(4)=640\).

## Assumptions and scope

Here \(Q_0\) and \(Q_1\) denote finite sets of vertices and labelled arrows. Distinct length-two paths remain linearly independent in the truncated path algebra, even when their endpoints agree. A loop is an arrow with identical initial and terminal vertices, and is excluded from \(\Gamma_Q\) because its coefficient must vanish at every geometric involution point. The arrow ideal in \(kQ/J^3\) satisfies \(J^3=0\). For a finite field, \(q=2^e\) with \(e\ge1\). The variety and reduced-scheme statements hold over arbitrary characteristic-two fields, including imperfect ones, and over their algebraic closures. The ring \(kQ/J^3\) need not be local, acyclic, or loopless.

The independent-set polynomial uses nonempty and empty independent sets, the latter contributing \(1\). The full unit group's order-two **geometric points** coincide with those in \(G\), but its nonreduced scheme is not identified with the normalized scheme: diagonal equations can carry additional infinitesimal structure.

## Proof

**Step 1 (normalization).** A unit of \(A\) maps to a unit of the semisimple quotient \(A/J\cong k^{Q_0}\). If \(g^2=1\), each image coordinate \(\lambda_v\) satisfies \(\lambda_v^2=1\), which in characteristic two forces \(\lambda_v=1\) on field-valued points. Thus every order-dividing-two unit is uniquely \(g=1+u\), where \(u\in J\). Conversely, \(1+u\) is invertible for every \(u\in J\).

**Step 2 (independent monomial equations).** Write \(u=u_1+u_2\), with \(u_1=\sum_{a\in Q_1}c_a a\) and \(u_2\) a linear combination of length-two paths. Since \(J^3=0\), \(u^2=u_1^2\), while \((1+u)^2=1+u^2\). For every length-two path \((a,b)\) with \(t(a)=s(b)\), its coefficient in \(u_1^2\) is exactly \(c_a c_b\). All such paths form a basis of \(J^2\); therefore \(u^2=0\) if and only if \(c_ac_b=0\) for every composable ordered pair. When \(a\) is a loop, \((a,a)\) imposes \(c_a^2=0\), whence \(c_a=0\) on field-valued points. For distinct nonloop arrows this becomes precisely the edge monomials of \(\Gamma_Q\). All \(p_2\) coefficients of \(u_2\) are unrestricted.

**Step 3 (scheme and components).** The coordinate ring of the normalized involution scheme is a polynomial ring in the arrow and length-two-path coefficients modulo the homogeneous quadratic monomials of Step 2. Its radical is obtained by setting each loop variable to zero and imposing the squarefree edge ideal of \(\Gamma_Q\). A squarefree monomial edge ideal is the intersection of the monomial primes \((c_a:a\notin S)\) over maximal independent sets \(S\) (the claim follows directly by testing monomial supports). These primes are incomparable, giving exactly the asserted components and dimensions. If there is a loop its variable is a nonzero nilpotent class, since its square is in the defining ideal but the variable itself is not in this quadratic ideal; with no loops the ideal is squarefree and hence radical.

**Step 4 (directed cuts).** Any independent set of arrows \(S\) has disjoint source-vertex and target-vertex sets: otherwise two supported arrows could concatenate. Thus \(S\) is contained in the set of all arrows crossing the directed cut from its source set to its complement. Conversely every directed-cut arrow set is independent, because its arrows all point out of the cut subset and none can follow another. Hence \(\alpha(\Gamma_Q)=\operatorname{MaxDiCut}(Q)\), proving the dimension formula. For an undirected graph \(H\), construct \(Q\) with both orientations of every edge of \(H\). Every directed cut of \(Q\) has size exactly the corresponding undirected cut in \(H\). The number \(p_2=\sum_v\deg_H(v)^2\) is directly computable. Thus a polynomial-time dimension algorithm would compute MaxCut, which is NP-hard even for unweighted simple graphs (Garey–Johnson–Stockmeyer 1976).

**Step 5 (finite-field counts and exponent).** A support \(S\) of nonzero arrow coefficients is admissible exactly when \(S\) is an independent set. Each supported arrow coefficient can take \(q-1\) nonzero values, and all \(p_2\) length-two coefficients can take \(q\) values. Summation gives \(N_Q(q)=q^{p_2}I_{\Gamma_Q}(q-1)\). The group has cardinality \(q^{m+p_2}\). In characteristic two \((1+u)^4=1+u^4=1\) because \(J^3=0\). If any length-two path exists, choose an arrow coefficient on each participating arrow equal to \(1\); if they coincide choose just its loop coefficient. The resulting \(u^2\ne0\), so there is an element of exact order \(4\). Otherwise \(J^2=0\) and every unit in \(G\) has order at most \(2\). For an oriented cycle, \(\Gamma_Q\) is an undirected cycle; its independence polynomial is the stated recurrence sequence via the standard two-state transfer matrix (or deletion recurrence) and the cycle closure condition.

## Verification

Run `python3 verify.py` using Python 3 without third-party packages. The program constructs all vertex, arrow and length-two-path basis elements, forms the full multiplication table, and directly squares every element \(1+u\) in 27 complete small finite-field cases over \(\mathbb F_2\), \(\mathbb F_4\) and \(\mathbb F_8\). It independently counts admissible arrow supports and evaluates the right-hand side of the formula, and it checks maximum independent-set size against maximum directed cut in twelve quivers. The tested quivers include loops, two loops at a vertex, parallel arrows, cycles, paths, forks and disconnected cases. The terminal success marker is `CUBIC_QUIVER_INVOLUTION_OK 27 complete finite-field multiplications 12 geometry comparisons`.

Finite checks are not an infinite proof and do not certify novelty; all universal conclusions follow from the preceding algebraic and graph-theoretic arguments.

## Relationship to prior work

Dugas, Huisgen-Zimmermann and Learned (arXiv:1407.2672v1, 10 July 2014) define and investigate truncated path algebras and their homological/module-theoretic invariants. Bleher, Chinburg and Huisgen-Zimmermann (arXiv:1407.3045v1, 11 July 2014) classify irreducible components of **module representation varieties** for radical-square-zero algebras. Neither inspected work gives the present characteristic-two equation \(g^2=1\) in the **unit group** of a radical-cube-zero algebra or its directed-cut dimension and finite-field census. André, Freitas and Neto (arXiv:1502.01512v1, 5 February 2015) develop supercharacter theory for algebra groups equipped with **algebra anti-involutions in odd characteristic**; their word "involutive" does not mean counting order-two group elements, and their scope differs. Standard edge-ideal/independence-complex theory supplies the coordinate-subspace step, and the NP-hardness reduction uses the established NP-completeness of MaxCut; those background facts are not themselves new.

The claimed addition is the simultaneous natural identification of the normalized order-two-unit geometry, exact field counts, order distribution, directed-cut dimension, and scheme-reducedness criterion for all finite quivers at radical length three. This is a combination of standard tools applied to a distinct natural object, not a claim to new methods in monomial-ideal theory or graph complexity.

## Limitations

The theorem is specific to characteristic two and the length-three truncation. It does not enumerate conjugacy classes of order-two elements, classify the full automorphism group, or identify the nonreduced full-unit-group involution scheme. It does not address other nilpotence lengths or quotient relations identifying distinct length-two paths. Inaccessible or unindexed literature could already contain a substantially equivalent result; no exhaustive historical publication-priority certification or independent mathematical audit has been performed.

## References

1. A. Dugas, B. Huisgen-Zimmermann, J. Learned, *Truncated path algebras are homologically transparent*, arXiv:1407.2672v1 (first public posting 2014-07-10), https://arxiv.org/pdf/1407.2672.
2. F. M. Bleher, T. Chinburg, B. Huisgen-Zimmermann, *The geometry of finite dimensional algebras with vanishing radical square*, arXiv:1407.3045v1 (2014-07-11), https://arxiv.org/pdf/1407.3045.
3. C. A. M. André, P. J. Freitas, A. M. Neto, *A supercharacter theory for involutive algebra groups*, arXiv:1502.01512v1 (2015-02-05), https://arxiv.org/pdf/1502.01512.
4. M. R. Garey, D. S. Johnson, L. Stockmeyer, *Some simplified NP-complete graph problems*, Theoretical Computer Science 1 (1976), 237–267, https://doi.org/10.1016/0304-3975(76)90059-1.
