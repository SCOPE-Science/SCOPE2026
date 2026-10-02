# Independent audit — 2026-10-01

## Final claim

Sharp Y bound for the four-ring square confinement template

## Disposition

**Passed.** Correctness, originality, and value all pass for the final claim as stated in `RESULT.md`; no claim repair is required.

## Correctness

Writing \(S=b+c\) and \(C=1+1/\sqrt2\), the witness geometry gives \(a>1+S/2\), \(s>2S\), and \(s\ge C(a+1)\). The first two strict confinement margins plus \(p+q\ge s-S\) imply \(Q=8as+6Ss-5s^2-S^2>0\). On the admissible region with \(S\le Y<7/4\), \(Q\) decreases with \(s\); after setting \(s=C(a+1)\), it also decreases with \(a\). Hence \(0<Q< Q(1+S/2,S,C(2+S/2))=F(S)/8\le0\), a contradiction. Independent symbolic algebra verified this identity and the positive root \(Y=1.68448774587235\). The source's full square-limit note explicitly constructs the matching four-ring family with \(\rho\downarrow Y\), so the template infimum is sharp and unattained.

## Originality

Aguilar Martin's source proves the matching four-ring upper-bound family and explicitly says it does not prove \(Y\) is the global threshold or the infimum of the broader slipped/certifier families. The audited result adds a lower bound for a precisely defined canonical witness-and-quadrant-confinement branch, and the source family supplies sharpness inside that branch. No prior statement of this exact template infimum was located.

### Equivalent formulations

**Searches**
- Published-record semantic search: four ring square confinement template threshold greedy packing nested rings Y
- Source-repository search: Y 1.684487745872346; cuadrado_limite; lower bound; optimality

**Evidence**
- The source repository repeatedly records \(\tau_\square\le Y\) and explicitly says optimality is not proved; the only exact published-record match for the canonical lower bound was the audited record.

**Reasoning**

Searches included the equivalent language of slipped square families, quadrant confinement, four-ring witnesses, and the algebraic constant Y.

### Broader coverage

**Searches**
- Javier Aguilar Martin, arXiv:2609.15554
- Full source note docs/drafts/cuadrado_limite.md in the Calamares repository

**Evidence**
- The full source note constructs four-ring failures with \(\rho\downarrow Y\) and explicitly states that it does not prove Y is the global threshold nor the infimum of the whole slipped/Q-certified family.

**Reasoning**

The source gives the upper/sharpness half but not the audited lower bound for the canonical subclass.

### Exact database or table

**Searches**
- Source repository exact constant and rational witness table
- Published-record semantic search for the Y threshold

**Evidence**
- The source note tabulates three rational approximants approaching Y, but explicitly says the examples prove only finite upper bounds; no table supplies the canonical lower bound.

**Reasoning**

The audited lower bound is a geometric inequality, not a re-reading of the source witness table.

### Claim versus prior implication

**Searches**
- Direct comparison of source continuity family and quadrant-confinement conditions with the audited Q(a,S,s) monotonicity argument

**Evidence**
- The source family establishes existence of failures above Y. The audited proof derives necessary inequalities for every member of the canonical class and forces \(S>Y\).

**Reasoning**

An approximating upper-bound family cannot imply the universal lower bound for the class; that is the new implication.

### Source inspections

- **Una familia aproximante y una cota algebraica para el cuadrado** — UPPER_BOUND_AND_SHARPNESS_INPUT_NOT_LOWER_BOUND. Complete source note, including the balanced wall, perturbation family, witness execution, rational approximants, and explicit scope/optimality caveat. The note states \(1\le\tau_\square\le Y\), constructs \(\rho\downarrow Y\), and explicitly says it does not prove Y is the global threshold or the infimum of the broader family.

- **Greedy Packing of Nested Rings: The Golden Threshold, Placement Rules, and a Tribonacci Floor** — RELATED_NOT_COVERING_LOWER_BOUND. Current abstract/source summary describing the square upper bound and open optimality question. The inspected source materials present the Y construction as an upper bound, not the canonical-template lower theorem.

### Checked sources
- https://arxiv.org/abs/2609.15554
- https://github.com/JaviMaligno/calamares/blob/main/docs/drafts/cuadrado_limite.md
- Published-record semantic search

### Residual risks
- The source is recent and may receive rapid revisions; the claim is deliberately limited to the canonical template rather than global square optimality.

## Value

The canonical four-ring branch is the source architecture producing the best known square upper bound; proving its exact unattained infimum isolates a genuine structural boundary and shows that any global improvement below Y must leave this mechanism. That is a motivated boundary theorem, not an arbitrary parameter slice.

## Limitations

The sharp value is only for the explicitly defined canonical four-ring quadrant-confinement template, not the global square threshold or every slipped/confinement family. The primary source is very recent, so later revisions remain a residual originality risk.
