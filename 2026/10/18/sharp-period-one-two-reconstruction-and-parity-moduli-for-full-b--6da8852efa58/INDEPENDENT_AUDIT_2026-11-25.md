# Independent mathematical audit

## correctness

PASS

The inverse branch on each closed lap is a strict contraction, hence has one fixed point; no interior knot is fixed, and sorting recovers the branch indices. The first point is always 0, and the last is 1 exactly in odd parity. For each interior lap, solving its affine fixed-point equation expresses the next knot as an affine function of the previous one with nonzero slope. Starting at t=b1, the final even lap determines b_(m-1) from p_m=1/(2-b_(m-1)), so it determines t, including m=2. The final odd lap instead gives p_m=1 identically; strict ordering cuts the one-dimensional affine fiber into a nonempty open interval. A knot cannot be in an exact two-cycle since it maps to an endpoint and endpoints are fixed or map to the fixed endpoint 0. Compositions of two inverse branches are contractions; distinct-lap ordered pairs yield interior primitive points, same-lap pairs yield fixed points, and each primitive point has a unique ordered itinerary. Thus the minimum lies in lap 1 with successor in lap 2 by ordering of inverse ranges. With u=b2, the two-branch return gives q=tu/(1+t(u-t)); substituting p2=u/(1+u-t) gives the claimed inversion and positive fiber derivative. The open odd fiber proves sharp necessity; no noise or nonaffine claim is needed. Exact forward evaluations confirmed the two three-lap examples in /workspace/branches/audit_witnesses.py; the proof covers all real strict knot vectors.

## originality

PASS

Pass for the stated continuous, alternating, variable-knot affine class: the explicit parity of fixed-point fibers and a sharp finite cutoff with one least two-periodic coordinate are not furnished by full-period rigidity. A discontinuous Bernoulli model already demonstrates the analogous one-scalar identification pattern; it is not credited as a new general principle here. Comparison is bounded, not a priority certification.

## value

PASS

Geometric positions carry information that periodic orbit counts cannot distinguish in this full-branch family. The theorem determines the complete fixed-data fiber, gives the minimal maximum period in both parities, and shows how one canonically selected point removes the remaining modulus. This is actionable exact identification in a natural model, not a generic robustness claim or just the enumeration of periodic points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
