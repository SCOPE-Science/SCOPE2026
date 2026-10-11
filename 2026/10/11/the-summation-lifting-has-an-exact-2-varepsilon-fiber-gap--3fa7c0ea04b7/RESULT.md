# The summation lifting has an exact \(2\varepsilon\) fiber gap
## Finding
Let \(E_m=\operatorname{span}\{e_1,\ldots,e_m\}\subset c_0\), \(Y=(\bigoplus_{m\ge1}E_m)_{\ell_1}\), and let \(Q:Y\to c_0\) be the summation quotient from Acuaviva's construction. Put \(Z=(\bigoplus_{m\ge1}E_m^*)_{c_0}\), so \(Y=Z^*\), and let \(P=J_Z^*:Y^{**}\to Y\) be the natural projection. For every isometric lifting \(S:c_0\to Y^{**}\) obtained by the weak-star ultralimit construction of Proposition 4.1 of arXiv:2607.12935v1, one has \(PS=0\). Consequently, for every \(x\in c_0\), \[\inf_{Qy=x}\|Sx-J_Yy\|_{Y^{**}}=2\|x\|_\infty.\] For every \(\varepsilon>0\), if \(Y_\varepsilon\) carries the norm \(\|y\|_\varepsilon=\max\{\varepsilon\|y\|_Y,\|Qy\|_\infty\}\), then \[\inf_{Qy=x}\|Sx-J_Yy\|_{Y_\varepsilon^{**}}=2\varepsilon\|x\|_\infty.\] Thus the factor \(M+1=2\) in the canonical lifting-to-fiber comparison used in Acuaviva's lower-bound mechanism is sharp for this summation quotient and this ultralimit lifting construction; no claim is made that the resulting global retraction lower bound is itself optimal.

## Assumptions and scope
Work over the real scalars. Let \(E_m=\operatorname{span}\{e_1,\ldots,e_m\}\subset c_0\) and
\[
Y=\left(\bigoplus_{m\ge1}E_m\right)_{\ell_1},\qquad
Z=\left(\bigoplus_{m\ge1}E_m^*\right)_{c_0}.
\]
The standard duality identifies \(Y=Z^*\). The summation map is
\[
Q((u_m)_m)=\sum_{m\ge1}u_m\in c_0.
\]
The map \(S:c_0\to Y^{**}\) is any isometric right lifting produced by the weak-star ultralimit construction in Proposition 4.1 of the cited preprint, with an ultrafilter containing all directed tails. The projection
\[
P=J_Z^*:Z^{***}=Y^{**}\longrightarrow Z^*=Y
\]
is the natural restriction projection. The result concerns this prescribed family of ultralimit liftings; it does not assert the same formula for every possible linear lifting of \(Q^{**}\).

## Proof
Fix \(x\in c_0\) and an integer \(N\ge1\). In the construction of Proposition 4.1, the directed indices contain a finite-dimensional subspace \(F\subset c_0\), and the associated local lifting uses integers
\[
m_1<m_2<\cdots
\]
chosen so that, for a fixed number \(0<r<1\),
\[
\left\|(I-P_{m_k})|_F\right\|\le r^k.
\]
Consider the directed tail on which
\[
\operatorname{span}\{x,e_{N+1}\}\subset F.
\]
On this tail one must have \(m_1>N\). Indeed, if \(m_1\le N\), then
\[
\|(I-P_{m_1})e_{N+1}\|_\infty=1,
\]
contradicting \(\|(I-P_{m_1})|_F\|\le r<1\). Therefore every local vector representing \(x\) on this tail has zero coordinates in the first \(N\) summands of \(Y\).

Let \(z=(z_m)\in Z\) have finite support contained in \(\{1,\ldots,N\}\). The preceding support escape gives
\[
\langle J_Yv_i(x),z\rangle=0
\]
on a directed tail, hence the weak-star ultralimit satisfies
\[
\langle Sx,z\rangle=0.
\]
Finitely supported vectors are dense in the \(c_0\)-sum \(Z\), while \(Sx\in Z^{***}\) is bounded. It follows that \(Sx\) annihilates all of \(Z\), so \(PSx=0\). Thus \(PS=0\).

