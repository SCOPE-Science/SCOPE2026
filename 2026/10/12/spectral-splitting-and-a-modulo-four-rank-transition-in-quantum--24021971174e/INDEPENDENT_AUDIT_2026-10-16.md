# Independent mathematical audit

## correctness

PASS

For each real symmetric base adjacency A, the corona H=[A,I;I,0] has orthogonal fiber eigenprojectors Q_lambda,+ and Q_lambda,- attached to each distinct base spectral projector E_lambda, with no overlap across branches. Direct 2x2 Schur squares satisfy Q+◦Q++Q-◦Q-=P+ +(lambda²/(lambda²+4))P-. Therefore average Cesàro mixing splits into R⊗P+ +S⊗P- with R=Σ E◦E and S=Σ lambda²/(lambda²+4)(E◦E). Cycle Fourier projectors F_j obey F_j◦F_k=F_{j+k}/n. For odd n, both R,S have rank n. For even n, R has rank n/2, S has n/2 except when 4|n, where the unique zero eigenvalue of C_n kills one even Fourier mode so rank S=n/2-1. Independent full projector diagonalizations for n=3..16 confirmed rank 2n/n/n-1 and block identity, max absolute difference below 8e-11. Analytic Fourier proof, not finite numerics, covers all n>=3.

## originality

PASS

Godsil supplies exact cycle average mixing R_n; Ackelsberg et al. provide general corona spectral eigenprojectors for state transfer, while average-mixing literature supplies Schur-square projector sum. The assessed weighted sector S_n, full sunlet Fourier-indexed spectrum, and sharp modulo-four zero-mode defect require nontrivial additional synthesis and were not located as a stated dominating theorem. Existing general projectors alone are not the precise answer without this additional calculation.

## value

PASS

The natural family of graphs with one leaf per cycle vertex exhibits a complete average-mixing spectrum and an arithmetic rank phase transition at n divisible by four. Its extra isolated null direction is structurally explained by a zero adjacency mode, making the result useful for quantum-walk average observables beyond finite numerical tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
