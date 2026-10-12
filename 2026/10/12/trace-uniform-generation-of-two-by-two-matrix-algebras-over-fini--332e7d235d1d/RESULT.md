# Trace-uniform generation of two-by-two matrix algebras over finite fields

## Finding
Let \(q\) be any prime power, let \(m\ge1\), and put \(A=M_2(\mathbb F_q)\). For any vector \(\boldsymbol\tau=(\tau_1,\ldots,\tau_m)\in\mathbb F_q^m\), define the fixed-trace generating fiber
\[
N_{q,m}(\boldsymbol\tau)=\#\bigl\{(X_1,\ldots,X_m)\in A^m:\operatorname{tr}X_i=\tau_i\;(1\le i\le m),\;\mathbb F_q\langle I,X_1,\ldots,X_m\rangle=A\bigr\}.
\]
Then **every trace fiber has exactly the same number of algebra generators**:
\[
\boxed{N_{q,m}(\boldsymbol\tau)=q^m(q^m-1)(q^m-q).}
\]
This includes characteristic two, where adding a scalar matrix cannot change its trace. The statement is non-vacuous exactly when \(m\ge2\).

Write \(G_{q,m}=q^{2m}(q^m-1)(q^m-q)\) and \(g_q=q(q^2-1)\). For each integer \(k\ge1\), the number of ordered \(m\)-tuples that generate the *whole* unital algebra \(A^k\) is
\[
\boxed{\prod_{j=0}^{k-1}(G_{q,m}-jg_q)}
\]
when \(k\le G_{q,m}/g_q\), and is zero otherwise. In particular, the sharp two-generator threshold is
\[
\boxed{d\bigl(M_2(\mathbb F_q)^k\bigr)\le2\ \Longleftrightarrow\ k\le q^4(q-1).}
\]
Here \(d\) is the minimum cardinality of a unital algebra generating set; for positive \(k\) it cannot be one because every one-generated unital associative algebra is commutative, whereas \(A^k\) is noncommutative.

## Assumptions and scope
The base field is \(\mathbb F_q\), including \(q=2\) and extension fields. All algebras and all generation are **unital and over the given base field**. Matrix trace is the ordinary trace \(a+d\) of a two-by-two matrix, with no rescaling. The prescribed trace vector ranges over all \(q^m\) vectors. Elements of the direct product are arbitrary tuples of matrices with coordinatewise operations; \(k\) is any positive integer. No restriction to invertible or to traceless matrices is imposed.

## Proof
**Step 1: all obstructions to generation.** A tuple fails to generate \(A\) exactly when it lies in some proper unital \(\mathbb F_q\)-subalgebra. Every proper unital subalgebra is contained either in the stabilizer \(B_\ell\) of an \(\mathbb F_q\)-rational line \(\ell\le\mathbb F_q^2\), or in an embedded quadratic field \(E\cong\mathbb F_{q^2}\). To justify completeness, take a maximal proper subalgebra \(S\). If it acts reducibly, it stabilizes a rational line. If irreducibly, its radical acts trivially on the faithful simple natural module, so the radical is zero. A faithful irreducible semisimple algebra acting on a two-dimensional \(\mathbb F_q\)-space is either the full matrix algebra or a quadratic field (the scalar algebra acts reducibly). The full case is excluded.

There are \(b=q+1\) distinct line-stabilizing algebras. There are \(e=q(q-1)/2\) embedded quadratic fields: the conjugation stabilizer of a fixed copy of \(\mathbb F_{q^2}\) has size \(2(q^2-1)\), so the number is \(\lvert\operatorname{GL}_2(\mathbb F_q)\rvert/[2(q^2-1)]\). Any two distinct line stabilizers meet in a split diagonal algebra of dimension two, and any three meet in the scalar matrices \(\mathbb F_q I\). Any two different embedded quadratic fields intersect only in scalars; moreover a nonscalar element of such a field has irreducible quadratic minimal polynomial, so lies in no rational-line stabilizer.

**Step 2: count with a trace prescription.** Fix any \(\boldsymbol\tau\). In the full algebra there are exactly \(q^{3m}\) tuples with this trace vector. In any single \(B_\ell\), the number is \(q^{2m}\), and in the intersection of any two distinct \(B_\ell\) it is \(q^m\), because the trace maps on these three- and two-dimensional vector spaces are surjective. In each embedded quadratic field \(E\), ordinary matrix trace is the separable field trace \(\operatorname{Tr}_{\mathbb F_{q^2}/\mathbb F_q}\), so its fixed-vector fiber has size \(q^m\) in *every* characteristic.

