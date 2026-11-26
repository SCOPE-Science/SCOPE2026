# Independent mathematical audit

## correctness

PASS

At each p-grid point in binade k the strict a < u_E <= u_k bound keeps the exact sum below the next grid point, including the last point before a power of two. Deterministic guard truncation keeps exactly floor(a/v_k) guard units. Hence the first binade losing every unit starts at L=E+1+floor(log2(a/v_E)), including exact threshold equality cases. Before L each upward probability q_k is positive, constant over the 2^(p-1) increments in that binade. The independent trial stream regenerates at each first upward passage; geometric waiting times therefore give the stated independent negative-binomial convolution, PGF and moments. In ideal rounding all one-state passage times are finite almost surely, and their countable intersection gives divergence in the stipulated unbounded-exponent model. An independent exact forward propagation on enumerated p- and guard grids matched probability coefficients through t=30 in two three-binade cases (one at a guard threshold); this supplements, not replaces, the proof.

## originality

PASS

Prior operator definitions, small-addend loss and stagnation are not novel. The inspected results do not give the absorbing exponent together with the full fixed-increment binade passage law in the frozen model.

## value

PASS

A fixed increment is a natural recursive-summation stress test, not an arbitrary numerical slice. The result separates an infinite-time failure from the known local bias: it says exactly where the sum stalls and quantifies when, including an exact exponentially large mean delay at the first guard threshold. The law is useful when assessing whether finite-horizon progress masks eventual stagnation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
