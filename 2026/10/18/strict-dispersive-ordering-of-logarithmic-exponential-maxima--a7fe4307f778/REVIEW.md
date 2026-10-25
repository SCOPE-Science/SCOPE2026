# Independent mathematical audit

## correctness

PASS

Inversion of F_a(y)=(1−e^(−e^y))^a gives Q_a(u)=log[−log(1−u^(1/a))]. Differentiating gives Q_a′(u)=h(u^(1/a))/[u(−log u)], h(z)=z(−log z)/[(1−z)(−log(1−z))]. Its logarithmic derivative has numerator 1−(1−z)/(−log z)−z/(−log(1−z))<0 for 0<z<1, by strict log x<x−1 twice. Thus Q_b′(u)<Q_a′(u) whenever 0<a<b, and integrating gives every strict quantile-span inequality. Quantile coupling with two independent uniforms yields almost-sure strict contraction of pairwise gaps; exponential/double-exponential tails ensure finite second moments, so variance strictly contracts. Independently checked analytic derivative and representative parameter-quantile pairs; not a universal numerical proof.

## originality

PASS

Giam’s 2026 result is already sufficient for the integer variance corollary, which is not claimed novel. The full continuous-a, all-u<v quantile-width comparison is strictly stronger. Inspected DFR-parent order-statistic comparison theorems do not apply since log(E) has strictly increasing hazard e^y; no direct published implication found, with unread Giam body and transform-order generalizations material risks.

## value

PASS

The problem originates in variance of logarithmic exponential maxima (coupon-collector coefficient), but strict dispersive order is substantially stronger than known variance monotonicity: it orders every interquantile width and all coupled two-sample gaps for a natural continuum of power-CDF parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
