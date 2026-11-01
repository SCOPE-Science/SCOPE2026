# Independent mathematical audit

## correctness

PASS

For a genuine two-cycle on a connected graph, L(f+g)=0 forces each vertex to fire once in two updates, excluding 0/2 constant patterns as fixed states. For a first-round firing phase f, all vertices require at least one opposite-phase neighbor, with c_v cut degree. Conditional chip counts are exactly [deg(v),deg(v)+c_v-1] for firing vertices or [deg(v)-c_v,deg(v)-1] for waiting vertices. An independent offset a_v in 0..c_v-1 establishes the bijection cut+offsets modulo two phase choices; total mass 2(n-1)-|S|+sum a_v. For P_n the allowed cuts have endpoint bits 1 and no consecutive 00. Their two-state weighted transfer has characteristic equation producing C_2=z,C_3=z²(1+z), C_n=z(1+z)C_{n-1}+z³C_{n-2}; rational GF and binomial formula follow. The n−1..2n−3 support, unit extrema, reciprocity, mean (3n−4)/2 and Pell total follow exactly. Dominant analytic eigenvalue lambda_+(z)=z(1+z+sqrt(1+6z+z²))/2 gives cumulant first derivative 3/2 and second derivative sqrt(2)/8 at z=1, justifying the CLT by a uniform neighborhood spectral gap and mgf convergence. Fresh independent Python executed direct two-update enumeration for 349,524 states over n=2..10 and cut/offset enumeration n=2..10; all mass coefficients equaled the recurrence/binomial values. SymPy independently established the asymptotic variance coefficient. Finite checks corroborate, not replace, the all-n proof.

## originality

PASS

Best-of-knowledge originality is confined to the full open-path primitive-period-two mass polynomial, Pell orbit census, reciprocity and Gaussian mass fluctuations; periodic firing alternation, tree period bounds and total-chip interval are credited as old. The full Scully-Zhang-Jiang 2011 tree paper supplies local 2-periodic constraints and chip-count intervals but does not count period-two orbits by chip mass. Full Dall’Asta 2006 paper studies the periodic degree-two ring, even describing generating functions for ring periodic populations, but not the open path with degree-one endpoints. No stronger prior implication was found on statement comparison, with explicit residual priority risk for a 1992 primary paper unavailable in full.

## value

PASS

Complete mass-by-mass counting of primitive cycles for all path lengths is a natural dynamical invariant beyond a yes/no period test. Its exact Pell census, symmetric coefficient law, sharp support and Gaussian limit quantify the diversity and typical mass of recurrent configurations. It is not a renamed general period theorem or arbitrary finite slice; the exact polynomial survives independent of uncomputed attraction basins.

The dated certificate retains the supplied scientific assessment, sources and limitations.
