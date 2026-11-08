# Independent mathematical audit

## correctness

PASS

For the unit-mass symmetric reflecting path L_n, C_n(s)=2(I+sL_n)^-1-I; the irreducible M-matrix inverse has positive off-diagonals so positivity is equivalent to its smallest return diagonal >=1/2. The four-image reflected Green kernel with z satisfying s=z/(1-z)^2 solves interior recurrence, both Neumann endpoint relations and the source jump exactly. Its diagonal min is unique at the center (or central pair), H_n(z)=(1-z)/(1+z)*(1+z^n)/(1-z^n) for odd n, or *(1+z^(n-1))(1+z^(n+1))/(1-z^(2n)) for even n. The spectral measure makes H strictly decreasing from 1 to 1/n, so n=2 never fails at finite s and n>=3 has one crossing. Solving H=1/2 gives the stated parity-specific polynomial root, the ratios H_(n+1)/H_n<1 show sigma_n strictly decreases, and Taylor expansion about z=1/3 yields sigma_n=3/4+4*3^-n+O(n9^-n) for odd n or 3/4+(20/3)*3^-n+O(n9^-n) for even n. Independent direct tridiagonal inversions and root searches at n=3...8 confirmed the formula and trends; infinite claims are analytic.

## originality

PASS

The exact Cayley/resolvent test C=2G-I and general reversible-chain crossing law are already publicly established and are explicitly acknowledged; here the new material is the complete reflecting-path Green kernel evaluation, center minimizer, exact finite-n polynomial thresholds, mesh monotonicity and two parity corrections. Higueras–Roldán arXiv:2301.01066 analyze Dirichlet difference rows with different endpoint control and asymptotics. Gao–Sun Neumann higher-order compact heat scheme is a plausible source but not fully accessible; without whole-text comparison it remains a documented priority risk, not an automatic failure.

## value

PASS

Reflecting/no-flux heat discretizations have different boundary rows and positivity thresholds from Dirichlet schemes. This complete finite-path threshold classification identifies the controlling center node, a sharp mesh-uniform CFL bound kappa*dt/dx^2<=3/2, and genuinely nontrivial parity-sensitive finite-size corrections. It provides natural positive-semigroup numerical analysis data not supplied by the general resolvent criterion alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
