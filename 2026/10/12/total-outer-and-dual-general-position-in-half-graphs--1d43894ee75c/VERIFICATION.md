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

The checker constructs the half graph \(H_n\) for
\[
4\le n\le7.
\]

For every vertex subset \(X\), it tests \(X\)-positionability directly: a third selected vertex \(x\) obstructs the pair \(u,v\) exactly when
\[
d(u,x)+d(x,v)=d(u,v).
\]

Using only this definition, the program tests total, outer, and dual general position for every subset, computes each maximum size, and compares the complete maximum-set family with the theorem.

Recorded output:

```text
VERIFY_OK
n=4: gp_t=2 (1 max set), gp_o=2 (6 max sets), gp_d=2 (1 max set)
n=5: gp_t=2 (1 max set), gp_o=2 (10 max sets), gp_d=2 (1 max set)
n=6: gp_t=2 (1 max set), gp_o=2 (15 max sets), gp_d=2 (1 max set)
n=7: gp_t=2 (1 max set), gp_o=2 (21 max sets), gp_d=2 (1 max set)
subsets_checked = 21760
all maximum-set classifications matched the theorem
```

The checker exhausts \(21{,}760\) subsets. This is complete for the tested orders and corroborative for the arbitrary-\(n\) theorem, whose proof is structural.
