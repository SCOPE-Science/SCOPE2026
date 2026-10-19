# Dense arithmetic jumps in Fourier-zero density for weighted Sierpiński measures

## Finding

Fix three probabilities \(a,b,c>0\) with \(a+b+c=1\). Let \(\mu_{a,b,c}\) be the planar self-similar probability measure that is the law of \(\sum_{j=1}^{\infty}2^{-j}D_j\), where the independent digits \(D_j\) take the values \((0,0)\), \((1,0)\), and \((0,1)\) with probabilities \(a\), \(b\), and \(c\), respectively. Use \(\widehat\mu(\xi)=\int e^{-2\pi i\langle\xi,x\rangle}\,d\mu(x)\). Write \(N_{a,b,c}(R)\) for the number of *distinct real* Fourier zeros with Euclidean norm at most \(R\).

There is an exact coefficient \(d(a,b,c)\) such that
\[
N_{a,b,c}(R)=\pi d(a,b,c)R^2+O_{a,b,c}(R+1).
\]
If \(\max(a,b,c)>1/2\), then \(\widehat\mu\) has no real zeros and \(d=0\). If \(\max(a,b,c)=1/2\), then \(d=1/3\), and every real zero is an isolated order-one zero with local phase index zero.

Suppose \(\max(a,b,c)<1/2\). The torus zeros of the mask
\[
m(s,t)=a+b e^{-2\pi i s}+c e^{-2\pi i t}
\]
are precisely \(\{\omega,-\omega\}\pmod{\mathbb Z^2}\), with distinct points. Define the **first signed doubling return**
\[
h=\min\bigl\{j\ge1:(2^j-1)\omega\in\mathbb Z^2\ \text{or}\ (2^j+1)\omega\in\mathbb Z^2\bigr\},
\]
with \(h=\infty\) when the set is empty. Then
\[
\boxed{\quad d(a,b,c)=
\begin{cases}
\displaystyle \frac23(1-4^{-h}),&h<\infty,\\[3pt]
\displaystyle\frac23,&h=\infty.
\end{cases}\quad}
\]
Finite \(h\) occurs exactly when \(\omega\) is a torsion point of *odd* order in \(\mathbb R^2/\mathbb Z^2\). The corresponding weight triples form a **countable dense subset** of the strict triangle-inequality region. Inside that region, \(d\) is continuous at every nonresonant triple and discontinuous at every resonant triple; its generic value is \(2/3\).

For \(h=\infty\), all real Fourier zeros are simple (their two-real-variable Jacobian is invertible), and their local phase indices are \(+1\) and \(-1\) in exactly equal numbers in *every centered disk*. At every finite-\(h\) triple the orders of Fourier zeros are unbounded. The equal-weight case has \(h=1\), giving the previously known density \(1/2\); the unequal-weight example with mask root \(\omega=(1/5,3/5)\) has \(h=2\) and density \(5/8\).

## Assumptions and scope

All weights are strictly positive and normalized to sum to one. The contraction factor is exactly \(1/2\) and the digit set is exactly \(\{(0,0),(1,0),(0,1)\}\), with the stated Euclidean frequency coordinates. Zero counts are by *distinct points*, not by multiplicity, and centered disks are used. The implicit error constants may depend on the fixed weights and are not uniform near resonances or triangle-inequality boundaries. The phase index at an isolated zero is the winding number of the Fourier transform on a sufficiently small positively oriented circle.

## Proof

**1. Product formula and exhaustion of real zeros.** Independence gives
\[
\widehat\mu(\xi)=\prod_{k=1}^{\infty}m(2^{-k}\xi),\qquad \xi\in\mathbb R^2.
\]
For any fixed \(\xi\), the sum \(\sum_{k\ge1}|m(2^{-k}\xi)-1|\) is finite, since \(m(0)=1\) and \(m\) is Lipschitz. For sufficiently large \(k\), its factors are within \(1/2\) of one, so their infinite tail product is nonzero. Consequently \(\widehat\mu(\xi)=0\) if and only if at least one *finite-index* mask factor vanishes.

