# Nine-species threshold for reversed coextinction-richness variance in degree-matched mutualistic networks

## Finding

**Theorem.** Consider a finite simple bipartite interaction graph with a nonempty plant guild and a nonempty pollinator guild. Every pollinator independently becomes extinct with probability \(q\in(0,1)\), and a plant persists precisely when at least one of its neighbors persists. Let \(R_G(q)\) be the number of surviving plants. Two graphs are *bidegree matched* if the multisets of degrees within **each** guild are identical; the guild sizes therefore agree. Every bidegree-matched pair with at most eight total species has variance functions that are weakly ordered in one direction for all \(0<q<1\), with equality allowed. The cutoff is sharp: two graphs with four plants and five pollinators, whose plant-degree multiset is \((1,2,3,3)\) and pollinator-degree multiset is \((1,1,2,2,3)\), have

\[
\operatorname{Var}(R_A(q))-\operatorname{Var}(R_B(q))
=-2q^2(1-q)^2(1-2q).
\]

Their mean surviving richness is identical for every \(q\), but the variance ordering reverses exactly once, at \(q=1/2\). Consequently, equal degree profiles in both guilds do not determine even the *ordering* of coextinction-richness volatility across extinction intensities.

## Assumptions and scope

The bipartite graph is finite, undirected, simple, and contains no probabilistic interaction weights. Each pollinator has independent Bernoulli extinction with the **same** probability \(q\). Plants have no direct primary extinction, no rescue through undisclosed partners, and no secondary cascades beyond the loss of all their pollinators. The random variable \(R_G(q)\) counts plant species that retain at least one pollinator. The theorem compares graphs with separately identical multisets of plant degrees and pollinator degrees; node labels and identities are irrelevant. Isolated species may be removed from both graphs, preserving comparisons, so enumeration may restrict attention to nonzero degree rows and columns.

One exact pair is specified using the pollinator labels \(1,2,3,4,5\). For graph \(A\), its four plant neighborhoods are

\[
\{2\},\quad \{1,5\},\quad \{2,3,4\},\quad \{2,3,4\}.
\]

For graph \(B\), they are

\[
\{5\},\quad \{1,5\},\quad \{1,2,3\},\quad \{1,2,4\}.
\]

The networks are distinct despite matched degrees in both guilds. Their common mean richness is \(4-q-q^2-2q^3\).

## Proof

**Step 1: exact variance identity.** Let \(N_i\) be the pollinator neighborhood of plant \(i\), let \(d_i=|N_i|\), and let \(h_{ij}=|N_i\cap N_j|\). Writing \(X_i\) for the indicator that plant \(i\) survives, its extinction probability is \(q^{d_i}\). For distinct plants, the probability they both go extinct is \(q^{|N_i\cup N_j|}=q^{d_i+d_j-h_{ij}}\). The survival covariance equals the extinction covariance, hence

\[
\operatorname{Var}(R_G(q))=\sum_i q^{d_i}(1-q^{d_i})+2\sum_{i<j}\left(q^{d_i+d_j-h_{ij}}-q^{d_i+d_j}\right). \tag{1}
\]

The first sum and the negative terms of the second depend only on plant degrees; the positive terms depend on the overlap geometry. Formula (1) proves that bidegree-matched graphs always have equal mean richness, but need not have equal variance.

**Step 2: nine-vertex witness.** Directly taking degrees and neighborhood unions of the two displayed matrices gives

\[
\operatorname{Var}(R_A(q))=-4q^6-5q^4+8q^3+q,
\qquad \operatorname{Var}(R_B(q))=-4q^6-4q^5+5q^4+2q^2+q.
\]

Subtracting and factoring yields the theorem's \(-2q^2(1-q)^2(1-2q)\) identity. For example, at \(q=1/4\), the two variances are respectively \(363/1024\) and \(399/1024\); at \(q=3/4\), they are respectively \(1875/1024\) and \(1839/1024\). Their strict ranking therefore reverses, with the unique interior equality at \(q=1/2\).

**Step 3: exhaustive lower bound for eight or fewer species.** For each pair of guild sizes \(r,c\ge2\) with \(r+c\le8\), enumerate every binary \(r\times c\) incidence matrix with no zero row or column. The row order can be chosen canonically by sorting each row's \(c\)-bit binary mask, without losing any isomorphism type or any variance polynomial. Group these matrices by their ordered pair of *sorted* row- and column-degree sequences. Within each group, compute the integer polynomial consisting of the positive overlap term from (1), namely \(2\sum_{i<j}q^{|N_i\cup N_j|}\); all remaining terms cancel when two group members are compared.

