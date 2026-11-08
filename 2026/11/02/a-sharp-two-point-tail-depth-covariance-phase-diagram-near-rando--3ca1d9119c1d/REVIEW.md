# Independent mathematical audit

## correctness

PASS

Conditional on the cyclic set, all directed forests with those k roots are equiprobable because their k! cyclic permutations are equinumerous. Collapse each root arrow to one symbol; each admissible parent vector with r root arrows contributes k^r. Enumerating all (m+1)^m parent vectors with explicit cycle rejection yields exact polynomials W_m=k(k+m)^(m−1), A_m=ka_m and B_m=kb_m for m=2..5. Cov=(b_m(k)(k+m)^(m−1)−a_m(k)²)/(k+m)^(2m−2), giving P2=−1; P3=k²−2k−19; P4=3k⁴+46k³+192k²+24k−836; P5=5k⁶+168k⁵+2217k⁴+14072k³+40503k²+25728k−64261. Sign P3 changes between 5 and 6; P4 between 1 and 2; P5 positive for all k>=1; P2 negative throughout. m≥2 and k≥1 are enforced, and n<=5 has no positive instance. Independent exact parent-vector implementation checked 16 polynomial assertions and reproduced m=5 W/A/B coefficient rows; polynomial symbolic enumeration proves every integer k in scope, unlike finite k sampling.

## originality

PASS

Uniform rooted-forest counting and conditional random-mapping/forest equivalence are classical, particularly Pitman and Berlinkov. The new claim is a complete pairwise marked-depth covariance polynomial and sign transition for each m=2..5, not the well-known count W_m. Accessible Pitman Sec 2.1 and Berlinkov tree-height asymptotic results do not state this two-marked exact sign diagram. Hansen–Jaworski is a closer potential general-multivariate source; accessible summaries are insufficient for entire noncoverage. Best-of-knowledge PASS with explicit risk that a broader forest generating function implies these polynomial special cases.

## value

PASS

The first positive covariance at n=6 and opposite sign boundaries for the smallest four noncyclic populations identify a natural first dependence transition in random mappings near permutations. Exact symbolic finite-structure census for all root counts k provides a complete meaningful classification on this motivated near-permutation domain, not arbitrary numerical tables or an unjustified all-m claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
