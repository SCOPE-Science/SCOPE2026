# A sharp time–fidelity law for three-community quantum-wave transfer

## Finding

Consider a three-vertex path with equal positive vertex masses \(M\) and equal positive edge weights \(k\). Put
\[
L=\frac{k}{M}\begin{pmatrix}1&-1&0\\-1&2&-1\\0&-1&1\end{pmatrix},\qquad
P(\tau)=\left|\big[\cos(\tau\sqrt L)\big]_{1,3}\right|^2.
\]
Then transfer between the endpoints is arbitrarily close to perfect, but never exactly perfect at a finite time. Its **sharp global long-time fidelity law** is
\[
\boxed{\liminf_{\tau\to\infty}\tau^2\bigl(1-P(\tau)\bigr)
=\frac{M}{k}\frac{\pi^4}{144}.}
\]
In particular, an asymptotic infidelity of order \(o(\tau^{-2})\) is impossible, while an explicit infinite sequence of readout times attains the constant. The matching lower bound, not merely an approximation subsequence, is the assertion of the theorem.

For \(j\ge0\), define positive integers \(p_j,q_j\) by
\[
p_j+q_j\sqrt3=(2+\sqrt3)^{2j+1},\qquad
z_j=p_j+q_j\sqrt3,
\qquad
\tau_j=\pi\sqrt{\frac{M}{k}}\frac{z_j}{2\sqrt3}.
\]
Then
\[
1-P(\tau_j)=\frac{\pi^2}{12z_j^2}+O(z_j^{-4}),
\qquad
\tau_j^2\bigl(1-P(\tau_j)\bigr)
\longrightarrow \frac{M}{k}\frac{\pi^4}{144}.
\]
At the source's three-\(K_4\) example, \(M=12\) and \(k=1\), the sharp constant is \(\pi^4/12=8.117424252833536\ldots\).

## Assumptions and scope

The quantities \(M,k\) are fixed positive real numbers for the reduced wave equation; in the weak-edge Grover-walk interpretation they are, respectively, the common number of internal directed arcs of each community and the common number of weak links joining successive communities (hence positive integers for realizable graphs). The path comprises exactly three communities and has no direct first-to-third weak link. The transfer observable is the squared real endpoint entry of the reduced propagator \(\cos(\tau\sqrt L)\), with continuous reduced time \(\tau\ge0\). The two limiting operations discussed below are not interchanged.

## Proof

**Spectral reduction.** Set \(s=\tau\sqrt{k/M}\). The path Laplacian before multiplication by \(k/M\) has simple eigenvalues \(0,1,3\), with normalized eigenvectors
\[
\frac1{\sqrt3}(1,1,1),\quad
\frac1{\sqrt2}(1,0,-1),\quad
\frac1{\sqrt6}(1,-2,1).
\]
Their endpoint projection products are \(1/3,-1/2,1/6\). Therefore
\[
a(s):=[\cos(s\sqrt{L(P_3)})]_{1,3}
=\frac13-\frac12\cos s+\frac16\cos(\sqrt3s),
\qquad P(\tau)=a(s)^2.
\]
Since \(-1/3\le a(s)\le1\) and
\[
1-a(s)=\frac{1+\cos s}{2}+\frac{1-\cos(\sqrt3s)}6,
\]
exact unit transfer would require \(s=(2r+1)\pi\) and \(\sqrt3s=2m\pi\) for integers \(r,m\). The irrationality of \(\sqrt3\) excludes this.

**Universal lower bound.** It suffices to consider an arbitrary sequence \(s_n\to\infty\) with bounded \(s_n^2(1-a(s_n)^2)\); other sequences cannot decrease the liminf. Since \(1+a(s_n)\ge 2/3\), the displayed nonnegative decomposition forces \(1+\cos s_n=O(s_n^{-2})\) and \(1-\cos(\sqrt3s_n)=O(s_n^{-2})\). Thus there are odd integers \(q_n\) and even integers \(p_n\) with
\[
e_{1,n}=s_n-\pi q_n=O(s_n^{-1}),\qquad
e_{2,n}=\sqrt3s_n-\pi p_n=O(s_n^{-1}).
\]
Taylor expansion with uniform remainders in this regime gives
\[
1-a(s_n)^2=\frac{e_{1,n}^2}{2}
+\frac{e_{2,n}^2}{6}+O(s_n^{-4}).
\]
The exact sum-of-squares identity
\[
\frac{e_1^2}{2}+\frac{e_2^2}{6}
=\frac{(e_2-\sqrt3e_1)^2}{12}
+\frac{(\sqrt3e_1+e_2)^2}{12}
\]
and the phase relation \(e_{2,n}-\sqrt3e_{1,n}=\pi(\sqrt3q_n-p_n)\) imply
\[
1-a(s_n)^2\ge
\frac{\pi^2}{12}
\frac{(p_n^2-3q_n^2)^2}{(p_n+\sqrt3q_n)^2}
-O(s_n^{-4}).
\]
The integer \(p_n^2-3q_n^2\) is nonzero, since \(\sqrt3\) is irrational. Moreover, \(p_n+\sqrt3q_n=2\sqrt3s_n/\pi+O(s_n^{-1})\). Multiplying through by \(s_n^2\) and using \((p_n^2-3q_n^2)^2\ge1\) proves
\[
\liminf_{s\to\infty}s^2(1-a(s)^2)\ge\pi^4/144.
\]
This argument applies to every high-fidelity sequence, not merely times arising from continued fractions.

