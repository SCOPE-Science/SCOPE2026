# Independent mathematical audit

## correctness

PASS

Reconstructed the argument for the displayed map with literal first-coordinate linear multiplier −1. For x₀≠0, |x_n| decreases to a limit U. If U>0, |x_{n+1}/x_n|→1 forces y_n→0; the identity x_n=y_{n+1}−by_n then contradicts U>0. Once x_n→0, summation of the stable filter with |b|<1 gives y_n→0. The axis orbit x₀=0 is exactly (0,b^n y₀). For other orbits let q_n=x_n², r_n=y_n/x_n, s_n=1/q_n and D=1+b. The exact r-recurrence can be treated along the orbit as affine with slope −b(1+y_n²), eventually uniformly contractive, and constant term tending to −1. Thus r_n→−1/D, and Δs_n=2r_n²+r_n⁴q_n→c=2/D², giving q_n∼1/(cn). In the r equation the first forcing after subtracting its limit is −q_n/D³, and geometric convolution first gives r_n+1/D=O(1/n). Subtracting −q_n/D⁴ then leaves a stable recurrence forced at O(n⁻²), since q_{n+1}−q_n=O(q_n²). This proves the stable-fiber expansion. The increment has coefficient H=4/D⁵+1/D⁴=(5+b)/D⁵ on q_n, so s_n=cn+O(log n). Subtracting cn+(H/c)log n leaves increments O(log n/n²); their absolute summability and tail estimate give finite C and O(log n/n). Sign alternation and the ratio limit give both signed amplitudes, including the b-independent transverse one. Inspected the supplied symbolic/finite-iterate checker without executing it; a finite set of orbits cannot establish these quantifiers or the asymptotic error.

## originality

PASS

The rational map and generic critical flip exponent are prior context. Distinct supported content is convergence on the full real plane on the critical slice together with the explicit orbital logarithmic term, finite renormalized constant and error bound. Related catalogue results are for different maps. The closest same-map papers were not readable in the attempted lawful copies; possible overlap, particularly with local coefficients, is not excluded or treated as negative evidence. No independent priority claim is made for the generic exponent or for constants that an earlier map-specific local expansion may imply.

## value

PASS

For this previously studied map the result gives more than the usual local power law: it accounts for every finite initial state, isolates the stable-axis exception and shows that the first accumulated correction to inverse-square growth is logarithmic with a controlled remainder and a finite orbit-dependent offset. This distinguishes geometric transients and critical relaxation in an exact example and gives physical-coordinate coefficients against which local normal-form approximations can be checked.

The dated certificate retains the supplied scientific assessment, sources and limitations.
