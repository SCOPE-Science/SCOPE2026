# Independent mathematical audit

## correctness

PASS

The move set T±,X,R,S has T+ raising petal count by 2 and T− lowering by 2. From nine petals to one, d−a=4, L=2a+4+p; externally established hardness implies a≥1, so any L≤7 path has exactly a=1,d=5,p≤1. Inspected all source of artifacts/verify_petal_distance.py (Git blob a29ab50e1f1fecfb0243b6df5fce6766a1bdfdc0), including exact cyclic representatives, all insertion/deletion/exchange cases, height rotation/halfturn symmetry, dynamic state recurrence, and both 8-step upper paths. Reimplemented move enumeration and path-transition checks in a separate local Python script; for EACH alpha and beta confirmed counts (one add=144, add+delete=1, add+exchange=6, add+two deletes=0, terminal (1,5,0)=0 and (1,5,1)=0) and validated the eight listed transitions. Giving R and S zero cost is a relaxation in the safe direction: any alleged ≤7 genuine path would appear in these exhaustive finite counter-patterns. Therefore exact distance 8, conditional on the accurately cited published knot-type/hardness facts.

## originality

PASS

Compared against Vernitski 2026 hard-petal paper, whose publicly accessible description and externally supplied upper sequences concern hardness/excess and do not establish geodesicity. The new result proves absence of every 7-move route in a relaxed move graph, which is a stronger metric assertion than the published eight-step upper path and minimum extra petal count. A complete full-text primary comparison was blocked, so exact shortest-move overlap remains a clearly stated bibliographic risk, not an automatic failure; no strong covering theorem was found.

## value

PASS

Shortest counted move distances are natural invariants of the Reidemeister-type graph and matter for understanding the minimal hard nine-petal unknot obstructions. Exact geodesicity of two named minimal difficult witnesses refines mere petal-excess classification; an exhaustive finite cutoff is genuinely mathematical even without computing all knot distances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
