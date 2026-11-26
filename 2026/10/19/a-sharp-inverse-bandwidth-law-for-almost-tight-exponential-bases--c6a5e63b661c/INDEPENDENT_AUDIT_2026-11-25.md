# Independent mathematical audit

## correctness

PASS

Horizontal Fourier series split synthesis into identical three-dimensional fibers, so the squared Riesz ratio is the ratio of extremal Gram eigenvalues in every nonsingular case. The vertical Fourier factor has no real zero: vanishing would require t and sqrt(2)*t to be the complementary third-integer residues. Thus orthogonal frequencies occupy distinct channels of one translated integer lattice, leaving a complement within each occupied three-dimensional fiber. For the global lower bound, F(u,v)=1+e^(2pi i u)+e^(2pi i v) has just the two torus zeros and determinant magnitude 2pi^2 sqrt(3) there. Compactness and the local smooth inverse therefore put (3t,3sqrt(2)t) within O(delta) of complementary residues (q,p) when delta=kappa-1 is small, since average Gram eigenvalue one implies ||G-I||<=delta. The integer norm |p^2-2q^2|>=1 forces delta>=c/(1+R); large delta and singular instances satisfy that lower bound too. Multiplication by 17+12sqrt(2) preserves Pell norm 2, switches the complementary nonzero residues, and keeps q_(j+1)<=41q_j. Taking the last admissible denominator yields the required all-large-R upper estimate, not just a subsequence. As an independent check of the coefficient, at t_j=q_j/3 the first two rows are orthogonal. In the row Gram the centered spectrum is exactly -s,0,s, with s^2=2[(1-cos theta)^2+3sin^2 theta]/9, theta=2pi*(sqrt(2)q_j-p_j)/3, for either residue orientation. Thus kappa-1=2s/(1-s) and q_j*|theta| tends to 2pi/(3sqrt(2)), giving 4pi/(3sqrt(3)). The uploaded VERIFY.py was inspected, not executed. Its line 52 subtracts the absolute error when printing the last scaled coefficient and so is not a reliable signed diagnostic: evaluating the independent row-Gram identity at j=6 gives about 2.418399153889, above the limit 2.418399152312. The unsigned error assertions and analytic theorem are unaffected.

## originality

PASS

The distinct claim is quantitative: the sharp inverse vertical-bandwidth order in the fixed equally spaced three-coset family and the exact Pell-sequence leading coefficient. Qualitative nonspectrality is covered as a corollary of the interval-factor spectrality result plus the elementary atom obstruction, and is not independently credited. None of the inspected quantitative analogues determines this bandwidth law or coefficient. No claim is made for unrestricted frequency design or for the exact limit of R*(K(R)-1).

## value

PASS

The example quantifies the cost of approaching tightness on a nonspectral product for a natural frequency family: increasing vertical bandwidth can make the basis almost tight, but cannot beat inverse bandwidth in that family. The constructive denominators work at every large bandwidth and the exact subsequence coefficient calibrates their performance. This is a genuine sharp obstruction together with a matching construction, not just a finite Gram-matrix example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
