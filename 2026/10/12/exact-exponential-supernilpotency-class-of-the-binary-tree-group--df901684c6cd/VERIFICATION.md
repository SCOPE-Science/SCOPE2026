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

The proof-critical invariant is the leaf capacity \(c(a_i)=2^{n-1-\lfloor\log_2 i\rfloor}\). For each allowed nonzero product \(a_{2i}a_{2i+1}=a_i\), the verifier checks
\[
c(a_{2i})+c(a_{2i+1})=c(a_i).
\]
It then computes recursively, for every nonzero element, the maximum number of leaves and maximum depth of a nonzero term evaluating to that element. For each \(3\le n\le10\), the maximum at \(a_1\) is respectively \(2^{n-1}\) leaves and depth \(n-1\). The script also reconstructs the complete balanced bottom product and checks that it evaluates to \(a_1\).

Run:

`python verify_exact_Hn_classes.py`

Expected terminal line: `VERIFY_OK`.

The finite run is a regression check on the multiplication indexing and the structural recurrence. It does not establish the theorem for unbounded \(n\); the arbitrary-\(n\) result is proved by the induction in `RESULT.md`. No independent audit has been performed.
