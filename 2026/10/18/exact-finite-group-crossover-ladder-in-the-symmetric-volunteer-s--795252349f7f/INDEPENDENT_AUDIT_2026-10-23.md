# Independent mathematical audit

## correctness

PASS

For one required volunteer, b>c>0, each of n≥2 symmetric agents independently volunteers with q_n=1−e^(−lambda/(n−1)), lambda=log(b/c). V_n=nq_n is the expected total count (NOT success probability). Writing z=e^(−lambda/[n(n−1)]) factors V_(n+1)−V_n=(1−z)z^(n−1)(S_n(lambda)−1), S_n=Σ_{j=1}^{n−1}(e^(lambda j/[n(n−1)])−1). Each S_n strictly rises from 0, giving one root. The n-entry coefficient vector for S_n strictly majorizes that for S_(n+1); explicit first-r gap r(n−r)/[n(n²−1)]>0 and Karamata give S_n>S_(n+1), hence lambda_n<lambda_(n+1). Taylor S_n=lambda/2+lambda²/(6n)+O(n−2) gives lambda_n=2−4/(3n)+O(n−2) and bracketed optimizer scaling. Independently checked 1,176 rational majorization partial sums and numerical roots n≤149; finite tests do not establish global monotonicity.

## originality

PASS

The game and equilibrium q_n, decreasing success probability and large-n limit were already known. Nöldeke–Peña (2020) Proposition 5 studies eventual sign of expected participation in a broader contributor-threshold game; their discussion distinguishes k>1 and does not in inspected passages give exact all-n strict ordering/unique peak and 4/3 shift in the k=1 game. Archetti 2009 basic model of volunteering compares probability the public good is provided or probability nobody volunteers; these are different than expected total contributor count. Another Archetti 2009 paper with group-size optimality was found by title/abstract only, where objective is production probability; residual risk of unexamined full text or textbook proof of exact V_n ladder. The new finite-size root ladder and exact maxima are modest but distinct from asymptotic sign statements.

## value

PASS

The complete finite-group response of expected collective contributions under the canonical symmetric mixed Nash equilibrium gives exact optimal group size, tie boundaries, and critical drift for all cost/benefit ratios, disambiguating expected volunteer count from public-good success probability. This is an interpretable, intrinsic comparative-statics answer for a standard social dilemma, not an arbitrary parameter slice or mere rewriting of q_n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
