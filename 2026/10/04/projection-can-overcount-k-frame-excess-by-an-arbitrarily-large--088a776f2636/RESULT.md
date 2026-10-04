# Projection can overcount \(K\)-frame excess by an arbitrarily large amount
## Finding
Let \(K\) be a nonzero bounded operator with closed range on a Hilbert space \(\mathcal H\), let \(R=R(K)\), and let \(P_R\) be the orthogonal projection onto \(R\). For every \(K\)-frame \(\Phi=(\varphi_i)_{i\in I}\), the projected family \(P_R\Phi=(P_R\varphi_i)_{i\in I}\) is an ordinary frame for \(R\), and the two excesses satisfy
\[
E_K(\Phi)\le E(P_R\Phi).
\]
Equality holds whenever \(\Phi\) is a near \(K\)-Riesz basis. Equality also holds, without a near-Riesz hypothesis, whenever every atom \(\varphi_i\) lies in \(R\).

The inequality can be arbitrarily far from equality. For every integer \(N\ge2\), there are \(\mathcal H=\mathbb R^N\), a rank-one orthogonal projection \(K\), and an orthonormal basis \(\Phi_N\) such that
\[
E_K(\Phi_N)=0,
\qquad
E(P_R\Phi_N)=N-1
=
\dim\ker(P_RT_{\Phi_N}).
\]
Consequently the unrestricted identity \(E_K(\Phi)=E(P_{R(K)}\Phi)\) printed as equation (5.1) in Theorem 5.9 of Agheshteh Moghaddam--Arefijamaal is not valid for arbitrary \(K\)-frames. Its near \(K\)-Riesz-basis regime survives, but projection alone can create arbitrarily large apparent redundancy outside that regime.

## Assumptions and scope
The operator \(K\) is assumed nonzero and to have closed range. The excess \(E_K(\Phi)\) is the greatest number of atoms that can be deleted while leaving a \(K\)-frame, with value \(+\infty\) if there is no finite upper bound. The ordinary frame excess \(E(P_R\Phi)\) is defined analogously for the projected frame on \(R\).

The closed-range assumption is used only to obtain a constant \(c>0\) such that
\[
\|K^*f\|\ge c\|f\|
\quad\text{for every }f\in R.
\]
No assertion is made here for non-closed-range operators, where that uniform lower bound can fail.

## Proof
Because \(K\) has closed range, \(R=N(K^*)^\perp\), and the restriction of \(K^*\) to \(R\) is bounded below. If a subfamily \(\Psi=(\psi_i)_{i\in J}\) is a \(K\)-frame with lower bound \(A>0\), then for every \(f\in R\),
\[
\sum_{i\in J}|\langle f,P_R\psi_i\rangle|^2
=
\sum_{i\in J}|\langle f,\psi_i\rangle|^2
\ge A\|K^*f\|^2
\ge Ac^2\|f\|^2.
\]
The Bessel upper bound is inherited as well, so \(P_R\Psi\) is a frame for \(R\). Therefore every deletion that is legal for the \(K\)-frame is also legal for the projected ordinary frame. This proves
\[
E_K(\Phi)\le E(P_R\Phi),
\]
including the case in which one or both excesses are infinite.

Now suppose that \(\Phi\) is a near \(K\)-Riesz basis. By definition there is a finite set \(\sigma\subset I\) such that \(\Phi_{I\setminus\sigma}\) is a \(K\)-Riesz basis. Hence deleting \(\sigma\) is legal, so \(E_K(\Phi)\ge|\sigma|\). The projected family \(P_R\Phi_{I\setminus\sigma}\) is both a frame for \(R\) and a Riesz sequence, hence a Riesz basis for \(R\). Thus \(P_R\Phi\) is a Riesz basis plus \(|\sigma|\) additional atoms, and its ordinary excess is exactly \(|\sigma|\). Combining this with the universal inequality gives
\[
E_K(\Phi)=E(P_R\Phi)=|\sigma|.
\]

There is a second sufficient condition for equality. If every \(\varphi_i\in R\), then for any subfamily and any \(f\in\mathcal H\),
\[
\langle f,\varphi_i\rangle
=
\langle P_Rf,\varphi_i\rangle.
\]
If that subfamily is a frame for \(R\) with lower bound \(a>0\), then
\[
\sum_i|\langle f,\varphi_i\rangle|^2
\ge a\|P_Rf\|^2
\ge \frac{a}{\|K\|^2}\|K^*f\|^2,
\]
so it is a \(K\)-frame. The converse was proved in the first paragraph. Thus exactly the same deletion sets are legal for the \(K\)-frame and the projected frame, giving equality of excesses.

