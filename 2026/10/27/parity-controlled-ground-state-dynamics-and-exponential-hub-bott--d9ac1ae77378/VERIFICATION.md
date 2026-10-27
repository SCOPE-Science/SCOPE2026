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

The full mathematical proof is in `RESULT.md`. The independent-of-formula finite enumeration supplied here is **not** an independent audit: it is an executable same-author verification aid.

Run `python verify.py` in a directory containing the two embedded files `verify.py` and `verification_output.txt`. The script uses Python's standard library and should end with `CHECK_OK cases 21`. It enumerates every spin configuration in twenty-one parameter pairs with up to eleven vertices, builds all single-site spin-flip transitions, computes terminal strongly connected components using Tarjan's algorithm, checks reversibility of recurrent transitions, and compares the resulting attractor sets with the claimed parity rules. `verification_output.txt` is the output observed for the packaged script.

For the general theorem, the crucial proof checks are: (i) a spin flip with \(u\) equal-colour neighbours changes the number of monochromatic edges by \(d-2u\); (ii) a peripheral spin has equal-colour count \(s-k_j\) or \(k_j-1\); (iii) even-size blocks allow hub flips only at all-\(\ell\) configurations; (iv) the local subset-inclusion graphs are connected; and (v) the stationary boundary flux of the hub-colour half is \(q^r/(2N)\). These are established symbolically in the proof for arbitrary parameter values.

Limits: finite exhaustive checks cover only the listed small instances, and the mixing result is a lower bound, not an exact asymptotic or matching upper bound. Full-text access to the 2008 preprint was not available; the later openly rendered primary article was inspected. No independent audit or external certification is claimed.
