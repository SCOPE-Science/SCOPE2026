# The five-point cutoff for band \(\mathcal R\)-cross-sections of finite-chain transformations

## Finding
For each integer \(n\ge 2\), let \(\mathcal O_n\) be the monoid of all order-preserving self-maps of the chain \([n]=\{1,\ldots,n\}\), with transformations acting on the right. A Green \(\mathcal R\)-cross-section is a subsemigroup containing precisely one map from each kernel class. A *band cross-section* is such a subsemigroup in which every map is idempotent.

**Theorem.** The band \(\mathcal R\)-cross-sections of \(\mathcal O_n\) are indexed exactly by the points \(r\in[n]\) satisfying
\[
r-1\le2,\qquad n-r\le2.
\]
For each admissible \(r\), the corresponding cross-section has one representative \(\alpha_{\pi,r}\) for every partition \(\pi\) of \([n]\) into nonempty consecutive intervals. For \(x\) in its interval block \(B\in\pi\), define
\[
x\alpha_{\pi,r}=\begin{cases}
r,&r\in B,\\
\min B,&\max B<r,\\
\max B,&\min B>r.
\end{cases}
\]
There are no other band \(\mathcal R\)-cross-sections. Their number is \(2,3,2,1\) for \(n=2,3,4,5\), respectively, and zero for every \(n\ge6\). In particular, band cross-sections exist **if and only if** \(n\le5\) (within the stated \(n\ge2\) domain).

Moreover, the band indexed by \(r\) has the abstract structure
\[
\mathcal B_r\cong Q_{r-1}\times Q_{n-r},
\]
where \(Q_0\) is the one-element monoid, \(Q_1\) is the two-element semilattice, and \(Q_2\) is the four-element band consisting of identity, zero, and two further idempotents \(a,b\) with \(ab=a\) and \(ba=b\). Thus the isomorphism types at \(n=3,4,5\) are respectively \(Q_2,Q_1\times Q_1,Q_2\), then two copies of \(Q_1\times Q_2\), then one copy of \(Q_2\times Q_2\) as labeled cross-sections.

## Assumptions and scope
All transformation maps are total and weakly increasing. Composition uses right-action notation: \(x(\alpha\beta)=(x\alpha)\beta\). The phrase 'one representative per kernel class' uses the usual Green \(\mathcal R\)-relation with this convention. Band means every element satisfies \(\alpha^2=\alpha\), not that the band is commutative. Cross-sections are distinguished as actual subsets of \(\mathcal O_n\), not merely up to isomorphism. The theorem makes no claim about partial or orientation-reversing transformation monoids.

## Proof
**1. Kernels and a universal fixed point.** The kernel blocks of any order-preserving map are consecutive intervals. Conversely, each interval partition is a kernel, so there are \(2^{n-1}\) kernel classes. Any cross-section \(S\) contains exactly one constant map, say \(c_r\). For every \(f\in S\), the product \(c_r f=c_{r f}\) belongs to \(S\). Since there is just one constant, \(r f=r\). Hence every map in \(S\) fixes the same point \(r\). This fixed-point argument is also present in Bondar's Lemma 4.7.

**2. Forced adjacent collapses.** Let \(S\) be a band cross-section. An idempotent transformation chooses, for each kernel block, a representative **inside that block**: if \(f(x)=y\) and \(f^2=f\), then \(f(y)=y\), so \(y\) belongs to the block mapped to \(y\). For each adjacent pair \(\{i,i+1\}\), the unique representative \(e_i\in S\) with just this nonsingleton kernel block therefore fixes all other points and either sends \(i+1\) to \(i\) (type \(L\)) or sends \(i\) to \(i+1\) (type \(R\)).

Two consecutive collapses cannot both have type \(L\): in the product \(e_i e_{i+1}\) the chain \(i+2\mapsto i+1\mapsto i\) appears, so this product is not idempotent. Likewise, if they both have type \(R\), the reverse product \(e_{i+1}e_i\) has \(i\mapsto i+1\mapsto i+2\) and is not idempotent. Thus their types **alternate**. Since every element fixes \(r\), the collapse \(e_r\), when present, must have type \(L\), and \(e_{r-1}\), when present, must have type \(R\).

