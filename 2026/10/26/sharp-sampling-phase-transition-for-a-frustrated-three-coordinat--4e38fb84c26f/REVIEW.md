# Independent mathematical audit

## correctness

PASS

The exact objective decrement is (Cx)_i²/2; after a C^(1/2) change of variables the minimax constant is lambda_min(C^(1/2)PC^(1/2)). Concavity in p and swap invariance globally reduce to symmetric p=(u,u,1-2u), not a uniqueness claim for all p. The scaled Hessian decomposes into antisymmetric eigenvalue (1-r)u and the 2x2 symmetric block with smaller eigenvalue ell(u). Its radical discriminant has strictly positive second derivative for c>0, so ell is strictly concave, uniquely maximized at u_s=(1+c)/(3+r+4c). The crossing with the antisymmetric branch occurs at u_b=(r-c²)/(r(3-r)-2c²). Comparing u_s and u_b yields the stated critical quadratic 2c²+(1-r)c-2r=0 and correct two closed-form gamma values. Endpoint gamma=0, C positive definite on stated domain. New independent symbolic identities and 12,500 random-simplex comparisons across 50 parameters passed; numerical tests are not a proof of optimality.

## originality

PASS

Best-of-knowledge originality of the precise stated full theorem: mathematical antecedents and equivalent formulations were compared from real source readings. Standard ingredients are credited and genuine historical coverage risks remain; unsuccessful search is not a novelty proof. Already gives the general semidefinite design optimization formulation; it does not evaluate this frustrated symmetric family or its phase transition in the inspected section. Generic SDP coverage acknowledged without pretending special-case formula is free. Requires C^-1 entrywise nonnegative (even after coordinate sign conjugation); target inverse has three negative off-diagonal entries with negative sign product so that decisive hypothesis is violated. No implication. General optimal-design weights may include a closed-form special case; no full-text negative assertion or unverified uniqueness claim is made.

## value

PASS

Nonuniform randomized coordinate descent is a natural algorithmic design variable. This two-parameter family is the smallest frustrated Hessian whose inverse cannot be sign-gauged entrywise nonnegative; the exact optimizer has a meaningful active-eigenmode phase boundary despite equal diagonal coordinate curvatures, exceeding generic SDP restatement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
