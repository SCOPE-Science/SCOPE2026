---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For Haar random plane normal, x=|U·e_3| is uniform [0,1] and y=sqrt(1−x²); orthogonal cylinder shadow is ellipse of axes r,rx Minkowski-added to an axial segment length hy, hence A=πr²x+2rhy, P=4rE(1−x²)+2hy. Beta integrals yield E[x]=1/2, E[y]=π/4, E[xy]=1/3, E[y²]=2/3; exchanging elliptic integrals yields E[E]=π²/8 and E[xE]=2/3; weighted I=E[yE]. These reconstruct E[AP]=(8π/3)r³+(2π/3+8I)r²h+(8/3)rh² and the covariance quadratic r³[4C(h/r)²+B(h/r)+4πC]. The 144-term rational hypergeometric truncation plus tail and Machin arctangent enclosure gives 0.930<I<0.933, C>0.0498, −0.69<B<−0.65, B²<(0.69)²<64(3.14)(0.0498)²<64πC²; discriminant negative with C>0 and vertex h/r=−B/(8C)>0. Independent high-precision integral gives I≈0.9318171570247627, minimizer≈1.68126868048556, minimum≈0.06275436161117 r³; finite polygonal tests are only geometric sanity checks, not universal proof.

## originality

PASS

Finch computes random projection mixed geometric moments for selected regular polyhedra, and a weighted elliptic integral also occurs there. That prior integral itself is covered. Its cubical results and projection-volume distribution theorems do not imply the right-cylinder mixed AP moment or strict covariance quadratic for all positive aspects. New science is the shape-wide sign and sharp interior optimizer, subject to literature residuals.

## value

PASS

Area–perimeter correlation of random shadows can vary across bodies (the Finch polyhedral comparisons motivate the sign question); proving a strictly positive covariance for every member of the natural continuous family of right circular cylinders and locating its unique optimal aspect ratio is a meaningful exact convex-geometric benchmark. A rational discriminant certificate gives information beyond tabulating two separate expected values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
