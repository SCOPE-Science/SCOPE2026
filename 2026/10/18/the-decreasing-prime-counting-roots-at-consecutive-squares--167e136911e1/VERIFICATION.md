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
# Verification of square-prime-counting root monotonicity

## Reproducing the finite certificate

Place `VERIFY.py` and `FINITE_CASES.csv` in the same folder and execute `python VERIFY.py` with standard Python 3. The program compares two independently coded exact primality indicators through \(10000\), regenerates each of the 97 \((n,\pi(n^2),\pi((n+1)^2))\) records, and tests \(\pi(n^2)^{n+1}>\pi((n+1)^2)^n\) using unrestricted integers. It also tests the reverse inequality at \(n=2\). No packages or approximate calculations are required.

## Non-computational verification

Check that in any block of six consecutive integers exactly two are coprime to six, and in any leftover block of at most five at most two are coprime to six. With the Rosser--Schoenfeld lower bound \(\pi(x)>x/\log x\) for \(x\ge17\), deduce \(n\log(B/A)<(69/50)\log n\) for \(n\ge100\). The monotone function \(\sqrt t-2\log t\), positive at \(100\), implies \(\log A>(3/2)\log n\). These steps prove the infinite tail separately from the finite certificate.

## Limits

The computational table is exhaustive only over \(3\le n\le99\). All larger indices are covered analytically. The external classical bound is cited, not re-proved here. No independent validation has been performed.
