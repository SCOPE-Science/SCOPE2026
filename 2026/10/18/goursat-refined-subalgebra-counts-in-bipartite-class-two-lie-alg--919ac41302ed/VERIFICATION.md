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

# Reproducible mathematical checks

Run `python3 verification/verify.py` with standard Python 3 and no extra packages. The program explicitly enumerates every reduced-row-echelon subspace of the ambient vector space, independently checks Lie closure by direct coordinate brackets, computes the invariants \((i,j,t,e)\) from ranks, and compares the actual count in **each** stratum to the theoretical Gaussian product. Its RREF generator does not construct candidate subalgebras from the theorem.

The eight completely enumerated configurations are \((a,b,q)=(1,1,2),(1,1,3),(1,1,4),(1,1,5),(1,2,2),(1,2,3),(2,1,2),(2,2,2)\). The extension-field case \(q=4\) explicitly implements \(\mathbb F_2[X]/(X^2+X+1)\). The last case has ambient dimension eight; its \(15727\) subalgebras occupy fifty-five four-way profile strata and have dimension histogram \(1,255,2347,6147,5267,1443,251,15,1\). Every expected stratum count matched the independent enumeration and the program ended with `ALL_EXACT_STRATUM_CHECKS_PASSED 8 cases`.

The proof, not a finite test, establishes the result for unbounded \(a,b\) and every prime power \(q\). No machine formalization or external expert certification is claimed. Independent audit has not been performed.
