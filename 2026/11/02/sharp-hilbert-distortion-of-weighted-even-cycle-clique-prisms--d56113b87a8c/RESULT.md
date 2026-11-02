# Sharp Hilbert distortion of weighted even-cycle clique prisms

## Finding

For every integer \(m\ge2\), every integer \(r\ge2\), and every real \(0<\lambda\le1\), give the set \(X=\mathbb Z/(2m)\mathbb Z\times\{1,\ldots,r\}\) the metric
\[
 d_\lambda((i,a),(j,b))=\min\{|i-j|,2m-|i-j|\}+\lambda\mathbf1_{a\ne b}.
\]
This is the shortest-path metric of the Cartesian product of a unit-edge cycle with a complete graph whose edges have length \(\lambda\). Its least bilipschitz distortion into any real Hilbert space satisfies
\[
 \boxed{c_2(X)^2=\frac{(m+\lambda)^2\sin^2(\pi/(2m))}{1+\lambda^2\sin^2(\pi/(2m))}.}
\]
The optimizer is explicit in dimension \(r+1\). In particular the sharp constant is independent of \(r\), strictly increases with \(\lambda\in(0,1)\), and converges to \(\pi/2\) as \(m\to\infty\) at every fixed \(0<\lambda\le1\). The genuinely new asserted profile is at \(0<\lambda<1\); the unit-weight endpoint is included as a consistency boundary already covered in the unweighted-product literature [1].

## Assumptions and scope

For a finite metric space \((X,d)\), \(c_2(X)\) is the infimum, over injective maps \(f:X\to H\) into arbitrary real Hilbert spaces, of
\[
\left(\max_{x\ne y}\frac{\|f(x)-f(y)\|}{d(x,y)}\right)
\left(\max_{x\ne y}\frac{d(x,y)}{\|f(x)-f(y)\|}\right).
\]
Rescaling permits the equivalent optimization over noncontracting embeddings, with their greatest expansion minimized. All indices are cyclic modulo \(2m\). The integer \(r\) is the clique-fiber cardinality; it is not a real weight. Only real, positive \(\lambda\le1\) is asserted. No restrictions on Hilbert dimension or equivariance enter the lower bound.

## Proof

**1. A cycle antipodal energy inequality.** Put \(\theta=\pi/(2m)\), \(c=\sin^2\theta\), and \(K=1/c\). Any Hilbert-valued cyclic sequence \((a_i)_{i\in\mathbb Z/(2m)\mathbb Z}\) satisfies
\[
\frac1{2m}\sum_i\|a_i-a_{i+m}\|^2
\le K\frac1{2m}\sum_i\|a_i-a_{i+1}\|^2. \tag{1}
\]
Indeed, decompose the mean-zero sequence into Fourier modes. For frequency \(j\not\equiv0\pmod{2m}\), the quotient of antipodal squared difference to unit-step squared difference equals
\[
\frac{|1-(-1)^j|^2}{|1-e^{\pi i j/m}|^2}.
\]
It vanishes for even \(j\), and for odd \(j\) is \(\sin^{-2}(\pi j/(2m))\le \sin^{-2}\theta=K\). Parseval yields (1), also for arbitrary Hilbert targets because the finite Fourier transform acts on the finite-dimensional span of the sequence.

**2. Unrestricted lower bound from two fibers.** Let \(f\) be any noncontracting embedding with maximum expansion \(D\). Select two distinct fiber labels and set \(x_i=f(i,1)\), \(y_i=f(i,2)\), \(a_i=(x_i+y_i)/2\), \(b_i=(x_i-y_i)/2\). Convexity gives
\[
\frac1{2m}\sum_i\|a_{i+1}-a_i\|^2\le D^2,
\qquad 4\|b_i\|^2=\|x_i-y_i\|^2\le D^2\lambda^2.\tag{2}
\]
The \(2m\) cross-fiber antipodal pairs have original distance \(m+\lambda\). The identities
\[
x_i-y_{i+m}=(a_i-a_{i+m})+(b_i+b_{i+m})
\]
and the interchange \(i\mapsto i+m\) show that the average mixed inner product vanishes. By (1), (2), and \(\|u+v\|^2\le2(\|u\|^2+\|v\|^2)\),
\[
(m+\lambda)^2\le \frac1{2m}\sum_i\|x_i-y_{i+m}\|^2
\le KD^2+D^2\lambda^2.
\]
Therefore \(D^2\ge(m+\lambda)^2/(K+\lambda^2)\), precisely the displayed lower bound. This argument does not presuppose a symmetric embedding and works for all \(r\ge2\).

