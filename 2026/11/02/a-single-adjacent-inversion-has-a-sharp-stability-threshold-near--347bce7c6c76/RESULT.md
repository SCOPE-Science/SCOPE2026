# A single adjacent inversion has a sharp stability threshold near a common roommate ranking

## Finding

**Theorem (exact one-inversion law).** Let \(n=2k\ge4\) and label the participants \(1,2,\ldots,n\). Originally every participant ranks every other participant by increasing label. Choose exactly one participant \(x\) and swap two adjacent entries in that participant's list, leaving all other lists unchanged. Let \(\mathcal M\) be the set of stable perfect matchings under the resulting strict, complete preferences. Then:

1. \(\mathcal M=\varnothing\) **if and only if** \(x=2j\) for some \(1\le j<k\) and the exchanged entries, in their original order, are \(2j-1\) and \(2j+1\).
2. In every other case, \(\mathcal M\) contains **exactly one** matching. This is the standard adjacent pairing \(M_0=\{\{2i-1,2i\}:1\le i\le k\}\), except when \(x=2j-1\) and the exchanged entries are \(2j,2j+1\), for some \(1\le j<k\). In that exception, the unique matching is obtained from \(M_0\) by replacing pairs \(\{2j-1,2j\}\) and \(\{2j+1,2j+2\}\) with \(\{2j-1,2j+1\}\) and \(\{2j,2j+2\}\).

Exactly \(k-1\) of the \(n(n-2)\) possible participant-plus-adjacent-swap choices destroy solvability, and exactly \(k-1\) preserve solvability while changing the unique matching. With the choice uniform among these possibilities, the probability of having **no** stable perfect matching is therefore exactly \(1/(2n)\), for every even \(n\ge4\).

## Assumptions and scope

All lists are complete, strict and contain the other \(n-1\) people. A stable perfect matching pairs every participant, and it has no *blocking pair*: two unmatched-to-each-other people who both prefer one another over their assigned partners. The common master order ranks smaller labels higher, but a participant never lists themselves. The perturbation changes only one list and consists of exactly one transposition of consecutive entries in that list. The count treats the participant and swap position as distinct equiprobable choices. No claim is made for two or more inversions, ties, incomplete lists, or odd participant counts.

## Proof

**Forced-pair lemma.** If two people are each other's top remaining acceptable choices inside a set of currently unmatched people, every stable matching of the whole instance consistent with already forced pairs must pair them, provided those earlier pairs cannot form a new blocking pair. Otherwise they would block each other's outside partners. The argument applies recursively when each removed pair is also mutually first among the then-unremoved people and strictly prefers its own partner to every person removed at a later stage; all earlier forced pairs have this property here.

Write \(M_0=\{\{1,2\},\{3,4\},\ldots,\{n-1,n\}\}\). Without the perturbation its pairs are successively mutually first among the unpaired people, hence it is stable and unique. A single adjacent swap can change a person's comparison involving their \(M_0\)-partner only when their partner exchanges positions with another entry. If the partner is promoted, or the swap excludes the partner, no new blocking pair can arise from \(M_0\): all preferences besides those of \(x\) are unchanged, and \(x\) has not acquired any new person preferred to its partner. In each such case the recursive mutually-first-pair induction also still forces every pair of \(M_0\) (the canonical partner remains the first available choice of \(x\) after smaller-label pairs have been removed), giving uniqueness.

For \(x=2j-1\), the only possible *demotion below an available alternative* occurs by swapping canonical partner \(2j\) with \(2j+1\); this requires \(j<k\). All pairs strictly before \(j\) are forced as above. In the residual instance the people \(2j-1\) and \(2j+1\) rank each other first, so they must be paired. The next mutually first residual pair is \(\{2j,2j+2\}\); all subsequent original adjacent pairs are forced. This is the asserted sole candidate. It is stable: the earlier and later adjacent pairs cannot block across blocks, since each person in an earlier unmodified pair prefers their partner to everyone with larger label; inside the changed four-person block, \(2j-1\) and \(2j+1\) get their favorite remaining partner, while \(2j\) and \(2j+2\) are the best available partners after removal of that pair, and neither of the first pair prefers switching. Therefore the candidate has no blocking pair, so it is uniquely stable.

