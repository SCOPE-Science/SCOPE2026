---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Encoding each circular-ladder rung by a 2-bit mask yields a 16-state pair transfer T with triple-mask admissibility iff induced selected degree<=1, so D_n(z)=tr T(z)^n for n>=3. Independently rebuilt T and computed all 16 Newton characteristic coefficients at 33 integer z values 0..32, verifying det(I-uT)=Q(u,z) exactly: each coefficient has z degree <=32, hence equality at 33 points is an algebraically exhaustive polynomial identity. Log determinant gives full all-n rational generating formula and recurrence. A double-selected rung forces two adjacent empties, proving |S|<=n. At equality either every rung is singleton with cyclic binary layers avoiding constant triples (OEIS A007040) or even n alternates empty/double rung (two extra configurations). Hence max count L_n+3*1_{3|n}-1+2*1_{2|n}. Independent brute-force all subsets n=3..8 matched all coefficients and maxima.

## originality

PASS

OEIS A007040 explicitly supplies the cyclic singleton-word counts and maximal-independent-set prism interpretation (prior, not novel). This claim adds full dissociation polynomial for all prism sizes plus double/empty configurations and six-step rational characteristic identity. Published fan/windmill polynomial formulas concern different graph families. No identical full prism dissociation polynomial located, although a hidden earlier transfer enumeration remains a risk.

## value

PASS

Circular ladders are canonical 3-regular graph families. An exact polynomial classifies ALL dissociation-set sizes, not only a coefficient or extremal number, and a structural theorem identifies every maximum configuration and separates the two even-order patterns invisible to the known OEIS count. The all-n invariant is independently useful in extremal cubic-graph enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
