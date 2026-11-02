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

# Reproducibility and limitations

Run `python3 check_commuting_B2.py` from this package's file directory. The expected final output marker is `B2_BAD_PRIME_COMMUTING_TUPLES_OK 10_REDUCED 4_FULL`.

The checker uses integer-coordinate arithmetic for finite fields of sizes \(2,3,4,5,7,9\). For \(\mathbb F_4\), it constructs the field by reducing polynomials modulo \(t^2+t+1\); for \(\mathbb F_9\), modulo \(t^2+1\). It independently evaluates original Lie brackets, all determinantal conditions and the two formula families. Every coordinate triple \(a,b,c\) is exhaustively enumerated for ten tested \((q,m)\) configurations; central row \(d\) contributes a proven free factor \(q^m\). In four separate field configurations with \(m=2\), the checker also exhaustively enumerates the full original eight-coordinate pair space rather than factoring out central coordinates. The captured stdout is `check_output.txt`.

Correctness for all fields and all \(m\ge2\) follows from the original-bracket and determinantal arguments in `RESULT.md`, not finite extrapolation. The proof does not claim that the unreduced commuting scheme is reduced. External literature priority is provisional; independent audit is not performed.
