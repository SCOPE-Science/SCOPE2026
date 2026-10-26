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

# Reproduction and limits

The finite checks are recorded in `verification/check_spectrum.py` and `verification/check_output.txt`. Run `python3 verification/check_spectrum.py` to reproduce the printed cases \(2\le k\le8\); only Python's standard library is required. The script counts the exact congruence conditions, tests Fourier extrema numerically, checks short-grid shift reachability, and evaluates the \(r=1\) forcing response. All such checks passed at those stated integers. The mathematical theorem for every \(k\ge2\) relies instead on the character-basis proof in `RESULT.md`. The forcing response applies for every \(k\ge3\) and each fixed \(r>0\).

Literature inspection compared the original scheme in arXiv:2604.02797v1, the older wide-stencil theory arXiv:0910.1046 and the accessible abstract of doi:10.1137/0732037. The final historical full-text comparison remains incomplete. No external or independent scientific validation has been performed.
