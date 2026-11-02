# Independent mathematical audit

## correctness

PASS

PASS: On K_{m,n}, m,n>=1, fixed eta>0, spin-reversal symmetry forces stationary mean zero and independent flip noise makes the continuous-time chain irreducible. Writing x,y,z for exchangeable pair correlations, the generator gives 0=-4eta*x+2lambda_A(z-x), 0=-4eta*y+2lambda_B(z-y), and 0=-4eta*z+lambda_A(1/n+(n-1)y/n-z)+lambda_B(1/m+(m-1)x/m-z). The rates are (lambda_A,lambda_B)=(1,1) for per-vertex copying and (n,m) for per-directed-edge copying. Direct substitution gives x=lambda_A*z/(lambda_A+2eta), y=lambda_B*z/(lambda_B+2eta), a strictly positive z denominator and the exact rational V=[N+m(m-1)x+n(n-1)y+2mnz]/N^2. Independent SymPy algebra checks proved equivalence with the two displayed closed forms, and independent exact rational full 2^(m+n)-state generators independently checked 8 noise/size/protocol cases including singleton sides. SymPy limits checked fixed m, balanced sizes and the n^(1/2) topology regime; asymptotic algebra gives sqrt(n)*VV -> 1/[8eta(1+eta)c], sqrt(n)*VE -> c/eta and VE/VV -> 8(1+eta)c^2 for m/sqrt(n)->c>0. The strict crossover sign follows for c != [8(1+eta)]^-1/2. Singleton within-side correlations are unobservable placeholders multiplied by zero, not fabricated pair expectations. Finitely many cases alone do not prove general or infinite limit; the closed pair-generator identities and limit argument do.

## originality

PASS

PASS (qualified best-of-knowledge): Sood–Antal–Redner develops noise-free voter/link clocks and complete bipartite consensus, while Carro–Toral–San Miguel develops general *node-clock* noisy-voter moment equations. Pymar–Rivera offers a broader noisy coalescing dual and degree-weighted density, but the inspected statements do not evaluate both continuous-time clock conventions for normalized K_{m,n} magnetization nor their common sharp sqrt(n) crossover. The exact second-moment closure is not itself novel. Relevant primary full-text sections and Resultary searches were inspected; no identified existing result directly dominates the full comparative claim. This is not proof of absolute priority: a general stationary covariance identity may yield the final formula through graph-specific specialization, and unindexed equivalent work may exist. The exact statement-vs-prior comparisons appear in the four checks below.

## value

PASS

PASS: The complete bipartite graph is a canonical heterogeneous-network family, and allocating copying activity per vertex versus per interaction are meaningful nonequivalent kinetic rules. At fixed flip-noise eta, the exact positive all-size rational variances reveal a sharp intermediate m~sqrt(n) reversal, with explicit crossover c*=[8(1+eta)]^-1/2. The reversal is not a trivial normalization identity: it depends on combining exact pair-correlation solutions with competing asymptotic regimes, and supplies reusable checks for noisy-voter approximations. The fixed-m and balanced-m/n limits further locate its boundary. Does not claim a phase transition, full law, mixing theorem, equal overall attempts, or exact critical-size sign.

The dated certificate retains the supplied scientific assessment, sources and limitations.
