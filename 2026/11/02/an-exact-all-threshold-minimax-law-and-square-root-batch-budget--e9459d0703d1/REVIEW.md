# Independent mathematical audit

## correctness

PASS

Completing the square along one line gives the squared normalized energy-coordinate inner product. After rotating and scaling the energy covariance to diag(1,K), Gaussian radial integration gives the stated projective angular density with denominator K cos²φ + sin²φ. The success arc has radius r=arccos(sqrt(t)); differentiating its mass at the two endpoints gives the difference of reciprocal denominators with numerator (K−1) sin(2θ) sin(2r). This is strictly positive for interior θ from the small to large eigenaxis if K>1 and constant in angle when K=1. Thus the worst start is unique as a projective direction for each threshold if K>1. At that axis the squared alignment is 1/(1+K C²) for a standard Cauchy C, giving the stated CDF; there are no atoms at internal thresholds. Independence raises the CDF to the m-th power at the same fixed start. Strict increase in K gives the unique covariance ray proportional to H⁻¹. Taking logs gives the ceiling, and −sqrt(K) log F_K tends to (2/π)sqrt((1−t)/t), proving the coefficient and all three regimes. Partial fractions of the Cauchy integral give mean 1/(1+sqrt(K)), and setting the CDF to 1/2 gives median 1/(1+K). These conclusions do not describe sequential updates or minimization over the joint span.

## originality

PASS

The distinct contribution supported by the comparison is the precise threshold-wise extremum over starts, with equality cases, for fixed-start independent Gaussian exact line candidates, and the resulting sharp batch law. Exact random line search, covariance adaptation including the inverse-Hessian design idea, standard direction distributions, and order statistics are prior or elementary ingredients.

## value

PASS

The sharp quantile budget quantifies conditioning in a different way from expected decrease: at the bad axis the single-candidate mean and median scale differently, and a fixed reliability level requires order sqrt(κ) independent trials with an exact leading constant. This is a natural benchmark for parallel exact-line selection, not a claim about an optimizer's total runtime.

The dated certificate retains the supplied scientific assessment, sources and limitations.
