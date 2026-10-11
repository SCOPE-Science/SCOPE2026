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

# Reproducibility and limits

Run `python3 verify.py` with Python 3.8 or later; no external packages or data are required. The program exhausts all \(S_n\) elements for \(2\le n\le6\), evaluates the alternating signed trace on the multigraded cellular basis by enumerating fixed injective words, and separately computes the induced character through falling factorials and the orientation sign. It checks 4,166 full degree/permutation character pairs, including identity ranks, and evaluates 15 full-group invariant averages. It records 20,496 fixed oriented-cell contributions. The expected successful stdout begins `VERIFY_OK`.

The comparison is a finite consistency test of two distinct arithmetic implementations. It does not certify the infinite homotopy statement; the proof relies on the cited integral Hochster theorem, injective-word shellability, exact cell-orientation accounting and finite-group rational cohomology invariants. No test establishes integral acyclicity of the quotient or an equivariant homotopy splitting. The special case \(n=2\) checks explicitly that a transposition acts by \(-1\) in degree four.
