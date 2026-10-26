# Sharp diameter of the 321-avoiding adjacent-swap graph

## Finding

For each integer \(n\ge 1\), let \(G_n\) have one vertex for each permutation of \(1,\ldots,n\) with no indices \(i<j<k\) such that \(\pi_i>\pi_j>\pi_k\). Two vertices are adjacent exactly if they differ by a swap of consecutive positions and both are 321-avoiding. For \(u,v\in G_n\), write \(\ell(u)\) for the inversion number, and \(u\wedge v\) for their meet in right weak order. Then

\[
d_{G_n}(u,v)=\ell(u)+\ell(v)-2\ell(u\wedge v).
\]

In particular the sharp diameter, for every \(n\ge1\), is

\[
\operatorname{diam}(G_n)=
\begin{cases}
(n^2-1)/2 &\text{if }n\text{ is odd},\\
n^2/2-1 &\text{if }n\text{ is even}.
\end{cases}
\]

For \(n\ge3\), this exceeds the diameter \(n(n-1)/2\) of the unrestricted adjacent-swap permutohedron by \((n-1)/2\) when \(n\) is odd and by \(n/2-1\) when \(n\) is even.

## Assumptions and scope

The forbidden pattern is a *classical*, not consecutive, three-term pattern. An adjacent swap interchanges positions, not arbitrary values. Weak order is the **right weak order** in the convention that its covers are \(w\lessdot ws_i\) when the inversion number increases by one, with \(s_i\) interchanging positions \(i,i+1\). The identity is its minimum element. Graph distance counts undirected permitted adjacent swaps. The meet \(u\wedge v\) exists in the full weak-order lattice and belongs to the avoidance class, as shown below.

Write \(T_q=(q+1,q+2,\ldots,n,1,2,\ldots,q)\) for \(0\le q<n\), with either block allowed to be empty. Its inversion number is \(q(n-q)\). If \(n=1\), the sole vertex has diameter zero; the following argument includes this boundary case.

## Proof

**1. A metric lemma.** Let \(L\) be a finite graded meet-semilattice with minimum, in which each principal interval \([\hat0,x]\) is a distributive lattice. Let \(J\) be the set of elements of \(L\) having exactly one lower cover and set \(I(x)=\{j\in J:j\le x\}\). All lower covers of \(j\le x\) are still in \([\hat0,x]\), so the join-irreducibles of the distributive interval \([\hat0,x]\) are precisely \(J\cap[\hat0,x]\). Birkhoff's ideal representation theorem gives \(\lvert I(x)\rvert=\operatorname{rk}(x)\). Moreover, \(I(x)\cap I(y)=I(x\wedge y)\). For a cover \(x\lessdot y\), inclusion \(I(x)\subset I(y)\), together with the rank difference of one, shows exactly one membership coordinate changes. Hence every path between \(x\) and \(y\) in the undirected cover graph has length at least

\[
\lvert I(x)\mathbin{\triangle}I(y)\rvert
=\operatorname{rk}(x)+\operatorname{rk}(y)-2\operatorname{rk}(x\wedge y).
\]

A saturated descent from \(x\) to \(x\wedge y\), followed by a saturated ascent to \(y\), is a path attaining this bound. This proves the metric lemma (a standard consequence of the distributive-interval structure).

**2. Application to avoidance.** By the fully commutative characterization in type \(A\), a permutation avoids 321 exactly when it is fully commutative. Every weak-order predecessor of a fully commutative element is fully commutative: a reduced expression of the predecessor is a prefix of a reduced expression of its successor; a noncommutation braid in the predecessor's reduced words would also occur in a reduced expression of the successor. Therefore these permutations form a lower order ideal \(L_n\) in right weak order. The full weak order of the finite symmetric group is a lattice, so \(L_n\) inherits meets. Stembridge's distributive-interval theorem for fully commutative elements identifies each \([e,w]\) with the order-ideal lattice of the heap of a reduced expression for \(w\). Thus \(L_n\) fulfills the metric lemma. Its rank is the inversion count, and its undirected Hasse diagram is exactly \(G_n\). This proves the displayed distance formula.

