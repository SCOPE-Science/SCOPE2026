# Centralizer spectra and commuting pairs in truncated parallel-arrow chain algebras

## Finding

Let \(q\) be any prime power, \(h\geq1\), and \(m\geq1\). Let \(Q_{m,h}\) have vertices \(0,1,\ldots,m\), with exactly \(h\) parallel arrows from \(i-1\) to \(i\). Write \(R=\mathbb F_qQ_{m,h}/J_Q^3\), where \(J_Q\) is the arrow ideal of the path algebra, and write \(J=\operatorname{rad}(R)\). For \(x\in J\), set \(C_J(x)=\{y\in J:xy=yx\}\).

Every \(x\) has \(m\) arrow-coefficient vectors \(a_i\in\mathbb F_q^h\) and \((m-1)h^2\) freely chosen length-two path coefficients. Let \(\epsilon_i=1\) when \(a_i\ne0\), and \(\epsilon_i=0\) otherwise. Define \(u(\epsilon)\) as the number of maximal runs of ones having length one, \(v(\epsilon)\) as the number of maximal runs of ones having length at least two, and \(w(\epsilon)\) as the number of zero positions with no neighboring one (with nonexistent neighbors disregarded). Set
\[
D_h(\epsilon)=h\bigl(u(\epsilon)+w(\epsilon)\bigr)+v(\epsilon).
\]
The exact centralizer size is
\[
\boxed{|C_J(x)|=q^{(m-1)h^2+D_h(\epsilon)}.}
\]
Thus the complete centralizer-size spectrum, with each element counted once, is
\[
\boxed{\#\{x\in J:|C_J(x)|=q^{(m-1)h^2+d}\}
 =q^{(m-1)h^2}\sum_{\substack{\epsilon\in\{0,1\}^m\\D_h(\epsilon)=d}}(q^h-1)^{\sum_i\epsilon_i}.}
\]
The same spectrum determines the rank of every commutator operator \(\operatorname{ad}_x:J\to J\): its rank is exactly \(mh-D_h(\epsilon)\).

Define \(F_m(q,h)\) as the number of ordered pairs of arrow-coordinate arrays that satisfy all commuting equations (ignoring freely chosen length-two coordinates), and define \(F_0(q,h)=1\). Put \(A=q^h-1\) and \(B=(q^h-1)(q^h-q)\). The entire commuting-pair sequence has rational generating function
\[
\boxed{\sum_{m\ge0}F_m(q,h)z^m=
\frac{1+(qA+B)z-ABz^2}{1-(A+1)z-(qA+B)z^2+ABz^3}.}
\]
Consequently the exact number of commuting ordered pairs in \(J\) is \(q^{2(m-1)h^2}F_m(q,h)\), and the probability that two independent uniform elements of \(J\) commute is \(F_m(q,h)/q^{2mh}\). In particular \(F_1(q,h)=q^{2h}\) and
\[
F_2(q,h)=2q^{2h}-1+(q+1)(q^h-1)^2.
\]
For \(m\ge3\) the coefficients obey
\[
F_m=(A+1)F_{m-1}+(qA+B)F_{m-2}-ABF_{m-3}.
\]
For \(h\ge2\) and \(m\ge2\), the minimum \(\mathbb F_q\)-dimension of \(C_J(x)/J^2\) is one. It occurs exactly when the binary support is a single run of at least two ones, with at most one zero at each end. The numbers of these arrow-coordinate arrays for \(m=2\), \(m=3\), and \(m\ge4\), respectively, are
\[
A^2,\qquad A^3+2A^2,\qquad A^{m-2}(A+1)^2.
\]
To obtain the numbers of the corresponding elements \(x\), multiply by \(q^{(m-1)h^2}\). For \(m\ge2\), the center of the associative (nonunital) algebra \(J\) is exactly \(J^2\).

## Assumptions and scope

