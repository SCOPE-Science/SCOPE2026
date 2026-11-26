# Independent mathematical audit

## correctness

PASS

The mean projector diagonalizes Q into the constant and mean-zero spaces, giving positive diagonal/off-diagonal semigroup coefficients p and their integrals k. In each row the independent input coordinates maximize odd cubics g(v)=pv+k(v-v^3). These have maximum p iff 2k<=p and otherwise attain the printed interior maximum. Since the p row sum is one, the two coefficient tests are both necessary and sufficient. The off-diagonal test holds strictly for h<=1/2 by increase of p_o(s); the diagonal test has a unique crossing below 1/2 since k_d grows and p_d decreases. Constant vectors rule out larger steps. With v=1-epsilon the excess is (2k-p)epsilon-3k epsilon^2+k epsilon^3; maximizing yields the claimed quadratic coefficient once k_d'=p_d is used. In the parameter y=gamma h_*, gamma(y) strictly increases from zero to infinity, and h'(y) has the sign of H_a(y). Its third derivative is positive, H_a'' starts negative and all three lower derivatives/functions ultimately grow with the positive exponential; thus there is one positive zero of H_a and one minimum in gamma. Expanding the threshold equation gives the two fixed-dimension endpoint expansions, and dividing by n-1 and using the strict scalar limiting root gives the large-dimension limit.

## originality

PASS

The original ETD1 formula and the maximum-bound results for stabilized splits are not claimed as new. The supported distinct result solves the exact all-input cube optimization for the unshifted complete-graph cubic map and gives its sharp horizon, unique interior mixing minimum and overshoot onset. The relevant published comparison theorems use a different split; the unread 2005 paper remains a named risk, not evidence of noncoverage.

## value

PASS

The exact Allen–Cahn flow preserves a canonical physical cube. A sharp all-input time-step bound for the standard unshifted method is useful even on the idealized complete graph. The unique intermediate mixing minimum and explicit maximizing witnesses show why stronger mixing need not monotonically aid cube preservation, and the quadratic onset quantifies the size of the worst violation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
