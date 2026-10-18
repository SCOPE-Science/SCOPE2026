# Exact optimal satisfiability gaps for finite Boolean Ockham automorphisms

## Finding

Let \(E:t(x_1,\ldots,x_k)=u(x_1,\ldots,x_k)\) be any equation in the bounded-distributive-lattice language \(\{\wedge,\vee,\sim,0,1\}\), with \(k\geq1\). Let \(d\) be the largest number of nested occurrences of \(\sim\) in either term, \(D=d+1\), and \(q=2^k\). Consider **only** finite nontrivial Boolean lattices equipped with a **bijective dual lattice automorphism** \(\sim\) (a Boolean-type Ockham algebra; this is not the class of all Ockham algebras).

There is an explicitly constructible nonnegative integral \(q^d\)-square transfer matrix \(T_E\) (one-by-one when \(d=0\)) such that if the underlying atom permutation has \(m_\ell\) cycles of length \(\ell\), then
\[
 \operatorname{ds}(E)=\prod_{\ell\geq1}\left(\frac{\operatorname{tr}(T_E^{\ell})}{q^{\ell}}\right)^{m_\ell}.
\]
The product has finitely many nonunit exponents. The equality \(\operatorname{ds}(E)=1\) holds for all these algebras **if and only if** it holds in the single Boolean Ockham algebra induced by one cyclic permutation on \(D\) atoms. Otherwise there is an **effectively computable, attained, optimal finite satisfiability gap**: a rational number \(\gamma(E)>0\) such that every such algebra has satisfaction degree either \(1\) or at most \(1-\gamma(E)\), and some algebra attains equality. Moreover \(\gamma(E)\geq q^{-D}\), and an extremizer can always be chosen with a single atom cycle.

For the family \(E_a:\sim^{a}x=x\) with even integer \(a\ge2\) (superscripts denote repeated unary application), its sharp gap is explicitly
\[
 \gamma(E_a)=1-2^{-\mu(a)},\qquad
 \mu(a)=\min_{p\text{ prime}}p^{v_p(a)}(p-1).
\]
For example \(\gamma(E_2)=3/4\) and \(\gamma(E_{12})=15/16\). The minimum is a finite, effective computation: any prime \(p\) with \(p-1\) exceeding the current best candidate may be omitted.

## Assumptions and scope

The underlying Boolean lattice is \(\mathcal P(X)\) for a **nonempty finite** set \(X\). Every bijective dual endomorphism has the form
\[
 \sim A=\{v\in X:\sigma(v)\notin A\}
\]
for a permutation \(\sigma:X\to X\). The variables independently range uniformly over \(\mathcal P(X)\). All assertions concern equations, not arbitrary first-order formulas, and the signature contains only the indicated operations. The Boolean complement is used in representing \(\sim\), but is **not** a primitive operation of the equation language. The automorphism restriction is essential to the cycle decomposition.

Write \(\mathcal A=\{0,1\}^k\). At a position \(v\) record the \(k\)-bit vector of the memberships of \(v\) in the \(k\) variable subsets. Inductively, evaluation of a term at \(v\) depends only on the vectors at \(v,\sigma(v),\ldots,\sigma^d(v)\). Negation of a subterm at \(v\) is one minus that subterm's value at \(\sigma(v)\). Consequently the equation determines an explicit allowed-block predicate \(F_E\subseteq\mathcal A^D\), and a word is satisfying on a permutation cycle exactly when all cyclic length-\(D\) blocks lie in \(F_E\).

## Proof

**Transfer matrix.** For \(d\ge1\), index the vertices of the order-\(d\) de Bruijn graph by words in \(\mathcal A^d\). Place one directed edge from \((a_0,\ldots,a_{d-1})\) to \((a_1,\ldots,a_d)\) exactly when \((a_0,\ldots,a_d)\in F_E\). Define \(T_E\) as its adjacency matrix. For \(d=0\), take the scalar \(T_E=|F_E|\). A closed walk of length \(\ell\), with a distinguished starting time, is in bijection with a cyclically indexed \(\ell\)-word whose every length-\(D\) cyclic block is allowed, **including** the case \(\ell<D\) where indices repeat. Thus its count is \(\operatorname{tr}(T_E^\ell)\). Different permutation cycles use disjoint atom coordinates, proving the product formula.

**One-cycle universal test.** If every possible length-\(D\) block belongs to \(F_E\), the equation is universally true. If a block is forbidden, place its \(D\) symbols around a \(D\)-cycle; the equation fails at the first position. Hence validity on that single \(D\)-cycle is equivalent to the full-block predicate. This does **not** assert that the test length is minimal for every equation.

**Uniform positive gap and a decay bound.** Suppose \(F_E\ne\mathcal A^D\). In any permutation algebra where the equation fails on at least one assignment, fixing the at most \(D\) atom symbols around one violating coordinate enforces failure. Its probability is at least \(q^{-D}\); hence the satisfaction degree is at most \(1-q^{-D}\). On a cycle of length \(\ell\ge D\), take \(\lfloor\ell/D\rfloor\) disjoint length-\(D\) windows. They are independent under uniform input, and each is forbidden with probability at least \(q^{-D}\). Therefore, writing \(s_\ell=\operatorname{tr}(T_E^\ell)/q^\ell\),
\[
 s_\ell\le(1-q^{-D})^{\lfloor\ell/D\rfloor}.
\]
In particular \(s_\ell<1\) for \(\ell\ge D\) and \(s_\ell\to0\) exponentially as \(\ell\to\infty\).

