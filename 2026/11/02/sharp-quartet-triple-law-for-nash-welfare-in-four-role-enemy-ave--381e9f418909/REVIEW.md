# Scientific review

## Correctness — PASS

The exact claim uses four role classes, symmetric valuations \(+1\) across classes and \(-n\) within classes, individual rationality, and the geometric-mean Nash objective. A group containing an enemy cannot be individually rational; a transversal clique of size \(s\) contributes \((s-1)^s\) to the product. The Gale–Ryser row inequalities reduce realizability of a proposed \((p,t,q)\) spectrum to \(q\le d\), \(t+2q\le n-2a\) and the size equation. The strict quartet-increasing transformations preserve those inequalities and increase the product by factors \(81/64\) or \(81\). Largest feasible triple count then uniquely selects the optimal spectrum. The polynomial-coefficient argument independently counts every labeled partition of that spectrum. Exact arithmetic tests in `verify.py` corroborated each component; they do not substitute for the universal proof. Zero-optimum instances are excluded from the count assertion.

## Originality — PASS, qualified

The primary study of Nash welfare in additive hedonic games, arXiv:2605.19030v1, defines this objective and its enemy-averse clique constraint and already contrasts two triples with a quartet and a pair. This new claim does not present those components as novel. Inspection of the source's definition, enemy-averse results and appendix found no exact four-partite role-class formula or tied-optimizer enumeration. The older arXiv:2503.06017v1 concerns a utilitarian objective and probabilistic multipartite constructions; it does not cover the deterministic geometric-mean claim. An existing exact analysis for three roles covers the \(d=0\) boundary, not the first nontrivial four-positive-role case. Comparable work that is unindexed or inaccessible remains a priority risk, so this is not a claim of exhaustive novelty certification.

## Mathematical value — PASS

The first additional role beyond tripartite friendship introduces four-agent coalitions and a nontrivial exchange \(81>64\) between one quartet plus one pair and two triples. The result resolves the exact welfare maximum, feasible positive-welfare boundary, complete structural shape of all optimizers, and their labeled count for an infinite natural graph family. In particular, the profile \((5,4,4,1)\) has welfare-product optimum \(5184\), defeating the no-quartet value \(4096\), and has \(34560\) distinct labeled optimal partitions. A coefficient dynamic program makes uniform optimal tie-breaking possible by standard exact-count backtracking. The proof is specific to the four-role family and does not yield a general-graph algorithm.

Self-review: passed. Independent audit: not yet performed.
