# Crown-graph defensive alliances: exact local/global minimal censuses and a binomial-square parity law

## Finding

Let \(\operatorname{Cr}_n=K_{n,n}-M\) be the crown graph obtained by deleting a perfect matching, where \(n\ge3\). An ordinary defensive alliance is a **nonempty** vertex set \(S\) such that, for every \(v\in S\),
\[
|N(v)\cap S|+1\ge |N(v)\setminus S|.
\]
It is **locally minimal** if deleting any one selected vertex destroys the alliance property, and **globally minimal** if no nonempty proper subset is an alliance. These are distinct notions; “globally minimal” does **not** mean “global defensive alliance” (which additionally requires domination).

Put \(t=\lfloor(n-1)/2\rfloor\), \(s=t+1\), and adopt the convention \(\binom ab=0\) when \(b\notin\{0,\ldots,a\}\). Define
\[
D_n=\binom nt\binom{n-t}{t},\qquad
H_{n,r}=\binom ns\binom sr\binom{n-s}{s-r}.
\]
If \(L_n(z)\), respectively \(G_n(z)\), enumerates locally, respectively globally, minimal defensive alliances by their number of vertices, then **for every \(n\ge3\)**
\[
\boxed{L_n(z)=D_nz^{2t}+\left(\sum_{r=2}^{s}H_{n,r}\right)z^{2s}},
\]
\[
\boxed{G_n(z)=D_nz^{2t}+\left(\sum_{r=3}^{s}H_{n,r}\right)z^{2s}}.
\]
In particular, the exact number of locally minimal alliances that are **not** globally minimal is
\[
\boxed{B_n=\binom ns\binom s2\binom{n-s}{s-2}}.
\]
Every such exceptional set has exactly two matching indices selected on both shores.

There is a parity-sensitive simplification. For odd \(n=2k+1\), where \(k\ge1\), write \(C=\binom{2k+1}{k+1}\). Then
\[
\boxed{L_{2k+1}(1)=C^2,\qquad G_{2k+1}(1)=C^2-\frac{k^2(k+1)}2C.}
\]
For even \(n=2k\), where \(k\ge2\), write \(C=\binom{2k}k\). Then
\[
\boxed{L_{2k}(1)=C^2-\left(1+\frac{k^2}{2}\right)C,}
\]
\[
\boxed{G_{2k}(1)=C^2-\left(1+\frac{k^2}{2}+\binom k2^2\right)C.}
\]
Thus the number of locally minimal alliances is **exactly the square of a central binomial coefficient at every odd parameter**, but has a nonzero explicit correction at every even parameter. Moreover, a uniformly chosen locally minimal alliance fails global minimality with probability
\[
\frac{B_{2k+1}}{L_{2k+1}(1)}
 =\frac{\sqrt\pi}{4}\frac{k^{7/2}}{4^k}\bigl(1+O(k^{-1})\bigr)
\]
for odd orders, and
\[
\frac{B_{2k}}{L_{2k}(1)}
 =\frac{\sqrt\pi}{4}\frac{k^{9/2}}{4^k}\bigl(1+O(k^{-1})\bigr)
\]
for even orders. Both probabilities tend exponentially to zero.

## Assumptions and scope

Throughout \(n\ge3\). Label the shores \(\{a_i:i\in[n]\}\) and \(\{b_i:i\in[n]\}\); the edge \(a_ib_j\) exists exactly when \(i\ne j\). For a selected set \(S\), write \(X=\{i:a_i\in S\}\), \(Y=\{j:b_j\in S\}\), and \(x=|X|\), \(y=|Y|\), \(r=|X\cap Y|\). All sets and counts are **labeled**; graph automorphisms are not factored out. The polynomial \(G_n\) refers to inclusion-minimality among defensive alliances, not to alliances that dominate the graph.

The complete structural classification is:

* Locally minimal: either \(X\cap Y=\varnothing\) with \(x=y=t\), or \(r\ge2\) with \(x=y=s\).
* Globally minimal: either \(X\cap Y=\varnothing\) with \(x=y=t\), or \(r\ge3\) with \(x=y=s\).

