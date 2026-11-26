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

In characteristic 3 the partials e2−x_i e1+x_i² constrain coordinates to at most two values. For distinct a,b the two gradient conditions are equivalent to e1=a+b and e2=ab, and give (|S|−1)a=(|Sᶜ|−1)b=0 by the first two power sums. With one zero value, the nonzero support r is 1 mod 3 and the additional equation binom(r,3)=0 cuts it down to 1 mod 9. The all-equal nonzero case requires n≡1 or 2 mod 9. With two nonzero values, block sizes 1+3u and 1+3v give cubic u a³+v b³ by the degree-three coefficient of the block product. Equal nonzero residues yield the signed points; opposite nonzero residues force a=b; a single nonzero residue cannot give two nonzero values; both zero give entire partition lines. This exhausts geometric support and gives the counts and concurrence by unordered bipartitions. The homogeneous Hessian has off-diagonal entry e1−x_i−x_j and zero diagonal: its split blocks have rank n−1 for the node residues and n−2 at the other isolated points and along the distinct-value line locus. Dividing the radial direction out on a projective chart, rank n−1 gives a reduced ordinary double point. Rank n−2 gives gradient tangent dimension one; a two-block projective line lies in the gradient scheme through the point, forcing the local ring to be regular of dimension one and the line to be the whole local scheme there. Restriction of e3 is a nonzero cube at the isolated support, of length three, and identically zero at the generic line points, giving generic reducedness. This does not decide the scheme at the common diagonal in the line regime. Multilinearity partitions variables in any factorization; homogeneous factors would fix the number drawn from either side in every monomial, contradicted by exchanging a cross-part pair while keeping two other indices. Normality then follows by S2 and singular codimension at least two, including the first line case n=11. `python3 /workspace/branches/independent_checks.py 4` checked weighted projective F3 multiplicity types via block coefficient and deletion formulas for 4≤n≤40, reproducing 5, 43, 11, 2731 isolated points at n=5,8,10,14 and 11 and 92398 line components at n=11,20 by the verified point counts 34 and 277195. The finite check corroborates support and counts, not geometric exhaustiveness, Hessian length, or normality; the uploaded checker was not executed.

## originality

PASS

Xie already gives the dimension cutoff, the precise extremal partition lines and their generic reducedness, and the coordinate-axis local rings in the isolated cases. The line count and concurrence follow immediately from those named lines, and normality is routine from integrality and the dimension estimate. The distinct supported increment is the complete geometric support including all noncoordinate strata and exhaustion away from the extremal strata, together with the node/curvilinear classification at every isolated point. A later-dated catalogue record overlaps the complete isolated point census, without deciding the local schemes or earlier priority.

## value

PASS

The local and support invariants refine a previously established dimension transition for a basic symmetric hypersurface. They detect the noncoordinate signed stratum (35 extra points already at n=8), distinguish reduced nodes from a length-three curvilinear singular scheme, and determine the full reduced geometry in the one-dimensional residue. The geometric census is meaningful even given prior dimension and generic coordinate results; the concurrent point's full scheme is not needed for the stated value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
