# Independent mathematical audit — SCOPE-20260921-72e2e9305815

Final disposition: **PASS**.

## Correctness
**PASS** — For the explicit polynomial family, \(g'(z)=zh'(z)\), so the dilatation is \(\omega(z)=z\) and the Jacobian is positive in the disk because \(Na<1\). The identity \(zh'(z)/h(z)-\beta=(1-\beta)(1-w)/(1-aw)\), with \(w=z^{N-1}\), proves starlikeness of exact order \(\beta\). For \(H=h-g\), the boundary expansion at 1 and the implicit-function theorem give a nonreal level branch \(H(z)\in\mathbb R\) inside the disk when \(N>3\beta/[2(1-\beta)]\); conjugate points on that branch have the same harmonic image. Independent symbolic checking reproduced the constants \(A\), \(B\), and \(c=N(1-\beta)/(3\beta)>1/2\), and the repository verifier was inspected as supplementary evidence.

## Originality
**PASS** — Zhu and Huang's complete 2015 open article was inspected and Remark 18 explicitly states that the sharp starlike-order threshold for univalence of locally univalent sense-preserving harmonic maps is open. Earlier Hotta-Michalski work treats starlike analytic parts without resolving the threshold. The potentially overlapping Yavuz Janowski-starlike paper was also checked: its class is defined inside harmonic univalent functions and its results give coefficient/distortion-type sufficient subclass information rather than a universal implication from starlike order. Targeted searches found no prior family producing nonunivalence at every order below one. Originality therefore passes to the best of current knowledge.

### Equivalent formulations
The comparison includes standard starlike-order, Janowski-starlike, and locally-univalent harmonic formulations.

### Broader coverage
The inspected literature supplies special cases and sufficient subclasses, not the all-orders counterfamily.

### Exact database or table
The decisive evidence is the explicit open problem and direct comparison with the closest cited literature.

### Claim versus prior implication
The assigned family supplies a genuinely stronger counterexample continuum.

## Value
**PASS** — The theorem gives a negative resolution of an explicit threshold problem: no nondegenerate starlike order below one can by itself force harmonic univalence. The exact-order polynomial family and boundary-fold mechanism provide a structural counterexample scheme rather than an isolated example.

## Source inspections
- **The Distortion Theorems for Harmonic Mappings with Analytic Parts Convex or Starlike Functions of Order beta** (https://doi.org/10.1155/2015/460191): complete open primary article, including definitions, main estimates, and Remark 18 Method: primary full-text inspection. Assessment: PRIMARY_SOURCE_STATES_OPEN_PROBLEM. Evidence: Remark 18 explicitly says the univalence problem is open and the sharp beta is unknown.
- **Harmonic univalent functions with Janowski starlike analytic part** (https://openaccess.iku.edu.tr/entities/publication/8c18390e-307d-40dc-9fc3-29365e174a3a): complete eight-page primary paper inspected through its class definitions and main coefficient/distortion results Method: primary full-text inspection. Assessment: RESTRICTED_UNIVALENT_SUBCLASS_NOT_COVERING. Evidence: The paper studies harmonic univalent functions whose analytic part satisfies a Janowski condition; it does not prove that starlike order alone forces univalence or give the assigned all-orders counterfamily.

## Residual risks
- Differently parameterized harmonic-mapping literature may contain an equivalent family that was not indexed by the searched terminology.
- The theorem rules out criteria based only on starlike order; additional dilatation or geometric hypotheses may restore univalence.
