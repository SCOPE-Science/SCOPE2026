# Independent mathematical audit

## correctness

PASS

For fixed b>0 the Jacobian polynomial is (lambda+b)(lambda²-a lambda+1), so eigenvalue pair crosses at a=0 with derivative 1/2 and third eigenvalue -b. Independently formed right q=(1,i,0), adjoint p=(1/2,i/2,1/[2(b-i)]), quadratic tensor B(u,v)=(0,0,2u_x v_x); symbolic resolvent substitution gives G21=-4i/[3(b+i)(b+2i)] and Re G21=-4b/[(b²+1)(b²+4)]. Therefore l1=-2b/[(b²+1)(b²+4)]<0. A separate quadratic center manifold z=[(b²+2)x²-2bxy+2y²]/[b(b²+4)]+O(||(x,y)||³) solves the invariance identity exactly. Classical Hopf theory yields unique orbitally stable local cycle for small a>0 with physical radius sqrt([(b²+1)(b²+4)/b]a)+O_b(a). At a=0, radial normal form drho/dt=-c_b rho³+O(rho^4) and local exponential stable foliation give t(x²+y²)->(b²+1)(b²+4)/b except for one-dimensional strong-stable manifold, where decay exponential. Distinguish standard normal-form theorem from finite symbolic check; no global flow claim.

## originality

PASS

Sprott 1994 primary 4-page paper introduces the flow and reports sample chaotic Lyapunov exponents; the 2013/2014 author technical note gives bifurcation regime graphics and exact model equations, but neither displayed an all-positive-b first Lyapunov coefficient or exact t^-1 critical constant in read material. Related Resultary Sprott S/P and case F stationary-moment claims concern other dynamics/invariants. General Hopf theory implies existence conditional on computed l1 but not this case-F rational coefficient. No matching published explicit formula found; unindexed specialized dynamical-system computation remains priority risk.

## value

PASS

An exact formula valid for every positive damping b rules out generalized-Hopf degeneracies along the local boundary; the physical amplitude and sharp critical relaxation with exceptional manifold give quantitative predictions unavailable from a mere numerical phase diagram. This is a motivated structural benchmark for chaotic-flow local bifurcation, not a routine linear type check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
