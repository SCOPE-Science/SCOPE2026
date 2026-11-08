# Independent mathematical audit

## correctness

PASS

For each N>=8 the restricted support is uniquely determined by a five-part integer composition (a,u,b,v,c) with occupied parts >=2 and gaps >=1, quotienting the normalized masks by reversal. A unit-cell indicator has Fourier transform a common sinc multiplier times P_x(exp(-2 pi i xi)); equality of continuous magnitudes is equivalent to equality of all aperiodic integer autocorrelations, with the maximal nonzero lag recovering N. Independently enumerated all compositions N=8..19, computed correlations by integer bit shifts, and independently checked the provided CHECK.py source: reversal-class counts 1,3,9,19,38,66,110,170,255,365,511,693 and distinct-signature counts identical until N=18, then 692 at N=19. Exactly one size-two fiber is represented by (2,1,10,3,3) and (2,3,5,1,8), sharing the 19-entry correlation (15,12,10,9,9,9,9,8,7,6,5,5,4,3,2,2,2,2,1). Independently checked the polynomial zero-flip Q=(1+z+z^2+z^6+z^7), A=(1+z^8+z^11), B=z^11 A(z^-1)=(1+z^3+z^11); QA,QB have disjoint binary coefficient supports and identical Laurent products. Full finite enumeration proves the first collision only in this restricted class, not unrestricted intervals.

## originality

PASS

Prior Xia–Xu arXiv:2606.19855 gives general three-interval nonuniqueness and polynomial factorization, not an observed complete 8..19 first-collision census with every occupied run of width at least two. The reported earlier three-run witness contains a singleton run; full direct primary PDF was not accessible in this audit, so an implicit classification remains a priority risk. Willms (2013) develops general binary autocorrelation/run relations, not a verified identical first-fiber table. Resultary search returned non-equivalent cyclic prime and sparse Fourier ambiguity records. The audit distinguishes the known zero-flip mechanism from the novel proposed finite restricted threshold.

## value

PASS

The first nonunique resolution N is a natural exact invariant of quantized three-component phase retrieval after excluding isolated one-cell features, and the complete first ambiguity fiber sharply separates reconstructible from nonreconstructible classes. Both the constraint and threshold have mathematical motivation; not a random arbitrary small-instance test. The exhaustive integer-arithmetic certificate and algebraic witness give an independently useful finite classification; no all-length or arbitrary-real-endpoint conclusion is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
