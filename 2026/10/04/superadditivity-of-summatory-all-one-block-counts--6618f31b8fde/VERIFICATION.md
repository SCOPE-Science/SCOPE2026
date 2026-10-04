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

Run `python3 verify.py`.

The verifier uses two independent finite descriptions of the object. First it counts overlapping occurrences of \(1^r\) directly in binary strings. Second it evaluates the positional residue formula
\[
F_q(N)=q\left\lfloor\frac{N}{2^r q}\right\rfloor+
\max\left\{0,(N\bmod 2^r q)-(2^r q-q)\right\}
\]
and sums over dyadic \(q\).

It compares those two descriptions for every \(N\le4096\) and \(2\le r\le6\), exhaustively tests superadditivity on a large finite grid, stress-tests full residue periods and all boundary residues for the local lemma, and exhaustively checks the dyadic equality strip through moderate scales.

The infinite result does not rely on those enumerations. The proof in `RESULT.md` establishes the local residue inequality for arbitrary \(q\), arbitrary \(r\ge2\), and arbitrary residues, then sums the finitely many nonzero positional contributions. The equality strip is proved directly from the binary prefix structure. No external or infinite certification is asserted.
