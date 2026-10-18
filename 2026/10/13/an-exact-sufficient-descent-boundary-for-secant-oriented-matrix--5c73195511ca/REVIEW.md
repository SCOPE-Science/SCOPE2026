# Independent mathematical audit

## correctness

PASS

From P=I-sy^T/(s^Ty)+(tI+nu yy^T)ss^T/(s^Ty) and t+nu||y||^2=1 (0<=t<=1), the symmetric 2D block is [[z(1+tq^2), q(z(1-t)-1)/2],[same,1]], q^2=m^-2-1, z=(s^Ty)/||y||^2. Sylvester's criterion gives iff Delta=z(1+tq^2)-q^2(z(1-t)-1)^2/4>0 for universal strict descent. For fixed noncollinear m any angle-only t<1 violates positivity at large z; t=1 violates it at small z. Recomputed exact SPD quadratic A=[[1,sqrt3],[sqrt3,4]]/80, b=(-5/8,0), first step alpha=64, s=(40,0), y=(1/2,sqrt3/2), m=1/2,z=20: strong Wolfe with c1=0.0001,c2=0.9; both source rho=eta=1 give t=nu=1/2, P=[[50,-sqrt3],[10sqrt3,1]], sym determinant -43/4, g1^T(-Pg1)=5/32>0. Local witness shows ascent for a permitted step, not forced convergence failure.

## originality

PASS

The 2026 Matrix Dai--Liao source provides the matrix and general descent conditions, but the inspected secant-setting discussion does not formulate the derived exact (m,z,t) iff boundary, universal obstruction to angle-only choices, or this admissible strong-Wolfe witness. Qualitative descent warnings about unrelated three-term CG algorithms are credited; Resultary's nearest returned topics are different descent variants. Best of knowledge, with inaccessible 2017 full text recorded.

## value

PASS

The exact if-and-only-if boundary locates a concrete safety defect in published secant-oriented optimization settings. The source-specific 2D strong-Wolfe example is a substantive boundary witness for algorithm design, not a generic caution that a matrix might be indefinite.

The dated certificate retains the supplied scientific assessment, sources and limitations.
