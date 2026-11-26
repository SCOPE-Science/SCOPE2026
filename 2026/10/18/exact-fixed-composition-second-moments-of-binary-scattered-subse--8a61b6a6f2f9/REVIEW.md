# Independent mathematical audit

## correctness

PASS

The repaired proof counts distinct words, not embeddings. Appending zero makes the complete ending-zero set equal to the old subsequence set with a zero appended, including previously present words. For inclusive counters (i,j) this gives (i+j,j), with the symmetric update for one and D=i+j-1. Splitting the weighted word sums by their last letter gives separate 2-by-2 and 3-by-3 systems for i,j and i^2,j^2,ij. I checked the determinants, adjugate entries and both resulting rational series by exact symbolic arithmetic independently of the frozen 9-state certificate. The empty term is one, and on either axis the series encode the unique constant word with D=n+1. Division by the binomial count normalizes the fixed-composition moments. Independently, the Stern-pair update gives D+1=d(2m+1) and taking the appropriate row differences gives the fair iid shifted-square OGF (4-z)/(1-5z/2+z^2/2); subtracting the shifted mean squared gives the stated, now attributed variance. The retained composition result and the attributed specialization are both mathematically correct.

## originality

PASS

PASS applies to the repaired composition-resolved second-moment evaluation only. The original scope was too broad: the evaluated fair iid second moment and variance follow directly from Stanley's already evaluated Stern-row square sums and the known mean, and the composition first moments are determined by the published arbitrary-bias mean. The repaired Finding no longer claims any of those as new and makes the exact Stern reduction explicit. The strongest checked Stern results sum over all indices; the later exact joint deletion-ball result marks deletion radii under fair iid words. Neither separates binary host compositions. The retained explicit bivariate function has distinct content on the inspected evidence; this is not a proof of priority.

## value

PASS

For the natural count of all distinct binary deletion outcomes, the two-variable evaluation gives exact conditional variability for each composition without summing over the individual words. It distinguishes fluctuations within a fixed letter composition from fluctuations under mixing, and evaluates the moment for every Bernoulli bias. These uses belong to the nontrivial square-moment evaluation; the already implied unweighted formula and general expectation are not counted as new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
