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

The checker constructs the friendship graph \(F_r\) directly. For each labeling
\[
f:V(F_r)\to\{0,1,2,3\},
\]
it independently tests the defining total double Roman conditions: every zero must see a label \(3\) or at least two labels \(2\), every one must see a label at least \(2\), and every positive vertex must have a positive neighbor.

For each \(r\in\{2,3,4\}\), the checker enumerates all labelings and compares the complete empirical weight distribution with
\[
z^3(P(z)^{2r}-1)+z^2Q_2(z)^r+zQ_1(z)^r+Q_0(z)^r.
\]
It also checks the minimum weight, the exact number of minimum functions, and the closed total count.

Recorded output:

```text
VERIFY_OK
friendship_parameters_checked = 2..4
labelings_checked = 279552
all weight-enumerator coefficients matched
all minimum weights matched 4
all minimum-function counts matched 2r
all total-function counts matched 16^r - 1 + 13^r + 10^r + 8^r
```

The computation is finite corroboration only. The theorem for every \(r\ge2\) follows from the exhaustive center-state proof in the result file.
