---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Reconstructed the rank computation: the zero-leading suffix lists merge by decreasing initial-zero length, with the first zero-run list winning ties iff b<d. The one-leading lists merge by increasing initial-one length, with the terminal one-run list winning ties. Counting ranks of the four run-start suffixes gives exactly u,v,p,q. The first X position and last Y position are marked; adjacency removes one internal change in X (different letters) and two in Y (same letter), and the two joins give the remaining indicators. Nine runs force u=1 and a>c. For b<d the remaining nonadjacencies and endpoints require c>=2 and d>=b+2; for b>d they require a>=c+2 and d>=2. For b=d the Y markers touch. Both families give the required boundary letters. Each family has independent positive baseline plus two unit-weight and two double-weight free parameters; the coefficient at z=1 is 1/2 times (1-z)^(-4), while the only other pole is of order two. Small coordinates and near ties have O(n^2) compositions; elsewhere exchanging a,c swaps the generic 8 and 9 classes. For the reverse, the initial 0, a predecessor 1 in the zero-leading block, then the distinct predecessors 0 and $ in the one-leading block give a four-run subsequence. In a fresh local Python calculation I sorted all rotations of w$ (equivalent to suffix sorting here: comparisons are decided by or before the unique sentinel) and used groupby for runs. All 4096 quadruples in [1,8]^4 and all 20,475 compositions of lengths 4..28 matched marker locations, run count, extremizers, and reverse lower bound. Replay by choosing three increasing cuts from 1..n-1 and taking successive differences; counting r=9 gives 2,4,10,16,28 at lengths 9..13. Witness transforms: 1$01011010 and 00011111$0, with 9 and 4 runs; all seven stated run-count witnesses match. The package code was inspected, not executed; its additional random checks were not replayed. The finite census establishes the small-length maxima, not the unrestricted theorem.

## originality

PASS

Best-of-knowledge pass for the explicit four-parameter sentinel transform and its extremal and distributional consequences, not for BWT construction or reversal asymmetry in general.

## value

PASS

The output run count controls compressed-index size. The simplest alternating inputs with two runs of each letter already have a nontrivial and exactly characterized expansion and reversal effect. The normal form supplies a short symbolic calculation for arbitrary run lengths; the extremizer series and 8/9 limit describe typical as well as worst-case behavior without treating the small census as a general result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
