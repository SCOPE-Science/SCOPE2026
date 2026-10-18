# Exact Fourier stability of the Wigner-enhanced polygonal isoperimetric deficit

## Finding

Let \(n\ge2\) be an integer and let \(P\) be a strictly convex equiangular Euclidean polygon with \(2n\) genuine sides, numbered cyclically, whose opposite sides are parallel. Write \(\ell_j>0\) for its successive side lengths, with subscripts modulo \(2n\), and define the opposite-edge pair sums and their mean by
\[
 p_j=\ell_j+\ell_{j+n},\qquad
 \bar p=\frac1n\sum_{j=0}^{n-1}p_j,\qquad 0\le j<n.
\]
Let \(W(P)\) be the Wigner caustic, the oriented closed polygonal chain of midpoints of opposite vertices, traversed once through \(n\) consecutive indices. Its signed area \(A^*(W(P))\) is the shoelace area of that chain; it need not be positive. Write \(L(P)\) and \(A(P)\) for perimeter and enclosed area. Put \(\theta=\pi/(2n)\) and
\[
 \mathcal D(P)=L(P)^2-8n\tan\theta\bigl(A(P)+2|A^*(W(P))|\bigr).
\]
Then the following **globally sharp quantitative refinement** holds:
\[
 \boxed{\ \mathcal D(P)\ge \frac{\kappa_n}{4}
             \sum_{j=0}^{n-1}(p_j-\bar p)^2\ },\qquad
 \kappa_n=\begin{cases}
  4n\tan^2\theta,&n\text{ even},\\
  \dfrac{4n\sin^2\theta}{\cos(2\theta)},&n\text{ odd}.
 \end{cases}
\]
The coefficient is attained by genuine, strictly convex polygons at every \(n\). In particular, for \(n=2\) or \(n=3\), **every** admissible polygon attains equality. For \(n\ge4\), equality holds precisely when the vector \((p_j-\bar p)_{j=0}^{n-1}\) has Fourier support in the maximally alternating modes: \(k=n/2\) for even \(n\), and \(k=(n-1)/2,(n+1)/2\) for odd \(n\). The usual zero-deficit equality criterion \(p_0=\cdots=p_{n-1}\) is consequently quantitative.

An exact, stronger identity gives every mode's contribution. Define
\[
 b_j=\frac{p_j}{2},\qquad
 \widehat b_k=\frac1n\sum_{j=0}^{n-1}b_j\exp(-2\pi i kj/n).
\]
Then
\[
 \boxed{\ \mathcal D(P)=n\sum_{k=1}^{n-1}
 \frac{4n\sin^2\theta}{\sin^2(\pi k/n)-\sin^2\theta}
 |\widehat b_k|^2.\ }
\]
This identity and the sharp inequality hold for all \(n\ge2\), without a fixed-perimeter or a central-symmetry assumption on \(P\).

## Assumptions and scope

Here **equiangular** means all exterior turning angles equal \(\pi/n\). **Opposite sides parallel** means that edge vectors \(e_j\) and \(e_{j+n}\) are collinear, oppositely directed, for every \(j\). The central symmetral \(Q=(P-P)/2\) is then a centrally symmetric equiangular \(2n\)-gon with edge lengths \(b_j=b_{j+n}=p_j/2\). All displayed quantities are Euclidean; there is no affine normalization. The signed-area convention is counterclockwise shoelace area, and the Wigner caustic is traversed through just one half-cycle of vertex-midpoints. The theorem does not assert a sharp variance inequality for non-equiangular polygons.

## Proof

**1. Reduction to a centrally symmetric polygon.**  Number vertices \(v_j\) counterclockwise, so \(e_j=v_{j+1}-v_j\). Define \(w_j=(v_j+v_{j+n})/2\) and \(q_j=(v_j-v_{j+n})/2\), extended cyclically. Then \(w_{j+n}=w_j\) and \(q_{j+n}=-q_j\); the \(q_j\) form the vertices of \(Q=(P-P)/2\). The \(j\)-th edge of \(Q\) is \((e_j-e_{j+n})/2\), hence has length \(b_j=(\ell_j+\ell_{j+n})/2\) and shares the original edge's direction. Consequently \(L(Q)=L(P)\). Expanding the shoelace determinant of \(v_j=w_j+q_j\), the cross terms cancel between indices \(j\) and \(j+n\), giving
\[
 A(P)=A(Q)+2A^*(W(P)).
\]
The Wigner caustic of a convex polygon with paired parallel opposite edges has \(A^*(W(P))\le0\); one can see this directly from the area identity and the planar Brunn–Minkowski inequality \(A((P-P)/2)\ge A(P)\), or from the pair-midpoint construction. Therefore
\[
 A(Q)=A(P)+2|A^*(W(P))|,
\]
and the enhanced deficit equals the ordinary fixed-side-count isoperimetric deficit of \(Q\):
\[
 \mathcal D(P)=L(Q)^2-8n\tan\theta\,A(Q).
\]
These relations are also equations (4.4)–(4.9) in the motivating work of Konicer and collaborators.

