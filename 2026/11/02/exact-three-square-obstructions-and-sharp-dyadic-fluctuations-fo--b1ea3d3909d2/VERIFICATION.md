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

# Verification record

The standalone `verify.py` is compatible with Python 3.10+ and requires only the standard library. Run it without arguments. It reconstructs the exact \(32\)-state matrix from the digit recurrence, checks both graph directions and the self-loop, verifies that the \(18\)-degree annihilator evaluates to the zero matrix, and replays the first \(34\) identities which, via Cayley--Hamilton in dimension \(34\), imply the infinite dyadic formula. All matrix arithmetic uses arbitrary-precision integers.

The script additionally verifies the local binary odd-part formula for \(16384\) indices and checks the criterion against independently accumulated factorial and superfactorial valuations and odd parts for \(0\le n\le4096\). These finite numerical cross-checks are not substitutes for the infinite mathematical argument; the finite matrix identities *are* explicitly used as rigorous finite premises of that argument.

Reproduction output:

`VERIFY_OK states=32 matrix_nonzero_entries=64 annihilator_degree=18 dyadic_Cayley_Hamilton_terms=34 checked_arithmetic_n=4097 obstructions_in_range=768 digit_cases=16384`

The code provides no external independent audit and no claimed independent certification. The result has undergone only the stated self-review.
