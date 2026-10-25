# Independent mathematical audit

## correctness

PASS

For j=1,2,3, survival of ordered marked leaves as singletons to k blocks gives E[(S_k)_j]=(k)_j(k-1)_j/(n-1)_j. The chance two existing singletons eventually merge together before either merges otherwise is 2/[3(k-1)]. Conditional final cherry expectation is H_k+2*[S_k choose 2]/[3(k-1)] for k>=3. Pair-merger counting yields z_{k-1}=(k-2)z_k/k+F_3(k)/[k(k-1)] for z_k=E[S_k H_k], solved by z_k=k(k-1)/3*[1-(k-1)(k-2)(k-3)/((n-1)(n-2)(n-3))]. Combining with factorial moments gives the full negative covariance stage profile, zero at k=n-1,n; independent exponential waiting times E tau_k=2/[k(k-1)] give Cov(C_n,L_n)=-2/9 exactly after a finite falling-factorial sum. For n=2,3, C_n identically 1 so covariance 0. Established Var(C_n)=2n/45 and Var(L_n)~8log n/n yield correlation coefficient. Separate exact-fraction Markov-chain enumeration tested mean cherries for n=4..13 and independent full stage/joint calculations through bounded n; infinite validity rests on recursion, not test counts.

## originality

PASS

The complete Janson–Kersting Kingman paper studies external lengths and singleton counts but not cherry count cross-moments; the full Disanto–Wiehe ranked-tree paper studies cherries/pitchforks topologically but not external length. The new all-n mixed covariance and full negative stage profile are not entailed by marginal laws. The 2007 François–Mioland paper concerns cherry height and branch-length statistics, but only the abstract was confirmed: its full text remains a significant best-of-knowledge priority risk.

## value

PASS

The exact sample-size-independent negative covariance and its signed time-stage mechanism answer a natural joint genealogy-statistics question connecting topology (cherries) to metric branch length; usable for joint summaries and correlation asymptotics. Neither marginal alone determines the cross-moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
