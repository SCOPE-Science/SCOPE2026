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
`artifacts/verify.py` uses only the Python standard library.

For the source example
\[
(q,n,d,c)=(5,5,3,1),
\]
it constructs the Reed--Solomon MDS code
\[
[5,2,4]_5
\]
by evaluating every affine linear polynomial on \(\mathbb F_5\).

The script exhausts all nonzero codewords and verifies that every four-coordinate subset is the exact support of a minimum-weight word. For each erased coordinate it then enumerates all
\[
\binom43=4
\]
three-helper sets and checks that adjoining the erased coordinate gives one of those minimum supports.

It independently checks, for all
\[
2\le d\le n\le20,
\]
the identities
\[
N=\binom{n-1}{n-d+1}
\]
and
\[
N_t=\binom{n-1-t}{n-d+1-t}
\]
for helper-incidence counts, and verifies by exhaustive subset enumeration for \(n\le10\) that the maximum number of pairwise disjoint \(r\)-subsets is
\[
\left\lfloor\frac{n-1}{r}\right\rfloor.
\]

Successful replay prints `VERIFY_OK`.