Let \(s(\boldsymbol\tau)\) be the number of scalar tuples having the prescribed trace vector. For odd characteristic it is \(1\). For characteristic two it is \(q^m\) if all entries of \(\boldsymbol\tau\) vanish and \(0\) otherwise. Inclusion-exclusion for the \(b\) Borels yields
\[
\left|\bigcup_\ell B_\ell^m\right|_{\boldsymbol\tau}=
 bq^{2m}-{b\choose2}q^m+\left(1-b+{b\choose2}\right)s(\boldsymbol\tau).
\]
The portions of the quadratic-field tuples outside the Borel union are disjoint and contribute \(e(q^m-s(\boldsymbol\tau))\). As \({b\choose2}-e=q\) and \(1-b+{b\choose2}-e=0\), the scalar-dependent term cancels *exactly*. The total nongenerating fixed-trace count is
\[
(q+1)q^{2m}-q^{m+1}.
\]
Subtracting from \(q^{3m}\) proves
\[
N_{q,m}(\boldsymbol\tau)
=q^{3m}-(q+1)q^{2m}+q^{m+1}
=q^m(q^m-1)(q^m-q).
\]
There is no division by two in the trace argument; the proof covers characteristic two.

**Step 3: count direct-product generators.** Summing the fixed-trace count over all \(q^m\) vectors gives \(G_{q,m}\). Every \(\mathbb F_q\)-algebra automorphism of \(A\) is inner, so its automorphism group is \(\operatorname{PGL}_2(\mathbb F_q)\) of order \(g_q=q(q^2-1)\). This group acts freely on the generating \(m\)-tuples, as an automorphism fixing generators fixes every matrix. Hence exactly \(G_{q,m}/g_q\) automorphism-orbits of generating tuples exist.

An \(m\)-tuple in \(A^k\) generates all of \(A^k\) exactly when every coordinate projection generates \(A\) and the associated generating tuples lie in **distinct** automorphism-orbits. Indeed, every proper subdirect product of finite simple unital algebras has two coordinates identified through an algebra isomorphism: for two factors this is the simple-ring Goursat dichotomy, and induction on factors yields the general assertion. Conversely, pairwise nonisomorphic simple-coordinate quotients force the subdirect algebra to be the whole product. Ordering \(k\) distinct orbits and choosing one of \(g_q\) representatives in each gives the stated product. At \(m=2\), the number of orbits simplifies to \(q^4(q-1)\), proving the sharp threshold.

## Verification
The included standalone `verify.py` uses exact arithmetic in \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\). It exhaustively enumerates each prescribed trace pair of \(2\times2\) matrices over these fields and each trace triple over \(\mathbb F_2\). Generation is checked independently by closing the vector space of words under right multiplication until stabilization. The program checks all \(256\), \(6561\), and \(65536\) ordered pairs and \(4096\) ordered triples, respectively. It reports `VERIFY_OK_TRACE_GENERATION` when all fiber multiplicities and global totals agree.

## Relationship to prior work
Florentino (2008) studies simultaneous similarity, triangularizability and trace invariants of two-by-two matrix tuples; these structural results do not count the finite-field generating tuples with every prescribed trace vector. Quick and Ruškuc (2010) analyze the growth of generating sets of direct powers; the logarithmic growth result is broader structurally but does not supply the trace-fiber law or the explicit two-generator cutoff in this form. Reineke (2025, especially Example 4.6) *already gives* the polynomial for unconditioned absolutely irreducible two-dimensional free-algebra representations. Thus the unconditioned generator count, and the resulting orbit-based direct-power corollary, are **not claimed to be new in isolation**. In odd characteristic, the fixed-trace count is already an elementary corollary of the unconditioned count by the independent scalar shifts \(X_i\mapsto X_i+\lambda_i I\): each trace changes by \(2\lambda_i\), so those fibers are bijective. **The substantive new component is the characteristic-two fixed-trace equidistribution**, which such scalar shifts cannot establish, together with its uniform all-characteristic explanation. The direct-power threshold is a contextual corollary, not separately claimed new. No assertion of absolute bibliographic uniqueness is made.

## Limitations
This proof concerns two-by-two *full* matrix algebras over finite fields, not higher matrix sizes or arbitrary rings. The proof of the direct-power formula uses unital homomorphisms and simple-algebra structure. The numerical checks cover finitely many fields and tuple lengths; only the algebraic counting proof justifies the universal quantifiers. The trace-conditioned result has not received independent mathematical audit; an equivalent formula might occur in prior finite-field representation or character-variety literature not discovered in the comparisons.

## References
1. C. A. A. Florentino, “Simultaneous similarity and triangularization of sets of 2 by 2 matrices,” arXiv:0809.3032 (first submitted 2008-09-17), *Linear Algebra and its Applications* 431 (2009), 1652–1674, DOI: 10.1016/j.laa.2009.05.037.
2. M. Quick and N. Ruškuc, “Growth of generating sets for direct powers of classical algebraic structures,” *Journal of the Australian Mathematical Society* 89 (2010), 105–126, DOI: 10.1017/S1446788710001473, online 2010-09-21.
3. M. Reineke, “Counting generating spaces of matrices,” arXiv:2510.06959 (first submitted 2025-10-08), especially Example 4.6 and Lemma 3.1.
