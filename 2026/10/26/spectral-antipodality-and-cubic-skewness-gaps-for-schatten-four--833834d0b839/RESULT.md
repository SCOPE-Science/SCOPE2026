# Spectral antipodality and cubic skewness gaps for Schatten-four commutator costs

## Finding

For a complex Hilbert space \(H\) and a nonzero commutator \(T=[X,Y]\) with \(X,Y\in\mathcal S_4(H)\), define \(Q=XY+YX\). Then \(T,Q\in\mathcal S_2(H)\), and the following **cubic trace identity and quantitative factor-cost obstruction** hold:
\[
\operatorname{tr}(T^3)=-3\operatorname{tr}(Q^2T),\qquad
\|X\|_4^2\|Y\|_4^2\ge\frac14\left(\|T\|_2^2+\frac{|\operatorname{tr}(T^3)|}{3\|T\|}\right).
\]
In particular, when the cubic spectral moment is nonzero, the elementary lower cost \(\|T\|_2/2\) is strictly unattainable and quantitatively improved.

For a nonzero **normal, trace-zero** complex \(n\times n\) matrix \(T\), \(n\ge2\), set
\[
\kappa_2(T)=\min\{\|X\|_4\|Y\|_4:X,Y\in M_n(\mathbb C),\ [X,Y]=T\}.
\]
The minimum is well-defined and attained. The **exact saturation criterion** is
\[
\boxed{\ \kappa_2(T)=\tfrac12\|T\|_2\quad\Longleftrightarrow\quad
\text{the multiset of nonzero eigenvalues of }T\text{ is invariant under }\lambda\mapsto-\lambda.\ }
\]
For every such antipodally paired normal target, explicit same-size Schatten-four factors attain equality. No formula for \(\kappa_2(T)\) is asserted in the nonpaired case.

## Assumptions and scope

All Hilbert spaces are complex; \(\|\cdot\|_p\) is the Schatten \(p\)-norm, \(\|\cdot\|\) the operator norm, and the trace is unnormalized. The cubic inequality holds on arbitrary complex Hilbert spaces whenever \(X,Y\in\mathcal S_4\) and \([X,Y]\ne0\). The exact equality classification for the infimum concerns same-dimension matrix factorizations of nonzero normal trace-zero \(n\times n\) targets. Eigenvalue multiplicities are counted algebraically (equal geometrically for normal matrices); zero eigenvalues are unconstrained.

## Proof

**1. Trace identity.** Put \(A=XY\), \(B=YX\), \(T=A-B\), and \(Q=A+B\). Schatten Hölder gives \(A,B\in\mathcal S_2\), hence \(A^3,B^3,T^3,Q^2T\) are trace class. Cyclicity gives \(\operatorname{tr}(A^3)=\operatorname{tr}(B^3)\); this also follows by finite-rank approximation of \(X,Y\) in \(\mathcal S_4\) followed by trace-norm continuity. Expanding \(A=(Q+T)/2\) and \(B=(Q-T)/2\), then cyclically collecting terms, yields
\[
0=\operatorname{tr}(A^3-B^3)=\tfrac14\bigl(3\operatorname{tr}(Q^2T)+\operatorname{tr}(T^3)\bigr).
\]
This is the claimed exact identity.

**2. Quantitative obstruction.** The Hilbert–Schmidt parallelogram identity and Schatten Hölder imply
\[
\|T\|_2^2+\|Q\|_2^2
=2\|XY\|_2^2+2\|YX\|_2^2
\le4\|X\|_4^2\|Y\|_4^2.
\]
Also
\[
|\operatorname{tr}(T^3)|=3|\operatorname{tr}(Q^2T)|
\le3\|T\|\,\|Q^2\|_1
\le3\|T\|\,\|Q\|_2^2.
\]
Combining establishes the displayed lower bound. It does not assume that \(T\) is normal.

**3. Matrix factorization existence and attainment.** Every finite trace-zero matrix has a same-size commutator representation. Indeed, diagonalize a normal target as \(V\operatorname{diag}(\lambda_j)V^*\), conjugate the diagonal by the discrete Fourier matrix so that every diagonal entry becomes \(n^{-1}\sum_j\lambda_j=0\), and write the resulting zero-diagonal matrix as \([D,Z]\) with \(D=\operatorname{diag}(1,\ldots,n)\), \(Z_{ij}=H_{ij}/(i-j)\) for \(i\ne j\), \(Z_{ii}=0\). Undo the unitary conjugations. For a minimizing sequence, reciprocally rescale \(X,Y\) so that \(\|X\|_4=\|Y\|_4\); the balanced factors remain bounded, and finite-dimensional compactness supplies an attaining pair.

