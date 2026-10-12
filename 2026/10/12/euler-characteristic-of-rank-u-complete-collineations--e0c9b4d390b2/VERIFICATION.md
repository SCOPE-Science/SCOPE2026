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
The checker evaluates the square recurrence
\[
E_n
=
n^2+
\sum_{r=1}^{n-1}
\left((n-r)^2-1\right)
\binom nr^2 E_r
\]
through \(n=30\) and verifies
\[
E_n=(n!)^2.
\]

It then evaluates the general rank-\(u\) recurrence
\[
E(v,w,u)
=
\binom vu
\left[
uw+
\sum_{r=1}^{u-1}
\left((u-r)(w-r)-1\right)
\binom ur\binom wr(r!)^2
\right]
\]
for every tested triple with
\[
1\le v,w\le14,
\qquad
1\le u\le\min(v,w),
\]
and verifies
\[
E(v,w,u)
=
\binom vu\binom wu(u!)^2.
\]

It separately checks the two rational telescoping identities term by term using exact integer cross-multiplication.

These finite checks are regression evidence only. The all-parameter result is the symbolic blow-up proof in `RESULT.md`.
