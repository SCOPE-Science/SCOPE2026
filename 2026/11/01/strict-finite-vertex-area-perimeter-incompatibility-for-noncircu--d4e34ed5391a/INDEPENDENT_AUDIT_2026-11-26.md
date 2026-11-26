# Independent mathematical audit

## correctness

PASS

Verified the all-phase claim analytically. Under inverse ellipse scaling, area maximization reduces to maximizing the sum of sines of the cyclic gaps. On the compact space with nonnegative gaps, a coincident-vertex polygon is not a maximizer: insertion on an open boundary arc makes a positive-area addition for a polygon with ≥3 distinct vertices, or yields positive area starting with ≤2. At an interior maximum the adjacent two-gap sine identity makes each adjacent gap pair equal. For the resulting equal-angle family the moving-vertex tangent is the average of the two unnormalized chord directions divided by cos(h); dotting it with the difference of incident unit chord vectors gives D_j=(F⁻−F⁺)(1−cos θ)/(2 cos h). The determinant ab sin(2h) makes the second factor strictly positive, and the squared norm difference is −(a²−b²)sin(2h)sin(2t_j). Thus simultaneous vanishing requires n=4 and a vertex phase in (π/2)Z. The grid modulo π gives max |sin(2t_j)|≥cos(π/(2N)); F⁻+F⁺≤2a and 1−cos θ≥sin²θ/2 give the stated G. Moving a single angle by up to h preserves order and gives incident gaps in [h,3h]⊂[h,π], so chord norms are at least 2b sin(h/2). The twice-differentiated norm bound then gives precisely H and the Taylor increment ≥G min(h,G/H)/2. Compactness gives a maximum; a collapsed polygon can strictly increase perimeter by insertion by strict triangle inequality, so an actual distinct-vertex maximum exists. The tests were inspected as diagnostics, not executed or used as a continuum proof. No claim of global maximality at n=4.

## originality

PASS

The affine-area extremizers, their restricted phase selection, and the positive explicit triangle-order gap already have precedents. The distinct claim is the simultaneous independent-vertex stationarity classification for all n, together with a fixed-(ellipse,n) phase-uniform explicit bound for all nonexceptional orders. The inspected billiard literature establishes the reflection mechanism but does not solve the equal-affine-angle restriction or give this quantitative gap.

## value

PASS

A natural comparison of two classical objective functions at fixed vertex count gives an exact exceptional stationarity case and an explicit gain in every other case. It genuinely distinguishes unrestricted optimization from the rotating family and generalizes the previously treated triangle case across vertex orders without an asymptotic assumption.

The dated certificate retains the supplied scientific assessment, sources and limitations.
