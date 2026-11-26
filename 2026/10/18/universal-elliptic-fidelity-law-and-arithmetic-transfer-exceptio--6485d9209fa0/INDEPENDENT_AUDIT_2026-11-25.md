# Independent mathematical audit

## correctness

PASS

Frozen claim: the bounded bipartite Hamiltonian has A-sector H² diagonal 4J² and cancellations across odd plaquettes; even powers give the exact dimer cosine propagator with the displayed frequencies. For irrational ratio the nonconstant torus characters have zero time averages. The sum/difference integer torus covering preserves Haar measure, and the independent arcsine product, change of variables and K expansion give the displayed law and tail. For rationals, coprimality gives opposite-parity exact tuning; the phase-target distances give the stated nonsharp odd–odd cap, including the no-coupling endpoint. Independent bounded reproduction (python3 /workspace/audit_checks.py, check 5) used the cosine difference directly: second fidelity moment 9/64 and at infidelity tolerance 0.2, torus-grid fraction 0.069105 vs elliptic quadrature 0.069066. No uploaded executable was run. Repaired claim: for 1/√3≤p/q<1 odd–odd, q>p≥3. For either ordering of the cosines the two opposite-parity targets differ by an odd integer in the lifted resonance relation, hence the unsigned errors satisfy qa+pb≥π. Radial shrinking to equality improves their cosine sum. The converse is essential: Bézout gives qu−pv=1, and shifting (u,v) by (p,q) makes u even and v odd. Each equality pair is then realized by consistent phases pθ=πu−a and qθ=πv+b, with nonnegative time by periodicity. The segment lies in [0,π/3]², so the cosine sum is strictly concave with inward first derivatives at both endpoints; p sin a=q sin b has a unique positive solution there. The squared-length minimum on the segment is π²/(p²+q²), and the Taylor remainder is uniformly O(q⁻⁴) on it, which sandwiches the optimum from both sides. For p=q=1 the exact probability is zero. Ran the authored replacement checker with cd /workspace/repairs/5 && python3 verify.py; it passed 11 odd–odd pairs and the endpoint. These finite checks are corroborative; the exact maximum and uniform error follow from the proof.

## originality

PASS

PASS for the repaired quantitative odd–odd claim only. The frozen centerpiece fails originality: Li et al. give the very same two-cosine amplitude and exact-transfer condition. Torus equidistribution of that amplitude gives exactly the square of the published square-lattice structure-function law; alternatively the displayed density and small-threshold Taylor expansion follow by direct specialization of Dunkl's two-beta formula. The irrational recurrence and qualitative rational failure are also direct consequences of the known phases. None of that is retained as novel. What survives is the actual best obstructed transfer probability, characterized by an attained, optimal mismatch allocation, and the uniform leading infidelity coefficient. The old nonsharp bound supplies the obstruction but not attainment or the exact optimum. No inspected antecedent gives the repaired unweighted optimum; the closest indexed optimization solves a different support/weighting problem.

## value

PASS

For the repaired claim, an odd–odd static cell has an otherwise undetermined attainable fidelity threshold. The exact maximum, an attainable phase construction, and its leading suppression for large denominator make the quantitative obstruction usable; a nonsharp upper bound or an existence-only theorem cannot decide which thresholds below that bound are achievable. The scale is uniform in the physically allowed ratio interval, not a single arbitrary rational point. The mechanism is exact for the ideal resonance and is not advertised as tolerance under noise or as a near-irrational finite-waiting-time law. No separate value is assigned to rediscovering the known distribution as a frozen novelty claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
