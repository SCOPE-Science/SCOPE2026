# Independent mathematical audit

## correctness

PASS

For a strictly convex planar quadrilateral Q, maximizing the absolute affine determinant separately in each triangle vertex reduces T(Q) to four vertex triangles. The affine diagonal-intersection normal form A=(a,0),B=(0,b),C=(a−1,0),D=(0,b−1), 0<a≤b≤1/2, gives S=1/2 and largest vertex-triangle area T=(1−a)/2. All 16 vertex differences are contained in the octagon spanned by (−1,0),(a−1,−b),(0,−1),(1−a,b−1),(1,0),(1−a,b),(0,1),(a−1,1−b); unused differences are in the coordinate diamond. Consecutive turning determinants b−a, 1−a, 1−a−b, a (repeated) are nonnegative. Independent symbolic shoelace evaluation gives area(Q−Q)=3−2a. Area(Q−Q)=2S+2V2(Q,−Q) gives V2=1−a=2T, hence full reflection polynomial and deficit 2(S−T); affine scaling restores arbitrary Q. Independently checked exact Fraction monotone-chain difference hulls for 296 rational (a,b) pairs and Sympy exact determinants; those finite tests corroborate rather than replace the universal proof. Degenerate triangular limit by continuity only.

## originality

PASS

Best-of-knowledge comparison of exact statements, applicable conditions, reductions and primary literature; documented specific residual source risks rather than treating negative searches as novelty proof.

## value

PASS

Convex quadrilaterals are the minimal nonsimplex polytopes where Godbersen equality fails. Identifying the EXACT affine-invariant deficiency by the intrinsic best inscribed triangle is a motivated sharp quantitative stability refinement: it determines the complete area(Q+t(−Q)) polynomial and exact degeneration/parallelogram endpoints rather than merely strictness. The exact ratio is not a fixed trivial parameter substitution from the known general inequality, and would be a useful model for higher-vertex quantitative stability. No general convex-body statement is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
