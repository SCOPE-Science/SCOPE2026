# Sharp degree-four realization of the pentagonal nonnegative Fourier Gram obstruction

## Finding

Let \(\varphi=(1+\sqrt5)/2\), \(\eta=(\sqrt5-1)/2\), and \(\theta=2\pi/5\). Consider the class of real even trigonometric polynomials
\[
 f(t)=a_0+2\sum_{j=1}^{m}a_j\cos(jt),\qquad a_j\geq0,\quad f(t)\geq0\ \text{for every }t,\quad f(0)=1,\quad f(2\theta)=0.
\]
The conditions \(a_j\geq0\) mean that \(f\) is positive definite on the circle. With \(q=f(\theta)\), the following bounds are sharp:
\[
 \sup_{m\leq3}q=\eta^2=\frac{3-\sqrt5}{2},\qquad
 \sup_{m<\infty}q=\eta=\frac{\sqrt5-1}{2}.
\]
The first supremum has exactly one normalized optimizer, \(f_2(t)=((\cos t+\varphi/2)/(1+\varphi/2))^2\). The second is attained at Fourier degree four by
\[
 F(t)=\frac{5\varphi+8\cos t+2\cos(4t)}{5(\varphi+2)}.
\]
For the five equally spaced nodes \(t_j=j\theta\), the sampled matrix \(G_f=(f(t_j-t_k))_{0\leq j,k<5}\) of every admissible polynomial of degree at most three is completely positive as a real matrix, whereas \(G_F\) is doubly nonnegative but not completely positive. Thus degree four is the minimum degree that realizes the *exact five-cycle zero-chord obstruction* under simultaneous pointwise nonnegativity and Fourier positive definiteness.

The separation also persists with strictly positive polynomial values and a positive-definite (full-rank) sampled matrix at degree four. For every \(0<\delta<9-4\sqrt5\), the polynomial
\[
 K_\delta(t)=\frac{F(t)+\delta(1+\cos2t)}{1+2\delta}
\]
is strictly positive for all real \(t\), positive definite on the circle, and has a strictly positive definite, entrywise strictly positive five-point Gram matrix \(G_{K_\delta}\) that is not completely positive. In this perturbation the exact zero-chord requirement is intentionally released.

## Assumptions and scope

The group is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). A function is positive definite when every matrix of pairwise differences is Hermitian positive semidefinite. For a real even finite Fourier series this is equivalent to nonnegative complex Fourier coefficients \(a_j\). A real symmetric matrix is *completely positive* if it admits a finite decomposition \(\sum_\ell v_\ell v_\ell^T\) with all \(v_\ell\) entrywise nonnegative. *Doubly nonnegative* means real symmetric, positive semidefinite, and entrywise nonnegative. The sampled matrix has order five. The optimization over Fourier degrees at most three is nonempty (the degree-two optimizer belongs to it). No claim is made for arbitrary noneven or complex-valued kernels, other node configurations, or minimal Fourier degree for non-complete positivity without the zero-chord constraint.

## Proof

**1. Unrestricted sharp pentagonal bound.** Because the sampled nodes are a cyclic five-point subgroup, a normalized real even \(f\) with \(f(2\theta)=0\) has the circulant sample matrix
\[
 G_f=I+q A,
\]
where \(A\) is the adjacency matrix of the cycle \(C_5\) and \(q=f(\theta)\geq0\). Its Fourier eigenvalues are \(1+2q\cos(2\pi k/5)\), for \(0\leq k<5\). At \(k=2,3\), nonnegativity yields \(1-\varphi q\geq0\), hence \(q\leq1/\varphi=\eta\). No assumption on the Fourier degree was used.

