# Independent mathematical audit

## correctness

PASS

For the repaired RESULT.md, dividing the scalar skew difference by |a|^p+|b|^p reduces its absolute value to the one-variable quotient with u in (0,1), up to endpoint zeros and inversion. With u=exp(−s), stationarity gives cosh((p−1)s)=(p−1)cosh s. The log-derivative of the cosh ratio is (p−1)tanh((p−1)s)−tanh s, with strict sign of p−2 for s>0; the endpoint values give existence and uniqueness on either side of p=2. Equality in the nonnegative pointwise slack therefore forces exactly the indicated signed ratios almost everywhere off the common zero set, and unit normalization forces their |x|^p masses 1/(1+u^p), u^p/(1+u^p). Conversely the two bands make the slack zero. The disjoint-support construction gives two output coefficient lists identical up to permutation and signs, for every τ. Scalar Taylor bounds integrated using Hölder give the uniform O_p(τ^min(p,2)) norm remainders; arithmetic-mean domination supplies the lower bound uniformly even at t=∞ and the balanced pair supplies the common upper bound. Comparing these proves the near-minimizer slack estimate, not a norm-distance claim. The repair explicitly separates the p=2 degeneracy (D_2 identically zero, an orthogonal pair upper bounds all means). Dividing the stationarity residual by p−2 leaves a smooth equation near the Hilbert point; s sinh s−cosh s has derivative s cosh s>0 at its positive root, giving the displayed cusp by the implicit function theorem. Triple and quintuple angles give the stated p=4 and p=6 values. Independent finite replay: python3 -B /workspace/branches/reproduce_frozen_checks.py 1 checked eight direct scalar maximizations and 24 balanced output pairs; it does not certify universal expansions. The frozen numerical checker was inspected, not run.

## originality

PASS

Pass applies to the repaired focus: unique optimizer and the signed-band equality and quantitative deficit classification on general real non-Hilbert Lp spaces beyond the overlapping quartic specialization. The scalar variational coefficient M_p is in older numerical-radius literature. The sharp first-order transfer in t follows from Xu–Liu, and the distinct same-day quartic results give the actual equality and deficit, not just matching parameters. The repair credits all of this and retains the law and quartic formulas as context. Neither the same-day date nor the catalogue itself assigns chronological priority. In the retrieved nonquartic material no result supplied the full signed-band structure and uniform near-minimizer estimate.

## value

PASS

The comparison of a known scalar numerical radius to the geometry of equality in an infinite-dimensional pairwise perturbation is useful beyond the numerical coefficient. Two uniquely located bands, their exact masses, and the near-optimal slack condition provide a reusable diagnostic throughout the non-Hilbert range and for the extreme outer mean, whereas a single attaining two-vector construction or a quartic square identity does not describe that range. The scope is first-order and integrated, not a finite-skew or strong metric stability theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
