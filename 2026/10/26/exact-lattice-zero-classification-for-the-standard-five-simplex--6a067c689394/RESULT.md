# Exact lattice-zero classification for the standard five-simplex \(\Delta_5\)

## Finding

Let
\[
\Delta_5=\{x\in\mathbb R^5:x_j\ge 0\ (1\le j\le5),\ x_1+\cdots+x_5\le1\},
\qquad
F(k)=\int_{\Delta_5}e^{-2\pi i\langle k,x\rangle}\,dx,
\]
where \(k=(k_1,\ldots,k_5)\in\mathbb Z^5\) and the measure is ordinary Lebesgue measure. Write \(\Lambda(k)=\{0,k_1,\ldots,k_5\}\) as a multiset. Then \(F(k)=0\) if and only if one of the following holds:

1. The six nodes of \(\Lambda(k)\) are pairwise distinct.
2. After a common integer translation that makes the minimum node zero,
   \[
   \Lambda=\{0,0,p,p+q,p+q,p+q+r\},\qquad qr=p(p+q+r),
   \]
   for positive integers \(p,q,r\).
3. After such a translation,
   \[
   \Lambda=\{0,p,p,p+q,p+q+r,p+q+r\},\qquad pq=r(p+q+r),
   \]
   for positive integers \(p,q,r\).

The two repeated-node families are infinite. In the first family, the equation is equivalent to \(r>p\) and
\[
\delta=r-p\mid 2p^2,\qquad q=p+\frac{2p^2}{\delta}.
\]
In the reflected family it is equivalent to \(p>r\) and
\[
\delta=p-r\mid 2r^2,\qquad q=r+\frac{2r^2}{\delta}.
\]

## Assumptions and scope

The claim concerns only the standard five-simplex and integer frequencies under the Fourier convention displayed above. It is an exact classification of the zeros on \(\mathbb Z^5\), not a description of the full real or complex zero set, and not a statement about arbitrary affine simplices without transporting the frequency lattice. The multiset formulation is natural because the simplex transform is symmetric in its six barycentric frequency nodes.

## Proof

Put \(c=2\pi i\), \(f(t)=e^{-ct}\), and \(D=f[\lambda_0,\ldots,\lambda_5]\), where \(\lambda_0=0\) and \(\lambda_j=k_j\). The Hermite divided-difference formula gives
\[
F(k)=(-c)^{-5}D.
\]
Thus the transform and the divided difference have the same zero set. If the six integer nodes are distinct, \(f(\lambda_j)=1\) for every node, so \(D=\sum_j\prod_{\ell\ne j}(\lambda_j-\lambda_\ell)^{-1}=0\): this is the vanishing of the leading coefficient in the Lagrange interpolation formula for the constant function.

For repeated nodes, let \(x_0<\cdots<x_{s-1}\) be the distinct integer values, with multiplicities \(m_0,\ldots,m_{s-1}\) summing to six. The confluent residue formula is
\[
D=\sum_{j=0}^{s-1}\operatorname{Res}_{z=x_j}
\frac{e^{-cz}}{\prod_{\ell=0}^{s-1}(z-x_\ell)^{m_\ell}}.
\]
Because \(e^{-cx_j}=1\), each residue is obtained by differentiating a rational function and multiplying by powers of \(c\). The following exhaustive multiplicity check leaves only the type \(2+2+1+1\) as a possible zero:

- Type \(6\) gives \(D=(-c)^5/5!\ne0\).
- Type \(5+1\), with node difference \(d\in\mathbb Z\setminus\{0\}\), has
  \[
  \Re D=\frac{2\pi^2}{d^3}\left(1-\frac{\pi^2d^2}{3}\right)\ne0,
  \]
  since \(|d|\ge1\) and \(\pi^2>3\).
- Type \(4+2\) gives \(D=-c(c^2d^2-6cd+24)/(6d^4)\ne0\), because the bracket has nonzero imaginary part \(-6cd\).
- Type \(4+1+1\), after translating the quadruple node to zero and writing the other nodes as distinct nonzero integers \(a,b\), has
  \[
  D=-\frac{c^3}{6ab}+\frac{c^2(a+b)}{2a^2b^2}-\frac{c(a^2+ab+b^2)}{a^3b^3}.
  \]
  Its real part forces \(a+b=0\). Then \(D=\frac{c}{a^4}(1-2\pi^2a^2/3)\ne0\).
