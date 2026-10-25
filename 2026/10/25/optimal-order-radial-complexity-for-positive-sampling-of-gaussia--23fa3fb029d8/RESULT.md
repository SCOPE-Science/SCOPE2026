# Optimal-order radial complexity for positive sampling of Gaussian Fock polynomials

## Finding

Let \(\mathcal P_N\), for every integer \(N\ge1\), be the holomorphic polynomials of degree at most \(N\) in the Gaussian Fock norm
\[
\|P\|_{\mathcal F}^2=\frac1\pi\int_{\mathbb C}|P(z)|^2e^{-|z|^2}\,dA(z).
\]
A positive weighted point sampler is a finite family of points and strictly positive weights, with sampled energy
\[
\mathcal S_N(P)=\sum_{\nu}w_\nu e^{-|z_\nu|^2}|P(z_\nu)|^2.
\]
Suppose \(0<A\le B<\infty\), independent of \(N\), satisfy
\[
 A\|P\|_{\mathcal F}^2\le\mathcal S_N(P)\le B\|P\|_{\mathcal F}^2
 \qquad(P\in\mathcal P_N).
\]
**Radial necessity:** if the sampling locations use \(r_N\) distinct moduli, regardless of the number or disposition of angular sites, then
\[
 \boxed{r_N\ge\frac{A}{3eB}\sqrt{N+1}.}
\]
**Radial sufficiency with explicit uniform bounds:** put \(J=\lceil\sqrt N\rceil\), \(M=N+1\), and \(\zeta=\exp(2\pi i/M)\). The positive sampler
\[
 \mathcal Q_N(P)=|P(0)|^2+
 \sum_{j=1}^{J}\frac{(2j+1)e^{-j^2}}{M}
 \sum_{s=0}^{M-1}|P(j\zeta^s)|^2
\]
satisfies, for **every** \(P\in\mathcal P_N\),
\[
 \boxed{\frac15\|P\|_{\mathcal F}^2\le
 \mathcal Q_N(P)\le8\|P\|_{\mathcal F}^2.}
\]
The displayed sampler has exactly \(\lceil\sqrt N\rceil+1\) distinct radii and at most \(1+(N+1)\lceil\sqrt N\rceil\) distinct sites. Thus the sharp *order* of the minimum number of radii, with fixed positive uniform frame bounds, is \(\Theta(\sqrt N)\). The numerical constants \(1/5,8\), and \(1/(3e)\) are explicit valid bounds and are **not** claimed to be numerically optimal.

## Assumptions and scope

All point weights are positive and independent of the test polynomial. The comparison constants \(A,B\) may be chosen arbitrarily but must be fixed across degrees when interpreting radial order. The arbitrary sampler need not have rotational symmetry or equally spaced angular sites. The constructive sampler uses equal angular increments at each nonzero radius and individual weights as displayed. Counting distinct radii includes radius zero. No bound on the total number of sites is claimed to be order-optimal.

## Proof

**1. Monomial reduction.** The normalized monomials \(e_k(z)=z^k/\sqrt{k!}\), \(0\le k\le N\), form an orthonormal basis. Write
\[
 p_t(k)=e^{-t}\frac{t^k}{k!}\quad(t>0),\qquad
 p_0(0)=1,\quad p_0(k)=0\ (k\ge1).
\]
Grouping an arbitrary sampler by its distinct squared radii \(t_1,\ldots,t_r\) and summing weights at each radius to \(b_j>0\), testing the frame inequality on each \(e_k\) gives
\[
 A\le L_k:=\sum_{j=1}^r b_jp_{t_j}(k)\le B
 \qquad (0\le k\le N).
\]
These inequalities do not depend on any angular assumptions.

**2. Uniform truncated Poisson width.** For every \(N\ge1\), \(t\ge0\),
\[
 \sum_{k=0}^Np_t(k)\le3e\sqrt{N+1}\max_{0\le k\le N}p_t(k).
\]
For \(0\le t\le N\), the full Poisson mass is one. If \(t<1\), its maximum over the truncated range is at least \(p_t(0)\ge e^{-1}\). Otherwise put \(m=\lfloor t\rfloor\), so \(1\le m\le N\). Using \(m!\le3\sqrt m(m/e)^m\), \(t\in[m,m+1)\), and \(t^m\ge m^m\),
\[
 p_t(m)=e^{-t}t^m/m!\ge (3e\sqrt m)^{-1}
 \ge(3e\sqrt{N+1})^{-1}.
\]
If \(t>N\), then \(p_t(k)\) is increasing on \(0\le k\le N\). For \(1\le h\le N\),
\[
 \frac{p_t(N-h)}{p_t(N)}
 =\prod_{j=0}^{h-1}\frac{N-j}{t}
 \le \exp\bigl(-h(h-1)/(2N)\bigr).
\]
Hence the truncated mass divided by its maximum is at most
\[
 2+\sum_{u=1}^{\infty}e^{-u^2/(2N)}
 \le2+\sqrt{\pi N/2}\le3e\sqrt{N+1}.
\]
For \(t=0\) the inequality is immediate.

**3. Necessary number of radii.** For each \(j\), the positive sequence \(b_jp_{t_j}(k)\) has every term at most \(B\), so the width estimate bounds its total truncated mass by \(3eB\sqrt{N+1}\). Summing the inequalities \(L_k\ge A\) over \(0\le k\le N\) proves
\[
 A(N+1)\le3eBr\sqrt{N+1},
\]
which gives the claimed lower bound.

