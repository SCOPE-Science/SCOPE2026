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

The claim was checked by direct conditional row-sampling probabilities, exact combinatorial counting of directed cycles, algebraic signs of \((n-\ell)((n-1)/(n-2))^\ell-n\), and a fixed-parameter binomial expansion. This is the complete analytical argument for every \(n\ge3\), \(1\le k\le n-1\), and \(2\le\ell\le n\).

The standalone `verify.py` checks exact rational moments for all allowed \(k\) at \(n=3,4,5\), plus \((n,k)=(6,1)\), and separately enumerates all directed Erdős–Rényi arc sets at \(n=4\) with \(p=1/3\). It prints `VERIFY_OK` on success. The tests cover finite samples only, and numerical experiments cannot prove the full quantified theorem. The fixed-parameter limits require \(k\) and \(\ell\) to remain fixed as \(n\to\infty\).

The literature comparison has historical-priority uncertainty. The self-review does not constitute independent verification, and no independent audit has been performed.
