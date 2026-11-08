# Independent mathematical audit

## correctness

PASS

The final integer sum reduces parity term-by-term before summing, not the parity of a global sum. The published run-length transform has S(2m)=1 and S(2m-1)=m. Appending a terminal zero to exactly r padded bits yields uniquely factored one-run tokens with deficit delta(length)=length+1-4v2(S(length)). Nonnegative deficits and only two zero tokens (1110,11111110) give M_r=floor((r+1)/4) and the full 0..M_r spectrum. For deficit s=(r+1) mod4, coefficient extraction from [1-y-y²-z-z²-z³]^-1 gives the four maximizer laws. Fixed positive deficit d uses finitely many positive-deficit tokens and powers of (1-x4-x8)^-1, proving rationality and denominator bound. Checked n=0,r=0, leading zeros, all residues s. Independently computed direct Lucas parity versus run product for n<4096 and all n<2^r up to r=12, recovering all maxima/counts. The primary 2024 published journal PDF was separately inspected: its Theorem 14 (page 12) states this exact parity sum and run transform, confirming the citation. The 2023 arXiv preprint uses Theorem 17 for the same result; different numbering is not a mathematical gap.

## originality

PASS

The transform identity of Rampersad–Wiebe is explicitly pre-existing, whereas the exact valuation edge language, 2-adic spectrum, four Fibonacci-denominator counting formulas and fixed-deficit recurrences require separate arithmetic optimization. Kropf–Wagner treats general block-transform and limit laws, not these sharp finite dyadic maxima. Best-of-knowledge originality PASS for the new classification, not for the underlying transform.

## value

PASS

This supplies a complete, naturally parameterized valuation-edge distribution for a published nontrivial binomial parity sum, including the entire maximizing language and all fixed-edge recurrences. The questions are arithmetically motivated by the known run-length transform, not arbitrary test digits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
