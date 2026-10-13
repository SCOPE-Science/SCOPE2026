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
For a balanced table with \(n\) subjects per arm, treatment events \(a\), and control events \(b\),
\[
RR=\frac ab,
\qquad
OR=\frac{a(n-b)}{b(n-a)}.
\]

For two tables \((a,b)\) and \((c,d)\), the exact signs of the differences are determined by
\[
ad-bc
\]
and
\[
ad(n-b)(n-c)-bc(n-a)(n-d).
\]

The embedded `verify_rr_or_minimal_reversal.py` computes both the direct rational comparisons and these independent cross-multiplied signs.

It verifies:
- protective table counts \(0,1,3,6\) for \(n=2,3,4,5\);
- strict-reversal counts \(0,0,0,1\) on those same domains;
- the first weak-order mismatch at \(n=4\), where \((1,2)\) and \((2,3)\) tie under \(OR\);
- the unique first strict reversal at \(n=5\), \((2,3)\) versus \((3,4)\);
- exact witness values \(RR=2/3,3/4\) and \(OR=4/9,3/8\);
- the continuation family for every \(5\le n\le500\).

The family for every integer \(n\ge5\) is proved symbolically in `RESULT.md` through
\[
4(n-3)(n-1)-3(n-2)^2=n(n-4)>0.
\]

Run:

`python3 verify_rr_or_minimal_reversal.py`

The first output line must be:

`VERIFY_OK`
