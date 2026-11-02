---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Best response max(0,q-neighbor sum) follows from strict concavity and monotone benefit. At positive vertex local 3-effort sum=q; all-positive subtraction forces x_{i+3}=x_i. With zeros, positive and zero runs cannot exceed length two; two-zero gaps force singleton q endpoints, and a one-zero D-D gap forces next D parameter >= previous. Both directions of block-equilibrium correspondence were checked. With s singleton blocks, t double blocks, r doubled gaps, n=2s+3t+r; if mixed s,t, r<=s-1, yielding the stated sharp t by residue n mod3, with all-positive dimension 2 at multiples of3. Independent support-stratum linear feasibility/dimension checks n=3..10 passed; these do not extend the proof.

## originality

PASS

Bramoullé--Kranton derive the local best-response condition and special equilibria, and Naghizadeh--Liu give LCP representation for broad graphs. They do not state the all-strata S/D/gap classification or maximal dimension by n mod3 in the material inspected. Equivalent polyhedral cycle LCP results could potentially subsume it, so original only best-of-knowledge.

## value

PASS

Exact equilibrium-set dimension, including a sharp modulo-three oscillation, measures nonunique continuous equilibrium freedom in a canonical network game, beyond existence of independent-set specialized equilibria. The block parameterization exposes equality, inequality and degeneracy structure needed to study equilibrium selection/perturbations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
