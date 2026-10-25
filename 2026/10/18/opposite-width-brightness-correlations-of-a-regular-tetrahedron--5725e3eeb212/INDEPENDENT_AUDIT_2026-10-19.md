# Independent mathematical audit

## correctness

PASS

For ordered absolute view coordinates x>=y>=z>=0, support functions give W_O=2x and W_T=2(x+y), while Cauchy projection-area summation over the 8 octahedral and 4 tetrahedral facet normals gives B_O=max(2x,x+y+z), B_T=2B_O. Decompose each of the 48 spherical order chambers at x=y+z into two spherical triangles, and apply integration by parts using Laplace–Beltrami identities Delta(u_i)=-2u_i and Delta(u_i u_j)=2 delta_ij-6u_i u_j; the explicit boundary side formulas reconstruct the exact mixed moments. Their exact radical/arctangent combinations yield cov_O=2/3+(4sqrt(2)+8omega-6sqrt(6)theta)/pi>0 and cov_T=8/3+8sqrt(6)/pi-12sqrt(6)(pi/2-theta)/pi<0. Inspected exact rational arctan-bracketing certificate and spherical_integrals_check.py; independent high-resolution Gaussian/spherical quadrature gave approximately 0.0206678447 and -0.0340466734, corroborating the algebra and strict margins rather than replacing certified signs.

## originality

PASS

Joint same-direction width–brightness sign divergence despite identical normalized brightness is distinct from separate width or brightness laws and from mixed two-dimensional shadow area–perimeter moments. Direct primary comparison includes relevant full Abas preprint sections and Resultary studies of orthotopes and tetrahedral projection moments; no dominating result yielding the opposite signs for this aligned pair was identified.

## value

PASS

A concrete exact counterexample shows brightness information, even pointwise up to scale, fails to determine the sign of an intrinsically geometric mixed width–brightness covariance. This is a substantive reconstruction/identifiability boundary in stochastic convex geometry, not a gratuitous numerical polytope moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
