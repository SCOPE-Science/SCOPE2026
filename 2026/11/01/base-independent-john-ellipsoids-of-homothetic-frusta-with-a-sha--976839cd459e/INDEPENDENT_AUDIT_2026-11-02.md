# Independent mathematical audit

## correctness

PASS

For J(B)=B_m, the candidate axis ellipsoid center t=a, axial semiaxis a, transverse semiaxis b has lateral support equality (1-lambda)a+sqrt((1-lambda)^2 a²+b²)=1. Its height [0,2a] fits below the top cap iff a<=1/2. When lambda<=lambda_c=(n-1)/(n+1), a=[(n+1)(1-lambda)]^-1 and b²=(n-1)/(n+1); above lambda_c, a=1/2,b²=lambda. Any base John frame with sum c_i u_i=0 and sum c_i u_i u_i^T=I_m lifts to lateral contact points (q,sqrt(1-q²)u_i), where q=(1-lambda)a/[1-(1-lambda)a]. Weights c_i/(1-q²), plus alpha=(1-nq)/[2(1-q)] at the upper cap and beta=(1+nq)/[2(1+q)] at lower cap, are nonnegative and have zero first and identity second moments. John sufficiency and uniqueness yield global optimality without symmetric base. Alpha changes 0 to positive precisely at lambda_c. Volume a b^(n-1) is C1 not C2 at transition; affine shear transports to any base. Independently checked 168 exact rational support/contact equations for dimensions 2..29; actual check_frusta.py uses finite rationals but full theorem follows from contact-frame proof.

## originality

PASS

The older Khachiyan half-cone result covers a specific round cone and a central cut, and is explicitly credited. Güler–Gürtuna solve outer/covering truncated second-order cones, while noting the inner truncated-cone problem is unsolved; their inner ellipsoids concern different slab bodies. The fully inspected Santaló-law record concerns polar-volume products, not John ellipsoids. No inspected source entails the all-base all-ratio John formula or contact transition.

## value

PASS

Gives a universal, shape-independent reduction of a natural maximum-volume inscribed ellipsoid optimization for every asymmetric or nonsmooth convex base to one scalar ratio; includes an exact regime switch and nonsmooth second derivative. This is a general structural theorem, not a trivial special-case computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
