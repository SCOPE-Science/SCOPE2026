# Independent mathematical audit

## correctness

PASS

For regular tetrahedron with vertices (1,1,1),(1,−1,−1),(−1,1,−1),(−1,−1,1), edge 2√2, Cauchy brightness yields A(u)=max{2∑|u_i|,4 max|u_i|}. The projected silhouette is triangular iff 2max|u_i|<∑|u_i|, quadrilateral otherwise (null boundary ignored). These cases partition eight octants into a central spherical triangle and 24 axis cones. In polar coordinates about body diagonal e, the allowed azimuth for triangle cases is 2π before the inradius then 2π−6acos(cotρ/(2√2)); area A=2√3 cosρ with |dA/dρ|=2√3 sinρ. Axis-cone azimuth for quad is π/2 then π/2−2acos(cotθ/√2), with A=4cosθ. Sphere factors 8/(4π) and 24/(4π) yield exact f3 and f4 with common b*=4√(2/3), triangular endpoint b3=2√3 and quad endpoint 4. On b*<t<b3 their constants are 2/√3 and 3/4, hence posterior 8/(8+3√3). Independent numerical quadrature reproduces P(N=3)=2(π/2−3asin(1/3))/π≈0.35095931218 and first weighted moments 2/√3 and 4/√3; analytic change of variables, not sampling, proves the continuous densities.

## originality

PASS

The full 2001 Vickers–Brown paper supplies the unconditional area density including its plateaus and cone analysis, not the two type-resolved measures. A published all-tetrahedra result gives the first two silhouette-conditional area moments, but finitely many moments do not determine an entire density or posterior plateau. This claim restricts to a natural regular tetrahedron and gives an exact joint law; full older stereology might implicitly contain equivalent equations.

## value

PASS

The natural joint metric/combinatorial law for a random regular tetrahedron shadow is fully solved, supplying elementary f3,f4 on all area thresholds and a nontrivial constant area-only Bayesian silhouette probability over a positive-length interval; this is genuinely additional information beyond the known marginal or finitely many conditional moments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
