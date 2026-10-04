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

The proof reduces every one-variable theory to integer feasibility.

For an \(n\)-element universe and \(k=|p|\), the only nontrivial sentence conditions are:
\[
k=0,\quad k=n,\quad k>0,\quad k<n,\quad
k\ge n-k,\quad k\le n-k,\quad k>n-k,\quad k<n-k.
\]

These yield a strongest lower bound chosen from
\[
0,\ 1,\ \lceil n/2\rceil,\ \lfloor n/2\rfloor+1,\ n
\]
and a strongest upper bound chosen from
\[
n,\ n-1,\ \lfloor n/2\rfloor,\ \lceil n/2\rceil-1,\ 0.
\]

A model exists exactly when the lower bound does not exceed the upper bound. The \(25\) comparisons produce only
\[
\varnothing,\ T_1,\ T_2,\ T_3,\ E_2.
\]

The bundled `verify.py` checks every subset of the eight nontrivial conditions and independently checks all \(25\) bound pairs on universe sizes through \(64\). It also verifies concrete theories realizing all five spectra and prints `VERIFY_OK`.

## Limits

The computation corroborates the symbolic proof. The theorem is only for one raw variable and the original non-Boolean sentence language.
