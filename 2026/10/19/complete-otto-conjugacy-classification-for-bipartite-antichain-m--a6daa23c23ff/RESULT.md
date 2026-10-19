# Complete Otto-conjugacy classification for bipartite antichain monoids

## Finding

For a field \(K\), let \(P=U\sqcup V\) be a finite height-two poset with \(U=\{u_1,\ldots,u_k\}\) its minimal elements and \(V=\{v_1,\ldots,v_m\}\) its maximal elements, where \(k,m\ge1\) and each maximal element covers at least one minimal element. Let \(N_j=\{i:u_i<v_j\}\) and \(d_j=|N_j|\). Put \(M=\mathbf I(P,V)\), the antichain submonoid of the incidence monoid determined by its maximal antichain \(V\). Every element has a unique block-matrix form
\[
 X(B,T)=\begin{pmatrix}I_k&B\\0&T\end{pmatrix},\qquad
 T=\operatorname{diag}(t_1,\ldots,t_m),\quad
 b_j\in K^{N_j},
\]
where \(b_j\) denotes column \(j\) of \(B\) restricted to its allowed incidences. No invertibility condition is imposed on \(t_j\).

Otto conjugacy is \(X\sim_o Y\) when there exist \(G,H\in M\) such that \(XG=GY\) and \(YH=HX\). For each column define its tag
\[
 \tau_j(t,b)=\begin{cases}
  *,&t\ne1\ \text{or}\ b=0,\\
  Kb\in\mathbb P(K^{N_j}),&t=1\ \text{and}\ b\ne0.
 \end{cases}
\]
**Complete classification:** for any \(X,Y\in M\),
\[
 X\sim_o Y\quad\Longleftrightarrow\quad
 \tau_j(X)=\tau_j(Y)\ \text{for every}\ 1\le j\le m.
\]
In particular, the class set is canonically the Cartesian product
\[
 M/{\sim_o}\ \cong\ \prod_{j=1}^m\bigl(\{*\}\sqcup\mathbb P^{d_j-1}(K)\bigr).
\]
This is a classification for the monoid relation, rather than conjugation by units, and holds over arbitrary fields, including infinite fields and characteristic two.

Over \(K=\mathbf F_q\), set
\[
 a_j=\frac{q^{d_j}-1}{q-1},\qquad B_j=1+(q-1)q^{d_j}.
\]
There are exactly \(\prod_j(1+a_j)\) Otto-conjugacy classes. More precisely, for every subset \(S\subseteq\{1,\ldots,m\}\), there are \(\prod_{j\in S}a_j\) classes with projective tags exactly at \(S\), each of size
\[
 (q-1)^{|S|}\prod_{j\notin S}B_j.
\]
The all-star class contains every idempotent and has size \(\prod_j B_j\), whereas the number of idempotents is \(\prod_j(1+q^{d_j})\). Consequently **the set of all idempotents is itself exactly one entire Otto-conjugacy class if and only if \(q=2\)**. Over every field possessing a scalar \(a\notin\{0,1\}\), the all-star class strictly contains the idempotents: the nonidempotent unit \(\operatorname{diag}(I_k,a I_m)\) belongs to it. This answers the idempotent-class question within Open Problem 7.5 of Can, Casimiro and Malheiro negatively over their complex base field.

For the complete bipartite poset \(K_{k,m}\), all \(d_j=k\), so the class number specializes to
\[
 \left(1+\frac{q^k-1}{q-1}\right)^m.
\]

## Assumptions and scope

The height-two hypothesis means that all nontrivial comparable pairs run from \(U\) to \(V\), and \(V\) consists of all maximal vertices. Every permitted incidence provides one freely chosen entry of \(B\). The relative monoid operation is ordinary matrix multiplication and is closed, since the upper-left block is fixed to \(I_k\) and lower-right blocks are diagonal. We do **not** claim a classification in the larger full incidence monoid: Otto conjugacy is determined by witnesses within \(M\), and changing the witness monoid may change the relation.

The formula applies to finite fields of prime-power order, not merely prime fields. Nonemptiness of the neighborhoods is assumed to make the projective factors standard; the elementary scalar proof also accommodates empty neighborhoods when those factors are omitted.

## Proof

Write \(X=X(B,T)\), \(Y=X(C,S)\), where \(T=\operatorname{diag}(t_j)\) and \(S=\operatorname{diag}(s_j)\). Choose witnesses \(G=X(Z,U)\) and \(H=X(W,V)\), with \(U=\operatorname{diag}(u_j)\) and \(V=\operatorname{diag}(v_j)\). Matrix multiplication gives
\[
 X(B,T)X(Z,U)=X(Z+BU,TU),\qquad
 X(Z,U)X(C,S)=X(C+ZS,US).
\]
Therefore \(XG=GY\) holds precisely when, for every \(j\),
\[
 (t_j-s_j)u_j=0,\qquad (1-s_j)z_j=c_j-b_j u_j. \tag{1}
\]
Likewise \(YH=HX\) holds precisely when
\[
 (t_j-s_j)v_j=0,\qquad (1-t_j)w_j=b_j-c_j v_j. \tag{2}
\]
All equations are independent across columns, and each \(z_j,w_j\) may be an arbitrary vector supported on \(N_j\).

