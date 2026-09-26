# Independent audit — 2026-09-26

Record: `2026/09/09/040`. Verdict: **correctness PASS; originality PASS (bounded); scientific value PASS (bounded).** Disposition: retain accepted.

## Correctness

I independently enumerated all 183 normalized line equations over F13 and all 13 affine graph points plus their determined directions for each polynomial. The independently computed direction sets and intersection spectra agree exactly with RESULT.md: x^7 has 8 directions, spectrum {1:126,2:18,3:36,8:3}, with all 21 points on a tangent; x^9+x^5 has 10 directions, spectrum {1:96,2:52,3:32,6:1,10:2}, with 23 tangencies; x^7+2x^3 has 11 directions, spectrum {1:91,2:59,3:16,4:14,6:2,11:1}, with 24 tangencies. Each spectrum sums to 183 and has no zero intersection. Separately, I enumerated 156 nonzero monomial forms, 11,232 binomial forms, 41,184 monic trinomial forms, and 402,233 normalized degree-2-to-6 forms. No form has nine directions; their direction-count sets respectively are {1,8,12,13}, {1,8,10,11,12,13}, {8,10,11,12,13}, {1,11,12,13}. Linear forms have one direction. Scaling and adding a linear/constant term permute slopes, so the stated normalization and at-least-four-terms, degree-at-least-seven implication hold. These computations were implemented independently from the record scripts.

## Prior work and originality

The Blokhuis 1986 lower bound of 3(p+1)/2 supplies the known 21 minimum and the Rédei direction framework is classical; neither is new here. Kadoo, *The Minimal Blocking Set Of Size 22 In PG(2,13)* (2010), DOI 10.33899/csmj.2010.163898, expressly claims a minimal 22-point Rédei-type set, omitted from this record's references. I read the open journal PDF. Its printed 13 affine points at p.84 and nine infinity points at p.85 (PDF pp.8–9), taken literally, yield 22 points and line spectrum {1:113,2:31,3:36,8:2,9:1}, but only 21 essential points; the printed infinity point (1,6,0) has no tangent. This explicit check prevents treating that printed construction as a certified minimal counterexample to this record's cautiously qualified 'remains open' sentence. The three stated witness spectra and finite polynomial exclusion remain a bounded computational contribution; no global classification or PGL uniqueness is established. The omission of Kadoo and its problematic witness materially limits any novelty claim about size 22.

## Scientific value and limits

The exact small-field certificates and polynomial-family restriction are reusable for a search for nine-direction functions, but only the listed families and three witnesses are covered. The claimed coding connection is motivation rather than a derived code parameter result. The status of all size-22 minimal blocking sets is not resolved by this package or by the literal coordinates in the cited 2010 paper. This audit does not assert its full proof is invalid beyond the printed witness checked here.

Sources: record RESULT.md and artifacts/verify.py, artifacts/polylog.py; Kadoo journal PDF https://csmj.uomosul.edu.iq/index.php/csmj/article/download/36365/36155/36458; Blokhuis, *On the size of a blocking set in PG(2,p)*, Combinatorica 6 (1986), 111–114.
