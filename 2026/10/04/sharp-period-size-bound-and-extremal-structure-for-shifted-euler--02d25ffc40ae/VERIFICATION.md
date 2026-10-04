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
Run `python3 verify.py`.

The checker uses deterministic integer factorization and primality testing. For every \(2\le k\le80\) and every start \(1\le x_1\le600\), it follows the exact map \(F_k(n)=\varphi(n)+k\) to its repeated state, extracts the minimal cycle, and verifies:

\[
\sum_i (x_i-\varphi(x_i))=Tk,
\]

\[
M\le[T(k-1)+1]^2,
\]

and the full equality structure whenever the bound is attained.

It separately checks the exact extremal cycles for \((T,k)=(2,3)\), \((3,3301)\), and \((4,8401)\), including deterministic primality of every required progression term and the return map from the terminal prime square.

A successful replay prints `VERIFY_OK`.

These are finite regression checks, not an exhaustive proof. The infinite theorem is established symbolically in `RESULT.md` by the cyclic cototient identity and the composite totient inequality.
