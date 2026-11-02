---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For each of the n−2 length-three windows, a nonconstant triple supplies two nonidentity rotations while a constant triple supplies zero. Distinct nonidentity outputs cannot coincide across windows separated by >=2 because their altered supports intersect in <=1 position and each permutation changes at least two letters. Adjacent windows coincide exactly when a length-four abcd has b != c and a,d ∈ {b,c}; the unique overlapping adjacent swap gives one duplicate. Therefore |B_3(x)|=2n−3−2H−K for every q>=2,n>=3. The T/S/D three-state transfer tracks b=c, b!=c and a∈{b,c}, or all distinct, giving exactly the displayed v_q and M_q and hence the complete population polynomial for all n by induction. Setting defect variable t=0 and inverting I−zM_q(0) gives the stated extremizer generating function for q>=3; three distinct symbols repeated attain 2n−3. Linearity of expected H and K gives the mean. Independently reconstructed output sets for q=2,n=9; q=3,n=7; q=4,n=6; q=5,n=5; q=4,n=6 exact spectrum 4u+24u^3+60u^4+132u^5+312u^6+720u^7+972u^8+1872u^9. These bounded tests corroborate the all-length structural argument.

## originality

PASS

Best-of-knowledge PASS for the exact q-ary cyclic-three output-sphere population law, collision defect and extremal finite-state enumeration. Chen–Milenkovic define cyclic bursts and code redundancy, so the channel is prior art; the inspected abstract does not state the exact q-ary enumerator, but the article full text was inaccessible and no whole-document noncoverage is asserted. The published binary (3,1)-burst code-size record answers a different optimization problem and is not the requested channel population; previous unrestricted S3 permutation sphere results use a strictly larger output set for q>=3. No indexed source examined entails the specific matrix distribution. Residual priority risk retained for the full 2026 primary preprint and unindexed enumerations.

## value

PASS

The full spectrum of one-error output balls is a natural exact invariant for combinatorial burst coding: it identifies the actual variation of packing-ball sizes, the sharp maximum and how frequently each sphere size occurs, not merely a routine single evaluation. Collision classification is necessary because overlapping windows break the naive 2(n−2)+1 count. The result is a uniform finite-alphabet/length formula useful independently of any new error-correcting code construction; it does not itself claim improved redundancy.

The dated certificate retains the supplied scientific assessment, sources and limitations.
