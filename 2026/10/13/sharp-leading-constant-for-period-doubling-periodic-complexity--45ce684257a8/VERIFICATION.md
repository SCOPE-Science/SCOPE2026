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

Run `python3 verify.py` beside `certificate.json`.

The verifier generates the period-doubling word and evaluates the local-period definition directly at the first \(128\) positions. Those values are checked against the six-dimensional matrix representation used in the proof, including the published first sixteen local periods.

It then constructs the affine functional for
\[
q(n)=p(2n)+p(2n+1)-2p(n)-1
\]
and checks all seven kernel vectors, outputs, and transitions by exact integer arithmetic. The resulting recurrences for the two auxiliary sequences are checked through \(20000\) indices.

The summatory discrepancy bound
\[
|3Q(n)-n|\le5(\lfloor\log_2n\rfloor+1)
\]
and the exact identity
\[
P(2n)-2P(n)=n+Q(n)
\]
are replayed through \(n=50000\). Finally, the verifier independently reproduces the published formula for \(P(2^\ell)\) through \(\ell=15\).

These computations verify the finite matrix algebra and source normalization. The asymptotic theorem follows from the symbolic recurrence and interpolation proof in `RESULT.md`, not from finite experiments.
