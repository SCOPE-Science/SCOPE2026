# Independent mathematical audit

## correctness

PASS

PASS. Reconstructed the unnormalized Laplacian on 01,12,23,30, unit-priced first three edges and closing price tau>0, nonnegative independent weights and total price B>0. Reflection concavity reduces maximum Fiedler value to weights (a,b,a,c); zero-sum symmetry gives even eigenvalue 2a and the odd 2x2 block [[a+2c,-a],[-a,a+2b]]. At unit gap the PSD constraints a>=1/2, U=a+2b-1>0, V=a+2c-1>0, UV>=a^2, yield cost >=(1+tau+(3-tau+2sqrt(tau))a)/2 by AM-GM. If tau<=9 the minimum at a=1/2 gives gap 4B/(5+tau+2sqrt(tau)), unique among reflection-fixed allocations when tau<9. If tau=9, equality yields the claimed interval 1/2<=a<=3/2, b=a+1/2, c=1/2-a/3 at unit gap. If tau>=9, unrestricted Rayleigh vector (-3/2,-1/2,1/2,3/2) has squared jumps 1,1,1,9 and norm^2 5; hence lambda_2<=B/5 with equality at path weights (3B/10,2B/5,3B/10,0), unique for tau>9. Closing-edge positivity for tau<9 follows strict gap increase above B/5. Independent numpy eigenspectrum and price comparisons checked 9 regimes; numerical tests only corroborate the proof.

## originality

PASS

Best-of-knowledge, theorem/implication-based comparison of relevant primary literature; a failed search by itself does not prove historical priority. Closest known published results address different parameters/objects or only more general frameworks.

## value

PASS

PASS. Exact one-exceptional-edge C4 conductance allocation is a natural graph-design boundary problem, and the nontrivial edge-retention/deletion price threshold 9 plus critical optimizer face is an independently useful network design fact. It is not merely naming a general semidefinite program or tabulating one arbitrary graph: the sharp all-price transition and unrestricted uniqueness supply a structural threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
