# Independent mathematical audit

## correctness

PASS

The first new transmission has rate 2λ and no stifling competitor. Immediately afterwards the two endpoints of the informed interval are active spreaders; the original seed is itself the second tip. Each has a permanently informed inward neighbor and an ignorant outward neighbor, with respective stifling and transmission rates 1 and λ. Directed clocks driving the tips are independent even when they share the first informed edge, because stifling changes only the contacting spreader and informed status never reverts. After a birth the moving tip has fresh clocks; an old interior spreader cannot affect future births. This reduces each side to rate-λ Poisson births killed at independent Exp(1), independently of the initial time and the other side. The probability of no birth later than u is 1−e^(−u)+e^(−u)/(1+λ)=1−a e^(−u); finiteness follows from killing in finite time. The squared CDF for the maximum gives the atom, density, transform, and tail integral stated in the finding. Differentiation gives the cited cubic over a positive denominator, and its single positive sign change and endpoint signs give one strict minimizer. The mean minus 3/2 is (1−λ−λ²)/(2λ(1+λ)²), so the upper-rate limit is approached from below. Direct bisection independently gives 1.4811943040920155 and mean 1.3533164361622998. The uploaded sitewise Monte Carlo checker was inspected, not run; the argument is analytic.

## originality

PASS

The supported distinct claim is the stopping-time law in physical time and the resulting nonmonotone mean for the unit-stifling infinite-line process, not the frontier geometry, final range or almost-sure extinction. The closest inspected prior uses identical transition rates but proves the spatial count at absorption by geometric ranges. It does not specify the time of the last birth or the temporal combination of the two fronts. The other closest catalogue and literature matches differ in observable or rates and geometry. No exact or stronger covering statement was established in the checks below.

## value

PASS

On the natural infinite nearest-neighbor benchmark, the elapsed time of the last new spread is not measured by ultimate reach or extinction. The exact law gives deadline probabilities and an explicit, genuinely nonmonotone mean despite increasing expected reach. It isolates the competition between the faster initial birth and the longer final activity of the surviving fronts, with a sharp and reproducible rate boundary. The result is not just a moment at one chosen rate or a renaming of the final-count law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
