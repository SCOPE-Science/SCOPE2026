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

The finite checker independently generates equality/parameter-identification patterns. It does not use either closed counting formula as its enumerator: new equality classes are introduced canonically in restricted-growth order, while parameter classes are named.

For every parameter size \(0\leq m\leq3\), arity \(1\leq n\leq6\), and possible number \(k\) of genuinely new classes, the checker compares the direct enumeration with
\[
N_{m,n,k}=\frac1{k!}\sum_{i=0}^k(-1)^i\binom ki(m+k-i)^n
\]
and with
\[
N_{m,n,k}=\sum_{j=0}^{\min(m,n-k)}{n\brace j+k}\binom{j+k}j(m)_j.
\]
It then sums the layers and checks
\[
C_{m,n}=\sum_{q=0}^n\binom nq m^{n-q}B_q.
\]
It also verifies the maximum component dimension \(mn+\binom n2\).

As a separate finite sanity check for the geometric step, the script tests every triangle whose three side lengths lie in the grid \(\{1/2,2/3,3/4,1}\) and confirms that the triangle inequalities are automatic. The general reason is proved in `RESULT.md`: every side is at most \(1\) and the sum of any other two nonzero sides is at least \(1\).

Replay command:

`python3 artifacts/verify.py`

Observed output:

```
checked parameter sizes m=0..3 and arities n=1..6
component totals for m=0: [1, 2, 5, 15, 52, 203]
component totals for m=1: [2, 5, 15, 52, 203, 877]
sample layer counts m=2,n=5: [32, 211, 285, 125, 20, 1]
top dimension m=3,n=6: 33
VERIFY_OK
```

The script verifies the combinatorial and finite metric core. The identification with complete type spaces uses the source's quantifier-elimination and model-completion theorem and is established deductively in `RESULT.md`.
