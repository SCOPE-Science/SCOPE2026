# Independent mathematical audit

## correctness

PASS

The CRT representation n=au+bv+ab t with 0<=u<b, 0<=v<a, t>=-1 is unique; for t>=0 the exact triple denumerant is sum_{j=0}^t(1+min(u+bj,v+a(t-j))). At t=0, the exact multiplicity is 1+min(u,v); t=1 gives 2+u+v in its low-multiplicity triangle; t>=2 yields at least a+3. Counting rectangle levels and triangle diagonals gives N_k=a+b-k (1<=k<=a), N_{a+1}=a and the stated G_k. Taking weighted maxima among t=0 and t=1 yields g_k=ab-a-b+bk and g_{a+1}=b(2a-1), hence the first increment change b to a. Zero case follows Sylvester genus. Independently implemented integer generating-function DP for 52 coprime (a,b) pairs and checked all levels through a+1. The mathematical proof, not the bounded DP, handles all coprime 2<=a<b.

## originality

PASS

The uniform exact initial representation spectrum and first slope kink for the special labeled (a,b,a+b) family were not established by inspected prior statements. The general three-coin quasipolynomial bounds of Aldrich et al., generalized Frobenius algorithms, and Komatsu arithmetic-progression/Fibonacci triple results provide context or disjoint parameter coverage. Broad denumerant methods may still imply the displayed formulas, and the relevant 2026 full text was inaccessible; therefore priority is qualified.

## value

PASS

The redundant third generator does not change the ordinary Frobenius semigroup but changes the exact multiplicity distribution. A complete first phase and sharp first kink for all coprime pairs are natural generalized Frobenius invariants with a mechanism that distinguishes membership from representations; this is not an arbitrary fixed small numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
