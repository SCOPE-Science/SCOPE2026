# Independent mathematical audit

## correctness

PASS

I checked the published system (2), conditions (5)–(6), and the definitions of M_i and R_i. The published dimensional restriction θ_i<α_i gives c_i<p_i because the two scales share the positive factor K_i/d. For M=n+∑a_i and q_i=Mp_i/a_i, (5) puts q_i in (0,1). Then c_iR_i≤c_i(1−q_i)/2<p_i(1−q_i)/2=(a_i/2M)q_i(1−q_i)≤a_i/(8M). Strictness follows from 1−q_i>0 and does not require a sign argument on H_i or the trajectory. Summing gives ∑c_iR_i<(∑a_i)/(8M)<1/8 for n≥1, while (6) demands >1+∑b_i>1. The final printed differential inequality, if its positive constant were attainable, would force growth incompatible with Theorem 1, but that is not needed for the contradiction. This is vacuity, not a counterexample with feasible hypotheses or a claim ruling out permanence. VERIFICATION.md and verify.py were inspected, not executed; the rational examples and quadratic identity checks do not prove more than the universal analytic argument.

## originality

PASS

The distinct claim is that the printed hypotheses of this particular permanence theorem cannot be satisfied. The proof uses an elementary scalar bound, but the actual exact-source match in the catalogue treats a different theorem and leaves this incompatibility unaddressed.

## value

PASS

The paper offers the permanence test as a substantive result, yet not one parameter vector in the stated model can use it. A uniform cap that is separated from the required threshold exposes this limitation without mistaking it for nonpermanence of the actual dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
