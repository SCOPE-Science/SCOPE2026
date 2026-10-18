# Sharp cross-length dependence law for burst-deletion balls

## Finding

For a word \(w=w_1\cdots w_n\) over an alphabet of size \(q\ge 2\), let \(\mathcal D_b(w)\) be the **set of distinct** length-\(n-b\) words obtained by deleting exactly \(b\) consecutive positions, and put \(B_b(w)=|\mathcal D_b(w)|\). Choose \(W\) uniformly from all \(q^n\) words, so its letters are independent and uniform. For \(1\le b<n\), write

\[
\mu_b=\mathbb E B_b(W)=1+\frac{(n-b)(q-1)}q.
\]

**Cross-length dependence theorem.** For every \(q\ge2\), \(n\ge3\), and distinct burst lengths \(1\le a<b<n\), the ball sizes \(B_a(W)\) and \(B_b(W)\) always have zero covariance, but they are statistically independent **if and only if**

\[
 n\le a+b-\gcd(a,b).
\]

There is an exact dependence certificate even when their covariance vanishes. With \(g=\gcd(a,b)\),

\[
\frac{\Pr(B_a(W)=1,\ B_b(W)=1)}{\Pr(B_a(W)=1)\Pr(B_b(W)=1)}
=q^{\max\{0,n-a-b+g\}}.
\]

At the first dependent length \(n=a+b-g+1\), the simultaneous minimum-ball event is therefore exactly \(q\) times as likely as a product-of-marginals calculation predicts.

For any **three distinct** burst lengths \(1\le a<b<c<n\), the first nonzero mixed centered moment has an additive-resonance rule:

\[
\mathbb E\!\left[(B_a-\mu_a)(B_b-\mu_b)(B_c-\mu_c)\right]
=\begin{cases}
-\dfrac{2(n-c)(q-1)}{q^3},&c=a+b,\\[3pt]
0,&c\ne a+b.
\end{cases}
\]

These assertions concern distinct deletion **outputs**, not the multiplicities of deletion positions producing the same output.

## Assumptions and scope

The alphabet is an arbitrary finite set of cardinality \(q\); a finite-field structure is not assumed. All word positions are linear (not circular). Each burst deletes **exactly** the indicated number of consecutive symbols. The integer \(n\) satisfies \(n>b\) for two lengths and \(n>c\) for three lengths. Random words have independent uniform symbols. Independence refers to the two full integer-valued random variables, not merely to their means, covariances, or particular events.

## Proof

**1. Deletion-ball identity.** Index deletion starts by \(i=0,\ldots,n-b\), and denote by \(f_i\) the output after deleting positions \(i+1,\ldots,i+b\). For \(i<j\), cancellation of their common initial and terminal segments gives

\[
 f_i=f_j\quad\Longleftrightarrow\quad
 w_{i+1}\cdots w_j=w_{i+b+1}\cdots w_{j+b}.
\]

Thus, \(f_i=f_j\) holds precisely when \(w_t=w_{t+b}\) for every \(i<t\le j\). In particular, equal outputs occupy contiguous ranges of deletion starts. Their number is exactly

\[
 B_b(w)=1+\sum_{i=1}^{n-b}\mathbf 1\{w_i\ne w_{i+b}\}. \tag{1}
\]

This known single-length identity is the starting point, not the novelty claim. Set \(p=(q-1)/q\) and \(Y_{ij}=\mathbf 1\{W_i\ne W_j\}-p\). If two distinct unordered edges are disjoint, their indicators are independent. If they share exactly one vertex, conditioning on that vertex again gives independent Bernoulli variables of parameter \(p\). Hence \(\mathbb E[Y_{ij}Y_{kl}]=0\) for any distinct edges. Since the edges at distances \(a\) and \(b\) never coincide, (1) proves \(\operatorname{Cov}(B_a,B_b)=0\) and the stated values of \(\mu_b\).

**2. The exact graph-cycle threshold.** Let \(G_{a,b}(n)\) be the simple graph on vertices \(1,\ldots,n\) whose edges have absolute length \(a\) or \(b\). A forest has jointly independent mismatch indicators: orient its edges away from a root in each component and expose the letters root-first. Each successive child's match/mismatch decision is an independent Bernoulli variable of parameter \(p\), even conditional on everything previously exposed.

Put \(L=a+b\) and \(g=\gcd(a,b)\). On \(1,\ldots,L\), draw directed edges \(i\mapsto i+a\pmod L\), using representatives \(1,\ldots,L\). Ignoring orientation gives exactly \(G_{a,b}(L)\): an edge of ordinary length \(a\) when no wrap occurs and one of ordinary length \(b\) otherwise. Because \(a\ne b\), its connected components are \(g\) genuine cycles, each of length \(L/g\ge3\). These are the residue classes modulo \(g\). For \(n\le L\), the graph \(G_{a,b}(n)\) is the induced subgraph of this disjoint-cycle graph on vertices \(1,\ldots,n\). The earliest residue-class cycle to be wholly included has last vertex \(L-g+1\). Accordingly the graph is a forest for \(n\le L-g\), and contains a cycle for \(n\ge L-g+1\); the latter remains true for \(n>L\).

Furthermore its cycle rank, \(\beta=|E|-|V|+\kappa\) where \(\kappa\) is the number of connected components, satisfies

\[
\beta(G_{a,b}(n))=\max\{0,n-L+g\}.\tag{2}
\]

