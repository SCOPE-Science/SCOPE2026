# Independent mathematical audit

## correctness

PASS

Read pinned RESULT.md and checker.py. For n=m+1 regular-simplex vertices, same-edge, adjacent-edge and disjoint-edge absolute inner products are a=2/(m+1), b=(m-3)/(m^2-1), c=4/(m^2-1); the chosen scaling gives sum vv^*=I. Unsigned vertex-edge incidence Q obeys Q^TQ=2I+A and QQ^T=(n-2)I+J, deriving triangular graph adjacency eigenvalues 2(n-2), n-4, -2 with multiplicities 1,m,N-m-1. G=(a-c)I+(b-c)A+cJ therefore has Lambda=4(m-2)/(m+1), Theta=(m-3)(m-5)/(m^2-1), Nu=8/(m^2-1). The transverse maximum switches at m=7, producing gamma=4m(m-3)/(m^2-1) for m<=7, gamma=(3m-7)/(m-1) for m>=8, and all transverse eigenvalues coincide m=7. Orthogonal splitting t=hu+z proves the deficit on the entire nonnegative unit sphere; a small strictly positive eigenvector perturbation realizes equality, and positivity of gap gives unique uniform maximizer. Independent numerical real-symmetric eigensolver recreated spectra for m=4..12, not substituted for universal proof. m=3 excluded because no positive rigidity gap.

## originality

PASS

Best-of-knowledge PASS for the novel sharp fixed-frame nonuniform weight stability and spectral crossover, *not* for the known unperturbed projection value or triangular graph eigenvalues. Primary Deregowska–Lewandowska regular-simplex midpoint construction identifies the equal-weight optimal relative projection quantity; the present spectral deficit and its exact crossover are additional. Kumar et al.'s ambient-dimension stabilization and graph-spectral projection bounds have different quantified objects. Published-record semantic results on simplex edge configurations address different objectives. No equivalent earlier theorem located; an older implicit triangular-graph Rayleigh bound or frame-stability paper remains a priority risk.

## value

PASS

A natural fixed optimal-frame objective needs quantitative robustness to nonuniform edge weights, not just its maximizer. The exact best global deficit and sharp transition of destabilizing eigenspace at m=7 are independent structural invariants in all dimensions m>=4 and could be used for perturbative projection-constant work. The conclusion does not assert global frame optimality across all frames.

The dated certificate retains the supplied scientific assessment, sources and limitations.
