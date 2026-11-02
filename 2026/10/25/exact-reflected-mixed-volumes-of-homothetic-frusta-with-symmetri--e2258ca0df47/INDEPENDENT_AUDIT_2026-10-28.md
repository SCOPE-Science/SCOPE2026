# Independent mathematical audit

## correctness

PASS

For lambda>=0 the horizontal z-section of F_a(B)+lambda(-F_a(B)) is a union of centered homothetic copies indexed by u−lambda v=z, u,v in [0,1]. Because -B=B, their scale is 1+lambda−(1−a)(u+lambda v), maximized at u+lambda v=|z|; the copies are nested, so the exact section is (1+lambda−(1−a)|z|)B for -lambda<=z<=1. Integrating its (d−1)-volume gives the polynomial ratio [2(1+lambda)^d−(a+lambda)^d−(1+a lambda)^d]/(1−a^d), normalized by vol(F_a(B)); at a=1 F_1(B) is a centrally symmetric prism modulo translation, yielding (1+lambda)^d. Comparing coefficients with binomial mixed-volume convention gives R_dk=(2−a^k−a^(d−k))/(1−a^d)=1+(1−a^k)(1−a^(d−k))/(1−a^d); k=0,d each 1. A direct derivative of (1−u)(1−v)/(1−uv), u=a^k,v=a^(d−k), proves strict decreasing with a for 0<a<1. Difference R_{k+1}−R_k=(1−a)(a^k−a^(d-k-1))/(1−a^d) establishes symmetric strict unimodality and central tie when d odd. Independent convex-hull Minkowski-sum computations for d=3,4, a=0,.2,.6,1 and lambda=.2,.8,1.4 agree. The nested-section argument, not the finite hull sample, proves arbitrary B and d.

## originality

PASS

The universal Godbersen inequality is known, and prior work computes mixed volumes for a truncated simplex and Santaló/Mahler functionals for homothetic frusta. Here the full reflected polynomial for every centrally symmetric (not necessarily polygonal) base, including all coefficients and exact monotone profile, is not a consequence of either inspected result.

## value

PASS

An exact closed-form all-index mixed-volume law for a natural cone-to-prism family is independently useful in convex geometry, especially because its normalized values are independent of arbitrary base shape and interpolate sharp extremal endpoints; this does not require claiming a new universal inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
