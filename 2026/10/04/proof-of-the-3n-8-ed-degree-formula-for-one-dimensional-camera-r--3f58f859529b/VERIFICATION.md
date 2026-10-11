---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The proof was independently reconstructed. Eliminating a and b by the two weighted normal equations gives a one-variable rational objective phi=N/D. Cauchy--Binet gives generic degrees deg N=deg D=2n-4, so the induced map P1 to P1 has total ramification 4n-10. On the rank-one locus a=bc, the first two normal equations force b to the sample mean and reduce the remaining condition to a degree n-2 polynomial; the third critical equation factors by the rank defect, and genericity makes those n-2 roots simple and disjoint from the remaining exceptional loci. Duff--Rydell's proved singular-locus theorem identifies exactly these points as singular-image criticals, leaving 3n-8 smooth ED-critical image tuples. Fresh exact rational reconstructions for n=4,5,6 gave degree tuples (4,4,6,2,4), (6,6,10,3,7), and (8,8,14,4,10) for N,D,J,S,J/S and verified coprimality/divisibility; these finite checks corroborate rather than replace the generic proof.

## originality

PASS

Originality passes. Duff--Rydell explicitly state the exact formula as Conjecture 7.5(1), while their proved structural results identify the singular rank-one stratum and smooth PGL2 stratum but do not compute the ramification subtraction. The later Finkel--Rodriguez theorem concerns rational curves and line multiview varieties, not this three-dimensional resectioning stratum. Resultary search returned the audited record but no prior proof of the resectioning formula.

## value

PASS

The theorem resolves a named conjecture in metric multiview geometry for every n at once and explains the linear ED degree structurally as total parameter ramification minus the singular-camera contribution. The result is therefore more than reproduction of a numerical sequence and provides a reusable mechanism for optimization on a singular resectioning variety.

The dated certificate retains the supplied scientific assessment, sources and limitations.
