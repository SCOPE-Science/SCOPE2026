# Exact latent-ranking recovery from sequentially anchored voting ballots

## Finding

In the sequential anchoring model of Fioravanti and Terzopoulou, recording the order in which alternatives were shown converts a ranked ballot into an **exactly identified rooted-tree partial order** on the voter's intrinsic preferences, even when the acceptability cutoff is unobserved. For every feasible observation, this description gives all and only the compatible strict rankings, the exact number of them, and the precise pairwise comparisons identified. The value of disclosing the presentation order, relative to knowing the ranked ballot alone, is explicit.

Let \(m\ge 3\), let \(\sigma=(\sigma_1,\ldots,\sigma_m)\) be a permutation of the alternatives, and suppose that the ballot retains exactly the alternatives at positions \(1\le r_1<\cdots<r_k\le m\), listed on the ballot as \(\sigma_{r_k}\succ\cdots\succ\sigma_{r_1}\). Let \(\mathcal P(\sigma,r)\) be the set of strict intrinsic rankings compatible with this ballot for **at least one** integer acceptability cutoff between \(1\) and \(m\).

**Exact identified set.** Construct a rooted tree \(T(\sigma,r)\), with better alternatives above worse alternatives, by making each retained alternative \(\sigma_{r_h}\) for \(h<k\) a child of \(\sigma_{r_{h+1}}\). Attach each unretained alternative appearing before \(r_1\) to \(\sigma_{r_1}\). Attach an unretained alternative appearing between two consecutive retained positions to the earlier retained alternative, and each unretained alternative after \(r_k\) to \(\sigma_{r_k}\). The root is \(\sigma_{r_k}\). Then \(\mathcal P(\sigma,r)\) is precisely the set of linear extensions of the ancestor-before-descendant order of this tree.

**Exact ambiguity and identified comparisons.** The number \(L\) of compatible intrinsic strict rankings, and the number \(C\) of unordered pairs whose preference direction is logically forced, satisfy

\[
L=\frac{(m-1)!}{\prod_{h=2}^{k}(r_h-1)},\qquad
C=m-k+\sum_{h=2}^{k}(r_h-1).
\]

Empty products and sums are \(1\) and \(0\). If the presentation order was **not** recorded, but the same top-truncated ballot of length \(k\) was observed, then the corresponding exact values are

\[
L_0=\frac{(m-1)!}{(k-1)!},\qquad
C_0=m-1+\binom{k-1}{2}.
\]

Thus publishing the order reduces the number of compatible rankings by the exact factor

\[
\frac{L_0}{L}=\frac{\prod_{h=2}^{k}(r_h-1)}{(k-1)!},
\]

and reveals exactly \(C-C_0=\sum_{h=2}^{k}(r_h-h)\) additional pairwise comparisons. Both quantities are sharp identities, and the factor is at least one.

For example, with five alternatives presented as \((a,b,c,d,e)\), the ballot \(e\succ b\) corresponds to retained positions \((2,5)\). Without the presentation log, \(24\) intrinsic rankings are compatible. With the log, precisely \(6\) rankings are compatible, and \(7\) of the \(10\) pairwise comparisons are forced; notably, \(b\) must be the voter's second choice.

**Uniform tolerant benchmark.** When all alternatives are acceptable and the intrinsic ranking is uniformly random, the number \(C_m\) of identified comparisons has the exact probability generating function

\[
\mathbb E[z^{C_m}]=z^{m-1}\prod_{j=2}^{m}\left(\frac{j-1}{j}+\frac{z^{j-2}}{j}\right).
\]

In particular, with \(H_m=\sum_{j=1}^{m}1/j\) and \(H_m^{(2)}=\sum_{j=1}^{m}1/j^2\),

\[
\mathbb E C_m=2m-2H_m,\qquad
\operatorname{Var}(C_m)=\frac{m^2-9m}{2}+8H_m-4H_m^{(2)}.
\]

The expected proportion of identifiable comparisons among all \(\binom m2\) pairs tends to zero, with leading term \(4/m\). The normalized count \(C_m/m\) converges in law to \(1+Y\), where \(Y\) has characteristic function

\[
\mathbb E e^{itY}=\exp\left(\int_0^1\frac{e^{itx}-1}{x}\,dx\right).
\]

This last distribution is the classical Dickman record-position limit; the distribution itself is **not** claimed as new. The voting-specific identification and comparison formulas are the substantive finding.