**Sharpness and exact timing.** Powers of \(2+\sqrt3\) give \(p_j\) even, \(q_j\) odd, and \(p_j^2-3q_j^2=1\). Set \(z_j=p_j+\sqrt3q_j\); then \(p_j-\sqrt3q_j=z_j^{-1}\). At \(s_j=\pi z_j/(2\sqrt3)\), the phase errors relative to the required odd/even multiples of \(\pi\) are exactly
\[
e_{1,j}=\frac{\pi}{2\sqrt3z_j},\qquad
e_{2,j}=-\frac{\pi}{2z_j}.
\]
They annihilate the second square in the displayed identity. Therefore
\[
1-a(s_j)^2=\frac{\pi^2}{12z_j^2}+O(z_j^{-4}),
\qquad s_j^2(1-a(s_j)^2)\to\pi^4/144.
\]
Together with the lower bound, this proves the claimed sharp limit inferior. Scaling \(s=\tau\sqrt{k/M}\) gives the factor \(M/k\).

## Verification

The bundled `verify.py` uses an independent numerical eigendecomposition of the three-by-three path Laplacian, a direct test of the completed-square identity, exact integer Pell recurrences, and 100-digit trigonometric evaluation at optimized and unshifted Pell readout times. It completed **319 finite assertions**, including agreement with the sharp constant \(\pi^4/144\). These checks are independent corroboration; the infinite-time lower bound is proved above, not inferred from numerics. Run `python verify.py` with the dependencies in `requirements.txt`.

## Relationship to prior work

Hosaka and Segawa, *Pulsation of quantum walk on finite graphs*, arXiv:2610.07768v1, Theorem 3.1 and Section 4.1, establish the reduced wave equation and its three-community cosine formula, including the \(M=12,k=1\) example. Those formulas are premises, not new discoveries here. General quantum-walk transfer theory is developed by Chan and Zhan (arXiv:2105.03762) and by Guo and Schmeits (arXiv:2411.05560), but the inspected results do not evaluate the sharp continuous-time three-community fidelity constant.

Qualitative arbitrarily accurate endpoint transfer and **unshifted Pell observation times** with infidelity \(O(q^{-2})\) are already available for this reduced-path model. The present theorem claims neither the qualitative transfer conditions nor Pell recurrence itself as new. Its added content is a **matching lower bound valid over all observation times**, an exact optimal constant, and the shifted readout times that saturate it; this improves the preceding unshifted-time constant by a factor of two. No conclusion is drawn about uniqueness across the full literature.

## Limitations

The sharp rate concerns only the symmetric three-community reduced wave with equal masses and equal bridge weights. For the full weighted discrete-time Grover walk, the motivating theorem gives convergence to this reduced probability as the weak-link strength tends to zero **at each fixed rescaled time**. Its error bound is not uniform in the unbounded Pell-time sequence, so this result does **not** claim a simultaneous small-coupling/large-observation-time asymptotic for the original discrete walk. It does not cover asymmetric three-community systems, networks of four or more communities, or optimal integer step counts in the original dynamics. An independently established priority assessment is not available.

## References

1. T. Hosaka and E. Segawa, *Pulsation of quantum walk on finite graphs*, arXiv:2610.07768v1 (first public 2026-10-06), particularly Theorem 3.1 and Section 4.1. https://arxiv.org/html/2610.07768v1
2. A. Chan and H. Zhan, *Pretty good state transfer in discrete-time quantum walks*, arXiv:2105.03762 (2021). https://arxiv.org/abs/2105.03762
3. K. Guo and V. Schmeits, *State transfer in discrete-time quantum walks via projected transition matrices*, arXiv:2411.05560v2 (2025 version). https://arxiv.org/html/2411.05560v2
