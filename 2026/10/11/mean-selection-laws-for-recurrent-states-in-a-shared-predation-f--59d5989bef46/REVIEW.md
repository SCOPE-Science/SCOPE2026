# Independent mathematical audit

## correctness

PASS

With all parameters positive and μ compactly supported strictly inside the positive octant, log(u1), log(u2), log(v) are bounded C¹ observables on a neighborhood of invariant support. Their invariant integrals give r_i E[(1+k_i v)^−1]−d_i−a_i ū_i−p_i vbar=0 and A1 ū1+A2 ū2=m. The exact reciprocal identity 1/(1+kv)=1/(1+k vbar)−k(v−vbar)/(1+k vbar)^2+k²(v−vbar)²/[(1+k vbar)^2(1+kv)] produces J_i≥0. Subtracting the equilibrium equations gives a_i(ū_i−u_i*)=r_i J_i−(p_i+r_i C_i)(vbar−v*) and the claimed strictly positive denominator quotient. If any J_i=0 then v is constant on invariant support; each prey follows a scalar logistic equation, whose only complete orbit confined to a compact positive interval is its equilibrium, so uniqueness of the positive equilibrium gives μ=δ_E*. Thus nontrivial μ has J_i>0 and vbar>v*. If k1=k2, the quotient/J is a positive weighted mean of q_i=r_i/(p_i+r_i C), and q1−q2 has sign r1 p2−r2 p1, proving opposite prey-shift sorting. An independent SymPy check verified the reciprocal identity; reviewed supplied verification/check.py. Nothing asserts that nontrivial compact interior recurrence actually exists.

## originality

PASS

Best-of-knowledge original model-specific conditional measure theorem. The full 21-page Wang–Smit article specifies exactly the linear-response vector field and proves coexistence equilibrium existence and local stability (Theorems 3.6–3.7), while Remark 1 explicitly leaves global stability as conjecture; it does not present the J_i Jensen-defect formula or equal-fear sign sorting. Published Resultary analogues concern different predator–prey systems or discrete fear maps, not this exact vector field and identities. Abrams–Holt–Roth (1998) is highly relevant conceptually on mean population densities in cycling shared predation; only its abstract was accessible despite lawful attempts, so the unresolved text-level priority risk remains explicit and does not by itself invalidate originality.

## value

PASS

An exact finite-amplitude predator mean uplift law and equal-fear prey shift direction across arbitrary compact invariant statistical states are mathematically meaningful constraints on recurrent dynamics for a specific open-stability ecological model. The formulas expose how nonlinear fear curvature enters and could constrain potential periodic/ergodic states without assuming small amplitude. This is more than a textbook equilibrium restatement despite being conditional; no assertion of actual non-equilibrium recurrence is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
