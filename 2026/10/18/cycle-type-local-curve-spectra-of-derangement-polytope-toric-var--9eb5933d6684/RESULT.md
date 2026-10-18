# Cycle-type local curve spectra of derangement-polytope toric varieties

## Finding

Let \(D_n\) be the derangement face of the Birkhoff polytope. Its normal-fan projective toric variety has a torus-fixed point \(p_\sigma\) for each derangement \(\sigma\in S_n\). For every \(n\ge3\), the complete distribution of torus-invariant curves incident at \(p_\sigma\), refined by the number of permutation indices changed by their endpoints, is determined solely by the cycle type \(\lambda=(\ell_1,\ldots,\ell_r)\) of \(\sigma\), with each \(\ell_i\ge2\).

For an integer \(\ell\ge2\), set
\[
 L_\ell(X,Y)=1+\sum_{s=1}^{\ell-1}\sum_{h=1}^{\min(s,\ell-s)}(-1)^s\frac{\ell}{h}\binom{s-1}{h-1}\binom{\ell-s-1}{h-1}X^{s+h}Y^h.
\]
Define \(C_\lambda(v,h)=[X^vY^h]\prod_{i=1}^r L_{\ell_i}(X,Y)\). Then the length-refined local curve-degree polynomial is
\[
 \boxed{\mathcal D_\lambda(T)=
 \sum_{v,h}C_\lambda(v,h)
 \sum_{\substack{0\le m\le n-v\\v+m\ge2,\;h+m\ge1}}
 \binom{n-v}{m}(h+m-1)!\,T^{v+m}
 +\sum_{i=1}^r(-1)^{\ell_i}T^{\ell_i}.}
\]
Its \(T^q\)-coefficient is the number of such incident curves with a changed support of size \(q\); evaluation at \(T=1\) is the full number of incident curves. Here factorials are evaluated only on nonnegative arguments. The sum includes the \((v,h)=(0,0)\) term.

In particular, \(D_n\) has dimension \(n^2-3n+1\), and \(p_\sigma\) is singular for every derangement \(\sigma\) when \(n\ge4\). For \(n=3\), \(D_3\) is a segment and \(X_3\simeq\mathbb P^1\). If \(m_j\) denotes the multiplicity of part size \(j\) in \(\lambda\), then the number of edges of \(D_n\) is exactly
\[
 \frac12\sum_{\substack{\lambda\vdash n\\\text{all parts}\ge2}}\frac{n!}{\prod_{j\ge2}j^{m_j}m_j!}\,\mathcal D_\lambda(1).
\]

## Assumptions and scope

Fix an algebraically closed field \(k\) of arbitrary characteristic and \(n\ge3\). The polytope is
\[
 D_n=\bigl\{(x_{ij})\in\mathbb R_{\ge0}^{n\times n}:\sum_jx_{ij}=\sum_ix_{ij}=1,\;x_{ii}=0\bigr\}.
\]
The toric variety is the normal projective variety determined by the **normal fan** of \(D_n\). Torus-fixed points and invariant curves correspond respectively to vertices and edges of \(D_n\). An edge has support length \(q\) when its endpoint permutations differ on precisely \(q\) indices. The claim is about torus-fixed local curve incidence, not the entire singular locus or the scheme structure of singularities.

## Proof

**Vertices and dimension.** The intersection \(D_n\) is a face of the Birkhoff polytope, hence its vertices are exactly the derangement permutation matrices. The off-diagonal constant matrix with entries \(1/(n-1)\) is strictly positive on the edges of the connected crown graph \(K_{n,n}\) with one perfect matching removed. The bipartite incidence constraints have rank \(2n-1\), so the dimension equals \(n(n-1)-(2n-1)=n^2-3n+1\).

**Adjacency.** For two perfect matchings of a bipartite graph, their union decomposes into vertex-disjoint alternating even cycles. Their minimal containing face has one independent segment factor per alternating cycle. Therefore two distinct derangement permutations \(\sigma,\tau\) are adjacent if and only if \(c=\sigma^{-1}\circ\tau\) has precisely one nontrivial permutation cycle. This is also the applicable specialization of the general perfect-matching polytope adjacency criterion (Behrend, Corollary 26).

**Forbidden arcs.** Fix \(\sigma\) and write \(\tau=\sigma\circ c\). On the changed support \(S\), \(c\) is a cyclic permutation. The condition that \(\tau\) has no fixed point is exactly \(c(i)\ne\sigma^{-1}(i)\) for all \(i\in S\). Consequently the prohibited directed arcs \(i\to\sigma^{-1}(i)\) form disjoint directed cycles with lengths \(\ell_1,\ldots,\ell_r\).

**Proper forbidden-arc sets.** In inclusion-exclusion, choose a set \(E\) of prohibited arcs that does not contain an entire directed \(\sigma\)-cycle. Its components are \(h\) disjoint directed paths and isolated vertices. If \(s\) arcs were chosen, the number of vertices involved is \(v=s+h\). On a forbidden cycle of length \(\ell\), the number of proper arc subsets with \(s\) selected arcs distributed into \(h\) cyclic runs is
\[
 \frac\ell h\binom{s-1}{h-1}\binom{\ell-s-1}{h-1},
 \qquad 1\le h\le\min(s,\ell-s).
\]
Indeed, mark a first selected run, cyclically arrange \(h\) positive selected-run lengths summing to \(s\) and \(h\) positive gap lengths summing to \(\ell-s\), choose its initial vertex in \(\ell\) ways, then divide by \(h\) choices of marked run. Multiplying the signed run polynomials over the disjoint forbidden cycles gives \(C_\lambda(v,h)\).

