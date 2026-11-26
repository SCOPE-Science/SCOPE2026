# Independent mathematical audit

## correctness

PASS

Write C=αI+S and D=(αI−H)(αI+H)^−1. The similarity CMC^−1=DQ with orthogonal Q=(αI−S)C^−1 gives the spectral bound, not in general the ordinary Euclidean norm bound. In real dimension two, S²=−s²I makes C a scalar times an orthogonal matrix; thus the original M and DQ have the same singular values. In dimension one S=0. For the displayed dimension-three family use k=(e1−e3)/sqrt(2), h=(e1+e3)/sqrt(2), m=e2. D swaps k,h with factor 1/3 and kills m. S kills k, sends h to −sqrt(2)t m and m to sqrt(2)t h. The image of DQ lies in span(k,h), and its restriction there sends k to h/3 and h to rk/3 with r=(2−t²)/(2+t²). Its characteristic polynomial is therefore λ(λ²−r/9), including the zero-rate case t²=2. Also D(2I−S)m=−sqrt(2)t k/3; C^−1 divides that vector by two. This gives the asserted exact image at t=6 and lower bound t/(3 sqrt(2)) for all t. The classical factor is minimized by balancing the two endpoint magnitudes at α=2 and equals 1/3. Every A is positive definite since its skew part contributes zero to xᵀAx. The conclusion is exact one-step growth across a family, not unbounded powers of an individual matrix; the fixed data do not include the actual spectral radius or the full system's condition number. The rational sample checker was read only, and the all-t and low-dimensional results were verified analytically.

## originality

PASS

Credit the joint HSS-specific sharp real dimension boundary, especially the explicit fixed-H, fixed-α arbitrarily amplifying 3D family. Do not credit the prior Cayley similarity, weighted-norm contraction, standard optimal bound parameter, or the low-dimensional identity in isolation as a substantial departure from that similarity.

## value

PASS

Sharp minimal dimension for losing practical stepwise Euclidean error control answers a natural distinction left by a spectral-rate guarantee. The fixed-H construction shows that the parameters practically used to select α and predict a rate do not control even one Euclidean error step, and demonstrates the phenomenon at its first possible real dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
