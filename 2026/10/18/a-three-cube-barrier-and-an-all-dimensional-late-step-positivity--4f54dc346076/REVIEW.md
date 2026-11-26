# Independent mathematical audit

## correctness

PASS

At rate one per coordinate the Walsh eigenvalues of Q_d are -2k; the shell weights are the coefficients of (1-z)^j(1+z)^(d-j). The scalar numerator and denominator are positive, r_0=1, and symmetry follows from the orthogonal spectral decomposition. The exact heat kernel is a tensor product of strictly positive two-state kernels for h>0. Let D_k=1+kh+k^2 h^2/3, so r_k=1-2kh/D_k. The off-diagonal two-cube shells simplify to h/D_2 and h(1/D_1-1/D_2), both strictly positive, as is h/D_1 on the one-cube. On Q_3 inserting the four coefficient lists (1,3,3,1), (1,1,-1,-1), (1,-1,-1,1), (1,-3,3,-1) and clearing positive denominators gives the displayed four shell numerators. The first, third and fourth have positive coefficients after their h factors are removed; the second is -3h times the quartic. Descartes' sign rule and the sign change from h=0 to infinity give a unique positive threshold; exact rational evaluation brackets it between 8.583763463733358 and 8.583763463733359. At zero the update is the identity; at the cutoff only the neighbor shell vanishes. For arbitrary fixed d, expansion of 1-2kh/D_k gives 1-6/(kh)+O(h^-2). The constant terms cancel off the diagonal; the neighbor coefficient is -6 S_d/2^d. Pascal's identity gives the increment (2^(d+1)-1)/(d+1) in the reciprocal-binomial sum, yielding the stated increment of S_d. Since S_3=1/6, the leading term is negative in every d>=3. The uploaded verifier was inspected, not executed: it makes finite exact checks (including a bracket 8<h<9), not a proof of the recurrence for unbounded d or a computation of the printed root precision.

## originality

PASS

The supported distinct claim is the unit-rate reversible cube sharp first-failure threshold and the universal late-step edge sign, not standard Walsh diagonalization, the elementary small cubes taken alone, or generic Padé nonpositivity. A separately indexed November 8 result mathematically covers the whole claim at two stages and extends the sign law to even stage counts; a second November 8 product theorem covers the dimension boundary and large-step sign but not the sharp quartic. Both are later displayed than the frozen October 18 record, and the inspection did not establish an earlier version or priority. The earlier same-map general-CTMC obstruction and same-day different-map cycle theorem are different claims. No inspected earlier result establishes the full cube theorem.

## value

PASS

A sharp admissible timestep on the smallest failing reversible Boolean cube and an explicit negative edge sign in every larger dimension distinguish endpoint mass positivity from unconditional spectral stability for a natural implicit fourth-order method. The obstruction is structural and materially more informative than sampling a bad timestep or giving another directed counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
