---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In the fixed point ones lie in the last position of a substitution block. Successive preimage zeros have gap one or two (both occur), giving the two internal zero-run lengths q-1 and 2q-1; the initial run does not add a new extension pair. Testing a core of j zeros against those lengths gives all four extensions for j=q-1, only the two mixed extensions for j=2q-2, and all but (1,1) for the other eligible seeds. The empty core misses only (1,1). For a bispecial core containing 1, its left 1-extension forces alignment at the start of a block and its right 1-extension forces length -1 modulo q; the invertible block encoding identifies a unique shorter core. The extension pairs complement exactly, so iteration exhausts all the cores. In the minimal-absence implication, the missing pair plus recurrence lets each occurring maximal proper factor be extended on the missing side with the other bit, proving bispeciality. Reversal commutes with T_q; the absent endpoints match; and the surviving seeds have j+1 in [2,2q-1] not divisible by q, making scales disjoint. The length formula, generating series and forbidden basis follow. Independent exact bounded test: python3 /workspace/reproduction/3.py (output 3.txt). Images of the three legal adjacent pairs at a scale with block size at least 160 cover the full infinite-word factor language through length 160 for each of q=3,4,5,6,7,8,9,12,17,31; direct enumeration agrees. The general result uses desubstitution, not a finite-prefix extrapolation.

## originality

PASS

Best-of-knowledge pass for the complete binary, q-uniform, q>=3 list, including extension deficits and palindromicity; neither the accepted q=2 seed/desubstitution precedent nor general bispecial algorithms are new. Exact all-length results for q-letter generalizations concern different words.

## value

PASS

A complete antidictionary is a natural intrinsic description of a factor language, enabling membership tests by forbidden-pattern avoidance. The all-scale exact seed deficit structure and the fact that every minimal obstruction is a palindrome are useful structural information, not an arbitrary bounded enumeration of absent strings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
