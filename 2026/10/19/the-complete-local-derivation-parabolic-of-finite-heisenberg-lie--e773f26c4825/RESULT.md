# The complete local-derivation parabolic of finite Heisenberg Lie algebras

## Finding

For every field \(K\) and integer \(n\ge1\), the space of **linear local derivations** of the \((2n+1)\)-dimensional Heisenberg Lie algebra is exactly the stabilizer of its one-dimensional center:

\[
\operatorname{LocDer}(H_n(K))=\{T\in\operatorname{End}_K(H_n(K)):T(Kz)\subseteq Kz\}.
\]

Every element, and only an element, has the block form

\[
T=\begin{pmatrix}B&0\\f&\lambda\end{pmatrix},\quad B\in\operatorname{End}_K(K^{2n}),\quad f\in(K^{2n})^*,\quad\lambda\in K.
\]

An element of this space is an ordinary derivation exactly when the \(V\)-block is infinitesimally conformally symplectic. Hence

\[
\dim_K\operatorname{LocDer}(H_n)=4n^2+2n+1,\qquad
\dim_K\operatorname{Der}(H_n)=2n^2+3n+1.
\]

For a finite field \(K=\mathbb F_q\), the respective counts are \(q^{4n^2+2n+1}\) and \(q^{2n^2+3n+1}\); the global-derivation proportion among local derivations is \(q^{-n(2n-1)}\). The formula holds also when \(\operatorname{char}K=2\).

## Assumptions and scope

Let \(n\ge1\) and let \(V\) be a \(2n\)-dimensional vector space over an arbitrary field \(K\), with a nondegenerate **alternating** bilinear form \(\omega\). Define \(H_n=V\oplus Kz\) by \([u+az,v+bz]=\omega(u,v)z\); this is a Lie bracket also in characteristic two, because \(\omega(v,v)=0\). The center and derived subalgebra both equal \(Kz\). A *derivation* is a \(K\)-linear map \(D\) satisfying \(D([x,y])=[Dx,y]+[x,Dy]\) for all \(x,y\). A *linear local derivation* is a \(K\)-linear map \(\Delta\) such that, for each individual \(x\in H_n\), some derivation \(D_x\) (depending on \(x\)) satisfies \(D_x(x)=\Delta(x)\). No common derivation \(D_x\) for distinct \(x\) is assumed.

## Proof

**1. Ordinary derivations.** Since the center is characteristic under derivations, every derivation \(D\) has \(D(z)=\lambda z\) and \(D(v)=Bv+f(v)z\), for some \(\lambda\in K\), \(B\in\operatorname{End}_K(V)\), and \(f\in V^*\). Applying the derivation identity to \([u,v]=\omega(u,v)z\) gives exactly

\[
\omega(Bu,v)+\omega(u,Bv)=\lambda\omega(u,v)\qquad(u,v\in V).
\tag{1}
\]

Conversely, any triple satisfying (1) defines a derivation, since the center brackets to zero. Fix a symplectic basis \((e_1,\ldots,e_n,f_1,\ldots,f_n)\), so \(\omega\) has matrix \(J=\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix}\). Equation (1) is \(B^{\mathsf T}J+JB=\lambda J\). For each \(\lambda\), the block matrix \(B_0=\operatorname{diag}(\lambda I_n,0)\) solves the equation, even in characteristic two. The solution set is the affine translate \(B_0+\mathfrak{sp}(V,\omega)\).

**2. Evaluation-surjectivity lemma.** For every nonzero \(v\in V\),

\[
\{Sv:S\in\mathfrak{sp}(V,\omega)\}=V.
\tag{2}
\]

To prove it, extend \(v\) to a symplectic basis with \(v=e_1\). Relative to that basis, every block matrix

\[
S=\begin{pmatrix}P&Q\\R&-P^{\mathsf T}\end{pmatrix}
\quad\text{with}\quad Q^{\mathsf T}=Q,\ R^{\mathsf T}=R
\]

lies in \(\mathfrak{sp}(V,\omega)\). The image \(Se_1\) comprises the first column of \(P\) and the first column of \(R\). These two columns may be chosen independently and arbitrarily, because any prescribed first column can be extended to a symmetric \(R\). This proves (2). No division by two is used; (2) remains true in characteristic two.

**3. Locality of every center-preserving map.** Any local derivation must preserve \(Kz\), since evaluating it at \(z\) agrees with an ordinary derivation there. Conversely, fix an arbitrary \(K\)-linear center-preserving map \(\Delta\), with blocks \((B,f,\lambda)\), and any \(x=v+tz\in H_n\). Choose \(B_0=\operatorname{diag}(\lambda I_n,0)\) as above. If \(v=0\), the genuine derivation with blocks \((B_0,f,\lambda)\) agrees with \(\Delta\) at \(x\). If \(v\ne0\), equation (2) supplies \(S\in\mathfrak{sp}(V,\omega)\) satisfying \(Sv=(B-B_0)v\). Then the genuine derivation \(D_x\) with blocks \((B_0+S,f,\lambda)\) satisfies

