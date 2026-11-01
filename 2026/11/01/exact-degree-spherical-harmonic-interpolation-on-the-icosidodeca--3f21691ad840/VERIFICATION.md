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

The command `python3 check_icosidodecahedron.py` was executed on the supplied file after packaging content review. It reconstructs the thirty exact vertices in \(\mathbb Q(\varphi)\) and verifies fifteen antipodal representatives and their possible dot products. It computes exact matrix ranks for degrees \(0\)–\(14\), including exact constant-vector null identities at degrees \(8\) and \(14\). Its finite-field rank computation certifies all \(248\) degrees \(15\)–\(262\) modulo prime \(1009\), with valid denominators. Finally, it checks the integer inequality closing the analytic strict-diagonal-dominance argument from degree \(263\). The analytic ingredient is the published Legendre Bernstein bound and is not experimentally inferred by the checker.

The source file is self-contained and uses Python standard-library rational and finite-field operations. All scientific limits and possible literature-equivalence risks are stated in `RESULT.md` and `REVIEW.md`. No independent mathematical validation is claimed.
