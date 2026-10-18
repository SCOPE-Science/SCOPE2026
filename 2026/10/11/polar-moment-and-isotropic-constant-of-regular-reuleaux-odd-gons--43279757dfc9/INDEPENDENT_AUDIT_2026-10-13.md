# Independent mathematical audit

## correctness

PASS

For width one, generating odd n-gon circumradius R=(2cos(π/2n))^{−1}. Each curved piece is a unit circular sector of half-angle t minus its isosceles triangle; exact sector moments are area t, first coordinate 2sin(t)/3, polar moment t/2, and the triangle formulas from barycentric integration. Translate each sector-minus-triangle piece from arc center at (−R,0), adding R² area and −2R first moment, and sum with n identical radial generating-polygon triangles. Algebra reduces to J=[2π(3+tan²t)−n tan t(11+tan²t)]/16; area=(π−n tan t)/2. Dihedral symmetry yields covariance J/(2A)I, L²=J/(2A²). I independently recomputed the n^{−2}, n^{−4} coefficients by SymPy exact series; J=π/32−π³/(192n²)+π⁵/(2560n⁴)+..., L²=1/(4π)+π³/(180n⁴)+..., confirming the cancellation. Restoring w scales J by w⁴ and A by w².

## originality

PASS

The natural all-odd-order Reuleaux moment formula and quartic cancellation are not stated or immediately implied by the inspected Jin–Guo regular-family asymmetry treatment or the 2014 exact *triangle* inertia calculation. That calculation uses the same sector decomposition and says methodology could extend to pentagons, a significant obvious-method risk but no pentagon/heptagon/all-order formula or isotropic asymptotic is given.

## value

PASS

Centroidal polar second moment and affine-isotropic constant are natural mechanical and convex-geometric invariants of the canonical regular constant-width approximants to a circle; the all-odd-order exact formula and unexpected cancellation of the quadratic defect under normalization give more than a table extension or n=3 recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
