# Independent mathematical audit

## correctness

PASS

Direct first-step conditioning gives H_{0,k}-H_{0,k-1}=d_k/(qm) and H_{1,k+1}-H_{1,k}=qd_k/m, where d_k=H_{1,k}-H_{0,k}; these are valid at the endpoint k=m and k=0 of their respective ranges. Thus d_{k+1}/d_k=R_m(q), and the two unanimous boundaries give d_0=1/Z_m(q). Absorption is almost sure on the finite connected star with both acceptances positive, so this harmonic solution is unique. Uniform seeding weights the center once and leaves m times. The Riemann sum with m log R_m(q) tending to q-1/q yields the positive constant C(q); it is uniform in the summation variable for fixed q. For q_n=1+λ/n, m log R_m(q_n) tends to zero, so the terms tend uniformly to one and Z_m tends to two. The clique has constant down/up ratio q and gambler's ruin gives its stated fixed- and weak-bias limits. Neutrality gives H_{0,k}=k/(2m) and H_{1,k}=1/2+k/(2m), hence uniform probability 1/n, including λ=0. The exact-fraction verifier was inspected, not needed to extend the proof to arbitrary m.

## originality

PASS

Credit the adoption rule, clique formula and equivalent biased-voter jump mechanism as prior. The checked earlier sources do not give or mechanically imply the arbitrary-bias exact harmonic function on the star. Its exact overlap with a separately indexed later Resultary item is explicit below; the finding is credited only for the star specialization and its consequences, not for an exclusive priority claim.

## value

PASS

This solves fixation at every starting state on a canonical heterogeneous graph, rather than supplying a particular-size simulation or just rederiving the clique result. It quantifies a qualitative effect under the same copying rule: a fixed favorable bias gives order 1/n instead of order one on a star, and a fixed unfavorable bias gives order 1/n instead of exponential suppression. Exact hub-versus-leaf initialization and the weak-bias scale make the result useful without asserting extremality among graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
