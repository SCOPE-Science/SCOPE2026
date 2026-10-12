# Exact singular-defect transfer for structured perturbations over arbitrary rings
## Finding
Let \(R\) be a nonzero unital associative ring and let \(n\ge k\ge1\). Suppose \(A\in M_n(R)\), \(E\in M_{n\times k}(R)\), and \(F\in M_{k\times n}(R)\) satisfy the hypotheses used in Öinert's structured-perturbation theorem:
\[
F|_{\ker A}:\ker A\longrightarrow R^k\text{ is an isomorphism},\qquad
R^n=\operatorname{im}A\oplus\operatorname{im}E,
\]
and \(E\) is injective. Let \(X,G,Y\) be the associated maps from Lemma 2.1 of that source. For arbitrary \(D\in M_k(R)\), including singular \(D\), define
\[
T_D=A+EDF.
\]
Then the entire singular defect of \(T_D\) is carried by \(D\). More precisely, with
\[
A_0=A|_{\ker F}:\ker F\longrightarrow\operatorname{im}A,
\]
the isomorphisms
\[
\phi:\ker F\oplus R^k\longrightarrow R^n,\quad \phi(u,c)=u+Xc,
\]
\[
\psi:\operatorname{im}A\oplus R^k\longrightarrow R^n,\quad \psi(a,c)=a+Ec
\]
satisfy
\[
\psi^{-1}T_D\phi=A_0\oplus D.
\]
Since \(A_0\) is an isomorphism, this gives
\[
\ker T_D=X(\ker D),\qquad \operatorname{coker}T_D\cong\operatorname{coker}D,
\]
where the cokernel isomorphism is induced by \(Y\). It also gives an exact transfer of von Neumann regularity: \(T_D\) is regular if and only if \(D\) is regular.

If \(H\in M_k(R)\) is an inner inverse of \(D\), so \(DHD=D\), then
\[
S_H=G+XHY
\]
is an inner inverse of \(T_D\). If \(H\) is reflexive, so also \(HDH=H\), then \(S_H\) is reflexive. Conversely, if \(Q\) is any inner inverse of \(T_D\), then \(FQE\) is an inner inverse of \(D\).

Over a field, the block normal form immediately yields
\[
\operatorname{rank}T_D=n-k+\operatorname{rank}D,
\qquad
\operatorname{nullity}T_D=\operatorname{nullity}D.
\]

## Assumptions and scope
Matrices act on free right \(R\)-modules by left multiplication, as in the source. No commutativity, stable finiteness, determinant, adjoint, inner product, or invertibility of \(D\) is assumed. The direct-sum hypothesis on the codomain and the isomorphism hypothesis on \(F|_{\ker A}\) are essential to the stated normal form.

The conclusion is stronger than an invertibility criterion: it identifies the two-term module map represented by \(T_D\) with the direct sum of an isomorphism and the map represented by \(D\). Thus kernels, cokernels, and regular generalized inverses reduce exactly to the smaller matrix.

## Proof
Lemma 2.1 of the motivating source provides \(X,G,Y\) satisfying
\[
AX=0,\quad FX=I_k,\quad FG=0,\quad GE=0,\quad YA=0,\quad YE=I_k,
\]
\[
AG+EY=I_n,\qquad GA+XF=I_n.
\]
It also proves
\[
R^n=\ker F\oplus\ker A,
\]
with \(X(R^k)=\ker A\), and that \(A_0=A|_{\ker F}\) is an isomorphism onto \(\operatorname{im}A\). Hence \(\phi\) above is an isomorphism. The source hypotheses give \(R^n=\operatorname{im}A\oplus E(R^k)\), and injectivity of \(E\) makes \(\psi\) an isomorphism.

For \(u\in\ker F\) and \(c\in R^k\),
\[
T_D(u+Xc)=Au+AXc+EDFu+EDFXc=A_0u+EDc,
\]
because \(Fu=0\), \(AX=0\), and \(FX=I_k\). Therefore
\[
\psi^{-1}T_D\phi(u,c)=(A_0u,Dc),
\]
which is the claimed block normal form.

