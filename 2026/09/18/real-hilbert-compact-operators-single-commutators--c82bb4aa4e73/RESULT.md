# Every compact operator on a real Hilbert space is a compact commutator

## Result

Let \(H\) be a separable infinite-dimensional real Hilbert space. There is an absolute constant \(C_{\mathbb R}>0\) such that every compact real-linear operator \(T\in\mathcal K(H)\) admits compact real-linear factors \(A,B\in\mathcal K(H)\) with
\[
T=[A,B],\qquad
\max\{\|A\|,\|B\|\}\le C_{\mathbb R}\|T\|^{1/2}.
\]

Zhichao Liu proved this statement for complex Hilbert spaces. The real extension is not obtained by simply forgetting complex scalars: Liu's non-trace-class reduction uses complex phases and the ability to multiply an operator by \(i\). The real proof below replaces those steps, while Tuan Tran's dimension-free real matrix commutator theorem supplies the finite-dimensional input.

## Literature inputs

Liu proves that every compact operator on a separable infinite-dimensional complex Hilbert space is a single commutator of compact operators with a universal square-root norm bound; his paper explicitly assumes all Hilbert spaces are complex.

Tran proves that for \(\mathbb F\in\{\mathbb R,\mathbb C\}\), every traceless \(D\in M_n(\mathbb F)\) has same-field factors
\[
D=[U,V],\qquad \|U\|\,\|V\|\le K\|D\|,
\]
where \(K\) is absolute and independent of \(n\).

References:

- Z. Liu, *Every compact operator is a commutator of compact operators*, arXiv:2609.20672 (2026), https://arxiv.org/abs/2609.20672.
- T. Tran, *Quantum expanders and dimension-free commutator bounds*, arXiv:2609.20161 (2026), https://arxiv.org/abs/2609.20161.
- J. Anderson, *Commutators of compact operators*, J. Reine Angew. Math. 291 (1977), 128--132, https://doi.org/10.1515/crll.1977.291.128.
- D. Beltiţă, S. Patnaik, G. Weiss, *B(H)-Commutators: A Historical Survey II and recent advances on commutators of compact operators*, arXiv:1303.4844.
- P. Fan, *On the diagonal of an operator*, Trans. Amer. Math. Soc. 283 (1984), 239--251, https://doi.org/10.1090/S0002-9947-1984-0735419-8.
- P. Fan and C.-K. Fong, *Operators similar to zero diagonal operators*, Proc. Roy. Irish Acad. Sect. A 87A (1987), 147--153.

## Proof

### 1. Zero-diagonal compact operators over the real field

Assume \(T\in\mathcal K(H)\) has zero diagonal in a real orthonormal basis. Liu's Proposition 2.8 partitions that basis into finite blocks. Each diagonal compression is traceless; the only field-sensitive input is a dimension-free finite-matrix commutator bound. Replacing Liu's complex matrix input by Tran's theorem gives real finite-block factors with uniform control. The remaining scalar shifts, Sylvester equations, Neumann series, block estimates, and compactness argument are all valid over \(\mathbb R\).

Hence there is an absolute \(C_0\) such that every real zero-diagonal compact operator satisfies
\[
T=[A,B],\qquad A,B\in\mathcal K(H),\qquad
\|A\|\,\|B\|\le C_0\|T\|.
\]
The same replacement makes Liu's block-assembly lemma valid over \(\mathbb R\).

### 2. Real self-adjoint zero-diagonal lemma

We need only the following self-adjoint form of the diagonal theorem.

**Lemma.** Let \(S=S^*\in\mathcal K(H)\) be real self-adjoint. If either

1. \(S\) is trace class and \(\operatorname{Tr}S=0\), or
2. \(\operatorname{Tr}S_+=\operatorname{Tr}S_-=\infty\),

then \(S\) has zero diagonal in a real orthonormal basis.

**Proof.** Diagonalize \(S\) over \(\mathbb R\), with positive eigenvectors \(p_j\), negative eigenvectors \(n_j\), and eigenvalues \(\alpha_j>0\), \(-\beta_j<0\). On two orthogonal vectors \(u,v\) whose quadratic values are \(a>0\) and \(-b<0\), and whose \(S\)-cross term is zero, the real rotation
\[
w=\sqrt{\frac{b}{a+b}}\,u+\sqrt{\frac{a}{a+b}}\,v
\]
has \(\langle Sw,w\rangle=0\); the orthogonal vector carries residual quadratic value \(a-b\).

Starting from the eigenbasis, repeatedly combine the current residual with an unused eigenvector of the opposite sign. Each step emits one zero-diagonal vector. In the finite-trace case equality of the positive and negative traces forces the residual quadratic value to tend to zero. In the infinite-trace case alternate at each sign crossing; compactness gives \(\alpha_j,\beta_j\to0\), so the crossing overshoots tend to zero. Every eigenvector is eventually introduced, and the moving residual converges weakly to zero, so the emitted vectors are complete in the nonzero spectral subspace. Append an orthonormal basis of \(\ker S\). \(\square\)

Consequently, if a compact real operator \(X\) has an orthonormal basis and a subsequence of partial diagonal sums tending to \(0\), then \(X\) has zero diagonal. Indeed its diagonal equals that of
\[
S=\frac{X+X^*}{2}.
\]
For any orthonormal basis, Tonelli gives
\[
\sum_j\langle S_+e_j,e_j\rangle=\operatorname{Tr}S_+,\qquad
\sum_j\langle S_-e_j,e_j\rangle=\operatorname{Tr}S_-.
\]
A subsequence of partial sums can approach \(0\) only if both traces are finite and equal, or both are infinite. The lemma applies.