For \(x=2j\), the only demotion below an available alternative is the exchange of partner \(a=2j-1\) with \(b=2j+1\), which again requires \(j<k\). All earlier pairs are forced. The three remaining people \(a,x,b\) prefer both other members of this triple to every person with a larger label; their respective top choices *within the triple* form the directed cycle
\[
a\longrightarrow x\longrightarrow b\longrightarrow a.
\]
In any perfect matching, either none or exactly one pair lies entirely within this three-person set. If none lies inside, any two members block their outside partners. If one pair lies inside, the remaining triple member is partnered outside; among the two inside partners, one prefers this outsider-matched triple member to the current partner, and that outsider-matched member prefers both other triple members to their partner. These two block. Hence no stable perfect matching exists.

For the final count, each of the \(n\) lists has \(n-2\) adjacent swap positions. There are exactly \(k-1\) qualifying even agents with their unique fatal swap and \(k-1\) qualifying odd agents with their unique matching-changing swap. Thus the fatal fraction is
\[
\frac{k-1}{n(n-2)}=\frac1{2n},
\]
as claimed. Every case has been exhausted.

## Verification

Run `python verify.py` with standard-library Python. The independently written checker generates every one-list adjacent-swap profile for \(n\in\{4,6,8,10\}\), enumerates *all* perfect matchings and tests each unordered pair for mutual blocking. The observed counts of no-solution, changed-unique-solution and nonunique-solution profiles are, respectively, \((1,1,0)\), \((2,2,0)\), \((3,3,0)\), and \((4,4,0)\), from \(8,24,48,80\) total perturbations. Each actual stable matching is compared with the independently computed predicted matching. The finite checks corroborate, but do not replace, the all-size proof.

## Relationship to prior work

A strict shared master ranking produces an easily forced adjacent-pair stable matching, a standard baseline considered in the literature on preference master lists. Stable-roommates instances may lack solutions under arbitrary preferences; Chin and Michelen (2026) establish asymptotic nonexistence under completely independent, uniformly random rankings. Chen and Schlotter (2025/2026) study adjacent-swap interventions as part of general control and bribery complexity, rather than this distance-one, common-baseline exact classification. The result here identifies the exact boundary in the *opposite*, highly correlated, one-inversion regime, including the all-size uniqueness and exact solvability-loss frequency; it does not claim discovery of odd-cycle blocking obstructions or general stable-matching algorithms.

## Limitations

The theorem assumes a strict common order, exactly one adjacent reversal, complete preferences, an even participant count and the usual pairwise stability notion. The frequency \(1/(2n)\) holds only under uniform participant-and-swap-position sampling. The source comparisons cannot exclude previously unpublished or unindexed formulations of the same specialized classification. Computational validation covers \(n\le10\) only; generality follows from the proof.

## References

- Chin, B. and Michelen, M., *The random stable roommates problem typically has no solution* (first public 12 January 2026), https://arxiv.org/abs/2601.07612.
- Bredereck, R., Heeger, K., Knop, D. and Niedermeier, R., *Multidimensional Stable Roommates with Master List* (2020), https://arxiv.org/abs/2009.14191.
- Chen, J. and Schlotter, I., *Control and Bribery in Stable Marriage and Stable Roommates: A Complete Complexity Landscape* (2025, revised 2026), https://arxiv.org/abs/2502.01215.
- Bredereck, R., Chen, J., Finnendahl, U. P. and Niedermeier, R., *Stable roommates with narcissistic, single-peaked, and single-crossing preferences* (2020), https://doi.org/10.1007/s10458-020-09470-x.
