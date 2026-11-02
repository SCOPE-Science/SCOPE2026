# Six-voter pivotal fairness collapses to the icosahedral rule

## Finding

**Theorem (complete six-voter classification).** Let \(N=\{0,1,2,3,4,5\}\). Let \(f:2^N\to\{0,1\}\) be a deterministic, monotone, candidate-neutral two-candidate voting rule: \(S\subseteq T\) implies \(f(S)\le f(T)\), and \(f(N\setminus S)=1-f(S)\). Let \(W=\{S:f(S)=1\}\). The following conditions are equivalent:

1. All six Shapley–Shubik pivotal probabilities are equal.
2. All six unnormalized Banzhaf pivotal probabilities are equal.
3. Each voter has exactly five winning three-voter coalitions containing them and no winning coalition has fewer than three voters.
4. Fixing voter \(0\), the five winning triples containing \(0\) have the form \(\{0,i,j\}\), where the edges \(\{i,j\}\) form a five-cycle on \(\{1,2,3,4,5\}\). The remaining five winning triples are the complements, in \(N\), of triples \(\{0,i,j\}\) for nonedges \(\{i,j\}\) of that cycle.
5. The rule is *equitable*: its voter-permutation automorphism group is transitive.

There are exactly \((5-1)!/2=12\) such rules on the specified labeled voter set. They are all isomorphic, coincide (up to voter relabeling) with the known icosahedral rule *Icos*, have precisely ten minimal winning triples, and have automorphism groups of order \(60\). Each voter has Shapley–Shubik index \(1/6\) and raw Banzhaf pivotal probability \(10/32=5/16\).

The new assertion is the **exhaustive weak-fairness classification**: the existence and equitability of Icos are established in earlier literature and are not claimed as new.

## Assumptions and scope

The model has exactly six *labeled* voters, two alternatives, binary ballots and a deterministic outcome. Candidate neutrality is the complement identity above; monotonicity concerns increasing support for the chosen alternative. Neither voter anonymity nor voter transitivity is assumed. All coalitions are allowed and voters have equal a priori pivotal sampling under the respective index. No weighted voting, abstentions, additional candidates or probabilistic decision rules are included.

For a voter \(i\), write \(B_i\) for the number of subsets \(S\subseteq N\setminus\{i\}\) such that \(f(S)=0\) and \(f(S\cup\{i\})=1\). The raw Banzhaf probability is \(B_i/2^5\). Write \(H_i\) for the number of permutations of all six voters in which voter \(i\) is pivotal. The Shapley–Shubik index is \(H_i/6!\). Equal influence means, respectively, that the \(B_i\)'s or the \(H_i\)'s are all equal. The automorphisms of \(f\) permute voters while preserving all winning coalitions.

## Proof

**1. Restrict the lower winning coalitions.** Neutrality and monotonicity imply \(f(\varnothing)=0\), \(f(N)=1\), and every two winning coalitions intersect. If a singleton \(\{i\}\) wins, then neutrality and monotonicity force \(f(S)=1\) exactly when \(i\in S\): the rule is a dictatorship and neither pivotal index is equal across voters. Thus a fair rule has no winning singleton.

Let \(E\) denote its set of winning two-voter coalitions. Write \(m=|E|\), \(e_i=|\{P\in E:i\in P\}|\), and \(t_i=|\{T\in W:|T|=3, i\in T\}|\). Since \(E\) is pairwise intersecting as a graph of edges on six vertices, either \(E\) is a star with \(m\le5\) edges (including the empty star) or \(E\) is a triangle with \(m=3\). By complementarity there are exactly ten winning triples, all five- and six-voter coalitions win, and precisely the complements of the \(m\) winning pairs are losing four-voter coalitions.

A winning two-voter coalition containing \(i\) contributes \(e_i\). Four-voter winning coalitions containing \(i\) number \(10-m+e_i\), because a losing four-set has a winning two-set complement avoiding \(i\). Thus, writing \(w_i^{(k)}\) for winning size-\(k\) coalitions containing \(i\), the nonconstant levels are

