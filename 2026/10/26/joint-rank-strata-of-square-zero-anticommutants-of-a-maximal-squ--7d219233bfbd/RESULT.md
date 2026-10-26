# Joint rank strata of square-zero anticommutants of a maximal square-zero matrix

## Finding

Let \(q\) be any prime power and let \(A\in M_{2r}(\mathbb F_q)\), \(r\ge1\), satisfy \(A^2=0\) and \(\operatorname{rank}A=r\). Define
\[
\mathcal E_A=\{B\in M_{2r}(\mathbb F_q):B^2=0,\ AB+BA=0\}.
\]
For \(B\in\mathcal E_A\), write \(t=\operatorname{rank}(AB)\), \(b=\operatorname{rank}B\), \(h=r-2t\), and \(u=b-2t\). Then \(\mathcal E_A\) has elements with these ranks **if and only if**
\[
0\le t\le\lfloor r/2\rfloor,\qquad 0\le u\le h.
\]
For every feasible pair the exact number of such \(B\) is
\[
\boxed{N_{r,q}(t,u)=
{r\brack t}_q{r-t\brack t}_q\,|\operatorname{GL}_t(\mathbb F_q)|\,
q^{(r-t)^2+t^2-h^2}\,{h\brack u}_q
\prod_{i=0}^{u-1}(q^h-q^i).}
\]
Here \({m\brack j}_q\) is the Gaussian binomial coefficient; empty products and \(|\operatorname{GL}_0|\) equal one. The expression is zero outside the indicated range. In particular, among elements with fixed \(\operatorname{rank}(AB)=t\), the distribution of \(\operatorname{rank}B-2t\) is **exactly the rank distribution of a uniformly random endomorphism of an \(h\)-dimensional vector space** over \(\mathbb F_q\).

Over any algebraically closed field, the reduced locally closed locus with ranks \((\operatorname{rank}(AB),\operatorname{rank}B)=(t,2t+u)\) is smooth and irreducible of dimension \(r^2-(h-u)^2\). Its dimension-\(r^2\) subloci correspond to \(u=h\); their closures are the \(\lfloor r/2\rfloor+1\) irreducible components of the reduced square-zero anticommutant locus. Component equidimensionality and the characteristic-two component count have known antecedents (see References and Relationship to prior work); the claimed refinement is the exact joint rank distribution, together with its fine-stratum description.

## Assumptions and scope

The first matrix \(A\) is **fixed and labeled**, rather than sampled up to conjugacy, and is a maximal-rank square-zero matrix in even dimension. Both square-zero conditions are literal equations over the stated field. Anticommutation \(AB+BA=0\) includes commuting in characteristic two. The proof is field-independent; finite-field counting holds for prime powers, not merely prime orders. Algebraic-geometric assertions concern reduced underlying varieties, not the potentially nonreduced scheme structure of a polynomial-equation presentation.

## Proof

**1. Unique block parametrization.** Since \(\operatorname{im}A=\ker A\) has dimension \(r\), choose a basis with
\[
A=\begin{pmatrix}0&I_r\\0&0\end{pmatrix}.
\]
Writing \(B\) in four \(r\times r\) blocks, \(AB+BA=0\) forces
\[
B=\begin{pmatrix}P&Y\\0&-P\end{pmatrix}
\]
with uniquely determined \(P,Y\in M_r(\mathbb F_q)\). Direct multiplication shows that \(B^2=0\) is equivalent to \(P^2=0\) and \(PY=YP\), in every characteristic. Moreover, \(\operatorname{rank}(AB)=\operatorname{rank}P=t\).

**2. Rank of the full matrix.** Let \(U=\operatorname{im}P\) and \(K=\ker P\), so \(U\subseteq K\). A commuting \(Y\) preserves \(U\) and \(K\), hence induces an endomorphism \(\bar Y\) of the homology space \(H=K/U\), of dimension \(h=r-2t\). Project \(\operatorname{im}B\) onto the second \(r\)-dimensional block. The projected image is \(U\), of dimension \(t\); the kernel of this projection inside \(\operatorname{im}B\) is \(U+Y(K)\) in the first block. Because \(Y(K)\subseteq K\), this kernel has dimension \(t+\operatorname{rank}\bar Y\). Thus
\[
\operatorname{rank}B=2t+\operatorname{rank}\bar Y.
\]
This proves the asserted feasibility range once all endomorphisms of \(H\) are shown to lift.

**3. Number of square-zero \(P\).** A square-zero \(P\) of rank \(t\) is specified by \(U=\operatorname{im}P\) (a \(t\)-space), \(K=\ker P\) (an \((r-t)\)-space containing \(U\)), and an isomorphism \(\mathbb F_q^r/K\to U\). These choices give
\[
{r\brack t}_q{r-t\brack t}_q|\operatorname{GL}_t(\mathbb F_q)|.
\]
They exist exactly when \(2t\le r\).

**4. Centralizer-to-homology surjection.** As a module over \(\mathbb F_q[z]/(z^2)\), the pair \((\mathbb F_q^r,P)\) has \(t\) summands of length two and \(h\) trivial summands. Counting homomorphisms between these summands gives
\[
\dim_{\mathbb F_q}\{Y:PY=YP\}=2t^2+2th+h^2=(r-t)^2+t^2=:c.
\]
Choose a Jordan splitting \(\mathbb F_q^r\simeq U\oplus H\oplus W\), with \(P:W\to U\) an isomorphism. Every endomorphism of \(H\) extends to one commuting with \(P\) by acting on the middle summand and by zero on \(U,W\). Therefore the linear map \(Y\mapsto\bar Y\) from the centralizer onto \(\operatorname{End}(H)\) is surjective with kernel dimension \(c-h^2\). Each prescribed \(\bar Y\) has exactly \(q^{c-h^2}\) commuting lifts.

