# The tensor-product \(g\)-fusion synthesis domain is not a vector space

## Finding
Note 3.2 of Ghosh--Samanta defines the coefficient object for tensor-product \(g\)-fusion frames by
\[
\ell^2(\{H_i\otimes K_j\})
=
\left\{
\{f_i\otimes g_j\}_{i,j}:
\sum_{i,j}\|f_i\otimes g_j\|^2<\infty
\right\}
\]
and states that it is a Hilbert space. Under the displayed formula, the same \(f_i\) is used across all columns and the same \(g_j\) across all rows. The resulting globally separable arrays are not closed under addition.

Let
\[
I=J=\{1,2\},\qquad H_i=K_j=\mathbb R.
\]
Consider
\[
A=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
B=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
\]
Both are outer-product arrays of the form prescribed in Note 3.2. Their sum is
\[
A+B=
\begin{pmatrix}
1&0\\
0&1
\end{pmatrix},
\]
which has determinant \(1\). Every prescribed array \((f_i g_j)_{i,j}\) has rank at most \(1\) and determinant \(0\). Hence \(A+B\) is not in the displayed set.

Thus the coefficient object of Note 3.2 is not a vector space. Consequently, the synthesis operator in Note 3.5 is not a bounded linear operator on the claimed Hilbert domain as written, and the synthesis identity in Theorem 3.6 requires a type correction.

The natural coefficient Hilbert space is
\[
G=
\bigoplus_{(i,j)\in I\times J}^{\ell^2}
(H_i\otimes K_j).
\]
If
\[
E=\bigoplus_i^{\ell^2}H_i,
\qquad
F=\bigoplus_j^{\ell^2}K_j,
\]
there is a canonical unitary
\[
U:E\otimes F\to G
\]
given on simple coefficient tensors by
\[
U((f_i)_i\otimes(g_j)_j)
=
(f_i\otimes g_j)_{i,j}.
\]
The correct synthesis identity is
\[
T_{\Lambda\otimes\Gamma}U
=
T_\Lambda\otimes T_\Gamma.
\]

## Assumptions and scope
The counterexample concerns the literal coefficient-space formula printed in Note 3.2 and the synthesis construction that depends on it. It does not dispute the elementary fact that tensor products of suitable frame systems can again form frame systems.

The scalar choice \(H_i=K_j=\mathbb R\) removes all possible ambiguity about whether individual entries are legitimate elements of \(H_i\otimes K_j\). Each coefficient entry is simply a real number.

The repair uses the standard Hilbert direct sum over the product index set. It allows arbitrary square-summable coefficient arrays, including nonseparable arrays such as the identity matrix above.

## Proof
For \(I=J=\{1,2\}\) and scalar coefficient spaces, an element displayed in Note 3.2 has the form
\[
(f_i g_j)_{i,j}
=
\begin{pmatrix}
f_1g_1&f_1g_2\\
f_2g_1&f_2g_2
\end{pmatrix}.
\]
Its determinant is
\[
f_1f_2g_1g_2-f_1f_2g_2g_1=0.
\]
The two matrices
\[
A=e_1e_1^{\mathsf T},
\qquad
B=e_2e_2^{\mathsf T}
\]
both have this form, but
\[
\det(A+B)=1.
\]
Therefore the displayed coefficient set is not closed under addition.

For the repair, first define on algebraic simple tensors
\[
U_0((f_i)_i\otimes(g_j)_j)
=
(f_i\otimes g_j)_{i,j}.
\]
Its norm is
\[
\begin{aligned}
\|U_0((f_i)_i\otimes(g_j)_j)\|_G^2
&=
\sum_{i,j}\|f_i\otimes g_j\|^2\\
&=
\left(\sum_i\|f_i\|^2\right)
\left(\sum_j\|g_j\|^2\right)\\
&=
\|(f_i)_i\otimes(g_j)_j\|_{E\otimes F}^2.
\end{aligned}
\]
By polarization, the same calculation gives preservation of inner products on the algebraic tensor product, so \(U_0\) extends isometrically to
\[
U:E\otimes F\to G.
\]

For any \(i,j\), any \(x\in H_i\), and any \(y\in K_j\), the coefficient array supported only at \((i,j)\) with value \(x\otimes y\) lies in the range of \(U_0\). Finite linear combinations of such elementary tensors are dense in \(G\), so the extended isometry is onto and hence unitary.

