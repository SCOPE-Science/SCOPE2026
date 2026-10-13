# Exact simultaneous full-support similarity for commuting two-dimensional matrices

## Finding

Let \(q\) be any prime power and \(k\geq1\). A matrix is **fully nonzero** if all four of its entries are nonzero. For pairwise commuting, nonscalar matrices \(A_1,\ldots,A_k\in M_2(\mathbb F_q)\), put \(A=A_1\), \(t=\operatorname{tr}(A)\), and \(d=\det(A)\). There are unique scalars \(u_j\in\mathbb F_q\) and \(v_j\in\mathbb F_q^\times\) such that \(A_j=u_jI+v_jA\), with \(u_1=0\), \(v_1=1\). Define
\[
E=\bigcup_{j=1}^k\{-u_j/v_j,\ t+u_j/v_j\},\qquad
Z=\{a\in\mathbb F_q:a^2-ta+d=0\}.
\]
Then **the exact number of simultaneous conjugates** of this tuple for which every matrix is fully nonzero is
\[
\boxed{N=(q-1)\bigl(q-|E\cup Z|\bigr).}
\]
Equivalently, exactly \(N\lvert C_{\operatorname{GL}_2(\mathbb F_q)}(A)\rvert\) ordered changes of basis \(P\in\operatorname{GL}_2(\mathbb F_q)\) make all entries of every \(P^{-1}A_jP\) nonzero. The number of admissible simultaneous conjugates is positive precisely when \(E\cup Z\ne\mathbb F_q\). The proportion of all changes of basis that are admissible equals \(N/|\operatorname{Orb}(A)|\).

For every such tuple, \(|E|\leq2k\) and \(|Z|\leq2\), so the uniform guarantee \(q>2k+2\) follows. This is sharp at infinitely many field sizes: for every \(q=2^m\) with \(m\geq3\), a commuting family of \(k=q/2-1\) nonscalar matrices has **no** common fully-nonzero basis, although each member separately has one.

Already over \(\mathbb F_5\), the commuting pair
\[
A=\begin{pmatrix}0&1\\1&1\end{pmatrix},\qquad B=A+3I
\]
has no common fully-nonzero basis. Nonetheless, each matrix separately has exactly \(8\) fully-nonzero conjugates in its \(24\)-element similarity class.

## Assumptions and scope

The field is any finite field \(\mathbb F_q\), including characteristics two and three. The matrices have size exactly \(2\times2\), commute pairwise, and are each nonscalar. If any member is scalar then no fully-nonzero simultaneous conjugate exists, because a scalar matrix has zero off-diagonal entries in every basis. The integer \(k\) is arbitrary and repetitions of non-scalar family members are permitted. "Count" means distinct conjugated ordered tuples, not labelled bases, unless bases are explicitly mentioned.

For completeness, \(\operatorname{Orb}(A)\), the similarity orbit of a nonscalar \(2\times2\) matrix, has size
\[
|\operatorname{Orb}(A)|=\begin{cases}
q(q-1),&X^2-tX+d\text{ irreducible},\\
q(q+1),&X^2-tX+d\text{ has distinct roots in }\mathbb F_q,\\
q^2-1,&X^2-tX+d\text{ has a repeated root in }\mathbb F_q.
\end{cases}
\]
The corresponding invertible centralizer orders are respectively \(q^2-1\), \((q-1)^2\), and \(q(q-1)\). Here these standard formulas refer to the **nonscalar** similarity class; for a repeated root a separate scalar class also exists.

## Proof

**Step 1: commuting families reduce to one cyclic matrix.** Every nonscalar \(2\times2\) matrix over a field has minimal polynomial of degree two and has a cyclic vector. Hence its matrix centralizer is \(\mathbb F_q I+\mathbb F_q A\), and the representation \(A_j=u_jI+v_j A\) is unique. The coefficient \(v_j\) is nonzero exactly because \(A_j\) is nonscalar. All commuting members therefore transform under the same similarity as \(A\).

**Step 2: parametrize every admissible conjugate.** A nonscalar matrix \(C\) with trace \(t\) and determinant \(d\) is similar to \(A\), because all nonscalar \(2\times2\) matrices with a given characteristic polynomial have the same cyclic rational canonical form. Write
\[
C=\begin{pmatrix}a&b\\c&t-a\end{pmatrix}.
\]
The determinant constraint is \(bc=a(t-a)-d\). Every \(u_jI+v_jC\) has off-diagonal entries \(v_jb,v_jc\), so all off-diagonal entries in the tuple are nonzero if and only if \(b,c\ne0\). This is equivalent to \(a\notin Z\) under the determinant constraint.

The two diagonal entries of \(u_jI+v_jC\) are \(u_j+v_ja\) and \(u_j+v_j(t-a)\). Their simultaneous nonvanishing for all \(j\) is equivalent to \(a\notin E\). For each \(a\notin E\cup Z\), the product \(bc=a(t-a)-d\) is nonzero; there are exactly \(q-1\) pairs \((b,c)\in(\mathbb F_q^\times)^2\) realizing this product. Conversely, each admissible simultaneous conjugate arises uniquely in this way. This proves the formula for \(N\).

