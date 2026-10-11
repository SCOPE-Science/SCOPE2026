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
# Verification

The accepted theorem is proved symbolically; no finite computation is used as proof.

The primary full text was inspected at the exact points needed for the argument. Lemma 7.2 supplies a finite good triangulation subordinate to isotropy strata. Corollary 8.5 lists the only possible minimum ranks in dimension five. Proposition 8.7 gives a regular bundle of rank \(4\gcd(4,e_5(M))\). Proposition 9.3 supplies the smooth rank-four both-stabilizer example and the mapping-torus suborbifold that rules out rank two. Question 10.2 explicitly leaves the nonorientable sharp bound open.

For the new top-cohomology step, write the top cellular cochain group on the coarse triangulation. A codimension-one simplex has one or two top cofaces. Its coboundary therefore has either one unit coefficient or two unit coefficients. On each component of the resulting signed adjacency graph, the two-term relations reduce all top generators to one generator up to sign. A one-term relation kills that generator; otherwise a sign-consistent component contributes \(\mathbb Z\), and a sign-inconsistent component contributes exactly \(\mathbb Z/2\). Thus
\[
H^5(M;\mathbb Z)\cong \mathbb Z^a\oplus(\mathbb Z/2)^b,
\]
so \(e_5(M)\le2\).

The lower-bound example is checked locally at free points. Removing a small free ball from the source's oriented example and a ball from \(\mathbb{RP}^4\times S^1\) changes no stabilizer data outside those balls. The mapping-torus obstruction lies away from the chosen ball and persists. The rank-four bundle is trivial over the removed ball and therefore glues to a trivial rank-four bundle on the punctured ordinary manifold.

Limit: this verification proves only \(4\le B\le8\) for the sharp nonorientable both-stabilizer bound. It does not exhibit a smooth orbifold whose minimum regular rank is \(8\).
