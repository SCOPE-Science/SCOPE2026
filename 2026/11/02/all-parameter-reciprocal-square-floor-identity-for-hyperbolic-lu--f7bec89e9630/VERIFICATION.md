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

# Verification notes

Reproduce by running `python3 verify.py` with Python 3, using only the standard library. Expected successful output: `VERIFY_OK certified_cases=256 integer_parameters=3..10,1..4,1..8`.

The exact computation constructs integer recurrence terms, then bounds \(S=\sum_{k=n}^{\infty} U_{rk}^{-2}\) between rational values \(L\) and \(H\). The lower endpoint is the finite partial sum through \(k=3n+12\). The upper endpoint adds a rigorous geometric tail bound. Since \(U_{j+1}\ge2U_j\) for all \(j\ge1\) at \(s\ge3\), the subsequence ratios are at least \(2^r\), giving a tail bound \(U_{r(3n+13)}^{-2}/(1-4^{-r})\). All \(256\) triples pass the exact rational tests \(AL>1\) and \((A-1)H<1\) when \(A>1\). The \(A=1\) boundary requires only the first test.

The theorem itself holds for infinitely many triples and is established by the displayed Binet-series inequalities in `RESULT.md`, not by enumeration. Neither third-party verification nor a separate independent audit has been performed. Conjectured extensions to other recurrence parameters or powers have not been proved here.