**2. The three-weight mask phase diagram.** A zero of \(m\) means that three vectors of lengths \(a,b,c\) sum to zero. Positivity makes this possible exactly when the three weights satisfy the triangle inequalities, equivalent here to \(\max(a,b,c)\le1/2\). For strict inequalities there are exactly two conjugate oriented triangles, hence two mask roots \(\pm\omega\) modulo \(\mathbb Z^2\). The representative \(\omega=(u,v)\) can be chosen uniquely in
\[
0<u<\frac12<v<1,\qquad 0<v-u<\frac12.
\]
Conversely, every such \((u,v)\) determines a strictly triangular weight triple through
\[
(a,b,c)=\frac{1}{S}
\bigl(\sin(2\pi(v-u)),\ \sin(2\pi(1-v)),\ \sin(2\pi u)\bigr),
\]
where \(S\) is the sum of the displayed positive sines. This follows from the sine rule, or directly from the real and imaginary parts of \(m(u,v)=0\). The map between the oriented root domain and the strict weight region is continuous in both directions by the nondegenerate triangle geometry.

At \(\omega\), the real Jacobian determinant of \(m\) is
\[
\det D_{\mathbb R}m(\omega)=-(2\pi)^2bc\sin(2\pi(v-u))<0;
\]
at \(-\omega\) it has the opposite sign. Thus both strict-triangle mask zeros are simple with phase indices \(-1\) and \(+1\). At a boundary weight, one coefficient equals the sum of the other two and the mask has just one root modulo the torus, one of \((1/2,1/2)\), \((1/2,0)\), or \((0,1/2)\). It has nonzero linear imaginary part, and the quadratic real part restricted to the line on which that imaginary linear part vanishes is nonzero with a fixed sign. For example, when \(b=a+c\), the root is \((1/2,0)\), the imaginary linear part is \(2\pi(b\delta_1-c\delta_2)\), and the real quadratic part on its kernel is \(-2\pi^2ac\delta_2^2/b\). This nondegenerate fold root is isolated, has Taylor order one, and its local winding is zero.

**3. Scaling-coset collisions.** In the strict case write
\[
L_{k,\sigma}=2^k(\mathbb Z^2+\sigma\omega),\qquad k\ge1,\quad\sigma\in\{-1,1\}.
\]
The product formula gives \(Z(\widehat\mu)=\bigcup_{k,\sigma}L_{k,\sigma}\). For \(k<\ell\), the intersection \(L_{k,\sigma}\cap L_{\ell,\tau}\) is nonempty if and only if
\[
\sigma\omega-2^{\ell-k}\tau\omega\in\mathbb Z^2.
\]
When this happens the *whole* finer coset \(L_{\ell,\tau}\) is contained in the coarser \(L_{k,\sigma}\). The two cosets at the same level are disjoint because \(2\omega\notin\mathbb Z^2\).

If \(h=\infty\), every displayed coset is disjoint from every other one. If \(h<\infty\), the \(2h\) cosets with \(1\le k\le h\) are pairwise disjoint, and each later coset is contained in one of those earlier cosets by repeatedly reducing its level by \(h\). Therefore
\[
Z(\widehat\mu)=\bigsqcup_{k=1}^{h}\bigl(L_{k,+}\sqcup L_{k,-}\bigr)
\]
when \(h\) is finite, with the identical expression interpreted as an infinite disjoint union when \(h=\infty\). A signed doubling return means that an odd integer \(2^h\pm1\) annihilates \(\omega\). Conversely, if \(\omega\) has odd additive order \(q\), some positive power of two equals one modulo \(q\). This proves the asserted equivalence.

**4. Counting.** A single level-\(k\) lattice coset has covolume \(4^k\), so the elementary disk lattice estimate is
\[
\#\bigl(L_{k,\sigma}\cap B_R\bigr)
=\pi R^2/4^k+O(R/2^k+1).
\]
For finite \(h\), summing over the disjoint first \(h\) levels gives \(d=2\sum_{k=1}^{h}4^{-k}=\frac23(1-4^{-h})\). When \(h=\infty\), the roots stay a positive distance from \(\mathbb Z^2\), so the level-\(k\) cosets are absent from \(B_R\) once \(2^k\) exceeds a constant times \(R\). Summing up to \(O(\log(R+2))\) levels gives main term \(2\sum_{k\ge1}4^{-k}=2/3\), error \(O(R+\log(R+2))=O(R+1)\). At the triangle boundary the single half-integer-root cosets at different levels are disjoint and have total density \(\sum_{k\ge1}4^{-k}=1/3\). Above the boundary no mask factor vanishes.

