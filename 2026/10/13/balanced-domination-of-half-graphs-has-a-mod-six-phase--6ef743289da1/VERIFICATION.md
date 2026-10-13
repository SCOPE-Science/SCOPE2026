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

The verifier constructs the half graph directly from

\[
a_i b_j\in E(H_n)\quad\Longleftrightarrow\quad i\le j.
\]

For every labeling in \(\{-1,0,1\}^{2n}\) with \(1\le n\le6\), it tests every closed neighborhood and retains exactly those labelings whose label sum is zero at every vertex. It then compares the full solution set, not only the optimum value, with the six-periodic family stated in `RESULT.md`.

Recorded output:

```text
VERIFY_OK
n=1: BDFs=3, weights=[0, 0, 0], gamma_b=0
n=2: BDFs=1, weights=[0], gamma_b=0
n=3: BDFs=1, weights=[0], gamma_b=0
n=4: BDFs=3, weights=[-2, 0, 2], gamma_b=2
n=5: BDFs=1, weights=[0], gamma_b=0
n=6: BDFs=1, weights=[0], gamma_b=0
brute_force_labelings_checked = 597870
symbolic_parameter_values_checked = 360
all balanced-function families and weights matched the theorem
```

The direct enumeration checks \(597{,}870\) labelings. A separate recurrence calculation tests all three starting parameters for every \(1\le n\le120\), checking the endpoint condition and the exact weight. The finite checks are corroborative only; the theorem for arbitrary \(n\) follows from the symbolic recurrence proof.
