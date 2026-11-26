# Independent mathematical audit

## correctness

PASS

The canonical weight for occupancies 0, 1, 2 is proportional to (t,1+t,1). As an independent check, put A_b=[b]_t and B_b=1+t−A_b; the adjacent weight ratios give incoming clockwise flux divided by the destination weight equal to B_b A_c at a bond (b,c), versus outgoing A_b B_c. Their difference telescopes on the ring, as does the reversed contribution. Positivity and connectivity give the stationary law also at q=0. At fixed mass, the configuration weights vary with M only through z^M. The identity V=n/L+2E[M]/L−(n/L)² gives derivative 2Var(M)/L with respect to log z, strictly positive exactly when 2≤n≤2L−2. At t=1 the two-slot hypergeometric computation gives (2). The strict Stirling-entropy maximum solves (3); expansion at ρ=1+ξ√z+o(√z) gives y(y−ξ)=1 for y=u/√z and hence the stated variance coefficient. For n=L+k, after removing the common L^|k| factor the falling-factorial weight is bounded by a^j/[j!(j+|k|)!], also summable after multiplication by j. This gives the claimed total variation and first-moment convergence, and LV=2E[J]+|k|−k²/L gives (6). The infimum at t→0 or t→∞ discussed in the proof is not attained in nontrivial sectors; the finite-t maximum and the stated limits are unaffected. CHECKER.py was inspected but not executed; no independent replay of its reported 414 tests is claimed.

## originality

PASS

Credit the product stationary law, reciprocal parameter symmetry and the Bessel distribution itself as established ingredients. The supported distinct conclusions are the strict finite-ring variance optimization and the two explicitly ordered half-filling limits, in particular the fixed-doping total-variation and moment asymptotics for this canonical ring. The strongest inspected same-process result and the analogous Bessel result in a different model did not supply these conclusions.

## value

PASS

Near one particle per site, the canonical constraint couples vacancies and double occupancies. The ordered limits identify when a deterministic defect density is informative and when only finitely many paired defects remain, and quantify the resulting variance in both regimes. Total variation and moment control matter for that comparison; the scientific content is the ring asymptotics, not merely naming a classical count law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
