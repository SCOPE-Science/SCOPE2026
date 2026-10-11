# Independent mathematical audit

## correctness

PASS

The sequential solves give trace (2+2t-kappa^2 t^2)/(1+t)^2 and determinant 1/(1+t)^2. Jury conditions reduce to 4+4t+(1-kappa^2)t^2>0, yielding all-step stability for kappa<=1 and t<2/(kappa-1) for kappa>1, with multiplier -1 at equality. The discriminant is kappa^2 t^2[kappa^2 t^2-4(1+t)]/(1+t)^4, giving the unique collision t_star. Before it the radius is 1/(1+t); after it the dominant negative root increases, so t_star is the unique rate minimizer. The simultaneous resolvent has factor 1/sqrt((1+t)^2+kappa^2 t^2), strictly decreasing for all t>0.

## originality

PASS

Originality passes. The focal source defines the staggered implicit update and proves convergence under sufficient parameter rules, while Ouyang likewise gives sufficient alternating-proximity conditions. No inspected theorem gives this exact necessary-and-sufficient scalar coupling frontier together with the unique rate-optimal discriminant collision.

## value

PASS

This gives a sharp boundary between full-resolvent stability and staggered block implicitness, plus the exact fastest step. Both are natural calibration facts for a current minimax method and explain why the word implicit does not guarantee unconditional stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
