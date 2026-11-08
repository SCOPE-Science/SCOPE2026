# Independent mathematical audit

## correctness

PASS

For the degree-proportional one-parent tree started from edge {1,2}, conditionally J_t=attachment to vertex j and U_t=attachment to a leaf satisfy E[J_t U_t|T_t]=p_t I_{t,j}, p_t=1/(2(t-1)). Hence covariance increments are p_t^2 d_t mu_t-p_t q_t. The leaf mean is 2(t-1)/3+4h_t/3. Recursions for d_t, q_t and d_t h_t telescope exactly to (a_{n,j}+3b_{n,j}-4+4(h_j-a_{n,j}h_n))/3, including n=j. Since d_t/q_t=(t-3/2)/(j-3/2), the increment sign uses an increasing B_t=(t-3/2)mu_t/[2(t-1)]; increments are negative then positive, net covariance tends +infinity, so there is a single eventual positive transition (possibly an intervening zero). Uniform product asymptotics for n/j to rho>1 give (sqrt(rho)-1)(sqrt(rho)-3)/(3sqrt(rho)), with threshold rho=9. Independently enumerated all weighted parent histories for n=3..7 using exact fractions, agreeing with formula. The proof does not assign a sign at the critical birth fraction 1/9.

## originality

PASS

Full source comparison distinguishes PA trees from uniform-parent recursive trees and separates birth-indexed degree from number of leaf neighbors. The exact covariance trajectory and 1/9 threshold are not yielded by the inspected age-agnostic PA formulas or uniform-recursive-tree results. This is a qualified best-of-knowledge novelty assessment, not absolute priority proof.

## value

PASS

A signed, birth-age-resolved correlation change and the sharp macroscopic 1/9 threshold make a natural refinement of global PA leaf statistics. The exact finite-size formula can serve as a reusable age-indexed second-moment benchmark; it is not just an unmotivated small-instance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
