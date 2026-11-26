# Strict amplification under a twist of a circular ladder

## Finding

For each integer \(m\ge3\), let \(M_m\) be the Möbius ladder, with the cycle edges of \(C_{2m}\) and the \(m\) chords joining antipodal vertices. Let \(Q_m=C_m\square K_2\) be the ordinary prism. Write \(P_G\) for the orthogonal projection onto gradient edge flows of \(G\), with unit conductance at every edge. Then
\[
\|P_{M_m}\|_{\infty\to\infty}>\|P_{Q_m}\|_{\infty\to\infty}\qquad (m\ge3).
\]
With \(r=2-\sqrt3\), the sharp gaps along the even and odd subsequences are
\[
\begin{aligned}
\|P_{M_{2h}}\|_{\infty\to\infty}-\|P_{Q_{2h}}\|_{\infty\to\infty}
 &=\frac{2}{\sqrt3}r^h+o(r^h),\\
\|P_{M_{2h+1}}\|_{\infty\to\infty}-\|P_{Q_{2h+1}}\|_{\infty\to\infty}
 &=\frac{1+r}{\sqrt3}r^h+o(r^h).
\end{aligned}
\]
Thus the boundary twist has a strictly positive but exponentially small effect on the maximum-coordinate amplification. The separate Möbius-ladder norm formula and its logarithmic deficit from three are not contributions of this result.

## Assumptions and scope

The edges are real coordinates with the usual Euclidean inner product and the maximum-coordinate norm. If \(B\) is an oriented edge-by-vertex incidence matrix, then \(P_G=B(B^{\mathsf T}B)^\dagger B^{\mathsf T}\). Orientation changes conjugate this matrix by a diagonal sign matrix, which preserves the induced norm. That norm is the largest absolute row sum. No weighted or open ladders are included.

## Proof

**Row formulas used for the comparison.** Pair the vertices across each rung and decompose the Laplacian into the symmetric and antisymmetric sectors under exchanging the partners. The symmetric sector has the ordinary cycle Laplacian in both graphs; on cycle-edge gradients its projection has entries \(\delta_{j0}-1/m\) in the row at zero. In the antisymmetric sector the operator is \(4I-S-S^{-1}\), with the shift \(S\) antiperiodic for \(M_m\) and periodic for \(Q_m\). Write respectively \(b_j\) and \(p_j\) for the Green function at zero, so that for \(0\le j\le m\)
\[
b_j=\frac{r^j-r^{m-j}}{2\sqrt3(1+r^m)},\qquad
p_j=\frac{r^j+r^{m-j}}{2\sqrt3(1-r^m)}.
\]
These expressions solve the homogeneous recurrence off zero by \(r^2-4r+1=0\), give \(4g_0-2g_1=1\) there, and extend by \(b_{j+m}=-b_j\), \(p_{j+m}=p_j\). The two massive operators are invertible.

For a cycle-edge row, the two cycle-edge coordinates at rung index \(j\) are, up to sign, the half-sum and half-difference of the corresponding symmetric and antisymmetric sector entries. For \(g=b\) or \(p\) the latter entry is the second difference \(2g_j-g_{j-1}-g_{j+1}=\delta_{j0}-2g_j\). The pair therefore contributes \(\max\{|\delta_{j0}-1/m|,|\delta_{j0}-2g_j|\}\). At zero the contribution is \(1-1/m\): \(b_0\ge5/18\) and \(p_0>1/(2\sqrt3)\), while both are less than \(1/2\). The rung-coordinate contributions are the sum of the absolute first differences of \(g\) over a period (antiperiod for \(b\)); the incidence factors \(1/\sqrt2\) and \(\sqrt2\) cancel. The sequence \(b_j\) decreases from \(b_0\) to \(-b_0\); \(p_j\) decreases to its central minimum at \(h=\lfloor m/2\rfloor\) and returns to \(p_0\). For a rung row the corresponding first-difference sum is doubled because there are two cycle-edge copies, and the rung-rung contribution is \(2\sum_{j=0}^{m-1}|g_j|\). In the periodic case the last sum is \(1\) since the Green entries are positive and sum to \(1/2\). Thus the Möbius cycle and rung row sums \(S_m,R_m\), and the prism cycle and rung row sums \(H_m,V_m\), are
\[
\begin{aligned}
S_m &=1-\frac1m+\sum_{j=1}^{m-1}\max\{1/m,2|b_j|\}+2b_0, &
R_m &=4b_0+2\sum_{j=0}^{m-1}|b_j|,\\
H_m &=1-\frac1m+\sum_{j=1}^{m-1}\max\{1/m,2p_j\}+2(p_0-p_h), &
V_m &=1+4(p_0-p_h).
\end{aligned}
\]
Rotations and layer exchange act transitively on each of the two edge types as needed, so these exhaust the row sums. Direct substitution at \(m=3\) gives \((S_3,R_3,H_3,V_3)=(17/9,17/9,26/15,9/5)\), proving the strict comparison there. At \(m=4\) the four entries are \((29/14,2,2,2)\). For \(m\ge5\), the estimates \(S_m\ge2-2/m+2b_0\), \(b_0<1/(2\sqrt3)\), and \(\sum_{j=1}^{m-1}|b_j|<r/[\sqrt3(1-r)]\) give \(S_m-R_m>1-2/m-1/\sqrt3>0\). Also \(H_m-V_m\ge 1-2/m-2p_0>0\): \(p_0\) decreases in \(m\), with \(2p_0=11/19\) at \(m=5\). Hence for \(m\ge4\) the desired gap is \(S_m-H_m\).

