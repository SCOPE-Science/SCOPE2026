# Independent mathematical audit — SCOPE-20260912-071

Disposition: **repaired**.

## Correctness
**PASS** — After correcting one terminology error, the operator-specific proof is sound. The rational Riccati obstruction follows from finite-pole residue 1 together with the infinity coefficient 2s(1+k). A rational symmetric-square solution cannot have finite poles because the third derivative has uniquely highest pole order, and no polynomial solution exists because the leading term is -(4d+8)c_d x to the power d+3. The Lax scalar equation has neither rational poles nor a polynomial solution, so the family is non-isomonodromic. Cassidy's Zariski-dense subgroup dichotomy then leaves the full differential-algebraic SL2. The stored phrase 'full constant SL2 with no dt-equations' was contradictory: the dt-constant subgroup would itself satisfy dt(g_ij)=0; that wording is repaired.

## Originality
**PASS** — Arreche gives the general PPV algorithm and Cassidy subgroup dichotomy, and the classical quartic-potential Galois exclusions are standard Kovacic-style consequences. Resultary and targeted literature searches did not locate a prior statement computing this exact t-parameter quartic oscillator's PPV group together with its rational Lax obstruction. The surviving contribution is the operator-specific exact hypothesis verification, not the general theory.

### Equivalent formulations
The final claim is equivalent to classical SL2 plus failure of the rational isomonodromy equation; the literature found supplied the framework but not this exact combined specialization.

### Broader coverage
Those results do not by themselves record the exact rational Lax obstruction for q=x⁴+t x²+1; the necessary specialization was independently checked.

### Exact database or table search
Database absence is only supporting evidence, not the novelty proof.

### Claim versus prior implication
Prior theory implies the final result only after the nontrivial operator-specific Riccati, symmetric-square and Lax calculations supplied here.

## Value
**PASS** — The quartic anharmonic oscillator is a standard natural family, and an exact PPV/non-isomonodromy classification is a reusable invariant rather than an arbitrary finite computation. The value lies in closing a concrete natural parameterized-Galois case; no paper-sized generalization is required.

## Source inspections
- **Arreche, Computing the differential Galois group of a one-parameter family of second order linear differential equations** (arXiv:1208.2226): full arXiv HTML introduction and subgroup-classification passages, including lines 54-85 and Cassidy theorem quoted at lines 124-132 Assessment: General PPV algorithms and the SL2 full-vs-constant dichotomy are prior; the exact quartic-oscillator Lax obstruction was not stated there. Evidence: The paper explicitly computes PPV groups for general second-order one-parameter equations and quotes that a Zariski-dense differential-algebraic subgroup of SL2 is either full SL2 or conjugate to constant SL2.
- **Resultary semantic search** (Resultary local research index): top semantic hits for quartic anharmonic oscillator PPV/non-isomonodromy Assessment: The direct hit was this record; nearby records concern different equations. Evidence: No earlier SCOPE hit with the same q=x⁴+t x²+1 PPV/Lax statement was returned.
- **Liouvillian solutions for second order linear differential equations with Laurent polynomial coefficient** (São Paulo J. Math. Sci., 2023, DOI 10.1007/s40863-023-00359-7): web full-text Kovacic-analysis section surfaced by search Assessment: Confirms broad classical Kovacic classifications for Laurent-polynomial coefficients but does not state the parameterized quartic Lax result. Evidence: The article classifies possible classical algebraic subgroups by pole orders and Kovacic cases.

## Residual risks
- The literature search cannot prove global novelty; exact originality is limited to the operator-specific specialization of general PPV theory.
- The repaired statement concerns transcendental t only; exceptional algebraic specializations are not classified.
