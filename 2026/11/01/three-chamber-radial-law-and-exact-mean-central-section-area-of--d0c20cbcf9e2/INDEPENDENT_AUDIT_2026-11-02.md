# Independent mathematical audit

## correctness

PASS

The exact halfspace definition gives rho(u)=2/(a+b) for ordered |u| coordinates. The twelve facet-normal spherical Voronoi cells, with angular boundary h(phi)=cos(phi)+sqrt2 sin(phi), partition the geodesic angle into three regimes at radii 2sqrt(2/3) and sqrt3; the Jacobian d alpha/dr gives precisely the three density formulas with coefficient 12sqrt2/(pi r^2). Differentiation yields jump 8sqrt3/pi at sqrt3, and local squares around six coordinate-axis directions yield tail 3 eps^2/(2pi)+O(eps^3). The polar area identity E area(K∩H)=pi E rho^2, followed by 48 gnomonic chambers and two elementary exact integrals, gives 8sqrt3 log(1+sqrt3)-2pi. Independently integrated all three density pieces at 55-digit precision (masses 0.803847577293368,0.136273417736563,0.0598790049700692, sum1); density second moment, gnomonic integral and closed expression agree to >50 digits, and tail ratios converge to 3/(2pi). These checks corroborate the analytic proof.

## originality

PASS

The most plausible 2026 prior, Abas, includes an exact law for the **width of the rhombic dodecahedron**, whereas the audited R is a **radial gauge of the dodecahedron** (a reciprocal support/width of its polar cuboctahedron, up to normalization). These are not the same random variable; its abstract does not explicitly give this polar law or the mean central Euclidean section area. General slice-moment algorithms of Brandenburg et al. are not the explicit Haar-integrated evaluated formula. Full Abas text was inaccessible via lawful arXiv/OA attempts and authorized Oxford (VPN disconnected); therefore best-of-knowledge PASS is conditional on material access risk and is not a whole-paper noncoverage claim.

## value

PASS

The regular rhombic dodecahedron is a canonical Voronoi parallelohedron, and its random radial gauge/central Euclidean section is a natural stochastic-geometric invariant. Three exact phase transitions, a nontrivial derivative jump, sharp endpoint tail, and the closed Haar sectional mean provide precise object-specific information not furnished by the generic definitions or basic volume relations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