**2. The exact area quadratic form.**  Rotate coordinates so that the first \(n\) successive edge vectors of \(Q\) have arguments \(j\pi/n\), for \(0\le j<n\); their lengths are \(b_j>0\). The remaining \(n\) edges are their negatives. Shoelace expansion, or decomposing the resulting zonogon into pairwise parallelograms, yields
\[
 A(Q)=\sum_{0\le j<r<n} b_jb_r\sin\frac{(r-j)\pi}{n}.
\]
For completeness, the closed edge chain has total area
\(\frac12\sum_{0\le a<c<2n}\det(e_a,e_c)\); pairing \(e_{j+n}=-e_j\) makes each first-half pair contribute \(b_jb_r\sin((r-j)\pi/n)\). Introduce the real symmetric circulant matrix
\[
 B_{jr}=\begin{cases}0,&j=r,\\
 \frac12\sin(\pi|j-r|/n),&j\ne r.
 \end{cases}
\]
The matrix is circulant because \(\sin(\pi(n-d)/n)=\sin(\pi d/n)\). Then \(A(Q)=b^{\mathsf T}Bb\), \(L(Q)=2\sum_jb_j\), and
\[
 \mathcal D(P)=b^{\mathsf T}\bigl(4J-8n\tan\theta\,B\bigr)b,
\]
where \(J\) is the all-ones matrix.

**3. Complete Fourier diagonalization.**  On the Fourier vector with \(j\)-th component \(\exp(2\pi i kj/n)\), the matrix \(B\) has eigenvalue
\[
 \mu_k=\frac12\sum_{r=1}^{n-1}\sin(\pi r/n)\cos(2\pi kr/n).
\]
The geometric-series identity \(\sum_{r=1}^{n-1}\sin(m\pi r/n)=\cot(m\pi/(2n))\) for odd integer \(m\) gives, for \(1\le k<n\),
\[
 \mu_k=\frac14\bigl(\cot((2k+1)\theta)-\cot((2k-1)\theta)\bigr)
 =-\frac{\sin(2\theta)}{4\bigl(\sin^2(\pi k/n)-\sin^2\theta\bigr)}.
\]
For \(k=0\), \(\mu_0=\frac12\cot\theta\). Thus the zero-frequency eigenvalue of \(4J-8n\tan\theta\,B\) is \(4n-8n\tan\theta\,(\cot\theta/2)=0\). At nonzero frequencies \(J\) vanishes, and the eigenvalues are
\[
 \lambda_k=-8n\tan\theta\,\mu_k
 =\frac{4n\sin^2\theta}{\sin^2(\pi k/n)-\sin^2\theta}>0.
\]
The denominator is positive because \(\sin(\pi k/n)\ge\sin(\pi/n)>\sin\theta\). Parseval's formula \(\sum_j|b_j|^2=n\sum_k|\widehat b_k|^2\) gives the asserted exact identity.

**4. Sharp constant and all equality modes.**  The smallest nonzero eigenvalue occurs where \(\sin^2(\pi k/n)\) is largest. For even \(n\), its unique maximizing frequency is \(k=n/2\), and \(\lambda_{n/2}=4n\tan^2\theta\). For odd \(n\), the two maximizing frequencies are \(k=(n\pm1)/2\), and since \(\sin^2(\pi(n-1)/(2n))=\cos^2\theta\), their common eigenvalue is \(4n\sin^2\theta/\cos(2\theta)\). Parseval applied to the mean-zero part of \(b\) yields
\[
 \mathcal D(P)\ge\kappa_n\sum_{j=0}^{n-1}(b_j-\bar b)^2
   =\frac{\kappa_n}{4}\sum_{j=0}^{n-1}(p_j-\bar p)^2.
\]
Equality holds exactly for the real eigenspace of this lowest eigenvalue. In concrete terms, \(b_j=c+a(-1)^j\) for even \(n\), and \(b_j=c+a\cos(\pi(n-1)j/n)+d\sin(\pi(n-1)j/n)\) for odd \(n\), with positive entries. Each such vector is realizable: draw consecutive edges \(b_j\exp(\pi i j/n)\), followed by their negatives. The resulting closed polygon is centrally symmetric, has strictly positive sides and equal exterior angles, and achieves equality. For \(n=2,3\) the minimizing modes exhaust the entire nonconstant spectrum. This establishes both global sharpness and the asserted equality classification. \(\square\)