## Assumptions and scope

A strict intrinsic ranking \(p\) of \(m\) distinct alternatives assigns each alternative a distinct rank \(1,\ldots,m\), with smaller rank preferred. An acceptability cutoff \(t\in\{1,\ldots,m\}\) makes exactly the top \(t\) alternatives acceptable. Alternatives appear in the publicly known order \(\sigma\). At each step, an alternative is retained if and only if it is acceptable and it is strictly better than **every** alternative previously displayed. Retention is irrevocable. The submitted ranked ballot orders all retained alternatives according to the intrinsic ranking, rather than the order of presentation.

Only observations whose retained alternatives occur in *increasing* positions but *decreasing* preference rank are feasible. In particular, if a purported ballot ranks any earlier-retained alternative above a later-retained alternative, no strict intrinsic ranking and cutoff can produce it. All exact formulas above apply to nonempty feasible observations and arbitrary, unobserved individual cutoffs. They do not assume voters' reports are truthful outside the specified deterministic anchoring mechanism, nor that multiple voters share preferences or cutoffs.

## Proof

**1. The recorded ballot determines the stated tree constraints.** Every retained alternative is acceptable and is better than all previously seen alternatives. Hence every later retained alternative outranks the preceding retained alternative and, by transitivity, its entire earlier tree subtree. Every alternative before the first retained position must be unacceptable: the first acceptable alternative encountered would necessarily be retained. Accordingly, the first retained alternative outranks them all. At any later nonretained position, the most recent retained alternative is the best alternative yet seen. If the current item is acceptable, failure to retain it means that this previous best outranks it. If the item is unacceptable, the previous best is acceptable and therefore also outranks it. These are exactly the edges described in the tree.

**2. The constraints are sufficient, even without knowing the cutoff.** Fix any strict linear extension \(p\) of the tree. If \(r_1=1\), choose \(t=m\), so all items are acceptable. Each retained node is a new running best, and each nonretained node after it is below the running best, giving precisely the stated ballot. If \(r_1>1\), let \(q\) be the highest-ranked among \(\sigma_1,\ldots,\sigma_{r_1-1}\). The tree places \(\sigma_{r_1}\), and therefore every later retained item, strictly above \(q\). Set \(t=\operatorname{rank}_p(q)-1\), which belongs to \(\{1,\ldots,m\}\). Every earlier item is then unacceptable and every retained item acceptable. At any later nonretained position the previous retained record outranks the current item. It is therefore either unacceptable or not a record. Thus the observation is produced exactly. This constructs a valid cutoff for every tree linear extension, completing equality of the identified sets.

**3. Count the linear extensions.** For a rooted-tree partial order in which parents precede descendants, its number of strict linear extensions is \(m!\) divided by the product of all subtree cardinalities. This follows inductively by interleaving the independent extension orders on the children, giving a multinomial coefficient at every node. Every nonretained leaf has subtree cardinality one. The retained node at position \(r_h\), \(h<k\), has exactly the candidates displayed before \(r_{h+1}\) in its subtree, so its cardinality is \(r_{h+1}-1\). The final retained root has subtree cardinality \(m\). Substitution proves the formula for \(L\).

**4. Identify every forced comparison.** The ancestor relation of \(T\) is forced. Conversely, for incomparable elements of any finite poset, both orientations occur among its linear extensions: adjoining either directed relation cannot create a directed cycle and can be extended to a total order. Hence precisely the ancestor–descendant pairs are identified. At each retained position \(r_h\), that retained alternative dominates all \(r_h-1\) earlier positions. At each later nonretained position, precisely one retained record above it is an ancestor already uncounted at that position. Earlier nonretained positions are counted when the first record occurs. It follows that the total is \(\sum_h(r_h-1)+m-r_1-(k-1)=m-k+\sum_{h=2}^k(r_h-1)\).

**5. Remove the presentation log.** Even without \(\sigma\), the voter's true top is the first entry of the ballot, and the retained alternatives preserve their relative intrinsic order. These are the only restrictions: for any strict ranking with this top and this restricted order, present the retained alternatives from worst to best first, followed by all unretained alternatives, and choose \(t=m\). The desired ballot results. There are \((m-1)!/(k-1)!\) such strict rankings. The top outranks all other candidates and the other \(k-1\) retained candidates are ordered among themselves; this gives \(m-1+\binom{k-1}{2}\) forced pairs. Subtracting the two pair-count expressions yields \(\sum_{h=2}^k(r_h-h)\), and dividing the two extension counts gives the displayed ambiguity reduction.

