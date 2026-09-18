# Single commutators and trace rigidity in norm reduced products of finite von Neumann algebras

## Statement

Let \((M_n)_{n\ge 1}\) be nonzero finite von Neumann algebras and let
\[
T_n:M_n\to Z(M_n)
\]
be their normalized center-valued traces. Put
\[
\mathcal A=\prod_{n}M_n\Big/\bigoplus_{n}M_n,
\qquad
\mathcal Z=\prod_n Z(M_n)\Big/\bigoplus_n Z(M_n),
\]
where the direct sums are the norm-null sequences. Coordinatewise center-valued trace induces a contractive unital positive map
\[
\overline T:\mathcal A\to\mathcal Z,
\qquad
\overline T([(x_n)])=[(T_n(x_n))].
\]
Then:

1. **Exact single-commutator criterion.**
   \[
   \{[b,c]:b,c\in\mathcal A\}=\ker \overline T.
   \]
   If \(K\) is any universal constant valid in the uniform finite-von-Neumann-algebra commutator theorem, every \(x\in\ker\overline T\) has a representation
   \[
   x=[b,c],\qquad \|b\|\,\|c\|\le K\|x\|.
   \]

2. **The single commutators form a closed linear subspace.** In fact the induced map is an isometric linear isomorphism
   \[
   \mathcal A/\{[b,c]:b,c\in\mathcal A\}\ \cong\ \mathcal Z.
   \]
   Thus, in this class of operator-norm C*-quotients, the set of single additive commutators is not merely stable under scalar multiplication: it is exactly a closed linear kernel.

3. **All tracial states are central.** Restriction to \(\mathcal Z\) gives an affine bijection
   \[
   T(\mathcal A)\cong S(\mathcal Z),
   \]
   whose inverse sends a state \(\varphi\) on \(\mathcal Z\) to \(\varphi\circ\overline T\). Consequently every tracial state on \(\mathcal A\) is completely determined by its values on the central reduced product.

The same statements hold for norm ultraproducts. In particular, if \(\omega\) is a free ultrafilter and every \(M_n\) is a finite factor, then
\[
\mathcal A_\omega=\prod_n M_n/\{(x_n):\lim_{n\to\omega}\|x_n\|=0\}
\]
has a unique tracial state \(\tau_\omega\), and
\[
\boxed{\ \ker\tau_\omega=\{[b,c]:b,c\in\mathcal A_\omega\}\ }
\]
with the same universal bound \(\|b\|\|c\|\le K\|x\|\). Hence the single commutators in a factor norm ultraproduct form a closed codimension-one hyperplane.

## Proof

Let \(x=[(x_n)]\in\ker\overline T\). Then
\[
\|T_n(x_n)\|\longrightarrow0.
\]
Set
\[
a_n=x_n-T_n(x_n).
\]
The sequence \((a_n)\) represents the same element \(x\), satisfies \(T_n(a_n)=0\) for every \(n\), and obeys
\[
\limsup_n\|a_n\|=\limsup_n\|x_n\|=\|x\|.
\]
By the uniform commutator theorem for finite von Neumann algebras, for every \(n\) there are \(u_n,v_n\in M_n\) such that
\[
a_n=[u_n,v_n],\qquad \|u_n\|\,\|v_n\|\le K\|a_n\|.
\]
Rescale each nonzero pair reciprocally so that
\[
\|u_n\|=\|v_n\|=(\|u_n\|\|v_n\|)^{1/2};
\]
for \(a_n=0\), take \(u_n=v_n=0\). The resulting factor sequences are bounded, and for their quotient classes \(u,v\in\mathcal A\),
\[
x=[u,v],
\qquad
\|u\|\,\|v\|
\le K\limsup_n\|a_n\|
=K\|x\|.
\]
This proves \(\ker\overline T\subseteq\{[b,c]\}\). The reverse inclusion follows coordinatewise from
\[
T_n(rs)=T_n(sr).
\]

