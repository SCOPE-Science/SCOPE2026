# Independent mathematical audit

## correctness

PASS

For the finite irreducible SIS chain with known alpha_i,delta_i>0 and calibrated small contact epsilon, pi0 is independent Bernoulli(p_i), p_i=alpha_i/(alpha_i+delta_i), s_i=alpha_i+delta_i. Differentiating pi_epsilon Q_epsilon=0, the perturbation density is quadratic in centered coordinates Y_i=X_i-p_i, since Q0 acts with eigenvalues -s_i,-(s_i+s_j) on first/second products. Direct generator computation yields pi0'/pi0=sum_i (A_i/(p_i s_i))Y_i +sum_(i<j)[(beta_ji/p_i+beta_ij/p_j)/(s_i+s_j)]Y_iY_j, A_i=sum_j p_j beta_ji. Hence prevalence slopes M_i=(1-p_i)sum_j p_j beta_ji/s_i and covariance slopes C_ij=(1-p_i)(1-p_j)(p_j beta_ji+p_i beta_ij)/(s_i+s_j). Strict bidirectional positive support implies C_ij>0 exactly on contact edges. Reparameterize by directed a_(j->i)=p_j beta_ji: edge totals T_ij and incoming vertex sums U_i are observed. After fixing edge sums, differences form the signed incidence matrix of rank n-c, yielding dimension m-n+c with an interior positive neighborhood. Forest leaf peeling gives unique reconstruction; cycle circulations give nontrivial aliases. Independently solved the 8-state triangle differentiated stationary generator exactly for symmetric 2/2 vs cyclic 3/1 rates, obtaining identical complete pi0' and slopes 1/2,1/8. The full arbitrary finite-n proof comes from the symbolic spectral basis and incidence rank, not finite sampling. No higher-order/nonzero-contact identifiability is asserted.

## originality

PASS

Compared the exact claim and implications with the named primary mathematics and published Resultary records. The actual semantic query was 'Resultary: weak transmissibility independent cascade epidemic inverse problem graph cycle space reconstruction edge probabilities'. No materially inspected source supplies or logically dominates the stated instance; inaccessible/unindexed source risks remain.

## value

PASS

A sharp if-and-only-if forest condition and exact m-n+c ambiguity dimension form a natural structural identifiability theorem for directional contact rates. It establishes first-order sufficiency of means and covariances for an entire 2^n-state stationary distribution, a nontrivial observation-map reduction with a motivated cycle-space obstruction. It does not claim noisy-data or general nonlinear inference.

The dated certificate retains the supplied scientific assessment, sources and limitations.
