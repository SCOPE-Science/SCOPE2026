---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For every n>=4 and algebraically closed k in any characteristic, source correctly uses normal fan of the even-parity binary polytope P_n in its even-sum lattice L_n (dual Z^n+Z(1/2,...,1/2)), not the ambient Z^n lattice. Even cut-edge supports characterize vertices; coordinate flips by even subsets act transitively. At vertex 0 the 2n tight facets give primitive normals u_i=-e_i and v_i=e_i-h. Classifying all intersections by selected coordinate facets A and singleton parity facets B shows all faces of dimension >=2 have saturated simplicial normal cones; each edge [0,e_i+e_j] has an (n-1)-cone with n rays v_i,v_j,u_k for k outside {i,j}, unique circuit v_i+v_j=sum u_k, hence nonregular. Every singular orbit belongs to an edge-curve closure; counts are 2^(n-2) binom(n,2) curves P1 and binom(n,2) through each of 2^(n-1) fixed points. The dual semigroup for each edge cone is Z plus the nonnegative integral tuples (a,b,c_1,...,c_{n-2}) with a+b=sum c; it is the rank-one 2x(n-2) Segre semigroup. Hence the affine chart is Gm times that cone, transverse multiplicity n-2, non-Q-factorial; n>=5 non-Q-Gorenstein by circuit height discrepancy 2!=n-2. n=4 Gorenstein follows from height-one support vector. An independently constructed parity vertex and Hamming-edge count for 4<=n<=8 corroborates edge totals 24,80,240,672,1792, not the infinite proof.

## originality

PASS

The new portion is all-length singular-curve, incidence and Segre transverse-ring classification; standard cut-polytope facet inequalities, graph smoothness criterion, normality and Gorenstein cutoff are acknowledged premises.

## value

PASS

Cycle cut models are canonical normal projective toric models. An exact whole-singular-locus description in every dimension, exponential number of rational-curve components and their fixed-point incidences, and a uniform transverse 2x(n-2) determinantal germ with multiplicity and a Q-Gorenstein boundary are natural, useful geometric invariants beyond known binary smoothness conditions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
