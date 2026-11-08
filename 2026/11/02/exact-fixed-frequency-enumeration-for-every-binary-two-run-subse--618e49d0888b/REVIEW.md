# Independent mathematical audit

## correctness

PASS

After the a-th zero, enumerate q>=b ones, and let t_i be preceding-zero totals. Classifying an occurrence by its first chosen 1 gives the exact weighted identity k=sum_{i=1}^{q-b+1} binom(q-i,b-1)binom(t_i,a). The first r=q-b+1 monotone t_i determine all contributing terms; binom(q,b)<=k and binom(t_r,a)<=k ensure a finite profile set, including b=1 boundary. The first a zeros and remaining b-1 unconstrained ones delimit a+b free slots, giving unique length decomposition q+t_r+sum free nonnegative gaps, hence generating function numerator over (1-z)^(a+b). Positive numerator at z=1 proves exact eventual degree if attainable. The example a=b=2,k=5 has unique (q=3;t=2,3) giving z^6/(1-z)^4. Independently enumerated all short binary words with DP occurrence counting and confirmed profile results; this does not prove unbounded parameters.

## originality

PASS

Best-of-knowledge originality for complete stated claim, after explicit same-object and strong-theorem comparisons; known ingredients and limitations credited. Historical priority is not certified.

## value

PASS

An exact all-positive-frequency rational enumerator and complete sharp-degree characterization for a broad natural two-run class go beyond a known general eventual-degree upper bound and settle the documented difficult 0011-frequency-five regime as an illustration. The positive-coefficient numerator gives useful exact coefficients, not just a degree estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