\[
w_i^{(2)}=e_i,\qquad w_i^{(3)}=t_i,\qquad w_i^{(4)}=10-m+e_i.
\]

For a pivotal predecessor coalition of size \(k\), the count is \(p_i^{(k)}=w_i^{(k+1)}+w_i^{(k)}-W_k\), where \(W_k\) is the *total* number of winning size-\(k\) coalitions. Direct substitution gives

\[
(p_i^{(0)},p_i^{(1)},p_i^{(2)},p_i^{(3)},p_i^{(4)},p_i^{(5)})
=(0,e_i,t_i+e_i-m,t_i+e_i-m,e_i,0).
\]

Consequently the total Banzhaf swing count and Shapley–Shubik pivotal-permutation count are

\[
B_i=2(t_i+2e_i-m),\qquad H_i=24(t_i+3e_i-m).
\]

The totals over voters are, respectively, \(\sum_iB_i=60-4m\) and \(\sum_iH_i=720\). Therefore equality across all six voters means

\[
\text{Shapley–Shubik: }t_i+3e_i=5+m,\qquad
\text{Banzhaf: }t_i+2e_i=5+\frac{2m}{3}.
\]

**2. Neither weak fairness condition permits a winning pair.** If \(E\) is a nonempty star with center \(v\) and \(m\) edges, then \(e_v=m\) and each triple containing \(v\) and a star edge must win, giving

\[
t_v\ge {5\choose2}-{5-m\choose2}.
\]

For Shapley–Shubik equality, \(t_v=5-2m\), which is \(3\) for \(m=1\), \(1\) for \(m=2\), and negative for \(m\ge3\); the lower bound is already \(4\) for \(m=1\) and \(7\) for \(m=2\). For a triangle, \(m=3\), each triangle vertex has \(e_v=2\) and at least \(\(4+4-1=7\)\) winning triples, whereas Shapley–Shubik equality requires \(t_v=2\). Hence Shapley–Shubik fairness forces \(E=\varnothing\).

For Banzhaf equality the integer \(t_i+2e_i\) equals \(5+2m/3\), so \(3\mid m\). A nonempty intersecting edge family has at most five edges; thus \(m=3\), which is either a three-edge star or a triangle. A three-edge star requires \(t_v=5+2-6=1\) at its center, yet forces at least \(10-{2\choose2}=9\) winning triples. A triangle requires \(t_v=5+2-4=3\) at its vertices, yet forces at least seven winning triples. Hence Banzhaf fairness also forces \(E=\varnothing\).

**3. Turn fairness into a five-cycle.** When \(E=\varnothing\), every size-two set loses and every size-four set wins. For each complementary pair of size-three subsets, exactly one wins. Equality of either index becomes \(t_i=5\) for every voter. Fix voter \(0\). The winning triples through \(0\) correspond to edges of a simple graph \(G\) on the five other voters. Then \(t_0=|E(G)|=5\), so \(G\) has five edges. For each other voter \(j\), its winning triples comprise the \(\deg_G(j)\) selected triples through \(0\), together with the triples in \(N\setminus\{0\}\) complementary to *nonedges* of \(G\) avoiding \(j\). The latter number is

\[
5-(4-\deg_G(j))=1+\deg_G(j).
\]

Thus \(t_j=1+2\deg_G(j)\), and \(t_j=5\) if and only if \(\deg_G(j)=2\). A simple two-regular graph on five vertices is necessarily one five-cycle. Conversely, every five-cycle yields exactly the described ten triples, and adjoining all four-, five- and six-sets as winning produces a monotone, neutral rule satisfying both fairness conditions. There are \((5-1)!/2=12\) undirected five-cycles on five *labeled* vertices.

**4. Establish the equality of fairness and transitive symmetry.** All five-cycles are isomorphic by a permutation of the five vertices other than \(0\), so the twelve fair rules form one orbit under all \(6!\) voter permutations. Each rule's full automorphism group therefore has size \(6!/12=60\). The automorphisms fixing voter \(0\) are exactly the ten dihedral symmetries of its five-cycle. Hence the automorphism orbit of voter \(0\) has size \(60/10=6\), proving transitivity. Conversely, transitivity implies equal pivotal influence under either index, because voter relabeling carries pivotal events bijectively. For each rule \(t_i=5\), so the formulas above give \(B_i=10\) and \(H_i=120\). This proves all equivalences and counts. \(\square\)