All path products are interpreted by concatenation; reversing the path-composition convention produces the same zero equations and counts. There are no arrows other than the specified consecutive parallel arrows. The truncation is by all paths of length at least three. The family includes \(m=1\), when \(J^2=0\) and every pair commutes. The formulas hold over every finite field, not only prime fields. A centralizer is taken **inside the radical** \(J\), not in the full unital algebra \(R\) or in a full matrix algebra.

## Proof

**Path-basis reduction.** Let \(a_i\in\mathbb F_q^h\) and \(b_i\in\mathbb F_q^h\) be the length-one coordinates of \(x,y\in J\). Length-two path coefficients contribute nothing to either \(xy\) or \(yx\) because \(J^3=0\). The \(h^2\) paths between vertices \(i-1\) and \(i+1\) are linearly independent. Therefore
\[
xy=yx\quad\Longleftrightarrow\quad
 a_i\otimes b_{i+1}=b_i\otimes a_{i+1}\quad(1\le i<m).
\]
This equality is over \(\mathbb F_q\) in the tensor product of the two consecutive arrow spaces; there are no cancellations between different length-two paths.

**Centralizer normal form.** If consecutive vectors \(a_i,a_{i+1}\) are both nonzero, the equality of two pure tensors implies that both \(b_i\) and \(b_{i+1}\) are the **same scalar** times \(a_i,a_{i+1}\). One proof applies a linear functional taking value one on \(a_i\), then applies a nonzero functional on \(a_{i+1}\); it also covers a zero tensor by forcing both corresponding coefficients to vanish. Propagation along a maximal nonzero run of length at least two supplies exactly one free scalar, regardless of the run length. A singleton nonzero position does not lie in a nonzero adjacency and its \(b_i\) is an arbitrary vector of dimension \(h\). If \(a_i=0\) and at least one neighboring arrow-coordinate vector is nonzero, the relevant tensor equation forces \(b_i=0\). At any other zero position, \(b_i\) is arbitrary of dimension \(h\). These free choices are independent across the maximal nonzero runs and isolated zero positions, proving \(\dim\ker(\operatorname{ad}_x|_{J/J^2})=D_h(\epsilon)\). Every length-two coordinate of \(y\) is free, giving the centralizer formula; the image of the commutator map lies in \(J^2\), and its rank is \(mh-D_h(\epsilon)\).

For each prescribed binary support, every one position admits exactly \(A=q^h-1\) choices for its \(a_i\), and every zero position one choice. The length-two part of \(x\) is completely free, contributing \(q^{(m-1)h^2}\). Summing these disjoint cases proves the complete spectrum.

**Commuting pair generating function.** At one arrow position record the \(2\times h\) matrix with rows \(a_i,b_i\). Its rank is zero, one, or two. A nonzero rank-one matrix is uniquely specified by a projective line in \(\mathbb F_q^2\) (\(q+1\) possibilities) and a nonzero row-scale vector in \(\mathbb F_q^h\) (\(A\) possibilities). There are \(B\) rank-two matrices. For two adjacent positions to satisfy the tensor equation, either one is zero or both have rank one with the same projective line. Indeed, if \(a_i,b_i\) are independent, applying two dual functionals forces the two coordinates at position \(i+1\) to vanish. If one position is nonzero rank one, the equality forces any nonzero neighbor to lie on its same projective line. This argument works for arbitrary field characteristic.

A maximal consecutive nonzero block of length \(\ell\) therefore either consists entirely of rank-one matrices sharing one of \(q+1\) projective lines (weight \((q+1)A^\ell\)), or is a singleton rank-two matrix (weight \(B\)). Its ordinary length generating series is
\[
W(z)=Bz+\frac{(q+1)Az}{1-Az}.
\]
Unique decomposition into arbitrary strings of zero positions and such blocks, separated by at least one zero, yields
\[
\sum_{m\ge0}F_mz^m=\frac{1+W(z)}{1-z-zW(z)}.
\]
Multiplying numerator and denominator by \(1-Az\) gives the displayed rational expression. Every ordered pair of radical elements additionally has two arbitrary collections of length-two path coefficients, so its total cardinality acquires the factor \(q^{2(m-1)h^2}\). The coefficient identity and probability now follow.