Indeed it is zero in the forest regime. At \(n=L-g+1\), the first completed class contributes one cycle and each other class is a path, so \(\kappa=g\). Thereafter every new vertex has an edge to its existing residue-class component; thus \(\kappa=g\), while the total number of edges is \((n-a)+(n-b)=2n-L\), giving \(\beta=n-L+g\). This also covers the remaining values \(n\le L\) directly by the partially filled cycles.

**3. Necessity of the independence threshold.** The minimum event \(B_b=1\) holds if and only if all distance-\(b\) edges have equal endpoint labels. The distance-\(b\) graph consists of \(b\) paths; hence \(\Pr(B_b=1)=q^{b-n}\). Jointly, \(B_a=B_b=1\) requires equal letters throughout each component of \(G_{a,b}(n)\), so

\[
\Pr(B_a=B_b=1)=q^{\kappa-n}.
\]

Dividing by the two marginal probabilities and using \(\kappa=n-(2n-L)+\beta=L-n+\beta\) proves the displayed ratio \(q^\beta\). When the graph contains a cycle, this ratio is strictly greater than one because \(q\ge2\), ruling out independence. When it is a forest, all the underlying edge indicators—and hence their sums \(B_a,B_b\)—are independent. This establishes both directions and the sharp cutoff.

**4. Additive third moment.** Expand the centered product using (1). For three *distinct* unordered edges, \(\mathbb E[Y_{e_1}Y_{e_2}Y_{e_3}]=0\) whenever their graph is a forest: condition on the letter at a leaf, whose sole centered incident-edge indicator has conditional expectation zero. The only possible three-edge cycle in a simple graph is a triangle. Three edge lengths \(a<b<c\) can form a triangle along the line precisely when \(c=a+b\). For each left endpoint \(i=1,\ldots,n-c\), its two possible middle vertices are \(i+a\) and \(i+b\); they are distinct. Hence there are exactly \(2(n-c)\) contributing triangles.

On one triangle, the probability that all three edges join unequal letters is \((q-1)(q-2)/q^2\). Distinct-edge indicators are pairwise independent, so their centered triple expectation is

\[
\frac{(q-1)(q-2)}{q^2}-\left(\frac{q-1}{q}\right)^3
=-\frac{q-1}{q^3}.
\]

Multiplication by the exact triangle count proves the third-moment formula, including \(q=2\) and every admissible boundary value of \(n\).

## Verification

The included independent finite checker `checker.py` explicitly constructs all distinct burst-deletion output words, instead of implementing the graph formula as its sole oracle. It tests every alphabet word for \(q=2\), \(2\le n\le9\); \(q=3\), \(2\le n\le7\); and \(q=4\), \(2\le n\le6\), comprising 19 complete alphabet/length cases. In every case it checks (1), every one-length count against the known binomial law, every pair's exact zero covariance, the full-distribution independence cutoff, and the exact joint-minimum count. Every triple of distinct burst lengths is checked against the stated centered-moment formula using exact rational arithmetic. Execution of `python3 checker.py` from the extracted package produced `ALL_BURST_JOINT_STATISTICS_PASSED 19 parameter_cases`.

The computations are finite corroboration; the proof above supplies the claims for all integers in scope.

## Relationship to prior work

Schoeny, Wachter-Zeh, Gabrys and Yaakobi [1] state Levenshtein's single-burst-ball identity in their equation (2) and derive the binary **one-length** ball-size distribution in Appendix A, Lemma 8. Those are acknowledged prior results. The single-length marginal cannot by itself determine independence of ball sizes at two different burst lengths, their sharp arithmetic threshold, or a mixed third moment. Song and Cai [2] study \(q\)-ary deletion- and burst-correcting code constructions; their pertinent discussion supplies the channel setting but not the cross-length theorem. Pseudorandom-sequence correlation measures [3] study worst-case shifted products, not this finite uniform-word distribution of exact burst-ball cardinalities.

The present theorem instead identifies precisely when two different burst lengths yield independent ball sizes, supplies an exact dependence ratio past the threshold, and characterizes the first additive three-way interaction despite zero pairwise covariance. It does **not** claim novelty for the one-length deletion-ball formula, marginal binomial counts, or general forest independence in random colorings.

## Limitations

The random-word law assumes independent *uniform* symbols; fixed-composition or nonuniform models can have different covariances. Burst lengths are distinct in the independence and third-moment assertions. Only linear words and exact consecutive deletion bursts are treated. No conclusion about correction-code capacity, channel decoding performance, or arbitrary simultaneous deletion patterns follows from these ball-size moment formulas. Possible related results in unindexed literature on lag mismatches, autocorrelation, and graph-dependent random colorings remain an originality risk. Independent audit has not been performed.

## References

[1] C. Schoeny, A. Wachter-Zeh, R. Gabrys, and E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820v2 (2016), especially §IV equation (2) and Appendix A Lemma 8. https://arxiv.org/abs/1602.06820

[2] W. Song and K. Cai, *Non-binary Two-Deletion Correcting Codes and Burst-Deletion Correcting Codes*, arXiv:2210.14006v1 (first public 2022-10-25), especially §I–II and burst-code construction sections. https://arxiv.org/abs/2210.14006

[3] A. Winterhof, *Pseudorandom binary sequences: quality measures and number-theoretic constructions*, arXiv:2305.11486 (2023), §4 on higher-order correlation measures. https://arxiv.org/abs/2305.11486
