# Exact nonexistence and one-seat repair census in a two-hospital couples market

## Finding

In the fully specified two-hospital, four-doctor market described below, the complete count of capacity-\((1,1)\) BIS-unstable instances (instances with no BIS-stable matching) is exactly \(640\) among \(11{,}520\) labeled profiles. Each such instance becomes BIS-stable after **either** one-place expansion, to \((2,1)\) or to \((1,2)\). The count by the couple's ordered acceptable-option list is

| Couple options, in preference order | Profiles | No stable matching at \((1,1)\) | Stable at \((1,1)\) |
|---|---:|---:|---:|
| empty | 2,304 | 0 | 2,304 |
| \(((A,B))\) | 2,304 | 128 | 2,176 |
| \(((B,A))\) | 2,304 | 128 | 2,176 |
| \(((A,B),(B,A))\) | 2,304 | 192 | 2,112 |
| \(((B,A),(A,B))\) | 2,304 | 192 | 2,112 |

Thus uniform independent choices of a hospital priority at each hospital, single-doctor preference order at each single, and one of the five couple lists give nonexistence probability \(1/18\). Conditional on a nonempty couple list the probability is \(5/72\). Within the one-option and two-option list strata it is respectively \(1/18\) and \(1/12\). The count in each list stratum is unchanged when the pair of singles' preference orders is held fixed: there are respectively \(0,32,32,48,48\) nonexistence instances among \(576\) hospital-priority pairs for each fixed preference pair.

## Assumptions and scope

There are two labeled hospitals \(A,B\), initially each with one post, one couple consisting of labeled doctors \(a,b\), and two labeled singles \(s,t\). Each single has a strict, complete ranking of \(A,B\) and prefers either hospital to unemployment. Every hospital has a strict, complete priority ranking of all four doctors. The couple ranks a possibly empty ordered subset of the two **distinct-hospital** assignments \((A,B)\), \((B,A)\), and prefers any listed assignment to joint unemployment; it cannot separate and neither member can take an individually assigned post. We do not require sub-completeness of couple preferences. There are exactly five ordered lists, two single-doctor rankings for each single, and \(4!\) hospital-priority orders at each hospital, giving \(5\cdot 2^2\cdot (4!)^2=11{,}520\) profiles.

A matching permits each single to be unemployed or assigned to one hospital, and the couple to be jointly unemployed or assigned to a listed ordered pair. Capacities are upper bounds, not requirements that all posts be occupied. We use the BIS stability definition with single-doctor blocks (S1) and two-distinct-hospital couple blocks (S2). A single blocks with a preferred hospital if it has a vacancy or prefers that single to a current occupant. A couple blocks with a strictly preferred listed pair if each proposed doctor can be admitted at the corresponding hospital by a vacancy, by displacing a worse occupant, or by already occupying the proposed position. Since both listed pairs have different destinations, there are no S3 deviations.

## Proof

**Structural criterion at unit capacity.** If the couple is assigned to a listed pair \(p\), both singles are unemployed. The single-doctor block condition requires the couple member at each hospital to rank strictly above **both** singles there. Call such an option *dominant*. If a dominant chosen option is blocked by a more-preferred couple option, the latter is also dominant: at each hospital, the incoming partner must outrank the incumbent partner, who already outranks both singles. Hence choosing the most-preferred dominant option gives a stable matching. Conversely a couple-assigned stable matching must use a dominant option.

If the couple is unemployed, any S1-stable matching must put the two singles at distinct hospitals: otherwise a free post and an unemployed single cause a block. There are exactly two bijections \((s\mapsto A,t\mapsto B)\) and \((t\mapsto A,s\mapsto B)\). A bijection is S1-stable precisely when neither assigned single can improve by displacing the other at the preferred hospital. It is BIS-stable precisely when no listed couple option places \(a,b\) above the respective incumbents at both hospitals. Therefore a capacity-\((1,1)\) stable matching exists **if and only if** a dominant couple option exists or one of those two bijections passes the single and couple tests.

**Exact finite census.** Enumerate independently all \(24\) priorities at \(A\), all \(24\) at \(B\), both binary singles' preference orders, and the five ordered couple lists. The executable `verify_structural.py` implements the preceding necessary-and-sufficient criterion. It produces the nonexistence column \((0,128,128,192,192)\). It also exhibits witnesses for each nonempty option stratum. Separately, `verify_direct.py` exhausts every feasible couple state and each of the \(3^2\) single states, and tests every S1 and S2 deviation without invoking the structural criterion. Its results agree for all five strata.

**Repair at either hospital.** The direct verifier applies the **same** matching/deviation enumeration to all original-nonexistence profiles under capacities \((2,1)\) and \((1,2)\). The exhaustive result is that every one of the \(640\) has at least one BIS-stable matching under each expanded vector; the counts for repair at only one specified hospital and for failure after both expansions are all zero. The finite loops cover every admissible profile and every matching state, so the verification is an exhaustive finite proof, not random sampling. Its source is a complete standalone certificate in this package.

For an explicit nonexistence witness, take sole couple option \((A,B)\), both singles preferring \(A\succ B\), and hospital priorities \(A:a\succ b\succ s\succ t\) and \(B:a\succ s\succ b\succ t\). If the couple occupies both posts, \(s\) blocks at \(B\); otherwise the only S1-stable singles assignment puts \(s\) at \(A\), \(t\) at \(B\), and the couple blocks. Expanding either hospital admits a BIS-stable outcome.

## Verification

Run `python3 verify_structural.py` and `python3 verify_direct.py` from the same directory. Each script is entirely self-contained and checks the exact five-stratum counts. The direct verifier independently tests both individual one-post expansion locations and asserts all \(11{,}520\) classifications. No external packages or data files are needed. A third, independently implemented C++ enumeration was also run, confirming \(10{,}880\) original-stable and \(640\) one-place-repairable profiles (but the portable two-script certificate suffices for reproduction).

## Relationship to prior work

Wu, Xu and Biró (2026) introduce exact integer-programming formulations for stable matching under capacity changes and show global modification guarantees. Their stated results, inspected in Sections 3–4 and the Appendix, do not give the complete four-doctor, two-hospital labeled-profile census or the location-independent one-post repair assertion established here. The underlying BIS definition is credited to Biró et al. (2011) and discussed by Delorme et al. (2021). Earlier work on stable matching with couples already contains nonexistence examples, which are not claimed as new here. The contribution here is a complete small-market frequency classification coupled with an exact site-robustness statement.

## Limitations

The result is restricted to two hospitals, exactly two single doctors, one couple, strict complete hospital priorities, and distinct-hospital listed couple placements. It does not assert that either-site unit repair holds for arbitrary markets, more singles, same-hospital couple options, or alternative stability definitions. The uniform-profile probabilities are relative to the explicitly specified finite sample space, not an empirical probability for actual medical matching markets. Bibliographic priority remains subject to independently locating equivalent earlier exact finite classifications; independent scientific review has not been performed.

## References

- Z. Wu, G. Xu, P. Biró, *Capacity Modification for Matching with Couples: An Integer Programming and Computational Study*, first posted 2026-10-23, https://arxiv.org/abs/2610.32793.
- D. Marx and I. Schlotter, *Stable assignment with couples: Parameterized complexity and local search*, *Discrete Optimization* 8 (2011), 25–40, https://doi.org/10.1016/j.disopt.2010.07.004.