**2. Sharp degree-at-most-three bound.** Write \(x=\cos t\) and \(c=\cos(2\theta)=-\varphi/2\). If \(f\) has trigonometric degree at most three, then \(f(t)=P(x)\) for a real polynomial \(P\) of degree at most three that is nonnegative on \([-1,1]\). The interior zero \(P(c)=0\) must have even multiplicity: \(P'(c)=0\). Thus
\[
 P(x)=(x-c)^2(A_0+Bx).
\]
Here \(A_0+Bx\geq0\) throughout \([-1,1]\), by continuity. The coefficient of \(\cos3t\) in \(P(\cos t)\) equals \(B/4\); positive definiteness forces \(B\geq0\). Since \(d=\cos\theta=(\sqrt5-1)/4<1\), one has \(A_0+Bd\leq A_0+B\). Therefore
\[
 q=\frac{P(d)}{P(1)}
 \leq\left(\frac{d-c}{1-c}\right)^2
 =\eta^2.
\]
Equality forces \(B=0\), because \(d<1\) and \(P(1)>0\), leaving uniquely the displayed \(f_2\). This polynomial is nonnegative and has nonnegative Fourier coefficients: using \(\cos^2t=(1+\cos2t)/2\), its constant, first-cosine, and second-cosine coefficients are respectively positive. This proves sharp attainment.

**3. Complete positivity below degree four.** Since \(\eta^2<1/2\), each degree-at-most-three sample matrix \(I+qA\) has the explicit nonnegative Gram decomposition
\[
 I+qA=(1-2q)I+q\sum_{j=0}^4(e_j+e_{j+1})(e_j+e_{j+1})^T,
\]
indices interpreted modulo five. All factors are nonnegative and \(q\geq0\). Thus its five-point Gram is completely positive.

**4. Degree-four sharp witness.** The Fourier coefficients of \(F\) are \(\widehat F(0)=\varphi/(\varphi+2)\), \(\widehat F(\pm1)=4/[5(\varphi+2)]\), and \(\widehat F(\pm4)=1/[5(\varphi+2)]\), with all others zero; hence \(F\) is positive definite. The exact cosine identity
\[
 5\varphi+8x+2(8x^4-8x^2+1)
 =16(x+\varphi/2)^2\left(x^2-\varphi x+\frac{1+3\sqrt5}{8}\right)
\]
shows \(F\geq0\): the quadratic factor has positive leading coefficient and discriminant \(1-\sqrt5<0\). Its only zeros on the circle are \(t\equiv\pm2\theta\pmod{2\pi}\). Direct exact evaluation gives \(F(0)=1\), \(F(\theta)=\eta\), \(F(2\theta)=0\). Thus \(G_F=I+\eta A\), saturating the universal eigenvalue bound. This rank-three, non-completely-positive pentagonal matrix is a classical example; its matrix-level non-complete positivity is not asserted as new.

For completeness, let \(J\) be the all-ones matrix and set \(H=J-2A\). For every entrywise nonnegative \(v\),
\[
 v^THv=\left(\sum_i v_i\right)^2-4\sum_{\{i,j\}\in E(C_5)}v_iv_j\geq0.
\]
The last inequality follows by the elementary triangle-free clique bound: while two nonadjacent coordinates are positive, transferring their fixed total mass wholly to whichever coordinate has the larger weighted neighbor sum does not decrease the edge-product sum; iteration ends on a clique of at most two vertices, whose edge product is at most a quarter of the squared mass. Thus \(H\) is copositive. Yet
\[
 \langle H,G_F\rangle=5-10\eta=5(2-\sqrt5)<0,
\]
which precludes any nonnegative rank-one Gram decomposition of \(G_F\).

**5. Strict interior witness without increasing degree.** The perturbation \(L(t)=1+\cos2t\) is nonnegative, and its Fourier coefficients are nonnegative. The zero sets of \(F\) and \(L\) are disjoint, so \(K_\delta>0\) pointwise when \(\delta>0\). Its nonnegative Fourier coefficients occur with strict positivity at frequencies \(0,\pm1,\pm2,\pm4\); these represent all residues modulo five, so its five-point Gram is strictly positive definite. All matrix entries are strictly positive because \(K_\delta>0\). An exact calculation using the above copositive \(H\) gives
\[
 \langle H,G_{K_\delta}\rangle
 =\frac{5[(2-\sqrt5)+\delta(2+\sqrt5)]}{1+2\delta}<0
 \quad\text{for }0<\delta<9-4\sqrt5.
\]
Thus even a strictly positive, finite-bandwidth positive-definite circle function can yield a strictly positive definite, entrywise positive, non-completely-positive five-point Gram. The claimed upper endpoint for \(\delta\) certifies the displayed Horn inequality; no claim about complete positivity beyond that endpoint is made.

## Verification

Running `python verify.py` with SymPy checks, using exact rational radicals, the quartic factorization, discriminant, sample values, extremal cubic ratio, Fourier coefficients, the two Horn trace identities, and the displayed perturbation interval. For the rational test \(\delta=1/100\), the checker also computes the five-point Gram eigenvalues and verifies their positivity and strict Horn separation. The universal upper bounds, factorization-based positivity on the entire circle, and copositivity of \(H\) are proved above and are not inferred from numerical sampling. The checker relies only on SymPy and Python 3.

## Relationship to prior work

The five-cycle matrix \(I+\eta A\), its doubly-nonnegative nature, and its failure to be completely positive were already explicitly described by Peyré (2026), with the five-dimensional DNN-versus-CP structure treated by Burer, Anstreicher, and Dür (2009). The Horn copositive certificate is also classical. Those facts are credited, not reasserted as original. Damase and Pascoe (arXiv:2602.09010v1, first public 2026-02-09, primary MSC2020 43A35) study partially specified positive-definite data and extension problems; their operator-algebra notion of completely positive maps is distinct from entrywise-completely-positive real Gram matrices. The contribution here is the **sharp Fourier-degree-three obstruction and degree-four nonnegative positive-definite interpolation at the specific two pentagonal chord values**, together with a degree-preserving strictly positive/full-rank separation. Literature searches and full-text examinations did not reveal that joint assertion, but do not constitute a proof of historical priority.

## Limitations

The sharp degree threshold requires the exact zero constraint at chord angle \(4\pi/5\); without it, non-completely-positive Gram matrices can occur at smaller Fourier degree. The perturbation interval is a sufficient range for the specified family and the specified Horn witness, not a necessary-and-sufficient characterization of complete positivity for every parameter. The result addresses exactly five equally spaced nodes and real even functions; it does not determine general sampling or nontranslation-invariant kernel problems. Historical literature may contain equivalent formulations not found in the inspected material. Independent scientific validation has not been performed.

## References

1. S. S. Damase and J. E. Pascoe, *Complete Discrete Schoenberg-Delsarte theory for homogeneous spaces*, arXiv:2602.09010v1 (public 2026-02-09), https://arxiv.org/html/2602.09010v1 .
2. G. Peyré, *Two notions of positivity, separated by a pentagon* (2026-07-04), https://www.gpeyre.com/blog/2026/07/04/doubly-nonnegative-completely-positive/ .
3. S. Burer, K. M. Anstreicher, and M. Dür, *The difference between 5 × 5 doubly nonnegative and completely positive matrices*, Linear Algebra Appl. **431** (2009), 1539–1552, https://doi.org/10.1016/j.laa.2009.05.021 .
4. J. S. Geronimo and H. J. Woerdeman, *Positive extensions, Fejér–Riesz factorization and autoregressive filters in two variables*, Ann. of Math. **160** (2004), 839–906, https://doi.org/10.4007/annals.2004.160.839 (background on positivity extension rather than the present univariate constraint).
