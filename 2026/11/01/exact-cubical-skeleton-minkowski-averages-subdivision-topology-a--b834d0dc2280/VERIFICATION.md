---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

In any orthotope closed k-skeleton, each summand has at most k nonendpoint coordinates. An averaged off-grid coordinate needs at least one interior slot, giving the <=mk necessity. Conversely assign each off-grid coordinate to one of mk slots of m summands, at most k per summand, and use its sole free interval together with m−1 endpoint signs: the m intervals of length 2a_i/m tile the whole coordinate range. All on-grid coordinates use only endpoints; thus the exact set is the mk-skeleton of the m-subdivision for mk<d, and equals Q at mk>=d. For any coordinate ℓ_p metric, rounding the r=d−min(mk,d) least costly coordinate grid deviations yields the exact point distance; cell midpoints attain simultaneously the maxima a_i/m, proving formulas for p finite and infinity. The cubical t-skeleton of the contractible cubical d-ball is (t−1)-connected, and a finite (t−1)-connected t-complex is a wedge of t-spheres; Euler characteristic f_j=binom(d,j)m^j(m+1)^(d−j) gives exactly the claimed integer beta. The k=0, p=infinity and threshold boundary are addressed. Independently enumerated exact small lattice sums in five cases; these finite tests supplement, not replace, the general constructive proof.

## originality

PASS

Best-of-knowledge PASS: prior simplex skeleton threshold numerically coincides, but it acts on simplices and states neither exact grid subcomplex nor all-order metric/topology of orthotopes. General convergence/threshold bounds do not imply this shape-specific identity, which was not found in exact cubical skeleton searches.

## value

PASS

PASS: a natural entire family of nonconvex k-skeleta gets a complete geometry-to-topology phase diagram, with exact intermediate sets, anisotropic sharp Hausdorff errors and integral Betti multiplicities, not merely a generic convergence bound. The cubical independence is mathematically structural rather than arbitrary parameter slicing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
