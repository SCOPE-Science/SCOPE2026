# Independent mathematical audit

## correctness

PASS

Changing from ordered samples to nonnegative increments puts the interpolant at each \(t\) as a linear functional on a simplex with coefficients \(1,q_0,q_1,q_2\), where \(q_0=1+\sigma t(1-t)^2\), \(0\le q_1\le1\), and \(q_2=-\sigma t^2(1-t)\). Thus the exact pointwise extrema allocate all variation to \(d_0\) or \(d_2\), and the two cubic shape factors both have maximum \(4/27\). Fresh symbolic algebra independently verified the coefficient factorization and extremizers; the strict-positive witness follows by direct substitution.

## originality

PASS

Huang--Han--Gong's complete primary article explicitly states that original Catmull--Rom overshoots can violate global stability and develops a monotonic/adaptive repair, but it gives no exact bounded-data overshoot constant; indeed it notes the lack of a theoretical stability characterization for the original scheme. The exact \(2/27\) standard defect, the whole \(\sigma\)-profile and the strict-positive monotone witness were not found in targeted Resultary searches. The qualitative overshoot phenomenon is prior; originality is confined to the sharp extremal range.

## value

PASS

The exact global-range defect is a natural stability invariant for a standard interpolation rule whose overshoot is explicitly identified as problematic in the literature. The theorem gives the optimal constant, extremizing data, the entire tension path, and a strictly increasing positive counterexample family, so it is a motivated sharp classification rather than a routine sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
