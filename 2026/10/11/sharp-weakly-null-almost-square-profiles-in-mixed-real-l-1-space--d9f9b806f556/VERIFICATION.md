---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For real scalars, (|u+v|+|u-v|)/2=max(|u|,|v|) identically. Schur of atomic l1 forces the weak-null sequence atomic norm to zero; on diffuse support, max integral forces a+max(b,t). Dyadic nonatomic Rademacher signs weakly converge after multiplication by any L1 density, and y_n=(t/b)x_diff r_n attains the bound when b>0, with separate disjoint diffuse witness at b=0. The set of exactly norm-one perturbation sizes is [0,b], tolerances give b+epsilon, and minimizing L1 distance to the unit diffuse sphere yields 2a. Purely atomic measure with no diffuse part is explicitly excluded for t>0.

## originality

PASS

Rodríguez–Rueda Zoca 2023 Lemma 2.1 and Theorem 1.1 already prove weak nullity of Rademacher products and pure-diffuse qualitative WASQ; these steps are prior covered, not claimed new. Hardtke 2018 full article treats whole-space WASQ stability under absolute sums, not per-vector t-dependent profiles, tolerance radius or distance. Abrahamsen–Langemets–Lima 2014 introduces LASQ/WASQ qualitatively; Ciaci 2022 investigates positive LASQ for Banach lattices. No inspected full source computes max(1,a+t) for mixed real L1, and no stronger result was found through Resultary; unindexed pointwise Banach lattice classifications remain risk.

## value

PASS

The exact local weak-almost-square spectrum, additive tolerance cost and metric distance to square-point locus quantify a classical geometric property in the canonical mixed atomic/diffuse L1 family. This complete natural classification and sharp stability are more than a routine restatement of global WASQ or a numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
