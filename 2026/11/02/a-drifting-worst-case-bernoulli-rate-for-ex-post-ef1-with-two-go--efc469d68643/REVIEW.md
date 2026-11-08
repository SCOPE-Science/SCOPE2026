# Independent mathematical audit

## correctness

PASS

With a fixed 2-item bundle per participant and independent Bernoulli(p) values on all ordered participant-good pairs, a participant violates EF1 iff both own values are zero and some other bundle values two ones for that participant. Independence of rival pairs gives failure f_m=(1-p)²[1-(1-p²)^m] (m=n-1), and independence of entire participant rows gives P_n=(1-f_m)^n. The derivative sign is determined by 1-G_m(p), where G_m= p/[m(1-p)]·sum_{j=0}^{m-1}(1-p²)^(-j), strictly increases 0→infinity; hence a unique p_n in (0,1) minimizes P_n, and increasing m strictly increases G_m at fixed p so p_n decreases, p_2=1/2. At the critical root t=mp_n² tends infinity but is O(log m); logarithmic equation yields 2t=log m+log log m-log 2+o(1). Also 1-f_m(p_n)=2p_n(1+o(1)), giving log P_min=-n/2 log n+n/2 log log n+n/2 log 2+o(n). Inspected actual verify.py exact binary enumerator and root checks; finite n tests are not the all-n asymptotic proof.

## originality

PASS

PASS best-of-knowledge for exact frozen two-good allocation EF1 chance, unique drifting worst Bernoulli rate and precise logarithmic asymptotic. Prior randomized online and known-valuation best-of-both-worlds EF1 papers concern distinct randomness and conditioning, rather than the fixed-allocation ex-post probability.

## value

PASS

The smallest equal-bundle size capable of failing EF1 yields a natural stochastic fairness risk, with a unique least-favorable distribution parameter that changes with population size and a nontrivial log-log extremal law. Exact result can inform nonadaptive fair-division reliability without claiming policy optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