## Verification

The standalone `CHECK.py` reconstructs polygons directly from independently generated edge vectors, computes their shoelace area and Wigner-caustic area, compares the geometric deficit against a separate discrete-Fourier calculation, and verifies positivity and equality for the minimizing modes. Executing `python3 CHECK.py` passed 1,163 test polygons of orders \(2\le n\le21\), with maximum absolute residual below \(6\times10^{-12}\), and tested equality at each order. These are finite consistency checks; the universal claim follows from the explicit algebraic proof above, not from finite tests.

## Relationship to prior work

Konicer, Murawski, Rogala, Wieczorek, and Zwierzyński (2026), Theorem 4.4, establish the Wigner-enhanced inequality and characterize its **zero deficit**, but do not state the sharp stability coefficient, its parity split, or the complete opposite-edge-pair Fourier spectrum. Their Remark 4.6 notes a discrete Fourier route to the qualitative inequality, citing Kwong (2024) and Fisher–Ruoff–Shilleto (1985). Kwong's published Fourier inequalities concern general polygonal Hermitian forms and squared-edge energies, not the exact optimal coefficient for the enhanced perimeter-squared deficit expressed in opposite-side sums. Indrei's (2015) general quantitative polygonal inequality supplies a dimension-dependent stability constant without this optimized equiangular CPPOS coefficient or its equality eigenspaces. Joós–Lángi (2023) study extremal zonotope intrinsic volumes, a related but distinct optimization problem. These broader techniques are acknowledged; the claimed increment is the **explicit sharp quantitative coefficient and equality-mode classification** for the Wigner-enhanced deficit, not the existence of Fourier methods or the unstrengthened inequality.

## Limitations

The result assumes equal exterior turning angles and parallel opposite sides and does not give a stability coefficient for arbitrary CPPOSes. It measures imbalance in opposite-edge **pair sums**, not individual opposite edges; distinct nonsymmetric polygons sharing the same central symmetral cannot be distinguished by this deficit. The main sharp coefficient has units of a squared length on each side of the inequality. An independent historical-priority audit has not been undertaken. Older polygonal Fourier sources may contain reformulations of the sharp special-case coefficient; the full text of Fisher–Ruoff–Shilleto (1985) was not accessible during this review, although its role as antecedent is recognized. The inequality is therefore presented with that priority limitation, without claiming a new Fourier method.

## References

1. I. Konicer, B. Murawski, B. Rogala, T. Wieczorek, and M. Zwierzyński, *Convex Polygons with Parallel Opposite Sides: Convergence, Reconstruction, and Isoperimetric Inequalities*, arXiv:2606.22612 (first submitted 2026-06-21), Theorem 4.4 and Remark 4.6. https://arxiv.org/abs/2606.22612
2. K.-K. Kwong, *A unified approach to higher order discrete and smooth isoperimetric inequalities*, Mathematika 70 (2024), e12238. https://doi.org/10.1112/mtk.12238
3. E. Indrei, *A sharp lower bound on the polygonal isoperimetric deficit*, Proc. Amer. Math. Soc. (2016), arXiv:1502.05978. https://arxiv.org/abs/1502.05978
4. E. Indrei and L. Nurbekyan, *On the stability of the polygonal isoperimetric inequality*, Adv. Math. 276 (2015), 62–86, arXiv:1402.4460. https://arxiv.org/abs/1402.4460
5. J. C. Fisher, D. Ruoff, and J. Shilleto, *Perpendicular Polygons*, Amer. Math. Monthly 92 (1985), 23–37. https://doi.org/10.2307/2322190
6. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, Mathematika 69 (2023), 508–534. https://doi.org/10.1112/mtk.12191
