# Eleven pollinators are necessary for a three-plant coextinction-variance reversal

## Finding

**Theorem (sharp three-plant threshold).** Let \(G\) be a connected simple bipartite graph consisting of exactly three plant species and \(n\ge1\) pollinator species, without isolated vertices. Independently remove every pollinator with probability \(q\in(0,1)\), and let \(X_G(q)\) count plants that lose *all* their original pollinators. Two networks are *degree-matched* when both their plant-degree multisets and their pollinator-degree multisets agree. Define a variance-ranking reversal between degree-matched networks as a sign change of \(\operatorname{Var}(X_G(q))-\operatorname{Var}(X_H(q))\) inside \((0,1)\).

**No pair of degree-matched connected three-plant networks with at most ten pollinators admits a variance-ranking reversal. Eleven pollinators suffice.** One exact witness has the following multisets of pollinator types: write \(a,b,c\) for the numbers visiting only plants \(1,2,3\), respectively; \(d,e,f\) for those visiting exactly \(\{1,2\},\{1,3\},\{2,3\}\), respectively; and \(g\) for those visiting all three plants. Take

\[
G:(a,b,c,d,e,f,g)=(4,4,0,0,2,0,1),\qquad
H:(a,b,c,d,e,f,g)=(5,2,1,1,0,1,1).
\]

Both networks are connected. Their three plant degrees, in increasing order, are \((3,5,7)\); their eleven pollinators have degrees \(1\) (eight instances), \(2\) (two instances), and \(3\) (one instance). Their expected secondary-extinction counts agree for every \(q\):

\[\mathbb E[X_G(q)]=\mathbb E[X_H(q)]=q^3+q^5+q^7.\]

Nevertheless,

\[
\boxed{\operatorname{Var}(X_G(q))-\operatorname{Var}(X_H(q))=2q^6(1-q)^2(q^3+q^2-1).}
\]

Thus \(G\) has strictly smaller variance below the unique interior threshold \(q_*\), and strictly larger variance above it, where

\[\boxed{q_*^3+q_*^2=1,\qquad q_*\approx0.754877666247.}\]

Equivalently, \(q_*\) is the reciprocal of the plastic constant. The threshold applies to the entire probability interval, not a numerical sample. The minimum number of pollinator species for this reversal among connected three-plant networks is **exactly eleven**, making fourteen species in total.

## Assumptions and scope

A graph is finite, simple, undirected and bipartite. The three plant vertices and all pollinator vertices have positive degrees, and the interaction graph is connected. Each pollinator independently disappears with the same probability \(q\), and a plant is counted as secondarily lost precisely when no incident pollinator remains. Plant extinctions do not in turn remove pollinators; no demographic, demographic-rescue, interaction-rewiring, or additional cascading assumptions are made. Degrees are unordered multisets separately for the two guilds, not a fixed labeled correspondence. There is no randomness over network structure; the variance is conditional on each fixed network.

For each plant \(i\in\{1,2,3\}\), let \(N_i\) be its original pollinator neighborhood, \(d_i=|N_i|\), and \(I_i\) indicate the event that all members of \(N_i\) disappear. Then \(X_G=I_1+I_2+I_3\).

## Proof

**1. Moment identity and three-plant simplification.** Independently lost pollinators yield \(\mathbb E[I_i]=q^{d_i}\) and \(\mathbb E[I_iI_j]=q^{|N_i\cup N_j|}\), hence

\[
\operatorname{Var}(X_G)=\sum_i q^{d_i}(1-q^{d_i})+2\sum_{i<j}\big(q^{|N_i\cup N_j|}-q^{d_i+d_j}\big).
\]

For degree-matched graphs, all terms besides the sum of union probabilities cancel in a variance difference. Because there are **exactly three** plants and no pollinator is isolated, a pollinator is absent from \(N_1\cup N_2\) if and only if it visits *only* plant \(3\), and similarly cyclically. Therefore the multiset of three union sizes is exactly \(\{n-a,n-b,n-c\}\). The variance comparison between any two degree-matched three-plant networks is consequently

\[
\frac{\operatorname{Var}(X_G)-\operatorname{Var}(X_H)}2
=\sum_{u\in U_G}q^u-\sum_{u\in U_H}q^u,\quad U_G=\{n-a,n-b,n-c\}.
\]

**2. Complete finite parametrization.** Every simple three-plant graph has each pollinator adjacent to one of the seven nonempty subsets of the plant guild, so it is completely determined, up to pollinator relabeling, by a unique seven-tuple of nonnegative integers \((a,b,c,d,e,f,g)\) summing to \(n\). Its plant degrees are

\[
(a+d+e+g,\ b+d+f+g,\ c+e+f+g),
\]

and its pollinator degree multiset has \(a+b+c\) entries equal to one, \(d+e+f\) entries equal to two, and \(g\) entries equal to three. The incidence graph is connected exactly when all three plant degrees are positive and at least two of \(d+g,e+g,f+g\) are positive; equivalently the three-plant overlap graph is connected. This is an exact combinatorial characterization, not a statistical filter.

**3. Exact non-reversal certificate through ten pollinators.** For each integer \(1\le n\le10\), the standalone `verify.py` enumerates all seven-part nonnegative compositions of \(n\), retains precisely the connected types just characterized, sorts the plant degrees, and uses the pollinator degree multiplicities to form *all* degree-matching classes. Within each class it retains every possible sorted union-size triple \(U\). Every possible variance comparison in the finite problem is therefore present, with no sampling or unenumerated graph type.

