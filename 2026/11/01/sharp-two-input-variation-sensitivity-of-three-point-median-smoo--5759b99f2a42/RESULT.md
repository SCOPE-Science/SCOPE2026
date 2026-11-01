# Sharp two-input variation sensitivity of three-point median smoothing on finite paths

## Finding

For every integer \(n\ge 2\), define the endpoint-preserving three-point running median \(T:\mathbb R^n\to\mathbb R^n\) by
\[
(Tf)_1=f_1,\qquad (Tf)_i=\operatorname{median}(f_{i-1},f_i,f_{i+1})\ (2\le i\le n-1),\qquad (Tf)_n=f_n.
\]
For independently chosen positive edge weights \(w_1,\ldots,w_{n-1}\), write
\[
V_w(h)=\sum_{i=1}^{n-1}w_i|h_{i+1}-h_i|,\qquad
L_n(w)=\sup_{V_w(f-g)>0}\frac{V_w(Tf-Tg)}{V_w(f-g)}.
\]
For \(n=2\), the sharp coefficient is \(L_2(w)=1\). For every \(n\ge 3\), letting \(m=n-1\), the exact **attained** coefficient is
\[
\boxed{L_n(w)=\max\!\left\{1,\frac{w_2}{w_1},\frac{w_{m-1}}{w_m},\max_{2\le k\le m-1}\frac{w_{k-1}+w_k+w_{k+1}}{w_k}\right\}.}
\]
The last maximum is omitted when its index set is empty. Moreover,
\[
\boxed{\inf_{w_i>0} L_n(w)=1+2\cos\!\left(\frac{\pi}{n-1}\right),\quad n\ge 3.}
\]
The infimum is a minimum, uniquely attained up to positive common scale by
\[
w_i=\sin\!\left(\frac{(i-\tfrac12)\pi}{n-1}\right),\quad 1\le i\le n-1.
\]
In particular, if \(n\ge4\), no strictly positive edge weighting makes the running median nonexpansive as a two-input map in weighted total variation. With unit weights the sharp modulus is \(3\) for \(n\ge4\), whereas optimal weights reduce it to \(2\) at \(n=4\) and to an increasing sequence tending to \(3\) as \(n\to\infty\).

## Assumptions and scope

Signals are real-valued vectors on the ordered path of \(n\) vertices, the center median uses the triple containing the vertex, the two endpoint values are left unchanged, and all edge weights are strictly positive. The seminorm \(V_w\) annihilates constants. The operator is translation-equivariant, so the two-input quotient is well-defined on the quotient modulo constants. All upper bounds hold for every pair of real-valued input vectors, including tied values. Sharpness is achieved by pairs in a strict-order chamber; no generic-position assumption appears in the theorem.

## Proof

**1. Piecewise-linear selector representation.** Partition \(\mathbb R^n\) into the finitely many polyhedral chambers determined by coordinate order. In any chamber with strictly ordered coordinates, the output at each interior site is precisely one input coordinate. Thus \(T\) equals a linear selector \(S\) on that chamber; it has exactly one \(1\) in each row and zero otherwise, and its endpoint rows select their own coordinates. In particular \(S\mathbf1=\mathbf1\). Continuity of the median extends the local description across chamber boundaries.

**2. Difference-column norm.** For \(k=1,\ldots,m\), let \(H_k\in\mathbb R^n\) be the step with \((H_k)_i=0\) for \(i\le k\) and \((H_k)_i=1\) for \(i>k\). Every vector decomposes exactly as
\[
h=h_1\mathbf1+\sum_{k=1}^{m}(h_{k+1}-h_k)H_k.
\]
Since \(S\mathbf1=\mathbf1\), homogeneity and the triangle inequality give
\[
V_w(Sh)\le\sum_{k=1}^{m}|h_{k+1}-h_k|V_w(SH_k)
\le\left(\max_k\frac{V_w(SH_k)}{w_k}\right)V_w(h).
\]
Equality in the induced seminorm is attained by one of the columns \(H_k\). Thus the selector norm is **exactly** the largest step-column ratio.

**3. Sharp column bounds.** An interior median at site \(i\) selects only a coordinate in \(\{i-1,i,i+1\}\). For a step \(H_k\), every selected value is zero at output sites \(i\le k-1\) and one at sites \(i\ge k+2\). Consequently, for \(2\le k\le m-1\) all nonzero output differences lie among the three edges \(k-1,k,k+1\), and
\[
V_w(SH_k)\le w_{k-1}+w_k+w_{k+1}.
\]
For \(k=1\), the endpoint remains zero, the last \(n-2\) outputs are one starting at site \(3\), and the only free output is site \(2\). Hence \(V_w(SH_1)\le\max\{w_1,w_2\}\); the right endpoint gives \(V_w(SH_m)\le\max\{w_{m-1},w_m\}\). These together prove the displayed global upper bound on the norm of every local selector.

The interior three-edge bound is achievable at any \(2\le k\le m-1\): choose a strict global ordering consistent with the local assignments
\[
f_{k-1}=0,\qquad f_{k+1}=1,\qquad f_k=2,\qquad f_{k+2}=3.
\]
Then at output site \(k\) the median selects the right input \(k+1\), while at site \(k+1\) it selects the left input \(k\). Therefore the step-column outputs near the cut alternate \(0,1,0,1\), attaining the three-edge sum. All other coordinates can be chosen distinctly without affecting these selections. At the left boundary, the ordering \(f_2<f_1<f_3\) attains column ratio \(w_2/w_1\); reversing the corresponding relations attains the mirror ratio \(w_{m-1}/w_m\). The identity selector on a globally increasing signal gives ratio \(1\). Thus every listed term is achievable by a strict-order chamber.