**Step 3: count changes of basis and derive the threshold.** The stabilizer of the complete tuple equals the invertible centralizer of \(A\), because \(A_1=A\). Thus each admissible tuple has exactly \(\lvert C_{\operatorname{GL}_2}(A)\rvert\) conjugating bases and all bases have equally many representatives in each orbit point. The orbit sizes follow from \(|\operatorname{GL}_2(\mathbb F_q)|=(q^2-1)(q^2-q)\) and the standard three centralizer orders. As \(|E\cup Z|\leq2k+2\), the condition \(q>2k+2\) forces \(N>0\).

**Step 4: infinite sharpness.** Let \(q=2^m\geq8\), select \(t=1\) and \(\alpha\in\mathbb F_q\setminus\{0,1\}\), and let \(d=\alpha(\alpha+1)\). The polynomial \(X^2+X+d\) has exactly the two distinct roots \(\alpha,\alpha+1\). Translation by \(1\) partitions the field into \(q/2\) disjoint pairs \(\{s,s+1\}\). Choose one representative \(s\) from every pair except \(\{\alpha,\alpha+1\}\), including \(s=0\) from \(\{0,1\}\). Let \(A\) have trace \(1\), determinant \(d\), and be nonscalar, and form the \(k=q/2-1\) matrices \(A+sI\) for these representatives. Their forbidden diagonal sets cover \(E=\mathbb F_q\setminus\{\alpha,\alpha+1\}\), whereas \(Z=\{\alpha,\alpha+1\}\); thus \(N=0\). For each one matrix, the forbidden union comprises at most four field elements, so since \(q\geq8\) its individual fully-nonzero count is strictly positive. Equality \(q=2k+2\) therefore cannot be included in a universal guarantee.

**Step 5: an explicit commuting-pair obstruction.** Over \(\mathbb F_5\), the displayed matrix \(A\) has \(t=1\), \(d=4\), and \(Z=\{3\}\). For \((A,A+3I)\) the forbidden set is \(E=\{0,1,2,4\}\), whence \(N=0\). Separately, \(A\) and \(A+3I\) each have forbidden diagonal sets of size two, disjoint from the single root in \(Z\), yielding \((5-1)(5-3)=8\) admissible conjugates each. The common conjugacy orbit has size \(5^2-1=24\). This checks that individual existence need not imply joint existence.

## Verification

The standalone, dependency-free `verify.py` exhaustively enumerates all \(2\times2\) matrices for field sizes \(2,3,4,5,7,8,9,11\), verifies all predicted single-matrix counts for every trace/determinant pair, independently constructs each nonscalar similarity orbit for \(q\leq5\) by direct conjugation through all invertible matrices, and checks the simultaneous counting formula for every scalar-shift pair in these small fields. For \(q\leq4\), it additionally exhausts all ordered triples of scalar shifts. Independent conjugation enumeration verifies the individual-versus-joint obstructions at \(q=5\) and \(q=8\). The local execution printed `VERIFY_OK`; this finite checking is corroboration of, not a replacement for, the all-\(q\), all-\(k\) proof.

Reproduce with `python3 verify.py`, using Python 3 standard library only. Field extensions are implemented explicitly via irreducible defining polynomials in the verifier.

## Relationship to prior work

Marcoux, Radjavi, Yahaghi and Zhang prove existence of a fully-nonzero conjugate for one nonscalar matrix over sufficiently large fields, with the threshold \(q\geq5\) for the single \(2\times2\) case stated in their remark after Theorem 3.1. Their Theorem 3.2 concerns simultaneous fully-nonzero representations for operators over the quaternions; it does not imply the finite-field result, where the simultaneous obstruction above occurs. The present statement instead gives an exact **joint** orbit count, an exact algorithm to decide admissibility for every commuting finite-field tuple, a uniform threshold in the tuple length, and equality-case counterexamples.

Sharma's classification of simultaneous similarity classes of commuting matrices over finite fields supplies the familiar centralizer structure but does not impose fully-nonzero entry conditions on every tuple component. Bodine and McDonald's study of spectrally arbitrary zero-nonzero patterns establishes that the full \(2\times2\) pattern is spectrally arbitrary once the field has at least five elements; that is a one-matrix existential assertion, not the simultaneous conjugation criterion. The new count is compatible with both results.

## Limitations

The criterion requires commuting families of \(2\times2\) matrices, and it does not claim anything about general noncommuting families, higher-dimensional representations, or quaternionic unitary conjugacy. The uniform size inequality is a sufficient condition, not a necessary one for a particular family; the exact test is the stated forbidden-set formula. Related older matrix-pattern literature has not been comprehensively exhausted, so equivalent historical formulations cannot be ruled out solely by the searches performed.

## References

1. L. W. Marcoux, H. Radjavi, B. R. Yahaghi, Y. Zhang, *Fully non-zero matrices and generators of full algebras of operators*, arXiv:2608.21154v1, first public 2026-08-21, https://arxiv.org/abs/2608.21154 . Theorem 3.1, subsequent remark and Theorem 3.2 inspected in the full public preprint.
2. U. B. Sharma, *Simultaneous Similarity Classes of Commuting matrices over a finite field*, arXiv:1409.2698, https://arxiv.org/abs/1409.2698 ; Linear Algebra and its Applications 501 (2016), 48–97, DOI:10.1016/j.laa.2016.03.015. See section 3 on the regular centralizer and commuting-tuple orbit counts.
3. E. J. Bodine and J. J. McDonald, *Spectrally arbitrary patterns over finite fields*, Linear and Multilinear Algebra 60 (2012), 285–299, DOI:10.1080/03081087.2011.591395. The public abstract establishes the full two-by-two pattern threshold.
