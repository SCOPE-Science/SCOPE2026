# A Poisson window and reentrant validity for the modal density axiom on sparse random frames

## Finding

Let \(D_n\) be the loop-free directed random graph on \([n]\), with every ordered arc \(u\to v\) for \(u\ne v\) chosen independently with probability \(p_n\). Write \(X_n\) for the number of present arcs lacking a directed two-step alternative route between the same endpoints. The standard modal density scheme \(\Box\Box q\to\Box q\) is valid on \(D_n\) under every propositional valuation precisely when \(X_n=0\).

For every fixed real \(t\), suppose that for all sufficiently large \(n\)
\[
n p_n^2=\frac32\log n+\frac12\log\log n+t.
\]
Then
\[
X_n\ \xrightarrow{\mathrm d}\ \operatorname{Poisson}\!\left(\sqrt{\frac32}\,e^{-t}\right),
\qquad
\Pr\bigl(D_n\models\Box\Box q\to\Box q\bigr)
\longrightarrow \exp\!\left(-\sqrt{\frac32}\,e^{-t}\right).
\]
If the left-hand side exceeds the right-hand centering by a quantity tending to positive infinity, the validity probability tends to one. This is an **upper, nonmonotone** transition: the density scheme also holds with high probability at \(p_n=n^{-3}\), but fails with high probability at \(p_n=n^{-1}\).

## Assumptions and scope

All graphs are directed, labelled, simple in the sense of no self-loops, and allow both opposing arcs. For every unordered pair of different vertices, its two possible orientations are sampled independently. The threshold assertion is asymptotic as \(n\to\infty\). Its modal statement concerns frame validity (all valuations at all worlds), not truth at a fixed assignment. The proposition letter \(q\) is distinct from the edge-density parameter \(p_n\). No independence or monotonicity of the validity events as \(p_n\) varies is assumed.

Write \(R\) for the directed edge relation and \(R^2\) for relational composition. For a single arc \((u,v)\in R\), a *witness* is a vertex \(z\) with \((u,z),(z,v)\in R\). Since loops are excluded, witnesses are necessarily different from both endpoints. The number of arcs without witnesses is \(X_n\).

## Proof

**1. Frame correspondence.** If \(R\subseteq R^2\), any world verifying \(\Box\Box q\) also verifies \(\Box q\), for every valuation. Conversely, if \((u,v)\in R\setminus R^2\), interpret \(q\) as true exactly at all points in \(R^2[u]\). At \(u\) the premise holds while \(\Box q\) fails at \(v\). Thus frame validity is exactly \(R\subseteq R^2\), equivalently \(X_n=0\).

**2. Exact first moment and scaling.** For distinct \(u,v\), the possible witness events indexed by \(z\notin\{u,v\}\) use disjoint pairs of independent arcs. The original arc is independent of all these pairs. Hence
\[
\mathbb E X_n=n(n-1)p_n(1-p_n^2)^{n-2}.
\]
Under the displayed scaling, \(p_n\sim\sqrt{(3/2)\log n/n}\), \(n p_n^4\to0\), and
\[
\mathbb E X_n\longrightarrow \lambda_t:=\sqrt{\frac32}\,e^{-t}.
\]

**3. Factorial moments.** Fix a positive integer \(r\), and consider \(r\) ordered, pairwise distinct proposed offending arcs \(a_i\to b_i\). Let \(S\) denote their endpoint union, with \(|S|\le2r\). Requiring the \(r\) arcs has probability \(p_n^r\). Conditional on those arcs, for each \(z\notin S\) let \(A_i(z)\) be the event that both \(a_i\to z\) and \(z\to b_i\) occur. Each has probability \(p_n^2\). For distinct indices \(i,j\), their two required-arc pairs have at least three distinct directed edges, so
\[
\Pr(A_i(z)\cap A_j(z))\le p_n^3.
\]
Bonferroni therefore bounds the probability of seeing no witness at the external vertex by
\[
\Pr\Bigl(\bigcap_{i=1}^{r}A_i(z)^c\Bigr)
\le 1-rp_n^2+\binom r2p_n^3.
\]
The underlying edge sets are disjoint for different external vertices \(z\), so independence across those vertices gives, uniformly over all distinct proposed arcs,
\[
\Pr(\text{all proposed arcs are unwitnessed})
\le p_n^r\exp\bigl(-r n p_n^2+O_r(p_n^2+n p_n^3)\bigr).
\]
There are at most \(O_r(n^{2r-1})\) ordered configurations whose \(2r\) endpoints are not all distinct, and \(n p_n^3\to0\). Their total contribution to the \(r\)-th factorial moment is bounded by
\[
O_r(n^{2r-1}p_n^r e^{-rn p_n^2+o(1)})=o(1).
\]

