# Independent mathematical audit

## correctness

PASS

For ordered distinct iid nodes the exponential covariance has an exact Markov-innovation precision form z1²+sum_i (z_{i+1}-r_i z_i)²/(1-r_i²) with r_i=e^(-gamma d_i); a unique collapsing gap delta makes the spectral norm 1/(gamma delta)+O(1) when other gaps are bounded below. The full operator norm has deterministic O(1/delta_min) upper bound. Pair-collision inclusion-exclusion yields P(delta_min<a)=n(n-1)a integral w²+o(a), and multiple near-collisions have O(a epsilon) probability under bounded w. Sending t->infinity then epsilon->0 gives P(||K^-1||>t)~C/t and P(lambda_min<s)~Cs, C=n(n-1) integral(w²)/gamma. Layer-cake gives the q<1 moment threshold; integration by parts yields E||(K+tau I)^-1||~C log(1/tau), q>1 constant C/(q-1)*tau^(1-q). Cauchy–Schwarz makes uniform w uniquely optimal at leading order; exact uniform spacing and two-node identities follow from simplex volume and 2x2 diagonalization.

## originality

PASS

Sharp fixed-n random-site Ornstein–Uhlenbeck inverse-conditioning tail coefficient, all-moment phase boundary and nugget expectation laws are not implied by the classical Markov precision, fixed positive-nugget conditioning or a fixed-site flat-kernel limit. Priority remains qualified for inaccessible specialized random-kernel work.

## value

PASS

An exact Pareto tail and universal critical moment exponent for finite random OU covariance matrices quantify a natural severe conditioning mechanism; the exact coefficient and optimizing design density are useful beyond classical deterministic precision structure or qualitative nugget regularization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
