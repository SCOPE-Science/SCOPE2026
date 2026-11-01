# Exact determinant fibers of normalized symmetric circulants over odd finite fields

## Finding
Let \(q\) be an odd prime power with characteristic \(\ell\), and let \(n\ge1\). Let \(C_{n,q}\) denote all symmetric \(n\)-by-\(n\) circulant matrices over \(\mathbb F_q\) with every row sum equal to \(1\). For \(t\in\mathbb F_q\), write \(N_{n,q}(t)=\#\{A\in C_{n,q}:\det A=t\}\).

Write \(n=\ell^s m\), with \(\ell\nmid m\). Remove \(0\), and also \(m/2\) when \(m\) is even, from \(\mathbb Z/m\mathbb Z\). Partition the remaining classes into orbits \(O\) under multiplication by \(q\) and negation. Every orbit has even size \(2e_O\). Define the computable integers
\[
U_{m,q}=\prod_O(q^{e_O}-1),\qquad L_{n,q}=q^{(n-m)/2},
\]
with the empty product equal to \(1\). Then the complete determinant distribution is as follows:

* If \(n\) is even, \(N_{n,q}(t)=L_{n,q}U_{m,q}\) for each \(t\ne0\), while
\[
N_{n,q}(0)=q^{n/2}-(q-1)L_{n,q}U_{m,q}.
\]
Thus every nonzero determinant occurs equally often.
* If \(n\) is odd and \(m>1\), \(N_{n,q}(t)=2L_{n,q}U_{m,q}/(q-1)\) for each nonzero square \(t\), \(N_{n,q}(t)=0\) for each nonsquare \(t\), and
\[
N_{n,q}(0)=q^{(n-1)/2}-L_{n,q}U_{m,q}.
\]
Thus every nonzero square occurs equally often and no nonsquare is a determinant.
* If \(m=1\) (necessarily \(n\) odd), all \(q^{(n-1)/2}\) matrices have determinant \(1\), so \(N_{n,q}(1)=q^{(n-1)/2}\) and \(N_{n,q}(t)=0\) for \(t\ne1\).

The third case includes \(n=1\) and every pure \(\ell\)-power index. The theorem covers all finite fields of odd characteristic, including cases where the characteristic divides the circulant order.

## Assumptions and scope
A circulant is determined by its first row \((c_0,\ldots,c_{n-1})\); it is symmetric exactly when \(c_j=c_{n-j}\) for all indices modulo \(n\). Its row sum is \(\sum_jc_j\). Consequently \(C_{n,q}\) contains exactly \(q^{\lfloor n/2\rfloor}\) matrices. The orbit action uses the residue of the integer \(q\) modulo \(m\). The zero and potential half-index exceptions correspond to the fixed roots \(1\) and \(-1\); their removal is essential.

## Proof
Associate a circulant to the class of its first-row polynomial \(f(X)=\sum_j c_jX^j\) in
\[
R=\mathbb F_q[X]/(X^n-1).
\]
The involution \(\iota:f(X)\mapsto f(X^{-1})\) is well defined. Symmetric circulants correspond exactly to \(R^\iota\), and row sum \(1\) is the augmentation equation \(f(1)=1\). The invariant subspace has dimension \(\lfloor n/2\rfloor+1\), since the basis monomials pair by reversal; augmentation is a nonzero linear functional. Thus the stated total count follows.

As \(\ell\) is odd,
\[
X^n-1=(X^m-1)^{\ell^s}.
\]
Let \(S=\mathbb F_q[X]/(X^m-1)\). Reduction \(R\to S\) commutes with \(\iota\). It restricts to a surjection \(R^\iota\to S^\iota\): to lift an invariant element, lift it arbitrarily and average the lift with its reversal, dividing by \(2\) in \(\mathbb F_q\). The dimensions of the two invariant subspaces differ by \((n-m)/2\), since \(n,m\) have the same parity. Augmentation is preserved, so every normalized invariant class in \(S\) has exactly \(L_{n,q}\) normalized invariant lifts in \(R\).

Since \(\ell\nmid m\), \(X^m-1\) is separable. Over a splitting field its roots are \(\zeta^j\) indexed by \(j\in\mathbb Z/m\mathbb Z\). A class \(f\in S^\iota\) has equal values at reciprocal roots, while the values on a \(q\)-Frobenius orbit are related by \(a\mapsto a^q\). For an orbit \(O\) of the joint actions \(j\mapsto qj\) and \(j\mapsto-j\), different from the fixed root positions, the invariant values form one independent field factor \(\mathbb F_{q^{e_O}}\), with \(|O|=2e_O\). Indeed the inversion and Frobenius relations identify exactly one degree of freedom per pair of root positions, and finite-field descent gives the specified extension. The distinguished root \(1\) contributes a factor \(\mathbb F_q\), fixed to \(1\) by normalization. When \(m\) is even, the distinguished root \(-1\) contributes one further independent factor \(v\in\mathbb F_q\).

For a circulant polynomial \(f\), the determinant equals the product of its evaluations at all \(n\)-th roots counted with their algebraic multiplicity. Hence, for an invariant normalized class and its reduced parameters \(u_O\in\mathbb F_{q^{e_O}}\),
\[
\det C(f)=\begin{cases}
\displaystyle \left(\prod_O N_{\mathbb F_{q^{e_O}}/\mathbb F_q}(u_O)\right)^{2\ell^s},&m\text{ odd},\\[4pt]
\displaystyle v^{\ell^s}\left(\prod_O N_{\mathbb F_{q^{e_O}}/\mathbb F_q}(u_O)\right)^{2\ell^s},&m\text{ even}.
\end{cases}
\]
This equality is valid in the repeated-root case because each root of \(X^m-1\) appears with multiplicity \(\ell^s\) in \(X^n-1\). In particular, nilpotent lifts do not change the determinant.

Every finite-field norm map from \(\mathbb F_{q^e}^{\times}\) onto \(\mathbb F_q^{\times}\) is surjective. The number of nonzero assignments of the \(u_O\) is \(U_{m,q}\). If \(m\) is even, \(v\) ranges independently over all \(\mathbb F_q^{\times}\); since the map \(v\mapsto v^{\ell^s}\) is bijective on \(\mathbb F_q^{\times}\), exactly \(U_{m,q}\) reduced assignments give any prescribed nonzero determinant. Multiplying by \(L_{n,q}\) and subtracting from the total \(q^{n/2}\) proves the even case.

If \(m>1\) is odd, at least one joint orbit exists. Thus the product of norms is uniformly distributed over \(\mathbb F_q^{\times}\) among the \(U_{m,q}\) nonzero assignments, with \(U_{m,q}/(q-1)\) assignments for each product. Because \(\ell^s\) is odd, exponentiation by \(2\ell^s\) has the same two-element kernel and nonzero-square image as squaring in \(\mathbb F_q^{\times}\). Every square determinant consequently has exactly \(2U_{m,q}/(q-1)\) reduced assignments. Multiplication by \(L_{n,q}\) and subtraction from the total \(q^{(n-1)/2}\) proves the odd \(m>1\) case.

Finally, if \(m=1\), the only reduced root is \(1\). Its value is fixed to \(1\), and the determinant of every nilpotent lift is \(1^{\ell^s}=1\). This proves the exceptional case and completes the classification.

## Verification
The accompanying `verify.py` independently enumerates all symmetric circulant first rows with row sum \(1\), forms the corresponding matrices, and evaluates their determinants using finite-field Gaussian elimination (not the proof's root-factor formula). It compares every determinant fiber against the closed formulas for 44 order/field cases across \(\mathbb F_3,\mathbb F_5,\mathbb F_7,\mathbb F_{11},\mathbb F_9\), including eight cases where the characteristic divides the index. It checks 19,740 matrices in total. The exact observed output is documented in `VERIFICATION.md`. Finite checks corroborate, but are not the universal proof.

## Relationship to prior work
Daniel Appel's archival *Regular Circulant Matrices* (arXiv:0909.3507v1, first public 18 September 2009) determines counts of unrestricted invertible circulants over finite fields and observes uniform nonzero determinant fibers in that unrestricted class. These are different objects from symmetric circulants of prescribed row sum: the involution ties reciprocal eigenvalues, introduces a square-class restriction in odd orders, and leaves a special factor at \(-1\) in even orders. The present result proves the complete distribution on that normalized symmetric subalgebra, including indices divisible by the characteristic; unrestricted uniformity does not imply this distribution. The finite-field polynomial representation of circulants is standard.

The related 1994 article by Jungnickel, Beth and Geiselmann on *orthogonal* circulants was located bibliographically; the full text was not available for a decisive comparison, and orthogonality is a different restriction. Searches for normalized symmetric/reversible circulant determinant fibers did not locate equivalent coverage. This absence does not establish novelty independently of the mathematical implication comparisons.

## Limitations
This theorem assumes odd field characteristic. The involution-averaging step fails as stated in characteristic \(2\); no claim is made for even finite fields. The matrices are unrestricted except for symmetry and row sum exactly \(1\); the classification does not address additional sparsity, nonnegative integer entries, or restrictions on individual coefficients. The claim has been checked by the same research process, not independently certified, and possible equivalent statements in older specialized finite-field/circulant literature remain a residual originality risk.

## References
1. D. Appel, *Regular Circulant Matrices*, arXiv:0909.3507v1, first posted 18 September 2009, https://arxiv.org/abs/0909.3507.
2. D. Jungnickel, T. Beth and W. Geiselmann, *A note on orthogonal circulant matrices over finite fields*, Archiv der Mathematik 62 (1994), 126–133, DOI 10.1007/BF01198667 (bibliographic details only inspected).
3. A. Muratović, *Representation of Polynomials Over Finite Fields With Circulants*, Sarajevo Journal of Mathematics 1 (2005), 21–26, DOI 10.5644/SJM.01.1.04 (abstract inspected).
