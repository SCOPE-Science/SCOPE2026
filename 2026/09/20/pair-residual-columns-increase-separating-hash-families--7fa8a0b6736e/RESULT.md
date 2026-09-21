# Pair-residual columns increase for separating hash families

## Statement

Let \(T=\{w_1,\ldots,w_r\}\) with \(r\ge 2\), every \(w_i\ge 1\), and
\[
W=\sum_{i=1}^r w_i\ge 3.
\]
An \(\operatorname{SHF}(N;n,m,T)\) is an \(N\times n\) array on at most \(m\) symbols such that, for every choice of pairwise disjoint column sets
\(C_1,\ldots,C_r\) with \(|C_i|=w_i\), some row has pairwise disjoint symbol sets on
\(C_1,\ldots,C_r\).

For \(1\le i<j\le r\), define the **pair residual**
\[
T_{ij}
=
\{w_1,\ldots,w_i-1,\ldots,w_j-1,\ldots,w_r\},
\]
with zero parts deleted. A hash family is **pair-residual for \(T\)** if it is simultaneously an SHF of every distinct type \(T_{ij}\). A one-part residual imposes no separation condition, but the array is taken to have at least one row.

### Theorem (pair-residual columns increase)

Assume \(n\ge W\), \(2\le x\le m-1\), and that

- \(A\) is an \(\operatorname{SHF}(N_A;n,m,T)\);
- \(B\) is an \(N_B\times(n-1)\) hash family on at most \(m-x\) symbols that is pair-residual for \(T\).

Then there exists an
\[
\operatorname{SHF}(N_A+N_B;\ n+x-1,\ m,\ T).
\]

Thus the auxiliary ingredient has total residual strength \(W-2\), rather than the original strength \(W\), although it must handle the compound collection of pair residuals.

## Construction

Choose one source column of \(A\). In the top block, keep the other \(n-1\) columns and replace the source column by \(x\) identical copies. These \(x\) columns will be called **special columns**.

Relabel the alphabet of \(B\), if necessary, into \(m-x\) symbols of the ambient \(m\)-symbol alphabet. In the bottom block, place \(B\) under the \(n-1\) ordinary columns. Under the \(x\) special columns place \(x\) distinct constant symbols
\[
\alpha_1,\ldots,\alpha_x
\]
that are not used by \(B\). The resulting array has \(n+x-1\) columns and uses at most \(m\) symbols in every row.

## Proof

Fix pairwise disjoint target classes \(C_1,\ldots,C_r\) with \(|C_i|=w_i\).

### Case 1: special columns meet at most one target class

If no special column is selected, the original \(A\) already separates the target classes.

Otherwise suppose exactly one target class, say \(C_i\), contains special columns, and let it contain \(s\ge1\) of them. Project all \(s\) selected special columns to the single source column of \(A\). The projected \(i\)-th class then has \(w_i-s+1\) distinct columns, while all other classes retain their original sizes.

The projected classes occupy \(W-s+1\) distinct columns of \(A\). Since \(n\ge W\), there are at least \(s-1\) unused columns, so the projected \(i\)-th class can be padded to size \(w_i\) without touching the other classes. A row of \(A\) separates these padded classes. In the constructed top block the \(s\) special columns all carry the source-column symbol; they all belong to the same target class, so this repetition is harmless. Hence the original \(C_1,\ldots,C_r\) are separated.

### Case 2: special columns meet at least two target classes

Choose two target classes \(C_i,C_j\) that each contain a special column. Let \(D_k\) be the set of ordinary columns in \(C_k\). Then
\[
|D_i|\le w_i-1,\qquad |D_j|\le w_j-1,\qquad |D_k|\le w_k\quad(k\ne i,j).
\]
The target sizes of \(T_{ij}\) sum to \(W-2\). Because \(n-1\ge W-1\), the ordinary sets \(D_k\) can be padded, using unused ordinary columns, to disjoint sets with exactly the sizes prescribed by \(T_{ij}\) (zero parts omitted).

