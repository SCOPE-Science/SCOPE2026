# Orthogonal retracts of symmetric central Leibniz algebras

## Finding

Let \(L_B\) be the two-step nilpotent central Leibniz algebra constructed from a nondegenerate symmetric bilinear space \((V,B)\). Every idempotent endomorphism other than the identity is exactly
\[
F(v+az)=P(v)+\psi(Pv)z,
\]
where \(P:V\to V\) is a projection, its image \(U=\operatorname{im}(P)\) is totally isotropic for \(B\), and \(\psi\in U^*\). In particular, a nonzero proper retract exists if and only if \(B\) represents zero nontrivially.

For every odd prime power \(q\), let \(I_B(k)\) denote the number of \(k\)-dimensional totally isotropic subspaces over \(\mathbf F_q\). The number of idempotent endomorphisms of rank \(k\) and the number of their distinct image subalgebras are, respectively,
\[
E_k(q)=I_B(k)q^{k(n-k+1)},\qquad R_k(q)=I_B(k)q^k\quad(1\le k\le w),
\]
where \(w\) is the Witt index. Each such image is the image of exactly \(q^{k(n-k)}\) retractions. The complete count, including the zero map and the identity, is
\[
\#\operatorname{IdemEnd}(L_B)=2+\sum_{k=1}^{w}I_B(k)q^{k(n-k+1)}.
\]

The isotropic-subspace counts are explicit. Put \([k]_q=(q^k-1)/(q-1)\) and \(I_B(0)=1\). For \(1\le k\le w\),
\[
I_B(k)=\frac{I_B(k-1)\ell_{n-2k+2}}{[k]_q}.
\]
In odd dimension \(n=2m+1\), the Witt index is \(w=m\) and \(\ell_{2h+1}=(q^{2h}-1)/(q-1)\). In even dimension \(n=2m\), set \(\epsilon=\chi_q((-1)^m\det B)\). The Witt index is \(m\) for \(\epsilon=1\) and \(m-1\) for \(\epsilon=-1\), and \(\ell_{2h}=(q^{h-1}+\epsilon)(q^h-\epsilon)/(q-1)\). Here \(\chi_q\) is the quadratic character of \(\mathbf F_q^*\).

## Assumptions and scope

Let \(K\) be a field of characteristic different from two, \(n=\dim_K V\ge2\), and \(B:V\times V\to K\) symmetric and nondegenerate. Define \(L_B=V\oplus Kz\) with the bilinear bracket
\[
[v+az,w+bz]=B(v,w)z
\]
for all \(v,w\in V\) and \(a,b\in K\). Centrality of \(z\) makes this a left Leibniz algebra; its derived ideal is \(Kz\). Endomorphisms and images are **labeled** in the fixed space, not counted up to isomorphism. The algebra need not be Lie. A retract means the image of an idempotent algebra endomorphism, and \(\operatorname{rank}F\) means vector-space rank. The general classification holds over any such \(K\); finite counting formulas assume \(K=\mathbf F_q\) with \(q\) odd.

## Proof

**1. Endomorphism normal form.** An algebra endomorphism preserves the derived ideal \([L_B,L_B]=Kz\), hence sends \(z\) to \(\lambda z\). Its restriction to \(V\) has the unique form \(v\mapsto Av+\phi(v)z\), with \(A\in\operatorname{End}_K(V)\), \(\phi\in V^*\). Comparing images of \([v,w]\) with \([F(v),F(w)]\) gives the necessary-and-sufficient identity
\[
B(Av,Aw)=\lambda B(v,w)\qquad(v,w\in V).
\]
Indeed brackets with \(z\) vanish, so this condition checks all defining brackets.

**2. Idempotents.** The equality \(F^2=F\) gives \(A^2=A\), \(\lambda^2=\lambda\), and \(\phi A+\lambda\phi=\phi\). Since a field has only the idempotent scalars zero and one, \(\lambda=0\) or \(1\). If \(\lambda=1\), preservation of the nondegenerate \(B\) makes \(A\) injective, thus invertible; \(A^2=A\) forces \(A=1_V\), and the equation for \(\phi\) then forces \(\phi=0\). This is the identity endomorphism. If \(\lambda=0\), the normal form is equivalent to
\[
P^2=P,\quad B(Pv,Pw)=0\quad(v,w\in V),\quad\phi P=\phi.
\]
Thus \(P\) is any projection onto a totally isotropic subspace \(U\), and \(\phi\) factors uniquely through \(P\) as \(\psi P\) for a unique \(\psi\in U^*\). Conversely these relations imply bracket preservation and idempotence. For \(U=0\), this is exactly the zero endomorphism. All other proper images are the abelian graphs \(\{u+\psi(u)z:u\in U\}\). Since projection fixes its image, every isotropic \(U\) and every \(\psi\) give an embedded retract.

