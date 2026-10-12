# Third-moment reversals first appear at seven species in degree-matched coextinction networks

## Finding

Let \(G\) and \(H\) be connected bipartite plant–pollinator networks with exactly three plant vertices, the same number \(n\) of pollinator vertices, no isolated pollinators, and identical multisets of plant degrees. Each plant disappears secondarily exactly when all its pollinators disappear primarily. Suppose the subsets of deleted pollinators in the two networks have the same **exchangeable** probability law (the law is invariant under permuting pollinator labels). Write \(X_G\) and \(X_H\) for the numbers of secondary plant extinctions and \(\mu=\mathbb E X_G=\mathbb E X_H\). Then

\[
\boxed{\mathbb E[(X_G-\mu)^3]-\mathbb E[(X_H-\mu)^3]
=3(1-\mu)(\operatorname{Var}X_G-\operatorname{Var}X_H).}
\]

Under independently and identically deleted pollinators with deletion probability \(0<q<1\), the smallest pair of **connected, degree-matched** networks whose third-central-moment order reverses as \(q\) varies has **seven total vertices** (plants plus pollinators). The bound holds even after requiring equal plant- and pollinator-degree multisets and is attained by two seven-vertex bipartite trees. Their means agree, and one variance is strictly greater for every \(q\), yet their third central moments change order once.

## Assumptions and scope

Every graph is simple and bipartite, with plant vertex set \(P\) and pollinator vertex set \(Q\). Every vertex has a neighbor. A plant \(i\in P\) has nonempty neighborhood \(N_i\subseteq Q\). A random subset \(D\subseteq Q\) of pollinators disappears, and plant \(i\) disappears if and only if \(N_i\subseteq D\). Thus

\[
X_G=\sum_{i\in P}{\bf1}_{\{N_i\subseteq D\}}.
\]

An exchangeable deletion law means \(\Pr(S\subseteq D)\) is the same for every fixed subset \(S\subseteq Q\) of the same size. The same law is used for the compared networks. Uniformly deleting exactly \(k\) of \(n\) pollinators and deleting each pollinator independently with probability \(q\) are both included. The moment identity requires exactly three plants and equal plant-degree multisets, but not equal pollinator-degree multisets. The sharp minimum statement additionally requires both guilds' degree multisets to match, connectedness, and iid primary deletions.

## Proof

**Universal three-plant identity.** Let \(Y_i={\bf1}_{\{N_i\subseteq D\}}\) and let \(B=\sum_{i<j}\mathbb E(Y_iY_j)\). Exchangeability gives \(\mathbb EY_i=r_{|N_i|}\) for numbers \(r_d\) independent of the network, so common plant-degree multisets give the common mean \(\mu\). Since there are only three plant vertices and every pollinator has at least one incident edge, \(\bigcup_iN_i=Q\). Consequently \(Y_1Y_2Y_3={\bf1}_{\{D=Q\}}\); its mean \(p_*=\Pr(D=Q)\) is common. The identities \(Y_i^2=Y_i\) yield

\[
\mathbb E X^2=\mu+2B,\qquad
\mathbb E X^3=\mu+6B+6p_*.
\]

Hence \(\operatorname{Var}X=\mu+2B-\mu^2\) and

\[
\mathbb E[(X-\mu)^3]
=\mu+6B+6p_*-3\mu(\mu+2B)+2\mu^3.
\]

Subtract these equations for \(G,H\). The common \(\mu\) and \(p_*\) cancel, giving \(\Delta\operatorname{Var}=2\Delta B\) and \(\Delta m_3=6(1-\mu)\Delta B=3(1-\mu)\Delta\operatorname{Var}\). No independence assumption is used in this step.

**Six-vertex lower bound.** For each ordered pair of positive guild sizes \((m,n)\) with \(m+n\le6\), enumerate every binary \(m\)-by-\(n\) incidence matrix. Discard disconnected graphs and graphs with empty rows or columns. Group the remainder by the ordered pair of **sorted** plant- and pollinator-degree sequences. For each matrix, all \(k\in\{0,\ldots,n\}\), and all counts \(r\in\{0,\ldots,m\}\), enumerate the exact integer count

\[
a_{k,r}=\#\{D\subseteq Q:|D|=k,\ X_G(D)=r\}.
\]

The included exhaustive standard-library checker visits all \(387\) admissible labeled matrices in \(44\) degree-signature groups. Within **each** group the entire array \((a_{k,r})\) is identical. Because any exchangeable deletion law is a mixture of uniform fixed-\(k\) deletion laws, matched signatures therefore imply identical **full distributions** of \(X\) whenever \(m+n\le6\). In particular their third-central-moment ordering cannot reverse. This is an exhaustive finite verification, not a claim about arbitrary larger graphs.