Since \(\ker\overline T\) is a closed linear subspace, the first assertion immediately implies that the set of single commutators is closed and linear. Moreover, \(\overline T\) is the identity on the embedded central algebra \(\mathcal Z\). For \(N=\ker\overline T\), contractivity gives
\[
\|\overline T(x)\|\le \operatorname{dist}(x,N),
\]
while \(x-\overline T(x)\in N\) gives the reverse inequality. Hence
\[
\operatorname{dist}(x,N)=\|\overline T(x)\|,
\]
which proves the claimed isometric quotient identification.

If \(\tau\) is a tracial state on \(\mathcal A\), then \(x-\overline T(x)\) is a single commutator, so
\[
\tau(x)=\tau(\overline T(x)).
\]
Thus \(\tau\) is determined by its restriction to \(\mathcal Z\). Conversely, because \(\overline T\) is unital and positive and satisfies \(\overline T(xy)=\overline T(yx)\), every state \(\varphi\) on \(\mathcal Z\) yields a tracial state \(\varphi\circ\overline T\). This proves the trace-space identification.

For a norm ultraproduct, replace ordinary norm convergence by convergence along \(\omega\) throughout. If all coordinates are factors, the center quotient is the scalar norm ultraproduct, canonically \(\mathbb C\) by ultralimit, so the tracial state is unique.

## Relation to prior literature

Jiaqi Wang's 2026 Theorem 1.1 proves the uniform single-commutator bound in every finite von Neumann algebra: center-valued trace zero is equivalent to being one additive commutator, with an absolute norm-product bound. The result above transfers that uniform theorem through **operator-norm** reduced products and ultraproducts, which need not themselves be von Neumann algebras, and identifies their entire trace spaces and Banach-space abelianizations.

For matrix norm ultraproducts, Hardy's work on pseudomatricial C*-algebras already gives unique tracial state and proves that self-adjoint trace-zero elements are self-commutators. The present consequence is different in two ways: it covers arbitrary, not necessarily self-adjoint, trace-zero elements by a single additive commutator with a universal operator-norm bound, and it applies to norm reduced products of arbitrary finite von Neumann algebras with nontrivial centers. Bice--Farah show that traces on general C*-ultrapowers can be much less rigid, so the factorization of every trace through \(\overline T\) is a special consequence of the new uniform commutator theorem rather than a generic ultrapower phenomenon.

## Originality and limitations

To the best of our knowledge, the norm-reduced-product/ultraproduct classification above is not stated in the cited sources. It is a new structural consequence of Wang's September 2026 uniform theorem rather than a new proof of that theorem. The matrix-ultraproduct special case overlaps substantially with older pseudomatricial trace rigidity: uniqueness of trace and the self-adjoint self-commutator statement are not claimed as new here. The claimed new content is the exact **single additive commutator** kernel with a universal norm bound in operator-norm reduced products, the resulting closed-linear/isometric quotient description, and the extension to arbitrary finite-von-Neumann coordinate algebras.

No assertion is made for arbitrary C*-algebra ultraproducts lacking a uniform coordinatewise single-commutator theorem, nor for quotients defined by 2-norm null ideals (the usual tracial ultraproduct construction), where different standard arguments and structures apply.

## Sources

- Jiaqi Wang, *A uniform commutator bound in finite von Neumann algebras*, arXiv:2609.16932 (2026).
- Hao Shen, Jiaqi Wang, Lihong Zhi, *A Dimension-Independent Commutator Bound*, arXiv:2609.09938 (2026).
- Stephen Hardy, *Pseudocompact C*-algebras*, arXiv:1609.06275 (2016).
- Tristan Bice and Ilijas Farah, *Traces, Ultrapowers and the Pedersen-Petersen C*-Algebras*, arXiv:1307.0111; Houston J. Math. 41 (2015), 1175–1190.
