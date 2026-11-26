# Independent mathematical audit

## correctness

PASS

Conditioning on the independent parent choice for m>i gives the weighted joint PGF recurrence with the old depth marker retained. Updating the weighted sum from m−1 to m multiplies the joint PGF for the next label by 1−p_m+p_m z, giving exactly the independent convolution in the younger coordinate, including the empty sum. The weighted depth mean increments by p_m(1+xi_m) and the innovations are orthogonal; common terms in the two centered depths give the displayed covariance. Parent depths 0 and 1 both have strictly positive conditional probabilities, proving strictness for i≥3. For the upper bound, Bernoulli convolution is log-concave and hence unimodal, so unit-shift TV is its maximum mass; shift telescoping and then averaging over the coupled fibers give the factor E|Y−Y'|. Fourier inversion with |phi(t)|≤exp(−2V sin²(t/2)) gives the stated constant. For the lower bound, the summed centered absolute third moments are at most V and the same Fourier bound dominates the rescaled inversion integral. This proves the central local limit for each bounded offset, giving a threshold-test discrepancy C_i/((i−1)sqrt(2πV)) in absolute value to first order. The [0,1] test is admissible for the specified TV convention. Power sums give V asymptotic to (alpha+1)log j or log log j. In the summable power case the Bernoulli tail probability gives TV convergence; finite second moments and positive limiting covariance force strictly positive limiting TV. No finite simulation is used for any infinite assertion.

## originality

PASS

The repaired claim credits the martingale covariance and one-vertex variance regimes as prior consequences. Inspected earlier statements do not supply the exact fixed-label bivariate law and two-sided TV order to the product law or the persistent-dependence power regime. The rate transfers from standard smoothing estimates only after identifying this specific joint signal and giving a nonzero matching lower bound.

## value

PASS

Even with strictly persistent covariance, the repaired theorem shows sharp asymptotic independence in total variation whenever younger-label noise grows, and identifies when dependence instead persists in the natural power family. The lower bound makes the answer quantitative rather than qualitative, and the exact joint-law factorization explains why noise masks but does not erase the covariance. This is useful beyond reciting the known one-depth phase boundary or measuring correlation alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