**Minimum and center.** For \(m\ge2\), a nonzero arrow-support run of length at least two gives centralizer-quotient dimension one. When \(h\ge2\), each singleton one run or unforced zero position contributes at least two dimensions, and each long one run contributes one; hence the unique support patterns giving dimension one are exactly those stated. Counting their three possible endpoint regimes gives the displayed extremizer counts. Any nonzero arrow coefficient at a position with an adjacent site permits choosing \(y\) supported on the adjacent arrow site so that \([x,y]\ne0\). Thus an element of \(J\) is central precisely when all arrow coefficients vanish, i.e. when it lies in \(J^2\). All arguments are valid over any finite field.

## Verification

The attached `verify.py` independently constructs each commutator linear system in the length-two path basis and Gaussian-eliminates it over prime fields. It checks the resulting nullity against the binary-support formula for every arrow-coordinate assignment in the stated finite test ranges. It separately enumerates commuting pairs of arrow-coordinate arrays in bounded cases; the independently derived rational recurrence and full support-weight spectrum are cross-checked. Run `python verify.py`. The expected terminal marker is `VERIFY_OK_PARALLEL_ARROW_COMMUTANT_CENSUS`. The checks include \(q\in\{2,3,5\}\), multiplicities \(h\in\{1,2,3\}\), and small chain lengths; all larger cases rest on the field-independent proof, not on finite sampling.

## Relationship to prior work

Xu, Han, and Jiang (2005) studied Hochschild cohomology of truncated quiver algebras in arbitrary characteristic, supplying a general foundational context rather than radical commutant statistics. Britnell and Wildon (2010) studied commuting similarity **classes** of full matrices, including nilpotent class types; those results concern different ambient algebras and do not determine how the radical-restricted centralizer of an individual element depends on consecutive arrow-coordinate supports. Green and Schroll (2023) studied a **quotient algebra** obtained by identifying parallel paths; their term “commuting algebra” does not refer to the locus of commuting pairs of elements in a fixed radical. The present count does not follow by changing only the terminology in those results. Hennecart and Perry (2022) formulated radical commuting-pair enumeration for projective representations of acyclic quivers and proved explicit results for quivers without directed paths of length greater than two. In particular their framework includes commuting-pair enumeration for the untruncated three-vertex line (the present \(m=2\) aggregate case); that known aggregate case is not asserted as novel. Their examined statements do not determine the complete elementwise radical-centralizer spectrum for arbitrary \(m\) with length-three truncation, and the latter is the principal refinement claimed here. This is not a claim of exhaustive historical priority.

## Limitations

The results do not count centralizers in the full unital algebra, nontrivial truncation lengths greater than three, nonconsecutive arrow patterns, or conjugacy classes. In the \(h=1\) case the path constraints have familiar determinantal and combinatorial interpretations; those general background structures are not claimed as new. Priority over all earlier treatments of radical commuting probability has not been conclusively established. No independent mathematical audit has been performed.

## References

1. Y. Xu, Y. Han, W. Jiang, *Hochschild cohomology of truncated quiver algebras*, arXiv:math/0509202 (first arXiv release 9 September 2005), https://arxiv.org/abs/math/0509202.
2. J. R. Britnell, M. Wildon, *On types and classes of commuting matrices over finite fields*, arXiv:1001.0811 (first arXiv release 6 January 2010), https://arxiv.org/abs/1001.0811.
3. L. Hennecart, N. Perry, *A Quiver Analogue of Higman’s Conjecture*, arXiv:2208.07738 (first arXiv release 16 August 2022), https://arxiv.org/abs/2208.07738.
4. E. L. Green, S. Schroll, *The Commuting Algebra*, arXiv:2302.08169 (first arXiv release 16 February 2023), https://arxiv.org/abs/2302.08169.
