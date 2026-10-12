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

The analytic proof establishes the statement for every integer pair \(k\ge2\), \(m\ge2\). The attached script `verify_windmill_drs.py` is an independent finite regression check of the definitions and closed form.

It builds \(W_{k,m}=K_1\vee kK_m\), computes shortest-path distances, and for every vertex subset \(S\) tests directly whether each distinct vertex pair has at least two different values of \(d(u,s)-d(v,s)\) as \(s\) ranges over \(S\). It compares that test with the condition \(|B_i\setminus S|\le1\) for every peripheral clique. It also compares the full subset-size distribution with the coefficients of
\[
(1+z)\bigl(mz^{m-1}+z^m\bigr)^k.
\]

Replay command:

`python verify_windmill_drs.py`

Observed output:

`VERIFY_OK parameter_pairs=8 subset_checks=18720 basis_checks=225 max_order=13 boundary_checks=2`

The parameter pairs checked are the eight pairs in \(\{2,3,4\}^2\) whose graph order is at most \(13\). The script also checks that each excluded boundary \(k=1\) and \(m=1\) has a counterexample to the bladewise criterion. These computations do not certify unbounded parameter ranges; they only test the proof against exhaustive finite instances.
