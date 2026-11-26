# Independent mathematical audit

## correctness

PASS

Independently recovered exhaustiveness without executing the polygon checker. On a 3-periodic orbit with y-coordinates y_i in [0,1), x_i≡y_i−y_(i−1) (mod 1); conversely the orbit equations reduce to S≡3y_i+f(y_i) (mod 1) for each i, with S=Σy_i. Split at 2/3, assigning the switching point to the upper interval. With an upper coordinate, S is integral and every lower coordinate is 0, 2/9 or 4/9. Three uppers force S=2 and y_i=2/3. Two uppers force S=2: the lower coordinate cannot be 0, and 2/9 and 4/9 give respectively the open J₁ interval and closed J₂ interval in the unique lower phase. One upper forces S=1 and the triple to be a permutation of (0,2/9,7/9); the two cyclic orders are precisely the two endpoints of J₁ and their images. With no upper coordinate, write (9/2)y_i=S+k_i for integers k_i. Then S=2Σk_i/3<2, so S is 0, 2/3 or 4/3. The last two cases force k multisets (0,0,1) and (0,1,1), respectively, using 0≤S+k_i<3. They give y multisets (4,4,10)/27 and (8,14,14)/27, i.e. the two isolated cycles with the stated seeds. The all-zero tuple gives the other fixed point. The congruences are sufficient as well as necessary, so no boundary points or primitive cycles are missed. Direct branch multiplication gives B²A=[[1,9/2],[0,1]] on both smooth interval interiors; the other phases are conjugate. All-lower isolated cycles have derivative A³, hyperbolic since det A=1 and trace A=7/2. Length uses the three phase tangents (1,0),(1,1),(−2,−1), with no positive-length overlap; each base interval is 2/9 long. The finite points do not affect the measure. Frozen checker.py and VERIFICATION.md were inspected, not executed; the congruence calculation is an independent exact exhaustion including wrap edges.

## originality

PASS

Earlier primary work fixes the map, the loss of hyperbolicity, and the period-three islands above threshold. The closest exact indexed result is dated later than the frozen record and establishes the same non-isolated locus and length but not the isolated-cycle census. No inspected earlier statement covers the full critical classification. This is not a claim of exclusive or absolute priority.

## value

PASS

Period three is the itinerary responsible for loss of hyperbolicity at the authors' natural threshold. The exact all-orbit critical census identifies the parabolic geometry, distinguishes isolated saddles at the same critical parameter, and measures the neutral locus. These are specific useful data at a motivated boundary, not an arbitrary small-period sample or a general ergodicity claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
