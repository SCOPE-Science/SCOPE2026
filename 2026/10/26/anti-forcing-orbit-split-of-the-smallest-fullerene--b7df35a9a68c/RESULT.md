# Anti-forcing orbit split of the smallest fullerene

## Finding
For the dodecahedral graph \(D\), the anti-forcing polynomial (counting perfect matchings by the fewest nonmatching edges whose deletion leaves them unique) is
\[
\operatorname{Af}(D;z)=30z^4+6z^5.
\]
The 30 perfect matchings whose complementary spanning two-factor is a single 20-cycle each have anti-forcing number four and exactly eight four-edge minimum anti-forcing sets. The other six perfect matchings have complementary cycle lengths \((5,5,10)\), anti-forcing number five, and exactly 22 five-edge minimum anti-forcing sets. Hence there are exactly 240 minimum four-edge deletion sets associated to the former matchings and exactly 132 minimum five-edge deletion sets associated to the latter. These counts refer to distinct edge subsets of \(D\); every such subset leaves a unique matching.

## Assumptions and scope
Let \(D=GP(10,2)\), with vertices \(u_i,v_i\), \(i\in\mathbb Z/10\mathbb Z\), and edges \(u_iu_{i+1}\), \(u_iv_i\), and \(v_iv_{i+2}\). The twenty vertices and thirty edges are simple and undirected. A perfect matching \(M\) contains ten independent edges meeting all vertices. Define \(a_D(M)\) as the minimum cardinality of \(F\subseteq E(D)\setminus M\) for which \(D-F\) has \(M\) as its unique perfect matching. For each \(M\), let \(N_D(M)\) count all such \(F\) with \(|F|=a_D(M)\). No claim is made about larger fullerenes or anti-Kekulé edge deletions, which have a different objective.

## Proof
A finite exhaustive proof is given by two fully specified algorithms, with complete runnable implementations in `verify_gp.py` and `verify_lcf.py`. The exhaustiveness argument is as follows.

For any finite even vertex subset \(U\), enumerate its perfect matchings by taking the least-labeled vertex \(v\in U\) and joining it in turn to each neighbor \(w\in U\), then recursively enumerating matchings of \(U\setminus\{v,w\}\). The empty set has exactly one empty matching. Induction on \(|U|\) proves that this recurrence lists every perfect matching exactly once; no heuristic cutoff is used. On the explicit thirty-edge model of \(D\), the recurrence produces exactly 36 distinct ten-edge matchings.

For every \(F\subseteq E(D)\) of size at most five, calculate \(s(F)=|\{M\in\mathcal P(D):M\cap F=\varnothing\}|\), where \(\mathcal P(D)\) is the exhaustive matching family. The condition \(s(F)=1\) is necessary and sufficient for \(F\) to be an anti-forcing set of its unique surviving matching. All \(\binom{30}{k}\) subsets are traversed for each \(0\le k\le5\). The resulting counts of subsets with \(s(F)=1\) at sizes zero through five are, respectively, \(0,0,0,0,240,7272\). Of the 36 matchings, exactly 30 are first isolated at size four, each by eight distinct four-edge sets. The other six are first isolated at size five, each by 22 distinct five-edge sets. Thus every matching has a demonstrated anti-forcing set of size at most five, and none has a smaller one than stated; sets of size more than five are irrelevant to minimality.

To classify the matchings intrinsically, delete the ten matching edges from \(D\). Cubicity gives a spanning two-factor. The same exhaustive enumeration determines its component cycle lengths, yielding precisely 30 cases \((20)\) and six cases \((5,5,10)\). Crossing the two-factor profile with the minimum deletion counts gives the asserted exact correspondence and polynomial. An independent implementation uses the twenty-cycle LCF representation \([10,7,4,-4,-7,10,-4,7,-7,4]^2\), checks an explicit vertex bijection with \(GP(10,2)\), constructs matchings by a distinct recursion, and separately searches all candidate deletion subsets outside each matching. It reproduces every class count and minimum-set multiplicity.

## Verification
Run `python3 verify_gp.py` and `python3 verify_lcf.py` in a Python 3.9-or-newer standard-library environment. The first checks every edge-deletion set of size at most five globally. The second checks every matching against all allowed nonmatching-edge deletion sets of sizes four and five, independently confirming that sizes zero through three cannot matter because the first program exhaustively proves there is no unique survivor at those sizes. Outputs are supplied in `verify_gp.out` and `verify_lcf.out`. The first also hashes its entire normalized 36-row table: `e34881d9fea638d39521166c53d761f8e950f4b5772bab727e7ea29e9d423e21`. Both scripts terminate normally with `all_verified: true`; the assertions test the stated conclusions and the graph-isomorphism prerequisite.

## Relationship to prior work
Lei, Yeh and Zhang [1] introduced the matching-specific anti-forcing number, including the dodecahedral graph as a counterexample to a nonmatching-edge-disjoint alternating-cycle packing equality outside planar bipartite graphs. That example supplies a lower bound on a particular matching, not the full anti-forcing polynomial or counts of minimum edge-deletion certificates. Yang, Zhang and Lin [2] established that every fullerene has anti-forcing number at least four, and explicitly showed that the dodecahedron attains four. This determines the minimum of the polynomial's exponents but not the upper exponent, its multiplicity, the complementary-cycle distinction, or the counts of minimum sets. The present classification retains those results and adds matching-wise structural and certificate multiplicities. Existing forcing-number results for the dodecahedron concern edges *inside* a matching and are distinct from anti-forcing.

## Limitations
This is a finite, algorithmically exhaustive theorem for one fixed graph. It does not give a uniform formula for larger fullerenes or imply chemical stability statements. The implementations use separate graph representations but are not independent formal proofs. The literature search does not exclude a previously distributed unindexed census, and no external independent audit has been performed.

## References
[1] H. Lei, Y.-N. Yeh and H. Zhang, *Anti-forcing numbers of perfect matchings of graphs*, arXiv:1406.3796v1, publicly posted 2014-06-15, https://arxiv.org/abs/1406.3796.

[2] Q. Yang, H. Zhang and Y. Lin, *On the anti-forcing number of fullerene graphs*, arXiv:1503.01900v1, publicly posted 2015-03-06, https://arxiv.org/abs/1503.01900.
