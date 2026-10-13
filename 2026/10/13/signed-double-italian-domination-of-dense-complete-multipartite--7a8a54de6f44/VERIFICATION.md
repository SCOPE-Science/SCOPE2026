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

The verifier exhaustively scans every labeling
\[
f:V(G)\to\{-1,1,2,3\}
\]
for every complete multipartite isomorphism type of orders \(6\) through \(9\) having at least three parts and no part smaller than two.

For each labeling it independently checks the closed-neighborhood inequality and the two defender-subset requirements by summing positive labels in the appropriate neighborhoods. It rejects every weight below the theorem's claimed minimum and separately constructs and verifies the explicit theorem witness.

Recorded output:

```text
VERIFY_OK
complete_multipartite_types_checked = 9
orders_checked = 6..9
labelings_scanned = 1265664
explicit_constructions_checked = 9
all parts >=2 and at least three parts
every minimum matched 2 iff a part has size 2, else 3
```

The exhaustive computation is corroborative only. The theorem for arbitrary part sizes follows from the symbolic part-sum lower bounds and explicit constructions in the proof.