### 3. Non-trace-class operators

Write
\[
T=S+K,\qquad S=\frac{T+T^*}{2},\qquad K=\frac{T-T^*}{2}.
\]

If \(S\notin\mathcal S_1\), Liu's bounded-similarity argument has a real version. After deleting a trace-class corner, diagonalize the remaining symmetric part. The relevant diagonal coefficients \(a_n\) are real, tend to zero, and satisfy \(\sum|a_n|=\infty\). Split the indices into two subsets, each carrying divergent \(\sum|a_n|\), and choose \(q_n\in\{-1,1\}\) so that \(q_na_n\) has the prescribed sign. Liu's \(2\times2\) blocks
\[
R_n=
\begin{pmatrix}
1&1\\
-q_n&1-q_n
\end{pmatrix}
\]
are then real and uniformly conditioned. The trace-class error has absolutely summable diagonal, so the same greedy tail selection produces a subsequence of partial diagonal sums tending to zero. Step 2 yields a real zero diagonal after a real orthogonal change of basis.

The genuinely new real issue occurs when \(S\in\mathcal S_1\). Then \(K\notin\mathcal S_1\). A compact real skew-adjoint operator is an orthogonal sum of rotation blocks
\[
K|_{E_n}=s_n
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\]
and a kernel, with \(\sum_ns_n=\infty\). On every \(E_n\), put
\[
D=\operatorname{diag}(2,1/2).
\]
The block-diagonal similarity \(R=\bigoplus D\) has
\[
\|R\|=\|R^{-1}\|=2,
\]
and direct calculation gives
\[
\operatorname{Sym}\!\left(
D^{-1}s_n
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
D\right)
=
\frac{15s_n}{8}
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]
Its trace norm is \(15s_n/4\). Therefore the symmetric part of \(R^{-1}KR\) is not trace class. The symmetric part of \(R^{-1}SR\) remains trace class, so
\[
\operatorname{Sym}(R^{-1}TR)\notin\mathcal S_1.
\]
We are reduced to the previous case.

Thus every non-trace-class real compact operator is boundedly similar, with a universal condition-number bound, to a zero-diagonal real compact operator. Step 1 then gives a compact real commutator representation with universal product-norm control.

### 4. Trace-class operators

If \(T\in\mathcal S_1(H)\) and \(\operatorname{Tr}T=0\), then its symmetric part is trace class with trace zero. Step 2 gives a real zero diagonal, so Step 1 applies.

Suppose now that \(\operatorname{Tr}T\ne0\). Liu's finite-block trace-concentration lemma transfers to the real setting. Its only superficially complex step is the use of polarization to choose \(u\) with \(\langle Tu,u\rangle\ne0\). Here this is valid over \(\mathbb R\) because
\[
\operatorname{Tr}\frac{T+T^*}{2}=\operatorname{Tr}T\ne0;
\]
hence the symmetric part is nonzero and has a vector with nonzero quadratic form. The remaining idempotent and similarity construction is real-linear.

One obtains, after a uniformly bounded real similarity,
\[
\widehat T=
\begin{pmatrix}D&E\\F&G\end{pmatrix},
\]
where \(D\) has finite rank and \(G\) is trace class with trace zero.

Anderson's rank-one compact-commutator construction can be taken over \(\mathbb R\): its standard block matrices use real square-root coefficients, as displayed explicitly in Beltiţă--Patnaik--Weiss. Liu's tensor amplification therefore represents every finite-rank real \(D\) as a commutator of compact real operators with universal \(\|D\|^{1/2}\) control. The real block-assembly lemma from Step 1 combines that representation with the zero-diagonal representation of \(G\).

Hence there is an absolute \(C_1\) such that every real trace-class compact operator satisfies
\[
T=[A,B],\qquad \|A\|\,\|B\|\le C_1\|T\|.
\]

### 5. Balancing the factors

Combining the two cases gives an absolute \(C\) with
\[
T=[A,B],\qquad \|A\|\,\|B\|\le C\|T\|.
\]
For nonzero \(T\), replace \(A,B\) by \(cA,c^{-1}B\), where
\[
c=\sqrt{\frac{\|B\|}{\|A\|}}>0.
\]
This preserves the real commutator and gives
\[
\max\{\|cA\|,\|c^{-1}B\|\}
=\sqrt{\|A\|\,\|B\|}
\le C^{1/2}\|T\|^{1/2}.
\]
The theorem follows.

## Why this is not a formal corollary of the complex theorem

Complexifying \(T\) and applying Liu gives complex compact factors, but a single complex commutator does not automatically descend to a single commutator of real factors. The obstruction is visible inside Liu's proof: the complex non-trace-class reduction can rotate by \(i\) and steer two real coordinates with four phases \(\{1,-1,i,-i\}\).

The fixed similarity above supplies the missing real mechanism. A non-trace-class skew-adjoint component is converted, with condition number \(4\), into a non-trace-class symmetric component, after which only the signs \(\pm1\) are needed.

## Limitations

The theorem is stated for separable infinite-dimensional real Hilbert spaces. The universal constant is not optimized. No claim is made for arbitrary real Banach spaces, nonseparable Hilbert spaces, or factors constrained to a prescribed smaller operator ideal.

Originality is asserted only to the best of our knowledge. Searches by real-Hilbert, compact-commutator, Pearcy--Topping, and zero-diagonal terminology found no prior theorem covering all real compact operators with two real compact factors and universal norm control. The original full texts of Anderson (1977) and Fan--Fong (1987) were not exhaustively checked for a separately stated global real-field theorem, so they remain the principal residual prior-art risk.
