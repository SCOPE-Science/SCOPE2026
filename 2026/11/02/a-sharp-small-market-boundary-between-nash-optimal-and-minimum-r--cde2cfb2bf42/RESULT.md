# A sharp small-market boundary between Nash-optimal and minimum-regret stable marriage

## Finding

Consider the classical balanced stable-marriage problem with \(n\geq 2\) men and \(n\) women, strict complete preference lists, and zero-based partner ranks. For a stable perfect matching \(M\), let
\[
R(M)=\max_{a}r_a(M(a)),\qquad P(M)=\prod_{a}(n-r_a(M(a))),
\]
where the product ranges over all \(2n\) participants. Minimizing \(R\) is the minimum-regret objective; maximizing \(P\) is equivalent to maximizing Nash social welfare for the positive rank-induced utilities \(n-r\).

**Sharp compatibility theorem.** For every profile with \(n=2\) or \(n=3\), every Nash-welfare-maximizing stable matching also minimizes regret:
\[
\underset{M\text{ stable}}{\operatorname{argmax}}\,P(M)
\ \subseteq\ 
\underset{M\text{ stable}}{\operatorname{argmin}}\,R(M).
\]
For \(n=3\), these two nonempty optimizer sets are equal for exactly \(39{,}672\) of the \(46{,}656\) labeled strict profiles and exhibit strict containment for the other \(6{,}984\). More strongly, at these market sizes, any two stable matchings with different regret scores have strictly oppositely ordered Nash products.

The inclusion fails sharply at \(n=4\): there are strict complete preferences with a unique Nash optimum and a *different* unique minimum-regret optimum. For every \(n\geq4\), there exist such profiles with disjoint optimizer sets.

## Assumptions and scope

An instance consists of labeled men \(m_0,\ldots,m_{n-1}\) and women \(w_0,\ldots,w_{n-1}\). Every agent strictly orders all members of the other side and prefers any match to being unmatched. A perfect matching is represented by the vector \((j_0,\ldots,j_{n-1})\), meaning that \(m_i\) is paired with \(w_{j_i}\). It is *stable* if no unmatched man–woman pair both strictly prefer one another to their assigned partners. The zero-based rank \(r_a(M(a))\) lies in \(\{0,\ldots,n-1\}\); the utility \(n-r_a(M(a))\) is consequently a positive integer. The extrema are over **stable** perfect matchings only; ties are treated as full sets of optimal matchings rather than resolved by a preference rule. No probability distribution over preferences is assumed for the universal assertion. In the reported labeled-profile census every agent independently ranges over all \(n!\) strict orders, yielding \((n!)^{2n}\) profiles.

## Proof

**Exhaustive finite lemma for the sharp lower side.** The accompanying standalone `CHECK.py` explicitly enumerates each of the \((n!)^{2n}\) labeled strict preference profiles for \(n=2\) and \(n=3\). For each profile it enumerates every one of the \(n!\) perfect matchings and declares a matching stable exactly when none of the \(n(n-1)\) off-matching man–woman pairs satisfy both strict blocking inequalities. It computes all participants' zero-based ranks directly from the lists, takes their maximum to compute \(R\), and multiplies their positive integer rank-induced utilities to compute \(P\). It then forms both *complete* optimizer sets, compares them as finite sets of labeled perfect matchings, and also checks every unordered pair of stable matchings with different regret scores. Thus the checked finite enumeration exhausts both the input universe and the permitted outcome universe; it is not a sample or a bound extrapolated from small data. All operations are exact integers.

For \(n=2\), the \(16\) profiles have identical Nash and regret optimizer sets. For \(n=3\), the \(46{,}656\) profiles divide into \(39{,}672\) equality cases and \(6{,}984\) strict Nash-set-containment cases; there are no other set relations. In all \(3{,}504\) stable-outcome comparisons in which two stable matchings have different regret, the outcome with smaller maximum rank has strictly larger \(P\). These exhaustive facts establish the stated universal inclusion and the labeled census.

**A four-by-four separating instance.** Let each row below list opposite-side labels from best to worst; labels are zero-based. The four men's lists are
\[
(3,2,0,1),\quad(1,2,0,3),\quad(2,0,1,3),\quad(3,0,2,1).
\]
The four women's lists are
\[
(0,3,1,2),\quad(2,1,3,0),\quad(0,3,2,1),\quad(1,3,0,2).
\]
Directly testing all \(4!=24\) perfect matchings against the blocking-pair definition shows that the complete set of stable matchings is precisely the following table. Each vector gives the women assigned in men's label order.

| Stable matching | Worst rank \(R\) | Nash product \(P\) | Total partner rank |
|:--|--:|--:|--:|
| \((2,0,1,3)\) | \(2\) | \(4608\) | \(8\) |
| \((2,1,0,3)\) | \(3\) | \(5184\) | \(7\) |
| \((2,3,1,0)\) | \(3\) | \(3456\) | \(8\) |

The first is the unique minimum-regret matching, whereas the second is the unique Nash-optimal matching. In particular, there is no matching that optimizes both criteria, and the \(n=4\) boundary is attained.

