# Independent mathematical audit

## correctness

PASS

The fixed counts leave (ab,bc,abc); the unique c cuts the m copies of b at position β. For both a's after c, the counts reduce to (v+2z,β,0) with v+z≤h, yielding the integer interval max(0,α−h)≤z≤floor(α/2). With one a on each side, the number of b's between the first a and c is γ and the number after the second a is α−γ−h, so the two feasibility intervals are sufficient and determine the unique word. For both a's before c the same interval count has budget β and argument γ, with α=γ+2h. The supports have sizes 2h+1,(β+1)(h+1),2β+1, pairwise intersection sizes h+1,β+1,1, and triple intersection size 1. Thus each cut has βh+2m+1 images, which sums to the stated polynomial. The triangular counts peak at floor(B/2)+1; they meet only at their respective endpoints, giving size 3 with the middle skeleton, while (α,β,γ)=(m,0,0) attains floor(m/2)+2 for m≥2. This also verifies m=0 and 1 via the common corner. Placement gives (m+1)(m+2)(m+3)/2 words, so the stated mean over images and the one-word-per-image zero-error interpretation are correct. The frozen checker was inspected, not run; the analytic count is exhaustive for all m.

## originality

PASS

The closest located fixed-content theorem enumerates images with two copies of each endpoint, not the multiplicities with one c. Accessible general Parikh results treat equivalence, distinguishability, rewriting or singletons, not the full pointwise fiber law. A reference to unidentified work at the same composition and an abstract-only 2023 comparison leave a priority risk, but no matching stronger or exact result was established.

## value

PASS

One c provides a natural cut and two a's are the first repetition on the opposite end that allows growth of a fiber within one ordered skeleton. The exact law identifies all ambiguities, gives the largest reconstructible fixed-content code, and separates bounded mean occupancy from linear worst ambiguity across an entire infinite family. It resolves more than equivalence testing or a partial word census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