**6. Derive the tolerant benchmark.** With \(t=m\), position \(1\) is always retained and, for \(j\ge2\), retention means that position \(j\) is a new best among the first \(j\) positions. In a uniformly random strict ranking these record indicators \(I_j\) are mutually independent and \(\Pr(I_j=1)=1/j\). This follows from the independent, uniformly distributed relative insertion ranks of a random permutation. The exact comparison formula becomes \(C_m=m-1+\sum_{j=2}^m(j-2)I_j\). Independence gives the generating function; direct summation gives the stated mean and variance. For the limit, the logarithm of the characteristic function of \(\sum_{j=2}^m jI_j/m\) is

\[
\sum_{j=2}^m\log\left(1+\frac{e^{itj/m}-1}{j}\right)
\longrightarrow\int_0^1\frac{e^{itx}-1}{x}\,dx.
\]

The quadratic logarithm remainders vanish and the first-order terms form a Riemann sum. Meanwhile \(m^{-1}\sum_{j=2}^m 2I_j\to0\) in mean. Lévy's continuity theorem therefore gives the announced translated Dickman limit. The underlying record-position limit also appears in Louchard (2014), and is cited here as prior theory.

## Verification

The accompanying `verify.py` uses exact integer and rational arithmetic to test all strict rankings and all acceptability cutoffs for presentation-order sizes \(m=3,4,5,6,7\). For every one of the \(243\) resulting nonempty retained-position sets, it reconstructs the exact compatible-ranking fiber, checks the tree constraints, compares every logically forced ordered pair with the actual intersection of compatible rankings, and confirms the hook-length count and the exact order-information gain. It also confirms the uniform tolerant mean and variance directly from the entire finite ranking space.

For \(m=3,4,5\), it additionally exhausts **every** strict ranking, cutoff, and presentation order, verifying the complete no-log ranking fibers for \(15\), \(64\), and \(325\) distinct submitted ranked ballots respectively. Reproduce with `python3 verify.py` using Python 3 standard library. These finite checks independently test the derivation on small domains but do not prove the unrestricted theorem; the proof is the six-step argument above.

## Relationship to prior work

Fioravanti and Terzopoulou (2026a) establish the anchoring mechanism for approval ballots and analyze invariance and presentation-order manipulation. Their 2026b ranked-ballot paper proves that anchor-proof ranked voting rules are precisely tops-only rules and explicitly raises order-aware rules as a possible further direction. Those results do **not**, by their statements or their inspected full texts, give the exact fiber of compatible latent strict rankings under an observed order, its rooted-tree representation, its number of linear extensions, or the pairwise-information gain from the order log.

The classical record-indicator independence and the Dickman limit for a sum of record positions were established well before this observation; see Louchard (2014), which is direct prior coverage of that probability ingredient. The novelty claim is confined to the **voting observation model's exact partial-identification structure and associated sharp information counts**, not the combinatorial tree hook formula or the Dickman probability law as general mathematical facts.

## Limitations

The theorem identifies rankings **compatible with some cutoff**, not the actual cutoff or the voter's actual ranking within that set. Distinct compatible rankings may have different cutoffs; knowing a fixed cutoff in advance can shrink the identified set and is not covered by the presented formula. The uniform tolerant benchmark assumes random strict rankings and full acceptability; it does not characterize a general empirical electorate or random preferences with arbitrary cutoff distributions. No outcome-level social-choice robustness guarantee or manipulator-optimal strategy is derived. There is residual historical-priority risk from related literature on inference under sequential choice and partial-order observations, despite the cited comparisons.

## References

1. F. Fioravanti and Z. Terzopoulou (2026), *Anchor-proofness in Voting with Ranked Ballots*, arXiv:2610.10316v1, first public version 2026-10-07. https://arxiv.org/html/2610.10316
2. F. Fioravanti and Z. Terzopoulou (2026), *Anchor-proofness in Voting*, arXiv:2602.04494v3 (first submitted 2026-02-04). https://arxiv.org/html/2602.04494v3
3. G. Louchard (2014), *Sum of positions of records in random permutations: asymptotic analysis*, Online Journal of Analytic Combinatorics 9, paper 1. DOI: 10.61091/ojac-901. https://combinatorialpress.com/article/ojac/vol9/81.pdf
