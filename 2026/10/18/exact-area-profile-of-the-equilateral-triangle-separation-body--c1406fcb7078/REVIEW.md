# Independent mathematical audit

## correctness

PASS

The perimeter normalization is m(T,z)=[Per(conv(T,z))-6]/pi, not a volume floating body. For side length two the side and opposite-vertex chambers have visible paths of lengths 2 and 4. Focal semiaxes (1+q/2,sqrt((1+q/2)^2-1)) and (2+q/2,sqrt((2+q/2)^2-1)) therefore follow from the same two foci. On extended edge ray AB the perimeter equation t+sqrt(t^2+2t+4)-2=q has unique nonnegative root u=q(q+4)/(2(q+3)); its endpoints force angles phi=asin(sqrt(3)u/(2b_f)), psi=asin(u/(2a_v)). Green boundary integrals give I_f=a_fb_f(pi-2phi)+2/sqrt(3)+u/sqrt(3) and I_v=2a_vb_v psi-u/sqrt(3), whose crossing terms cancel, giving area sqrt(3)+3/2[a_fb_f(pi-2phi)+2a_vb_v psi]. Both nondegenerate arc pieces persist for q>0; q=0 is the triangle. Independent radial convex-hull-perimeter quadrature at q=.05,.5,2 matches the closed form, and independent SymPy expansion in q=s^2 reproduces coefficients sqrt(3)+3*pi*s/2+15*pi*s^3/16-2*sqrt(3)*s^4/9. All-parameter proof rests on exact chamber geometry and Green integration, not finite quadrature; similarity substitution delta->2delta/L and area factor (L/2)^2 is correct.

## originality

PASS

Best-of-knowledge PASS limited to the evaluated six-piece equilateral triangle profile and nontrivial cancellation/coefficients. Schneider already establishes the construction, planar perimeter normalization and polygonal ellipse chambers; square published result gives a separate exact profile and cannot be affinely substituted because isotropic mean width is not affine invariant. Original triangular all-parameter joining and area expression were not found in the targeted published records or examined primary texts. This is not a claim of priority for separation bodies or ellipse arcs.

## value

PASS

A regular triangle is the canonical noncentrally symmetric polygon; an explicit complete separation-body area profile, rather than generic polygon ellipse-local geometry, supplies exact geometric and Poisson-hyperplane comparison benchmarks. The six-piece transition, exact formula valid for every delta, and cancellation of the linear area term constitute a motivated mathematical gap rather than arbitrary parameter substitution. No expectation for a random circumscribed cell is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
