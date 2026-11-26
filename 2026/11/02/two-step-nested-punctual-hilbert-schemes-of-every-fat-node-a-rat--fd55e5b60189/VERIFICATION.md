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

At fixed colength m, every ideal contains the m-th power of the maximal ideal, so the action and its weight decomposition can be checked in a finite truncation. The punctual pair locus is a closed finite-dimensional projective incidence locus. Torus Euler localization reduces its Euler characteristic to the finite set of fixed pairs; distinct monomial weights imply these are exactly monomial ideal pairs. For the larger diagram lambda, the condition is lambda_v<=u in zero-based row indexing, and taking the smaller diagram gives inclusion in the correct direction. Two removed boxes form two original corners, a horizontal domino at a gap of at least two, or a vertical domino at a repeated part size. Those disjoint cases yield the stated unweighted statistic. For exactly r rows longer than u, split off u from each, giving a length-r alpha and a bounded beta. Conjugation identifies alpha with parts <=r and at least one part of size r, preserving corner and two-box deletion counts. The cross term is the product of corner counts, and the only changed horizontal gap is the shortest long row when min(alpha)=1 and max(beta)<=u-1 (including empty beta); the generating term is q^((u+1)r) P_(r-1) P_(u-1). This proves the entire formula, including r=0 with its stated conventions, symmetry by conjugating the original diagrams, cancellation of q^-2 and the denominator bound. At q=1 only the r=v contribution can have order u+v, with coefficient (u+v)(u+v+1)/(2u!v!); other roots of unity lose at least the j=1 factor from each side, giving the stated coefficient asymptotic. An independent implementation enumerating two successive corner deletions and deduplicating endpoints matched 576 coefficients on u,v=1..6, n=0..15, and exact symbolic substitution also verified the displayed (2,2) numerator.

## originality

PASS

The inspected records and primary sources give single-ideal invariants, different flag data, one-box nesting or smooth-surface geometry. They do not state or mechanically yield the unweighted endpoint-incidence series uniformly for all fat-node multiplicities. The qualifying distinction is the two-box deletion series with its cross-boundary correction, not Euler localization, single Hilbert schemes, or claimed priority for reduced-node special cases.

## value

PASS

The unweighted endpoint Euler characteristic answers a natural nested-incidence question not captured by the single-ideal series or full flags. The formula relates both multiplicities to one boundary correction and determines all colengths and the leading growth, rather than just enumerating small examples. It also identifies precisely what information is lost when replacing two-box endpoints by generator numbers or by intermediate chains.

The dated certificate retains the supplied scientific assessment, sources and limitations.
