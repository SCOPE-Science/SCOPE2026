# Independent mathematical audit

## correctness

PASS

Reconstructed RESULT.md lines 49–123. Scale h to one and write v=vol_m(B). Both cone halves have sections homothetic to B, so the volume is v(1+t)/(m+1). The reflected section at height y intersects two scaled copies of B; its volume cannot exceed the volume of the smaller one, and concentric copies attain that bound at every height. At an interior axial height c, a nonzero horizontal displacement strictly reduces the overlap at y=c because a bounded full-dimensional convex body cannot agree in volume with a nontrivial translate. Continuity of slice overlap (the scaled and translated convex boundaries are null) extends that loss to a positive-height set. For 0<t<1, integrate the minimum slice radius to the power m over y≤c and double. For −t≤c≤0 the lower radius is minimal, for 0≤c≤(1−t)/2 it switches to 1−2c+y at y=−2ct/(1−t), and above (1−t)/2 that latter radius is minimal throughout the active interval. This gives the three branches; the outer ones are respectively increasing and decreasing, and in the middle the derivative changes sign exactly once at 1−c=2^(1/m)(1−2c/(1−t)). This gives the stated c* and maximum. At t=0 integrate over [max(0,2c−1),c] with radius 1−2c+y; at t=1 central symmetry and strict loss under nontrivial translation give the unique origin. The ratio has strictly positive derivative on the compact interval, proving global inversion and its dimensionwise Lipschitz property. The first axial moment has upper and lower contributions v/((m+1)(m+2)) and −t² times that number; the centroid gap and equality follow from 2^(1/m)≤1+1/m. Expanding 2^(1/m) at large m gives the displayed limit. The finite checker and recorded verification were inspected, not executed; the argument covers arbitrary nonsmooth full-dimensional B without inference from the cubical examples.

## originality

PASS

Pass is limited to the full asymmetric-bipyramid profile for a freely varying positive height ratio with arbitrary symmetric equator, its explicit maximizing location and the resulting comparison/limit. The underlying overlap invariant, general uniqueness, planar triangle case, and all-dimensional single-cone endpoint are covered and not credited as distinct. The strongest matching indexed statement treats frusta, whose nondegenerate positive-parameter shapes and profile differ. The assessment is to the best of checked knowledge, not a priority determination.

## value

PASS

This gives a natural body's exact maximal centrally symmetric volume and the location of its core in every dimension, without knowing the shape of the equator. The inverse recovers a geometric asymmetry parameter from an intrinsic volume ratio; the centroid comparison shows why an easily computed conventional center is generally not optimal. These are meaningful explicit outputs beyond a generic uniqueness theorem, lower bound, or one-sided endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