- Type \(3+3\), with node difference \(d\ne0\), gives \(D=6c/d^4\ne0\). Types \(3+2+1\) and \(3+1+1+1\) have a unique triple node, whose nonzero \(c^2\) coefficient cannot cancel.
- Type \(2+2+2\) has a nonzero \(c\) coefficient proportional to \(\sum_j\prod_{\ell\ne j}(x_j-x_\ell)^{-2}>0\). Type \(2+1+1+1+1\) has only one double node, giving a nonzero \(c\) coefficient.

It remains to handle type \(2+2+1+1\). For a double node \(x_j\), put
\[
A_j=\prod_{\ell\ne j}(x_j-x_\ell)^{-m_\ell}.
\]
The constant terms of the residues sum to zero, since \(1/\prod_j(z-x_j)^{m_j}=O(z^{-6})\) at infinity. Hence \(D=-c\sum_{j:m_j=2}A_j\). Write the four distinct nodes as \(x_0<x_1<x_2<x_3\), with gaps \(p=x_1-x_0\), \(q=x_2-x_1\), and \(r=x_3-x_2\), all positive integers. If the doubled positions are any of \(\{0,1\},\{0,3\},\{1,2\},\{2,3\}\), the two \(A_j\) have the same sign and cannot cancel. If the double nodes occupy positions \(0,2\), their sum is
\[
A_0+A_2=\frac{1}{(p+q)^2}\left(\frac{1}{p(p+q+r)}-\frac{1}{qr}\right),
\]
which vanishes exactly when \(qr=p(p+q+r)\). If the double nodes occupy positions \(1,3\), then
\[
A_1+A_3=\frac{1}{(q+r)^2}\left(-\frac{1}{pq}+\frac{1}{r(p+q+r)}\right),
\]
which vanishes exactly when \(pq=r(p+q+r)\). These are precisely the two stated families, proving necessity and sufficiency.

For the first equation, rearrangement gives \(q(r-p)=p(p+r)\), so \(r>p\); with \(\delta=r-p\), it becomes \(q=p+2p^2/\delta\), which is integral exactly when \(\delta\mid2p^2\). The second equation is the reflected case and yields the stated parameterization. Finally, a common integer translation preserves the exponential values at all nodes, and reflection conjugates the divided difference, so the normalized descriptions do not change whether the transform vanishes.

## Verification

The proof uses the exact simplex/divided-difference identity, the confluent residue formula, and a complete partition of the integer-node multiplicities of six. The repeated-node case is reduced to two explicit rational equations in positive integer gaps. The parameterizations follow by rearrangement and divisibility, not by finite enumeration. No assertion is made about zeros away from integer frequencies.

## Relationship to prior work

The general Fourier-transform formulas for polytopes and simplices express the transform through contour integrals or divided differences and allow coincident projected vertices. They supply the representation used here, but the inspected results do not state the complete integer-frequency zero classification or the two gap equations for the repeated-node case. Work on discrete Fourier analysis and cubature on a simplex concerns a different transform/operator, while recent work on polytopal Fourier-zero varieties excludes certain complex spheres and curves rather than classifying isolated integer-lattice zeros.

## Limitations

The classification is specific to \(\Delta_5\), the displayed Fourier normalization, and \(k\in\mathbb Z^5\). It does not classify the zero set in \(\mathbb R^5\) or \(\mathbb C^5\), nor does it prove an analogous theorem in every dimension. The literature search was bounded; originality is supported by the statement-level comparisons recorded separately, not by a claim that all published work has been exhausted.

## References

1. “Fourier transforms of polytopes, solid angle sums, and discrete volume,” arXiv:1602.08593v1 (2016), general polytope Fourier-transform formulas.
2. “Lattice points in algebraic cross-polytopes and simplices,” arXiv:1608.02417v1 (2016), Theorem 3 and the simplex contour formula.
3. “Curves in the Fourier zeros of polytopal regions and the Pompeiu problem,” arXiv:2404.03405v1 (2024), results on complex zero-set varieties.
4. H. Li and Y. Xu, “Discrete Fourier analysis on fundamental domain of \(A_d\) lattice and on simplex in \(d\)-variables,” arXiv:0809.1079v1 (2008), a discrete Fourier/cubature result on a different object.
