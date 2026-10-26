# First online-versus-static shattering gaps for maximal independent sets of cycles

## Finding

For an integer \(n\ge3\), write \(C_n\) for the ordinary undirected cycle on vertex set \(\{0,\ldots,n-1\}\), indices modulo \(n\). Let \(\mathcal M_n\) be the Boolean membership concept class of all *inclusion-maximal independent sets* of \(C_n\). A query names one vertex and asks whether it belongs to the unknown maximal independent set. The exact dimensions through order sixteen are:

| \(n\) | \(|\mathcal M_n|\) | VC dimension | Littlestone dimension |
|---:|---:|---:|---:|
| 3 | 3 | 1 | 1 |
| 4 | 2 | 1 | 1 |
| 5 | 5 | 2 | 2 |
| 6 | 5 | 2 | 2 |
| 7 | 7 | 2 | 2 |
| 8 | 10 | 3 | 3 |
| 9 | 12 | 3 | 3 |
| 10 | 17 | 3 | 3 |
| 11 | 22 | 4 | 4 |
| 12 | 29 | 4 | 4 |
| 13 | 39 | 4 | 5 |
| 14 | 51 | 5 | 5 |
| 15 | 68 | 5 | 5 |
| 16 | 90 | 5 | 6 |

In particular, the smallest cycle with a strict separation is \(C_{13}\):
\[
\operatorname{Ldim}(\mathcal M_{13})-\operatorname{VCdim}(\mathcal M_{13})=1.
\]
The gap then vanishes at orders fourteen and fifteen and reappears at sixteen. For every positive integer \(s\), on the disjoint union \(G_s\) of \(s\) thirteen-cycles, the corresponding maximal-independent-set membership class satisfies
\[
\operatorname{VCdim}(\mathcal M(G_s))=4s,\qquad
\operatorname{Ldim}(\mathcal M(G_s))=5s.
\]
Hence the gap is unbounded among two-regular graphs. The disjoint-union consequence does not claim connected extremizers.

## Assumptions and scope

An independent set contains no pair of adjacent vertices. It is *maximal* if adding any further vertex destroys independence; this is not the same as *maximum* cardinality. The VC dimension is the largest number of fixed vertex queries realizing all binary labelings, and Littlestone dimension is the largest depth of a complete binary adaptive query tree whose every root-to-leaf answer sequence is realized by at least one hypothesis. Repeated identical hypotheses are counted only once. The finite profile is claimed only for the displayed fourteen cycle orders \(3\le n\le16\); no formula for all cycles is asserted.

## Proof

**Finite hypotheses.** Identify a vertex subset with its length-\(n\) binary word \(b_0\ldots b_{n-1}\). It is a maximal independent set precisely when (i) no adjacent pair is \(11\) and (ii) no position occupied by \(0\) has both neighbors \(0\). Condition (ii) is equivalent to every omitted vertex being dominated by a chosen neighbor. Thus the complete hypothesis list is exactly the collection of cyclic binary words avoiding \(11\) and \(000\), with the wraparound positions included. `verify.py` implements this equivalence in two different enumerations: exhaustive integer bit masks and a recursively extended binary word with local checks and final wraparound checks. Their equality is asserted separately for each order.

**Exhaustive static bound.** For every subset \(S\) of the vertices, take the trace family \(\{M\cap S:M\in\mathcal M_n\}\). The set is shattered if and only if there are exactly \(2^{|S|}\) different traces. The verifier enumerates every subset \(S\) at each cardinality until none is shattered. Once no subset of size \(k\) is shattered, none of larger size can be, since every subset of a shattered set is shattered. This is a *complete*, not sampled, computation. The listed VC dimensions and witnesses follow.

**Exhaustive adaptive bound.** Let \(H\) be any nonempty subset of the enumerated hypotheses, and put \(d(H)=0\) if \(|H|\le1\). Otherwise define
\[
d(H)=\max_{v:\ H_{v,0},H_{v,1}\ne\varnothing}
\left(1+\min\{d(H_{v,0}),d(H_{v,1})\}\right),
\]
where \(H_{v,b}=\{h\in H:h(v)=b\}\), and the maximum is zero if no query splits \(H\). Induction on \(|H|\) shows this is exactly the largest complete adaptive shattering depth: the first question must split \(H\) into both nonempty branches and each branch must support the remaining depth. Every recursive child is a strict subset. Thus the memoized exhaustive evaluation of this recurrence proves both upper and lower bounds; its states are actual version-space subsets, not approximations. The verifier evaluates the recurrence twice, independently using integer bitsets and immutable sets of hypothesis integers, with equality asserted on each full cycle class.

