# Fourier saturation and a real three-dimensional obstruction for joint numerical indices

## Finding

For a scalar field \(\mathbb F\in\{\mathbb R,\mathbb C\}\), let \(X=\ell_1^m(\mathbb F)\), where \(m\ge1\). For integers \(k\ge1\) and real exponents \(2\le p<\infty\), define the joint numerical index below. Then:

1. **Complex saturation.** For every \(1\le k\le m\),
   \[
   n_{(p,k)}(\ell_1^m(\mathbb C))=k^{-1/p}.
   \]
2. **Real dyadic saturation.** If \(m\ge 2^{\lceil\log_2 k\rceil}\), with the power interpreted as \(1\) when \(k=1\), then
   \[
   n_{(p,k)}(\ell_1^m(\mathbb R))=k^{-1/p}.
   \]
3. **Dimension and scalar-field obstructions.** Over either scalar field, if \(k>m\), then
   \[
   n_{(p,k)}(\ell_1^m(\mathbb F))>k^{-1/p}.
   \]
   In addition, the first equal-size odd real case satisfies
   \[
   n_{(2,3)}(\ell_1^3(\mathbb R))>3^{-1/2}
   =n_{(2,3)}(\ell_1^3(\mathbb C)).
   \]
4. **Infinite-index consequence.** For any infinite index set \(I\), both real and complex \(\ell_1(I)\) satisfy \(n_{(p,k)}(\ell_1(I))=k^{-1/p}\) for every finite \(k\ge1\).

The strict inequalities concern the actual infima, not merely exclusion of equality for a particular construction.

## Assumptions and scope

Let \(\mathcal T=(T_1,\ldots,T_k)\) be bounded operators on \(X\), and write
\[
\|\mathcal T\|_p=\sup_{\|x\|_1=1}\Big(\sum_{i=1}^k\|T_i x\|_1^p\Big)^{1/p},
\qquad
w_p(\mathcal T)=\sup_{(x,f)\in\Pi_X}\Big(\sum_{i=1}^k|f(T_i x)|^p\Big)^{1/p},
\]
where \(\Pi_X=\{(x,f):\|x\|_1=\|f\|_\infty=1,\ f(x)=1\}\). Here a complex functional is complex-linear. The index is
\[
n_{(p,k)}(X)=\inf_{\|\mathcal T\|_p=1}w_p(\mathcal T).
\]
These are the joint operator norm and index from Mal, arXiv:2212.06500v1. Only finite \(p\ge2\) is asserted. The strictness statement for \(k>m\) uses finite-dimensional compactness; the infinite-index assertion does not claim analogous strictness.

## Proof

**1. Universal lower bound.** For each bounded \(T\) on \(\ell_1^m\), its norm is the largest \(\|Te_j\|_1\). For each \(j\), one can choose \(f\in\ell_\infty^m\) with \(\|f\|_\infty=1\), \(f(e_j)=1\), and \(|f(Te_j)|=\|Te_j\|_1\): take the phase of every other coordinate of \(f\) to align all nonzero terms with the prescribed \(j\)-th phase. Therefore \(w(T)=\|T\|\); the same follows for arbitrary \(\ell_1(I)\) by taking a supremum over coordinates. Consequently
\[
w_p(\mathcal T)\ge\max_i w(T_i)=\max_i\|T_i\|,
\quad
\|\mathcal T\|_p\le k^{1/p}\max_i\|T_i\|,
\]
so \(n_{(p,k)}(X)\ge k^{-1/p}\).

**2. Sharp unimodular orthogonal-column construction.** Assume that an integer \(q\le m\) admits a \(q\times q\) matrix \(U\) with unimodular entries, orthogonal columns \(U^*U=qI\), and first row consisting of ones. Choose its first \(k\le q\) columns, set
\[
v_i=q^{-1}\sum_{r=1}^q U_{ri}e_r,
\qquad T_i x=x_1v_i \quad(1\le i\le k),
\]
and extend all vectors by zeros to dimension \(m\) if necessary. Every \(\|v_i\|_1=1\), whence \(\|\mathcal T\|_p=k^{1/p}\), with equality at \(x=e_1\).