Fix a column and abbreviate \((t,b)\), \((s,c)\). If \(t\ne1\) and \(s\ne1\), choose \(u=v=0\), \(z=c/(1-s)\), \(w=b/(1-t)\). This solves (1)–(2) regardless of either scalar and of the vectors. If \(t=s=1\), (1)–(2) reduce to \(c=bu\) and \(b=cv\); these equations are solvable exactly when both vectors vanish, or when both are nonzero and span the same one-dimensional subspace. If \(t=1\) and \(s\ne1\), equation \((t-s)v=0\) forces \(v=0\), and (2) forces \(b=0\); conversely, with \(b=0\), take \(u=v=0\), \(z=c/(1-s)\) and any \(w\). The case \(s=1,t\ne1\) is symmetric, forcing and being characterized by \(c=0\). These four cases are exactly equality of the tags. Solving columns independently gives global witnesses within \(M\), proving both directions and exhaustion of the classes.

Over \(\mathbf F_q\), a nonzero vector line in \(\mathbf F_q^{d_j}\) contains \(q-1\) vectors and there are \(a_j=(q^{d_j}-1)/(q-1)\) lines. Every corresponding projective-tag fiber consists of exactly \(q-1\) pairs \((t,b)\), necessarily with \(t=1\). The star fiber consists of the \((q-1)q^{d_j}\) pairs with \(t\ne1\), together with \((t,b)=(1,0)\), hence has size \(B_j\). Taking Cartesian products proves both finite-field class formulas.

An element is idempotent exactly when \(t_j^2=t_j\) and \(b_j t_j=0\) for every \(j\). Over a field, these force either \(t_j=0\) with arbitrary \(b_j\), or \((t_j,b_j)=(1,0)\). All such tags are star, and their number is \(\prod_j(1+q^{d_j})\). If \(q=2\), the star condition allows only these idempotent pairs. If \(q>2\), choose \(a\in\mathbf F_q\setminus\{0,1\}\), so \(\operatorname{diag}(I_k,a I_m)\) has all-star tags but is not idempotent. The same counterexample works over any field with more than two elements, in particular over \(\mathbf C\).

## Verification

The standalone file `verify.py` uses only the Python standard library. Invoke `python3 verify.py`. It builds actual incidence-supported block matrices, computes their entire multiplication table over \(\mathbf F_2\), \(\mathbf F_3\), and \(\mathbf F_4\), tests **all ordered pairs** against the definition of Otto conjugacy by direct witness searches, and separately checks the predicted tag classes, class sizes, idempotent totals, and equality criterion. The implementation of \(\mathbf F_4\) is the polynomial basis modulo \(x^2+x+1\). The command prints `ALL_EXACT_CHECKS_PASSED` upon success, after ten independently selected small graph/field instances, including a non-complete height-two poset.

For \(K_{2,2}\) over \(\mathbf F_2\), the 64 elements fall into 16 classes: nine singleton classes, six classes of five, and one class of 25. For \(K_{1,1}\) over \(\mathbf F_3\), the nine elements form classes of sizes two and seven; the idempotents number four, so the idempotent-containing class is strictly larger. These finite checks corroborate but do not replace the general proof in the previous section.

## Relationship to prior work

Can, Casimiro and Malheiro, *Idempotent Varieties of Incidence Monoids and Bipartite Posets* (arXiv:2208.01073v1, first publicly dated August 1, 2022), develop the relevant antichain monoids and their Green relations. Their Proposition 7.4 proves mutual Otto conjugacy **among idempotents**, and Open Problem 7.5 asks to determine the full Otto classes and whether the set of idempotents is one entire class. Neither their unit/Green classifications nor their primary-conjugacy analysis implies the present full monoid Otto partition. The proof above resolves that specific Otto question for the complete bipartite case and, by identical column equations, for arbitrary height-two bipartite posets with the maximal antichain. It does not resolve the other questions in Open Problem 7.5 about primary, norm and trace relations on general incidence monoids.

Araújo, Kinyon, Konieczny and Malheiro, *Four notions of conjugacy for abstract semigroups* (arXiv:1503.00915), compares several abstract conjugacy relations but does not give this block-column classification. The 2023 work *Conjugacy in Semigroups: the Partition and Brauer Diagram Monoids, Conjugacy Growth, and Partial Inner Automorphisms* (arXiv:2301.04252) discusses Otto conjugacy in other semigroups but does not enumerate the classes of these incidence submonoids. The classification given here is not derived from a title or search absence; its novelty assessment rests chiefly on the explicit still-open Otto question in the directly relevant 2022 paper and comparison of statements and proofs.

## Limitations

The ambient witness semigroup is essential: enlarging to a semigroup containing a zero would collapse Otto conjugacy. The result concerns Otto conjugacy, not primary, trace, or unit conjugacy; it requires the maximal-antichain block structure. A later or unindexed independent proof may exist, and mathematical priority has not been independently established. Computational checks cover only specified small finite cases; the universal assertion follows from the scalar equations, not enumeration.

## References

1. M. Bilen Can, A. Casimiro and A. Malheiro, *Idempotent Varieties of Incidence Monoids and Bipartite Posets*, arXiv:2208.01073v1 (2022), especially Sections 4–7, Proposition 7.4 and Open Problem 7.5. https://arxiv.org/abs/2208.01073
2. J. Araújo, M. Kinyon, J. Konieczny and A. Malheiro, *Four notions of conjugacy for abstract semigroups*, arXiv:1503.00915 (2015). https://arxiv.org/abs/1503.00915
3. *Conjugacy in Semigroups: the Partition and Brauer Diagram Monoids, Conjugacy Growth, and Partial Inner Automorphisms*, arXiv:2301.04252 (2023). https://arxiv.org/abs/2301.04252
