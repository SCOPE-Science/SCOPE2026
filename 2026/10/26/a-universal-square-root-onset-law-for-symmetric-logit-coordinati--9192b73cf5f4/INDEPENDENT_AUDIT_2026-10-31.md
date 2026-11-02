# Independent mathematical audit

## correctness

PASS

Exact change z=x-y, v=z-dot conjugates the planar logit field to z-double-dot+f(z)z-dot+g(z)=0 with f=1-(lambda/4)sech^2(lambda*z/2) and g=(alpha/2)tanh(lambda*z/2). Direct differentiation checks the map and restoring force. For lambda<=4, proper energy E=v^2/2+(alpha/lambda)log cosh(lambda*z/2) decreases, and the only invariant subset with f(z)*v^2=0 is the origin; LaSalle includes equality lambda=4. For lambda>4, odd F=integral f has unique positive crossing, is increasing thereafter, and g is odd positive for z>0 with coercive potential; classical Lienard uniqueness yields one attracting nonconstant orbit. Logistic reflection fixes its half-period average. Taylor f=-delta/4+4z^2+O(delta*z^2+z^4), g=alpha*z+O(delta*z+z^3), and averaging <sin^2>=1/2, <sin^2 cos^2>=1/8 yield A-dot=delta A/8-A^3/2+higher terms, so the Hopf amplitude satisfies A^2=delta/4+O(delta^2) and T->2pi/sqrt(alpha). The exact inverse x=(S_lambda(z)+alpha/2-v)/(1+alpha), y=x-z gives centered x and y amplitudes 1/(2sqrt(1+alpha)) and sqrt(alpha)/(2sqrt(1+alpha)), respectively. Independent SymPy verification checked f,g and critical z^2 coefficient 4; finite simulation is not treated as the all-parameter proof.

## originality

PASS

Qualitative oscillations and Hopf square-root scaling are not new. The surviving precise model-specific result is the globally sharp critical case, exactly one orbit, and the explicit rate-independent 1/2 payoff-gap leading coefficient with both original coordinate amplitudes and exact cycle means. The inspected 2021/2022 model paper discusses the orbit and explicitly conjectures uniqueness rather than giving the three sharp coefficients. No identical source found, with ordinary Lienard and Hopf theory acknowledged as prior machinery.

## value

PASS

A universal *physical-coordinate* amplitude coefficient, including the critical equality and a global unique cycle, is a natural quantitative follow-up to the original logit feedback game. This is not valued for rediscovering generic Hopf/Lienard theory but for explicitly determining the onset magnitude in payoff and behavior variables uniformly over feedback rate alpha. A future researcher using this benchmark can require the coefficient and exact cycle means for quantitative comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.
