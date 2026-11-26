# Independent mathematical audit

## correctness

PASS

For each species, exactly C(r_i,k) of the C(n,k) samples retain it, independently of overlap with other species. Moving the k-tilted weights to level k+1 tilts by r_i-k; hence mu_(k+1)=mu_k+sigma_k^2/(mu_k-k) and R_k=(mu_k-k)/(n-k). Subtracting ratios gives the stated identity, on adjacent defined ratios (the terminal zero can be handled algebraically but is excluded from the turn count). Equal occupancies give a nonincreasing ratio, constant if the common occupancy is n. Independently rebuilt Pascal rows and exact rational Z_k and R_k, without executing the bundled checker: python3 /workspace/branches/recheck_zeta.py. Among 3654 unequal occupancy pairs across n=2–28, 1548 have zero turns and 2106 have one; at n=29 the counts are 141, 264 and 1 respectively. The only winner is (22,26), with full adjacent-difference sign string -++---------------------. The first five ratios are 139/168, 115/139, 4453/5382, 92114/111325, 27713/33496; the first four differences are -1/23352, 37/748098, 27323/599151150, -300819/3728942200. An independent direct recount of 146595 subsets at depths 1–5 agreed with their occupancy counts. Minimality and uniqueness are for two species, exact all-subsets sampling and the stated positive-ratio convention.

## originality

PASS

The accessible comparisons already give retention ratios and qualitative shapes, but do not supply or imply the sharp two-species minimum and uniqueness. The elementary size-bias identity is useful for interpreting the result, not the basis for a separate priority claim. This is a bounded judgment about the exact classification.

## value

PASS

Retention ratios are an established observable used to describe compositional change. A strict decrease–increase–decrease witness with only two species shows that multiple turns need not imply a complicated incidence profile; the minimum and uniqueness identify the exact small-design boundary for that observable. The tilted variance identity explains how this can occur despite depletion for each individual species. The magnitudes in the witness are tiny, so the result is about exact possible shapes, not the detectability or prevalence of those shapes in empirical surveys.

The dated certificate retains the supplied scientific assessment, sources and limitations.