Each \(E_m^*\) is finite dimensional and therefore reflexive. Reflexive spaces are trivially M-embedded, and the class of M-embedded spaces is stable under \(c_0\)-sums. Hence \(Z\) is M-embedded. For an M-embedded space, the natural projection from the third dual onto the dual is an L-projection. Consequently,
\[
Y^{**}=Z^{***}=J_Y(Y)\oplus_1\ker P.
\]
Since \(Sx\in\ker P\), for every \(y\in Y\),
\[
\|Sx-J_Yy\|_{Y^{**}}=\|Sx\|_{Y^{**}}+\|y\|_Y.
\]
The lifting \(S\) is isometric, so \(\|Sx\|=\|x\|_\infty\). The map \(Q\) is a norm-one quotient map onto \(c_0\), hence
\[
\inf_{Qy=x}\|y\|_Y=\|x\|_\infty.
\]
Taking the infimum over the affine fiber gives
\[
\inf_{Qy=x}\|Sx-J_Yy\|_{Y^{**}}=2\|x\|_\infty.
\]

Now equip \(Y\) with
\[
\|y\|_\varepsilon=\max\{\varepsilon\|y\|_Y,\|Qy\|_\infty\},\qquad \varepsilon>0.
\]
Proposition 2.4 of the focal paper identifies the bidual norm as
\[
\|z\|_{\varepsilon,**}=\max\{\varepsilon\|z\|_{Y^{**}},\|Q^{**}z\|_\infty\}.
\]
If \(Qy=x\), then \(Q^{**}(Sx-J_Yy)=0\). Therefore
\[
\|Sx-J_Yy\|_{\varepsilon,**}=\varepsilon\|Sx-J_Yy\|_{Y^{**}},
\]
and the previous formula yields
\[
\inf_{Qy=x}\|Sx-J_Yy\|_{Y_\varepsilon^{**}}=2\varepsilon\|x\|_\infty.
\]

## Verification
The support-escape argument uses only a directed tail containing both \(x\) and \(e_{N+1}\), so it is independent of the auxiliary choices of the increasing integers and of the particular tail-containing ultrafilter. The passage from finite-support \(z\) to arbitrary \(z\in Z\) is justified by density in the \(c_0\)-sum.

The exact additive norm identity is not inferred from a generic contractive projection: it uses the L-projection supplied by M-embeddedness of \(Z\). The relevant standard results are Proposition 1.2 and Theorem 1.6(c) in Chapter III of Harmand--Werner--Werner. The quotient identity uses the same norm-one quotient \(Q\) verified in Proposition 4.1 of the focal paper. No finite experiment or numerical approximation is used.

For the source's sequence \(\varepsilon=2^{-n}\), the exact fiber distance is
\[
2^{1-n}\|x\|_\infty.
\]
This shows that the coefficient \(M+1=2\) in the specific lifting-to-fiber estimate of Theorem 3.1 cannot be reduced for this construction by choosing a better representative in the fiber.

## Relationship to prior work
Acuaviva constructs the quotient \(Q:Y\to c_0\), proves that \(Q^{**}\) admits an isometric linear lifting by a weak-star ultralimit, and uses the general estimate \(M+1\) with \(M=1\) to obtain the lower bound appearing in Proposition 4.3. The paper also observes that \(Y=Z^*\) and uses the norm-one projection \(P=J_Z^*\) for the complementary upper bound.

The additional point proved here is that the particular ultralimit lifting has no \(Y\)-component at all:
\[
PS=0.
\]
Combining this support-escape fact with the standard M-embedded decomposition of \(Z\) upgrades the source's one-sided estimate to an exact distance from \(Sx\) to every genuine quotient fiber.

General M-ideal theory supplies the L-decomposition once \(Z\) is recognized as a \(c_0\)-sum of M-embedded spaces, but it does not identify the focal lifting with the singular summand. Conversely, the focal construction gives the lifting but does not state the singular-summand identity or the exact fiber-distance formula.

## Limitations
The theorem is a method-optimality statement for the ultralimit lifting construction in Proposition 4.1. It does not prove that every linear lifting of \(Q^{**}\) has the same distance profile, and it does not close the source's global factor-two gap for the Lipschitz retraction constants of the renormed spaces. The originality comparison found no statement implying the exact formula, but the focal preprint is recent and an equivalent special-case observation could exist under general M-ideal terminology. No independent audit has been performed.

## References
1. Antonio Acuaviva, “A Separable Banach Space with a Schauder Basis Which Is Not a Lipschitz Retract of Its Bidual,” arXiv:2607.12935v1, first public 14 July 2026; see Proposition 2.4, Theorem 3.1, and Propositions 4.1–4.3.
2. Peter Harmand, Dirk Werner, Wend Werner, *M-Ideals in Banach Spaces and Banach Algebras*, Lecture Notes in Mathematics 1547, Springer, 1993; Chapter III, Proposition 1.2 and Theorem 1.6.
