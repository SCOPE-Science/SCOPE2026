# A sharp period-minus-one cutoff for symmetric semilattice-relevance semantics

## Finding

Let \(S=\mathcal P_{\mathrm{fin}}(\mathbb N)\), with the operation of set union and unit \(\varnothing\). For integers \(k\ge0\) and \(m\ge1\), define the cardinality signature of a finite set \(X\) by
\[
\pi_{k,m}(X)=
\begin{cases}
s_{|X|},&|X|<k,\\
t_{|X|\bmod m},&|X|\ge k.
\end{cases}
\]
The distinct symbols \(s_0,\ldots,s_{k-1},t_0,\ldots,t_{m-1}\) form a set \(Q_{k,m}\) of exactly \(k+m\) states. A valuation is *signature-invariant* when each propositional letter holds on a union of fibers of \(\pi_{k,m}\).

**Theorem.** The following are equivalent:

1. Every formula of the positive relevant language \(\{\wedge,\vee,\to\}\), under every signature-invariant valuation, has a truth set that is a union of the signature fibers.
2. The map \(\pi_{k,m}\) is a surjective ternary bounded morphism onto the finite structure obtained by existentially projecting the union relation.
3. \(m=1\) or \(k\ge m-1\).

Whenever these conditions hold, \(Q_{k,m}\) is an exact finite semantics for arbitrarily nested formulas, including truth at the empty set. When they fail, two atomic predicates and one occurrence of relevant implication distinguish equal-signature finite sets. In particular, every finite family of ultimately periodic, cardinality-invariant atomic truth sets admits a common effective finite semantic quotient.

## Assumptions and scope

The ground set \(\mathbb N\) is infinite. Formulas are generated from propositional letters using conjunction, disjunction, and relevant implication; no negation, fusion, or additional connectives are asserted here. At a finite set \(X\), the semantic clauses are classical pointwise clauses for conjunction and disjunction, and
\[
X\vDash\varphi\to\psi\quad\Longleftrightarrow\quad
\forall Y\in S\; (Y\vDash\varphi\ \Longrightarrow\ X\cup Y\vDash\psi).
\]
Atomic valuations need not be upward-closed under inclusion. A ternary *bounded morphism* \(f:(S,R)\to(Q,T)\) means that \(f\) is surjective and satisfies the following two properties for \(R(X,Y,Z)\iff Z=X\cup Y\): (forth) \(R(X,Y,Z)\) implies \(T(fX,fY,fZ)\); and (back) for any \(X\) and \(T(fX,b,c)\), there exist \(Y,Z\) with \(fY=b\), \(fZ=c\), and \(Z=X\cup Y\). We take \(f(\varnothing)\) as the designated state in the quotient.

## Proof

**Interval lemma.** Fix finite \(X\) of size \(a\) and an integer \(b\ge0\). As \(Y\) ranges over all \(b\)-element finite subsets of the infinite ground set, the cardinalities of \(X\cup Y\) are exactly the integers
\[
\max(a,b)\le c\le a+b.
\]
For each such \(c\), choose \(a+b-c\) of the elements of \(Y\) inside \(X\) and the remaining elements outside \(X\). This is possible because \(0\le a+b-c\le\min(a,b)\) and the complement of \(X\) is infinite.

**Finite ternary frame.** Suppose \(m=1\) or \(k\ge m-1\). The following rules define a ternary relation \(T\) on \(Q_{k,m}\). Indices on tail symbols are understood modulo \(m\):

* \(T(s_a,s_b,q)\) holds precisely if \(q=\pi_{k,m}(Z)\) for some integer size \(|Z|=c\) with \(\max(a,b)\le c\le a+b\).
* \(T(s_a,t_r,t_u)\) holds precisely when \(u\equiv r+j\pmod m\) for some \(0\le j\le a\).
* \(T(t_r,s_b,t_u)\) holds precisely when \(u\equiv r+j\pmod m\) for some \(0\le j\le b\).
* \(T(t_r,t_s,t_u)\) holds for every tail symbol \(t_u\), and there are no other triples.

The interval lemma proves forth immediately. For back, fix \(X\) with a given signature. With two small states, the interval lemma realizes exactly the first row. With a small state and a tail state, choose a sufficiently large representative of the specified tail residue; its size exceeds the small size, so the interval lemma gives precisely the listed modular increments. With two tail states, \(|X|\ge k\ge m-1\) (or \(m=1\)); choose the size of \(Y\) sufficiently large with the required residue. Varying the number of new elements from \(Y\) relative to \(X\) over an interval of at least \(m\) consecutive integers realizes every output residue. All resulting unions have size at least \(k\). Thus back holds at **each fixed** \(X\), not merely for some representative of its signature.

An induction on formulas now gives \(X\vDash\theta\) if and only if \(\pi_{k,m}(X)\vDash\theta\), with the projected atomic valuation on the finite frame. The induction step for implication uses both forth and back, in the indicated quantifier order. This proves that condition 3 implies conditions 2 and 1, including arbitrary nesting and the empty-set distinguished point.

