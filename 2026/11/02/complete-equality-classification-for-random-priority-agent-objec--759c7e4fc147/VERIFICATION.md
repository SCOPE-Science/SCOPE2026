---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Finite domain exhausts all 24^4=331,776 strict preference profiles of three objects plus outside option, and 24 priority orders per profile. For each profile, u_i and v_x count separate marginal unassignment events, and W=max(min(u_i,v_x))/24 over acceptable pairs, with zero for no such pair. Inspected source C++ and independent Python logic; independently enumerated all labeled profiles and exactly reproduced counts 317664,1728,5040,6912,432 and exactly 432 equality cases. Independent S4×S3 relabeling orbit enumeration found six orbits of size72, and each case has one maximizing pair. The six normal forms are tied by the dependency of b on a and c on b, proving same priority-wise assignment. Complete finite enumeration is proof for this precise fixed-domain claim, not a larger-market theorem.

## originality

PASS

The sharp W≤1/6 bound and one attainment example are known from Basteck–Ehlers, and explicitly excluded from novelty. Full all-profile equality orbit classification/histogram/unique-witness claim was not observed in accessible abstract or related published mathematical records. Critical primary 2026 source PDF was unavailable on arXiv/OA and authorized Oxford download returned VPN disconnected, so its unseen Appendix B may conceivably contain equivalent classifications; serious residual priority risk.

## value

PASS

Determines the entire equality structure, not another worst-case example, for the smallest scarcity case: 6 orbits, occurrence frequency 1/768 and exact unique witness, plus behavioral equivalence of distinct rankings under every priority. These are meaningful finite assignment-mechanism invariants useful for empirical benchmarking and understanding sharpness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
