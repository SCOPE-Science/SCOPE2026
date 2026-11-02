---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The unitary Mellin transform converts H_a into a bounded bilateral weighted translation with modulus C_a/[cosh(pi s)cosh(pi(s-a))]^(1/2). Multipliers of H_a^n have strictly convex negative logs symmetric about n a/2, yielding the stated exact cosh-product power norms. Summed log cosh values give log norm = -(pi|a|/4)n²+n log(2C_a)+O_a(1). Neumann sum gives log resolvent <= L²/(pi|a|)+O(L), while short-support Mellin inputs make all terms orthogonal and produce the matching phase-uniform lower bound. The modulus spectrum [0,norm] has no eigenvalues, and every positive power remains noncompact. Independent Gamma and log-power calculations for 12 (a,n) samples corroborate formulas. No result is claimed at a=0.

## originality

PASS

Sang introduced exactly this homogeneous noncompact quasinilpotent Hankel model and its general Mellin weighted-translation power-supremum representation: those ingredients are not new. The evaluated closed all-power norm and sharp full-complex-resolvent log-square coefficient require the central product optimization and disjoint-translate lower bound. Ignatev studies unilateral decreasing weighted shifts; Pushnitski–Sobolev treats selfadjoint dilation-periodic Hankel, distinct. Full text of Sang was not obtained in this run (accessible abstract plus source-cited theorems only), a significant priority risk that does not alone refute originality.

## value

PASS

An explicit sharp quantitative resolvent growth scale for a canonical noncompact quasinilpotent Hankel operator resolves its otherwise unknown pseudospectral singularity and distinguishes it from the Carleman endpoint; exact norm formula is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
