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

# Verification of the cyclic-quintic Cartier identities

The included `verify.py` is a standalone Python 3 script. In a directory containing this file and `verify.py`, run `python3 verify.py`. The program computes in the polynomial ring \(\mathbf F_{11}[x,t]\) with dictionary coefficient arithmetic, expands \(h_j(x)f(x)^{2j}\) for each of four regular differentials, checks every Cartier-selected coefficient against \(H_j(t)h_j(x)^{11}\), and confirms the exact formulas for \(H_j\). It also establishes that the nonordinary locus is cut out by two different irreducible quadratic polynomials without \(\mathbf F_{11}\)-roots, and verifies their reciprocal relationship.

The checker has been run successfully on the packaged source before delivery; the expected final output line is `VERIFICATION_OK`. This universal finite polynomial identity supports the algebraic proof for all geometric parameters. The proof in `RESULT.md` additionally checks valuations and the genus, and explains the semilinear Cartier/p-rank relationship. The checker does not claim independent audit or prove any global publication-priority statement.
