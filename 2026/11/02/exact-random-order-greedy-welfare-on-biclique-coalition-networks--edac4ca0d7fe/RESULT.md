# Exact random-order greedy welfare on biclique coalition networks

## Finding

Let \(a,b\geq1\) be integers. In the complete bipartite additively separable hedonic game with parts of sizes \(a\) and \(b\), every cross-part pair has valuation \(1\) in each direction and every within-part pair has valuation \(0\). Agents arrive in a uniformly random permutation. On each arrival the greedy algorithm chooses a coalition giving the largest *strictly positive* increase in utilitarian social welfare, resolving equal positive increases in favor of the earliest-created coalition, and starts a singleton if no increase is positive.

Writing \(W\) for final social welfare and \(W^*=2ab\) for optimum, put \(Q=W/W^*\). Let \(N=a+b\) and \((x)_{\underline r}=x(x-1)\cdots(x-r+1)\). The full law of \(Q\) is given by the following two contributions, whose probabilities are to be added when values coincide: for each \(1\le r\le a\),

\[
\Pr\!\left(Q=1-\frac{r-1}{a},\ \text{first run is from the }a\text{-part}\right)
 =\frac{(a)_{\underline r}\,b}{(N)_{\underline{r+1}}},
\]

and, for each \(1\le r\le b\),

\[
\Pr\!\left(Q=1-\frac{r-1}{b},\ \text{first run is from the }b\text{-part}\right)
 =\frac{(b)_{\underline r}\,a}{(N)_{\underline{r+1}}}.
\]

In particular,

\[
\boxed{\mathbb E Q=1-\frac1{a+1}-\frac1{b+1}+\frac2{a+b}.}
\]

For each fixed total population \(N\), this expectation is minimal precisely for the star splits \(\{a,b\}=\{1,N-1\}\), with value \(\frac12+\frac1N\), and maximal for the balanced splits \(\{a,b\}=\{\lfloor N/2\rfloor,\lceil N/2\rceil\}\).

If \(a\ge1\) stays fixed and \(b\to\infty\), then \(Q\) converges in distribution to the \(\operatorname{Beta}(a,1)\) law, with cumulative distribution function \(t^a\) on \(0\le t\le1\). Thus star instances have a uniform limiting welfare fraction, not a concentrated half-welfare outcome. If both \(a,b\to\infty\), then \(Q\to1\) in mean and probability.

## Assumptions and scope

All vertices of the two parts arrive, with independent uniform ordering induced by one uniformly random permutation of the \(N\) distinct agents. The algorithm may append the arriving agent to exactly one existing coalition, without merging or rearranging existing coalitions. Social welfare is the sum of individual utilities, hence twice the number of cross-part edges internal to coalitions. No coalition-size constraint is imposed. An edge from one part to the other has constant positive symmetric valuation \(1\), and all within-part valuations are \(0\). The specific tie-breaking rule (earliest-created coalition) is **essential**; arbitrary resolutions of ties can give different welfare on some arrival orders. The algorithm creates a singleton whenever every joining choice has zero gain. The guarantee concerns this precise random-order greedy algorithm, not all online algorithms or other utilities.

## Proof

**Structure of the outcome.** Consider any arrival sequence. Its first \(r\ge1\) agents all belong to one side, say the side of size \(a\). They form \(r\) singleton coalitions because all mutual valuations vanish. The next agent belongs to the opposite part, and it has strictly positive welfare gain \(2\) from joining any of these singletons. Under earliest-created tie-breaking it joins the first singleton; call that coalition \(C\). The coalition \(C\) is mixed and is the earliest-created coalition. Every later agent belonging to the original side has a positive gain from joining \(C\), whereas it obtains zero from joining any remaining singleton of its own side. Every later agent from the opposite side has gain at least \(2\) from joining \(C\), and any remaining original-side singleton gives gain exactly \(2\); the earliest-created rule again selects \(C\). Induction shows that every subsequent arrival enters \(C\). The other \(r-1\) early agents remain singletons forever.

Consequently, if the initial monochromatic run comes from the \(a\)-part, the final mixed coalition has \(a-r+1\) agents from that part and all \(b\) agents from the other part. Thus \(W=2(a-r+1)b\) and \(Q=1-(r-1)/a\). Interchanging \(a,b\) gives the second case. The offline grand coalition contains all \(ab\) positive cross edges and attains \(W^*=2ab\), an upper bound for every partition, so this normalization is exact.

**Complete distribution.** For \(1\le r\le a\), the probability that the first \(r\) arrivals belong to the \(a\)-part and the next belongs to the \(b\)-part is

\[
\frac{a}{N}\frac{a-1}{N-1}\cdots\frac{a-r+1}{N-r+1}\frac{b}{N-r}
=\frac{(a)_{\underline r}b}{(N)_{\underline{r+1}}}.
\]

The analogous expression holds for the other side. These are disjoint events and exhaust all arrival orders, proving the law, including coincident values arising from both sides.

