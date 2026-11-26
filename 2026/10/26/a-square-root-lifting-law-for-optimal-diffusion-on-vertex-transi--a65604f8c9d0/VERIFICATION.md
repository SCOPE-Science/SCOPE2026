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

The Rayleigh minimum on the fixed orthogonal complement of constants is concave in all edge weights. Averaging over lifted core automorphisms and independent leaf permutations preserves cost and yields equal leaf weights with no loss, even against arbitrary asymmetric competitors. With equal y, the leaf-difference modes have eigenvalue y, while each core mode of eigenvalue a gives the 2×2 block with diagonal a+qy,y and off-diagonal -sqrt(q)y. For a>0 the smaller eigenvalue lies in (0,y) and increases strictly with a (its eigenvector has nonzero core component). Disconnected designs have zero gap. For a target r>0, the Schur complement at the core gap gives exactly y>r and a≥r(q+1+qr/(y-r)). Homogeneity gives the sharp lower cost a/β, attained by scaling any unit-cost base optimizer. With u=y/r, the remaining tradeoff is between q/[β(u-1)] and Nqd(u-1). Their product is q²Nd/β, so their sum has minimum 2q sqrt(Nd/β) exactly at u-1=1/sqrt(βNd). This proves the displayed total cost, attainment, and uniqueness of the scalar split among uniform-leaf optimizers. The cycle and prism formulas follow from their elementary spectra; s≥5 distinguishes the prism cycle edges from rungs by the number of 4-cycles they lie in. The supplied Python computes full eigenspectra but its numerical comparisons test only eig[1], not every eigenvalue. Those samples are supplementary and were not rerun.

## originality

PASS

Credit the earlier sunlet optimum, the known fastest-mixing variational framework and the corona spectral mechanism. The evidence supports the distinct general lifting statement: any leaf multiplicity, vertex-transitive cores with multiple invariant cost orbits, and an exact scalar reduction through β with unrestricted competitors. This is a bounded best-of-knowledge judgment, not publication priority certification.

## value

PASS

The theorem solves a natural continuous-time diffusion design problem, reducing a new optimization on the decorated graph to one base invariant plus a closed-form allocation. It certifies global optimality even against asymmetric competitors and preserves practicality when distinct edge orbits carry different prices; it is not just evaluation of a fixed-weight spectrum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
