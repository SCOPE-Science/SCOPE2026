# Independent mathematical audit

## correctness

PASS

Any new cube must be a suffix; a fixed constituent length determines at most one appended letter. Below length 8 there cannot be three distinct witness lengths. For lengths 8–10 the only possible triple is 1,2,3: the length-1 and length-2 constraints force the middle length-3 block of the final nine letters to contain one u and two v, incompatible with the final block uut for three distinct extension letters u,v,t. At length 11 the frozen proof also excludes 1,3,4 by comparing the count of the fourth-length witness letter in the middle and last four-blocks, and 2,3,4 by the mod-three composition of the first three and first six letters and the resulting two last-letter cases. Thus 1,2,4 are the unique constituent lengths. Labeling by that assignment gives terminal 100, with A and B permutations of 0012 and B ending in 01 or 10. No internal cube can contain a 2 because there are exactly two occurrences. All length-nine factors meet the 2 of B, and the only possible length-six factors avoiding 2 are 001100 and 010100, neither a cube. The only remaining obstruction is the four A/B joins forming 000. The 44 representatives each use all three symbols, and the normalization is unique. A separate prefix-Parikh exhaustive calculation on all words of lengths 0–11 reproduces no shorter crucial word, 50,520 cube-free length-11 words, and 264 crucial words normalizing to exactly the 44 constructions; each of the six witness assignments occurs 44 times. Replay: branches/803f0658-a80a-474d-b98c-43ae286ddbff/independent_ternary_cubes.py and its .out. The attached CSV has the stated 44 AB100 constructions.

## originality

PASS

The distinct result is the census, the complete normal form with its four exclusions, and the unique constituent witness-length profile. Minimum length, examples, and the full ambient avoidance count are established prior work. The sources compared support a bounded originality pass only for the distinct classification.

## value

PASS

The cutoff is the natural minimum for a classical avoidance problem, not an arbitrary word length. The result identifies every shortest right obstruction, explains why all three witnessed block lengths are determined, and lets later work use exact labeled or symmetry-reduced examples without repeating a search. This is more than reproducing the known minimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