**3. Explicit sharp embedding.** Let \(D^2=(m+\lambda)^2/(K+\lambda^2)\), and let \(p_i\in\mathbb R^2\) be the vertices of a regular \(2m\)-gon with consecutive chord length \(D\). Let \(s_1,\ldots,s_r\in\mathbb R^{r-1}\) form a regular simplex of pairwise distance \(D\lambda\), and use mutually orthogonal subspaces. Define \(f(i,a)=p_i\oplus s_a\). If \(k\in\{0,\ldots,m\}\) is the circular separation of the indices and \(\varepsilon=\mathbf1_{a\ne b}\), then
\[
\|f(i,a)-f(j,b)\|^2=
D^2\left(\frac{\sin^2(k\theta)}{c}+\varepsilon\lambda^2\right),
\qquad d_\lambda=k+\varepsilon\lambda.\tag{3}
\]
The sine inequality \(\sin(k\theta)\le k\sin\theta\) implies \(\|f(x)-f(y)\|\le Dd_\lambda(x,y)\). For \(k=m,\varepsilon=1\), equality holds in the lower Lipschitz inequality: (3) equals \(D^2(K+\lambda^2)=(m+\lambda)^2\). It remains to verify that (3) is at least \((k+\varepsilon\lambda)^2\) for every other pair type.

**4. The noncontraction inequalities.** The concavity of sine on \([0,\pi/2]\) implies \(\sin(k\theta)\ge k/m\). Also
\[
2\le m^2c\le\pi^2/4,
\quad K\le m^2/2.\tag{4}
\]
For the first inequality use monotonicity of \(\sin z/z\) on \((0,\pi/4]\), with equality at \(m=2\); the second bound is \(\sin z\le z\). Since \(0<\lambda\le1\) and \(2m+1>\pi^2/4\),
\[
 (m+\lambda)^2-m^2(1+c\lambda^2)
 =2m\lambda+\lambda^2(1-m^2c)\ge0.\tag{5}
\]
Thus \(D^2\ge m^2c\), and (3) is noncontracting for all within-fiber pairs (\(\varepsilon=0\)). The cross-fiber same-index pairs satisfy it because \(D^2\ge m^2c\ge2>1\).

For cross-fiber pairs with \(k=1\), the desired inequality is equivalent to
\[
(m+\lambda)^2(1+\lambda^2)
\ge(1+\lambda)^2(K+\lambda^2).
\]
By (4) it is enough to replace \(K\) on the right by \(m^2/2\). Subtracting this larger right side gives
\[
\frac{m^2}{2}(1-\lambda)^2
+2\lambda\bigl(m(1+\lambda^2)-\lambda^2\bigr)\ge0. \tag{6}
\]

For \(2\le k\le m\) we use the elementary inequality
\[
\sin(k\theta)\ge\frac{k+1}{m+1}. \tag{7}
\]
For fixed \(m\), the function \((m+1)\sin(k\theta)-(k+1)\) is concave in real \(k\in[2,m]\), hence its minimum lies at an endpoint. It equals zero at \(k=m\). At \(k=2\) nonnegativity is \((m+1)\sin(\pi/m)\ge3\): at \(m=2\) there is equality; at \(m=3,4\) one uses the exact sine values; for \(m=5,6\), \(\sin(\pi/m)\ge1/2\); and for \(m\ge7\), \(\sin z\ge z-z^3/6\) yields
\[
(m+1)\sin(\pi/m)\ge\pi\left(1-\frac{\pi^2}{6m^2}\right)
\ge \pi\left(1-\frac{\pi^2}{294}\right)>3.
\]
This proves (7). Because \(0<\lambda\le1\),
\[
\frac{k+\lambda}{m+\lambda}\le\frac{k+1}{m+1}\le\sin(k\theta).
\]
Writing \(R=(k+\lambda)/(m+\lambda)\le1\), (7) implies
\[
\sin^2(k\theta)+c\lambda^2
\ge R^2(1+c\lambda^2).
\]
Multiplying by \((m+\lambda)^2/(1+c\lambda^2)\) establishes the noncontraction inequality in (3). This covers all pair types, and proves the exact formula.

