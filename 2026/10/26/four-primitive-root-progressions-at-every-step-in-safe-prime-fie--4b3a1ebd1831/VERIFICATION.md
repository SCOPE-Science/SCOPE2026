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

# Verification

The argument is an analytic-plus-exhaustive finite proof. For all safe primes \(p\ge113\), the squarefree quartic character-sum bound \(|S_p|\le3\sqrt p\) proves that the step-independent baseline \(B_p\) exceeds four, while no more than four placements of the nonprimitive nonresidue \(-1\) may occur. Therefore \(N_p(d)\ge1\) for all nonzero \(d\), without exhaustive enumeration of large primes.

For the complementary finite range, run `python3 check_ap4.py`. It uses only the Python standard library, exhausts all safe primes below \(113\), and checks *every* \(1\le d<p\) and \(0\le x<p\) with a modular-exponentiation primitive-root predicate independent of the Legendre-character formula. It also evaluates the exact quartic character sum and \(E_p(d)\) to check the identity at every difference. All safe primes through \(1000\) are included as nonessential corroboration.

Expected final line: `VERIFY_OK: all safe primes below 113 exhaustive; exact identity and independent primitive-test through 1000`.

Finite testing through \(1000\) is not itself proof for the infinite domain, and the standalone script does not independently certify the standard Weil bound. Mathematical assessment here is not independent external review.
