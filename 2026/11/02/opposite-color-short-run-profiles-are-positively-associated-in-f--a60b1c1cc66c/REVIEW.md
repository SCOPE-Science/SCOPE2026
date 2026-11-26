# Independent mathematical audit

## correctness

PASS

Uniformly marking one of the r zero-run starts introduces no size bias within R=r: there is a bijection of marked labeled words to a labeled start and a pair of ordered positive compositions. Hence the two profiles are conditionally independent even for rotationally periodic words. Taking the first r−1 cuts in a uniform permutation of the internal gaps realizes each uniform composition and couples consecutive r by refinement. A split can never reduce a cumulative count, and the last coordinate rises strictly. Thus the conditional means of the indicated isotone functions are isotone in the shared scalar R, with strictness between r=1 and 2 for both strictly isotone functions and positive mass at both levels. The independent-copy formula for covariance proves the sign. The singleton conditional mean is r(r−1)/(m−1) for each color of content m≥2. Independently, the marked count is the hypergeometric mass binom(a,r) binom(b−1,b−r)/binom(n−1,b), giving exactly the quoted falling-factorial moments including the zero convention; the square of (R)_2 expands into (R)_4+4(R)_3+2(R)_2. One occurrence of a color makes its profile constant. The paragraph about monotone statistics is interpreted in the displayed nondecreasing order; reversing just one monotonicity reverses the sign. Fresh replay `python3 /workspace/review-evidence/reproduce.py 1` checked 3944 labeled words over 36 content pairs through n=11, including 243 joint conditional profile cells and the exact singleton covariance. The analytic argument, not that finite range, proves the theorem.

## originality

PASS

The supported distinction is a cross-color covariance sign for arbitrary isotone statistics of the cumulative circular profiles, with the exact circular singleton factorization. The cut-refinement mechanism has a close earlier linear antecedent, and the circular one-color and linear joint multicolor enumerations precede this record. Those are not the same claims; in particular the different linear conditional covariance shows why transferring the result from line to circle without a new argument is not valid.

## value

PASS

The fixed-composition circular null model is natural for run tests, and the theorem determines a structural sign for any opposite-color increasing profile tests simultaneously, not merely a single pair of run counts. It identifies which dependence survives conditioning, and the exact singleton covariance quantifies it; removing the circular sampling assumption changes the conditional mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
