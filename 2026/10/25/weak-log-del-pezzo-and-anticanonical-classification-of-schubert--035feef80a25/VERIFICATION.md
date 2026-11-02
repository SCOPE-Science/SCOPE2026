---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Read the same 2026 primary Schubert surface paper at Sections 3.11, 4.3, 4.5-4.8 to verify the blow-up resolution, quotient singularities, exceptional curve contractions and total-transform intersection basis. For the iterated blow-up of P² at κ chain points on line at infinity, the classes satisfy B=H-ΣE, B²=1-κ, K_X=-3H+ΣE and -K_X=2H+B. Singular pencils contract only crepant -2 strings and have f^*(-K_Y)=2H+B, volume 9-κ, B-intersection 3-κ. For regular pencils κ>=2 the additional B contraction has discrepancy a=(3-κ)/(κ-1), yielding f^*(-K_Y)=2H+(2/(κ-1))B and volume 4κ/(κ-1). Nefness is checked on every irreducible curve: nonexceptional D distinct from B has H.D>=1 and B.D>=0; exceptional surviving terminal A has positive intersection; intermediate surviving A has zero; singular B has 3-κ. Klt quotient singularities and characteristic-zero basepoint-free theorem yield the weak-Fano/Fano and anticanonical contraction criteria. Independently checked exact rational intersection identities for all κ<=8 and selected size profiles; finite checks do not replace all-curves proof.

## originality

PASS

Galgano–Gesmundo–Keneshlou (arxiv:2610.07164, posted October 5, 2026) completely establishes resolution, quotient types and intersection pairing. The new statement derives a sharp all-Kronecker-profile anticanonical nef/ample classification, volumes and contraction locus; no direct anticanonical classification appears in the inspected original sections. A nontrivial all-curves positivity argument is added, not merely renaming a published surface. However automatic use of source intersection data makes a possible unpublished corollary a residual risk.

## value

PASS

Weak log del Pezzo and log del Pezzo criteria are central birational-geometric positivity invariants. The classification gives a complete natural family boundary, exact anticanonical volumes and exceptional loci for all complex matrix-pencil Schubert surfaces, including the sharp κ=3 singular boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
