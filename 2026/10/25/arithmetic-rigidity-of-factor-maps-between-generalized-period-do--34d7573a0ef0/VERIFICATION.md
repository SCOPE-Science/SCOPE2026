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

# Reproducibility and verification

Run `python3 verify.py` from the package root with Python 3; no third-party dependencies are required. The expected final line is:

`VERIFY_OK substitution_alphabets=11 q_r_pairs=121 reduction_pairs_checked`

The script reconstructs \(\theta_q^j(0)\) for \(2\le q\le12\) through length \(4096\) and compares each symbol against \(\nu_2(n+1)\bmod q\). It checks the congruence obstruction for all \(121\) ordered pairs \((q,r)\), comparing finite windows obtained by moving an exceptional point through exponents separated by \(q\). These windows are valid stabilizing coordinate models for singular fibres, not an exhaustive test of arbitrary continuous factor maps. Finally, for \(r\mid q\) it checks equality of the reduced substitution prefixes and representative factor languages through word length \(21\).

The universal proof uses: (i) the exact \(2\)-adic fibre sizes and their disjointness; (ii) maximal equicontinuity of the almost-one-to-one adding-machine factor; (iii) surjectivity forcing the induced odometer translation to be an ordinary integer; (iv) disagreement of the singular-coordinate residues when \(r\nmid q\); and (v) density of nonsingular fibres for uniqueness. No finite numerical experiment is treated as a proof of an infinite classification. The review remains non-independent.
