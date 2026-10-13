# Cyclic upper-triangular matrices: diagonal-word orbits and exact finite-field density

## Finding

For each prime power \(q\ge 2\), let \(T_n(q)\) be the algebra of upper-triangular \(n\times n\) matrices over \(\mathbb F_q\), and let \(B_n(q)=T_n(q)^\times\) act on \(T_n(q)\) by conjugation. Call \(A\) *cyclic* if its characteristic and minimal polynomials coincide (equivalently, \(\deg m_A=n\)). Write \(N=\binom n2\). For a fixed diagonal word \(d=(d_1,\ldots,d_n)\), write \(k=|\{d_1,\ldots,d_n}\}|\).

**Theorem.** For every \(n\ge1\) and every ordered diagonal word, cyclic matrices with that word form exactly one \(B_n(q)\)-conjugacy orbit. Its size and the stabilizer size are
\[
\#\{A\in T_n(q):A\text{ cyclic},\ \operatorname{diag}A=d\}=q^{N-n+k}(q-1)^{n-k},
\qquad |C_{B_n(q)}(A)|=q^{n-k}(q-1)^k.
\]
In particular, there are exactly \(q^n\) such conjugacy orbits, each indexed by its ordered diagonal word. If \(f(t)=\prod_\lambda(t-\lambda)^{m_\lambda}\) splits in \(\mathbb F_q[t]\), let \(k\) denote the number of \(\lambda\) with \(m_\lambda>0\). Then the number of cyclic upper-triangular matrices with characteristic polynomial \(f\) is
\[
\frac{n!}{\prod_\lambda m_\lambda!}\,q^{N-n+k}(q-1)^{n-k}.
\]
A nonsplit characteristic polynomial occurs for no upper-triangular matrix.

Writing \(S(n,k)\) for Stirling numbers of the second kind, \((q)_k=q(q-1)\cdots(q-k+1)\), and \(\rho=(q-1)/q\), the exact cyclicity probability is
\[
P_{n,q}=\frac{1}{q^n}\sum_{k=1}^{\min(n,q)} (q)_k S(n,k)\rho^{n-k}.
\]
With \(P_{0,q}=1\), the exponential generating function is
\[
\sum_{n\ge0}q^nP_{n,q}\frac{z^n}{n!}
=\left(\frac{qe^{\rho z}-1}{q-1}\right)^q.
\]
For every fixed \(q\ge2\), as \(n\to\infty\),
\[
P_{n,q}\sim \left(\frac{q}{q-1}\right)^q \left(1-\frac{1}{q}\right)^n.
\]

## Assumptions and scope

The coefficient field is an arbitrary finite field, including extension fields and characteristic two. All ordered diagonal entries are specified, not only their multiset; the acting group is the full invertible upper-triangular group, not the unrestricted general linear group or the unitriangular subgroup. The sum counts matrices from the entire finite algebra \(T_n(q)\), of cardinality \(q^{n(n+1)/2}\). Every integer \(n\ge1\) is covered. Noncyclic matrices are not classified by the theorem.

## Proof

**1. Nonemptiness of every cyclic diagonal stratum.** Fix a word \(d\). For each distinct \(\lambda\), list the positions at which it appears as \(i_1<\cdots<i_m\). Define an upper-triangular matrix with diagonal \(d\) and entry \(1\) at every \((i_j,i_{j+1})\) in each such list, with all other strict upper entries zero. Reorder the standard basis by eigenvalue. The resulting operator is a direct sum of one Jordan block of size \(m\) for each eigenvalue; its minimal and characteristic polynomials are both \(f(t)=\prod_\lambda(t-\lambda)^{m_\lambda}\). Thus every word supports a cyclic matrix.

**2. Uniqueness of a cyclic orbit.** A cyclic matrix with characteristic polynomial \(f\) makes \(V=\mathbb F_q^n\) into a cyclic \(\mathbb F_q[t]\)-module isomorphic to \(R=\mathbb F_q[t]/(f)\), where \(t\) acts by the matrix. Every invariant subspace of \(R\) is a uniquely determined ideal \((h)/(f)\) for a monic divisor \(h\mid f\). Multiplication by \(t\) on this ideal has characteristic polynomial \(f/h\), since the module is isomorphic to \(\mathbb F_q[t]/(f/h)\). Consequently, for every monic divisor \(g\mid f\), there is **exactly one** invariant subspace of characteristic polynomial \(g\).

