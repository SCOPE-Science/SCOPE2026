# Independent mathematical audit

## correctness

PASS

On a finite upset algebra a vertex belongs to U→V exactly when its entire upward cone misses U minus V. In this frame the negated biconditional thus has leaf trace D, the symmetric difference of the inputs' traces, and contains the root exactly when D is the whole maximal set. In particular the two distinct elements with full trace have apartness zero. For three traces, D_xy is contained in D_xz union D_zy, so failure is possible only when D_xy is full and neither right-hand difference is full. For complementary endpoint traces the right join contains the root exactly when z has one of those endpoint traces. Writing s=2^m, the s-2 ordered complementary pairs away from the empty/full pair have s-1 bad z choices apiece; the four lifts of the two empty/full ordered pairs have s-2 each. This gives (s-2)(s+3) failures among (s+1)^3 triples, including zero for m=1. Direct negation gives WEM exactly on the empty upset, the leaf-only full trace and the whole poset. The exact degrees give a positive failure fraction tending to zero for m≥2 and WEM success tending to zero. Independent replay using pointwise cone semantics rather than residuation verified the failure predicate and WEM success set on every assignment for m=1–7 (2,463,045 triples): python3 /workspace/reproductions/cotransitivity.py. The uploaded script was inspected, not run.

## originality

PASS

Pass the distinct three-variable cotransitivity count and the consequent exact no-gap/contrasting-limits example. The two a priori older ingredients—the qualitative equivalence of global validity to WEM and the Boolean-plus-new-top family—are credited. The exact WEM subcount is directly covered by a distinct same-day general record and is not credited as new. None of the checked sources states or gives the three-variable count without additional reasoning.

## value

PASS

The motivating qualitative equivalence raises a genuine stability question. The exact counterfamily shows that arbitrarily high cotransitivity satisfaction need not even weakly enforce frequent WEM, and explains the mismatch by the rarity of complementary input traces. It provides the first-order failure rate on a natural family already used for satisfiability-gap questions, rather than treating the known unary count or family as the advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