**4. Explicit angular diagonalization.** With \(M=N+1\), the discrete root-of-unity identity
\[
 M^{-1}\sum_{s=0}^{M-1}\zeta^{s(k-h)}=\mathbf1_{k=h}
\]
holds for \(0\le k,h\le N\). Consequently
\[
 \mathcal Q_N(P)=\sum_{k=0}^N \lambda_{N,k}|c_k|^2,
 \quad P=\sum_{k=0}^Nc_ke_k,
 \quad \lambda_{N,k}=\sum_{j=0}^J(2j+1)p_{j^2}(k).
\]
It remains to bound the scalar eigenvalues uniformly.

**5. Lower eigenvalue bound.** For \(k=0\), \(\lambda_{N,0}\ge1\). For \(1\le k\le N\), write \(a=\sqrt{k}\) and choose an integer \(1\le j\le J\) nearest to \(a\), so \(|j-a|\le1/2\) and \(2j+1\ge2a\). The Poisson rate function at \(t=j^2\) is
\[
 I(j,k)=j^2-k-k\log(j^2/k)
 =k\bigl((j/a)^2-1-2\log(j/a)\bigr).
\]
Because \(j/a\ge1/2\), the function \(r^2-1-2\log r\) has second derivative at most \(10\) along the segment from \(1\) to \(j/a\), and its value and first derivative at \(1\) vanish. Therefore
\[
 0\le I(j,k)\le5(j-a)^2\le5/4.
\]
The standard explicit Stirling bound \(k!\le\sqrt{2\pi k}(k/e)^k e^{1/(12k)}\) implies
\[
 \lambda_{N,k}\ge(2j+1)p_{j^2}(k)
 \ge \frac{2e^{-4/3}}{\sqrt{2\pi}}>\frac15.
\]

**6. Upper eigenvalue bound.** For \(k=0\),
\[
 \lambda_{N,0}\le1+\sum_{j=1}^{\infty}(2j+1)e^{-j}
 =1+\frac{2e^{-1}}{(1-e^{-1})^2}
 +\frac{e^{-1}}{1-e^{-1}}<8.
\]
For \(k\ge1\), set \(a=\sqrt{k}\). The Stirling lower bound and \(r-1-\log r\ge0\) imply
\[
 p_{j^2}(k)\le\frac{1}{\sqrt{2\pi k}}
 \exp(-(j-a)^2)\qquad(j\ge1).
\]
For any real \(x\) in \([j-a-1/2,j-a+1/2]\),
\[
 e^{-(j-a)^2}\le e^{1/4}e^{-x^2/2},
 \qquad2j+1\le2a+2|x|+2.
\]
Integrating over disjoint unit intervals for \(j\ge0\) (which only enlarges the positive upper sum) gives
\[
 \lambda_{N,k}
 \le\frac{e^{1/4}}{\sqrt{2\pi}a}
 \int_{\mathbb R}(2a+2|x|+2)e^{-x^2/2}\,dx
 \le e^{1/4}\left(4+\frac4{\sqrt{2\pi}}\right)<8.
\]
Thus all eigenvalues lie in \([1/5,8]\), completing the proof.

## Verification

Run `python3 checker.py` with Python 3 standard library. The checker independently computes Poisson diagonal values through log-factorials for multiple polynomial degrees, compares direct complex-grid sample sums against diagonalization for random polynomials, and checks the Poisson-width inequality on a numerical grid. The recorded run returned **6,369 finite assertions passed**. These finite tests do not prove the all-degree statement or optimality of radial order; those rely on the analytical inequalities above.

## Relationship to prior work

Gröchenig's general Marcinkiewicz–Zygmund framework explains why uniformly stable polynomial sampling yields approximation and quadrature. Gröchenig–Ortega-Cerdà establish the Fock-polynomial setting and its connection to entire-space sampling and Hermite/Gabor frames. Speckbacher proves that unions of equally spaced concentric **continuous** circles are sampling trajectories for the short-time Fourier transform. These results motivate the circle geometry and establish important broader sampling constructions, but the inspected statements do not give the present quantitative lower bound for the number of distinct radii of *arbitrary finite positively weighted point samplers*, nor the finite root-of-unity construction with explicit degree-independent bounds.

Continuous-circle sampling and stable finite-dimensional sampling are mathematically related; the upper construction is not claimed to be the first demonstration that concentric circles can be sampling sets. The claimed addition is the matched radial-cardinality obstruction and explicit finite scheme in the stated positive-weight model.

## Limitations

The sharpness refers to growth order \(\Theta(\sqrt N)\), not the optimal leading coefficient or best frame bounds. Positive sampling weights are essential to the lower-bound proof; signed formulas are outside scope. The construction uses \(\Theta(N^{3/2})\) evaluation sites and makes no assertion of optimal total sample complexity. The cited literature and publicly searchable records cannot exclude every equivalent result in older, unindexed radial quadrature theory. Independent scholarly originality review has not been performed.

## References

1. K. Gröchenig, *Sampling, Marcinkiewicz–Zygmund Inequalities, Approximation, and Quadrature Rules*, arXiv:1909.07752 (first posted 17 September 2019), https://arxiv.org/abs/1909.07752.
2. M. Speckbacher, *Sampling trajectories for the short-time Fourier transform*, arXiv:2106.01018 (first posted 2 June 2021), https://arxiv.org/abs/2106.01018.
3. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund Inequalities for Polynomials in Fock Space*, arXiv:2109.11825 (first posted 24 September 2021), https://arxiv.org/html/2109.11825v1.
4. NIST Digital Library of Mathematical Functions, §5.11 (Stirling estimates), https://dlmf.nist.gov/5.11.