For any \((x,f)\in\Pi_X\), \(f(T_i x)=x_1f(v_i)\), and \(\|f\|_\infty=1\). Bessel's inequality applied to the first \(k\) columns of \(U/\sqrt q\) gives
\[
\sum_{i=1}^k |f(v_i)|^2
\le q^{-1}\sum_{r=1}^q|f(e_r)|^2\le1.
\]
Since \(p\ge2\), comparison of finite-dimensional sequence norms yields
\[
\Big(\sum_{i=1}^k|f(T_i x)|^p\Big)^{1/p}
\le |x_1|\Big(\sum_{i=1}^k|f(v_i)|^2\Big)^{1/2}\le1.
\]
Thus \(w_p(\mathcal T)\le1\). Equality is witnessed by \(x=e_1\) and the functional with coefficients \(f(e_r)=\overline{U_{r i_0}}\) on the block, where \(1\le i_0\le k\). The first-row condition gives \(f(e_1)=1\), while orthogonality gives \(f(v_i)=\delta_{ii_0}\). Hence \(w_p(\mathcal T)=1\), and division by \(k^{1/p}\) attains the universal lower bound.

For complex scalars take the discrete Fourier matrix of order \(q=m\); all its entries have modulus one, its first row is one, and its columns are orthogonal. For real scalars choose the Sylvester–Walsh matrix of dyadic order \(q=2^{\lceil\log_2 k\rceil}\), whenever \(q\le m\). For arbitrary infinite \(I\), embed a finite dyadic Walsh block into \(\ell_1(I)\) and use the same rank-one operators, establishing the infinite-index clause.

**3. The general dimension obstruction.** Suppose \(k>m\) and equality in the lower bound were attained. Rescale the tuple so that \(w_p(\mathcal T)=1\) and \(\|\mathcal T\|_p=k^{1/p}\). The equalities \(\|T_i\|=w(T_i)\le1\) hold for all \(i\). Since the joint norm on finite-dimensional \(\ell_1^m\) attains its maximum on a coordinate vector, some \(j\) satisfies
\[
\sum_{i=1}^k \|T_i e_j\|_1^p=k.
\]
Every summand is at most one, so the columns \(v_i=T_i e_j\) all have \(\|v_i\|_1=1\). For each \(i\), choose a unit dual functional \(f^{(i)}\) with \(f^{(i)}(e_j)=1\) and \(|f^{(i)}(v_i)|=1\), using the same coordinate-phase argument from step 1. Because the joint numerical radius equals one,
\[
\sum_{h=1}^k|f^{(i)}(v_h)|^p\le1,
\]
forcing \(f^{(i)}(v_h)=0\) whenever \(h\ne i\). This gives a dual biorthogonal family, so the \(k\) vectors \(v_i\) are linearly independent in dimension \(m\), a contradiction. Finally, both norms vary continuously with the finite matrix tuple, and the joint-operator-norm unit sphere is compact. Thus the infimum is attained and failure of equality gives a **strict** inequality.

