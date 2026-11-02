# Scientific review: exact John–Löwner ellipsoids of orthogonal block bicylinders

## Correctness — PASS

The proof treats every integer \(p,q\ge1\) with \(p+q\ge3\) and every \(a\ge b>0\). Global uniqueness forces independent orthogonal-block symmetry; exact endpoint tests characterize both ellipsoid inclusions. The inner semiaxes are optimal by direct coordinate monotonicity. The outer determinant reduces to a strictly concave logarithm on \((0,1)\); differentiation gives the stated radical and both sharp limits. The two-layer measure has positive weights summing to one, and its affine-normalized covariance is exactly \(I_d/d\); the common intersection ridge is shown to be the complete contact locus. The included verifier passed 4,791 exact-identity and independent numerical checks. Those checks support the all-parameter analytic proof but are not exhaustive computations.

## Originality — PASS (provisional historical priority)

The three-dimensional scalar bicylinder and the multi-coordinate intersection of individual cylinders are not claimed: the restriction \(p+q\ge3\) means at least one full quadratic Euclidean block. Equivalences and broader-result implications were compared against the three-dimensional Steinmetz geometry, the general John–Löwner contact theorems [1–3], and geometric and optimal-design literature. No source examined furnished the full exact semiaxes, contact ridge, design and all-dimension sharp ratio. A related SIAM chapter was available only through its contents, so its full text was not certified as non-covering. An unknown earlier equivalent calculation remains a priority risk.

## Mathematical value — PASS

The theorem gives a complete, closed-form extremal classification of genuine higher-dimensional intersections of two perpendicular Euclidean cylinders. Exact contacts and probability weights are structural results, and the strictly monotone volume ratio identifies sharp dimension-dependent distortion. It is not merely an approximation, a bounded special-value table or the established fully scalar case.

## Limitations

The statement does not cover nonorthogonal axes, translated cylinders or general ellipsoidal cross-sections. The computational verification has finitely many test cases and requires documented Python libraries. Independent review and validation have not been performed.

## Closest literature

[1] M. J. Todd (2007), *Minimum-Volume Ellipsoids: Applications, Duality, and Algorithms*, https://people.orie.cornell.edu/~miketodd/ublndetz.pdf.

[2] P. M. Gruber and F. E. Schuster (2012), *An arithmetic proof of John's ellipsoid theorem*, https://arxiv.org/abs/1207.7246.

[3] J.-B. Lasserre (2013), *A generalization of Löwner-John's ellipsoid theorem*, https://arxiv.org/abs/1302.1056.

Self-review: passed. Independent audit: not yet performed.
