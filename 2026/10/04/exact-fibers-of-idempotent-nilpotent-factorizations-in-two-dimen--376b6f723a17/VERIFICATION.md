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

The proof was checked symbolically at the level of all cases. For a fixed rank-one idempotent with image \(\operatorname{im}A\), the free entries of \(N\) reduce to the two necessary and sufficient nilpotency equations \(y=-\operatorname{tr}A\) and \(sx=-(\operatorname{tr}A)^2\). This directly gives the \(q+1\) and \(q-1\) nonzero fibers and isolates the unique failed complement \(\ker A\) in the nonnilpotent case.

The zero fiber was independently counted from the geometry of lines in \(\mathbb F_q^2\): \(q^2\) choices arise from \(E=0\), one from \(E=I\), and each of the \(q(q+1)\) rank-one idempotents admits exactly \(q\) nilpotents with image inside its kernel.

`verify_factorization_counts.py` exhaustively enumerates the factorization map over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), and \(\mathbb F_7\). The nonprime field \(\mathbb F_4\) is implemented independently as \(\mathbb F_2[t]/(t^2+t+1)\). The replay output is stored in `verification_output.txt` and ends with `VERIFY_OK`.

The finite replay is only a consistency check. The theorem for arbitrary prime powers follows from the line-counting proof and field algebra above; no extrapolation from the tested fields is used.
