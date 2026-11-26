# Independent mathematical audit

## correctness

PASS

Positive diagonal scaling and a sign change give r∈(0,1), q=1−β and s=βr for both directions. Current/current has eigenvalues q±s. One-stale on (u_k,v_k,v_{k−1}) has characteristic z(z−q)^2−s²: when q∈[0,1), |z|≥1 would imply |z||z−q|²≥β²>s². When β>1, put d=β−1. The polynomial z(z+d)^2−s² is negative for z≤0 and strictly increasing for z>0, with its positive root p<1 by evaluation at 1. The other roots are a conjugate pair of modulus p+d, by Vieta and p(p+d)^2=s². For 1<β<2, p+d<1 iff the polynomial is positive at 2−β, i.e. 2−β−β²r²>0, giving 4/(1+√(1+8r²)); β≥2 cannot be stable. The pair has unit modulus on the boundary. In stale/stale, the sum and difference quadratics are z²−qz±s. For β<2/(1+r), |s|<1 and both quadratics are positive at ±1, which are the real quadratic Schur conditions. At or above that β, the difference polynomial at −1 is nonpositive, so it has a root at or below −1. Arbitrary real initial histories permit real nondecaying modes whenever a spectral radius is at least one. Swapping the stale direction permutes variables. Strict gain follows from √(1+8r²)<1+2r; the square identity 81(1+8r²)−(7+16r)^2=8(7r−2)^2 gives the 9/8 bound and the sole equality at r=2/7. The ceilings there bracket β=5/3: 14/9<5/3<7/4. Setting q=0 in the three spectra yields the stated spectral factors at β=1. No finite grid is used to establish a universal statement.

## originality

PASS

The synchronized ceiling, the use of delay-state matrices and qualitative asynchronous advantage are prior art. The best supported distinct claim is the exact one-edge simultaneous-round ceiling compared with both zero and two stale directions, together with the maximal 9/8 gain. The inspected prior theorems do not yield that contrast or maximization.

## value

PASS

For the smallest coupled SPD system, the number and placement of stale edges matter even when the maximum delay and fresh self-read assumptions agree. The theorem separates a true one-edge enlargement from no enlargement with two stale edges, proves its exact best size, and includes an explicit separating β. The β=1 factors prevent a stability-window gain from being misread as equal-parameter speedup. This is a motivated, exact comparison not supplied by an arbitrary-delay sufficient bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
