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
For two equally weighted biallelic populations with exact allele-A counts \(a\) and \(b\) on a common denominator \(m\), define
\[
d=|a-b|,
\qquad
t=|a+b-m|.
\]

The proof reduces the statistics to
\[
G_{ST}=\frac{d^2}{m^2-t^2},
\qquad
D=\frac{2d^2}{m^2+d^2+t^2}.
\]

The embedded `verify_gst_jost_boundary.py` enumerates every positive biallelic two-population frequency configuration for
\[
2\le m\le5,
\]
quotients by population exchange and global allele relabeling, and checks every unordered pair.

It verifies no strict reversal through \(m=4\) and exactly one at \(m=5\):
\[
(1,2)\quad\text{versus}\quad(2,3).
\]

It also checks the fixed-gap antimonotonicity formula and replays the explicit reversal family for every \(5\le m\le100\).

Run:

`python3 verify_gst_jost_boundary.py`

The first output line must be:

`VERIFY_OK`

All calculations use exact integer or rational arithmetic.
