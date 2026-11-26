# Independent mathematical audit

## correctness

PASS

With invariant probability measure, the diagonal of the harmonic projector is its trace, the bidegree dimension (q+1)^3. The radial variable t=|<z,v>|² has density 2(1−t) on [0,1]; radial orthogonality to lower degrees gives P_q^(1,0)(2t−1), and dividing by q+1 normalizes its diagonal to one. Thus the only normalized entry values are 1,a_q,b_q. The Gram matrix acts as 1−a_q on the eight within-basis contrasts, 1+2a_q−3b_q on the three balanced basis constants and 1+2a_q+9b_q on the global constant. The exact low-degree spectra give the claimed attainable data subspaces. I independently checked every sector for q=3..16 against the frozen table via the direct Jacobi binomial formula, not the source's Legendre recurrence. The lower endpoint is attained only on the constant sector at q=5, where the spectrum is (7/6,70/81,2/27); the upper endpoint likewise occurs only in the constant sector at q=4. For the infinite tail the Christoffel identity and |P_q|≤1 give |b_q|≤3/[2(q+1)], so the spectrum stays in [1−31/(2(q+1)),1+31/(2(q+1))]. Even at q=17 the bounds 5/36,67/36 are strictly inside the two stated endpoints and the ratio is at most 67/5<63/4. This establishes full rank, all equalities and the sharp condition numbers. At q=0,1 all positive eigenvalues coincide; at q=2 their ratio is 10/3, so including only nonzero singular values at the deficient degrees does not change the worst evaluation condition number. For attainable y, E_q*G_q^+y solves the data and lies orthogonal to ker E_q, proving the reconstruction and squared norm formula.

## originality

PASS

Best-of-knowledge pass for the joint all-degree interpolation and sharp stability result, particularly the uniform lower and upper spectral constants and the global worst condition number with equality degrees. The addition kernel, MUB overlap design, three-sector decomposition once the Gram entries are known, and minimum-norm reconstruction use standard machinery and do not get independent novelty credit. The indexed November 2 MUB result actually covers the qutrit ranks at q=0,1,2,3 and the exact cubic spectrum, not just a related topic; its later date is not evidence against the October 18 result's priority. Its scope stops short of the all-degree bound and the distinguishing q=4,5 extrema. No inspected earlier statement covered those extrema; priority is not certified.

## value

PASS

This is an exact comparison of harmonic interpolation and its conditioning on a canonical projective design, not just an evaluation of the addition kernel. It specifies which data are forbidden in the low degrees, proves that the obstruction disappears for every later degree, and identifies a nontrivial deterioration at degree five despite a better-conditioned degree three and convergence of the normalized spectrum to one. The constants and equality modes quantify the worst minimum-norm reconstruction cost and distinguish invertibility from useful conditioning.

The dated certificate retains the supplied scientific assessment, sources and limitations.
