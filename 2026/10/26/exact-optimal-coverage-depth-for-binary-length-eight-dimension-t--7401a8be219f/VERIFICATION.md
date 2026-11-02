---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The rank-three failure event is the union over the seven Fano projective lines: with P(T>t)=Σ_L p_L^t−2Σ_P p_P^t for t≥1 (distinct lines meet in one point and each point is on exactly three lines). Summing tail gives 1+Σ_L p_L/(1−p_L)−2Σ_P p_P/(1−p_P). Zero-column replacement weakly improves each sample outcome and is harmless for finding a minimizer. Every no-zero 3×8 generator is encoded by exactly one of 3003 multiplicity compositions (up to column permutation); rank is checked by exclusion from all seven projective lines. Independent exact arithmetic enumerated 2702 full-rank profiles; seven minimizers with multiplicities 2,1,1,1,1,1,1 and value 422/105; runner-up 88/21 in 21 profiles. Independent absorbing-Markov recursion independently gave 422/105 for the minimizing profile. The finite census exhausts this exact finite problem, not arbitrary n or q.

## originality

PASS

No found prior statement identifies the first length above binary [7,3] simplex where projective multiplicities cannot be uniform. The objective and Fano inclusion–exclusion are not themselves new; the exact first nonuniform rank-three integer optimization and minimizer classification appear distinct under the inspected sources. Historical priority remains qualified.

## value

PASS

The first non-simplex length n=8 at rank 3 is a naturally motivated integer-design optimization for uniform random-access recovery, with a sharp time penalty of 43/420 relative to length-seven simplex and a complete characterization of optimal redundancy placement. This is an exact natural cutoff, not a claim about all code lengths.

The dated certificate retains the supplied scientific assessment, sources and limitations.
