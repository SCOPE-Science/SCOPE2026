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

The universal result is verified by the proof in `RESULT.md`. Its critical implications are:

1. If \(p\nmid(8\beta+r)\), Dirichlet's theorem supplies a prime term of the progression, so the universal modulo-\(4\) congruence fails.
2. If \(p^2\mid(8\beta+r)\), the unique possible numerator is \(rp^2\); a divisor-count witness gives value \(6\pmod4\), including a separate Dirichlet witness when \(p=r\).
3. If \(p\parallel(8\beta+r)\), the problem is exactly whether \(8pn+t\) can be a square. This is equivalent to solvability of \(x^2\equiv t\pmod{8p}\), hence to the simultaneous local conditions modulo \(8\) and modulo \(p\).
4. The candidate \(t\)-values are a complete residue system modulo \(p\); after deleting the zero residue, the quadratic nonresidues contribute exactly \((p-1)/2\).

`verify.py` performs an independent finite regression check for every odd prime \(p\le199\) and every \(r\in\{3,5,7\}\). It exhausts all \(\beta\), compares the claimed criterion against a direct square-congruence search modulo \(8p\), constructs exact square witnesses in every failing exact-\(p\) case, checks the predicted cardinalities, and evaluates initial divisor-count progression values for every predicted member.

Limits: the computation does not verify Dirichlet's theorem or establish an infinite statement by enumeration. It is intended to catch algebraic, boundary, and implementation errors in the symbolic argument.
