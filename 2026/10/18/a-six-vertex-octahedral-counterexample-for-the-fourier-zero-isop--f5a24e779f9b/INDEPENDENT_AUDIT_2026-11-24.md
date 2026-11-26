# Independent mathematical audit

## correctness

PASS

Quadrant symmetry gives the real diamond-section transform. Differentiating its nested integrals yields Φ''(s)≥4[1−(v²+w²)s²/2], strictly positive for s<1 on the closed frequency cylinder. With g(t)=Φ(1−t), the conditions g(1)=g'(1)=0 turn the axial cosine integral at u≠0 into (au)^−2 times the integral of g''(t)[1−cos(aut)], strictly positive even at v²+w²=2; at u=0 use g>0 on [0,1). At (0,s,s), the coordinates y+z,y−z give a square with Jacobian 1/2 and a marginal proportional to 1−p², giving 4a(sin s−s cos s)/s³. Its sign change gives a nonempty closed zero set and the least norm is attained, so it strictly exceeds √2. The equal-volume ball has radius (a/π)^(1/3), giving the stated comparison. Independently checked the ninth Taylor sum bound by exact scaled integer arithmetic and the rational sufficient threshold (<101); replay /workspace/branches/independent_checks.js. The Taylor terms decrease from the second onward and the first ball root lies in (π,3π/2), so the finite arithmetic checks are sufficient for the integer example but are not the uniform positivity proof. The six displayed vertices are exposed; antipodal spanning pairs prove the minimum in the stated class. The frozen checker was inspected, not executed.

## originality

PASS

The claim that the ball fails to maximize the first real Fourier-zero distance is already known. What survives is the uniform diamond-section cylinder bound and the explicit minimum-vertex polyhedral counterexample. Inspected primary and catalogue disproofs for d≥3 use disks and do not yield a six-vertex octahedron or a sign statement for its diamond sections.

## value

PASS

Six is a genuine sharp complexity bound within centrally symmetric 3-polytopes, and the example attains it with integral vertices. The continuum cylinder estimate and exact finite endpoint check make that sharp complexity statement usable without numerical zero searches; they are not merely an improvement of the already known circular threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