**5. Consequences.** Differentiating \(D^2=c(m+\lambda)^2/(1+c\lambda^2)\) shows its derivative has the sign of \(1-mc\lambda\). For \(m=2\) one has \(mc=1\), whereas for \(m\ge3\), (4) gives \(mc\le\pi^2/(4m)<1\); hence the profile increases strictly on \((0,1)\). Its \(\lambda\downarrow0\) limit is \(m^2c\), and for fixed \(\lambda\) the \(m\to\infty\) distortion limit is \(\pi/2\). The regular simplex has dimension \(r-1\), hence the whole construction is realized in \(r+1\) real dimensions.

## Verification

The included `CHECK.py` evaluates (3) for all separations on cyclic orders \(2m\), \(2\le m\le80\), and six positive values of \(\lambda\le1\). It also independently solves finite conditional-negative-type linear programs for two fibers, for seven even cycle orders and six weights. The observed replay is `CHECK_OK finite_pair_inequalities= 39342 independent_Fourier_LP_cases= 42 maximum_absolute_LP_error= 2.07e-13`. This is finite numerical corroboration only: the all-parameter proof is in steps 1–5. Execute `python CHECK.py` with NumPy and SciPy installed.

## Relationship to prior work

Linial and Magen [1, Theorem 3.5] prove optimality of standard Euclidean embeddings of **unweighted** Cartesian products of cycles. Their theorem directly covers the \(\lambda=1\) endpoint when the fiber is two points, and the unweighted product principle is acknowledged, not claimed as new. The complete \(0<\lambda<1\) weighted profile, its exact denominator and monotonicity, and the cardinality-independent extension to all complete fibers are the contributions assessed here. Their stated theorem does not assign independent continuous edge lengths to a factor, so it cannot by direct substitution determine the weighted optimum. Cioabă–Gupta–Ihringer–Kurihara [2] study graph-metric Hilbert distortion for distance-regular graphs, not this weighted product; at nonunit weights the metric is not a standard unweighted distance-regular graph. Berleant and collaborators [3] treat weighted-graph *isometric Hamming embeddings*, which use a different target geometry and invariant. Nearby studies of Lipschitz-free Banach–Mazur distances for weighted cycles likewise do not imply point-metric distortion constants.

## Limitations

No result is asserted for \(\lambda>1\), odd cycle lengths, non-complete fiber graphs, general independently weighted factors, or minimum *necessary* embedding dimension. The unit-weight boundary is covered by previous product-embedding work; it is retained only to close the proven weighted interval. Priorities under other terminology, especially weighted Cartesian-product semidefinite methods, remain a residual literature risk. The checker is finite and numerical; the result has not received independent mathematical validation.

## References

[1] N. Linial and A. Magen, *Least-Distortion Euclidean Embeddings of Graphs: Products of Cycles and Expanders*, Journal of Combinatorial Theory B **79** (2000), 157–171; DOI 10.1006/jctb.2000.1953; author manuscript: https://www.cs.toronto.edu/~avner/papers/least-distortion.pdf. Theorem 3.5 and its proof inspected.

[2] S. M. Cioabă, H. Gupta, F. Ihringer, H. Kurihara, *The least Euclidean distortion constant of a distance-regular graph*, arXiv:2109.09708, initial version submitted 2021-09-20; https://arxiv.org/abs/2109.09708. Introduction and general distortion results inspected.

[3] J. Berleant, K. Sheridan, A. Condon, V. Vassilevska Williams, M. Bathe, *Isometric Hamming embeddings of weighted graphs*, Discrete Applied Mathematics (2023), DOI 10.1016/j.dam.2023.02.005.
