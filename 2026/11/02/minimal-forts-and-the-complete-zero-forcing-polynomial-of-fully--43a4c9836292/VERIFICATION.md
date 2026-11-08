---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For fully subdivided K_n, cut-edge subdivisions must be in any fort containing both original and omitted vertices. A fort without originals corresponds to an edge set with no degree-one vertices, whose minimal members are simple cycles. The other minimal forts are all originals and n mixed star-complements. Hitting all forts is equivalent to a nonempty original seed selection and a forest of omitted subdivision edges, except n forbidden original-singleton/star pairs. Labeled forest exponential formula proves all coefficients and Cayley gives n(n^{n-2}-1) minimum forcing seeds for n>=3. Independent verification: Independently enumerated forts and ordinary forcing processes on fully subdivided K_3 and K_4. The complete forcing polynomials had coefficients n=3 {2:6,3:18,4:15,5:6,6:1}, n=4 {4:60,5:156,6:178,7:116,8:45,9:10,10:1}; both matched fort categories and forest formula. Inspected verify.py; finite n is not all-n evidence.

## originality

PASS

Best-of-knowledge: inspected accessible closely related primary PDFs, searched published mathematical records for aliases/stronger results, and compared implications. The scalar zero forcing number m-n+2 for fully subdivided Hamiltonian graphs is already known from Barrett et al./Catral et al. The present fort classification, all coefficients, and n(n^{n-2}-1) minimum sets do not follow solely from that scalar. Residual priority limitations are explicit.

## value

PASS

The full forcing polynomial and complete minimal-fort hypergraph for a canonical incidence subdivision give all seed-size populations, not just the already-known scalar zero forcing number. The labeled Cayley minimum-set census is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