For the \((n)_{2r}\) configurations with pairwise disjoint endpoints, the forbidden witness events at each external vertex use exactly \(2r\) distinct directed edges, and hence are independent. Their joint absence has probability \((1-p_n^2)^r\). Paths through one of the \(2r\) internal endpoints have probability \(O_r(p_n)\) of occurring, even after conditioning on the proposed arcs; no such path can consist of two conditioned edges because those edges form a directed matching. These internal-edge events are independent of all external-edge events. Consequently, uniformly over disjoint-endpoint configurations,
\[
\Pr(\text{all proposed arcs are unwitnessed})
=p_n^r(1-p_n^2)^{r(n-2r)}(1+o(1)).
\]
Summing these probabilities gives
\[
\mathbb E[(X_n)_r]
=(n)_{2r}p_n^r(1-p_n^2)^{r(n-2r)}(1+o(1))+o(1)
\longrightarrow \lambda_t^r,
\]
where \((X_n)_r\) is the falling factorial. Convergence of all fixed factorial moments to those of a Poisson variable implies \(X_n\xrightarrow{\mathrm d}\operatorname{Poisson}(\lambda_t)\), proving the displayed probability limit.

**4. Upper regime and nonmonotonicity.** If \(n p_n^2-\frac32\log n-\frac12\log\log n\to+\infty\), the first-moment formula and the fact that \(p\mapsto p e^{-(n-2)p^2}\) is decreasing once \(p\ge 1/\sqrt{2(n-2)}\) show \(\mathbb EX_n\to0\). Markov's inequality proves validity with high probability. At \(p_n=n^{-3}\), the expected total number of arcs is at most \(n^2p_n=n^{-1}\), so the relation is empty with high probability and is vacuously dense. At \(p_n=n^{-1}\), the total arc count is \(n+o_{\Pr}(n)\), whereas the expected number of *supported* arcs is at most \(n(n-1)(n-2)p_n^3=O(1)\). Thus at least one unsupported arc exists with high probability, and the frame axiom fails.

## Verification

The accompanying standalone `verify_random_density.py` enumerates every loop-free directed relation on \(n=2,3,4\) labelled points. For every relation it independently checks all truth assignments for \(q\), compares direct formula validity with the absence of unsupported arcs, and checks the exact \(p=1/2\) expected unsupported-arc count. The numbers of tested relations are respectively \(4\), \(64\), and \(4096\), and the counts of valid frames are \(1\), \(2\), and \(88\). All checks passed. These finite tests do not prove the asymptotic Poisson law; the factorial-moment argument does.

Run the checker with `python3 verify_random_density.py` from the directory containing the extracted file. It uses only the Python standard library.

## Relationship to prior work

The density axiom and its first-order relational correspondence \(R\subseteq R^2\) are classical modal logic, not new. Takahashi's 2026 work on finite-frame validity motivates quantifying this property on random frame classes but studies different complexity questions. Goranko's work on almost-sure frame validity studies random relational frames and limiting validity, principally in the conventional constant-edge-probability regime. In contrast, the present claim concerns the explicitly parameterized *sparse, loop-free* independent-arc model, a second-order centering \(\frac12\log\log n\), and a nondegenerate Poisson critical law. Karp's classical work concerns random-digraph reachability and strong components, not this finite-length-witness event.

The Poisson argument resembles general rooted-subgraph extension methods in random graph theory. A sufficiently general existing theorem for sharp coverings of **present arcs** by transitive directed triangles could subsume it; no absolute historical priority is asserted. The described finite-parameter statement and its proof were not identified in the sources checked for this result.

## Limitations

The limit is proved for loop-free directed frames with independently sampled ordered arcs; loops, correlated arcs, undirected edges, and arbitrary modal formulas require separate analysis. The theorem does not characterize every possible sparse regime between the two example densities. The external literature comparison is not an exhaustive priority proof, and some historical full texts could not be obtained. No independent validation has been performed.

## References

- T. Takahashi, *Non-elementary modal logics, assuming \(\mathsf P\neq\mathsf{NP}\)*, arXiv:2609.10872v1, first public 2026-09-09, https://arxiv.org/abs/2609.10872.
- V. Goranko, *The Modal Logic of Almost Sure Frame Validities in the Finite*, Advances in Modal Logic 13 (2020), 249–268, https://www.aiml.net/volumes/volume13/Goranko.pdf.
- V. Goranko and B. Kapron, *The modal logic of the countable random frame*, Archive for Mathematical Logic 42 (2003), 221–243, https://doi.org/10.1007/s001530100135.
- R. M. Karp, *The transitive closure of a random digraph*, Random Structures & Algorithms 1 (1990), 73–93, https://doi.org/10.1002/rsa.3240010106.
- *Modal Logic*, Stanford Encyclopedia of Philosophy, section on the density axiom \(\mathsf{C4}\), https://plato.stanford.edu/archives/sum2016/entries/logic-modal/.