For each pair of different triples \(U,V\) in the same class, form the exact integer polynomial

\[F(q)=\sum_{u\in U}q^u-\sum_{v\in V}q^v.\]

Set \(q=t/(1+t)\) for \(t>0\). The verifier expands the integer polynomial

\[P(t)=(1+t)^nF\!\left(\frac{t}{1+t}\right),\qquad
[t^k]P(t)=\sum_{j=0}^{k}c_j\binom{n-j}{k-j},\]

where \(c_j\) is the difference in multiplicities of union size \(j\). **Every** such coefficient vector, for all classes and all \(1\le n\le10\), consists either entirely of nonnegative entries or entirely of nonpositive entries. Since \(1+t>0\) and every \(t^k>0\), this exact sign certificate rules out a sign change for every real \(q\in(0,1)\). In total, it checks \(17{,}017\) connected type vectors, \(1{,}529\) distinct-profile comparisons, and all relevant class memberships. This finite exhaustive conclusion relies on the transparent standalone enumerator's mathematical completeness established above; it is not an inference from a finite probability grid.

**4. Sharp witness and unique crossing.** The displayed tuples each sum to eleven and have the same two degree multisets. Their union-size multisets are respectively \((7,7,11)\) and \((6,9,10)\). Substitution into the exact moment identity gives

\[
\tfrac12(\operatorname{Var}(X_G)-\operatorname{Var}(X_H))
=2q^7+q^{11}-q^6-q^9-q^{10}
=q^6(1-q)^2(q^3+q^2-1).
\]

The function \(q^3+q^2-1\) has derivative \(3q^2+2q>0\) on \((0,1)\), and values \(-1\) and \(1\) at the endpoints. It has exactly one root in the interval and strictly changes sign there. The factor \(q^6(1-q)^2\) is positive throughout the interval, completing the crossing proof. The connected eleven-pollinator construction and the ten-pollinator exclusion together prove minimality.

## Verification

Run `python3 verify.py` using only the Python standard library. It enumerates *all* connected type vectors for three plants and \(1\) through \(10\) pollinators, checks every degree-matched union-profile pair through exact nonnegative/nonpositive polynomial coefficients, and separately enumerates all \(2^{11}=2048\) binary pollinator-removal outcomes for each displayed witness. The latter independent moment expansion verifies the common mean \(q^3+q^5+q^7\) and exact variance-difference coefficients, in ascending powers, \((0,0,0,0,0,0,-2,4,0,-2,-2,2)\). On success the program prints `VERIFY_OK first_three_plant_reversal_at_eleven_pollinators`. Only integer arithmetic and finite exact binomial coefficients occur; no Monte Carlo simulation or floating-point sign decision is used.

## Relationship to prior work

Memmott, Waser, and Price (2004) introduced a comparable all-pollinators-lost secondary-extinction rule for plant–pollinator networks. Burgos et al. (2006/2007) examined nestedness and attack tolerance; Campbell et al. (2012) used a different dynamic extinction framework; Eklöf et al. (2013) developed a Bayesian secondary-extinction model. Chabert-Liddell, Barbillon, and Donnet (2021, Section 4.2) obtained analytical robustness variance expressions over *random bipartite network ensembles*, which is not a fixed-network, independent-per-pollinator variance comparison with matched dual degree multisets. General covariance calculations and qualitative topology effects are established precedents and are not claimed as new. The specific contribution is the sharp **three-plant eleven-pollinator first sign reversal** and an exact witness with its one-crossing law; earlier discoveries of reversals in larger plant guilds are not asserted to be new here.

## Limitations

The finding concerns the smallest pollinator guild for which the specified reversal exists with *exactly three* plants; it does not assert minimality among networks with an arbitrary number of plants, does not classify all possible eleven-pollinator witness graphs, and does not characterize dependence-weighted or correlated extinctions. The ecological interpretation is limited by identical independent primary hazards, absence of rewiring, and the all-neighbors-lost rule. The finite certificate has not received independent external audit. An equivalent analysis in unlocated exact reliability-polynomial or specialized ecology literature remains a priority risk, despite direct checks against the cited relevant full texts.

## References

1. Memmott, J., Waser, N. M., and Price, M. V. (2004). *Tolerance of pollination networks to species extinctions*. Proceedings of the Royal Society B 271, 2605–2611. DOI: 10.1098/rspb.2004.2909; published online 2004-12-06. Full author-hosted article: https://www.bio.bris.ac.uk/research/community/article_PDF/Memmottetal2004.pdf.
2. Burgos, E., Ceva, H., Perazzo, R. P. J., et al. (2007). *Why nestedness in mutualistic networks?* Journal of Theoretical Biology 249, 307–313. arXiv:q-bio/0609005 (2006 original preprint).
3. Campbell, C., Yang, S., Shea, K., and Albert, R. (2012). *Topology of plant-pollinator networks that are vulnerable to collapse from species extinction*. Physical Review E 86, 021924. DOI: 10.1103/PhysRevE.86.021924.
4. Eklöf, A., Tang, S., and Allesina, S. (2013). *Secondary extinctions in food webs: a Bayesian network approach*. Methods in Ecology and Evolution. DOI: 10.1111/2041-210X.12062.
5. Chabert-Liddell, S.-C., Barbillon, P., and Donnet, S. (2021). *Impact of the mesoscale structure of a bipartite ecological interaction network on its robustness through a probabilistic modeling*. arXiv:2106.06348; DOI: 10.1002/env.2709.