**Strict comparison.** Set
\[
D_m=\sum_{j=1}^{m-1}\left(\max\{1/m,2p_j\}-\max\{1/m,2|b_j|\}\right).
\]
Then \(S_m-H_m=2(b_0-p_0+p_h)-D_m\). Each bracket in \(D_m\) is nonnegative since \(p_j>|b_j|\). The central index (two reflected indices for odd \(m\)) contributes zero because \(2p_h<1/m\). To see this for all \(m\ge4\), the inequality holds at \(m=4,5\) by substitution. Along each parity, \(mr^{\lfloor m/2\rfloor}\) decreases since the ratio for \(m\mapsto m+2\) is \((m+2)r/m<1\); the factor \(1/(1-r^m)\) decreases as well. Reflection of the other indices and the 2-Lipschitz bound for \(x\mapsto\max\{1/m,2x\}\) give
\[
D_m\le4\sum_{j=1}^{h-1}(p_j-b_j)
=\frac{4\sum_{j=1}^{h-1}(r^{m-j}+r^{m+j})}{\sqrt3(1-r^{2m})}.
\]
For \(m=2h\), the positive term \(2(b_0-p_0+p_h)\) is
\[
\frac{2r^h(1-2r^h)}{\sqrt3(1-r^{2h})}.
\]
With \(t=r^h\), the ratio of the geometric bound for \(D_m\) to this positive term is less than
\[
\frac{2r}{1-r}\,\frac{1+t}{(1+t^2)(1-2t)}
\le\frac{2r}{1-r}\,\frac{1+r^2}{1-2r^2}<1
\qquad(h\ge2).
\]
For \(m=2h+1\), the positive term equals
\[
\frac{r^h[(1+r)(1+r^{2h+1})-4r^{h+1}]}{\sqrt3(1-r^{4h+2})},
\]
whereas the same geometric bound gives
\[
D_m<\frac{4r^{h+2}(1+r^h)}{\sqrt3(1-r)(1-r^{4h+2})}.
\]
The first exceeds the second when \(h\ge2\) because \(1+r-4r^3>4r^2(1+r^2)/(1-r)\). Both strict numerical inequalities follow, for example, from \(0<r<27/100\). This proves the comparison for all sizes.

**Asymptotic gap.** For \(d=\min(j,m-j)\), \(p_j\le C r^d\) with a constant independent of \(m,j\). A nonzero bracket in \(D_m\) must have \(p_j>1/(2m)\), hence \(d=O(\log m)\) and \(r^{-d}=O(m)\). At such an index \(p_j-|b_j|=O(r^{m-d})\), so \(D_m=O(m\log m\,r^m)=o(r^{\lfloor m/2\rfloor})\). Also \(b_0-p_0=O(r^m)\). From the explicit formula for \(p_h\), \(2p_h\) has leading coefficient \(2/\sqrt3\) times \(r^h\) for even \(m=2h\), and \((1+r)/\sqrt3\) times \(r^h\) for odd \(m=2h+1\). These are the claimed gaps.

## Verification

With SymPy installed, `python3 check.py` computes both projections over exact rationals for \(3\le m\le12\), compares all row sums with the expressions used above, and tests the strict comparison in that range. The test is finite; the universal inequality and the parity asymptotics are established by the analytic proof.

## Relationship to prior work

Azimi and Farrokhi Derakhshandeh Ghouchan, [arXiv:2306.10497](https://arxiv.org/abs/2306.10497), Corollaries 4.7 and 5.4, give explicit Laplacian pseudoinverses for the prism and Möbius ladder. These determine the projection entries but do not state the absolute-row-sum comparison or its parity asymptotics. [*Sharp logarithmic endpoint projection deficit on Möbius ladders*](https://github.com/Resultary/2026/tree/main/2026/10/26/SCOPE-sharp-logarithmic-endpoint-projection-deficit-on-m-bius-ladders--833010be3478) gives the equivalent Möbius cut-projector norm formula and its logarithmic deficit. The result here compares the two topologies, including the cancellation involved in determining their exponentially smaller norm difference.
