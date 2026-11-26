# Independent mathematical audit

## correctness

PASS

Walsh level k has adjacency eigenvalue d-2k; spectral projection gives the invariant span and the restriction matrix with entries (-1)^|S intersect T| for |T|=2 and |S|=k. On constant, vertex-additive zero-sum, and zero-row-sum pair arrays, the transpose maps are respectively ((d-2k)^2-d)/2, -2(d-2k) times a k-set sum of vertex coefficients, and four times a k-set sum of pair coefficients. The images are orthogonal: subset counts give zero mean on the last two sectors, and their mutual cross term counts whether a given vertex is or is not in a pair, reducing to zero pair row sums. Swapping one vertex between k-sets proves injectivity in the first-order sector except at k=0,d or d/2. In the pair sector, comparing T+i and T+j for all (k-1)-sets excluding i,j makes each row difference u_ia-u_ja constant in a, then zero; this uses 2<=k<=d-2. The pair image vanishes outside this range by the row-sum conditions. Thus the levelwise rank and its stated sum follow, including d=4 (rank 11). For imaginary spectrum, Hilbert–Schmidt dissipation forces each monitored-projector commutator to vanish. At nonzero frequency the diagonal at a monitor forces its scalar to zero, and the commutator equation propagates this vanishing on both sides along H^j of each monitor. At zero frequency H^2 has nonzero matrix elements between adjacent two-sets in the connected Johnson graph, forcing the monitor scalars to agree and hence the bright block to be scalar. Fixed positive rates give contraction, excluding imaginary-axis Jordan growth; all other modes decay. H and the projectors reduce to the bright and dark blocks, so conservation of bright trace sets the coefficient. At the zero corner the only candidate dark components are constant Walsh sums; precisely the two square-dimension zeros survive, each of squared norm a_d, giving the coherent amplitude 2a_d cos(s t) and a bright contribution (1-2a_d)^2/b_d. The parity of s and s^2 always agrees, and Stirling at deviation sqrt(d)/2 gives the stated peak scale 8/(pi e d); b_d is asymptotic to d^3/2. Analytic replay: frozen RESULT.md proof parts 1–4. Its sibling verify.py was inspected, not rerun; the frozen report describes bounded rank and radial checks and two finite-time dynamics checks, not a proof for all d. The error is at fixed dimension and rates; nonsquare dimensions can have dark states invisible to the initial corner.

## originality

PASS

Pass for the model-specific bright-space rank and asymptotic law together with the exact if-and-only-if square-dimension corner return. This does not claim priority for Walsh-slice harmonics, the general peripheral structure of finite-dimensional Lindblad semigroups, or arithmetic dark states under different dynamics. The strongest inspected Walsh antecedent treats a different band and a positive-eigenvalue collision, not the constant-sector zero or the Lindblad observable.

## value

PASS

A natural local noise configuration and a basic return observable exhibit an exact arithmetic split that cannot be inferred from global dark-state dimension. The theorem identifies the two accessible frequencies and separates a persistent peak of order d^-1 from a stationary return of order d^-3, with a full asymptotic law for arbitrary initial states and positive site-dependent rates. This model-specific effect and its observable size are substantive, independently of novelty of the standard spectral tools.

The dated certificate retains the supplied scientific assessment, sources and limitations.