Now suppose \(A,A'\) are cyclic upper-triangular matrices with the same word \(d\). Both are similar over \(\mathbb F_q\), because both have a single cyclic module with defining polynomial \(f\). Let \(S\in\operatorname{GL}_n(\mathbb F_q)\) intertwine their actions. For each \(1\le i\le n\), the standard prefix \(V_i=\operatorname{span}(e_1,\ldots,e_i)\) is invariant under both operators, and its characteristic polynomial is \(f_i(t)=\prod_{j\le i}(t-d_j)\). The unique-invariant-subspace property forces \(S(V_i)=V_i\) for every \(i\). Therefore \(S\) is invertible upper triangular, so the two matrices lie in one \(B_n(q)\)-orbit. Conjugation within \(B_n(q)\) preserves the diagonal word, so distinct words cannot give the same orbit.

**3. Finite orbit sizes.** Because \(A\) is cyclic, its full matrix centralizer is \(\mathbb F_q[A]\cong \mathbb F_q[t]/(f)\). Every commuting invertible matrix is a polynomial in the upper-triangular matrix \(A\), hence belongs to \(B_n(q)\). The Chinese remainder decomposition of \(f\) gives
\[
|C_{B_n(q)}(A)|=|R^\times|
=\prod_{\lambda:m_\lambda>0} (q^{m_\lambda}-q^{m_\lambda-1})
=q^{n-k}(q-1)^k.
\]
Since \(|B_n(q)|=(q-1)^nq^N\), orbit-stabilizer proves the fixed-word formula. There are \(n!/\prod m_\lambda!\) words with the given multiplicities, proving the prescribed-characteristic-polynomial formula.

**4. Exact total and density.** There are \((q)_k S(n,k)\) words on the field alphabet with exactly \(k\) distinct symbols: partition the \(n\) positions into \(k\) nonempty fibers and assign distinct field values to these fibers. Summing the preceding orbit sizes gives
\[
C_{n,q}=q^N\sum_{k=1}^{\min(n,q)}(q)_k S(n,k)\rho^{n-k},\qquad P_{n,q}=C_{n,q}/q^{n+N}.
\]
The standard Stirling exponential generating identity \(\sum_{n\ge k}S(n,k)u^n/n!=(e^u-1)^k/k!\) and the binomial theorem yield the stated generating function.

Expanding its \(q\)-th power gives, for \(n\ge1\), the exact finite power sum
\[
P_{n,q}=\frac{\rho^n}{q^n(q-1)^q}
\sum_{j=1}^q (-1)^{q-j}\binom qj q^j j^n.
\]
For fixed \(q\), the term \(j=q\) is \(q^q q^n\), and every other term is exponentially smaller by a factor at most \(((q-1)/q)^n\). This proves the asserted asymptotic and concludes the proof.

## Verification

The accompanying standalone `verify_cyclic_borel.py` independently computes \(\dim\mathbb F_q[A]\) as the rank of \(I,A,\ldots,A^{n-1}\) and compares its direct enumeration of every upper-triangular matrix with the theorem separately for **every prescribed diagonal word**. Exhaustive cases are \((q,n)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3),(3,4),(4,2),(4,3),(5,2),(5,3)\), with \(\mathbb F_4\) represented using \(u^2+u+1=0\). It additionally checks equality of the Stirling and finite-power-sum formulas for \(q=2,3,4,5,7,8,9,11\) and \(1\le n\le30\). The final-package replay is documented in `VERIFICATION.md`. Finite tests are corroboration, not an infinite proof.

For illustration, \(C_{4,2}=240\) out of \(1024\) upper-triangular matrices; \(C_{4,3}=31752\) out of \(59049\). The exact density tends to zero exponentially for fixed field order.

## Relationship to prior work

Neumann and Praeger (1995) and Wall (1999) study cyclic matrices in unrestricted finite-field matrix spaces, and therefore do not directly enumerate individual *flag-preserving* cyclic orbits. Brown, Praeger, and Giudici (2011) give a detailed enumeration of cyclic matrices preserving **one** subspace and prove the cyclic-module invariant-subspace lemma used here; preserving one subspace is substantially weaker than preserving the entire ordered complete flag. Their maximal-reducible-algebra asymptotics cannot supply the exact all-flag density without additional analysis.

The regular-nilpotent (single-eigenvalue, nilpotent) **special case is already known**: Fresse (2013, §4.2) describes the regular nilpotent Borel orbit, and Yip (2013, p.1018, Eq. (1) following it) explicitly records \((q-1)^{n-1}q^{\binom{n-1}2}\) nilpotent matrices with one Jordan block. The present combined claim is the precise **mixed-diagonal ordered-word** orbit decomposition for all finite fields, its fixed split polynomial multiplicities, and the complete Stirling density and exponential decay. None of these full formulas was identified in the inspected sources; this is not a claim of proof of historical uniqueness.

## Limitations

No classification of noncyclic Borel orbits, Jordan type strata with multiple blocks per eigenvalue, or upper unitriangular orbits is asserted. An exhaustive bibliographic audit is not possible; the relevant 1995 paper was accessible only through its catalog rather than full text. The 1995 publication month is verified but an exact first-publication day is not. The first-public-date field in the accompanying metadata therefore uses the fully verified day-level initial public date of the 2011 primary research source instead of fabricating a 1995 calendar day. Other equivalent historical formulations may exist. No independent mathematical audit has been performed.

## References

1. P. M. Neumann and C. E. Praeger, “Cyclic Matrices Over Finite Fields,” *Journal of the London Mathematical Society* **52** (1995), 263–284, DOI:10.1112/jlms/52.2.263. Publication month known; full text not inspected.
2. G. E. Wall, “Counting cyclic and separable matrices over a finite field,” *Bull. Austral. Math. Soc.* **60** (1999), 253–284, DOI:10.1017/S000497270003639X. Abstract/citation inspected, not full text.
3. S. Brown, C. E. Praeger and M. Giudici, “Proportions of Cyclic Matrices in Maximal Reducible Matrix Groups and Algebras,” arXiv:1105.4078v1 (20 May 2011), https://arxiv.org/pdf/1105.4078. Full primary text, in particular invariant-submodule results and §4.3, inspected.
4. L. Fresse, “Upper triangular parts of conjugacy classes of nilpotent matrices with finite number of B-orbits,” *J. Math. Soc. Japan* **65** (2013), 967–992, DOI:10.2969/jmsj/06530967, https://www.jstage.jst.go.jp/article/jmath/65/3/65_967/_pdf/-char/en. Full text inspected, including the regular-nilpotent case.
5. M. Yip, “q-Rook placements and Jordan forms of upper-triangular nilpotent matrices,” *Discrete Math. Theor. Comput. Sci.*, FPSAC 2013 proceedings, 1017–1028, DOI:10.46298/dmtcs.2362, https://dmtcs.episciences.org/en/articles/2362/download. Full text inspected, including p.1018.
