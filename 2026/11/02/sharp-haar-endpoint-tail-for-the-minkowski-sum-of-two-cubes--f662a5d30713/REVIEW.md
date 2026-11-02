# Scientific review: Sharp Haar endpoint tail for the Minkowski sum of two cubes

## Correctness — PASS

For arbitrary \(R\in SO(3)\), the six-generator zonotope determinant calculation yields exactly \(V=16(1+L)\). The sign/polar argument proves the global maximum \(L=5\), counts \(96\) distinct proper-rotation maximizers, and yields the common quadratic deficit \(24(\omega_1^2+\omega_2^2)+32\omega_3^2\). The normalized Haar local density \(1/(8\pi^2)\) and compactness prove the exact probability prefactor. Tail integration proves the large-real-\(k\) moment prefactor. The packaged exact rational enumeration confirms \(192\) full-rank sign matrices and \(96\) proper maximizers; the 250 floating-point minor checks had maximum absolute volume discrepancy below \(2.85	imes10^{-14}\). These finite tests do not prove either limiting theorem on their own.

## Originality — PASS (qualified)

Banica, Collins and Schlenker, *On orthogonal matrices maximizing the 1-norm* (arXiv:0901.2923v1, full preprint inspected), already proved the three-dimensional extremal norm \(5\) and developed local optimization methods. Those results are explicitly attributed. Lien, *Minkowski Sums of Rotating Convex Polyhedra* (SCG 2008, complete two-page paper inspected), addresses rotating-sum construction algorithms. General zonotope determinant formulas are standard. None of these inspected materials provides the claimed **sharp normalized Haar upper-volume probability prefactor** or its exact large-moment consequence. The closest located published findings concern single-body cube projections/sections or cube–crosspolytope volume products and do not imply this two-body Haar tail. Residual priority risk: an unlocated equivalent asymptotic may exist; the full Gover–Krikorian zonotope paper was not inspected.

## Mathematical value — PASS

The upper endpoint of a random orientation-dependent volume is a geometric extreme-event invariant. Its precise \(arepsilon^{3/2}\) coefficient depends on optimizer multiplicity, curvature and Haar density, rather than the already-known maximum alone. It solves a concrete three-dimensional, large-exponent asymptotic motivated explicitly in Banica and coauthors' 2009 treatment, with no arbitrary finite parameter slicing.

## Sources and limitations

Primary inspected full texts: Banica–Collins–Schlenker, arXiv:0901.2923v1; Lien, DOI `10.1145/1377676.1377716`. Gover–Krikorian (2010) was checked at bibliography/abstract level only. The result does not provide the complete volume distribution, a general-polytope law, or a higher-dimensional asymptotic. Historical priority needs independent verification.

Self-review: passed. Independent audit: not yet performed.
