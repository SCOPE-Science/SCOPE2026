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
The theorem is proved by a per-ballot identity.

For each nonempty ballot \(A_i\) and one-vacancy committee \(W_c=C\setminus\{c\}\),
\[
\operatorname{SAV}_i(W_c)
=
1-\mathbf 1_{\{c\in A_i\}}\frac1{|A_i|}
\]
and
\[
\operatorname{PAV}_i(W_c)
=
H_{|A_i|}
-\mathbf 1_{\{c\in A_i\}}\frac1{|A_i|}.
\]

Therefore
\[
\operatorname{PAV}(W_c)-\operatorname{SAV}(W_c)
=
\sum_i H_{|A_i|}-n,
\]
which is independent of the omitted candidate.

The embedded `verify_sav_pav_one_vacancy.py` checks these identities using exact rational arithmetic for every nonempty ballot through eight candidates and every possible omitted candidate.

It also exhausts every approval profile with two through four candidates and one through four voters, totaling \(57160\) profiles, and verifies:
- identical SAV and PAV winner sets;
- a committee-independent score difference;
- the minimum-normalized-support characterization.

Run:

`python3 verify_sav_pav_one_vacancy.py`

The first output line must be:

`VERIFY_OK`

The finite replay is only a consistency check; the proof covers every finite candidate and voter set satisfying the stated assumptions.
