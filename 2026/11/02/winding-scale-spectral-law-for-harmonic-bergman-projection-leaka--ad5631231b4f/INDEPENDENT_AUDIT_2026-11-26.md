# Independent mathematical audit

## correctness

PASS

Beta integration and angular orthogonality give the bilateral k-shift weight m_{(a+b)/2}/sqrt(m_a m_b), a=|n|, b=|n+k|. Strict convexity of h=log m gives a single zero mode for even k and none for odd k. The integral for h'' is positive, strictly decreasing and bounded by max(1,p)/(1+s)^2, so the exterior midpoint gap is O_p(k^2/(1+n)^2) and decreases as n increases. Inside, convexity of h(j)+h(k-j) puts the largest gap at an endpoint; the weights tend to one in the tails. This proves trace class, norm one and the exact inverse norm, whose constant follows from m_s~Gamma(p+1)s^{-p}. Uniform gamma-ratio asymptotics away from the finitely many scaled endpoints give the interior profile and two matching exterior profiles; trim endpoint intervals and use the O(1/R) normalized defect-tail bound for Lipschitz tests. For a fixed positive threshold the pointwise tail bound rules out all modes beyond sufficiently large R, and the limit profiles have measure-zero threshold boundaries. With u=(1-tau)^{1/p}, the interior length is 1-sqrt(1-u), and both exteriors together have length 1/sqrt(1-u)-1. Their sum yields the claimed count; integrating in tau gives p B(p+1,1/2). The p=1 square sums yield exactly both terms in the finite trace formula, also for k=1,2. Independent bounded replay: python3 /workspace/branches/review_checks.py 5; uses exact rational rising-product weights for p=1,2,3, k=101,907 and three thresholds, also checking the p=1 interior sum. The frozen checker was inspected, not executed.

## originality

PASS

The fixed-winding quasihomogeneous shift mechanism is known. The distinct supported contribution is the high-winding spectral counting and Lipschitz trace law for angular-character compression on the weighted harmonic disk, with its explicit coefficient and endpoint inverse amplification. The closest inspected catalog and primary sources do not cover that contribution by equivalence or a demonstrated stronger theorem; this is not a priority certificate.

## value

PASS

The natural positive defect measures energy outside the harmonic subspace. Its full normalized spectral law distinguishes the finite sign-crossing band from the two infinite tails and quantifies how many modes incur serious loss despite bounded invertibility at any fixed winding. The closed coefficient and inverse norm turn those complementary phenomena into usable quantitative invariants; neither follows from fixed-symbol boundedness alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.
