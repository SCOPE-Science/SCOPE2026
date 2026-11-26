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

Centering the window makes every first cosine positive for D<N/2, so such a window cannot have a nonzero nonnegative quadrature. At the odd borderline D=(N+1)/2, the two endpoint cosines are −a with a=sin(π/(2N)), and every interior cosine is at least sin(3π/(2N))>a. The polynomial x(x²−a²) is a linear combination of centered first and third cosines, vanishes at the endpoints and is positive in the interior. Its vanishing weighted sum forces support only at endpoints, which then cannot annihilate the first moment. At D=(N+3)/2 the first three reflected node pairs have levels −b,a,c with 0<a<b<c≤1. Positive masses A,B,C at a,c,−b balance the first and third powers since Aa=ac(c²−b²), Bc=ac(b²−a²) and Cb=ac(c²−a²), and multiplying the first two contributions by a²,c² gives their sum Cb³. Splitting the masses symmetrically kills both sine moments. The central pair at N=5 is correctly combined, and the even minimum follows by antipodal cancellation. The proof respects nonnegative weights, normalized Haar integration on the full circle, and a window containing D+1 candidate nodes; it does not assert Parseval exactness for {0,1,3} or any second-harmonic cancellation. The frozen verifier was inspected, not executed; its reported finite tests are supplementary.

## originality

PASS

The supported distinct claim is the exact odd-grid consecutive aperture for the sparse first-and-third harmonic constraints, with a matching explicit rule. The even case is the standard semicircle/antipodal calculation and is not individually novel. Same-spectrum global polynomial optimization, related continuous support-free arcs, and full-degree or unrestricted-node quadrature results were compared and do not give the odd-grid threshold. Sparse support as an abstract existence bound is also not new by convexity; the formula for the least aperture and the explicit construction are the contribution.

## value

PASS

For the natural window restriction on two low odd Fourier moments, the exact extra grid step in odd order gives information lost in both the continuous semicircle bound and abstract positive quadrature existence. An explicit separating polynomial and positive rule certify both sides for every finite order. The value is in the precisely located obstruction and construction, not a generic sparsity bound or the elementary even case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