**Seven-vertex construction and exact crossing.** Take plants \(A,B,C\) and four pollinators numbered \(1,2,3,4\). List each pollinator's set of plant neighbors in order:

\[
G:\ (\{A\},\{A\},\{A,B\},\{B,C\}),\qquad
H:\ (\{A\},\{B\},\{A,B\},\{A,C\}).
\]

Both are connected, have seven vertices and six edges (hence are trees), and both have sorted plant degrees \((1,2,3)\) and sorted pollinator degrees \((1,1,2,2)\). Under iid primary deletion with probability \(q\), each plant's extinction probability is \(q^{|N_i|}\), so in both networks

\[
\mu(q)=q+q^2+q^3.
\]

Simultaneous extinction of plants \(i,j\) has probability \(q^{|N_i\cup N_j|}\), giving

\[
B_G(q)=q^2+2q^4,\qquad B_H(q)=2q^3+q^4.
\]

Consequently

\[
\operatorname{Var}X_G-\operatorname{Var}X_H
=2(B_G-B_H)=2q^2(1-q)^2>0,
\]

and the three-plant identity yields

\[
\mathbb E[(X_G-\mu)^3]-\mathbb E[(X_H-\mu)^3]
=6q^2(1-q)^2(1-q-q^2-q^3).
\]

Since \(q+q^2+q^3\) is strictly increasing from \(0\) to \(3\) on \((0,1)\), there is exactly one root \(q_*\in(0,1)\) of \(q_*+q_*^2+q_*^3=1\), namely \(q_*=0.543689012692076\ldots\). For \(q<q_*\), the third central moment of \(G\) exceeds that of \(H\); for \(q>q_*\), the strict inequality reverses. This proves sharpness at seven total vertices.

## Verification

The independently executable `checker.py` uses only the Python standard library. Running `python checker.py` reproduces the exact finite census, comparing all fixed-deletion-count distributions within each bidegree signature. It also reconstructs both seven-vertex incidence matrices, checks connectedness and degree multisets, computes full probability-generating polynomials over integer coefficients, and verifies the three exact polynomial identities and four rational-\(q\) instances. Expected final line:

`VERIFY_OK labeled_connected_small=387 matched_degree_profiles=44 seven_species_trees=2 moment_polynomial_identities=3 exact_probability_tests=4`

The infinite-range moment identity and uniqueness of the positive crossover are proved algebraically above; no finite numerical sample substitutes for those proofs. The finite minimality assertion relies on a complete finite exhaustive enumeration through six total species.

## Relationship to prior work

Memmott, Waser and Price (2004) introduced a pollinator-removal model in which loss of all pollinators causes secondary plant extinction and analyzed attack-tolerance curves. Burgos and collaborators (2006 preprint, later published) established robustness relations for perfectly nested mutualistic networks under prescribed removal orders. Jones, Zurell and Wiesner (2024) developed analytic predictions of mean secondary extinctions, including arbitrary ecological networks and extensions to multiple layers. These are premises and context, not new claims. Their inspected methods and results focus on average robustness and do not state the three-plant third-moment identity or the seven-vertex degree-matched sharpness classification. The general elementary identities for sums of indicators are also not claimed as novel by themselves; the assessed result is their ecology-specific structural consequence together with a sharp minimum-size construction and exclusion. Equivalent specialized prior coverage is not definitively ruled out.

## Limitations

These are the **unstandardized third central moments**, not normalized skewness coefficients. A reversed third-moment ranking does not establish a reversal of tail risks, stochastic dominance, or a field-measured extinction frequency. The model treats interaction links as binary and equally sufficient, and models only a single wave of secondary plant extinctions after pollinator loss. The sharp minimum compares graphs with the same numbers of plant and pollinator species and the same degree multisets on **both** sides; no minimum is claimed under different comparison rules. The universal moment law is specific to three plants and exchangeable primary deletions with no isolated pollinator. The finite exact enumeration says nothing about all larger networks.

## References

1. Memmott, J., Waser, N. M., and Price, M. V. (2004), “Tolerance of pollination networks to species extinctions,” *Proceedings of the Royal Society B* 271, 2605–2611. First published online December 6, 2004. DOI: 10.1098/rspb.2004.2909. Accessible full text: https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf
2. Burgos et al. (2006), “Why Nestedness in Mutualistic Networks?” arXiv:q-bio/0609005, first submitted September 5, 2006. Full text: https://arxiv.org/pdf/q-bio/0609005
3. Jones, C., Zurell, D., and Wiesner, K. (2024), “Novel analytic methods for predicting extinctions in ecological networks,” *Ecological Monographs* 94, e1601. DOI: 10.1002/ecm.1601. Full text: https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/ecm.1601