Across all \(r,c\) with \(r+c\le8\), there are exactly \(93\) unordered comparisons of *distinct* overlap polynomials within common bidegree classes, yielding only \(13\) different nonzero polynomials up to sign (and removal of trailing zero coefficients). Each difference polynomial is divisible by some powers of \(q\) and \(1-q\). After removing those factors, reversing the overall sign if needed, and dividing by the positive integer content, **every reduced polynomial** belongs to

\[
\{1,\ 1+q,\ 1+2q,\ 1+q+q^2\}.
\]

Each is strictly positive on \(0<q<1\); thus no difference can change sign in that interval. This establishes the entire eight-species lower bound, not merely a grid of test probabilities. With a one-plant guild or one-pollinator guild, the graph (and hence its variance curve) is uniquely fixed by the degree sequences. An isolated species has deterministic behavior and may be deleted without changing the variance comparison, while preserving the matched degree profiles of the smaller networks. These observations cover every possible smaller graph.

The supplied standalone Python certificate enumerates the full finite matrix domain, forms the exact integer coefficient vectors, verifies all \(93\) comparisons and their reduced polynomials, and independently evaluates the witness via the entire \(2^5\)-state extinction probability space. The finite exhaustive step is an exact proof of the sharp lower bound because its search space and equivalence reduction are explicitly complete; the witness factorization proves the all-parameter reversal.

## Verification

Run `python verifier.py` beside `certificate.json`. The script uses only the Python standard library and prints one JSON record with exact counts, admissible polynomial factors, the two incidence matrices, and rational variance values. Its stdout must exactly match `certificate.json`. No stochastic simulation, floating-point tolerance, or external data are used. The finite search covers every bidegree-matched simple bipartite graph with at most eight vertices after deleting isolates; the witness factor identity holds for the full continuum \(q\in(0,1)\).

## Relationship to prior work

Memmott, Waser and Price (2004) motivate pollinator-removal coextinction and emphasize the role of partner redundancy. Burgos and collaborators (2008) study mutualistic-network nestedness and average attack-tolerance curves; Section 2 describes the uniform pollinator-removal null model and plant coextinction rule. Kaiser-Bunbury and collaborators (2010) analyze network robustness across pollinator-removal strategies. James, Pitchford and Plank (2012) caution that network degree effects and nestedness can be confounded. Vieira and Almeida-Neto (2015) examine richer stochastic coextinction mechanisms. The known expected-richness profile and elementary covariance formula (1) are not claimed as new. The finding here is the **sharp finite-size cutoff**, including full bidegree matching and reversal of *variance* ordering as the independent extinction probability changes. Earlier network-robustness results focused primarily on expectation, survival curves, or different stochastic rules and do not, in the material inspected, supply that finite classification.

## Limitations

This is a statement about a mathematically specified one-stage homogeneous extinction model, not a prediction for measured real communities without calibration. Variance of species richness is one measure of risk and is not an ordering of full extinction distributions. General multilayer networks, heterogeneous partner survival, adaptive rewiring and cascading mechanisms are outside scope. The eight-vertex sharpness requires a finite exhaustive enumeration; its code is part of the evidence rather than merely an illustration. Possible undiscovered equivalent finite tables or a broader reliability-theory theorem remain bibliographic risks. No independent review or independent replication is claimed.

## References

1. J. Memmott, N. M. Waser, M. V. Price (2004), *Tolerance of pollination networks to species extinctions*, Proceedings of the Royal Society B 271, 2605–2611, https://doi.org/10.1098/rspb.2004.2909. Online first 2004-12-06.
2. E. Burgos, H. Ceva, L. Hernández, R. P. J. Perazzo (2008), *Understanding and characterizing nestedness in mutualistic bipartite networks*, arXiv:0809.3681, https://arxiv.org/abs/0809.3681. First posted 2008-09-22.
3. C. N. Kaiser-Bunbury et al. (2010), *The robustness of pollination networks to the loss of species and interactions*, Ecology Letters 13, 442–452, https://doi.org/10.1111/j.1461-0248.2009.01437.x.
4. A. James, J. W. Pitchford, M. J. Plank (2012), *Disentangling nestedness from models of ecological complexity*, Nature 487, 227–230, https://doi.org/10.1038/nature11214.
5. M. C. Vieira, M. Almeida-Neto (2015), *A simple stochastic model for complex coextinctions in mutualistic networks*, Ecology Letters 18, 144–152, https://doi.org/10.1111/ele.12394.
