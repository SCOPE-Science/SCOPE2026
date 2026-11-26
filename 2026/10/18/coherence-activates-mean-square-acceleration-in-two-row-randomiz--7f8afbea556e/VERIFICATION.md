---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The two reflecting projections in bisector coordinates have diagonals q=(1−c)/2, r=(1+c)/2 and opposite off-diagonals. Independence gives the exact two-conjugation covariance average, splitting into even and odd symmetric dimensions six and four. I recomputed the symbolic blocks from conjugation of the symmetric basis, their full M=0 characteristic polynomials, both first derivatives and the exact even quadratic coefficient. For fixed c>0 the isolated leading even root L has the stated negative derivative; the zero-momentum initial projection is proportional to q e₁²+r e₂² and is bounded below on the unit circle, and the squared-error observable is positive on the leading right eigenmatrix. Thus the asymptotic root rate persists for every nonzero deterministic zero-velocity start for sufficiently small M. For orthogonal rows the scalar history cubic changes sign between t=1/2 and large t for every M>0. The brief observability argument in the frozen text can be made explicit: the normalized left eigenvector for a root t>1/2 pairs with the initial scalar history (1,1,1) as (t²−M²t+M³)/[t(t+M)]>0, since M⁴−4M³<0 on 0<M≤1; its right eigenvector has nonzero first component by the last two recurrence equations. Near (0,0) the even branch is analytic and strictly convex in M, with first derivative −2c²+O(c⁴) at zero and second-order coefficient 1+O(c²). The implicit-function critical point is c²+O(c⁴), giving gain c⁴+O(c⁶). There the odd branch is lower by c²+O(c⁴) and all other eigenvalues tend to zero. The strict orthogonal gap away from M=0 on compact subintervals of [0,1] confines all small-c global minimizers to the even convexity neighborhood. Since the radius is at least this branch and equals it at the critical point, the optimizer is unique globally. Replay: python /workspace/branches/independent_replay.py 4.

## originality

PASS

The supported novelty is the exact nonzero-coherence mean-square derivative, the resulting genuine small-momentum acceleration for every fixed positive overlap, and the unique global weak-overlap optimizer law. The algorithm and the idea that coherent data may benefit from momentum are both prior. In particular, Online Signal Recovery via Heavy Ball Kaczmarz (arXiv:2211.06391) is a material same-algorithm antecedent missing from the frozen bibliography. Its coherence experiments and sufficient mean-square convergence guarantee do not give the claimed exact comparison or optimizer. The pass is not a priority claim for the algorithm, qualitative acceleration idea or orthogonal stability frontier.

## value

PASS

This resolves an exact mean-square rate benchmark in the smallest nonorthogonal full-rank system and distinguishes strict acceleration from mere stability or acceleration of the signed mean. Orthogonality and any fixed positive overlap have opposite small-momentum behavior. The fourth-order gain is meaningful because it quantifies the onset of a mechanism, and the global weak-overlap uniqueness and quadratic tuning law rule out a better remote momentum in that regime rather than giving a numerical local optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