Since \(B\) is pair-residual for \(T\), some row of \(B\) separates those padded residual classes, and therefore separates the actual ordinary sets \(D_k\). In the same bottom row, every special column has its own symbol \(\alpha_\ell\), and none of those symbols occurs on an ordinary column. Thus symbols belonging to different target classes are pairwise disjoint, including when more than two target classes contain special columns.

Therefore every admissible \(C_1,\ldots,C_r\) is separated by either the top or bottom block, proving the theorem.

## Consequences

Write \(\operatorname{SHFN}(n,m,T)\) for the minimum row count of an SHF with the indicated parameters, and \(\operatorname{PHFN}\) analogously.

### 1. The two-class construction extends to arbitrary \(x\)

For \(T=\{w_1,w_2\}\), there is only one pair residual:
\[
T_{12}=\{w_1-1,w_2-1\}
\]
after deleting zero parts. Hence, whenever the auxiliary family exists,
\[
\operatorname{SHFN}(n+x-1,m,\{w_1,w_2\})
\le
\operatorname{SHFN}(n,m,\{w_1,w_2\})
+
\operatorname{SHFN}(n-1,m-x,\{w_1-1,w_2-1\}).
\]
For \(x=2\) this is exactly the two-class column-increase recurrence stated as Theorem 3.13 in Zaverucha's 2010 thesis. The formula above extends the same reduced-type mechanism to every admissible \(x\).

### 2. The perfect-hash recurrence is recovered

If \(T=\{1,1,\ldots,1\}\) has \(w\) parts, every pair residual is the same perfect-hash type with \(w-2\) singleton parts. The theorem becomes
\[
\operatorname{PHFN}(n+x-1,m,w)
\le
\operatorname{PHFN}(n,m,w)
+
\operatorname{PHFN}(n-1,m-x,w-2),
\]
recovering the columns-increase recurrence of Martirosyan and van Trung (2008).

### 3. Arbitrary types obtain a genuinely reduced-strength auxiliary

For \(x=2\), Zaverucha's Theorem 3.14 used a second ingredient of the full original type \(T\) and explicitly noted that the auxiliary was not of reduced strength. The present theorem shows that it is enough for the second ingredient to satisfy the compound collection
\[
\{T_{ij}:1\le i<j\le r\},
\]
whose individual types all have total strength \(W-2\).

More generally, a standard sufficient bound is obtained by vertically stacking ingredients for the distinct nontrivial residual types. If \(\mathcal R(T)\) denotes the set of distinct pair residuals having at least two positive parts, then
\[
N_B
\le
\sum_{R\in\mathcal R(T)} \operatorname{SHFN}(n-1,m-x,R),
\]
with \(N_B=1\) when every pair residual is one-part. Simultaneous constructions can be smaller than this stack bound.

### 4. A logarithmic auxiliary for type \(\{1,1,2\}\)

For \(T=\{1,1,2\}\), the only nontrivial pair residual is \(\{1,1\}\). An SHF of type \(\{1,1\}\) is exactly an array with distinct column vectors. Hence, for \(q=m-x\ge2\),
\[
\operatorname{SHFN}(n+x-1,m,\{1,1,2\})
\le
\operatorname{SHFN}(n,m,\{1,1,2\})
+
\left\lceil \log_q(n-1)\right\rceil.
\]
This makes the reduction from total strength four to residual strength two explicit.

### 5. Frameproof-code lifting

The standard code representation identifies an SHF of type \(\{1,w\}\) with a \(w\)-frameproof code (for the usual nonvacuous range \(n\ge w+1\)). Its unique pair residual is the one-part type \(\{w-1\}\), so a single constant row suffices for \(B\).

Let \(M_w(N,m)\) denote the maximum size of an \(m\)-ary \(w\)-frameproof code of length \(N\). For \(w\ge2\) and \(m\ge3\), whenever \(M_w(N,m)\ge w+1\),
\[
M_w(N+1,m)\ge M_w(N,m)+m-2.
\]
Indeed, apply the theorem with \(x=m-1\): one old codeword is replaced by \(m-1\) copies that are identical in the old coordinates and receive distinct symbols in one new coordinate, while all other old codewords receive the remaining symbol there.

