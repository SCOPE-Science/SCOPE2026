# Dense arithmetic jumps in Fourier-zero density for weighted Sierpiński measures

## Finding

Fix three probabilities \(a,b,c>0\) with \(a+b+c=1\). Let \(\mu_{a,b,c}\) be the law of \(\sum_{j\ge1}2^{-j}D_j\), where the independent digits take the values \((0,0),(1,0),(0,1)\) with probabilities \(a,b,c\), respectively. Use \(\widehat\mu(\xi)=\int e^{-2\pi i\langle\xi,x\rangle}\,d\mu(x)\). Write \(N_{a,b,c}(R)\) for the number of **distinct real** Fourier zeros in the centered Euclidean disk of radius \(R\). Then
\[
N_{a,b,c}(R)=\pi d(a,b,c)R^2+O(R+1),
\]
where the error constant can be taken absolute, independently of the weights. The coefficient and local zero structure are as follows.

* If \(\max(a,b,c)>1/2\), there are no real zeros and \(d=0\).
* If \(\max(a,b,c)=1/2\), then \(d=1/3\), and all real zeros are isolated zeros of Taylor order one and local phase index zero.
* If \(\max(a,b,c)<1/2\), the mask \(m(s,t)=a+b e^{-2\pi i s}+c e^{-2\pi i t}\) has distinct torus roots \(\omega,-\omega\). Let \(h\) be the smallest \(j\ge1\) such that \(2^j\omega\equiv\omega\) or \(2^j\omega\equiv-\omega\pmod{\mathbb Z^2}\), or \(\infty\) if there is no such \(j\). Then \(d=\tfrac23(1-4^{-h})\), with \(4^{-\infty}=0\). Finite \(h\) is equivalent to odd additive order of \(\omega\) on the torus. The strictly triangular weights with finite \(h\) form a countable dense set, exactly the discontinuities of \(d\) within that region. At finite \(h\) the Taylor orders of Fourier zeros are unbounded. At \(h=\infty\) all zeros have invertible real Jacobian, and the phase indices \(+1\) and \(-1\) occur equally often in every centered disk.

Equal weights give \(h=1\) and density \(1/2\). The unequal weights associated to \(\omega=(1/5,3/5)\) give \(h=2\) and density \(5/8\).

## Assumptions and scope

The digit set, contraction factor and Euclidean frequency coordinates are fixed as above. We count points, not multiplicities. Taylor order is the least total degree of a nonzero Taylor term, and the phase index of an isolated zero is the winding number of the transform on a sufficiently small positively oriented circle around it. An order-one zero need not have an invertible real Jacobian.

## Proof

**1. Product and zero exhaustion.** Independence gives \(\widehat\mu(\xi)=\prod_{k\ge1}m(2^{-k}\xi)\). The tail factors differ from one by a summable sequence, locally uniformly even on compact sets of complex frequencies, since \(m(0)=1\). Eventually their logarithms may be taken in a neighborhood of one; the summed logarithms define a nonvanishing analytic tail locally. Thus precisely the zeros of individual finite-index factors contribute, and at any fixed zero the nonvanishing factors form a locally nonvanishing analytic multiplier.

**2. Mask geometry.** A mask zero is a closing triangle of vectors of lengths \(a,b,c\), one lying on the positive real axis. It exists exactly for \(\max(a,b,c)\le1/2\). In the strict case the two orientations give conjugate roots. The representative \(\omega=(u,v)\) is uniquely chosen with \(0<u<1/2<v<1\) and \(0<v-u<1/2\). Conversely each such pair gives the weights
\[
(a,b,c)=\frac{\bigl(\sin(2\pi(v-u)),\sin(2\pi(1-v)),\sin(2\pi u)\bigr)}
{\sin(2\pi(v-u))+\sin(2\pi(1-v))+\sin(2\pi u)}.
\]
The sines are positive, and this follows by solving the real and imaginary cancellation equations and normalizing. The inverse is continuous by the nondegenerate triangle geometry. The real mask Jacobian at \(\omega\) is \(-(2\pi)^2bc\sin(2\pi(v-u))<0\) and its sign at \(-\omega\) is opposite.

At the triangle boundary the single mask root is one of \((1/2,1/2),(1/2,0),(0,1/2)\). There is a nonzero linear imaginary term and a nonzero real quadratic term restricted to its kernel. For \(b=a+c\), at \((1/2,0)\) these are \(2\pi(b\delta_1-c\delta_2)\) and \(-2\pi^2ac\delta_2^2/b\) on the kernel; the case \(c=a+b\) swaps the coordinates. For \(a=b+c\), the linear term is \(2\pi(b\delta_1+c\delta_2)\) and the real quadratic term is \(2\pi^2(b\delta_1^2+c\delta_2^2)\). Use the imaginary part as one local coordinate. On its zero line the real part has a nondegenerate extremum; this proves isolation, and a small real regular value of opposite sign has no local preimages, giving local degree (phase index) zero. The nonzero linear term gives Taylor order one.

