# Independent mathematical audit

## correctness

PASS

The recurrence can be reconstructed exactly stage by stage because every attainable sum is finite and its least prime factor can be computed deterministically. Independent replay reproduced all published cardinalities through generation 27, verified \(Q_n=M_n\) for every \(1\le n\le26\), and obtained \(|C_{26}|=105412\), \(M_{26}=162143\), \(|C_{27}|=170224\), \(M_{27}=262331\), \(R_{27}=262321\), \(Q_{27}=262313\). The positive maximum witness \(100188+162143=262331\) uses two elements of \(C_{26}\). Since \(2M_{26}<2R_{27}\), a composite sum cannot map to \(R_{27}\); exact pair-sum exclusion therefore certifies its absence. The computation is exhaustive integer arithmetic, not sampling.

## originality

PASS

Popescu's full primary preprint defines exactly \(M_n,R_n,Q_n\) and proves \(M_n\sim Q_n\sim c\varphi^n\), but it does not report the finite values \(262321\), \(262331\), or a generation-27 first gap. The earlier paper and OEIS record the cardinality sequence rather than the first missing-prime frontier. Exact-value and semantic searches found no prior report of the onset.

## value

PASS

The maximum and complete-prime frontier are central quantities in the recent asymptotic theory. Locating their first exact separation is a natural finite boundary that complements the asymptotic theorem and is supported by a complete stage-by-stage certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