**5. Dense discontinuities.** Rational torus points of odd order are countable and dense in the open oriented-root domain. By the continuous root-to-weight correspondence, the finite-\(h\) weights are countable and dense in the strict weight region. For any fixed upper bound \(H\), there are only finitely many torus points obeying \((2^j\pm1)\omega\in\mathbb Z^2\) for some \(1\le j\le H\). Thus along resonant weights approaching any *nonresonant* weight, their first signed periods tend to infinity and their density deficits \((2/3)4^{-h}\) tend to zero. At each resonant weight, arbitrarily close nonresonant weights have density \(2/3\), while that weight has strictly smaller density. This proves the claimed continuity characterization.

**6. Orders and phase indices.** At strict-triangle zeros, each vanishing mask factor has a nonzero real Jacobian determinant, and all remaining factors form a nonvanishing analytic multiplier. Hence the real Taylor vanishing order is exactly the number of vanishing factors at the frequency. With no signed return this number is one. Multiplication by a nonzero complex scalar preserves the local orientation sign, so the local index equals that of the unique mask root. Central reflection exchanges the two sign classes, giving exact balance in every centered disk. If \(h<\infty\), the frequencies \(2^K\omega\) have at least \(1+\lfloor(K-1)/h\rfloor\) vanishing factors, namely levels \(K,K-h,K-2h,\ldots\) as long as positive; their orders are therefore unbounded. At the boundary, half-integer roots cannot collide across different scales, and the single-factor local degree remains zero.

## Verification

The standalone `checker.py` uses exact rational pairs and integer lattice membership for the signed periods \(h=1,2,3\). At radius \(140\), it compares a ten-scale union against the first-\(h\) disjoint-level representation and tests the lattice density formula: the observed coefficients are approximately \(0.500038847\), \(0.625284043\), and \(0.656497900\), versus exact \(1/2\), \(5/8\), and \(21/32\). It checks exact level-\(K\) multiplicity lower bounds at \(K=24\), including orders at least \(24,12,8\), and numerically checks mask cancellation for an explicitly nonresonant irrational phase pair. The checker also tests the three boundary cases. These are finite checks; none is used in place of the unrestricted arguments above.

## Relationship to prior work

The affine-IFS Fourier-product formalism and Fourier orthogonality questions are classical in the Dutkay–Jorgensen work. Chen–Ai explicitly uses the homogeneous equal-weight mask zero-locus and its dilation union when studying spectral measures. A preceding note, “Zero multiplicities and phase indices of the Sierpiński-gasket Fourier transform,” identified the equal-weight multiplicity and density law; the present theorem recovers its density \(1/2\) but does not claim that specialization as original. What is new in the present classification is the dependence on **arbitrary positive weights**, the odd-torsion signed-return criterion, the exact density at every weighting, and the countable dense set of density discontinuities. The comparison concerns exact statements rather than name matching; spectrality and Fourier-zero density are different invariants.

## Limitations

This result does not classify the phase index of every *multiple* zero at resonant weights, and does not establish Fourier bases or spectrality for the measures. It does not address other digit sets, non-dyadic contractions, or non-Euclidean counting norms. The error estimate holds at each fixed weight but is not uniform as weights approach a resonance or the triangle-inequality boundary. An older unindexed treatment of nonuniform three-digit Fourier masks could contain an equivalent density formula; independent publication-priority review remains desirable.

## References

1. D. E. Dutkay and P. E. T. Jorgensen, “Fourier frequencies in affine iterated function systems,” arXiv:math/0604547 (first public version 2006-04-25), especially §2 on affine IFS measures and Fourier factors, and §5 examples. https://arxiv.org/abs/math/0604547
2. J.-L. Chen and W.-H. Ai, “On the spectral properties of a class of planar Sierpinski self-affine measures,” arXiv:2508.20809 (2025), especially §1 and equation (2.2) for uniform-weight mask-zero dilation unions. https://arxiv.org/abs/2508.20809
3. “Zero multiplicities and phase indices of the Sierpiński-gasket Fourier transform,” preceding mathematical note, identifier `1fa80c63-fc59-47bc-8e4d-2f95472a0f98` (equal-weight specialization; distinct nonuniform claims are established here).
