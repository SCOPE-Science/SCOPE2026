# Independent mathematical audit

## correctness

PASS

From the actual RESULT.md branch map and positivity intervals, derive the three index-edge sets: shifts {j,j+2m} (0<=j<n-2m), low reflections {j,4m-1-j} (m<=j<2m), and upper reflections {j,2n-4m-1-j} (n-3m<=j<n-2m). They give exactly n undirected edges on n states. Shift residue paths mod 2m are joined by involutions a(r)=-1-r and b(r)=2n-1-r; b∘a translates by 2n, transitive within each parity class since gcd(m,n)=1, while a swaps parity classes. The connected graph has precisely 2m leaves that meet degree-three vertices; removing leaves leaves one (n-2m)-cycle. Detailed balance sin(x_i)P_ij=sin(x_j)P_ji follows by checking the branch sine identities. The finite irreducible Markov chain period is odd/even parity of n. Verified independently by rebuilding integer edge graph and all four original branches for 228 parameter/offset cases, checking stochasticity, balance and sine normalization; that bounded check does not replace the all-parameter proof. Nongrid strict boundary and full phase-space billiard excluded.

## originality

PASS

Feres established the random billiard model and reversible angular laws. Vales and Pinto-de-Carvalho (arXiv:2005.01892, Section 5 Proposition 5.4) establish finite rational fibers and irreducible Markov shifts, not the general graph type/period calculation. Vales (arXiv:2212.00872, Section 3) explicitly exhibits pi/7 aperiodic and pi/8 period-two examples and considers continuum mixing, not all reduced fractions. Those examples do not logically imply a universal denominator-parity theorem or explicit n-2m core and 2m leaves. No covering Resultary hit found; an earlier general dihedral graph computation remains possible.

## value

PASS

The arithmetic dichotomy decides precisely when a rational-angle fiber approaches one distribution or alternates forever, a natural mixing/stability question after the two earlier examples; the explicit unicyclic graph and stationary law are useful for future spectral, hitting-time, and rate calculations. Not just routine Markov convergence because the support topology for every reduced parameter is the substantive theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
