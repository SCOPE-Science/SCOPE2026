# Independent mathematical audit

## correctness

PASS

A matching observation pattern diagonalizes after row/column permutations, so every iterate stays in the orthogonal rank-one span and soft-thresholding acts coordinatewise. Before activation, \(y_j^{k-1}=(k-1)\delta s_j\), giving \(\kappa_j=\lfloor\tau/(\delta s_j)\rfloor+2\). After activation the amplitude obeys \(x_{j}^{k+1}-s_j=(1-\delta)(x_j^k-s_j)\); the activation bound and \(|1-\delta|<1\) prove persistence and exact rank monotonicity. At \(\delta=1\), one affine update settles each direction and yields the ceiling formula. Independent scalar replays across steps below, at and above 1 confirmed activation and persistence.

## originality

PASS

The defining SVT paper explicitly says rank monotonicity is empirical and proves general convergence; its implementation discussion concerns the initial all-zero phase. The matching-pattern theorem proves rank monotonicity exactly and resolves every direction's activation and settling time. Linearized-Bregman work supplies related shrinkage/convergence machinery but not this matrix-completion matching decomposition. Targeted searches found no prior exact staircase or finite-termination resonance.

## value

PASS

The original SVT paper highlights empirical rank monotonicity as a practically important feature. The matching observation class is a clean, natural setting where that phenomenon can be proved exactly, with explicit activation times and a sharp finite-termination resonance at \(\delta=1\). This is a motivated solvable benchmark, not an arbitrary special case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
