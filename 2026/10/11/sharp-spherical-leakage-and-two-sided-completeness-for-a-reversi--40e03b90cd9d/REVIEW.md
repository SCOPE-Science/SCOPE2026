# Independent mathematical audit

## correctness

PASS

Independently differentiated V=(x-1)²+y²+(z+1)² along xdot=y+2xy+xz, ydot=1-2x²+yz, zdot=x-x²-y² with sympy, getting Vdot=-2q exactly, q=x²+xy+y²-x. Completing square q=(x-2/3)²+(x-2/3)(y+1/3)+(y+1/3)²-1/3 yields ellipse E with matrix [[1,1/2],[1/2,1]] and area 2pi/(3sqrt3). On a radius-R sphere, the two z-graphs exist over E for R>=2, normal velocity -q/R, area element R/sqrt(R²-rho²), so f_R=1/(2pi R²)int_E R/sqrt(R²-rho²), and J_R=2int_E(-q)/sqrt(R²-rho²). Exact ellipse integral int_E(-q)=pi/(9sqrt3) gives coefficients. Uniform expansion on bounded E establishes the claimed error orders. q>=-1/3 implies Vdot<=2/3 and forward nonexplosion; the reversing involution (x,-y,-z) verified symbolically gives backward nonexplosion and O(sqrt(1+|t|)). Integrating derivatives of V,z against compact invariant measures yields exactly E(xy)=0 and the shifted unit circle mean square 1/4. No global orbit boundedness or attractor existence is claimed.

## originality

PASS

The complete original three-page Sprott 2014 primary article (author-hosted PDF) was inspected page by page. It explicitly notes almost inward radial orientation with small polar holes, and reports numerical simulations of invariant tori/attractors; it does not compute the ellipse, area/flux constants, two-sided global existence bound or invariant-measure moment equalities. The 2015 follow-up concerns reversibility and attractor organization. Algaba–Merino–Qin–Rodríguez-Luis 2019 publisher-accessible title, abstract, introduction, theory and conclusion concern a family embedding, Hopf-zero and KAM bifurcations, not a cited sphere-flux formula; the inaccessible remainder is a residual risk, not proof of noncoverage. Resultary related Sprott records concern different vector fields/parameters and do not mathematically dominate the exact field/radial geometry.

## value

PASS

The original paper identifies but does not quantify spherical leakage, making exact outgoing patch area and normal flux natural numerical-to-analytic invariants. The sharp asymptotic constants resolve the geometric hole size and quantify its vanishing influence; two-sided completeness for a quadratic vector field and compact invariant-measure balance identities are independently meaningful, without inflating them to a global attracting-ball or escape-theorem claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
