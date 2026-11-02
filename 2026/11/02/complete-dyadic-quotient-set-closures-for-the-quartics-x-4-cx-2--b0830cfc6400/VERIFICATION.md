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
# Reproduction and logical checks

The complete infinite proof is in `RESULT.md`; it uses no computer-dependent premise. Its critical steps are: every dyadic unit square lies in \(1+8\mathbb Z_2\), every element of that ball is a unit square, and \(g_k(t)=t(c+2^{2k}t)\) is an isometric bijection from \(1+8\mathbb Z_2\) to \(c+2^{2k}+8\mathbb Z_2\) for odd \(c\) and each nonnegative integer \(k\). Taking quotients of the exact images yields all listed valuation/unit shells, and positive integers approximate the dyadic inputs away from poles.

Run `python3 verify.py` in the same directory as the proof. The script has no external dependencies. It checks odd-square residues and the image-ball statement through moduli \(2^4\) to \(2^{10}\) for thirteen positive and negative odd coefficients, with \(k=0,1,2,3,4,5\); it separately checks actual quotient residues modulo \(16\) at normalized valuations from \(-5\) through \(5\). Successful execution prints `VERIFY_OK` and the counts. Finite checks cannot certify universal quantifiers, absence of a publication, or an external review.