The kernel identity follows because \(A_0\) and \(E\) are injective. For the cokernel, the relation \(Y T_D=DF\) shows that \(Y\) descends to a map
\[
\overline Y:\operatorname{coker}T_D\longrightarrow\operatorname{coker}D.
\]
It is surjective because \(YE=I_k\). If \(Yv\in\operatorname{im}D\), write \(v=a+Ec\) with \(a\in\operatorname{im}A\) and \(c=Yv\), then choose \(u\in\ker F\) with \(Au=a\) and \(d\in R^k\) with \(Dd=c\). The block formula gives \(v=T_D(u+Xd)\), proving injectivity of \(\overline Y\).

For generalized inverses, direct multiplication using the displayed relations gives
\[
T_D(G+XHY)T_D=A+E(DHD)F.
\]
Thus \(DHD=D\) implies \(T_DS_HT_D=T_D\). A second multiplication gives
\[
(G+XHY)T_D(G+XHY)=G+X(HDH)Y,
\]
so reflexivity transfers as well. Conversely, if \(T_DQT_D=T_D\), then \(YT_D=DF\) and \(T_DX=ED\) imply
\[
D(FQE)D=(YT_D)Q(T_DX)=Y(T_DQT_D)X=YT_DX=D.
\]
Thus regularity is equivalent.

## Verification
The proof is symbolic and valid over an arbitrary unital associative ring. As a finite consistency check, the accompanying script uses the canonical case over \(\mathbb F_3\) with \(n=5\) and \(k=2\), exhausts all \(81\) matrices \(D\in M_2(\mathbb F_3)\), and verifies the factorization, rank transfer, existence and transfer of reflexive generalized inverses, and the converse inner-inverse construction. The script terminates with `CHECK_OK`.

The finite check is not used as a proof of the arbitrary-ring statement; the proof above is the evidence for the universal claim.

## Relationship to prior work
Öinert's 2026 preprint proves, under the same module-theoretic hypotheses, that \(T_D\) is invertible exactly when \(D\) is invertible and gives \(T_D^{-1}=G+XD^{-1}Y\). Its Lemma 2.1 constructs the splittings used here, and Remark 2.2 observes that \(G\) is a reflexive generalized inverse of \(A\). The paper does not state the all-\(D\) block normal form, kernel/cokernel transfer, or equivalence of von Neumann regularity.

Eriksson and Nordqvist treat the complex-field invertible case that motivated Öinert's work. The broader generalized-inverse literature includes Sherman-Morrison-Woodbury-type identities for rank-preserving or rank-augmenting low-rank updates, notably Deng and Jiao. Those results provide important comparison points, but the inspected statements are formulated for field matrices and generalized inverses or pseudoinverses under range/rank hypotheses; they do not state the present arbitrary-unital-ring module normal form or its cokernel transfer.

## Limitations
The theorem requires the full three hypotheses used in Öinert's Theorem A. It does not claim the same defect transfer under the weaker stably-finite-ring hypotheses of that paper. The generalized-inverse formula transfers inner and reflexive inverses but does not classify every possible generalized inverse of \(T_D\). Over noncommutative rings, no determinant or numerical rank statement is asserted.

A residual literature risk remains because generalized Sherman-Morrison-Woodbury formulas are extensive; an equivalent field-specialized generalized-inverse identity may exist under different notation. The arbitrary-ring block normal form and cokernel statement were not found in the inspected sources.

## References
1. Johan Öinert, “Invertibility of structured perturbations of singular matrices over unital rings,” arXiv:2610.01948v1, 2026. https://arxiv.org/abs/2610.01948
2. Sofia Eriksson and Jonas Nordqvist, “Inverting the sum of two singular matrices,” arXiv:2403.16896v2; Results in Applied Mathematics 22 (2024), 100463. https://arxiv.org/abs/2403.16896
3. Xiangmin Jiao, “Unified SMW-Like Identities of Low-Rank Updates for Generalized Inverses and Pseudoinverses,” SIAM Journal on Matrix Analysis and Applications 46 (2025), 1917–1929. https://doi.org/10.1137/25M1723724
4. C.-Y. Deng, “A generalization of the Sherman-Morrison-Woodbury formula,” Applied Mathematics Letters 24 (2011), 1561–1564. https://doi.org/10.1016/j.aml.2011.03.046
