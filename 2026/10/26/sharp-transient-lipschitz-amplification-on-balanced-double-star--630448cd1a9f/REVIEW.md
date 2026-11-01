# Independent mathematical audit

## correctness

PASS

Let B be oriented edge incidence of balanced double star, L=B^TB, M=BB^T. Since the graph is a tree, B maps vertex functions modulo constants onto all edge gradients, so the Lip operator norm of exp(-tL) is the maximum absolute row sum of E(t)=exp(-tM). Decomposing edge symmetry reduces central row to the positive two-dimensional semigroup exp(-t S_d), where eigenvalues are lambda±=(d+3±sqrt(d²+6d+1))/2 and central row sum X(t)=A exp(-lambda- t)-(A-1)exp(-lambda+ t). The delicate inequality excluding leaf rows follows because the Laplace transform of q(t)+d k(t)-exp(-t) is d²/[(z+1)(z+d+1)(z+lambda-)(z+lambda+)], a convolution of positive exponentials; central row strictly dominates for t>0. The same four-level unit-Lipschitz test function attains all times. Differentiating X gives unique positive peak for d>=2 and none for d=1, with 3-8/d+O(log d/d²) and t~(2log d-log3)/d. Independent fresh direct matrix exponentials checked 64 positive time/degree pairs and central-row strict dominance; all-d/all-t theorem relies on the analytic positive-kernel argument.

## originality

PASS

Fan–Godsil analyze precisely double-star graphs but with unitary adjacency quantum walks exp(it A), not diffusive positive combinatorial-Laplacian heat exp(-tL). Münch–Wojciechowski give a curvature versus heat-flow Lipschitz estimate on general graphs, not this all-time sharp norm or peak and attaining edge. General graph Laplacian heat methods are prior art, and the new claim is a model-specific all-t quantitative transport norm and asymptotic.

## value

PASS

The balanced double-star is a natural finite tree showing transient amplification in Lipschitz/Wasserstein distance despite positivity and sup-norm contraction. The all-time sharp norm, a single attaining potential, and asymptotic peak approaching three identify precise transport instability; these facts are not implied by generic contractivity or a two-vertex toy case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
