# Scientific assessment

## Correctness — PASS

For an arbitrary prescribed arrival-order outcome \(\pi\), the vacant set just before car \(i\) is forced. Its request choices are a singleton unless its allocated space is largest among the remaining spaces, in which case the choices are that space and the previously occupied smaller spaces, counted exactly by \(\pi_i-n+i\). Multiplication is justified inductively because these choices preserve the prescribed occupied set. For a right-to-left maximum, only a nonmaximum position can contribute an earlier smaller occupied space; the resulting bound \((k+1)^{n-k}\) is tight only for the specified prefix-small/suffix-decreasing form. Cases \(n=1\) and ties between maximizing \(k\) are explicitly covered. A direct simulator independently exhausts all preferences for \(1\le n\le7\). This finite test corroborates rather than proves the unrestricted theorem.

## Originality — PASS (best-knowledge comparison)

The nearest primary source, Hallam–Molebash–Porter (arXiv:2609.35638v1), introduces the *frustrated* rule and counts all successful words by a double factorial; it does not in the inspected main results give the full distribution by exact final permutation or the modes. Franks et al. (arXiv:2301.10830) previously investigated fibers under **different first-vacant-forward** parking rules. Their results motivate the question but do not furnish the record-maxima factor for the farthest-free rule. Further related parking-outcome work for MVP parking (arXiv:2207.13041) and interval Fubini rankings (arXiv:2603.00693) involves different dynamics. Searches for fixed outcomes, greatest-vacant parking, equivalent formulations, and broader fixed-order enumeration did not locate a covering result. Search absence is not proof of originality; older or unindexed equivalent formulations remain possible. The published total enumeration is expressly excluded from the claimed contribution.

## Value — PASS

The complete fiber formula refines the newly studied double-factorial class into an exact distribution over all \(n!\) feasible outcomes. It gives exact outcome probabilities, the maximal probability, and all modal outcomes, resolving a natural statistical feature of the model for every size. This is a genuinely parameter-wide distribution theorem, not merely a small numerical computation or a restatement of the total count. A prior fixed-order approach for other parking rules establishes motivation for this more refined statistic.

## Limitations

The theorem is for unit-size cars and the precise frustrated-driver rule; it makes no assertion about other parking variants. Bibliographic searches cannot establish uniqueness, and an independent mathematical audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
