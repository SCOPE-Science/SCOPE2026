# Independent mathematical audit

## correctness

PASS

The weighted wheel Laplacian decomposes into constant eigenvalue zero, radial hub-versus-ring eigenvalue (n+1)g, and ring Fourier eigenvalues g+2-2cos(2pi k/n) (paired frequencies real dimension 2 except even alternation). For symmetric L, Lagrange spectral projectors show Kalman span rank=sum rank(P_lambda B). Two-point evaluation on each paired Fourier space has determinant sin(2pi kd/n), rank loss iff n|2kd. Arithmetic count gives (gcd(n,d)-1)/2 generic losses for odd n; gcd(n/2,d)-1 for even. A radial collision only when g=(2-2cos(2pi k/n))/n; merged evaluation columns give one extra rank lost except when angular pair evaluation has opposite signs (n|2kd and n∤kd), or even alternating k=n/2 with odd offset d. These are the printed delta cases. Independent exact SymPy rational Kalman matrix ranks agreed with analytic formula for all offsets at n=3,4,6,8,12 for nonresonant rational g and every rational resonance. Finite tests corroborate all-n proof.

## originality

PASS

Qualified best-of-knowledge originality: compared exact claim and possible implications with relevant primary literature and two actual semantic published-record searches; a failed search is not proof of novelty. Parlangeli–Notarstefano cycle formulas imply the n|2kd Fourier degeneracy but do not yield the radial collision  g=(2-2cos)/n or losses after collision. A more general exact family including wheels would cover this statement; accessible texts did not show one, subject to Liu–Ji fulltext uncertainty.

## value

PASS

The formula gives exact controllable subspace dimensions and rare spoke-weight resonance failures with cancellation depending on actuator geometry. This is a natural quantitative network-control invariant, not an arbitrary parameter slice: the wheel is a canonical nontrivial augmentation of a cycle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
