# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The nilpotent decomposition was checked directly. If \(\pi\) is the set of prime divisors of \(k\), a finite nilpotent group splits as \(G=P\times H\) with \(P\) the Hall \(\pi\)-subgroup and \(H\) the Hall \(\pi'\)-subgroup. Every element of \(P\) is eventually sent to \(1\) by iterated \(k\)-th powers, whereas \(h\mapsto h^k\) is a permutation of \(H\).

For each cycle of that permutation, the vertices attached to every cycle vertex were explicitly identified with the same rooted tree \(T=D_k(P)\) after deleting the root loop. Writing \(A=\alpha(T-\{1\})\) and \(\varepsilon=\alpha(T)-A\), one has \(\varepsilon\in\{0,1\}\). A cycle of length \(r\) contributes exactly
\[
rA+\varepsilon\lfloor r/2\rfloor,
\]
including the loop case \(r=1\), where the root is forbidden. Summing gives the factorization theorem.

The coprime order-spectrum formula was checked from the exact cycle length of an element of order \(d\), namely \(\operatorname{ord}_d(k)\). The cyclic prime-power branch was checked separately by a bipartite matching argument on the level decomposition of \(D_p(C_{p^a})\). The two parity cases for the root contribution agree with the closed formula.

A standalone exact dynamic-programming verifier independently compared the cyclic prime formula with direct functional-graph optimization for 600 cases: \(p\in\{2,3,5,7,11\}\) and \(1\le n\le120\). All cases agreed, including \(s_2(C_{20})=12\), matching the example in the source paper. This computation is supporting evidence, not a substitute for the proof.

## Originality

PASS, to the best of our knowledge.

Blackburn--Hart--McVeagh, arXiv:2609.18513v1, was inspected for the definition of \(s_k(G)\), its functional-digraph interpretation, and its structural results on cycles and attached rooted trees. The paper studies groups for which \(s_k(G)\) is close to \(|G|\), and its displayed \(C_{20}\) example gives \(s_2(C_{20})=12\); no general exact nilpotent factorization or cyclic prime formula was located there.

Qureshi--Reis, arXiv:2107.00584v2, was inspected as prior art for the functional-graph decomposition of power maps on finite abelian groups. The 2026 paper of Fernandes--Qureshi--Reis--Ribas, arXiv:2609.20516, was also inspected as closely related work on invariants derived from power-map functional graphs. These structural and invariant frameworks are not claimed as new.

Two particularly relevant sources were not independently inspected in full. Fernandes--Reis, *Digraphs of power maps over finite nilpotent groups*, Discrete Mathematics 347 (2024), 114000, is the strongest residual prior-art risk for the nilpotent structural setting. McVeagh's 2026 thesis, *Square-free Sets in Groups and Groups with Many Roots*, is cited by Blackburn--Hart--McVeagh for \(k=2\) classification results and power-digraph symmetry and could contain an equivalent optimization formula. Bibliographic records and targeted searches did not provide concrete evidence that either source contains the present factorization or closed cyclic formula, but the uncertainty remains material.

The originality claim is therefore restricted to the exact independent-set factorization
\[
s_k(P\times H)=|H|A+\varepsilon s_k(H),
\]
the explicit coprime order-spectrum expression, and the closed formula for \(s_p(C_n)\), not to the underlying functional-graph structure.

## Value

PASS.

The result converts the newly emphasized extremal invariant \(s_k(G)\) into an exact computable expression on all finite nilpotent groups once the primary rooted-tree statistic is known. It applies equally to nonabelian nilpotent groups and separates the genuinely primary difficulty from a completely explicit coprime term.

For cyclic groups under prime powering, the remaining primary statistic is solved in closed form, giving \(s_p(C_n)\) for every \(n\). This both explains the \(C_{20}\) example in the source paper and provides a broad exact family beyond the near-\(|G|\) regime that motivates that paper.

## Limitations

For a general nonabelian primary factor \(P\), no closed formula for \(A=\alpha(T-\{1\})\) or \(\varepsilon\) is claimed. The result is an exact reduction rather than a complete group-theoretic evaluation of those two quantities.

The structural theory of power-map functional graphs is prior art. The two full texts identified above remain the principal originality uncertainty. No independent validation is asserted.
