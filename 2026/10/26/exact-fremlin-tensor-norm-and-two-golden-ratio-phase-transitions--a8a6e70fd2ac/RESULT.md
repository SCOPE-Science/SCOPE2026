# Exact Fremlin tensor norm and two golden-ratio phase transitions for a three-point path

## Finding

Let \(E=\ell_2^3(\mathbb R)\) with its coordinate Banach-lattice order, let \(S_3\) be the upper one-step shift, and let \(M_t=I_3+tS_3\), \(t\ge0\). Write \(\varphi=(1+\sqrt5)/2\). Then

\[
\boxed{\|M_t\|_{|\pi|}=\begin{cases}
3,&0\le t\le1,\\
1+t^2+t^{-2},&1\le t\le\sqrt\varphi,\\
2\sqrt{1+t^2},&t\ge\sqrt\varphi.
\end{cases}}
\]

Here the matrix is identified with the element \(\sum_{i,j}(M_t)_{ij}e_i\otimes e_j\) of \(E\otimes E\). The function is continuously differentiable on \([0,\infty)\) and has precisely two failures of twice differentiability in its interior, at \(t=1\) and \(t=\sqrt\varphi\). Each branch has explicit primal and dual optimizers.

## Assumptions and scope

All spaces and tensors are real. For a coordinatewise nonnegative matrix \(M\), the Fremlin positive projective tensor norm admits the finite-dimensional primal and dual descriptions

\[
\Gamma(M)=\inf\left\{\sum_{k=1}^r\|u_k\|_2\|v_k\|_2:\ u_k,v_k\ge0,\ M\le\sum_{k=1}^r u_kv_k^{\mathsf T}\text{ entrywise}\right\},
\]

\[
\Gamma(M)=\max\{\langle M,N\rangle:\ N\ge0,\ \|N\|_{2\to2}\le1\}.
\]

The first expression is the positive-projective gauge defining the positive cone norm, while the second is its finite-dimensional conic dual. For positive matrices, the regular-bilinear dual bound agrees with the ordinary Euclidean operator norm because a positive matrix attains its operator norm on nonnegative vectors. Every feasible positive rank-one majorant thus gives an upper bound; every feasible positive contraction gives a lower bound. No infinite-dimensional or complex-lattice assertion is made.

## Proof

**The regime \(0\le t\le1\).** The all-ones rank-one matrix majorizes \(M_t\), with tensor cost \(\|(1,1,1)\|_2^2=3\). The dual positive contraction \(N=I_3\) pairs with \(M_t\) to give \(3\). Hence equality holds.

**The regime \(1\le t\le\sqrt\varphi\).** Define

\[
u=(1,t^{-1},t^{-2})^{\mathsf T},\qquad v=(1,t,t^2)^{\mathsf T}.
\]

The rank-one matrix \(uv^{\mathsf T}\) majorizes \(M_t\): each diagonal entry is one and each first superdiagonal entry is \(t\). Its tensor cost is

\[\|u\|_2\|v\|_2=1+t^2+t^{-2}.\]

Set \(a=t^{-2}\), \(b=t-t^{-3}\), and \(c=1-t^2+t^{-2}\), and define

\[
N=\begin{pmatrix}a&b&0\\0&c&b\\0&0&a\end{pmatrix}.
\]

In the stated interval \(a,b,c\ge0\), since \(t^4-t^2-1\le0\). Direct multiplication gives \(Nv=t^2u\) and \(N^{\mathsf T}u=t^{-2}v\). Therefore \(Dv=0\) for the real symmetric matrix \(D=I_3-N^{\mathsf T}N\). Its two off-diagonal entries are nonpositive: \(D_{12}=-ab\) and \(D_{23}=-bc\). For every real \(z\), the exact ground-state identity yields

\[
z^{\mathsf T}Dz=abv_1v_2\left(\frac{z_1}{v_1}-\frac{z_2}{v_2}\right)^2+bcv_2v_3\left(\frac{z_2}{v_2}-\frac{z_3}{v_3}\right)^2\ge0.
\]

Thus \(N^{\mathsf T}N\le I_3\) and \(\|N\|_{2\to2}\le1\). Moreover

\[
\langle M_t,N\rangle=2a+c+2tb=1+t^2+t^{-2}.
\]

The upper and lower bounds coincide.

**The regime \(t\ge\sqrt\varphi\).** Write \(h=\sqrt{1+t^2}\), \(a=h^{-1}\), and \(b=t/h\). The positive matrix

\[
N=\begin{pmatrix}a&b&0\\0&0&b\\0&0&a\end{pmatrix}
\]

has spectral norm one: its first row is orthogonal to the remaining rows, its first-row norm is one, and the remaining two rows constitute a single column of total Euclidean norm one. Consequently, \(\langle M_t,N\rangle=2a+2tb=2h\).

For the converse, put \(x=(1,b,a)^{\mathsf T}\), \(y=(a,b,1)^{\mathsf T}\). The rank-one positive matrix \(hxy^{\mathsf T}\) has diagonal entries \(1,t^2/h,1\) and first superdiagonal entries \(t,t\). It majorizes \(M_t\) exactly when \(t^2/h\ge1\), equivalent to \(t^2\ge\varphi\). Since \(\|x\|_2=\|y\|_2=\sqrt2\), its tensor cost is \(2h\), attaining the dual bound.

**Transition regularity.** At \(t=1\), the first two formulas and first derivatives agree, but the second derivatives are \(0\) and \(8\). At \(t=\sqrt\varphi\), the last two values and first derivatives agree by \(\varphi^2=\varphi+1\), whereas the middle second derivative \(2+6/\varphi^2\) differs from the last branch's \(2/(1+\varphi)^{3/2}\). Thus both transitions are genuine curvature discontinuities.

## Verification

The included `verify.py` checks the primal/dual inequalities, exact rational algebra and contraction certificates throughout rational samples of the middle phase, and independently tests the rank-one domination and row-orthogonality assertions in the large phase. These checks corroborate but do not replace the all-parameter proof above.

## Relationship to prior work

The Fremlin projective tensor norm is a standard positive tensor-product norm; see D. H. Fremlin, *Tensor products of Banach lattices* (1974). A recent paper by Jaber and Troudi (arXiv:2610.13734, publicly submitted 2026-10-09) examines Arens regularity of tensor products of Banach lattice algebras and supplies context, but its results concern Arens regularity, not the precise norm of this three-point path tensor. The claim here is the exact parametric 3-by-3 evaluation and its two changes of optimizer, not invention of the positive-projective duality framework.

## Limitations

The theorem is confined to real \(\ell_2^3\) and the natural full parameter family \(I_3+tS_3\). It does not give arbitrary matrix formulas or higher-dimensional path norm formulas. A targeted literature and indexed-result search did not uncover an earlier equivalent formula; this is not a proof of publication priority. Earlier Fremlin-norm work has not all been inspected in full. Independent scientific validation has not been performed.

## References

1. D. H. Fremlin, *Tensor products of Banach lattices*, Mathematische Annalen **211** (1974), 87–106, https://doi.org/10.1007/BF01344164.
2. J. Jaber and M. Troudi, *The tensor product of the Fremlin tensor product of Banach lattice algebras*, arXiv:2610.13734v1 (2026-10-09), https://arxiv.org/abs/2610.13734.
3. S. Heinrich and N. J. Nielsen, *Order bounded operators and tensor products of Banach lattices*, Mathematica Scandinavica **49** (1981), 99–127, https://doi.org/10.7146/math.scand.a-11924.
