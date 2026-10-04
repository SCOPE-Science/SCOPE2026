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

Run:

```text
python verify.py
```

Expected terminal line:

```text
VERIFY_OK
```

The verifier performs three independent finite replays. First, for \(r=3,4,5\), it exhaustively enumerates every \(K_r\)-free graph through five vertices and checks that a neighborhood mask produces a \(K_r\)-free one-point extension if and only if the selected vertices induce no \(K_{r-1}\). It also checks the coefficient distribution by neighborhood size.

Second, it verifies the \(r=3\) independence-polynomial specialization on every triangle-free graph through six vertices, including the displayed \(C_5\) and \(K_{2,3}\) examples.

Third, for every \(3\le r\le7\), it enumerates all bipartite graphs with both parts of size at most three, constructs \(B\vee K_{r-3}\), checks that this graph is \(K_r\)-free, and verifies
\[
C_{r-1}(B\vee K_{r-3};1)=(2^{r-3}-1)2^{|B|}+i(B).
\]
The current replay reports 2,572 one-point instances and 3,445 hardness instances before printing `VERIFY_OK`.

This is same-model verification. Independent audit status: not performed.
