# Independent mathematical audit

## correctness

PASS

The frozen proof's equation (3) gives uncovered diagonal-strip area (1-W/sqrt(2))^2, not the expression in frozen line 108 (which even gives zero at the transition). The stated M(W) was correct; the exact corner triangle calculation confirms 1/4 uncovered at the transition (/workspace/branches/audit_witnesses.py). The replacement /workspace/repairs/2/RESULT.md fixes the substitution and the offset argument. For the global bound, flipping one maximizing sign in the Bang map gives a margin w_i/2 to its offset hyperplane; distinct signs separate images and each measurable cell translates. On the eroded rectangle this yields C <= a+b-ab, irrespective of offset. Writing s=a+b and a^2+b^2=W^2-Delta separates the deficit into the claimed angular and dispersion terms. The formulas agree at W=1/sqrt(2) and increase strictly, so lesser budgets cannot attain equality. The diagonal and wide contact normals both satisfy the two-tail regime (strictly inside it); the wide normal has a+b=1 and realizes the upper bound. For one strip the deficit identities determine the normal even at noncentral offsets, and the projection density proves unique centering: sliding is nonincreasing away from zero and strictly decreasing immediately next to zero. This classifies single-strip maximizers only. The inverse width formula follows by inversion. The family inequality is for exact total width.

## originality

PASS

Pass for the repaired framing, which identifies the direction-sensitive arbitrary-family deficit as the distinct quantitative finding. The exact square envelope is an explicit prior planar-theorem specialization, and the angle and offset are covered by a distinct indexed calculation after scaling. Neither is credited as a separate original contribution here. The quantitative bound is a square-specific extraction from the stronger erosion machinery; this is not a new Bang lemma or a priority certificate.

## value

PASS

The arbitrary-family quantitative comparison controls near-extremizers: for a budget and area gap it bounds width-weighted spread of their absolute normal vectors, and separately penalizes mismatch to the optimal contact condition. This information is not furnished by knowing the optimum or that a single strip realizes it. The exact square profile gives a natural sharp reference for the estimate, not a separate novelty claim. Reflected directions can share the same absolute normal, so it does not certify actual parallelism or classify general equality families.

The dated certificate retains the supplied scientific assessment, sources and limitations.
