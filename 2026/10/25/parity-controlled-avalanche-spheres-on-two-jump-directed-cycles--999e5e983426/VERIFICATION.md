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
# Reproducibility checks

Run `python3 verify.py` with Python 3.9 or later; no external libraries or network access are required.

The checker performs synchronous sandpile updates from full integer chip vectors until a configuration recurs. It also regenerates the same firing sets independently with the defect recurrence. For \(5\le n\le81\), both single-vertex grain values are tested, including the exact transient position and first repeated time, rather than relying on a preselected stopping round. It verifies omitted-vertex blocks, the conical early stages, partition assertions and the special last simplex in the contractible branch. Translating the exceptional vertex is checked for \(5\le n\le18\). Finally, every filtered avalanche complex for \(5\le n\le12\) is directly expanded into simplicial faces; boundary matrices are reduced exactly over \(\mathbb F_2\) without using the nerve model. The expected reduced Betti ranks agree in each tested case.

Observed final line: `VERIFY_OK orbit_cases=476 direct_mod2_stages=80`.

These checks do not establish the theorem for all \(n\), do not themselves certify integer torsion, and do not replace the proof of homotopy equivalence via the simplex-cover nerve theorem. No independent scientific audit was performed.