**Mean.** Conditional on the first agent belonging to the \(a\)-part, the number \(r-1\) of additional \(a\)-agents before the first \(b\)-agent has mean \((a-1)/(b+1)\). One direct proof places the \(b\) opposite-side agents as separators in the random order of the remaining \(a+b-1\) agents: each of the remaining \(a-1\) agents has probability \(1/(b+1)\) of lying in the initial gap. Since the first agent is in the \(a\)-part with probability \(a/N\), its contribution to the expected *relative* welfare deficit is

\[
\frac aN\cdot\frac{a-1}{b+1}\cdot\frac1a
=\frac{a-1}{N(b+1)}.
\]

Adding the symmetric contribution gives

\[
\mathbb E(1-Q)=\frac{a-1}{N(b+1)}+\frac{b-1}{N(a+1)}
=\frac1{a+1}+\frac1{b+1}-\frac2N.
\]

**Extrema for fixed total size.** With \(b=N-a\), the sum \(1/(a+1)+1/(N-a+1)\) is strictly convex and symmetric as a function of real \(a\in[1,N-1]\). Therefore it is largest at the endpoints and smallest at the integer(s) nearest \(N/2\). Negating this sum yields precisely the asserted extremal expectation. At the endpoints,

\[
\mathbb E Q=1-\frac12-\frac1N+\frac2N=\frac12+\frac1N.
\]

**Scaling laws.** Fix \(a\). As \(b\to\infty\), the probability the first agent belongs to the \(a\)-part tends to zero. The \(a\) arrival ranks of that part, divided by \(N\), converge jointly to \(a\) independent uniform \([0,1]\) random variables (their unordered sample positions become uniform). The first run then consists of the \(b\)-agents preceding the earliest \(a\)-agent. Consequently the welfare deficit tends to the minimum of \(a\) independent uniforms, whose survival function is \((1-t)^a\); hence the welfare fraction tends to \(\operatorname{Beta}(a,1)\). Conversely, if both part sizes diverge, the exact nonnegative mean deficit is \(1/(a+1)+1/(b+1)-2/(a+b)\to0\); since \(0\le Q\le1\), this implies convergence in \(L^1\) and in probability.

## Verification

The standalone Python program `CHECK.py` enumerates all part-color arrival words for \(1\le a,b\le8\) with \(a+b\le12\), and every labeled arrival permutation for \(1\le a,b\le8\) with \(a+b\le8\). It simulates coalition choices directly (earliest-created tie-breaking) and compares the final internal-edge count with the initial-run formula. Independently, exact rational probability mass functions and means are compared to the displayed expressions for all \(1\le a,b\le8\), and star distributions are checked through \(b=24\). The completed run returned 7,418 part-color words and 316,646 fully labeled permutations, with no mismatches. The program requires only the Python standard library. The enumerations confirm finite cases but do not replace the all-parameter proof above.

For example, at \(a=3,b=4\), the possible normalized welfare values, in increasing order, are \(1/4,1/3,1/2,2/3,3/4,1\), with respective probabilities \(1/35,1/35,3/35,4/35,6/35,4/7\). Their mean is \(117/140\).

## Relationship to prior work

Bullinger and Romen, *Online Coalition Formation under Random Arrival or Coalition Dissolution* (arXiv:2306.16965, first public preprint 29 June 2023; ESA 2023), define the online additively separable coalition model and prove general worst-case random-arrival approximation orders. Their published general bounds do not specify the exact distribution or topology-dependent biclique formulas above. The 2025 revision's model and algorithm definitions in sections 3 and 5 and the conclusions, references and appendix were compared. Flammini, Monaco, Moscardelli, Shalom and Zaks, *On the Online Coalition Structure Generation Problem* (JAIR 72, 2021), treat irrevocable online coalition generation and weight restrictions under adversarial arrival; their theorems do not provide this uniform-random-order biclique law. Matching results do not imply the claim because the output coalition here can have more than two members.

The exact probability distribution and asymptotic \(\operatorname{Beta}(a,1)\) law are not consequences of a generic \(\Theta\)-order competitive-ratio bound. Literature and indexed-result searches did not locate a mathematically equivalent statement, but absence from those searches is not a proof of publication priority.

## Limitations

This is a theorem for **uniform unit positive cross-part weights** and a **specified tie-break**. Weighted or irregular bipartite graphs, arbitrary tie-breaking, strategic self-interested arrival rules, matching-only algorithms, and non-uniform arrival distributions need not obey the formulas. The proof does not assert optimality of greedy among arbitrary online rules. The limit for one fixed part holds in distribution, not in probability to a constant. Priority relative to unindexed or unpublished literature remains uncertain, and no independent audit has been performed.

## References

1. M. Bullinger and R. Romen, *Online Coalition Formation under Random Arrival or Coalition Dissolution*, arXiv:2306.16965, initial submission 29 June 2023, https://arxiv.org/abs/2306.16965 ; ESA 2023 article, DOI:10.4230/LIPIcs.ESA.2023.27, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESA.2023.27 .
2. M. Flammini, G. Monaco, L. Moscardelli, M. Shalom and S. Zaks, *On the Online Coalition Structure Generation Problem*, Journal of Artificial Intelligence Research 72 (2021), 1215–1250, DOI:10.1613/JAIR.1.12989, https://jair.org/index.php/jair/article/download/12989/26746 .