For \(n=3,4\), only the first type is globally minimal. For every \(n\ge5\), both cardinalities \(2t\) and \(2s\) occur among globally minimal alliances.

## Proof

**1. All defensive alliances.** Every vertex has degree \(n-1\). For a selected \(a_i\), the number of selected neighbors is \(y-\mathbf 1_{i\in Y}\). Its defensive requirement is therefore
\[
2(y-\mathbf1_{i\in Y})+1\ge n-1
\quad\Longleftrightarrow\quad
 y-\mathbf1_{i\in Y}\ge\left\lceil\frac{n-2}{2}\right\rceil=t.
\]
The analogous condition for a selected \(b_j\) is \(x-\mathbf1_{j\in X}\ge t\). As \(t\ge1\), an alliance cannot occupy only one shore. If \(r=0\), the requirements reduce precisely to \(x,y\ge t\). If \(r\ge1\), they reduce precisely to \(x,y\ge s\), since some selected vertex on each shore is indexed in the intersection. Thus these two conditions are both necessary and sufficient.

**2. Local minimality.** If \(r=0\), deleting a selected vertex on either shore preserves disjointness. Hence the alliance is locally minimal exactly when \(x=y=t\). If \(r=1\), deleting the \(a_i\) belonging to the unique common index removes the intersection, leaving \(x-1\ge t\), \(y\ge s\ge t\); the result is still an alliance. So \(r=1\) is never locally minimal. If \(r\ge2\) and \(x>s\), deleting a selected \(a_i\) leaves the intersection nonempty and keeps \(x-1\ge s\), \(y\ge s\); similarly \(y>s\) precludes local minimality. Conversely, if \(r\ge2\) and \(x=y=s\), deleting one selected vertex leaves a nonempty intersection but makes the occupancy of its shore \(t<s\), violating the alliance criterion. This proves the asserted local classification.

**3. Global minimality.** Every globally minimal alliance is locally minimal. A disjoint local-minimal alliance with \(x=y=t\) has no defensive proper subset: a subset occupying both shores would have one occupancy less than \(t\), and a subset on one shore alone cannot be defensive. Consider a local-minimal alliance with \(r\ge2\) and \(x=y=s\). Any proper defensive subset that still has a common index would require at least \(s\) vertices from each shore and hence be the original set. A disjoint defensive subset would require at least \(t=s-1\) vertices from each shore, so at most one vertex could have been removed from each shore. To eliminate all \(r\) common indices requires at least \(r\) deletions. If \(r\ge3\), this is impossible. If \(r=2\), deleting an \(a\)-vertex from one common index and a \(b\)-vertex from the other leaves a disjoint defensive subset with exactly \(t\) selected vertices per shore. Thus the overlap type is globally minimal **exactly when \(r\ge3\)**.

**4. Enumeration.** The disjoint type is counted by first choosing \(X\) of size \(t\), then choosing \(Y\) of size \(t\) in its complement: this gives \(D_n\). For overlapping \(x=y=s\) with exactly \(r\) common indices, first choose \(X\) of size \(s\), then the \(r\) common indices within \(X\), and finally the other \(s-r\) indices of \(Y\) outside \(X\). This gives \(H_{n,r}\). Both polynomial identities and \(B_n=H_{n,2}\) follow immediately.

**5. Parity identities.** Let \(C=\binom ns\). The number of all ordered pairs \((X,Y)\) with \(x=y=s\) is \(C^2\). For \(n=2k+1\), \(s=k+1\), and there are no disjoint such pairs; exactly \(C(k+1)\) have intersection size one. Meanwhile \(D_n=C(k+1)\), so the singleton-intersection exclusion is exactly compensated by the disjoint local-minimal configurations. Thus \(L_{2k+1}(1)=C^2\). Furthermore \(B_n=\frac{k^2(k+1)}2C\).

