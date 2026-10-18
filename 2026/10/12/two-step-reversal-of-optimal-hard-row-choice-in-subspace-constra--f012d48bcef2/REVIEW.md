# Independent mathematical audit

## correctness

PASS

An invertible integer A=[[-2,-1,3],[-1,0,-3],[0,-2,1]] has determinant 17. For each enforced row i, the two projected remaining normals span the residual plane; p=a/(a+b), q=1-p, z=d^2/(ab) in [0,1). The projected line annihilators T,U satisfy TUT=zT, UTU=zU. The first-step M1=pT+qU has max eigenvalue (1+sqrt(1-4pq(1-z)))/2. The second-step M2=(p^2+pqz)T+(q^2+pqz)U has the claimed eigenvalue formula, and its two-coefficient positive recursion has Perron root rho=(1+sqrt((p-q)^2+4pq z^2))/2 for nonzero z. Independent exact rational Gram computations reproduced the source p,z values (91/136,7/585), (91/132,841/3731), (45/86,80/369), and separate radical comparisons prove L1(1)<L3(1)<L2(1) while L3(2)<L1(2)<L2(2); row 3 minimizes rho as well. Strict inequalities ensure openness. For nonsingular 2x2 and one fixed hard row, the one remaining projected row annihilates the one-dimensional error in one update; hence dimension three is minimal. Minimax is over different hard-row-specific unit initial errors, NOT over a single common initialization.

## originality

PASS

Sun et al. 2026 Sec 3.2 selects fixed subsystems using a convergence-factor surrogate; Lok-Rebrova 2024 introduce the projected SCRK update and bound its mean-square rate. Agaskar-Wang-Lu's prior exact MSE operator formalism can compute any fixed case, but its existence does not itself state an integer matrix where the OPTIMAL hard-row index reverses at t=1 versus t=2, nor dimension minimality. The source does not claim novelty of the projection recursion itself. Best-of-knowledge no exact equivalent found.

## value

PASS

This is a motivated, smallest-dimension discrete hard-equation selection reversal in a known preconditioned randomized algorithm. It cautions that optimizing a one-step minimax loss, even with exactly computable projected row weights, can select a different hard equation than two-step or long-run criteria. The exact integer witness, dimension barrier and open stability provide a nontrivial counterexample and structural boundary without claiming a new general MSE formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