**4. The real three-dimensional obstruction.** Assume by contradiction \(n_{(2,3)}(\ell_1^3(\mathbb R))=3^{-1/2}\). Compactness and the normalization above give a coordinate \(j\) and three real columns \(v_i\), each of \(\ell_1\)-norm one, for which the matrix \(V=(v_1\ v_2\ v_3)\) satisfies
\[
\|V^{\mathsf T}s\|_2^2\le1\qquad(s\in\{\pm1\}^3).
\]
Indeed, take \(f=s\) and \(x=s_j e_j\) in the norming-pair definition. Averaging the displayed inequality over all eight signs and using sign orthogonality gives
\[
\sum_{i=1}^3\|v_i\|_2^2=\mathbb E_s\|V^{\mathsf T}s\|_2^2\le1.
\]
By Cauchy–Schwarz, \(\|v_i\|_2^2\ge\|v_i\|_1^2/3=1/3\), so equality must hold everywhere. Thus all nine entries of \(V\) have modulus \(1/3\), and \(\|V^{\mathsf T}s\|_2^2=1\) for every sign vector. Fourier orthogonality on the sign cube forces the off-diagonal coefficients of the quadratic form \(s\mapsto s^{\mathsf T}VV^{\mathsf T}s\) to vanish. Since each diagonal coefficient is \(1/3\),
\[
VV^{\mathsf T}=\tfrac13 I_3.
\]
Putting \(H=3V\) would give a three-by-three sign matrix with \(HH^{\mathsf T}=3I_3\), impossible: the scalar product of two sign vectors of odd length three is an odd integer and cannot be zero. Compactness gives a strictly positive gap above \(3^{-1/2}\). The complex Fourier construction for \(m=k=3\) achieves exactly \(3^{-1/2}\), completing the scalar-field separation.

## Verification

Run `python3 verification/check_joint_index.py` with Python's standard library. The program constructs real Walsh matrices of orders \(1,2,4,8,16\) and complex Fourier matrices of orders \(2,3,5,6,7,9\); it checks Gram orthogonality, exact real sign-vector inequalities in smaller dimensions, bounded random complex phases, finite rational-style norm-witness identities, and exhausts all \(2^9\) three-by-three sign matrices for the odd-order obstruction. It also checks the universal lower-bound inequality on finite random integer tuples. The observed output is:

`VERIFY_OK checks=19847 real_orders=1,2,4,8,16 complex_orders=2,3,5,6,7,9 odd_hadamard_order3=excluded analytical_proof_required=True`

This finite checker tests examples; the unrestricted quantifiers, infinite-dimensional case, and strictness of index infima are proved analytically above and are not inferred from enumeration.

## Relationship to prior work

Arpita Mal's arXiv:2212.06500v1 (13 December 2022), Theorems 3.1 and 3.9, introduces the same joint-index normalization, proves the universal lower bound, gives exact values for \(\ell_\infty\) with arbitrary tuple length up to dimension, but obtains the corresponding \(\ell_1\) values only for two-tuples. Her Example 2.7 explicitly notes that taking adjoints does not preserve the joint operator norm, so the \(\ell_\infty\) result does not imply this new \(\ell_1\) formula by Banach duality. The present proof supplies an independent Fourier–Walsh construction, a dimension obstruction, and a real-versus-complex separation.

Mal's arXiv:2507.04700v1 develops subdifferentials and Gâteaux differentiation of the joint numerical-radius norm, not the optimal ratio defining this index. Grover–Singla's arXiv:2201.03055v1 treats joint-radius subdifferentials for Hilbert-space matrix tuples. Neither statement implies the sharp \(\ell_1\) formulas or the sign-parity exclusion here.

## Limitations

The exact index for general real non-dyadic pairs \((m,k)\) with \(3\le k\le m<2^{\lceil\log_2k\rceil}\), including the numerical value at \((m,k,p)=(3,3,2)\), is not determined. Only its strict separation from the universal lower bound is established in the smallest case. The formulas are proved for \(p\ge2\), and no claim is made for \(1\le p<2\). Exhaustive checks are finite; comprehensive prior-art coverage of unpublished or unindexed formulations is not claimed.

## References

1. A. Mal, *On joint numerical radius of operators and joint numerical index of a Banach space*, arXiv:2212.06500v1, first publicly posted 13 December 2022. Full text: https://arxiv.org/html/2212.06500v1. Relevant Theorems 2.6, 3.1, 3.9, Example 2.7.
2. A. Mal, *Joint numerical radius of Tuples: Extreme points, subdifferential set and Gateaux derivative*, arXiv:2507.04700v1 (2025). Full text: https://arxiv.org/html/2507.04700v1.
3. P. Grover and S. Singla, *Subdifferential of the joint numerical radius*, arXiv:2201.03055v1 (2022). Full text: https://arxiv.org/html/2201.03055v1.
