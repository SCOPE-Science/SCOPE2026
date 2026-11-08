# Independent mathematical audit

## correctness

PASS

Over F16 with θ^4+θ+1, the two parameter vectors (1,8,2,7) and (3,11,1,15) are in the general-position Weddle determinant setting of Dolgachev. The six marked A1 nodes each replace one F16-point by an exceptional P1 with 17 points (net +16). At the seventh rational D4 point, the tangent cone is a square and its restricted cubic has one vs three rational simple projective roots; each rational outer exceptional curve adds +16 beyond the central line net +16, giving D4 net corrections +32 and +64. Independent finite-field arithmetic enumerated all 4369 normalized projective points, resulting singular-quartic counts 417 and 449, and verified one vs three rational roots of binary cubics (2,4,3,9) and (0,4,2,0). Thus resolved K3 totals 545 and 609, the latter exactly 16^2+22*16+1, the Weil upper bound for smooth K3. Source verify_weddle16.py was read and its separate determinant expansion, tangent-cone extraction, 15 general-position tests were checked at algorithm level; local exceptional configuration depends on standard D4 resolution theorem plus the explicit blow-up argument, not just output logs.

## originality

PASS

Qualified best-of-knowledge PASS: Dolgachev 2024 Section 2 explicitly establishes the determinant construction, six ordinary nodes and a characteristic-two seventh D4 singularity with K3 resolution. Those geometric facts are not novel here. The two precise F16 vectors, their arithmetic D4 arm splitting and 545/609 point counts were not established by the inspected sections. Bolognesi studies Weddle moduli. Arithmetic K3 tabulations or uninspected Weddle papers may have the identical models.

## value

PASS

A geometrically canonical K3 construction with identical rational singularity pattern exhibits distinct Frobenius actions on D4 outer components. It provides exact opposite splitting witnesses and achieves the sharp K3 Weil bound q^2+22q+1 over F16, a motivated arithmetic-geometric distinction rather than an arbitrary isolated finite-field count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
