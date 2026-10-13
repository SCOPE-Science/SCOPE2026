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

The infinite proof has two components.

First, if doubling \(X=(a,c)_b\) causes no low-digit carry, then digitwise doubling gives
\[
S_{3,b}(2X)=8S_{3,b}(X),
\]
which is incompatible with
\[
S_{3,b}(X)=2X,\qquad S_{3,b}(2X)=X.
\]

Second, in the carry branch,
\[
2X<b^2
\]
forces
\[
a<b/2,
\]
while the carry forces
\[
c\ge b/2.
\]
The first cycle equation gives
\[
c^3\le b^2+b-2.
\]
Thus
\[
b^3/8\le b^2+b-2,
\]
which fails for every integer \(b\ge9\).

The attached checker exhausts the remaining bases \(2\le b\le8\). It visits exactly \(68\) digit pairs for which both \(X\) and \(2X\) are two-digit. Exactly one satisfies the first cycle equation:
\[
b=8,\qquad X=27=(33)_8.
\]
Its double is
\[
54=(66)_8,
\]
and
\[
S_{3,8}(54)=432,
\]
so it does not return to \(27\).

The file `small_b_certificate.csv` records the exact per-base counts reproduced by the checker. No finite experiment is used to justify the exclusion of bases \(b\ge9\).
