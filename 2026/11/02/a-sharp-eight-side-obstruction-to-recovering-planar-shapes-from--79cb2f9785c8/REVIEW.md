# Scientific review: rotational width-correlation inverse geometry

## Correctness

**PASS.** The object is a centered, full-dimensional, centrally symmetric equilateral polygon, with width measured as one-dimensional orthogonal projection length and pair-correlation normalized over a half-turn. The pointwise width is the sum of absolute projected generator lengths. Its nonvanishing cosine Fourier kernel makes the full width correlation equivalent to the circular difference multiset of generator directions. For two or three directions, the circular gap argument reconstructs the generator set up to rotation/reflection. The two exhibited four-direction sets have exactly one occurrence of each of the six interval classes, but different cyclic gap multisets. That proves identical correlations at every lag and noncongruence, not merely approximate coincidence.

For the cubic width moment, the explicitly listed sign-switch partitions and an explicit antiderivative yield the exact radical formula. The positive difference is checked by a strict radical inequality. The support-function identity supplies the area/perimeter formulas, including their curvature/distributional boundary interpretation. Positive Poisson convolution of polygon curvature measures gives analytic positive-curvature shapes; its nonzero Fourier multipliers preserve both the correlation equality and the noncongruence. The explicit third-order Fourier coefficient proves the smooth shapes remain distinguishable by a higher-order statistic.

The executable verifier passed 3,908 checks, including the SymPy exact radical integration path. Finite-grid enumeration is clearly distinguished from the proof of continuous uniqueness. Required assumptions and numerical versus exact roles are explicit.

## Originality

**PASS under the cited-source comparison, with historical-priority risk.** Baake and Grimm (arXiv:math/0610411) develop homometry and diffraction through difference measures, not inverse geometry of rotation-averaged convex-body widths. Gover (arXiv:1401.4749) treats generators, congruence, and determinant-volume formulas for zonotopes; the latter are acknowledged. Bianchi, Gardner, and Kiderlen (arXiv:1003.4486) investigate a different covariogram, namely the autocorrelation of the indicator function of a body, so its planar uniqueness theorems do not cover the width-power-spectrum inverse problem. The pair of four-point homometric angle sets is a pre-existing Z-related tetrachord pair and is not claimed as an original combinatorial discovery.

published-finding corpus comparisons found an inverse width-*distribution* classification for tangential symmetric polygons and previous width covariance work for regular polygons and orthotopes, but not the stated two-lag correlation equivalence together with the sharp equilateral four/six/eight cutoff and cubic-moment separation. One relevant published-finding corpus full-text URL was inaccessible, so only its returned scientific summary was assessed; this remains a concrete residual risk, not an asserted whole-document exclusion. No equivalent dominating theorem was identified in accessible primary full texts or research-index summaries. Independent historical priority has not been established.

## Mathematical value

**PASS.** This is a motivated inverse problem about recovering a convex shape from the complete second-order statistics of its projected widths under unknown rotation. It gives a sharp polygonal complexity boundary, a specific pair of unit-edge obstructions even after area and perimeter are known, an exact low-order statistic that separates the ambiguous pair, and an extension to analytic positive-curvature bodies near circular geometry. The identities showing which intrinsic volumes second-order statistics necessarily retain clarify the information loss. The result is not an arbitrary finite slice or a claimed general solution to phase retrieval.

## Limits and comparison cautions

Rigidity is restricted to centrally symmetric equilateral four- and six-gons; the octagonal pair proves failure in that class, not universal minimality among all convex polygons. The cubic moment separates the constructed pair, not every homometric configuration. The analytic extension is planar and noiseless. Literature from other fields may restate portions of the sharp obstruction in different language; the classical homometric prototype and standard Fourier facts are explicitly credited.

Self-review: passed. Independent audit: not yet performed.
