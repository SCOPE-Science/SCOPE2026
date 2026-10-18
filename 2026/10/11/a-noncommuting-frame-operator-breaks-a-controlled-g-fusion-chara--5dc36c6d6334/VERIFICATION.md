---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: At one-atom measure space, S=diag(1,2), T=U=[[2,1],[1,2]] >0; TST=[[6,6],[6,9]] has eigenvalues (15±3√17)/2 positive. Theorem 3.8 proposed (T²,I) form is <Λf,ΛT²f>=15+4i at f=(1,i) with source convention, nonreal. Independently multiplied matrices/characteristic polynomial. Source proof swaps TSU to STU without [T,S]=0; TS=ST suffices for this interchange. No need for infinite-dimensional/log proof.

## originality

PASS

PASS best-of-knowledge: original 2021 theorem and follow-on source do not supply this equal-positive-control counterexample to Thm 3.8; related published controlled K-g-fusion counterexample concerns a separate ordinary/controlled equivalence and distinct theorem, not implication of this exact failed characterization.

## value

PASS

PASS: Refutes an unconditional equivalence theorem central to a frame construction and pinpoints the missing commutator in the proof; commutation with the frame operator is a natural structural repair. The 2×2 size is smallest noncommuting positive matrix setting, mathematically motivated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
