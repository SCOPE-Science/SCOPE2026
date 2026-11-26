# Independent mathematical audit

## correctness

PASS

For positive gap k, the two floor equations give two unit half-open intervals whose displacement has magnitude k*epsilon. Their intersection is empty at and beyond k*epsilon=1. Choosing the smaller endpoint x=−floor(k/2) places the nonempty phase window wholly within [0,q); other x translate it by integer multiples of q and do not intersect that interval. The even windows [j*epsilon,1−j*epsilon) and the sign-dependent odd windows are nested on disjoint phase ranges. Thus N>=m is exactly the union of the even window at gap 2m and the odd one at 2m−1, including the endpoint convention. Counting integers with the resulting weak lower-window and strict upper-window tests gives a floor or ceiling count within one of the triangular height divided by epsilon, with the odd cutoff shifted by at most one mesh cell; [2,q) on the expanding side contributes zero. Setting m=floor(t/epsilon)+1 in the survival formula proves the stated CDF bound by Lipschitz continuity of positive part, and the bounded support gives moment convergence. On N>0 the available gaps are the first N even or odd gaps; coupling the rank to ceil(NV) makes the error relative to 2*epsilon*N*V at most 2*epsilon. The zero-cycle probability tends to zero, so conditioning does not affect the phase limit. Rescaling the phase to [0,2) gives the uniform triangular height independently of V, proving the joint law and the product-of-uniforms marginal. Independent direct iteration also agreed throughout 748 rational phase cells, with 2,534 profile/survival checks in addition to direct gap-list and half-open-cell checks.

## originality

PASS

Do not credit the fixed-offset periodic-orbit census. Credit the explicit two-sided parameter-ensemble law, pointwise profile and, in particular, the joint gap limit for uniform-within-phase cycle sampling. The strongest exact comparator repeats the contraction-side count formula and leading profile on a narrower parameter range; its later index date is reported without assigning historical priority. Its result does not state the two-sided law or the joint mark limit.

## value

PASS

A natural uniform translation-conjugacy phase turns the proliferation of periodic orbits near slope −1 into an exact finite-parameter law, including the different normalizations on the two sides. The marked law adds geometric information: the gaps are asymptotically uniform up to the phase-dependent maximum, while mixing over phases creates a logarithmic singularity. The within-phase sampling distinction makes this more than a restatement of the fixed-parameter census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