For the arbitrary-gap construction, fix \(N\ge2\), set \(\mathcal H=\mathbb R^N\), and let \(K=P_R\) where \(R=\operatorname{span}\{e_1\}\). Choose an orthonormal basis \(u_1,\ldots,u_N\) satisfying
\[
\langle e_1,u_j\rangle=N^{-1/2}
\quad (1\le j\le N).
\]
Such a basis exists because the unit vector \(N^{-1/2}(1,\ldots,1)\) can be chosen as the first row of an orthogonal matrix. Let \(\Phi_N=(u_j)_{j=1}^N\). Since \(\Phi_N\) is an orthonormal basis, it is a \(K\)-frame. If \(u_j\) is deleted, test the remaining family on \(f=u_j\): all remaining coefficients vanish, whereas
\[
\|K^*u_j\|^2=|\langle e_1,u_j\rangle|^2=\frac1N>0.
\]
Hence no atom can be deleted and \(E_K(\Phi_N)=0\). On the other hand,
\[
P_Ru_j=N^{-1/2}e_1
\quad (1\le j\le N),
\]
so the projected family consists of \(N\) identical nonzero vectors in a one-dimensional space. Exactly \(N-1\) of them can be removed. Therefore \(E(P_R\Phi_N)=N-1\), proving an arbitrarily large finite gap.

## Verification
The critical implications were checked directly from the definitions rather than inferred from equation (5.1). In particular: closed range gives the lower bound for \(K^*\) on \(R(K)\); every legal \(K\)-frame deletion projects to a legal ordinary-frame deletion; support inside \(R(K)\) makes the converse deletion implication valid; and the finite-dimensional orthonormal-basis family gives exact excesses \(0\) and \(N-1\) for every \(N\ge2\).

For the smallest instance, take \(N=2\), \(K=\operatorname{diag}(1,0)\), \(u_1=2^{-1/2}(1,1)\), and \(u_2=2^{-1/2}(1,-1)\). Deleting either vector annihilates all remaining coefficients on the deleted vector while \(K^*u_j\ne0\), so the \(K\)-excess is \(0\). The two projections are both \(2^{-1/2}e_1\), so the projected-frame excess is \(1\).

No computation is used to extrapolate from finite cases: the arbitrary-\(N\) construction and both excess values are proved symbolically.

## Relationship to prior work
Agheshteh Moghaddam and Arefijamaal define \(K\)-frame excess and state in Theorem 5.9 that, for a \(K\)-frame, equation (5.1) gives
\[
E_K(\Phi)=\dim\ker(P_{R(K)}T_\Phi)=E(P_{R(K)}\Phi).
\]
Their theorem first discusses near \(K\)-Riesz bases, but the displayed final assertion is stated for a \(K\)-frame and its proof separately treats infinite excess. The result above shows that the unrestricted extension is false while also explaining why equality is correct in the near \(K\)-Riesz regime.

The ordinary identity between frame excess and synthesis-kernel dimension, used in that paper through Holub's near-Riesz theory, remains valid for the projected ordinary frame. The failure occurs in identifying that projected redundancy with deletability in the original \(K\)-frame: components in \(R(K)^\perp\) can prevent deletions even though projection erases them.

## Limitations
The result does not classify every \(K\)-frame for which equality holds; it provides a universal one-sided inequality, two substantial equality classes, and an arbitrary-gap obstruction. It does not address operators whose range is not closed. It also does not reassess other theorems in the cited paper that may use equation (5.1).

## References
1. E. Agheshteh Moghaddam and A. A. Arefijamaal, *New aspects of weaving K-frames: the excess and duality*, Hacettepe Journal of Mathematics and Statistics 53(3) (2024), 652--666, DOI 10.15672/hujms.1008448. See Definition 5.1 and Theorem 5.9, especially equation (5.1).
2. J. R. Holub, *Pre-Frame Operators, Besselian Frames, and Near-Riesz Bases in Hilbert Spaces*, Proceedings of the American Mathematical Society 122(3) (1994), 779--785, DOI 10.1090/S0002-9939-1994-1204376-4.
