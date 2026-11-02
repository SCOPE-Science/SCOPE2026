# Independent mathematical audit

## correctness

PASS

Fiber integration gives vol(B1^d+[-h,h]e1)=2^d(1+dh)/d!. The polar inequality max_j|uj|+h|u1|<=1 has volume 2^d/(dh)[1-(1+h)^(-d)], hence the asserted normalized product. With t=(1+h)^-1 its excess over one is (sum_{j=1}^{d-1}t^j-(d-1)t^d)/d>0; dividing the derivative by t^(d-1) produces a strictly decreasing root equation with one maximizer for every integer d>=2. Setting alpha=dh gives the strict envelope g(alpha)=(1+1/alpha)(1-exp(-alpha)), uniquely maximized at the positive alpha solving exp(alpha)=1+alpha+alpha^2; monotonicity in d for fixed alpha and compactness of maximizing alpha show increasing peaks to C*=1.298425607525639... and dh_d->alpha*. Direct rational polynomial-integration and volume-product comparisons passed 33 independent low-dimensional parameter cases; universal assertions use the proof.

## originality

PASS

Existing Hanner local-minimality work concerns lower stability, not this global upper envelope. Full published cube/cross-polytope intersection and cube plus full cross-polytope Minkowski interpolation statements are geometrically different and do not specialize to a single-axis cross-polytope extrusion. The latter has the same scalar equation exp(alpha)=1+alpha+alpha^2 in a growing-dimensional saddle, which is explicitly acknowledged as prior shared numerical structure, not assumed independent novelty. The complete present profile and all-dimension optimal bound were not shown by inspected antecedents.

## value

PASS

This symmetric one-coordinate extrusion interpolates between two natural Hanner-type Mahler-minimizer shapes. A complete all-dimensional positive excursion, unique finite optimum, strictly increasing normalized peaks, and a sharp dimension-free ceiling are meaningful benchmarks for local/global volume-product stability; not simply a computed constant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