**3. Collisions across scales.** In the strict case let \(L_{k,\sigma}=2^k(\mathbb Z^2+\sigma\omega)\), \(k\ge1\), \(\sigma=\pm1\). For \(k<\ell\), these cosets at levels \(k,\ell\) intersect exactly when \(\sigma\omega\equiv 2^{\ell-k}\tau\omega\pmod{\mathbb Z^2}\), where \(\tau\) is the sign at level \(\ell\). In that event \(L_{\ell,\tau}\subset L_{k,\sigma}\). The two signs at the same level are disjoint. With no signed return all levels are disjoint. With first return at \(h\), the first \(h\) levels are disjoint and any level above \(h\) is contained in a coset at the level \(h\) steps earlier. Repetition reduces the union to the first \(h\) levels. A signed return annihilates \(\omega\) by the odd integer \(2^h\pm1\); conversely a power of two is one modulo any odd additive order. At the triangle boundary the single half-integer root is not an integer and doubles to zero modulo the lattice, so its cosets at different levels never meet.

**4. Counting and uniformity.** Each level-\(k\) coset has disk count \(\pi R^2 4^{-k}+O(R2^{-k}+1)\) with an absolute constant. Indeed the squares of side \(2^k\) centered at the lattice-coset points tile the plane, and only squares within distance \(2^k/\sqrt2\) of the disk boundary can contribute an area discrepancy. Moreover, all roots in the chosen oriented domain obey
\[
\operatorname{dist}(\omega,\mathbb Z^2)=\sqrt{u^2+(1-v)^2}
\ \ge\ \frac{u+1-v}{\sqrt{2}}>\frac1{2\sqrt2}.
\]
The opposite root has the same distance, and the boundary roots also satisfy this bound. Hence every coset at scale \(2^k>2\sqrt2 R\) misses the disk, uniformly in the weights. For \(R\ge1\), sum the disjoint coset estimates up to \(K=\lfloor\log_2(2\sqrt2 R)\rfloor\), keeping only the levels present in the disjoint representation from step 3. There are at most two cosets per level. The summed error is \(O(R+\log(R+2))\), and reinstating the omitted main terms costs at most \(2\pi R^2\sum_{k>K}4^{-k}=O(1)\). For \(0\le R<1\) only boundedly many scales and points occur, so the same absolute \(O(R+1)\) applies. Thus the coefficient is twice the sum of \(4^{-k}\) over the first \(h\) levels in the strict case, and once the sum over all levels on the boundary. With no roots the count is exactly zero.

**5. Continuity inside the strict region.** Odd-order rational torus points are countable and dense in the oriented domain. For fixed \(H\), the equations \((2^j\pm1)\omega\in\mathbb Z^2\) for \(1\le j\le H\) define a finite set of torus points. Consequently the deficits \(\tfrac23 4^{-h}\) of resonant triples tending to a nonresonant triple tend to zero. Every neighborhood of a resonant triple contains nonresonant ones with density \(2/3\), so continuity fails there.

**6. Orders and indices.** Each vanishing strict-triangle factor has order one, and its leading term is a nonzero complex polynomial in the real increments. Products of these polynomials do not vanish identically, so Taylor order equals the number of vanishing factors. With no signed return there is only one; multiplication by a nonzero analytic multiplier does not change its local index. Reflection \(\xi\mapsto-\xi\) exchanges the two signs and pairs the indices in each centered disk. If \(h<\infty\), at \(2^K\omega\) the levels \(K,K-h,\ldots\) down to the last positive one all vanish, which makes orders unbounded. At the boundary there is always just one vanishing factor, and the order and local degree established in step 2 carry over unchanged.

## Verification

The accompanying `checker.py` uses exact rational phase pairs and integer lattice membership for \(h=1,2,3\). At radius 140 the ten-scale unions coincide with the first-\(h\) disjoint-level representations; the counts are 30,790, 38,502 and 40,424. It counts vanishing factors at scale 24, tests three boundary masks and checks mask cancellation numerically for a nonresonant irrational phase pair. Run `python3 checker.py` for these finite checks. The arbitrary-weight counting error and phase results are proved above, not inferred from these checks.

## Relationship to prior work and limitations

Affine-IFS Fourier products are classical [1], and digit-mask dilation unions occur in the spectrality literature [2]. The present calculation concerns **distinct real zeros** for all positive three-weight choices in this dyadic family, including the signed-return density law and its exact discontinuity set. The equal-weight density and multiplicity phenomenon is a specialization, not an originality claim here. The result does not classify every phase index at a resonant multiple zero, give Fourier bases, or treat other digit sets or contractions.

## References

1. D. E. Dutkay and P. E. Jorgensen, *Fourier frequencies in affine iterated function systems*, [arXiv:math/0604547](https://arxiv.org/abs/math/0604547), §2.
2. J.-L. Chen and W.-H. Ai, *On the spectral properties of a class of planar Sierpinski self-affine measures*, [arXiv:2508.20809](https://arxiv.org/abs/2508.20809), §2, equation (2.2).