**3. Extremal inversion rank and its rigidity.** A 321-avoiding permutation may be partitioned into two increasing subsequences, of respective sizes \(a,b\), because its longest decreasing subsequence has length at most two. Every inversion crosses these two subsequences, so \(\ell(w)\le ab\le M_n:=\lfloor n^2/4\rfloor\). Equality requires balanced sizes and inversion of every cross-subsequence pair. To see the latter forces a two-block form, label the increasing subsequence containing the first position \(A\) and the other \(B\). The first entry \(a_1\) precedes every \(B\)-entry, hence is larger than every \(B\)-entry. Any later \(A\)-entry after a \(B\)-entry would be even larger than \(a_1\), making that cross pair a non-inversion. Therefore all entries of \(A\) precede all entries of \(B\), with all \(A\)-values larger than all \(B\)-values. Both subsequences must be increasing. Consequently the rank maximizers are exactly \(T_q\) with \(q(n-q)=M_n\): one maximizer if \(n\) is even and two if \(n>1\) is odd.

**4. Sharp pairs.** The simple weak-order atoms below \(T_q\), for \(1\le q<n\), consist of the single adjacent-value transposition \(s_q\). Indeed \(T_q\) inverts the consecutive values \(q,q+1\), and no other consecutive-value pair. For \(q=0\), \(T_q=e\) has no atom. A nonidentity weak-order element has at least one atom below it. Hence \(T_p\wedge T_q=e\) whenever \(p\ne q\): their common lower bound cannot contain an atom. If \(n=2k+1\ge3\), use \(T_k,T_{k+1}\), both of rank \(M_n=k(k+1)\). Their distance is \(2M_n=(n^2-1)/2\), and any pair has distance at most the sum of its two ranks, hence at most \(2M_n\). When \(n=2k\ge2\), use \(T_k,T_{k-1}\), having ranks \(k^2\) and \(k^2-1\), with meet \(e\); their distance is \(2k^2-1\). Since \(T_k\) is the **unique** maximum-rank permutation, two different vertices cannot both have rank \(k^2\). Thus every distinct pair has distance at most \(2k^2-1\); identical vertices have distance zero. The cases \(n=1\) and \(n=2\) agree with the formula. This proves the sharp diameters. \(\square\)

## Verification

Run \(`python3 verify_catalan_diameter.py`\) using Python 3.8 or later. The bundled implementation enumerates all 321-avoiding permutations for each \(1\le n\le8\), constructs every permitted adjacent swap, checks lower-cover ranks and all join-irreducible masks, then performs breadth-first search from **every** vertex and compares **every** distance with the derived Hamming metric. It verifies diameters \(0,1,4,7,12,17,24,31\) and finishes with `VERIFY_OK`. The program is a finite cross-check, not a substitute for the proof for arbitrary \(n\).

## Relationship to prior work

Stembridge (1996), especially the fully commutative characterization and distributivity of weak-order principal intervals, provides the critical structural premise. The general metric lemma is an elementary consequence of Birkhoff's representation for distributive lattices and is not itself asserted as a new theorem. Cheng, Elizalde, Kasraoui and Sagan (arXiv 2011) study inversion distributions in the same 321-avoidance class. Gunawan, Pan, Russell and Tenner (2022) study the weak order and RSK data of fully commutative permutations. None of the inspected material states the parity-sharp diameter for the induced adjacent-swap graph, identifies its extremal pair obstruction, or gives this entire graph's distance formula as an object-specific result. The main contribution is the **sharp diameter and extremizer argument**, not the antecedent distributive-order technology. A precise prior implication check remains subject to unindexed sources.

## Limitations

The result concerns only 321-avoidance, swaps of adjacent positions, and ordinary graph distance. It does not classify geodesics or other pattern classes. A targeted literature search did not locate an earlier identical diameter theorem, but absence from search results does not prove priority. The standalone enumerations cover \(n\le8\), whereas the proof covers every positive integer.

## References

1. J. R. Stembridge, *On the Fully Commutative Elements of Coxeter Groups*, Journal of Algebraic Combinatorics **5** (1996), 353–385. DOI: `10.1007/BF00193185`. In particular Theorem 3.2 and its heap interpretation.
2. S.-E. Cheng, S. Elizalde, A. Kasraoui and B. Sagan, *Inversion polynomials for 321-avoiding permutations*, arXiv:`1112.6014` (first version posted 2011-12-27).
3. R. P. Stanley, *Enumerative Combinatorics, Vol. 1*, second edition; distributive-lattice ideal representation and inversion/weak-order background.
4. M. Gunawan, B. Pan, H. Russell and B. E. Tenner, *RSK tableaux and the weak order on fully commutative permutations*, arXiv:`2212.05002` (2022).
