# Independent mathematical audit

## correctness

PASS

I independently enumerated all (n!)^(2n) labeled rank arrays for n=1,2,3. For each bijection, the replay forms the mask of pairs preferred by the men and the mask of pairs preferred by the women; their intersection is empty exactly for a stable matching. It collects exact integer side sums and utilities and maximizes the product at the minimum absolute gap without breaking ties arbitrarily. It returns unit ratio at n=1 and 2, and the five frequencies (44136,504,1728,144,144) at ratios (1,9/8,3/2,2,9/4). Independently applying Burnside to the rank arrays (two label permutations and an optional side swap) gives orbit frequencies (634,7,24,2,2); all 144 extremizers have trivial stabilizer. The replay is branches/independent-replays/matching.py. Inspection of the frozen checkers confirmed full profile coverage and the strict blocking criterion; the orbit companion prints rather than individually asserts the orbit histogram, which the independent calculation checks. For the displayed witness, the only stable matchings ABC and ACB have side sums (2,4) and (4,0) and products 36 and 81, respectively. For n=2 with both matchings stable, the four blocking tests force one side to unanimously prefer each matching and the other to prefer the opposite; both products are 4 and both disparities 2. The factor is a product ratio, not a geometric-mean factor. No larger market is covered.

## originality

PASS

The audited distinct result is the exact Nash-product price and its three-pair frequency and symmetry distribution, not the utility model, the finite profile enumeration problem, or the existence of competing stable-matchings objectives. Prior Resultary statements force 2,520 penalties, a material contribution to the count; they do not give their magnitudes.

## value

PASS

Sex-equality and Nash welfare are both motivated objectives on the same stable set. The smallest market where the requirement causes loss is a natural cutoff rather than an arbitrary slice. The exact sharp factor and the magnitudes and orbit counts distinguish severe penalties from simple criterion disagreement and give a complete reproducible benchmark for this low-order obstruction, without extrapolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
