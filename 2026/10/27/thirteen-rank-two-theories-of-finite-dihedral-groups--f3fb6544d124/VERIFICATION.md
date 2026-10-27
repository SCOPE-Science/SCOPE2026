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

# Reproducibility and scope

Run `python3 verify.py` (Python 3, standard library only) in the extracted directory. The output is reproducible and its captured text is included in `verification_output.txt`.

The verifier uses two separate constructions: (i) arithmetic eight-atom spectra from the explicit dihedral group law for indices \(3\) through \(300\), including all pairwise class comparisons, and (ii) a direct enumeration of all \(27\) multiplication atoms and equality atoms over \(\{e,a,b\}\) for indices \(3\) through \(33\). It also checks that the eight-atom signature completely determines the full atomic diagram for indices \(3\) through \(29\), and computes the minimal representatives among the observed classes. The checks passed and reproduced the thirteen classes and order-48 family bound.

The full infinite-dimensional conclusion requires the separate proof in `RESULT.md`: for any index at least nine the excluded-set bound produces generic noninvolutions, and the remaining profile conditions are exactly solvability of elementary congruences plus order-three/order-four divisibility. The program is not an independent proof of that universal lemma, and no formal proof-assistant or external independent audit was conducted.
