# Independent mathematical audit

## correctness

PASS

Uniqueness and the nontrivial rotational symmetry place the Santaló point at the origin. On a facet half-sector [0,alpha], the radial function is min(sec(theta),r); integrating its square gives the stated primal area. Independently, the support function is r cos(beta-theta) for 0<=theta<=beta (maximizer the side/arc junction), and r for beta<=theta<=alpha (the radial disk point is feasible). The polar radial function is its reciprocal, giving polar area n cos^2(beta)[tan(beta)+alpha-beta], including the endpoint geometries. Multiplying proves the formula and endpoint values. Differentiating the dimensionless product yields sin^2(beta)[(alpha-beta)(tan^2(beta)-1)-tan(beta)]. The bracket is negative for 0<beta<=pi/4; above pi/4 it is at most pi/6-1<0 using alpha<=pi/3. At the disk end the leading loss is n^2 alpha beta^3/3 with error O_n(beta^5), and beta^2=2(r-1)+O((r-1)^2). At the polygon end the chain rule gives derivative -n^2 sin^2(alpha) cos(alpha), with a quadratic remainder by analyticity. With beta=t alpha, expanding sin(beta)cos(beta) and tan(beta) through degree five gives normalized product 1-(t^3/3)alpha^2+(4t^5/15-2t^6/9)alpha^4+O(alpha^6) after dividing by pi^2. The remainders are uniform because |t|<=1. Dividing the deficit by its t=1 value gives the claimed correction and uniform O(n^-4). Independent reciprocal-support quadrature (`python3 /workspace/audit-evidence/replay.py 2`) checked 25 area pairs, with primal and polar absolute errors below 5e-9 and 1.2e-9 respectively; the universal results rest on the analytical proof.

## originality

PASS

The strongest inspected nearby exact results concern outer parallel bodies or intersections of rotated polygons of common inradius. The symmetry extremal inequality controls only the polygon endpoint; the classical upper bound controls only the disk endpoint. None of these states or mechanically implies the familywise clipped-body formula, strict decrease and quantitative deficit laws. This is a bounded best-of-knowledge result, not a priority certification.

## value

PASS

The natural one-parameter path connects two classical rotational extremizers. The result determines the entire volume-product change and strict direction of interpolation, not merely two known bounds. The distinct sharp endpoint orders and the uniform normalized cubic profile with the first correction quantify the distribution of the deficit across the path; that information can be used as an exact benchmark for stability and rounding comparisons. It is not a finite numerical coincidence or a parameter substitution into an inspected result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
