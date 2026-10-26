# Local derivations of Heisenberg Lie algebras over arbitrary fields

## Finding

Let \(K\) be any field, let \(n\ge 1\), and let \((V,\omega)\) be a \(2n\)-dimensional vector space with a nondegenerate alternating bilinear form. Define the Heisenberg Lie algebra
\[
\mathfrak h=V\oplus Kz,\qquad [v,w]=\omega(v,w)z,\qquad [z,\mathfrak h]=0.
\]
Then the space of local derivations is exactly
\[
\operatorname{LocDer}(\mathfrak h)=\{T\in\operatorname{End}_K(\mathfrak h):T(Kz)\subseteq Kz\}.
\]
In particular,
\[
\dim_K\operatorname{LocDer}(\mathfrak h)=4n^2+2n+1,
\qquad \dim_K\operatorname{Der}(\mathfrak h)=2n^2+3n+1,
\]
so the local-derivation space strictly contains the derivation space by dimension \(n(2n-1)\), for every \(n\ge1\) and in every characteristic.

## Assumptions and scope

The field is arbitrary, including characteristic two. The form \(\omega\) is alternating and nondegenerate; no algebraic-closure or finiteness assumption is used. A local derivation means a linear map \(\Delta\) such that for every \(x\in\mathfrak h\), some derivation \(D_x\) satisfies \(\Delta(x)=D_x(x)\). The statement concerns this Heisenberg family, not all two-step nilpotent Lie algebras.

## Proof

First, every derivation preserves the center. Since \(Z(\mathfrak h)=Kz\), every local derivation \(\Delta\) must satisfy \(\Delta(z)=cz\) for some \(c\in K\). Relative to the decomposition \(\mathfrak h=V\oplus Kz\), it therefore has the form
\[
\Delta(v+tz)=Lv+(\ell(v)+ct)z,
\]
for a linear map \(L:V\to V\) and a functional \(\ell\in V^*\). This proves the necessary inclusion.

For the converse, fix any such \(L,\ell,c\). The symplectic Lie algebra \(\mathfrak{sp}(V,\omega)\) acts transitively at the level of evaluation: for every nonzero \(v\in V\) and every \(w\in V\), there is \(S\in\mathfrak{sp}(V,\omega)\) with \(Sv=w\). To verify this, choose a symplectic basis with \(v\) as its first vector. In block form, matrices
\[
S=\begin{pmatrix}A&0\\ C&-A^{\mathsf T}\end{pmatrix},\qquad C=C^{\mathsf T},
\]
belong to \(\mathfrak{sp}(V,\omega)\); the first columns of \(A\) and \(C\) can be chosen independently to produce any target \(w\). This argument is valid in characteristic two as well.

Now take \(x=v+tz\). If \(v\ne0\), choose \(S\in\mathfrak{sp}(V,\omega)\) with \(Sv=Lv\), and choose \(\phi\in V^*\) such that \(\phi(v)=\ell(v)+ct\). The map
\[
D_x(u+sz)=Su+\phi(u)z,\qquad D_x(z)=0,
\]
is a derivation, because \(S\) preserves \(\omega\), and it satisfies \(D_x(x)=\Delta(x)\).

If \(v=0\), then \(x=tz\). For \(t\ne0\), choose a symplectic basis \(e_1,\ldots,e_n,f_1,\ldots,f_n\) and define \(M(e_i)=0\), \(M(f_i)=cf_i\). This map has conformal multiplier \(c\), meaning
\[
\omega(Mu,w)+\omega(u,Mw)=c\,\omega(u,w)
\]
for all \(u,w\in V\). Hence \(D(u+sz)=Mu+csz\) is a derivation and \(D(tz)=ctz=\Delta(tz)\). The zero vector is immediate. Thus every endomorphism preserving \(Kz\) is a local derivation.

For the dimensions, a derivation has the form \(D(v)=Mv+\phi(v)z\), \(D(z)=cz\), where \(M\) has conformal symplectic multiplier \(c\). The conformal symplectic space has dimension \(n(2n+1)+1\), and \(\phi\) contributes \(2n\) parameters. Therefore
\[
\dim_K\operatorname{Der}(\mathfrak h)=n(2n+1)+1+2n=2n^2+3n+1.
\]
An arbitrary endomorphism preserving \(Kz\) has an arbitrary \(2n\)-by-\(2n\) block, an arbitrary central functional, and one scalar on \(Kz\). Consequently
\[
\dim_K\operatorname{LocDer}(\mathfrak h)=(2n)^2+2n+1=4n^2+2n+1,
\]
and subtraction gives the stated gap \(n(2n-1)>0\).

## Verification

The proof uses only the derivation identity and the displayed symplectic-basis construction. The standalone script `artifacts/check_h3_f2.py` exhaustively enumerates all \(512\) linear maps on the three-dimensional Heisenberg algebra over \(\mathbb F_2\). It finds \(64\) derivations and \(128\) local derivations, exactly the \(128\) center-preserving maps. This finite check corroborates the smallest case; it is not used as proof for other dimensions or fields.

## Relationship to prior work

Khudoyberdiyev and Jumaniyozov study local derivations and automorphisms of nilpotent Lie algebras. Their 2024 preprint proves existence of a local derivation that is not a derivation for two-step nilpotent Lie algebras in characteristic different from two and gives a Heisenberg example. It also records different behavior in characteristic two, including a twelve-dimensional example where local derivations coincide with derivations. The present statement gives the full local-derivation space for the Heisenberg family in every characteristic, rather than only constructing a witness. The earlier work of Ayupov and Kudaybergenov treats semisimple Lie algebras in characteristic zero and supplies nilpotent examples, but does not state this all-field classification.

## Limitations

The classification depends on the one-dimensional center and the nondegenerate alternating form. It does not classify local derivations on arbitrary two-step nilpotent Lie algebras with larger center, nor on general nilpotent Lie algebras. The finite enumeration covers only the three-dimensional case over \(\mathbb F_2\); the general conclusion follows from the symbolic proof above.

## References

1. A. Khudoyberdiyev and D. Jumaniyozov, “Local derivations and automorphisms of nilpotent Lie algebras,” arXiv:2405.04209, first submitted 2024-05-07. https://arxiv.org/abs/2405.04209
2. Sh. Ayupov and K. Kudaybergenov, “Local derivations on finite-dimensional Lie algebras,” arXiv:1508.03939, first submitted 2015-08-17. https://arxiv.org/abs/1508.03939
