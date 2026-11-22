# Independent mathematical audit

## correctness

PASS

For fixed 0<c<1 and lambda>=0 and sufficiently large N, six distinct oriented endpoint arcs of total perimeter 2+c+o(1) have multinomial avoidance probabilities converging to six independent Exp(rate 1/P) gaps. Strictly positive first-order directional derivatives of Euclidean distance around the two and only two diametral vertex pairs AB and AC localize maximizers at O_p(1/N) endpoint offsets; convexity plus local Taylor expansion makes the deficit the minimum of these projected gaps up to o_p(1/N). The apex projections U=min(X,aY), V=min(Y,aX) share two independent Exp(1/P) ray gaps with a=1-c²/2; the B,C endpoint projections are independent Exp(beta) with beta=(1+2/c)/P=1/c. The AC side length contributes exactly lambda/N, yielding min(U+B,lambda+V+C). The joint survivor is exp[-(max(u,v/a)+max(v,u/a))/P], its marginal rate is kappa=(1+1/a)/P=(2-c)/(2-c²), and integration over v/u in [0,a],[a,1/a],[1/a,infty] gives E[UV]*kappa²=1+2a-a² and Corr=a(2-a). Conditioning on U,V proves the claimed CDF. For t<=lambda only U+B contributes; at lambda+h, the extra channel has mass kappa beta exp(-beta lambda)h²/2+O(h³), since on V<=h one has U<=h/a. At lambda=0, both channels yield total kappa beta t²+O(t³), with overlap order at least t³. For lambda_N→infty=o(N), the second channel is pushed out on every bounded scale. Excludes c=1 and boundary degenerations. Independent analytic survival integration and QMC checks verify rates, correlation, and one-channel CDF at three c values; independent finite geometry checks corroborate rather than replace proof.

## originality

PASS

No searched, materially compared prior statement supplies the fixed 0<c<1 perimeter-uniform triangular array with side split lambda/N, dependent apex exponential minima, the complete crossover, or its interior second-derivative jump. Wei Lao (2010), Theorem 5.2, proves the fixed equilateral three-diameter case; the published near-tied triangular result of October 25, 2026 samples triangle INTERIORS at sqrt(n) scale. Schrempp (2017), Section 6.1, explicitly requires disjoint poles for its finite multiple-major-axis setting and smooth area-density assumptions, excluding the shared apex and singular boundary measure. The inaccessible 2002 Appel–Najim–Russo article remains a genuine named priority risk, but its accessible abstract and Schrempp comparison describe area samples and nonshared endpoints; they are not positive coverage evidence. Originality is best-of-knowledge, not certified exhaustiveness.

## value

PASS

The nondegenerate triangle diameter has two adjacent competing maximizers that remain coupled through the shared apex. Asking how a deterministic perturbation of their lengths competes with random order-1/N nearest-endpoint gaps is a natural geometric-probability scaling problem, not a hand-picked numerical slice. The exact joint law, nontrivial positive apex correlation, critical 1/N crossover and measurable second-derivative discontinuity at lambda>0 provide a new phase-boundary description. The zero-split doubled small-tail coefficient is an exact structural endpoint classification; it is neither an elementary corollary of the equilateral c=1 result nor just a Monte Carlo fact. No unsupported claim about downstream theorems is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