**Preserving separation for every larger market.** Take the displayed instance and append \(k=n-4\geq 1\) additional men and women, paired by corresponding new labels. Each new agent ranks their corresponding new opposite-side agent *first*, followed by all other opposite-side agents in any strict order. Every old agent ranks **all** new opposite-side agents above all four old opposite-side agents, preserving the previous internal order of the four old labels. Every stable matching must contain each new mutual-top-choice pair: if either partner were assigned elsewhere, that pair would block. Consequently the stable matchings of the enlarged profile are exactly the old stable matchings extended by all new pairs: no new agent can participate in a blocking pair when assigned their first choice, and all old-to-old comparisons retain their original order.

For every old participant, an original partner of zero-based rank \(r\) now has rank \(r+k\), and their enlarged-market utility satisfies \(n-(r+k)=4-r\), exactly the original utility. Each of the \(2k\) new participants has rank zero and utility \(n\). Thus the enlarged Nash product is the old Nash product multiplied by the same positive constant \(n^{2k}\). The enlarged maximum rank is the old maximum rank plus \(k\), because each original stable matching has at least one old agent of positive rank and all new agents have rank zero. Hence both unique, distinct optima are preserved for every \(n\geq 5\), completing the proof.

## Verification

The self-contained standard-library program `CHECK.py` is a fully reproducible exhaustive finite proof/certificate and separately checks the padded construction at \(n=5,6\). Run `python3 CHECK.py` in the same directory as this document. A successful run prints:

`VERIFY_OK n2=16 n3=46656 equal=39672 proper=6984 cross-regret-pairs=3504 regret-subset-egal=1200 n4-stable=3 padding=5,6`

The program checks every profile and matching at \(n\leq3\), checks all stable outcomes for the four-pair witness, asserts the exact optimum-set separation, and verifies rank/product scaling at the first two padded sizes. The assertion-based exhaustive algorithm, together with the elementary padding proof, establishes the complete finite/infinite claim; finitely many padded tests alone would not establish the unrestricted extension. Reproduction assumes ordinary Python 3 with its standard library and exact integer semantics.

## Relationship to prior work

Desai, Rasheed M, Ghalme, and Gujar (2026) formulate rank-induced Nash social welfare and give an algorithm optimizing it subject to stable marriage; they compare it with minimum-regret matching, including a five-pair illustrative separation of traditional fairness measures. Their model uses precisely the positive rank utilities and zero-based ranks adopted here. Their algorithm and comparative experiments do not themselves assert the sharp universal two-/three-pair Nash-versus-regret inclusion or the \(46{,}656\)-profile optimizer-set classification. The minimum-regret objective and its computation are classical, notably in Gusfield (1987).

A separate small-market result establishes a relation between Nash-optimal **and egalitarian sum-of-ranks** stable matchings for three pairs. The present assertion concerns *maximum individual rank*, a distinct, nonadditive objective. It is not implied by that result even in conjunction with known nesting relations between egalitarian and minimum-regret optimizer sets: when minimum-regret optima form a proper subset of egalitarian optima, knowing only that Nash optima are egalitarian leaves their minimum-regret status unresolved. Related exact small-market comparisons of rank-maximality, sex equality, egalitarianism, and minimum regret similarly do not provide this Nash-product inclusion. This statement is a finite exact characterization of the interaction of two established criteria, not a new algorithm for computing either criterion.

## Limitations

The equality/strict-containment proportions are exact for **labeled strict complete** markets with three agents per side; they should not be interpreted as rates under correlated preference distributions or as counts up to isomorphism. The stronger cross-regret monotonicity is asserted only for \(n=2,3\). The existence construction for \(n\geq4\) does not classify all larger profiles. Changing the utility normalization, admitting ties, incomplete lists, transfers, or another stability concept can change Nash-optimal selections. The finite exhaustive certificate is machine-checkable but is not a formal proof-assistant development, and the literature comparison cannot exclude unpublished or unindexed equivalent results. No independent scientific audit has been performed.

## References

1. Parth Desai, Rasheed M, Ganesh Ghalme, and Sujit Gujar, *Fair Stable Matching: A Nash Social Welfare Approach* (2026), arXiv:2609.02354v1, first publicly submitted 2 September 2026. https://arxiv.org/html/2609.02354v1
2. Dan Gusfield, *Three Fast Algorithms for Four Problems in Stable Marriage*, SIAM Journal on Computing 16 (1987), DOI:10.1137/0216010.
3. Robert W. Irving, Paul Leather, and Dan Gusfield, *An Efficient Algorithm for the “Optimal” Stable Marriage*, Journal of the ACM 34 (1987), 532–543, DOI:10.1145/28869.28871. This work addresses the additive egalitarian criterion rather than the present Nash-versus-regret relation.
4. David Gale and Lloyd S. Shapley, *College Admissions and the Stability of Marriage*, American Mathematical Monthly 69 (1962), 9–15; DOI:10.2307/2312726.
