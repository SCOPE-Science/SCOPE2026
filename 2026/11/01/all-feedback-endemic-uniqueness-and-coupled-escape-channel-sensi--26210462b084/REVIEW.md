# Independent mathematical audit

## correctness

PASS

Reconstructed the autonomous four-compartment ODE with g=SI, σ=1 and strictly positive rates. I>0 forces S+C=k=(µ+α)/β<1; I=0 only disease-free. For k<1, set a=1−k,z=SI,U=µa,V=µ+γ,g=γε2 and solve the susceptible equation C=(βz−U)/(V+gz), S=k−C, I=z/S, R=a−I. On the positive feasible interval z∈(U/β,z_max), R decreases from >0 to 0. The C-stationarity scalar equation is G_g(z)=δ(1/z+ε1) with G_g=(β−U/z)(1+βz/[S(V+gz)])/R; every factor is positive and strictly increasing, giving exactly one root. At fixed z increasing g decreases C, increases S,R and lowers G_g, shifting z* upward; ε1 raises RHS, also shifting z* up. Stationary R gives I*=aM/(α+M), M=µ+δ(1+ε1 z*), yielding strict eps1 increase and strict eps2 increase iff ε1>0; ε1=0 makes I* independent of ε2. As g→∞, C→0 and limiting equation gives the stated unique positive polynomial root <ka. Independent SymPy verified S stationary and exact factorization. Finite 80-case source diagnostics cannot substitute for the quantified monotonic proof.

## originality

PASS

Best-of-knowledge originality passes for the exact g=SI σ=1 all-feedback unique endemic equilibrium and strict-vs-flat two-channel sensitivity; not for model invention, general endemic existence or previously published g=I uniqueness.

## value

PASS

The endpoint σ=1 is a natural maximal-reinfection boundary of a recently proposed SIRCm model. The theorem closes a specific intermediate-feedback equilibrium-uniqueness gap for arbitrary independent feedbacks and exposes a mathematically meaningful interaction switch: the second channel changes endemic burden only when first-channel feedback is active. The exact saturation limit supplies a reusable parametric boundary, distinct from model stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
