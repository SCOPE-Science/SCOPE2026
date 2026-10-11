---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The assigned exact formulas express \(p'-q'\) as a positive-denominator multiple of a quartic \(P_4\) and \(p'+q'\) as a positive-denominator multiple of a sextic \(P_6\), with the displayed overall signs. The inspected verifier reconstructs the rational functions from the source coefficients and proves both factorizations symbolically. Exact Sturm counts give zero roots of \(P_4\) and one root of \(P_6\) in \((-1,1)\); exact rational evaluations at the two decimal endpoints bracket the sextic root. Since \(P_4(0)<0\) and \(P_6(0)<0\), the factor signs yield exactly the stated Jacobian partition. An independent replay of the symbolic factorization and Sturm counts agreed with the package certificate.

## originality

PASS

The accessible primary record for Wang--Zhong states only that the new bounded convex harmonic self-convolution counterexample has a vanishing Jacobian at some interior point. The assigned exact analysis strengthens this to a complete real-diameter root count and sign partition using a new Sturm certificate. Resultary and targeted source searches returned no prior statement of the unique root or the quoted bracket. Because the full very recent preprint could not be securely inspected in this bounded run, the possibility of an unobserved in-paper remark is retained explicitly as a residual risk rather than being treated as negative evidence.

## value

PASS

The source is a new counterexample to a longstanding harmonic-convolution problem. Determining that its real diameter has one and only one fold, together with the exact orientation-reversing interval, is a natural geometric refinement of the mechanism by which the counterexample fails local univalence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
