---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Directly reconstructing the Markov-conditioned means yields two 2x2 blocks with dominant exponent -a-q+sqrt(q(q+b)), hence q_1=a²/(b-2a) for b>2a. The symmetric second-moment block M_+ has characteristic constant 2[4a²(a+q)-b²q], strictly positive other Hurwitz conditions, and is irreducible Metzler with positive noise forcing. The antisymmetric M_- remains Hurwitz wherever M_+ is nonpositive/stable, so no hidden earlier instability for general initial states. Its positive simple zero mode at q_2 and positive forcing give linear critical divergence; above q_2 the positive mode grows exponentially. Solving the stationary affine equations gives the stated covariance; its critical ratio is 2a/b. Independent exact symbolic computation reconstructed both cubic coefficients, Hurwitz determinants, stationary u,v,w and q_1-q_2=a²/(b+2a). Numeric eigenvalue checks at a=D=1,b=3,q=.5,.8,.9 agree with stable/critical/unstable sectors. This supports but does not replace the all-positive-parameter Routh-Hurwitz and Perron arguments.

## originality

PASS

Ogura–Preciado (2015) general matrix moment stability criterion covers the test method; Ferraro et al. (2024) already demonstrate qualitative mean finite and variance divergent in a different annealed large-N model; Sturman–Thiffeault analyze discrete products of shears. None of the inspected model/implication statements directly provides BOTH sharp thresholds, stationary covariance and critical ratio for these continuously switching common directed shears. Originality is the exact constrained phase diagram, not general moment instability or matrix criteria.

## value

PASS

A minimal explicit two-dimensional switching model separates first- and second-moment stability and has a fully solvable phase diagram. Exact noise-driven covariance, sharp nonzero interval and subunit critical correlation reveal a structural fluctuation mechanism, not only generic instability existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
