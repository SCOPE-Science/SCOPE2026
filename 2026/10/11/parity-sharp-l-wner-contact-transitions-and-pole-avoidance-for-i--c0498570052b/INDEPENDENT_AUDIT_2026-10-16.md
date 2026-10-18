# Independent mathematical audit

## correctness

PASS

Reconstructed all vertices ±w_S via active box/difference constraints (strict δ domain), symmetry reduction to H=hh^T and J=I-H, John facet constraints (u+(d-1)v)/d<=1 and 2v<=δ². For Löwner, vertex orbit projections are A_k=d(1-δ+δk/d)^2 and B_k=δ²k(d-k)/d. Dominance of k<ceil(d/2) reduces constraints; concavity of log t+(d-1)log s gives unique optimum and strict s>t. As function of k, A_k t+B_k s is a strictly concave quadratic, so 1 or 2 adjacent maximizers; stationary KKT yields exact candidate enumeration. Checked initial τ_d condition through next-layer inequality and δ>=d-√d as necessary/sufficient pole contact. Independently enumerated KKT rational solutions/contact layers and d*t<1 for d>=4 in 120 cases d=2..21 and six rational δ; original finite verifier reports 348 cases d=2..30. All-d proof rests on inequalities, not finite cases.

## originality

PASS

Compared statements with full-text early construction and two later de la Puente–Clavería papers for this exact polytope. Their results concern face structure, Euclidean/dual volumes and Mahler product; they do not furnish John/Löwner optimal shape or Hamming contact phase changes. Related earlier exact minimum Euclidean enclosing sphere is strictly weaker: Euclidean sphere poles differ from minimum-volume ellipsoid contacts.

## value

PASS

The same natural one-parameter alcoved polytope has a nontrivial two-eigenvalue extremal ellipsoid with exact parity-dependent contact transition and high-dimensional pole avoidance, not predictable from volume or minimum-radius sphere. Finite KKT enumeration gives a reproducible exact closed determination for every d and δ without hidden numerical optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