**4. Necessity of antipodal eigenvalues at equality.** Suppose an attaining pair has \(\|X\|_4\|Y\|_4=\|T\|_2/2\). The parallelogram inequality in Step 2 forces \(\|Q\|_2=0\). Thus \(XY=T/2\) and \(YX=-T/2\). Sylvester's determinant identity \(\det(I-zXY)=\det(I-zYX)\) shows that the two products have the same nonzero eigenvalues with algebraic multiplicities. Therefore \(T\) has antipodally symmetric nonzero spectrum.

**5. Sufficiency and explicit minimizers.** Suppose that a normal \(T\ne0\) has antipodally paired eigenvalues. Let \(T=U|T|\) be its polar decomposition, with \(U=0\) on the kernel. Pair the orthogonal eigenspaces at \(\lambda\) and \(-\lambda\) to construct a self-adjoint unitary involution \(J\), acting as the identity on the kernel, such that \(JTJ=-T\). Thus \(J|T|J=|T|\) and \(JUJ=-U\). Define
\[
X=J|T|^{1/2},\qquad Y=\tfrac12 JU|T|^{1/2}.
\]
Then \(XY=T/2\) and \(YX=-T/2\), so \([X,Y]=T\). Since the singular values of \(X\) are the square roots of those of \(|T|\), and those of \(Y\) are half as large,
\[
\|X\|_4\|Y\|_4=\tfrac12\|T\|_2.
\]
This attains the universal lower bound and proves the equivalence.

## Verification

All calculations above are analytic and dimension-independent where stated. The supplementary program `verify_commutator.py` checks the trace identity and quantitative inequality on deterministic complex test matrices, verifies explicit symmetric-spectrum equality factors, and checks a skewed three-level example. Run with `python3 verify_commutator.py` (NumPy required). Tests are not a substitute for the matrix or infinite-dimensional proofs.

For \(T=\operatorname{diag}(2,-1,-1)\), the cubic moment is \(6\), the squared Hilbert–Schmidt norm is \(6\), and the operator norm is \(2\). The bound is therefore
\[
\kappa_2(T)\ge\sqrt7/2>\sqrt6/2.
\]
For the cyclic permutation \(U_0 e_j=e_{j+1\;\mathrm{mod}\;3}\), put \(D=\operatorname{diag}(-1,0,1)\), \(X=U_0\operatorname{diag}(1,0,1)\), \(Y=DU_0^*\). Then \([X,Y]=T\) and \(\|X\|_4\|Y\|_4=\sqrt2\), giving \(\sqrt7/2\le\kappa_2(T)\le\sqrt2\). The exact cost in this nonpaired example is not determined here.

## Relationship to prior work

Liu, *Every compact operator is a commutator of compact operators*, arXiv:2609.20672v1 (first public 2026-09-17), establishes a universal compact-factor existence theorem and operator-norm bounds. A nearby quantitative normal-target result, *Rank-free mixed Schatten commutator cost for finite-rank normal operators* (public mathematical record, September 2026), proves comparison estimates for \(1/p+1/q<1/2\), strictly excluding the critical \(p=q=4\) case here. The later Liu–Yang paper *Single commutators in Schatten ideals*, arXiv:2610.27024 (first public 2026-10-19), treats target exponents strictly greater than two. Ordinary Schatten Hölder yields the baseline \(\kappa_2(T)\ge\|T\|_2/2\), but none of these inspected statements gives this spectral saturation classification or the displayed cubic-moment improvement.

## Limitations

The cubic-moment bound is not asserted optimal for nonsymmetric targets, and vanishing cubic moment need not imply spectral antipodality. The equality-if-and-only-if claim is made for normal finite matrices and same-size factors; no arbitrary infinite-dimensional attainment theorem is claimed. The argument does not classify nonnormal equality targets. The exact cost for a nonsymmetric normal spectrum is not determined. Older operator-ideal or trace-inequality literature may contain equivalent formulations of the cubic obstruction or the saturation test; publication priority is not independently certified. The related Tran 2026 matrix-commutator paper could be assessed only from its abstract, not complete text.

## References

1. Z. Liu, *Every compact operator is a commutator of compact operators*, arXiv:2609.20672v1 (2026). https://arxiv.org/abs/2609.20672
2. *Rank-free mixed Schatten commutator cost for finite-rank normal operators*, publicly indexed mathematical record (2026). https://github.com/Resultary/2026/tree/main/2026/9/19/SCOPE-rank-free-schatten-commutator-cost-normal-operators--1bafe9c58890
3. Z. Liu and S. Yang, *Single commutators in Schatten ideals*, arXiv:2610.27024v1 (2026). https://arxiv.org/abs/2610.27024
4. T. Tran, *Quantum expanders and dimension-free commutator bounds*, arXiv:2609.20161v1 (2026). https://arxiv.org/abs/2609.20161
5. K. Dykema, T. Figiel, G. Weiss, and M. Wodzicki, *The commutator structure of operator ideals*, Adv. Math. 185 (2004), 1–79. https://doi.org/10.1016/S0001-8708(03)00141-5
