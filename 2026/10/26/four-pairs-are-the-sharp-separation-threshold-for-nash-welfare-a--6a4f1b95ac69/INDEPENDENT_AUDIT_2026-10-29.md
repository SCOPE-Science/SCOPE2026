# Independent mathematical audit

## correctness

PASS

For strict complete n-by-n preferences let E(mu)=sum of all 2n partner ranks, N(mu)=product of n-rank. The primary proof is finite exhaustive for n<=3: enumerate (n!)^{2n} labeled profiles, all n! bijections, reject each blocking pair by independent strict rank tests, and retain all ties in argmin E/argmax N. An independent fresh implementation, distinct in structure from stable_welfare_boundary_check.py, enumerated every 46,656 n=3 profiles and found 34,080 single-stable equal sets; for 2 stables 9,180 equal and 2,304 proper Nash subset; for 3 stables 468 equal and 624 proper subset. It reproduced n<=2 as well. For n=4 the supplied rank vectors define a valid profile with precisely four stable matchings and (E,N): (0,1,2,3)->(11,768), (0,2,1,3)->(11,1536), (0,3,1,2)->(11,1728), (2,0,3,1)->(9,1536). The unique egalitarian and Nash optima are disjoint. Exhaustion gives n<=3 inclusion; the finite witness gives sharp n=4 separation without any unverified claim for larger n.

## originality

PASS

Best-of-knowledge new tight first-separation threshold plus labeled three-pair full census for this precise rank-induced cardinal utility. Desai et al (2026) introduce stable Nash-welfare optimization and empirical comparisons, but accessible original abstracts do not state this sharp threshold. Earlier Resultary published small-market sharp boundaries compare egalitarian with minimum-regret or rank-maximal/popularity, mathematically different objective functions; they do not imply the Nash-product result. Full Desai text was not available, so direct overlap is a material residual risk, not falsely excluded.

## value

PASS

The exact earliest size at which widely used stable-matching fairness objectives disagree, including unique incompatible optima, is a motivated sharp finite threshold with interpretive significance for algorithm selection. The exhaustive 3-by-3 census identifies how tie-induced inclusion arises and is not a mere unmotivated recomputation of stable matching counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
