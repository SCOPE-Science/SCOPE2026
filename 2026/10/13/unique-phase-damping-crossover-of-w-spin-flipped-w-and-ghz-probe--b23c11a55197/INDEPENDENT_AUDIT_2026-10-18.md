# Independent mathematical audit

## correctness

PASS

For n>=3, the n one-excitation strings and n (n-1)-excitation strings are disjoint. Their 2n-dimensional dephased density matrix block (A,B) is determined by Hamming distances 2,n,n-2; uniform and orthogonal eigenvectors yield two commuting spectral sectors. The mixed-state SLD formula for J_z gives F_WW=(n-2)^2 z^(n-2)[(n-1)(1+z)-(n-2)z^2]/[1+(n-1)z], while F_GHZ=n^2 z^n, z=(1-p)^2. The QFI ratio is strictly decreasing in z in (0,1], tends to infinity at z->0, and at z=1 equals (n-2)^2/n^2<1: unique interior crossover. Expanding at z=1-x/n and bracketing yields n p_c->1/2 and fixed lambda/n ratio 1+(8lambda-4)/n+O(n^-2). n=3 even though excitation sectors adjacent remains disjoint. Both endpoint p=1 QFIs vanish: there is no strict advantage there. Independent construction of all dephased 2n-by-2n density matrices and direct two-sided SLD spectral computation matched formula for n=3,4,5,6 and five p each (20 instances); bounded checks supplement the exact spectral algebra.

## originality

PASS

Sudha–Karthik–Akhilesh–Usha Devi 2026 investigate exactly the W-superposition/GHZ family with this phase damping channel and finite plots; Section III.B explicitly notes analytic characterization is beyond scope. Li–Ren 2023 study same WW probe and some noisy QFI but predominantly optimized-axis and small-n expressions; these are not identical to the fixed J_z all-n analytic comparison. The GHZ damping law and mixed-state SLD formula are established prior work. 2023 Li–Ren complete primary text inaccessible, so its exact scope is a significant residual risk, not a proof of noncoverage.

## value

PASS

Fixed-generator QFI is an operationally meaningful metrological quantity for specified longitudinal-phase sensing. A unique crossover separating two widely used probe families for every size and a sharp p_c~1/(2n) strength scale quantify a specific noise tradeoff beyond finite-size graphics, without claiming optimality for unrestricted encoding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
