# Rank distribution of self-inverse partial isometries of finite cycles

## Finding
For every integer \(n\ge4\), let \(C_n\) be the undirected cycle with vertex set \(V_n=\mathbb Z/n\mathbb Z\), equipped with graph distance. Write \(\operatorname{PIso}(C_n)\) for the inverse monoid of all distance-preserving partial bijections between subsets of \(V_n\), including the empty map. A *self-inverse* element is a partial bijection \(\alpha\) whose inverse partial bijection equals \(\alpha\); this includes partial identities. Define its rank polynomial by
\[
J_n(z)=\sum_{\substack{\alpha\in\operatorname{PIso}(C_n)\\\alpha=\alpha^{-1}}}z^{|\operatorname{dom}\alpha|}.
\]
The complete, all-rank formula is
\[
\boxed{J_n(z)=
\begin{cases}
(1+z)^n+n(1+z)(1+z^2)^{(n-1)/2}-n(1+z),&n\text{ odd},\\[3pt]
(1+z)^n+\dfrac n2(1+z)^2(1+z^2)^{(n-2)/2}
+\left(\dfrac n2+1\right)(1+z^2)^{n/2}-(n+1)-nz-nz^2,&n\text{ even}.
\end{cases}}
\]
In particular, \(J_n(0)=1\), the coefficients of \(z\) and \(z^2\) are respectively \(n\) and \(n(n-1)\), and the leading coefficient counts the global dihedral involutions: \(n+1\) for odd \(n\), \(n+2\) for even \(n\). At \(z=1\), the exact totals are
\[
J_n(1)=\begin{cases}
2^n+n\bigl(2^{(n+1)/2}-2\bigr),&n\text{ odd},\\
2^n+\left(\dfrac{3n}{2}+1\right)2^{n/2}-3n-1,&n\text{ even}.
\end{cases}
\]
The \(2^n\) partial identity maps therefore account for an asymptotic proportion tending to \(1\) of the self-inverse elements as \(n\to\infty\). These assertions all describe the same rank distribution and its immediate evaluations.

## Assumptions and scope
The graph distance is \(d(i,j)=\min(|i-j|,n-|i-j|)\), using representatives in \(\{0,\ldots,n-1\}\). A partial isometry is a bijection \(\alpha:D\to E\) between subsets such that \(d(\alpha(i),\alpha(j))=d(i,j)\) for all \(i,j\in D\). The inverse \(\alpha^{-1}:E\to D\) is the ordinary inverse bijection. The condition \(\alpha=\alpha^{-1}\) means \(D=E\) and \(\alpha^2=\operatorname{id}_D\), not merely that its square is idempotent or that it is an involution of the group of units. The empty partial map is included. All ranks are cardinalities of domains, ranging from \(0\) to \(n\). There is no prime, parity, or size restriction beyond \(n\ge4\).

## Proof
**1. Unique dihedral extension from rank three.** Fernandes and Paulista [1, Lemma 1.1] prove that every element of \(\operatorname{PIso}(C_n)\) is a restriction \(g|_D\) of some \(g\) in the dihedral group \(D_{2n}\) acting on the \(n\) cycle vertices, and that this extension is unique whenever \(|D|\ge3\). The uniqueness threshold is essential. It can be seen directly from their metric argument: a distance-preserving map on a nonantipodal ordered pair of distinct vertices determines a unique dihedral symmetry; three distinct vertices always contain such a pair, and their distance relations force the images of every remaining vertex. At two antipodal vertices when \(n\) is even, two ambient symmetries may give the same restriction. No other rank-at-least-two ambiguity occurs.

**2. Restriction criterion for self-inverses in rank at least three.** Let \(|D|\ge3\) and \(\alpha=g|_D\). If \(\alpha=\alpha^{-1}\), then its domain equals its image, so \(g(D)=D\), and \(g^2\) fixes every point of \(D\). Every nonidentity dihedral permutation fixes at most two vertices (a nontrivial rotation fixes none, and a reflection fixes at most two). Thus \(g^2=1\) globally. Conversely, if \(g^2=1\) and \(g(D)=D\), then \(g|_D\) is self-inverse. Since the ambient extension is unique in these ranks, distinct pairs \((g,D)\) contribute distinct partial maps when \(|D|\ge3\).

**3. Cycle-polynomial count of globally involutive symmetries.** For a permutation \(g\) with \(g^2=1\), let \(f(g)\) be its number of fixed points and \(t(g)\) its number of transpositions. A subset is \(g\)-invariant precisely when it is a union of cycles of \(g\). Its subset-size enumerator is therefore \((1+z)^{f(g)}(1+z^2)^{t(g)}\). The identity contributes \((1+z)^n\). If \(n\) is odd, the other group involutions are the \(n\) reflections, each with one fixed point and \((n-1)/2\) transpositions. If \(n=2m\), exactly \(m\) vertex-axis reflections have two fixed points and \(m-1\) transpositions; the other \(m\) reflections, together with the half-turn rotation, have no fixed points and \(m\) transpositions. Consequently the sum over all group involutions is
\[
F_n(z)=\begin{cases}
(1+z)^n+n(1+z)(1+z^2)^{(n-1)/2},&n\text{ odd},\\
(1+z)^n+m(1+z)^2(1+z^2)^{m-1}+(m+1)(1+z^2)^m,&n=2m.
\end{cases}
\]
By step 2, \(F_n\) and \(J_n\) have the same coefficients at every rank \(3,4,\ldots,n\).

