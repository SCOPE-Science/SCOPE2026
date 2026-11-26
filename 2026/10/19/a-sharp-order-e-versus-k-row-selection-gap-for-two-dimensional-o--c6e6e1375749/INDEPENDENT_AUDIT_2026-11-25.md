# Independent mathematical audit

## correctness

PASS

For a row of largest squared norm ell and a perpendicular unit vector, the sum of squared perpendicular projections of the other rows is exactly 1. Some pair has Gram determinant ell p with p>=1/(N-1) and trace at most 2 ell; determinant divided by trace bounds its lesser eigenvalue from below. Thus every E optimizer is invertible with sigma_min squared at least 1/[2(N-1)], including N=2, and deleting rows gives sigma_max<=1. In the witness, with t^2=1/(4N-11), the two axis squared sums are both (4N-11)t^2. A nonsingular pair uses both axes, and only pairing the largest horizontal row with a height-2t vertical row attains 2t for sigma_min. All N-3 such choices have kappa squared N-3, while the two height/width-t rows give condition 1. Since all condition numbers are at least 1, this proves the order of the worst multiplicative gap. Independently reproduced by exact rational enumeration for N=5 through 100 (`python3 repro_record1.py`); did not run the supplied checker. The algebra, not the replay, covers all N.

## originality

PASS

The distinct claim is the quantitative same-frame E-versus-K gap and explicit all-maximizer witness, not the already known E-optimal objective or the universal inverse-submatrix bound. Two indexed records substantially overlap mathematically. The leverage record explicitly credits the exact assigned finding as prior for this dimension-order result and disclaims the result as a new contribution; its inspected version cannot be treated as an independent earlier derivation just from its nominal date. The later SPD-Krylov record also covers the gap at the level of order, with a stronger witness in its setting. No verified earlier source established the gap itself; this is a bounded priority assessment, with a chronology limitation stated below.

## value

PASS

It rigorously quantifies how badly a legitimate stability objective can do for a different, scale-invariant objective, even for all ties in the global E optimum. A matching-order explicit witness with K optimum 1 is useful for analyzing unweighted two-row sketches. It illustrates the difference between preserving absolute lengths and minimizing norm distortion, without claiming that conditioning alone controls solver errors or that the example extends to uniform leverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