\[
D_x(v+tz)=(B_0+S)v+f(v)z+t\lambda z=Bv+f(v)z+t\lambda z=\Delta(x).
\]

As \(x\) is arbitrary, \(\Delta\) is local. Hence all and only center-preserving endomorphisms are local derivations.

**4. Dimensions and finite-field counts.** For a \(2n\)-dimensional symplectic space, \(\dim\mathfrak{sp}(V,\omega)=n(2n+1)\): the block \(P\) has \(n^2\) parameters and each symmetric block \(Q,R\) has \(n(n+1)/2\). The similitude scalar \(\lambda\) adds one parameter, while \(f\) adds \(2n\), giving \(\dim\operatorname{Der}=n(2n+1)+1+2n=2n^2+3n+1\). The unrestricted block \(B\), together with \(f\) and \(\lambda\), yields \(\dim\operatorname{LocDer}=(2n)^2+2n+1\). Subtract to obtain \(n(2n-1)\). Over \(\mathbb F_q\), exponentiating these dimensions gives the two claimed cardinalities and their ratio.

To see the local-global distinction directly, the map \(\Delta(z)=z\), \(\Delta(V)=0\) is local but not a derivation: for \(\omega(u,v)=1\), the left-hand side of the derivation identity equals \(z\), whereas the right-hand side is zero.

## Verification

The included standalone `verify.py` independently imposes the derivation equations on all endomorphism coordinates over prime fields, derives their nullspace, and for every nonzero algebra element computes the evaluation-image annihilator to impose the local condition. It then solves the complete system, checks that every resulting local map preserves the center, and tests both predicted dimensions. Successful runs: \((n,p)=(1,2),(1,3),(1,5),(2,2),(2,3),(3,2)\), producing dimensions \((6,7),(6,7),(6,7),(15,21),(15,21),(28,43)\) for (derivations, local derivations). Run with `python verify.py`; expected final line: `ALL_CHECKS_PASS`. These are finite-instance checks, not a substitute for the arbitrary-field proof.

## Relationship to prior work

Hao and Chen's 2026 study *Two Conjectures and Applications on Local and Almost Inner Derivations* establishes general algebraic-reflexive-hull structure and related bounds, but does not compute the center-stabilizer equality, infinite-family dimensions, or finite-field counts for Heisenberg Lie algebras. Their related September 2026 preprint *Local derivations is a Lie algebra* proves abstract closure under commutators rather than identifying this particular local-derivation algebra. Earlier work of Khudoyberdiyev and Jumaniyozov (2024, Theorem 3.1 and Example 3.2) **already exhibits** a non-derivation local map on every complex Heisenberg algebra; thus mere existence is not new here. Hao and Chen's 2025 low-dimensional tables similarly already cover individual small-dimensional complex cases. The distinction in the present finding is the complete, explicit classification for every symplectic rank and arbitrary characteristic, including exact finite-field enumeration. Results for larger Schrödinger and conformal-Galilei algebras do not imply local-derivation classifications of their Heisenberg ideals, because derivations of the ambient algebra need not restrict to all derivations of the ideal.

## Limitations

This concerns **linear** local derivations, not arbitrary nonlinear pointwise maps or 2-local derivations. The definition uses field-linear endomorphisms and an ordinary Heisenberg Lie algebra with a one-dimensional center and nondegenerate alternating bracket; it does not classify degenerate alternating extensions or general two-step nilpotent Lie algebras. Prime-field computations are illustrative only; the proof, not extrapolation, establishes the result over extension fields and all characteristics. Earlier unindexed formulations under reflexive-hull terminology remain a possible originality risk. No independent audit is represented.

## References

1. Z. Hao and L. Chen, *Two Conjectures and Applications on Local and Almost Inner Derivations*, author-posted full preprint, July 9, 2026, https://www.researchgate.net/publication/408607392_TWO_CONJECTURES_AND_APPLICATIONS_ON_LOCAL_AND_ALMOST_INNER_DERIVATIONS (MSC2020: 17B38).
2. Z. Hao and L. Chen, *Local derivations is a Lie algebra*, arXiv:2609.09198v1, September 4, 2026, https://arxiv.org/abs/2609.09198 (MSC2020: 17A36, 17B40).
3. A. Khudoyberdiyev and D. Jumaniyozov, *Local derivations and automorphisms of nilpotent Lie algebras*, arXiv:2405.04209v1, May 7, 2024, https://arxiv.org/abs/2405.04209 (especially Theorem 3.1, Example 3.2).
4. Z. Hao and L. Chen, *A computational approach to local derivations and almost inner derivations*, author-posted preprint, December 22, 2025, DOI:10.13140/RG.2.2.22944.44809, https://www.researchgate.net/publication/398952066_A_computational_approach_to_local_derivations_and_almost_inner_derivations (Theorem 3.2 and low-dimensional tables).
5. A. Alauadinov, B. Yusupov, and D. Jumaniyozov, *Local derivation on the n-th Schrödinger algebra*, arXiv:2406.04742v1, June 7, 2024, https://arxiv.org/abs/2406.04742 (a rigidity result for a different, larger Lie algebra).
