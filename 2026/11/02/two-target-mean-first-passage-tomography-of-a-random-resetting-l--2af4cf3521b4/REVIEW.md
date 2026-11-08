# Independent mathematical audit

## correctness

PASS

Read frozen RESULT.md and assumptions: generator D∂xx, independent Poisson rate r=Ds², fresh i.i.d μ after every reset, calibrated D,x0. Standard renewal from Brownian hitting transform gives M_c=[1-e^{-s|x0-c|}]/[Ds²Φ_c(s)], Φ_c(s)=∫e^{-s|y-c|}μ(dy)>0 for all probabilities even without moments. On each target, positive-rate accumulation inside (0,infty) determines entire Laplace transform by holomorphic identity and folded-distance law by Laplace uniqueness. If two μ,ν have same transforms at a≠b, finite signed difference η is antisymmetric under both R_a and R_b, hence invariant under nonzero translation 2(b-a), impossible for a nonzero finite signed measure. Explicit Fourier reconstruction from cosine folds has 2x2 determinant sin(k(b-a)); discrete resonant k filled by continuity. One target only knows folded law. m finite scalar readings have m+2-point null vector including normalization with both signs. Sources 1±epsilon sin(2πny) on [0,1] at targets 0,1 have TV gap 2epsilon/pi while responses converge O(1/n) uniformly on compact positive-rate intervals (base transform stays positive). Independently checked exact finite-measurement null vector, sine transform and TV instability; unrestricted identifiability uses measure symmetry argument, not numerical inversion.

## originality

PASS

Best-knowledge: distinct precise final statement not implied by inspected prior work; exact comparisons and known subclaims separated. Inaccessibility of some sources alone not a scientific failure; residual risks stated. A known forward transform does not by itself state the reflected-signed-measure uniqueness and data insufficiency/stability boundaries; no equivalence verified in primary results. General renewal and Laplace theory supply tools, not an identified dominating theorem explicitly ensuring arbitrary all-measure two-center identification and sharp finite-data limits.

## value

PASS

A sharp tomography theorem for the natural inverse resetting problem: the precise two-target threshold for arbitrary singular reset laws, with explicit insufficiency of one view, finitely many rate readings and strong TV stability. This is useful for experimental design and establishes exactly what ideal MFPT data determine.

The dated certificate retains the supplied scientific assessment, sources and limitations.
