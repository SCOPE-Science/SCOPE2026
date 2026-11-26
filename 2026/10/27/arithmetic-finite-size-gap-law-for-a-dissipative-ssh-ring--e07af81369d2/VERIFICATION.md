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

For the periodic gap 2 min Re beta, including zero rapidities, the source grid and branch formula have the stated normalization. With u=a+b cos q, v=b sin q, D=u²+(v+ig)², S=u²+v²+g² and Y=|Im sqrt D|, one has S²−|D|²=4g²u² and 2(g−Y)=4g²u²/[(S+|D|)(g+Y)]. All denominators are positive. The only zeros are ±q*, and the quadratic coefficient at either is g(b²−a²)/(b²−a²+g²). The nearest-grid distance is d_N=2π||Nθ||/N. Testing a nearest grid point gives an O(d_N²) upper bound; compactness away from the two zeros and the positive local quadratic lower bound then put every minimizer within O(d_N) of one zero. Bounding the Taylor coefficient there from below, and at a nearest point from above, gives the uniform relative O(N⁻¹) estimate regardless of which grid point minimizes and without dividing by a possible zero. Rational residue cycling, irrational density and convergent-denominator bounds give the exact resonance sizes, upper/lower limits and N⁻⁴ subsequence statements. The badly approximable lower bound follows from inf_N N||Nθ||>0. No finite script is needed for these all-size conclusions; the accompanying samples use the same band formula and are not an independent proof.

## originality

PASS

The exact spectral solution, allowed momenta and thermodynamic closure are prior. The supported distinction is the interior uniform relative finite-size law and its arithmetic consequences; neither the closest model-specific primary source nor the inspected related indexed results supply an equivalent theorem. This is a best-of-knowledge assessment, not priority certification.

## value

PASS

A bulk-closed gap alone cannot distinguish exactly resonant finite rings from positive gaps or describe sporadic anomalies in their decay scale. The result gives both the sharp normalization and a usable size/parameter classification including exact zeros, typical upper envelope, and N⁻⁴ near-resonances, without confusing them with the endpoint quartic band. The value attaches to that predictable finite-size behavior, not to a new band solution or claims about every observable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
