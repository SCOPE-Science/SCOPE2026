---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The 1-indexed sequence, chronological permutation and left multiplication fix the sign of the result. Each A_i squares to zero and entry (1,3) is supplied only by A_1 A_2. In separate time steps this contributes once per ordered-in-time pair; within a step it contributes exactly when operator 2 occurs before 1. Thus the exact difference from T^2/2 is h^2 D(N)/2. The six decoder bins have signs -,-,+,+,-,+. On the consecutive intervals cut by 1/3,2/3,5/6, the four-point sum at (x+j)/4 for j=0..3 takes values -2,2,0,0, agreeing with f+g; the two half-scale g terms cancel exactly. Summing complete four-point blocks and removing the zero-index term leaves the odd-prefix increment. With m=2r+1 and x=phi_2(r), the remaining evaluations have cuts at 1/3 and 2/3, and on each of the three pieces the sum is -2. Dyadic inputs cannot hit those non-dyadic cuts. So D(4m+1)=D(m)-2, D(3)=-1, and N_1=3, N_(k+1)=4N_k+1, proving the exact formula on all k. Since log N_k=k log 4+O(1), the normalized entry has the claimed limit, and any fixed subordinate norm bounds its magnitude up to a constant. The proof is a subsequence lower bound for the specified decoder, not a lower bound at every N. The separate exact checker /workspace/branches/e92b8a34-d494-4399-8cf2-ad81ce59b209/independent_replay.py propagates the column U_N e_3 with rational arithmetic and confirms k=1 through 7 at T=7/5, through N=13653. Replay with python3 on that file. The frozen verification and script were inspected, not executed.

## originality

PASS

The supported distinct contribution is a matching logarithmic lower bound, with an exact signed error and coefficient along a concrete subsequence, for the three-operator base-two direct decoder. Neither the existing general upper bound nor fixed-interval van der Corput discrepancy theory is claimed as new. The closest indexed lower bound has two operators and an odd radix, not three operators and base two.

## value

PASS

A concrete exact counterexample to dropping the logarithm resolves whether the loss in the bounded-linear upper estimate is an artifact of the proof for an important sampler and decoder. The construction isolates a single matrix entry, needs no numerical tolerances, and shows a distinction from binary two-operator ordering. It makes no assertion about different decoders, symmetrization, or typical-case error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
