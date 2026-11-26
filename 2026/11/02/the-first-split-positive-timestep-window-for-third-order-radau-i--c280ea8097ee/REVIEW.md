# Independent mathematical audit

## correctness

PASS

Since the spectrum of h(S-I) lies in the closed left half-plane and both poles are in the right half-plane, the map exists for every h>=0. Applying it to the constant vector yields row sum R(0)=1. The residue at 2+i sqrt(2) is 1-5i sqrt(2)/2; expanding the inverse in cyclic powers gives the stated numerator formula over |(h+2+i sqrt(2))^n-h^n|^2>0. Circulant shifts occupy disjoint positions in each row, so at h>0 each offset sign is exactly its reduced numerator sign. Independent exact symbolic matrix inversion and Sturm checks reproduced the polynomials and classifications for 2<=n<=8. For 2–5 all reduced numerators have nonnegative coefficients and positive constants. For 6 and 7 the diagonals stay positive and the last offset threshold dominates; the required roots are isolated in (0.208,0.209) and (0.663,0.664), respectively. At 8, offsets 5–7 each have one positive root, with the offset-7 root alpha largest. The diagonal has exactly two positive roots, with rational brackets (3.297,3.298) and (7.042,7.043) and sign changes + to - and - to +. Thus the admissible positive steps are exactly [alpha,beta] and [gamma,infinity), including all three endpoints by nonnegativity. At h=0 the map is the identity in every dimension. The independent check was exact, not timestepping on a numerical grid.

## originality

PASS

There is substantial existing coverage: the n<=6 phase diagram and the fact that n=8 has disconnected positive-step regions are not supported as distinct contributions. The frozen finding also makes the materially stronger exact classification at n=7 and n=8, including the least split dimension and all three algebraic eight-cycle endpoints. The strongest inspected same-problem records do not establish that classification or imply its exact boundaries and absence of further components. The pass is for this distinct strengthened classification, not for the already matched components or for historical priority.

## value

PASS

An exact sign phase diagram for a canonical method on directed Markov cycles distinguishes a genuine two-window domain from a few illustrative sample steps. Certifying that the immediately smaller cycle has one recovery interval settles where the first nonmonotone phase diagram occurs; the three precise boundaries tell which timesteps actually preserve stochasticity in that first dimension. This provides useful fixed-generator information not supplied by a general loss-of-positivity test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
