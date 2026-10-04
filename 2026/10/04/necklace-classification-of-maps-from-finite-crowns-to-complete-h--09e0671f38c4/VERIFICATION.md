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

The proof is structural. The computational artifact is a finite regression check, not an infinite certificate.

`artifacts/verify.py` constructs the crown order and the complete height-two target, enumerates all order-preserving maps for six small parameter tuples, builds the undirected comparability graph on those maps, and counts its connected components. It compares those counts with
\[
1+\sum_{\ell=2}^{m-1}\frac1\ell\sum_{d\mid\ell}\varphi(\ell/d)c_d(r)c_d(s)+c_m(r)c_m(s),
\]
where
\[
c_\ell(q)=(q-1)^\ell+(-1)^\ell(q-1).
\]

The checked tuples and expected component counts are
\[
(2,2,2)\mapsto5,\quad
(2,2,3)\mapsto13,\quad
(3,2,2)\mapsto3,\quad
(3,2,3)\mapsto7,\quad
(3,3,3)\mapsto55,\quad
(4,2,2)\mapsto7.
\]

The script additionally checks the two boundary identities: the \(m=2\) formula agrees with the complete-height-two source boundary, and the \(r=s=2\) formula agrees with the four-point crown-target formula for several \(m\).

Unproved by computation: all unbounded parameter values, uniqueness of the cyclically reduced core, and the fixed-length spur-sliding classification. Those points are proved in `RESULT.md`; the finite computation only stress-tests them on representative cases.
