# Independent mathematical audit

## correctness

PASS

Let n>=3 and K=B×[-h,h] in R^n with B⊂R^{n-1} centrally symmetric, C-infinity boundary and everywhere positive Gauss curvature; V=vol_{n-1}(B), H(v)=h_B(v) for unit v, and κ(v)>0 its Gauss curvature at the support point. For unit direction u=(cos(theta)v,sin(theta)), a central hyperplane section is parameterized by x↦(x,-cot(theta) <x,v>), x∈B with |<x,v>|<=h tan(theta), giving Jacobian csc(theta) for angle convention; equivalently choosing normal/axial angle complementary gives rho_I=sec(theta) vol_{n-1}{x in B:|<x,v>|<=h cot(theta)}. In the full-strip regime the section area is V sec(theta). In meridional coordinates r=rho cos(theta),z=rho sin(theta), so z=V and r=V tan(theta) traverses an axial top facet until tan(theta)=h/H(v), i.e. its boundary radius r_0=hV/H(v). This radial function over v is exactly hV times the polar base B^circ; central symmetry gives the opposite facet. Beyond tangency the missing strip volume consists of two small smooth curvature caps. The standard local paraboloid cap integral gives a single cap coefficient 2^{n/2} κ_{n-2}/(n sqrt(κ(v))) delta^{n/2} with delta=H-h cot(theta). Since the meridional radial increment satisfies r-r_0~(hV/H²)delta, the two-cap difference is V-z~[2^{n/2+1} κ_{n-2}/(n sqrt(κ(v)))] [H²/(hV)]^{n/2}(r-r_0)^{n/2}, with positive coefficient. Away from rim the section depends smoothly on the slicing plane; at rim, the one-sided t_+^{n/2} gives the sharp C^{ceil(n/2)-1, n/2-ceil(n/2)+1} global regularity, no better. The n=3 circular case and ellipsoidal anisotropy were independently spot-checked; finite quadrature is not an infinite proof.

## originality

PASS

Classical central-section integrals for cylinders and intersection-body equatorial smoothing are prior art, as is local cap asymptotic theory. The selected new claim combines (i) *anisotropic* axial facets equal to scaled polar B^circ, (ii) the explicit curvature-dependent n/2 contact coefficient, and (iii) a sharp dimension-indexed global regularity class. Dirksen’s full primary PDF treats round generalized cylinders and section maxima via Fourier–Bessel integrals rather than polar facet plus arbitrary-base curvature. Alfonseca–Kim’s indexed abstract emphasizes revolution bodies and near-equator asymptotics, a different locus; its full primary PDF remained inaccessible in this run. General Radon-transform singularity literature could imply the power law; absent full comparison is an explicit originality risk, not a fabricated not-covering proof.

## value

PASS

The natural intersection body of a product prism creates exposed axial facets whose geometry is the *polar* of the base, and the adjoining side has a curvature-governed contact singularity. This identifies a structural failure of strict convexity and an exact dimension-dependent smoothness threshold of a canonical integral transform. Unlike a ball-only formula, the coefficient reveals anisotropic local Gauss curvature and the facet shape uses the full polar gauge. An exact self-contained geometric classification has value independently of a broader extremal theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