**4. Low-rank correction.** There is exactly one empty partial map. There are \(n\) self-inverse singleton partial maps, all partial identities. For each unordered two-vertex subset there are exactly two self-inverse partial isometries on that subset: its identity and its swap, since either map preserves its sole pairwise distance. Thus the coefficients of ranks \(0,1,2\) in \(J_n\) are \(1,n,2\binom n2\).

When \(n\) is odd, the corresponding coefficients in \(F_n\) are \(n+1,2n,2\binom n2\), so \(J_n=F_n-n-nz\). When \(n=2m\), they are \(n+2,2n,2\binom n2+n\). Indeed, at degree two the vertex-axis contribution is \(m\bigl(1+(m-1)\bigr)=m^2\), the fixed-point-free contribution is \(m(m+1)\), and the identity contributes \(\binom n2\). Therefore \(J_n=F_n-(n+1)-nz-nz^2\). This proves both polynomial formulas, with every boundary rank accounted for.

**5. Evaluations.** Substituting \(z=0\), extracting the first two nonzero coefficients, and extracting the top coefficient yield the stated exact rank boundaries. Setting \(z=1\) gives the two exact totals. Subtracting the \(2^n\) partial identities leaves \(O(n2^{n/2})\) self-inverse elements, while the total is at least \(2^n\); hence their proportion among self-inverse elements tends to one.

## Verification
The accompanying standalone Python 3 program `checks/verify.py` constructs self-inverse partial permutations directly, checks pairwise graph-distance preservation, and compares the complete rank vectors against the formulas for every \(n\) from \(4\) through \(9\). This route does **not** use the dihedral extension theorem. It also enumerates **all** metric partial injections and compares that entire set with all deduplicated dihedral restrictions for \(4\le n\le7\), directly testing the cited extension lemma in bounded cases. Independently, it deduplicates restrictions of every dihedral symmetry and checks the self-inverse rank vector for \(4\le n\le12\). All tests print `VERIFY_OK` after their assertions pass. For \(n=4,5,6,7,8,9\), the full rank vectors are, respectively,
\[
(1,4,12,8,6),\quad (1,5,20,20,10,6),\quad
(1,6,30,32,36,12,8),
\]
\[
(1,7,42,56,56,42,14,8),\quad
(1,8,56,80,124,80,64,16,10),\quad
(1,9,72,120,180,180,120,72,18,10).
\]
The program is supplementary finite corroboration; the preceding proof establishes the result for all \(n\ge4\).

## Relationship to prior work
Fernandes and Paulista [1, Lemma 1.1] establish the crucial dihedral-restriction and extension-uniqueness theorem; [1, Theorem 1.4] counts *all* partial isometries without imposing self-inverseness. Thus the main structural input is known. The new enumerator isolates the self-inverse restriction locus, tracks every possible domain size, and repairs the nonunique low-rank representations differently for odd and even cycles. Standard cycle-type counting supplies the group-level terms but does not by itself perform the partial-map deduplication. Dimitrova, Fernandes, Koppitz, and Quinteiro [2] enumerate and study Green relations/ranks of three proper submonoids; [3] provides presentations for those submonoids. Their results do not state or imply this exact whole-monoid self-inverse rank distribution. A separate rank-and-nilpotency-index enumeration for partial isometries of cycles concerns elements whose powers become the empty map; except for the empty partial map, none can be self-inverse, so that distribution does not determine this one.

## Limitations
The formula counts self-inverse elements, including all idempotent partial identities; it does **not** count only group elements of exact order two, nor classify their multiplication or centralizers. Its ambient extension lemma is borrowed from [1], not reproved from first principles here. The cycle-type calculation is classical, and originality is claimed only for this exact domain-rank distribution and its low-rank correction, not for the general counting method. Finite checks do not certify the universal statement. The exact enumeration may have appeared in unindexed specialist work or the related 2022 master's thesis, for which complete online text was not located during the comparison.

## References
[1] V. H. Fernandes and T. Paulista, *On the monoid of partial isometries of a cycle graph*, arXiv:2205.02196v1 (first public posting 2022-05-04); Turkish Journal of Mathematics **47** (2023), 1746–1760, DOI:10.55730/1300-0098.3460. Full lawful preprint: https://arxiv.org/pdf/2205.02196.

[2] I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *On three submonoids of the dihedral inverse monoid on a finite set*, arXiv:2301.01519 (first posted 2023-01-04), https://arxiv.org/pdf/2301.01519.

[3] I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *Presentations for three remarkable submonoids of the dihedral inverse monoid on a finite set*, arXiv:2301.02474 (first posted 2023-01-06), https://arxiv.org/pdf/2301.02474.
