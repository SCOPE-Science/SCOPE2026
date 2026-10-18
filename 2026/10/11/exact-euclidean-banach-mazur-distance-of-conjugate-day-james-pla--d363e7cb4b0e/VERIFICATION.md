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

Coordinate swap averaging reduces all positive-definite forms to H_rho²=x²+y²+2rho xy. Hölder duality on the mixed conjugate quadrants shows normalized determinant antinorm equals N_p; the Euclidean antinorm of H_rho yields m_rho*M_rho=1/(1-rho²). On same-sign quadrant R=(1+t^p)^(2/p)/(1+t²+2rho t); f_p(t)=t(1-t^(p-2))/(1-t^p) increases from 0 to alpha. The strictly increasing G_p(s)=(1-s^(p-1))/[(1-s)(1+s^p)^alpha] crosses 2^alpha once, and same/opposite maxima equioscillate there. The source explicitly controls derivatives on either side and rho outside (-alpha,0), proving the global minimax, including p=4 value 6-2sqrt(6). Independent evaluations of balance/branch derivatives checked at several p but do not prove all p.

## originality

PASS

Best-of-knowledge original specific claim after object/implication comparisons against accessible primary texts; unavailable Resultary is explicitly NOT a negative search or originality proof. Martini–Swanepoel explicitly describe the same conjugate mixed quadrant norm as a Radon plane, while Alonso defines the Day–James presentation. The Radon antinorm identity alone relates extrema but does not state or compute their minimizing rho_p. The known p=3 value 2^(5/3)/3 specializes the new formula; one parameter point cannot imply the continuous p>2 optimization. A general self-duality theorem gives no numerical minimizer without the nontrivial balancing calculation.

## value

PASS

The conjugate family is a classical one-parameter family of self-antinorm (Radon) planes. The complete exact Euclidean-distance profile, unique scalar balance and analytic optimal-ellipse correlation illuminate a reusable duality/equioscillation phenomenon, and strictly extend a previously recorded p=3 special value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
