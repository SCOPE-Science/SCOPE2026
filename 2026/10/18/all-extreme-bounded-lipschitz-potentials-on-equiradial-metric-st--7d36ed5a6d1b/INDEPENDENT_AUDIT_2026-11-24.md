# Independent mathematical audit

## correctness

PASS

On the finite real equal-arm star the triangle inequality makes the edge maximum the Lipschitz seminorm. The box/edge lift has exactly one lift over every unit-sphere point, so extremality is equivalent there. At 0<t<1 each leaf supplies at least one active row; eliminating the leaf variables leaves two independent equations in the center and t. With an active center bound these require an opposite-sign double-saturated leaf and 2t=rho(1-t); without it the two double saturations must have opposite signs and give center zero and t=rho(1-t). Every allowed leaf must then be an endpoint, and these active systems conversely have full rank. The t=0 projection is interior and t=1 gives the two constants as endpoint vertices. This gives 3*2^m-2 vertices, all exposed. For facets, on the dense open set with unique maximizing signed coordinate and edge, the center and nonincident leaf winners must have sign opposite the edge, while an incident leaf must have the same sign. Thus by continuity the maximum of the retained forms is the norm everywhere, even at parameter values where excluded forms might coincide. The three strict witnesses at lines 90–92 verify a distinct facet for each retained form after rescaling; there are 2m(m+1). Maximizing over mixed signs loses twice the smallest magnitude only when all coefficients share one strict sign, proving the support formula, including zeros and nonzero total mass. This is a proof check for all stated m and rho, not a computation-based generalization. The frozen verify.py and VERIFICATION.md were inspected, not executed; the finite hull/LP checks are supplemental.

## originality

PASS

The distinct result supported here is the explicit simultaneous vertex classification and irredundant facet classification for every positive common arm length. The general finite-metric halfspaces are known, and the same-day heterogeneous-star formula already covers the all-mass norm as a mathematical specialization. No separate priority is credited for the all-mass value itself or for the previously known zero-mass formula; the sign-support expression is a consequence of the vertex result. The inspected statements do not resolve the face census. This is a best-of-knowledge assessment, not a priority certification.

## value

PASS

The face census identifies both the actual extremizing potentials and the minimal linear constraints for a natural real norm, uniformly over dimension and metric scale, rather than adding another LP for an already computable value. The three sign families explain the exponential vertex count alongside quadratic facet count and recover a compact support formula for arbitrary masses. The value rests on this structural classification, not on independent priority for norm evaluation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
