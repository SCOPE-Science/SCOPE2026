# Independent mathematical audit

## correctness

PASS

PASS. The generator L=sum r_i(I-tau_i) has eigenmultiplier s_i=e^{-2r_i t} for each single-bit Walsh character. At one output row its eight product probabilities are p(y)=prod_i(1+s_i y_i)/2. On the real mean-zero infinity-norm unit ball, every extreme vector is a balanced sign vector of exactly four + and four -, since seven saturated signs force the last. Therefore maximizing a row gives the sum of four largest minus four smallest probabilities; complex coefficients reduce to real parts after a global phase rotation. Sorting antipodal vertices by log likelihood weights a_i=log coth(r_i t), with a1>=a2>=a3>0, yields only two top-four sign patterns: majority if a1<a2+a3 and dictator y1 if a1>a2+a3. Their expectations are respectively (s1+s2+s3-s1s2s3)/2 and s1, proving the exact norm for all ordered positive rates and t>=0. For h(u)=log coth u the quantity G(u)=-u h prime(u)/h(u) strictly increases: J(u)=1/G(u)=h(u)sinh(2u)/(2u) admits a positive integral with strictly decreasing integrand, by 2coth(2u)-2coth(2u+2v)-1/u <0. Thus for r1<r2 the ratio (a2+a3)/a1 decreases strictly from 2 to 0, giving one transverse positive crossing, unequal analytic derivatives and a genuine cusp. If r1=r2 majority wins for all t>0. The exact small-time t² coefficient is 2 sum_{i<j}r_i r_j, while the large-time norm is precisely the slowest multiplier after t*. The transition tie and complex extension were checked.

## originality

PASS

PASS, best of knowledge. Standard Fourier–Walsh and fair-bit noise theory (O’Donnell), hypercontractive/spherical Hamming averages (Polyanskiy), and Mori’s three-bit majority optimality for nonlocal-box bias amplification supply related tools but not this anisotropic mean-zero L-infinity operator norm, its complete all-time branch formula, or its unique cusp for a simple slow rate. Balanced four-largest-atom rearrangement is elementary and acknowledged as antecedent, not itself novelty. A classical statistical decision or weighted-voting envelope theorem could cover the switch by a different name; that remains a recorded historical risk.

## value

PASS

PASS. A centered Markov semigroup has trivial full-space infinity norm one, so its mean-zero endpoint norm is a natural nontrivial mixing/contraction invariant. The smallest product cube supporting a genuine competition between a 3-coordinate majority and a 1-coordinate dictator has an exact nonanalytic time profile despite analytic heat entries. A strict unique positive transition, its extremizer rigidity and short-/long-time laws are structural results, not a numerical curve or textbook restatement of scalar decay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
