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

# Verification and exact scope

The proved claim is maximal **convex** spaceability, namely containment of a **closed convex** witness carrying continuum many independent copulas, for each exact Hausdorff support dimension \(s\in(1,2)\). It is not usual linear-subspace spaceability.

**Actual reproducible check:** run `python CHECK.py` in the same directory. The standalone Python 3 checker was executed from its actual file path; its status was `PASS`. It verifies positivity and normalization of the five weights, uniform marginal strip probabilities, multiple numerical Moran roots strictly between one and two, and nonzero determinants of finite exact-rational Vandermonde matrices, both before and after adding a common anchor. It does not enumerate all real parameters or infinite sample spaces.

**Decisive analytic checks:** coordinate projection of the invariant IFS is the unique length-weighted interval IFS, so both margins are uniform. Positivity of all five branch weights gives full support on the attractor; the open set condition yields its exact Hausdorff dimension. For every finite distinct parameter set, evaluating zero finite linear combinations on the nested lower-left squares gives a Vandermonde system. Weak limits of copula measures preserve concentration on the fixed closed attractor; the inequality \(\mu\ge\eta\mu_0\) passes to the limit using nonnegative continuous test functions, and ensures equality of supports. Subtraction of the common anchor after evaluating a finite relation at \((1,1)\) preserves independence. Together these analytic arguments, not finite computation, establish the universal theorem.

**Unproved limits:** no theorem is asserted at support dimensions one or two, for arbitrary prescribed compact supports, or for a closed linear subspace of copulas. Priority against unpublished or unindexed independent work is not certified; independent scientific audit has not been performed.
