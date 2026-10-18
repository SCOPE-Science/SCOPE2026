# Independent mathematical audit

## correctness

PASS

For z=(x,a) in the unit sphere of the real l1-sum of X and ell1(Gamma), the dual norm is max(||f||,||c||_infinity)=1. Every slice norms at least one block: an X-only witness gives sup distance at least b+dc_X(x), while an almost-normed atomic coordinate gives at least 2(1-m). Since any given slice belongs to one of those cases, the min of both is a universal lower bound. Conversely an X-functional slice forces atomic norm <epsilon, yielding <=b+dc_X(x); a coordinate slice at |a_gamma| approaching m forces distance <=2(1-|a_gamma|), yielding <=2(1-m). Endpoint b=0 and m=1 are consistent; if X is Daugavet, dc_X(x)=1+||x|| so min is 2(1-m). An independent exact-rational check of 14,640 normalized signed integer vectors in ell1^d, 2<=d<=5, matched the known pure ell1 formula. CAVEAT: the proof’s ancillary assertion that a nonzero ell1 vector's infinity norm may fail to be attained is false—nonzero ell1 vectors attain that supremum; it is an unnecessary overcautious limit argument, not a premise or failure of the theorem. The KaTeX equation has an extra right brace; this must be corrected before publication.

## originality

PASS

Best-of-knowledge PASS for the mixed arbitrary-Banach/atomic-ell1 minimum formula. Choi–Jung give pure ell1 exact constants and lower estimates for general l1-sums, and Haller–Pirk–Veeorg give qualitative point properties; neither inspected statement yields the second sharp matching upper bound for arbitrary X and Gamma. A recent mixed ellp-ell1 result returned by Resultary treats a Daugavet-component-specific case and does not dominate the arbitrary X theorem.

## value

PASS

The identity supplies a sharp quantitative preservation/obstruction formula for the natural construction X⊕_1 ell1(Gamma), upgrading pure-atomic exact constants and mixed-sum one-sided estimates. Identifies two geometrically meaningful competing slice mechanisms; useful independently as an exact stability law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