**Explicit adaptive witnesses.** The accompanying `certificate.json` supplies full depth-five and depth-six decision trees for \(C_{13}\) and \(C_{16}\), respectively. Every leaf records an integer encoding an actual maximal independent set; the verifier checks its answers at *every* ancestor. The trees have \(32\) and \(64\) validated leaves. Counting gives the complementary upper bounds: \(|\mathcal M_{13}|=39<64\) and \(|\mathcal M_{16}|=90<128\). Therefore their adaptive dimensions are exactly five and six. For all smaller displayed orders the same exhaustive recurrence gives the dimensions in the table, and the recorded routine produces independently checked full lower-bound trees for each.

**Disjoint unions.** Every maximal independent set in a disjoint union is uniquely the union of maximal independent sets in its components. On disjoint query domains the VC dimension of a Cartesian product of concept classes is the sum: trace shattering splits into componentwise trace shattering, and combining shattered sets yields the reverse inequality. Littlestone dimension is also additive. For the lower bound, concatenate complete shattered trees on the separate domains; for the upper bound, run optimal realizable online predictors on the components independently, accumulating at most the sum of their optimal mistake bounds. The classical equality between this bound and Littlestone dimension gives the upper bound. Consequently \(s\) copies of \(C_{13}\) yield the asserted dimensions.

## Verification

From the directory containing the supplied stand-alone files, execute `python3 verify.py certificate.json` using Python 3 with no external dependencies. The verifier performs both enumerations, both adaptive recurrences, exhaustive VC trace checks, validates lower-bound trees for all fourteen orders, and checks every branch/leaf of the two exported certificates. The recorded `verification_output.txt` is the output of `python3 verify.py`, which also created `certificate.json`; replay with the certificate file checks identical contents. The final printed sentinel is `ALL_CYCLE_CHECKS_PASS`. All computations are bounded by at most \(2^{16}\) candidate binary words per cycle and finite version-space states. Correctness for the fourteen enumerated orders follows from the exhaustive enumerator and rank recurrences, not from extending a numerical pattern.

## Relationship to prior work

Earlier investigations of maximal-independent-set membership on cycles have determined an all-order Boolean trace (VC) dimension; that static formula alone gives no adaptive decision-tree rank. Our new point is the first strict *online* separation for this specific cycle family, its disappearance and reappearance, and explicit adaptive certificates. Exact results for maximal matchings in paths concern a different concept class: an edge matching of a path corresponds to an independent set of its *line graph*, itself a path, not to a maximal independent set of a cycle. The known path results therefore do not imply the cyclic wraparound cases here.

Cormode, Dark and Konrad study streaming algorithms for finding maximal independent sets, not vertex-membership Littlestone trees. Manurangsi gives general inapproximability results for computing VC and Littlestone dimensions of explicitly represented classes; the inspected reductions and bounds do not give this cycle profile. Liu, Shangguan, Skokan and Xu study the maximal-independent-set hypergraph and, in their Lemma 27, an upper bound on its **VC** dimension by a bipartite induced matching number; their inspected work does not calculate this online rank. These comparisons concern mathematical implications, not merely source titles.

## Limitations

The finite results are restricted to \(3\le n\le16\). The unbounded-gap consequence is for *disconnected* two-regular graphs, not connected graphs or cycles of arbitrary order. The proof depends on a finite exhaustive program, which is included completely and can be replayed. General dimensional equality or inequality beyond the stated orders is unproved. There may be unindexed prior art with an equivalent cycle-specific Littlestone computation; absence from the checked searches does not prove absolute priority. The scientific review here is not an independent audit.

## References

1. G. Cormode, J. Dark and C. Konrad, *Independent Sets in Vertex-Arrival Streams*, ICALP 2019, https://wrap.warwick.ac.uk/id/eprint/117339/ . First open-access date verified as 2019-05-29.
2. P. Manurangsi, *Improved Inapproximability of VC Dimension and Littlestone's Dimension via (Unbalanced) Biclique*, arXiv:2211.01443, first posted 2022-11-02, https://arxiv.org/abs/2211.01443 .
3. H. Liu, C. Shangguan, J. Skokan and Z. Xu, *Beyond Chromatic Threshold via (p,q)-Theorem, and Blow-Up Phenomenon*, SoCG 2024, full text https://d-nb.info/1367513596/34 .
