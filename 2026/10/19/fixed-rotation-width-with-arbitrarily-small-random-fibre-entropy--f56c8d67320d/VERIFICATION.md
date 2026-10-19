---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and checks

Run `python3 verify.py` with Python 3 and no third-party packages. The script checks 3,317 finite assertions covering degree-one lift symmetry, both exact extreme displacements, finite interval inverse-branch endpoint/gap inequalities, all binary observation words of lengths one through ten, exact rational Bernoulli normalization and finite entropy-bound checks. It finished successfully with the message `PASS: 3317 finite assertions. Infinite results require the written proof.`

The assertion count, branch identities, and finite words are **not** a formal proof of the infinite claims. These follow from the written analytic argument using the strong law of large numbers, the random rotation interval theorem of Li–Lloyd–Romaña (arXiv:2606.16498), exact active-time Bowen metric equality, inverse-branch horseshoes, and a circle Lipschitz cover. The exact value of deterministic entropy is not determined. Independent audit is not performed.
