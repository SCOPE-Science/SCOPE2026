# Independent mathematical audit

## correctness

PASS

For n=m p^a q^b with (m,pq)=1 and positive derivative, D(n)=n(aq+bp)/(pq) is integral by the original two terms. Outside-prime valuations increase by those of aq+bp; on a finite positive orbit they must stay constant, so each positive coefficient aq+bp is supported on p,q and m remains unchanged. At a largest orbit integer, a/p+b/q≤1. Positive a,b imply a<p and b<q, making the coefficient >1 and coprime to pq, impossible. On the smaller-prime axis, smoothness leaves a=1 or p; on the larger-prime axis it leaves b=1, q, or p^k<q. Exponent 1 leads to m then zero; exponents p and q on their respective axes give fixed points. For b=p^k the next exponents are (k,p^k−1); the next coefficient kq+p(p^k−1) is >1 and prime to both p and q because 1≤k<p and 0<p^k−1<q. Here k<p follows from p^k<q≤p^p. This proves the whole positive-periodic set, including the converse by direct substitution and with arbitrary coprime m. The contrapositive does not assert existence above the bound. RESULT.md lines 18–58 carry the proof. The inspected verify.py and recorded verification_output.txt report a finite regression (236 pairs, 16,567 direct comparisons, 297 two-step candidates), not an exhaustion or a necessary certificate; no bundled code was run.

## originality

PASS

The fixed families and the instance {2,3} are not new. The distinct contribution of this frozen record is the uniform exclusion of nonfixed positive periods for p<q≤p^p. Two later catalogued all-pairs theorems subsume that exclusion, but their records postdate this result; no earlier disclosure of those stronger results was identified. The inspected earlier sources do not imply the uniform exclusion.

## value

PASS

The dynamics of positive integer iterates for a two-prime support are not determined by the known fixed-point theorem. This gives a uniform cycle exclusion and an explicit necessary bound tied to the prime-power exponent of a possible orbit maximum, not an arbitrary tested parameter box. The monotonicity/maximality argument shows why the bound arises and handles arbitrary outside-prime factors. The cutoff is not claimed optimal and the stronger later classification should be preferred for the unrestricted conclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
