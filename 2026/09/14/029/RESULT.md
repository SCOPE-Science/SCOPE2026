# Fixed-scale tortuosity excess in the 3x3 box: disproof with exact ledger

## Context
Critical Bernoulli bond percolation on Z^2 at p=1/2 is conjectured to exhibit tortuosity: the shortest open crossing of a box is typically strictly longer than the Euclidean width. Asymptotic work (Kesten-Zhang; Damron-Hanson-Sosoe) studies large boxes. The admitted target asks a fixed-scale instance: for the box B=[0,3]x[0,3], is the conditional mean shortest left-right crossing length at least 3.6?

## Definitions
Vertices V={(x,y): x,y in {0,1,2,3\}}, |V|=16. Edges E = all nearest-neighbour pairs with both endpoints in B: 12 horizontal + 12 vertical, |E|=24. Each configuration omega in {0,1}^E has probability 2^{-24} at p=1/2. Cross = event that some fully open path joins the left side {x=0\} to the right side {x=3\}. On Cross, S(omega) = minimum number of edges of any open left-right path; off Cross, S is undefined. The claim under test is E_{1/2}[S | Cross] >= 3.6 = 18/5.

## Result
The claim is FALSE. Exhaustive enumeration of all 2^24 = 16777216 configurations gives N_cross = 10575744, sum_S = 36373760, and length distribution N[S=3]=6942720, N[S=4]=2790784, N[S=5]=697472, N[S=6]=123264, N[S=7]=16896, N[S=8]=4224, N[S=9]=384. Hence E_{1/2}[S | Cross] = 36373760/10575744 = 284170/82623 ≈ 3.4393570797 < 3.6. The verdict inequality is exact integer arithmetic: 5*sum_S = 181868800 < 190363392 = 18*N_cross, gap 8494592.

## Proof / Evidence
Per configuration, multi-source breadth-first search from the four left-side vertices over open edges yields exact graph distances; the minimum over the four right-side vertices is the shortest open crossing length. BFS distances are true shortest-path distances on unweighted graphs. Two independently written implementations agree bit-for-bit: C/OpenMP bitmask BFS (enumerate.c producing ledger.txt) and separately written Python graph BFS with coprime-stride enumeration order visiting every mask exactly once (verify_independent.py producing verify_ledger.txt). The audit re-executed the C binary and reproduced ledger.txt exactly, and a third edge-set encoding agreed on 3000 random masks. Analytic spot check: S=3 requires a fully open straight row; inclusion-exclusion over the 4 disjoint triples gives 4*2^21-6*2^18+4*2^15-2^12 = 6942720, matching both programs. Histogram sums to N_cross; gcd(sum,N)=128 confirms the reduced fraction. No sampling or asymptotics is involved.

## Limitations
The disproof is specific to the fixed 3x3 box (4x4 vertices) at p=1/2 with the stated crossing and shortest-path definitions. It makes no claim about larger boxes, other p, site percolation, or asymptotic tortuosity exponents. Correctness rests on the BFS implementations, cross-validated as above.

## Reproducibility
Build and run: cc -O2 -fopenmp enumerate.c -o enumerate && ./enumerate. Expected output: n_cross=10575744, sum_S=36373760, histogram as above, VERDICT=MEAN_LT_3.6_DISPROVED. Independent check: python3 verify_independent.py. Source files are preserved in output/artifacts/.

## References
H. Kesten, Y. Zhang, The tortuosity of occupied crossings of a box in critical percolation, J. Stat. Phys. 1993. M. Damron, J. Hanson, P. Sosoe, On the chemical distance in critical percolation, Electron. J. Probab. 22 (2017), arXiv:1506.03461. R. M. Ziff, Exact critical exponent for the shortest-path scaling function in percolation, J. Phys. A 32 (1999).