**Sharp obstruction.** Suppose \(m>1\) and \(k<m-1\). Choose \(X,X'\) with sizes \(k\) and \(k+m\), respectively. Both have tail residue \(r\equiv k\pmod m\), hence identical signatures. Let atomic \(p\) be true precisely on tail class \(t_r\), and let atomic \(q\) be false precisely on tail class \(t_{r+k+1}\) and true elsewhere. For every \(Y\vDash p\), the increment from \(|Y|\) to \(|X\cup Y|\) is between \(0\) and \(k\). Because \(0,1,\ldots,k+1\) are distinct modulo \(m\), no such union has the prohibited residue. Therefore \(X\vDash p\to q\).

On the other hand, take \(Y\) of size \(k+m\) and choose exactly \(m-1\) elements of \(Y\) inside \(X'\), with all other elements outside. This is feasible, and \(|X'\cup Y|=|Y|+k+1\). Hence \(Y\vDash p\) but \(X'\cup Y\nvDash q\), proving \(X'\nvDash p\to q\). Thus condition 1 fails. Since a bounded morphism would preserve all projected atomic formulas, condition 2 fails as well.

**Effective periodic consequence.** Suppose each atomic truth set is invariant under permutations of \(\mathbb N\), and its set of permitted cardinalities is ultimately periodic. For the finitely many atoms appearing in a formula, compute a common period \(m\) (for example their least common multiple) and a common preperiod \(k_0\). Setting \(k=\max(k_0,m-1)\), the theorem yields an exact quotient with \(k+m\) states. For a fixed signature scheme and \(v\) propositional letters, validity under all signature-invariant valuations can be decided by enumerating the \(2^{v(k+m)}\) atomic assignments to the quotient and evaluating implication directly on its finite ternary relation.

## Verification

The independent arithmetic-and-set checker `verify_cardinality.py` reproduces the interval lemma for all subsets of universes of sizes \(1\) through \(7\), compares finite representatives' reachable signature pairs for \(0\le k\le7\), \(1\le m\le7\), checks the finite relation in all positive cases, and tests explicit depth-one counterexamples in all negative cases. Its completed output is `CARDINALITY_QUOTIENT_VERIFY_OK 2737`. These tests are finite corroboration; the unrestricted assertion is proved by the interval lemma and the case analysis above, not by extrapolation.

## Relationship to prior work

The distinct 2025 source motivating this question is Knudstorp's *Diamonds and Dominoes* (arXiv:2506.16366, originally posted 19 June 2025). It places undecidability at the center of the associative modal logic of the union frame \((\mathcal P(\mathbb N),\cup)\), and its Appendix A contrasts unrestricted valuations with a decidable class of restricted valuations and their morphic reduction. This motivates asking whether the shared finite-subset union operation admits a comparably transparent *symmetric observation* quotient for the residual relevant implication, which has different universal rather than existential semantics. The present result proves an exact necessary-and-sufficient criterion for this question, not a decidability theorem for the 2025 modal language.

Knudstorp's separate 2024 LICS conference work *Relevant S is Undecidable* (first public 8 July 2024) introduced the relevant union semantics and used even/odd and mod-four labels in a tiling encoding; it did **not** establish closure of globally cardinality-invariant exact-prefix/modular-tail observations under arbitrary nested implication. The expanded 2026 account *Undecidability in Relevant Logic* (an expansion of that 2024 work, **not** a new first-public source for the 2024 theorem) defines ternary p-morphisms and constructs an infinite two-coordinate cardinality p-morphism (Definitions 2.8 and 5.2 and Lemma 5.4). Its infinite-coordinate construction does not establish the sharp finite periodic-tail cutoff here. Kashima's semilattice proof-theoretic work likewise gives the semantics but not the present characterization in the inspected portions.

## Limitations

The decidability claim concerns bounded or individually specified ultimately periodic **cardinality-invariant** atomic valuations; it does not decide validity of the full semilattice relevant logic under arbitrary valuations. The finite frame is a ternary relational p-morphic image, generally **not** a semilattice homomorphic quotient: the cardinality of a union depends on overlap, not just on the two separate cardinalities. No claim is made that \(k+m\) is the smallest possible quotient for each particular atomic valuation. Priority in unindexed literature is not completely excluded.

## References

1. S. Brinck Knudstorp, *Diamonds and Dominoes: Impossibility Results for Associative Modal Logics*, arXiv:2506.16366, first public submission 19 June 2025, https://arxiv.org/abs/2506.16366 ; especially §§1–3 and Appendix A. The accessible PDF displays a later revision dated September 2026; this is not its first-public date.
2. S. Brinck Knudstorp, *Relevant S is Undecidable*, LICS 2024, DOI:10.1145/3661814.3662128, publicly released 8 July 2024, lawful OA https://pure.uva.nl/ws/files/232537714/3661814.3662128.pdf ; especially §§2–4.
3. S. Brinck Knudstorp, *Undecidability in Relevant Logic*, arXiv:2605.29880, submitted 28 May 2026, https://arxiv.org/abs/2605.29880 ; an expanded version of the 2024 work, particularly §§2.2 and 5.2.
4. R. Kashima, *Proof Theoretical Studies on Semilattice Relevant Logics*, Research Reports on Mathematical and Computing Sciences C-157 (2001), https://www.is.c.titech.ac.jp/users/kashima/pub/C-157.pdf ; introduction and semantic preliminaries.
5. Y. Weiss, *A Characteristic Frame for Positive Intuitionistic and Relevance Logic*, *Studia Logica* 109 (2021), 687–699, DOI:10.1007/s11225-020-09921-2 (bibliographic and abstract-level comparison).
