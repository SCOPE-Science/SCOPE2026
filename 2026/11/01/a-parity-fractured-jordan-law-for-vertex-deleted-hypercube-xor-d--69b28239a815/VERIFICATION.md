---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For the intact cube over char2, A=sum of commuting coordinate flips satisfies A^2=(d mod2)I. With K=A+epsilon I, K^2=0 and first-coordinate block form proves rank N/2. Deleting one vertex gives B^2=epsilon I+ww^T, Bw=0, and the compression rank lemma (surjectivity K(W)=im K) supplies rank B or rank(B+I)=N/2. Thus even d has one J3(0) and N/2-2 J2(0), whereas odd d has one J1(0) plus N/2-1 J2(1). Kernel growth and periodic-space dimensions yield all q-dependent counts. Independently constructed GF2 matrices for d=2..6 and checked rank(B),rank(B^2) (even d rank B=N/2 and B2=1, odd d rank B=N-2 and B2=N-2), confirming the nonstandard rank decomposition; q powers then follow exact linear algebra.

## originality

PASS

Qualified PASS for the complete mod-two Jordan decomposition and exact transient/periodic census of a singly vertex-punctured Boolean cube, not the real adjacency spectrum of the same graph. Li–Wang–Zhang restrict their theorem to Eulerian graphs, which fail after vertex deletion due to mixed degree parity.

## value

PASS

One-vertex deletion is a natural graph-fault perturbation whose mod-two Jordan response creates a size-3 nilpotent block for even dimension and a one-step transient direction for odd dimension; exact q-dependent population formulas are useful intrinsic invariants.

The dated certificate retains the supplied scientific assessment, sources and limitations.
