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

The exact domain is the standard uniform random recursive tree on \(n\ge2\) labelled vertices, with leaves defined by outdegree zero and Wiener index defined by unordered-pair graph distances.

The critical proof steps are:

1. \(W_{n+1}=W_n+n+D_n(U_n)\) and \(L_{n+1}=L_n+1-J_n\).
2. \(\sum_vD_n(v)=2W_n\).
3. The leaf-transmission statistic \(S_n=\sum_{v\text{ leaf}}D_n(v)\) satisfies
   \[
   \mathbb E[S_{n+1}\mid T_n]
   =
   S_n+\left(1-\frac1n\right)L_n+n+\frac2nW_n.
   \]
4. These identities give closed exact recurrences for \(\mathbb EW_n\), \(\mathbb ES_n\), and \(\mathbb E[L_nW_n]\), and hence for the covariance.

`checker.py` enumerates all \(46{,}233\) recursive trees of sizes \(2\) through \(9\) via their parent sequences and recomputes all graph distances directly. It checks the leaf mean, Wiener mean, leaf-transmission mean, and leaf-Wiener covariance exactly with rational arithmetic.

The checker also replays the closed recurrences over a larger finite range. The all-\(n\) theorem rests on the symbolic proof, not on finite enumeration.

No stochastic ordering, independence claim, or complete joint law is asserted.
