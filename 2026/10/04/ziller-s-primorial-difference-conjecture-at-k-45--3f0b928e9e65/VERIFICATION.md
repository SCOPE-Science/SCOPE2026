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
The infinite statement
\[
D(k)\subseteq D(k+1)
\]
is proved symbolically in `RESULT.md`; the computation is not used as an infinite proof.

The replay script `verify.py` checks the exact public finite inputs
\[
A329815(44)=308,\qquad A048670(44)=616,\qquad A048670(45)=642,
\]
and verifies that exactly \(308\) positive even integers lie in \([2,616]\).

As a regression check, the script explicitly constructs the reduced-residue gap sets for the first six primorial stages and confirms persistence between each adjacent pair. These small cases only test the implementation and normalization; the all-\(k\) argument rests on the endpoint-shift proof.
