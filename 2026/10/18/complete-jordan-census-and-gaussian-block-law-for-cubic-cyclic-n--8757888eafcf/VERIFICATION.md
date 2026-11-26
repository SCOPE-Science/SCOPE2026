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

With the stipulated left-to-right concatenation, left multiplication preserves terminal vertex. In the basis e_(i+2), a_(i+1), b_i the only possibly nonzero entries are x_(i+1), y_i, x_i below the diagonal, and the square has single possibly nonzero entry x_i x_(i+1). A nonzero square forces a size-three block, the zero matrix forces three size-one blocks, and all other cases have one size-two and one size-one block. Charge each nonzero x_i once on its outgoing support edge; independently summing y_i gives the four transfer entries, with the trace counting labeled cyclic sequences exactly once. The normalization is q^(2n); a proper run of a+1 nonzero x_i realizes exactly a adjacent pairs for 0<=a<=n-2, and any zero destroys at least two edges. The no-size-three event is a weighted cycle independent-set count; the eigenvalues are the roots of lambda²-lambda-(q-1), with |lambda_-|<lambda_+<q for q>=2. For covariance the single-site means are p² and r³, each same-type neighbor has joint expectation p³ or r⁵ respectively, and there are three disjoint-in-value overlapping cross terms per site, including at n=3. All other windows depend on disjoint underlying variables. This gives the stated matrix and determinant p³r⁴(r+4). After removing the seam and one site between consecutive blocks of length floor(n^(1/3)), retained scalar directional block sums are independent and uniformly o(sqrt n). The discarded variance is O(n^(2/3)) by finite dependence, so Lindeberg and Cramér–Wold give the claimed fixed-q limit. There is no rate claim. Independent exact rank and census replay on all elements at (q,n)=(2,3),(2,5),(4,3), using GF(4) arithmetic for the last case, also compared the cross-covariance and checked the determinant symbolically (python3 /workspace/branches/independent_replay.py 5). The frozen prime-field verifier was inspected, not executed. Neither replay proves the general limit.

## originality

PASS

A distinct later catalog report gives the same entire finite-field census and is stronger on support and motivic strata; the exact census overlap is credited, not treated as a novel change of variables. The visible dates are not a priority determination. Within inspected prior literature no statement gives this finite-field specialization and the explicit exact covariance and nondegenerate joint fluctuation law. The latter is an evaluated statistical refinement not stated by the overlapping report or the cited general limit methods. No novelty is assigned to the transfer technique or finite-dependence CLT themselves, nor to the square-zero count apart from its explicit evaluation in this family.

## value

PASS

The regular action's finite-field Jordan partition is a natural invariant of this constrained family. The exact narrow census is also available in the later catalog record, but the evaluated joint statistics provide a useful additional description: exact finite means and cross-covariance, strictly positive determinant, and a normal law governing the full block-count vector at fixed q. The negative covariance and the explicit cubic-radical block parameters come from the overlapping windows, not from unrestricted triangular ensembles. The value is this concrete statistical refinement of a natural algebraic invariant, not a claim of a general CLT or of a convergence rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
