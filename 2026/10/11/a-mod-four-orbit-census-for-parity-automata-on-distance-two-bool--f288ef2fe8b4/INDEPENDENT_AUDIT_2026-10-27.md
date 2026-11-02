# Independent mathematical audit

## correctness

PASS

For all n≥2, write the exact GF2 distance-two adjacency operator as multiplication in the truncated group algebra R_n=F2[y_1,...,y_n]/(y_i²). Its shifted positive-degree multiplier N=F+binom(n,2)I squares to zero by Frobenius. If n is even, N=e1+e2=(1+s)y1+p with (1+s)²=1, so an explicit invertible generator substitution sends N to a single generator and gives rank 2^{n-1}. For n=2m+1, N=e2 has alternating coefficient form J+I with one-dimensional radical; symplectic generator normal form N=sum u_jv_j and tensor homology (dimension 2^{m+1}) imply rank 2^{n-1}-2^m. The graph paths independently give F²=cI, c=binom(n,2) mod2, distinguishing n=0,1 mod4 nilpotent from n=2,3 mod4 involutory. Rank-nullity yields fixed/two-cycle and initial/one-step/two-step hitting counts, including n=2 and nonzero vs initially zero. Independently implemented GF2 Hamming-mask elimination agrees for 2≤n≤10 with ranks 2,2,8,12,32,56,128,240,512, and exact low-dimensional orbit enumeration agrees with formulas. Finite tests corroborate, not replace, the unrestricted proof.

## originality

PASS

Best-of-knowledge original natural all-dimensional finite-field rank and complete binary orbit census. Especially relevant full-text Key–Fish–Mwambene (2011) computes incidence and line-graph ranks of the same distance-two cube, but not the shifted vertex adjacency rank GG^T; Rollier–Baetens (2026) treats real Jacobian Lyapunov spectra, not GF2 state counts; Peeters (2002) treats distance-one Hamming adjacency. Searches of published mathematical findings found no mathematically dominating rank/orbit theorem. The possibility of an older specialist distance-two 2-rank formula remains a stated risk.

## value

PASS

Distance-two Boolean cubes are natural distance-regular Hamming graphs, and the XOR update is a standard graph parity dynamical model. The infinite family has 2^{2^n} configurations, yet the result classifies all trajectories exactly for every n≥2 with sharp modular-four nilpotent/involutory transition and odd-dimensional lower rank correction. The nonstandard alternation-to-Künneth computation supplies substantive mathematical content: neither ordinary adjacency eigenvalues over the reals nor published incidence/line-graph ranks make the GF2 orbit census automatic. The exact rank also describes code dimension and fixed configurations that researchers of additive dynamics and Hamming schemes may need. No unproved other-shell/forcing generalization or unstated application is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
