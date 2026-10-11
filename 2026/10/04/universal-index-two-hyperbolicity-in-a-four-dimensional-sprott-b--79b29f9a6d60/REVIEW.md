# Independent mathematical audit

## correctness

PASS

The equilibrium equations give exactly \(E_\pm=(\pm\sqrt b,\pm\sqrt b,0,0)\). Direct expansion of the Jacobian gives the displayed quartic with positive coefficients and the third Hurwitz determinant \(-bP(a,b,c)\), where every monomial of \(P\) has positive coefficient. Hence \(\Delta_3<0\) throughout \(a,b,c>0\). A zero eigenvalue is excluded by the positive constant term; a nonzero imaginary eigenvalue would force \(\Delta_3=0\). Thus the equilibria are hyperbolic on the connected positive octant. The exact Routh first column at \((1,1,2)\) has two sign changes, so the unstable dimension is everywhere two. The standard-library verifier independently expands the determinant and the Hurwitz polynomial exactly.

## originality

PASS

The introducing paper derives the same equilibria, states by Routh--Hurwitz that they are unstable for positive parameters, and gives one numerical saddle-focus spectrum at \((a,b,c)=(6,11,5)\). That does not fix the unstable dimension throughout parameter space or exclude imaginary-axis crossings. The submitted negative Hurwitz-determinant identity and connectedness argument provide the missing uniform index classification. Fresh Resultary search found the audited result as the only direct same-system hit; nearby results concern different four-dimensional flows.

## value

PASS

The exact unstable index is a natural local invariant of a parameter-scanned chaotic flow. Proving it constant throughout the full positive octant rules out all local equilibrium stability crossings as organizers of the reported windows, a materially stronger conclusion than generic instability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
