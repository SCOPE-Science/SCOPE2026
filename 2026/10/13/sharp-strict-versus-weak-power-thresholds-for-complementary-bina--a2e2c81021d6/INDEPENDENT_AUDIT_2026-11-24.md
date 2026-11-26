# Independent mathematical audit

## correctness

PASS

The frozen length-five and length-seven classifications are both correct: an independent run enumerated 16 and 64 normalized images and used maximal distance-p match runs to compute critical exponents, rather than replaying the uploaded factor tests. It found no strict survivors, and exactly the stated two normalized weak survivors at each length. The archived verifier and witness data were inspected, not executed. The repair retains only length seven. A fresh bounded check verified a single common exclusion input for each boundary: `01` (critical exponent 1) rules out all 64 normalized strict candidates, and `001` (critical exponent 2) rules out exactly 62 normalized weak candidates, leaving 0100110 and 0110010. A run of r matches at distance p corresponds exactly to a factor of length p+r and period p; comparing 2(p+r) to 5p detects the strict/weak forbidden exponents exactly. I checked the actual Kobayashi theorem (Shallit–Shur–Zorcic Theorem 4): each whole image must have exponent below two, endpoints separated, the stated long overlap condition, and preservation on admissible words of length at most four. The independent check confirmed least period 6 for each image, different first and last bits within each pair, no proper overlaps of lengths 4–6, and the weak condition on all 22 nonempty admissible short inputs for both survivors. The empty word is automatic; complementing the entire output yields the other two maps. The published criterion proves preservation for arbitrary finite length, not just the tested inputs. Repaired RESULT.md, SLOGAN.txt, VERIFICATION.md and verify_length7.js are in /workspace/repairs/4/; replay there with node verify_length7.js. The bounded certificate logic was independently executed and the frozen package is unchanged.

## originality

PASS

This is a fresh assessment of the narrowed length-seven claim. The original two-length novelty framing fails in part: the prior public Research Commons proof covers the complete length-five distinction, including the four weak maps by direct specialization and symmetry. That is verified statement coverage, not a finding that the frozen mathematics is false. Length five is removed from the claim. The remaining length-seven classification at 5/2, now with two common exclusion inputs and global weak preservation, is outside the proven ranges of the strongest inspected source statements. Neither the low-threshold complete classification nor the higher-threshold admissible-length theorem determines it.

## value

PASS

The repaired length-seven boundary is a concrete instance of the open short-length transition problem between 7/3 and 3. It distinguishes strict from weak preservation at the same threshold, classifies all preservers rather than giving a seed, and gives two short reusable obstruction inputs that work uniformly across all excluded cases. The gain is not merely a finite census: the weak positive condition holds for every input length by the criterion. The result neither claims the full transition spectrum nor reclaims the covered length-five case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