**Optimal-gap algorithm.** If the transfer digraph has no directed cycle (equivalently, \(\operatorname{tr}(T_E^\ell)=0\) for all positive \(\ell\)), every satisfaction degree on a nontrivial finite algebra is zero; output \(\gamma(E)=1\). Otherwise choose a directed cycle of length \(r\). Put \(L=r\lceil D/r\rceil\). Repetition of its word gives an allowed cyclic \(L\)-word, so \(s_L>0\), while \(L\ge D\) gives \(s_L<1\). Set \(b=s_L\). Select a positive integer \(K\) with \((1-q^{-D})^K<b\). Compute exactly all \(s_\ell\) for \(1\le\ell<DK\), omitting values equal to \(1\), and set \(M\) to their maximum. This is a finite nonempty set and \(M\ge b>0\). Every \(\ell\ge DK\) has \(s_\ell<b\le M\); therefore \(M=\max\{s_\ell:s_\ell<1,\ \ell\ge1\}\). For any nonvalid permutation algebra, at least one cycle has \(s_\ell<1\), and the product formula bounds its satisfaction degree by \(M\). A single cycle at an maximizing \(\ell\) attains \(M\). Thus \(\gamma(E)=1-M\). The algorithm is exact but may be extremely expensive; no polynomial-time complexity bound is asserted.

**Explicit even-iterate corollary.** On an \(\ell\)-cycle, \(\sim^{a}\) for even \(a\) acts by the atom permutation power \(\sigma^a\). Its fixed subsets have arbitrary membership constant on each of the \(\gcd(\ell,a)\) orbits, giving
\[
 s_\ell=2^{\gcd(\ell,a)-\ell}.
\]
The law is valid precisely when every atom-cycle length divides \(a\). For any \(\ell\nmid a\), choose a prime \(p\) whose valuation in \(\ell\) exceeds \(v_p(a)\). Then \(\gcd(\ell,a)\le\ell/p\), whence
\[
 \ell-\gcd(\ell,a)\ge\ell(1-1/p)\ge p^{v_p(a)}(p-1).
\]
Taking \(\ell=p^{v_p(a)+1}\) attains equality. Minimizing over primes proves the claimed sharp formula.

## Verification

The accompanying `code/verify.py` implements the semantics from subset masks independently of the local-block/transfer construction. It compares direct evaluation of equations on cyclic permutations with block enumeration and exact integer transfer-matrix traces. It then checks the multiplicative formula on every permutation of sets of size at most five for six equation templates, and checks the prime-power gap formula for the first forty positive even exponents. Run with `python3 code/verify.py` from the directory containing this document.

Expected terminating output:

```
VERIFY_OK equation_templates=10 independent_cycle_assignments=11588 full_transfer_matrix=YES
PERMUTATION_PRODUCT_OK models=918 size_at_most=5
ARITHMETIC_SHARP_GAP_OK even_iterates=2..80
```

These are finite cross-checks, **not** a computational proof for unbounded cycle lengths; the proof above establishes the general quantifiers.

## Relationship to prior work

Marcelino and Rivieccio (2021, arXiv:2102.05421), particularly Definition 2.3 and Section 5, study Ockham-algebra negation, bounded varieties, and finite axiomatizability. Their main results are proof-theoretic and do not provide equation-by-equation satisfaction-degree products or optimal numerical gaps for the finite Boolean automorphism subclass.

Bumpus and Kocsis (2021, arXiv:2110.11515), especially Definitions 1.1–1.2 and Proposition 1.14, establish the satisfiability-gap framework and the product rule for equations. They work with Heyting-algebra semantics, where negation is pseudocomplementation; that is **not** the dual automorphism in this statement.

The conversion from forbidden local blocks to a de Bruijn graph, as well as trace enumeration of periodic words, is standard finite-type symbolic dynamics (compare Sobottka, arXiv:2010.10595, Sections 2, 4, 5, whose subject is shift-space structure rather than Ockham satisfiability). No originality is attributed here to the underlying transfer-matrix technique. The specific conjunction of a one-cycle universal test, a **computable attained optimal equation-dependent gap** across all finite Boolean Ockham automorphisms, and the valuation formula for even negation iterates is the contribution assessed here.

## Limitations

The assertion does **not** cover nonbijective dual endomorphisms, non-Boolean Ockham lattices, arbitrary first-order formulas, or pseudocomplementation in Heyting algebras. The transfer graph may be exponentially large and the exact-gap cutoff enormous. A universal identity has no nonvalid algebra and therefore no positive-gap optimization instance. No independent human priority examination is claimed; an equivalent earlier treatment within periodic-point enumeration or algebraic logic remains possible.

## References

1. S. Marcelino and U. Rivieccio, *Finite axiomatizability of logics of distributive lattices with negation*, first public arXiv version 10 February 2021, arXiv:2102.05421, https://arxiv.org/abs/2102.05421 .
2. B. M. Bumpus and Z. A. Kocsis, *Degree of Satisfiability in Heyting Algebras*, first public arXiv version 21 October 2021, arXiv:2110.11515, https://arxiv.org/abs/2110.11515 .
3. M. Sobottka, *Some notes on the classification of shift spaces: Shifts of Finite Type; Sofic Shifts; and Finitely Defined Shifts*, first arXiv version 20 October 2020, arXiv:2010.10595, https://arxiv.org/abs/2010.10595 . Standard shift-space context only; later corrigendum exists and no corrected lemma is used.