**Counting cyclic extensions.** Contract each of the \(h\) selected directed paths to a block. Choose \(m\) additional vertices among the \(n-v\) vertices not incident to \(E\). There are \(h+m\) distinct blocks, and exactly \((h+m-1)!\) cyclic permutations of those blocks, provided \(h+m\ge1\). The total changed support is \(q=v+m\ge2\). This proves the double-sum contribution to \(\mathcal D_\lambda\), including the empty forbidden-arc set with \(h=v=0\).

**Entire forbidden cycles.** An inclusion-exclusion selection containing a complete prohibited directed cycle can be contained in an admissible cyclic permutation only when the selected set is *exactly* that complete cycle. It then forces the sole cyclic permutation equal to \(\sigma^{-1}\) restricted to that cycle. Its signed contribution is \((-1)^\ell T^\ell\), once for each prohibited cycle. Adding these terms yields the stated polynomial. The coefficient counts incident edges because each admissible cyclic permutation \(c\) gives a unique adjacent derangement \(\tau\).

**Smooth-point cutoff.** A smooth torus-fixed point of a dimension-\(d\) normal toric variety is represented by a unimodular full-dimensional normal cone, hence has exactly \(d\) incident invariant curves. For \(n=4\), the two derangement cycle types have degrees \(7\) and \(6\), exceeding \(d=5\); for \(n=5\), they have degrees \(33\) and \(31\), exceeding \(d=11\). For \(n\ge6\), among all transposition cycles \(c\), at most \(n\) are excluded by the \(n\) forbidden arcs, yielding at least \(\binom n2-n\) incident curves. Likewise, each forbidden arc belongs to exactly \(n-2\) oriented three-cycles, so at least \(2\binom n3-n(n-2)\) three-support curves remain. Thus
\[
 \deg(p_\sigma)\ge \binom n2-n+2\binom n3-n(n-2)=\frac{n(n-1)(2n-7)}6>n^2-3n+1
\]
for all \(n\ge6\). All normal cones at fixed points are therefore nonsimplicial, so these points are singular. For \(n=3\), there are precisely two derangements and one edge, hence \(X_3\simeq\mathbb P^1\).

Finally, permutations of a given cycle type \(\lambda\) occur with multiplicity \(n!/(\prod_{j\ge2}j^{m_j}m_j!)\). Summing the degrees and dividing by two counts the unoriented edges of \(D_n\).

## Verification

Run `python3 checker.py` using the Python standard library. It independently enumerates all cyclic permutations on changed supports for every derangement cycle type and each \(3\le n\le8\), compares these counts coefficient-by-coefficient with the inclusion-exclusion formula, and then directly enumerates adjacent derangement pairs for \(n\le6\). The program prints `VERIFY_OK` if every comparison passes. Total edge counts for \(n=3,4,5,6,7,8\) are respectively \(1,30,706,20770,835311,44963716\). Degrees by cycle type include \(n=4\): \((4)\mapsto7\), \((2,2)\mapsto6\); and \(n=6\): \((6)\mapsto160\), \((4,2)\mapsto151\), \((3,3)\mapsto167\), \((2,2,2)\mapsto138\). Finite enumeration corroborates but does not prove the all-parameter statement; the preceding argument supplies that proof.

## Relationship to prior work

Behrend's 2013 theory of fractional perfect \(b\)-matching polytopes includes a general face/adjacency criterion encompassing the present crown-graph matching polytope. That criterion establishes how to recognize an edge, but the inspected parts of that article do not provide the run-weighted cycle-type generating polynomial, the full changed-support spectra, or the sharp toric fixed-point regularity cutoff. Davis and Sagan's work on pattern-avoiding permutation and Birkhoff polytopes concerns distinct avoidance-defined subpolytopes; the word “derangement” there refers to another enumeration, not the diagonal-zero Birkhoff face. Abreu, Costa, do Nascimento and Patuzzi give a general degree formula for the polytope of *all* matchings of an arbitrary graph, in terms of alternating paths and cycles. The perfect-matching subface here only retains alternating-cycle edges; their general criterion does not state the explicit cycle-type-refined run polynomial. Related published degree formulas for rectangular doubly substochastic *partial*-matching polytopes concern different objects and do not imply this cycle-type refinement.

## Limitations

The classification is of invariant curves **incident at torus-fixed points**, not of every singular stratum or its local analytic type. The polynomial gives ordinary edge degrees, not affine divisor class groups. The fixed-point nonsmoothness deduction uses excess edge incidence as a necessary smoothness obstruction, not a converse. Although targeted literature comparisons did not uncover this particular formula, an equivalent enumeration under different terminology or in unindexed literature remains possible; independent mathematical audit has not been performed.

## References

1. R. E. Behrend, *Fractional Perfect b-Matching Polytopes. I: General Theory*, arXiv:1301.7356, version 1 first public 2013-01-30. Particularly the face and adjacency criteria in Sections 7–8, including Corollary 26.
2. R. Davis and B. Sagan, *Pattern-Avoiding Polytopes*, arXiv:1609.01782, version 1 first public 2016-09-06.
3. N. Abreu, L. Costa, C. H. do Nascimento, and L. Patuzzi, *On the vertex degrees of the skeleton of the matching polytope of a graph*, arXiv:1701.06210, version 1 first public 2017-01-22, particularly Theorem 2.3.