**3. The four-point obstruction.** Suppose \(r+3\le n\). Alternation forces \(e_{r+2}\) to be type \(L\), hence \((r+3)e_{r+2}=r+2\). The section must also contain the idempotent \(h\) whose kernel has precisely one nonsingleton block \(\{r,r+1,r+2\}\). Its output on that block is \(r\), since it fixes \(r\), and it fixes all remaining singleton blocks. In the product \(h e_{r+2}\), the points obey
\[
r+3\longmapsto r+2\longmapsto r.
\]
Consequently \((h e_{r+2})^2\ne h e_{r+2}\), contradicting closure of a band. Reversing the chain yields the same contradiction if \(r-3\ge1\). Hence \(r-1\le2\) and \(n-r\le2\). In particular no band section can exist for \(n\ge6\), since no such \(r\) exists.

**4. Construction and uniqueness.** Assume these two inequalities. The formula in the statement maps each block to a point within it and is weakly increasing, so its representatives are idempotent and have pairwise distinct interval kernels. The maps preserve the left and right half-chains \(\{1,\ldots,r\}\) and \(\{r,\ldots,n\}\), intersecting only at the common fixed point \(r\). Choices of cuts to the left and right of \(r\) are independent. On a half-chain with at most two non-root points, the possible maps form \(Q_0\), \(Q_1\), or \(Q_2\), respectively. On three points \(\{0,1,2\}\) with root \(0\), the four maps are \((0,1,2)\), \((0,0,2)\), \((0,2,2)\), \((0,0,0)\); direct composition proves closure and idempotence. Thus the constructed cross-section is the direct product \(Q_{r-1}\times Q_{n-r}\) and contains exactly one map for each of the \(2^{n-1}\) interval kernels.

Finally, in *any* band section with this fixed root, the image of the block containing \(r\) is forced to be \(r\). Every other nonsingleton block, if any, is an adjacent pair \(B=\{i,i+1\}\) wholly on one side, necessarily at distance two from \(r\). The representative \(f\) for any kernel containing this block must choose the same endpoint as \(e_i\): otherwise \(f e_i\) would differ from \(f\), while having exactly the same kernel, because \(e_i\) fixes every output from all other kernel blocks. This contradicts the single-representative property. Alternation forces \(e_i\) to choose the endpoint farther from \(r\). Hence every representative agrees with the construction. There is exactly one such section per admissible \(r\), proving the classification and the counts. \(\square\)

## Verification
The accompanying `verify_band_cross_sections.py` constructs the canonical band for each admissible root through \(n=5\), checks all \(2^{n-1}\) representatives, their distinct kernels and all products, and independently exhausts *every* possible band cross-section through \(n=4\). It also tests the nonidempotent four-point obstruction symbolically across all roots for \(6\le n\le15\). Execute `python3 verify_band_cross_sections.py`; the expected terminal marker is `VERIFY_OK`. The general impossibility for all \(n\ge6\) is proved above, not extrapolated from this finite test.

## Relationship to prior work
Bondar (arXiv:2208.09661, Theorem 4.14) gives a much broader classification of all \(\mathcal R\)-cross-sections of \(\mathcal O_n\) by decreasing binary trees; Lemma 4.7 supplies the fixed-point observation. The present theorem isolates the additional *band* condition and derives a sharp universal nonexistence threshold, a complete labeled count, and abstract product types through a local obstruction. The 2025 journal version of that work has the same general classification as its advertised scope. The result should be understood as a structural refinement of an existing classification, not as a new classification of arbitrary cross-sections.

Earlier classification of \(\mathcal R\)-cross-sections of the **full** transformation monoid (Pyekhtyeryev) concerns a larger ambient monoid and does not identify the band subclass of the order-preserving monoid. Generic Green-relation properties and kernel counts are standard and are not asserted to be new.

## Limitations
The result is not an independent priority certification: a different derivation of the band cutoff could exist, particularly in the complete 2025 journal text or specialized band-cross-section literature. The proof does not enumerate non-band cross-sections and does not imply that arbitrary order-preserving bands stop existing at size five. The finite verifier checks small cases; the universal claim depends on the four-point obstruction.

## References
- E. A. Bondar, *\(\mathcal R\)-cross-sections of the monoid of order-preserving transformations on a finite chain*, arXiv:2208.09661 (initial arXiv record, August 2022), especially Lemma 4.7 and Theorem 4.14; journal version *Semigroup Forum* 111 (2025), 24–56, doi:10.1007/s00233-025-10547-w.
- V. Pyekhtyeryev, *\(\mathcal H\)- and \(\mathcal R\)-cross-sections of the full finite semigroup \(T_n\)*, *Algebra and Discrete Mathematics* (2003), no. 3, 82–88.