**3. Count maps and distinct images.** For a fixed \(k\)-dimensional subspace \(U\subset V\), projections onto \(U\) correspond bijectively to complements of \(U\). Fix one complement \(W_0\); all complements are graphs of maps \(W_0\to U\), so there are \(q^{k(n-k)}\). There are independently \(q^k\) linear functionals \(\psi\in U^*\). The graph image uniquely determines the pair \((U,\psi)\) by projection to \(V\), and different projections with this pair give exactly the same retract image. Multiplying by the \(I_B(k)\) isotropic subspaces proves the three counting formulas. No nonzero proper idempotent can have a nonisotropic image.

**4. Isotropic-subspace recursion.** Choose a totally isotropic \((k-1)\)-plane \(W\). Totally isotropic \(k\)-planes containing \(W\) correspond to isotropic one-dimensional subspaces of the nondegenerate quotient \(W^\perp/W\), which has dimension \(n-2(k-1)\), and has the same anisotropic part as \((V,B)\). Counting incident pairs \(W\subset U\), \(\dim W=k-1\), \(\dim U=k\), gives
\[
I_B(k-1)\ell_{n-2k+2}=I_B(k)[k]_q.
\]
To obtain \(\ell\), use Witt decomposition. For odd rank \(2h+1\), a hyperbolic coordinate calculation for \(\sum_{i=1}^{h}x_i y_i+c t^2\) gives exactly \(q^{2h}\) zero vectors, hence \((q^{2h}-1)/(q-1)\) isotropic lines. For even rank \(2h\), the split and nonsplit forms have, respectively, \(q^{2h-1}+(q-1)q^{h-1}\) and \(q^{2h-1}-(q-1)q^{h-1}\) zero vectors. Subtracting the origin and dividing by \(q-1\) yields the displayed \(\ell_{2h}\), with \(\epsilon=\chi_q((-1)^m\det B)\); removing a hyperbolic plane does not change this type. These counts also identify the stated Witt indices. Together with step 3 this proves the theorem for every odd finite field.

## Verification

The standalone checker `verify.py` separately enumerates all \((n+1)\)-by-\((n+1)\) idempotent algebra endomorphism matrices for two-dimensional forms over \(\mathbf F_3\), enumerates every linear projection meeting the orthogonality equations for several diagonal forms over \(\mathbf F_3\) and \(\mathbf F_5\), and independently enumerates isotropic subspaces in dimensions two, three, and four over \(\mathbf F_3\). Running `python3 verify.py` returns `VERIFY_OK`. For anisotropic two-dimensional forms the total is \(2\); for hyperbolic planes it is \(2+2q^2\). For three-dimensional nondegenerate forms it is \(2+(q+1)q^3\). The four-dimensional split and nonsplit counts over \(\mathbf F_3\) are, respectively, \(7130\) and \(812\). The symbolic argument above, not these finite tests, establishes all-field and arbitrary-dimension claims.

## Relationship to prior work

Kurdachenko–Pypka–Subbotin (2022, arXiv:2211.01074v1) study the internal structure of three-dimensional Leibniz algebras. Kurdachenko–Pypka–Semko (2023, arXiv:2310.11180v1, especially the symmetric central bracket family in their analysis) determine automorphism groups of nilpotent three-dimensional Leibniz algebras. In contrast, the present theorem classifies **idempotent, generally singular endomorphisms** for a nondegenerate symmetric central bracket in all dimensions and counts both endomorphisms and distinct retract images over finite fields. The relevant classical orthogonal-geometry isotropic-plane formulas are used as standard inputs, with their recursion and point-count derivation repeated above; they are not claimed to be new. Existing automorphism classifications alone do not specify these singular-retraction strata.

## Limitations

This result is for nondegenerate symmetric forms and characteristic different from two; neither degenerate bilinear forms nor nonsymmetric central brackets are classified. The result counts labeled endomorphisms and labeled retract images, not automorphism-conjugacy or isomorphism classes. The geometric argument describes point parametrization and finite-field counts, not scheme-theoretic smoothness, irreducibility, or a moduli classification. Finite verification uses prime fields and cannot substitute for the proof for general prime powers. Equivalent special cases may exist under older orthogonal or Leibniz-semigroup terminology; no absolute novelty is asserted.

## References

1. L. A. Kurdachenko, O. O. Pypka, and I. Ya. Subbotin, *On the inner structure of 3-dimensional Leibniz algebras*, arXiv:2211.01074v1 (submitted 2022-11-02), https://arxiv.org/abs/2211.01074.
2. L. A. Kurdachenko, O. O. Pypka, and M. M. Semko, *On the automorphism groups of some nilpotent 3-dimensional Leibniz algebras*, arXiv:2310.11180v1 (submitted 2023-10-17), https://arxiv.org/abs/2310.11180.
3. Standard Witt decomposition and finite-field quadratic-form line counts (classical background, not an originality claim).
