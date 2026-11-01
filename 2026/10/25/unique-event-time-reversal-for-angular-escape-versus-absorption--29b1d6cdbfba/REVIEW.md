# Independent mathematical audit

## correctness

PASS

For angular Brownian exit T from (−L,L), generator D∂² and independent Exp(κ) E, solve backward ODE: F=E[e^(−κT)]=cosh(uz)/cosh z, u=|θ0|/L,z=L√(κ/D). Conditional E[T|T<E]=−F’/F and E[E|E<T]=1/κ+F’/(1−F), so signed difference is H(z,u)/[κ(1−F)]. H(z,0)>0, H(z,u)<0 near u=1; its derivative changes from negative to positive exactly once since Q(w)=sech(w)+(w/sinh w)sech²w decreases. Exactly one interior zero follows. Taylor expansion gives u_c=1/√5+(8√5/1875)z²+O(z⁴); u=1−w/z limit w/2−1+exp(−w) yields w*=1.59362426004... positive root. Independently numerically evaluated thresholds z=.2..40 and confirmed strong layer; analytic proof covers all positive parameters.

## originality

PASS

Bressloff 2023 already derives both conditional times and plots their angle dependence; these quantities themselves are NOT new. The source’s full accessible §3/figure 4 does not contain the all-rate one-crossing theorem with its analytic small/large-rate limiting constants. The new global sign-shape proof is a motivated continuation; possible broader killed-Brownian theorem remains risk.

## value

PASS

The unique angular event-order crossover for every reaction/diffusion ratio is a natural structural fact about two different conditional first-passage times already known separately. It replaces plotted behavior by a universal monotonicity theorem and gives two nontrivial endpoint scales, including a physical √(D/κ) boundary layer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