On simple coefficient tensors, the synthesis calculation is
\[
\begin{aligned}
T_{\Lambda\otimes\Gamma}
U((f_i)_i\otimes(g_j)_j)
&=
\sum_{i,j}
v_iw_j
\left(P_{V_i}\Lambda_i^*f_i\right)
\otimes
\left(P_{W_j}\Gamma_j^*g_j\right)\\
&=
T_\Lambda((f_i)_i)
\otimes
T_\Gamma((g_j)_j).
\end{aligned}
\]
Both sides are bounded linear operators, so equality on the dense algebraic tensor product gives
\[
T_{\Lambda\otimes\Gamma}U
=
T_\Lambda\otimes T_\Gamma.
\]
Taking adjoints yields
\[
U^*T_{\Lambda\otimes\Gamma}^*
=
T_\Lambda^*\otimes T_\Gamma^*.
\]
Consequently
\[
\begin{aligned}
S_{\Lambda\otimes\Gamma}
&=
T_{\Lambda\otimes\Gamma}
T_{\Lambda\otimes\Gamma}^*\\
&=
(T_\Lambda\otimes T_\Gamma)
(T_\Lambda^*\otimes T_\Gamma^*)\\
&=
S_\Lambda\otimes S_\Gamma.
\end{aligned}
\]

## Verification
The open preprint was inspected at Note 3.2, Note 3.5, and Theorem 3.6 together with the complete synthesis-operator calculation. The page containing Note 3.2 and the page containing Theorem 3.6 were also inspected as page images.

Note 3.2 explicitly writes coefficient families as \(\{f_i\otimes g_j\}_{i,j}\), factorizes their proposed inner product into the product of the two one-factor direct-sum inner products, and then declares the resulting set complete and Hilbert.

Theorem 3.6 proves the synthesis identity only on those factorized coefficient arrays. That calculation is correct on simple coefficient tensors; the error is identifying the simple-tensor locus with the full Hilbert coefficient space.

The repaired unitary is verified directly from the tensor norm and density of finitely supported elementary coefficient tensors. No numerical approximation is used.

## Relationship to prior work
Khosravi--Mirzaee Azandaryani study fusion frames and \(g\)-frames in tensor products and direct sums of Hilbert spaces using the standard Hilbert-space tensor-product framework. Their results establish tensor-product frame phenomena but do not identify the coefficient-space defect in the later \(g\)-fusion construction.

Balazs--Teofanov treat continuous frames in full tensor-product Hilbert spaces and explicitly discuss non-simple tensor-product frames. This underscores the structural distinction between a Hilbert tensor product and its simple-tensor locus.

The correction here preserves the intended product synthesis calculation: simple coefficient tensors remain a dense test class, but the bounded operator must act on the completed Hilbert direct sum \(G\), and the canonical unitary \(U\) must be included when comparing domains.

## Limitations
If the notation in Note 3.2 was intended informally to denote the full Hilbert direct sum rather than the set literally displayed, then the vector-space defect is a notation/definition defect rather than an intended restriction. Even under that charitable reading, the bare equality
\[
T_{\Lambda\otimes\Gamma}=T_\Lambda\otimes T_\Gamma
\]
still suppresses the canonical unitary identifying their different natural domains.

The result does not claim that the frame-operator tensor identity is false; after the coefficient-space repair, that identity remains valid.

No claim is made about tensor products of more than two coefficient direct sums beyond the analogous standard unitary identification.

## References
1. P. Ghosh and T. K. Samanta, *Generalized fusion frame in tensor product of Hilbert spaces*, arXiv:2101.06857v1, 18 January 2021; Journal of the Indian Mathematical Society 89(1--2) (2022), 58--71, DOI 10.18311/jims/2022/29307.
2. A. Khosravi and M. Mirzaee Azandaryani, *Fusion frames and \(g\)-frames in tensor product and direct sum of Hilbert spaces*, Applicable Analysis and Discrete Mathematics 6 (2012), 287--303, DOI 10.2298/AADM120619014K.
3. P. Balazs and N. Teofanov, *Continuous frames in tensor product Hilbert spaces, localization operators and density operators*, arXiv:2107.06628; Journal of Physics A: Mathematical and Theoretical 55 (2022), 145201.
