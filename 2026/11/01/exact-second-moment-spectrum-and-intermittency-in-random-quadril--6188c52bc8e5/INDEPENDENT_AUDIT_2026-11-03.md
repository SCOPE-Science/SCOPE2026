# Independent mathematical audit

## correctness

PASS

For any strictly convex counterclockwise quadrilateral Q, its signed adjacent-three-vertex triangle areas c_i obey c0+c2=c1+c3=A. D=(c0-c2)^2+(c1-c3)^2≥0 vanishes iff opposite sides match a parallelogram. Via orientation-preserving affine coordinates v0=(0,0),v1=(1,0),v2=(s,h),v3=(0,1), with s,h>0 and s+h>1, A=(s+h)/2 and D=[(2−s−h)^2+(h−s)^2]/4. Rebuilding all four new vertices v′_i=v_i+u_i(v_{i+1}−v_i), with independent uniform u_i, the shoelace polynomial and corner determinants integrate exactly to E[A′|Q]=A/2, E[(A′)^2|Q]=(37/144)A²+(7/288)D, E[D′|Q]=(7/72)A²+(1/16)D. I independently reconstructed the symbolic 4-variable integrations from the geometry and verified all three identities exactly using SymPy, as well as the 2x2 characteristic polynomial with eigenvalues λ±=(23±7√5)/144. Matrix spectral decomposition gives coefficients C±=1/2±1/√5±δ/(4√5), δ=D0/A0², and the strictly positive fixed-area variance gap δ(λ+^t−λ-^t)/(4√5) for t>=1; equality precisely parallelograms. W_t=2^tA_t/A0 is a mean-one nonnegative martingale; E[W_t²] grows as ((23+7√5)/36)^t. Since Y=2A′/A∈(0,2), E[Y|Q]=1 and Var(Y|Q)=1/36+7D/(72A²)≥1/36, the elementary concavity bound E sqrt Y≤1−1/[72(1+sqrt2)^2] gives geometric decay of E sqrt W_t, implying W_t→0 a.s. by Markov and Borel–Cantelli. This proof does not infer almost-sure collapse merely from unbounded second moment.

## originality

PASS

Qualified PASS for the explicit quadrilateral conditional second-moment operator and resulting variance/intermittency classification, NOT for the random subdivision mechanism, deterministic Varignon mean-half-area analogy or generic Lyapunov flattening. Nguyen–Volkov explicitly study the same random edgewise subdivision in full generality, but the reviewed primary material focuses on projective flattening and Lyapunov rates, not the exact two-statistic area operator. Wider specialist moment literature may contain equivalent formula.

## value

PASS

The random independent-side subdivision process is established prior work. The new exact two-statistic quadratic moment closure, complete spectral formula, sharp parallelogram minimum variance and coexistence of martingale mean preservation with typical collapse and divergent second moment are natural, motivated quantitative facts for its four-sided case, beyond a routine deterministic midpoint identity or finite numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
