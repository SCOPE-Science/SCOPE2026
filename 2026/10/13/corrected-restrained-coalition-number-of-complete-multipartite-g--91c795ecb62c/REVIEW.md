# Self-review

## Correctness
PASS. The restrained-dominating condition is reduced exactly to domination plus the requirement that the complement be empty or meet at least two partite classes. The three cases in the theorem are exhaustive. The maximal cases have explicit singleton partitions; the star case has only the whole vertex set as a restrained dominating set; and the unique-nonsingleton-part case with \(u\ge2\) has a matching \(u+2\) construction and upper bound via \(\operatorname{RDc}(G)\le C(G)\) and the direct computation \(C(G)=u+2\). Exhaustive labeled partition enumeration through order \(8\) agrees with the formula on all \(58\) profiles.

## Originality
PASS. The closest source is Proposition 2.17 of Nesam--Amutha--Anbazhagan (2025), which nominally states the stronger value \(\operatorname{RDc}(G)=|V(G)|\) for every complete multipartite graph. Taken with the standard convention \(n_i\ge1\), that statement is false: its own preceding star proposition conflicts with it, and the non-star graph \(K_{3,1,1}\) has value \(4\), not \(5\). The later Dobrynin--Glebov--Golmohammadi paper proves a general upper inequality and corrects cycles but does not give the multipartite boundary. Targeted literature-index and exact-web searches found no later corrected classification.

## Value
PASS. This is a natural complete classification on a canonical graph family for a recently introduced invariant. It does more than restate a counterexample: it identifies the exact structural boundary caused by having a unique non-singleton part and explains why the parameter drops. The result also resolves an overbroad published proposition without relying on computation for the infinite claim.

## Closest literature and limitations
The 2025 initiating paper is the decisive comparison because it explicitly claims a complete-multipartite formula. The present theorem agrees with that value on broad regimes but shows exactly where singleton partite classes invalidate it. The 2026 follow-up supplies the inequality used in one upper bound but no complete-multipartite theorem. A residual risk is that an erratum or poorly indexed later correction exists, or that some authors silently use a restricted convention excluding singleton partite classes.

Self-review: passed. Independent audit: not yet performed.
