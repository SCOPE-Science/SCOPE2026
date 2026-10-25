---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Confirmed exact positive Zumkeller summands, repetition permitted. Small Zumkeller 6,12,20 and 945 are verified from divisor equal-half subsets; no odd candidate <945 or between 945 and 971 meets necessary sigma(n)>=2n, by classification of odd prime-factor patterns. Using Somu-Kukla-Tran Proposition 4.6(a), every even N>=40 is a two-Zumkeller sum and 38 is not. Hence G_3=983=945+38 obstruction, while every N>=984 has a three-term sum. For k=4 even N>=980 are 6+6+two-sum, five consecutive odd numbers 981..989 have explicit four-term decompositions; 979 is obstructed. For any k>=4 odd obstruction T=6k+955 forces exactly one 945 and k-1 even terms with sum(y_i-6)=16, but y_i-6 is 0,6,14 only; impossible. Add 6 inductively to cover every integer above T. The finite verifier tests examples but does not prove the unbounded two-sum premise; that is explicitly imported from the published theorem.

## originality

PASS

No exact prior implication was located after source-specific comparison of definitions and named parameters; best-of-knowledge, with explicit residual risks. The searches and source inspections below are not a novelty certificate.

## value

PASS

Sharp eventual representation thresholds for every exact summand count k>=3 answer a natural additive-basis/Frobenius-type gap raised in the originating Zumkeller-sums paper, including a uniform obstruction and a nontrivial affine length law; not a table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