**5. Rank enumeration and conclusions.** Choose the image of a rank-\(u\) endomorphism of \(H\) in \({h\brack u}_q\) ways, then a surjection onto that image in \(\prod_{i=0}^{u-1}(q^h-q^i)\) ways. Multiplying by Steps 3 and 4 proves the formula and every feasibility boundary. Summing over \(u\) gives \(q^{h^2}\), so the counts sum for each fixed \(t\) to the number of square-zero \(P\) times \(q^c\), furnishing a consistency identity.

**6. Geometry of the refined strata.** Fix \(t\) over an algebraically closed field. The rank-\(t\) square-zero matrices \(P\) form a smooth irreducible \(\operatorname{GL}_r\)-orbit of dimension \(r^2-c\). Over this orbit, the centralizer spaces and the homology spaces form vector bundles; the preceding split surjection becomes a surjective vector-bundle map. The rank-\(u\) endomorphism locus on \(H\) is smooth irreducible of dimension \(h^2-(h-u)^2\). Pulling it back gives an affine-space bundle of relative dimension \(c-h^2\), hence a smooth irreducible stratum of total dimension
\[
(r^2-c)+(c-h^2)+h^2-(h-u)^2=r^2-(h-u)^2.
\]
The open \(u=h\) locus is dense for each fixed \(t\), and has dimension \(r^2\). All lower-\(u\) loci lie in the closure for that \(t\). The closures for different \(t\) are distinct: their generic \(\operatorname{rank}P\) differs. Since the variety is the finite union of these closures, they are exactly its irreducible components. This geometry is supplied to explain the counted ranks, without attributing the previously known characteristic-two equidimensionality to the present result.

## Verification

Run the supplied standalone `verify.py` with an ordinary Python 3 interpreter. It independently enumerates all \(P,Y\) for \((r,q)=(1,2),(1,3),(2,2),(2,3),(2,5),(3,2)\), selects precisely the pairs satisfying \(P^2=0\) and \(PY=YP\), constructs \(B\), verifies \(B^2=0\) and \(AB+BA=0\), and compares **every observed rank pair** to the closed formula. It separately scans **all 65,536** binary \(4\times4\) matrices, without imposing the block parametrization, finding the predicted \(28\) valid anticommutants. These finite checks test the proof's boundaries but do not establish the general theorem by exhaustive computation. The program performs arithmetic modulo a prime; the proof, not these computations, supplies the prime-power extension.

## Relationship to prior work

Levy, *Varieties of Modules for Z/2Z x Z/2Z* (arXiv:math/0609180, first available 2006), already studied square-zero commuting pairs in characteristic two and proved equidimensionality and component counts for their varieties. In the maximal-rank fixed-first-matrix fiber, the component count given here coincides with the one implicit in his Lemma 2.1 and Proposition 2.3; **that count is not claimed as new**. The present formula additionally distinguishes every \(\operatorname{rank}B\) and \(\operatorname{rank}(AB)\), for every finite-field order and characteristic.

Chen and Wang, *Anti-commuting varieties* (arXiv:1805.00378), Proposition 2.2, give Jordan-block normal forms for anticommutation and study varieties of anticommuting matrices, but do not impose both square-zero equations together to count this finite-field joint rank spectrum. Basili and Iarrobino, *Pairs of commuting nilpotent matrices, and Hilbert function* (arXiv:0709.2304), address nilpotent commuting geometry, not this fixed-fiber, two-rank point count. A thesis by C. K. Ngai, *Varieties of commuting matrices with prescribed ranks and kernels* (2024), is plausibly relevant, but its full text was inaccessible in this examination; its exact implications cannot be ruled out from the available title alone. Absence of a discovered formula is not a proof of historical novelty.

## Limitations

The statement fixes one maximal-rank square-zero first matrix in even dimension; it does not enumerate simultaneously varying first matrices, or all non-maximal first-matrix Jordan types. The geometry is the reduced stratum geometry, not a claim about scheme smoothness or reducedness at intersections. The finite computer checks exhaust only the explicitly named small fields and sizes. An equivalent unpublished or less readily accessible rank-refinement, including one in the inaccessible thesis above, remains possible. No independent mathematical audit has occurred.

## References

1. P. Levy, *Varieties of Modules for Z/2Z x Z/2Z*, arXiv:math/0609180 (2006), especially §1–2, Lemma 2.1 and Proposition 2.3. https://arxiv.org/abs/math/0609180
2. X. Chen and W. Wang, *Anti-commuting varieties*, arXiv:1805.00378 (2018), especially Proposition 2.2 and §6. https://arxiv.org/abs/1805.00378
3. R. Basili and A. Iarrobino, *Pairs of commuting nilpotent matrices, and Hilbert function*, arXiv:0709.2304 (2007). https://arxiv.org/abs/0709.2304
4. C. K. Ngai, *Varieties of commuting matrices with prescribed ranks and kernels*, master's thesis, Simon Fraser University (2024), full text not examined. https://summit.sfu.ca/item/39073