This corollary is a direct specialization of the structural theorem; it is not asserted to be the first possible proof of this elementary lifting operation.

## Relation to prior work

Zaverucha's thesis, Section 3.1.2, records three closely related facts:

- Theorem 3.13 gives the reduced-type one-column increase for two-class SHFs.
- Theorem 3.14 extends one-column increase to arbitrary type but uses an auxiliary of the unreduced original type, and the text explicitly points out this loss.
- Theorem 3.16 gives an arbitrary-type multi-column construction with a full-type auxiliary, followed by the observation that improvements should be possible for some values of the duplication parameter and type.
- Between them, Theorem 3.15 cites the Martirosyan--van Trung perfect-hash columns-increase recurrence, whose auxiliary has strength reduced by two.

The theorem above isolates the common reason the reduction works: the bottom block is used only when special columns occupy at least two target classes, so choosing any two such classes removes one required ordinary column from each. For arbitrary type, the correct auxiliary object is therefore the compound collection of all pair residuals.

Later work checked for coverage includes general bounds and constructions for separating hash families and distributing hash families. The searched sources did not reveal this pair-residual recurrence or its arbitrary-\(x\) two-class specialization.

## Limitations

- Originality is to the best of our knowledge. The literature is broad, and equivalent recursive constructions may exist under different terminology.
- The theorem does not claim that a pair-residual auxiliary is always numerically smaller than the full-type auxiliary in every parameter regime; it provides a weaker separation requirement of total strength \(W-2\).
- The stack bound for compound residual types can be nonoptimal because one array may satisfy several residual types simultaneously.
- The frameproof corollary is structurally useful but elementary once the construction is recognized; the principal contribution is the arbitrary-type pair-residual theorem.
- No independent audit has yet been performed.

## References

1. Gregory M. Zaverucha, *Hash Families and Cover-Free Families with Cryptographic Applications*, PhD thesis, University of Waterloo, 2010. Section 3.1.2, especially Theorems 3.13--3.16. https://uwspace.uwaterloo.ca/items/73fdcd45-2ba4-4d2b-851c-e5ec75e05ad6
2. Sosina Martirosyan and Tran van Trung, "Explicit constructions for perfect hash families," *Designs, Codes and Cryptography* 46 (2008), 97--112. https://doi.org/10.1007/s10623-007-9138-6
3. Robert A. Walker II and Charles J. Colbourn, "Perfect hash families: Constructions and existence," *Journal of Mathematical Cryptology* 1(2) (2007), 125--150. https://doi.org/10.1515/JMC.2007.008
4. Marjan Bazrafshan and Tran van Trung, "Bounds for separating hash families," *Journal of Combinatorial Theory, Series A* 118(3) (2011), 1129--1135. https://doi.org/10.1016/j.jcta.2010.11.006
5. Chong Shangguan and Gennian Ge, "Separating Hash Families: A Johnson-type bound and New Constructions," *SIAM Journal on Discrete Mathematics* 30 (2016). https://doi.org/10.1137/15M103827X
6. Charles J. Colbourn, Ryan E. Dougherty, and Daniel Horsley, "Distributing hash families with few rows," *Theoretical Computer Science* 800 (2019), 31--41. https://doi.org/10.1016/j.tcs.2019.10.014
7. Penying Rochanakul, "Improved Bounds on the Size of Separating Hash Families of Short Length," *Thai Journal of Mathematics* (2020), 401--412. https://thaijmath.com/index.php/thaijmath/article/view/979
8. Xin Wei, Xiande Zhang, and Gennian Ge, "Separating hash families with large universe," *Journal of Combinatorial Theory, Series A* 216 (2025), 106075. https://doi.org/10.1016/j.jcta.2025.106075
