# Independent mathematical audit

## correctness

PASS

The stopped generator with each sign change marked by z has off-diagonal terms rz and diagonal killing r+s. Diffusion gives both boundary values 1 at a. The process drifts to −∞ on non-hit paths (Y_t/t→ξ√(rD)−b<0); alternatively its finite almost-sure supremum gives decay of the hitting probability as the start recedes. A bounded decaying mode solution represents the transform by stopped Itô's formula and dominated convergence. For z>0 the characteristic quartic is negative at each uncoupled positive and negative root and positive at both infinities. At zero it is positive or, in the untitled hit-probability case z=1,s=0, it has a simple zero with positive slope. The sign intervals exhaust the degree, leaving exactly two strictly positive modes. To check the slow mode let ε=√(rD), x=εκ/r and A=r(x²+ξx−1)−uε. The characteristic equation becomes ε(A²−r²z²)−2brx A=0. At ε=0 its positive root k=kξ is simple; with κ=rk/ε+c, the order-ε equation is −r²z²−2brk(hξ c−u)=0. Hence c=u/hξ−rz²/(2bk hξ). For the fast root the scaled variable Dκ tends to the simple root 2b of x³(x−2b). The slow eigenvector has plus coordinate 1 and minus coordinate O(ε); the fast one has minus coordinate 1 and plus coordinate O(D). Thus the slow boundary amplitude tends to 1 and the fast term at distance a is negligible. The scalar z=0 case has the same expansion without the z² term. Dividing by z=1,u=0 yields the claimed transform; setting z=e^(−v) gives joint Laplace convergence, and parity follows on the integer count space. Inspected RESULT.md lines 39–86, VERIFICATION.md and verify.py. The supplied finite comparison uses the same quartic and is diagnostic; it was not rerun or used as the asymptotic proof.

## originality

PASS

The supported distinct claim is the critical thermal-window limit of the reversal-marked transform conditional on an eventual uphill hit, including its Poisson mean and deterministic time. Neither the two-state backward equations nor jump marking is new. The statement-level comparisons establish no prior exact or mechanical coverage of the singular conditional law within the inspected sources.

## value

PASS

At a natural balance between adverse force and propulsion, the model distinguishes rare successful paths from typical ones and resolves an order-one path statistic that a mean-time result misses. The paired Poisson structure with explicit load dependence and joint deterministic time describes the selected trajectories, not merely the leading exponential scale of the hit probability. Its value is confined to the stated whole-line, plus-start model, not a full bistable escape claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