## Verification

The accompanying standalone `verify.py` uses exact integers, generates every pairwise-intersecting set of potentially winning pairs, and exhausts all complement choices for triples subject to monotonicity. It checked **2640** non-dictatorial monotone neutral rules on six voters from **192** intersecting edge patterns. Exactly **12** were Shapley–Shubik-fair, exactly **12** were Banzhaf-fair, and they were the same rules. All have the required five-cycle structure and one labeled relabeling orbit; the computed automorphism order is \(60\). The six dictatorships are excluded analytically because of unequal power. This finite enumeration independently checks the short all-case proof; the proof itself does not rely on assuming a finite sample represents an infinite family.

Run `python3 verify.py` using Python's standard library only. The result is an exact integer check, without randomized sampling, optimization tolerances or network resources.

## Relationship to prior work

Dhar, Mittal and Thomas (2026) introduce the pivotal-index fairness question for neutral, monotone, resolute two-candidate voting rules, show which electorate sizes permit such rules, and identify Icos as a six-voter fair example. Their Proposition 2.2 develops formulas relating indices to sizes of winning coalitions; their displayed six-voter example is reused here as a **known** construction. Their article does not state the converse six-voter five-cycle classification, equivalence of the two index fairness notions at size six, or exactly twelve labeled possibilities.

Loeb and Conway (2000) study transitive maximal intersecting families and the Icos construction; transitivity is the *assumption* in their enumerative framework. Cameron, Frankl and Kantor (1989) study transitive and regular intersecting families, with general extremal and existence results. Langner (2012) provides all six-voter power-profile counts and algorithms over *all* simple games, not the explicit neutral six-voter exact classification proved here. Meyerowitz (1995) reports enumerating six-element maximal intersecting families; only the abstract was accessible during this comparison, so whether its full text contains an equivalent regularity classification is an outstanding literature risk. This result does not claim discovery of Icos, of the indexed fairness definitions, or of general intersecting-family enumeration.

## Limitations

The theorem is exact for six voters and deterministic monotone candidate-neutral two-alternative rules. It does not assert such a collapse of weak fairness to transitive symmetry for other electorate sizes, and does not address strategyproofness, asymmetric voter models or other indices. The classification and correctness have been checked mathematically and computationally, but independent validation has not been performed. Priority remains subject to inspection of any inaccessible earlier detailed classification, especially Meyerowitz (1995) and Loeb–Conway (2000), and any unindexed equivalent work.

## References

- M. Dhar, K. Mittal and C. Thomas, *Existence of Fair Resolute Voting Rules*, arXiv:2602.13894v1, first released February 14, 2026. https://arxiv.org/abs/2602.13894
- D. E. Loeb and A. R. Conway, *Voting Fairly: Transitive Maximal Intersecting Families of Sets*, Journal of Combinatorial Theory Series A 91 (2000), 386–410. https://doi.org/10.1006/jcta.2000.3103
- P. J. Cameron, P. Frankl and W. M. Kantor, *Intersecting Families of Finite Sets and Fixed-point-Free 2-Elements*, European Journal of Combinatorics 10 (1989), 149–160. https://pages.uoregon.edu/kantor/PAPERS/IntersectingFamilies.pdf
- A. Meyerowitz, *Maximal Intersecting Families*, European Journal of Combinatorics 16 (1995), 491–501. https://doi.org/10.1016/0195-6698(95)90004-7
- J. Langner, *Fairness, Efficiency and Democracy Deficit: Combinatorial Methods and Probabilistic Analysis on the Design of Voting Systems*, dissertation, FernUniversität in Hagen, 2012. https://ub-deposit.fernuni-hagen.de/servlets/MCRFileNodeServlet/mir_derivate_00000135/Diss_Langner_Fairness_2012.pdf