For \(n=2k\), \(s=k\). Exactly \(C\) pairs have empty intersection and \(Ck^2\) have intersection size one; the disjoint type contributes \(D_n=Ck^2/2\). Therefore \(L_{2k}(1)=C^2-C(1+k^2/2)\). The local-only contribution is \(B_n=C\binom k2^2\), proving the remaining formulas. Finally, Stirling's formula \(\binom{2k}k=\frac{4^k}{\sqrt{\pi k}}(1+O(k^{-1}))\) and \(\binom{2k+1}{k+1}=\frac{2\cdot4^k}{\sqrt{\pi k}}(1+O(k^{-1}))\) yield the two stated probability asymptotics. No limiting interchange beyond these exact finite identities is needed.

## Verification

The bundled standalone `verify.py` independently constructs all crown-graph adjacency masks rather than using the intersection criterion as its test oracle. It exhaustively checks all nonempty vertex subsets for each \(3\le n\le10\), evaluates the defensive inequality at every selected vertex, tests single-deletion minimality, and computes the existence of **any** defensive proper subset by dynamic subset recursion. It verifies both size polynomials, the structural classification, the exact local-only count, and the parity-specific total formula.

Run `python verify.py` in the directory containing the bundled source. The observed final line was:

`VERIFY_OK graph_orders=8 tested_nonempty_subsets=1398072 all_formulas_agree=true`

Finite enumeration is corroboration; the proof above establishes the all-parameter statements.

## Relationship to prior work

Bazgan, Fernau, and Tuza developed local/global minimal defensive alliances and studied upper parameters and complexity. Gaikwad and Maity subsequently investigated globally minimal alliances algorithmically, while Gaikwad, Maity, and Saurabh addressed the locally minimal version. Feng, Fernau, and Mann studied enumeration algorithms for both notions and gave explicit counts for certain trees. Ibrahim introduced the bivariate defensive-alliance polynomial, which counts **connected** induced vertex sets by order and a minimum-degree-balance statistic; the complete-bipartite specialization is not a formula for inclusion-minimal defensive alliances of crown graphs. None of these inspected treatments supplies the above crown-graph local/global structural classification, the two exact polynomials, or the parity-sensitive binomial-square identity.

The crown graph is the complete bipartite graph minus a perfect matching, not a complete multipartite graph of the ordinary kind for \(n\ge3\). Hence results about strong defensive alliances in complete multipartite graphs do not imply the ordinary defensive-alliance census here. Likewise, global **offensive** alliance formulas and ordinary domination counts are different conditions. The result should be understood as a direct structural refinement for a canonical regular bipartite family, not a claim that the general algorithmic questions have been resolved.

## Limitations

No theorem about all bipartite graphs is asserted. The asymptotic statement concerns uniformly chosen **locally minimal** alliances on crown graphs, not uniformly chosen arbitrary alliances. The graph family and ordinary defensive inequality must not be replaced by strong defensive or global-domination variants. Priority is not independently established; an older result under an unsearched name remains possible. The computation does not constitute an infinite or independent proof.

## References

1. C. Bazgan, H. Fernau, Zs. Tuza, “Aspects of upper defensive alliances,” *Discrete Applied Mathematics* 266 (2019), 111–120; available online 30 June 2018. https://doi.org/10.1016/j.dam.2018.05.061 ; author's full text https://www.lamsade.dauphine.fr/~bazgan/Papers/DAM19a.pdf
2. A. Gaikwad, S. Maity, “Globally Minimal Defensive Alliances: A Parameterized Perspective,” arXiv:2202.02010 (first posted 4 February 2022), https://arxiv.org/abs/2202.02010
3. A. Gaikwad, S. Maity, S. Saurabh, “Parameterized Algorithms for Locally Minimal Defensive Alliance,” arXiv:2208.03491 (first posted 6 August 2022), https://arxiv.org/abs/2208.03491
4. Z. Feng, H. Fernau, K. Mann, “Enumerating Minimal Defensive Alliances,” arXiv:2312.11963 (first posted 19 December 2023), https://arxiv.org/abs/2312.11963
5. H. Ibrahim, “Defensive alliance polynomial,” arXiv:1811.10089 (first posted 25 November 2018), https://arxiv.org/abs/1811.10089 .
