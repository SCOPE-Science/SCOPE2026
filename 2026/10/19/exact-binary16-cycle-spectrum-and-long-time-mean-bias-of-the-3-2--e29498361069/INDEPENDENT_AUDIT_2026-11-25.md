# Independent mathematical audit

## correctness

PASS

The unsigned positive encodings 0 through 0x3bff comprise 15·1024 states, counting one zero and keeping subnormals. Values are integers in units of 2⁻²⁴. An independent reproduction decoded these states and rounded the product using integer quotient/remainder against the binade spacing (even significand at ties), rather than midpoint search. Subtracting one at rounded products in [1,3/2] is exact: the difference is a multiple of 2⁻¹⁰ in [0,1/2]. The computed graph matched the source SHA-256 and all five (period, basin size, minimum encoding, max entry depth) tuples using forward path revisits and reverse label propagation rather than indegree peeling. Cycle means use exact rational arithmetic. Independently assigning each adjacent encoding gap half to each endpoint assigns the upper endpoint's half-cell to the basin of F(1)=1/2, without adding 1 to the stored domain. This gave weights with numerator vector (12777057,68656,7273607,4398294,9036818) and denominator 2²⁵; the stored and rounded means were 825722879/2751463424 and 13332128797227/45079976738816. Integrating the standard Parry density gives the ratio of the weighted endpoint-orbit square sum divided by twice the weighted linear sum. An exact 120-term dyadic-orbit reproduction bounds the denominator tail by 3(2/3)^120 and the numerator tail by half that. It recovered the stated enclosure width and certified the strict real-minus-rounded gap between 0.103 and 0.104.

## originality

PASS

The independent contribution supported by the comparisons is the exact ensemble-weighted long-time mean calculation, especially for uniform real initialization with the rounding-to-one cell, and its certified gap. The period/basin graph itself has an exact indexed overlap: the later two-rounding-order result's B map has the identical successor digest and period/basin pairs. Neither the general finite-precision pathology, the arithmetic model, the invariant density, the cell-weight method, nor the shared graph census alone warrants originality credit.

## value

PASS

The 3/2 map is an established finite-precision benchmark. The exact long-time scalar observable distinguishes uniform bit-pattern initialization from nearest rounding of a real-uniform input; these are easy to conflate and give measurably different expectations. The certified gap against the real invariant mean gives a quantitative reference for assessing precision and initialization choices without finite-orbit sampling or empirical burn-in.

The dated certificate retains the supplied scientific assessment, sources and limitations.
