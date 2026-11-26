# Independent mathematical audit

## correctness

PASS

Conservation follows from Q1=0 and symmetry; off-diagonal signs of S_h are those of the corresponding semigroup derivatives at t=alpha h. In the balanced case the eigenvectors (1,0,-1) and (1,-2,1) give decay rates c and 3c. The center diagonal has decrement (2/alpha)x exp(-3x) with x=alpha c h, attaining its maximum 2/(3e alpha); both endpoint decrements are bounded by this and the off-diagonals are positive. In the unbalanced case, symmetry and the stationary mass 1/3 leave two exponentials. Matching the initial off-diagonal value and derivative gives the printed coefficients. For the heavier edge r>s, (2r-s)^2-d^2=3r(r-s)>0, so its derivative has a negative slow term and a positive fast term. Initially the derivative is r>0; the ratio of the positive term to the magnitude of the negative term strictly decreases to zero, giving the unique claimed crossing. Rationalizing the slow coefficient gives C=r(r-s)/(2d(2r-s+d)), hence C=(r-s)/(4s)+O_s((r-s)^2); the rate difference tends to 2s and the logarithm has the stated constant and o(1) remainder. The modewise stability bound follows from maximizing x exp(-alpha x) and does not change the entry signs.

## originality

PASS

The same update and the negative-real-axis modal stability threshold are credited to the originating paper. The distinct claim is the stepwise entrywise nonnegativity classification for the symmetric path, and the heavier-edge sign crossing with exact logarithmic delay. The exact path positivity comparisons involve different matrix functions and do not imply this classification.

## value

PASS

The minimal heterogeneous reversible path gives a useful exact obstruction to interpreting a spectrally stable conservative integrator as a nonnegative transport step. The abrupt requirement of exact balance and the logarithmic delay explain why strict modal contraction and even long finite-step test ranges can hide the sign failure. The balanced sharp constant and the unbalanced explicit witness supplement, rather than rephrase, standard stability background.

The dated certificate retains the supplied scientific assessment, sources and limitations.
