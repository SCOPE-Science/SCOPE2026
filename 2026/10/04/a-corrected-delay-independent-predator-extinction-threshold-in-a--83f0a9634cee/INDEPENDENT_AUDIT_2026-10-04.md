# Independent mathematical audit

## correctness

PASS

The source's printed adult-predator upper bound is false because it omits the positive delayed maturation term c2 P2(t-tau2); the stated source parameters give exact values 0.68 versus 0.48. The corrected theorem follows from logistic control of prey, the inequalities P2'<=A_eps P3-qP2 and the exact adult equation, and the Lyapunov-Krasovskii functional L=P2+alpha P3+alpha c2 integral P2. Choosing A_eps/d3<alpha<q/c2 makes L' a strictly negative combination of P2, P3 and P3^2. Integrability plus bounded derivatives gives predator extinction, then scalar comparison gives P1->K. A fresh symbolic check reproduced the derivative cancellation.

## originality

PASS

The exact source contains the incorrect preliminary inequality and a Figure-3 stable coexistence equilibrium incompatible with the printed limiting formula. Related stage-structured predator-prey papers establish reproduction-threshold methodology in different maturation systems, but no inspected source states this model's corrected R_P threshold or Lyapunov-Krasovskii functional. Current Resultary search produced no same-result prior finding.

## value

PASS

The result corrects a concrete invalid argument and false limiting formula in a published delay model, while replacing them with a rigorous delay-independent criterion that is strictly less restrictive than the source's surviving qualitative condition. This is a useful source-specific stability correction with an exact parameter witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
