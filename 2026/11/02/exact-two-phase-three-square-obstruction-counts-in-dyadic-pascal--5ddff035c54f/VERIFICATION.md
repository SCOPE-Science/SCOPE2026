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
The standalone, standard-library-only verifier `verify_dyadic_binomial_three_squares.py` runs with `python3 verify_dyadic_binomial_three_squares.py`. It computes \(\binom{2^r}{k}\) as exact integers for every \(0\le k\le2^r\), \(1\le r\le13\), tests their full odd parts against Legendre's obstruction, and independently compares the algebraic index criterion. Across those rows it checks \(16{,}395\) coefficient entries. For \(14\le r\le20\), it checks a further \(2{,}080{,}761\) interior indices using the residue criterion and independently verifies the closed-form count; no giant integer binomial coefficients are formed in this extension.

All assertions completed without errors in the recorded execution. Finite checks cannot establish an infinite formula; the proof rests on the two-adic product and the exact congruence-stratified enumeration. No external proof assistant or independent mathematical validation is claimed. The script requires only Python 3 standard library and no online resources.