For an actual **pair of inputs**, choose such a strict-order base vector \(f\), let \(g=f+\varepsilon H_k\) with sufficiently small \(\varepsilon>0\), and note that the entire segment between them remains in the same chamber. Then \(Tg-Tf=\varepsilon SH_k\), and the chosen column ratio is attained exactly, not merely as a formal derivative. For example, at \(n=4\) and unit weights, take \(f=(0,2,1,3)\) and \(g=(0,2,1+\varepsilon,3+\varepsilon)\) with \(0<\varepsilon<1\); the input variation difference equals \(\varepsilon\), while the output variation difference equals \(3\varepsilon\).

**4. From local to global pairs.** For any \(f,g\), the segment \(f+t(g-f)\), \(0\le t\le1\), crosses only finitely many order-chamber boundaries, unless it lies in a boundary face, in which case it can be approximated by generic segments. On each chamber piece \(T\) is one of the selectors above and therefore obeys the same variation seminorm bound. The triangle inequality along the partition yields \(V_w(Tg-Tf)\le L_n(w)V_w(g-f)\). Continuity extends this to all degenerate segments, proving the exact global two-input modulus.

**5. Optimal variation weights.** For \(m=n-1\ge2\), define the irreducible nonnegative symmetric tridiagonal matrix \(A_m\) by
\[
(A_m)_{i,i+1}=(A_m)_{i+1,i}=1,\quad (A_m)_{i,i}=1\ (2\le i\le m-1),\quad (A_m)_{1,1}=(A_m)_{m,m}=0,
\]
all other entries zero. The formula from step 3 is exactly
\[
L_n(w)=\max_i\frac{(A_mw)_i}{w_i}.
\]
The positive vector \(v_i=\sin((i-\tfrac12)\theta)\), with \(\theta=\pi/m\), obeys \(A_mv=\lambda v\) for \(\lambda=1+2\cos\theta\). Interior equations follow from sine addition; the first boundary is \(v_2=\lambda v_1\) by \(\sin(3\theta/2)/\sin(\theta/2)=1+2\cos\theta\), and the last is its reflected counterpart. The same computation works for \(m=2\), giving \(\lambda=1\). Perron–Frobenius makes this the simple spectral-radius eigenvalue and \(v\) its unique positive eigenvector up to scale. The Collatz–Wielandt min-max formula yields
\[
\min_{w>0}\max_i\frac{(A_mw)_i}{w_i}=\rho(A_m)=1+2\cos\frac{\pi}{m}.
\]
This establishes both the sharp optimized modulus and uniqueness of the optimizing weights. The case \(n=2\) is the identity map and was treated separately.

## Verification

The included standalone file `verify_median_bv.py` enumerates every strict coordinate-order chamber for \(2\le n\le7\). For three independent positive rational weight vectors per size, it calculates each exact step-column ratio, verifies the upper bound, and confirms an attained matching column. The package checker also verifies the explicit four-site witness and the Perron sine eigenrelation for \(3\le n\le30\). This is finite corroboration; the infinite-family statements depend on the complete proof above.

## Relationship to prior work

Restrepo and Chacon (1994) establish that classical median filtering does not increase the **one-input** total variation \(V(Tf)\) relative to \(V(f)\); that is different from the two-input Lipschitz variation \(V(Tf-Tg)\) treated here. Maragos and Schafer (1987) analyze median filters as order-statistic and morphological filters and provide a minimum/maximum structural viewpoint, without the present weighted two-input norm classification in the inspected material. Suomela (2014) establishes an algorithmic equivalence between sliding median filtering and sorting, rather than a variation perturbation bound. No assertion of exhaustive novelty is made; older nonlinear filter-stability literature may conceal an equivalent special case.

## Limitations

This is not a one-input variation-amplification theorem: the two-input difference of outputs need not be the median of the input difference. All paths are finite and carry endpoint-preserving three-sample medians, with positive edge-variation weights. Other endpoint conventions, longer or weighted median windows, graphs with branches or cycles, and vector-valued filters are not classified. The prior-work comparison is limited by the inaccessible full text of the short 1994 paper; the publicly accessible abstract clearly describes one-input smoothing, but an implicit two-input statement cannot be completely excluded.

## References

1. A. Restrepo and L. Chacon, *A smoothing property of the median filter*, IEEE Transactions on Signal Processing 42(6), 1553–1555 (1994), DOI: 10.1109/78.286974. Accessible abstract: https://eurekamag.com/research/097/760/097760929.php.
2. P. Maragos and R. W. Schafer, *Morphological Filters—Part 2: Their Relations to Median, Order-Statistic, and Stack Filters*, University of Maryland technical report (1987), https://drum.lib.umd.edu/bitstreams/154a294b-2b9b-4c93-871a-8c68ed6834ff/download.
3. J. Suomela, *Median Filtering is Equivalent to Sorting*, arXiv:1406.1717v1, publicly submitted 2014-06-06, https://arxiv.org/abs/1406.1717.
