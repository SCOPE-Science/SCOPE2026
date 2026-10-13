# A unique covariance sign transition for gaps and coverage in random circular arcs

## Finding

**Theorem (sharp finite-sample sign transition).** Independently place \(n\ge2\) uniform points on a circle of circumference one and attach to each a clockwise arc of the same fixed length \(s\in(0,1)\). Let \(K_n(s)\) count uncovered connected gaps (zero if the circle is fully covered), and let \(C_n(s)\) be the covered fraction. Then
\[
\operatorname{Cov}(K_n(s),C_n(s))
 =n(1-s)^{2n-1}-(1-s)^n-(n-1)(1-2s)_+^n,
\]
where \(x_+=\max\{x,0\}\). For \(n=2\) this covariance is strictly positive for \(0<s<1/2\), zero at \(s=1/2\), and strictly negative for \(1/2<s<1\). For every \(n\ge3\), there is exactly one \(s_n\in(0,1/2)\) at which the covariance vanishes; it is strictly positive for \(0<s<s_n\) and strictly negative for \(s_n<s<1\). Thus the transition is unique at every nondegenerate sample size.

The first nontrivial zero is \(s_3\approx0.403330466413861\). Moreover, for fixed \(c>0\), as \(n\to\infty\),
\[
\operatorname{Cov}(K_n(c/n),C_n(c/n))
\longrightarrow e^{-2c}\bigl(1+c+c^2-e^c\bigr).
\]
Consequently \(ns_n\to c_*\approx1.793282132900761\), where \(c_*\) is the unique positive solution of \(e^{c_*}=1+c_*+c_*^2\). This is a sign transition of dependence, not a threshold for complete circle coverage.

## Assumptions and scope

The center points are independent and uniform on the continuous unit circle; arcs are oriented clockwise with equal deterministic lengths. Points coincide with probability zero. Index the cyclic spacings in clockwise order by \(D_1,\ldots,D_n\). Their joint law is \(\operatorname{Dirichlet}(1,\ldots,1)\), so \(\sum_iD_i=1\) and
\[
 K_n(s)=\sum_{i=1}^n\mathbf 1\{D_i>s\},\qquad
 C_n(s)=\sum_{i=1}^n\min\{D_i,s\}
 =1-\sum_{i=1}^n(D_i-s)_+.
\]
The quantity \(K_n(s)\) counts uncovered components, not arbitrary connected components of the covered set when there is complete coverage. It is deterministic at the excluded endpoints \(s=0\) and \(s=1\), where covariance is zero. For \(n=1\) both statistics are deterministic; the substantive theorem starts at \(n=2\).

## Proof

**Exact mixed moments.** For each spacing, the uniform-simplex marginal tail is
\[
\mathbb P(D_i>u)=(1-u)^{n-1},\qquad 0\le u\le1.
\]
For distinct spacings, their simultaneous tail is
\[
\mathbb P(D_i>u,D_j>v)=(1-u-v)_+^{n-1}.
\]
The formulas remain valid for \(n=2\), where the two spacings sum to one. Using layer-cake integration, for every \(s\in(0,1)\),
\[
\begin{aligned}
\mathbb E\mathbf 1\{D_i>s\}&=(1-s)^{n-1},\\
\mathbb E(D_i-s)_+&=\frac{(1-s)^n}{n},\\
\mathbb E[\mathbf 1\{D_i>s\}(D_i-s)_+]&=\frac{(1-s)^n}{n},\\
\mathbb E[\mathbf 1\{D_i>s\}(D_j-s)_+]&=\frac{(1-2s)_+^n}{n}\quad (i\ne j).
\end{aligned}
\]
For instance, the last equality integrates \(\mathbb P(D_i>s,D_j>t)\) over \(t\in[s,1]\). Summing diagonal and off-diagonal contributions gives
\[
\begin{aligned}
\mathbb E K_n(s)&=n(1-s)^{n-1},\\
\mathbb E C_n(s)&=1-(1-s)^n,\\
\mathbb E[K_n(s)C_n(s)]
 &=n(1-s)^{n-1}-(1-s)^n-(n-1)(1-2s)_+^n.
\end{aligned}
\]
Subtracting the product of means gives the claimed exact covariance.

**Unique transition.** For \(0<s<1/2\), factor the covariance as \((1-s)^nB_n(s)\), where
\[
 B_n(s)=n(1-s)^{n-1}-1
 -(n-1)\left(\frac{1-2s}{1-s}\right)^n.
\]
Differentiation gives
\[
 B_n'(s)=n(n-1)(1-s)^{n-2}\bigl(R_n(s)-1\bigr),
 \qquad R_n(s)=\frac{(1-2s)^{n-1}}{(1-s)^{2n-1}},
\]
and
\[
 \frac{d}{ds}\log R_n(s)
 =\frac{1-2ns}{(1-2s)(1-s)}.
\]
Thus \(R_n\) increases strictly from one on \((0,1/(2n))\), subsequently decreases strictly to zero, and crosses one exactly once in \((1/(2n),1/2)\). It follows that \(B_n\) increases and then decreases, with a unique maximum. Also \(B_n(0)=0\), \(B_n''(0)=n(n-1)>0\), and
\[
 B_n(1/2)=\frac{n}{2^{n-1}}-1.
\]
For \(n\ge3\) the last quantity is strictly negative, proving a unique root \(s_n\in(0,1/2)\), with the specified signs before and after that root up to \(s=1/2\). For \(s\ge1/2\), the covariance simplifies to \((1-s)^n[n(1-s)^{n-1}-1]\), which is strictly negative for \(n\ge3\). For \(n=2\), direct expansion gives \(s^2(1-2s)\) for \(0<s\le1/2\) and \((1-s)^2(1-2s)\) for \(1/2\le s<1\), yielding the remaining case.

**Sparse scaling.** Let \(s=c/n\) for a fixed positive \(c\) and sufficiently large \(n\). Expanding the three terms in the exact covariance uniformly for bounded \(c\),
\[
\begin{aligned}
 n(1-c/n)^{2n-1}&=ne^{-2c}+e^{-2c}(c-c^2)+O(n^{-1}),\\
 (n-1)(1-2c/n)^n&=ne^{-2c}-e^{-2c}(1+2c^2)+O(n^{-1}),\\
 (1-c/n)^n&=e^{-c}+O(n^{-1}),
\end{aligned}
\]
which gives the displayed limiting covariance. Write \(f(c)=e^c-1-c-c^2\). We have \(f(0)=f'(0)=0\), \(f''(0)=-1\), and \(f^{(3)}(c)=e^c>0\). Hence \(f''\) crosses zero once, \(f'\) crosses zero once at a positive point, and \(f\) crosses zero at exactly one positive point \(c_*\). The limiting covariance is positive below \(c_*\) and negative above it. For fixed \(c_1<c_*<c_2\), the exact covariances at arc lengths \(c_1/n\) and \(c_2/n\) have the corresponding signs for all sufficiently large \(n\). Since the finite transition is unique, \(c_1<ns_n<c_2\), proving \(ns_n\to c_*\).

## Verification

The self-contained `checker.py` uses no third-party packages. Its direct rational tests derive covariance two ways, one from the closed expression and the other from the distinct Dirichlet mixed moments. It also verifies the sign classification on rational grids, checks finite transition points and the asymptotic constant, generates normalized exponential spacings, and independently simulates the original uniformly placed circular centers. In the saved package, running `python checker.py` passed 5,434 checks. This computation is supportive; the all-\(n\), all-\(s\) theorem is proved above, not by finite enumeration or simulation.

## Relationship to prior work

The foundational circle-coverage literature contains strong results. Siegel (1978) analyzes the marginal covered fraction. Holst and Hüsler (1984) obtain joint limit distributions involving the number of gaps and uncovered fraction. Huillet (2003) supplies a much broader **joint transform for the lengths of covered connected components**, so the existence of an exact joint law and the possibility of deriving covariance moments from it are prior knowledge. No novelty is asserted for the Dirichlet spacing model, for the marginal laws, or for possession of the general joint law. The narrower contribution here is the explicit *complete finite-sample sign classification*, including the unique zero for every \(n\), together with its sparse-regime threshold. These properties were not located as statements in the inspected material. Durand (arXiv:0806.0880v1) supplies a precisely dated archival geometric-probability context for random arcs, but studies infinite limsup coverage rather than these finite correlations.

## Limitations

Prior joint-transform work is mathematically strong enough to determine the mixed covariance implicitly. Accordingly historical priority of the covariance expression is not claimed; the sign-classification analysis is the point requiring a new argument. One plausible historical source (Holst–Hüsler 1984) could not be inspected in full, so an exact earlier sign-classification theorem cannot be excluded. Nothing is proved for nonuniform centers, unequal or random arc lengths, or coverage in dimensions above one. The result is not independently audited or externally certified.

## References

1. A. F. Siegel, *Random arcs on the circle*, Journal of Applied Probability **15** (1978), 774–789. DOI: 10.2307/3213433.
2. L. Holst and J. Hüsler, *On the random coverage of the circle*, Journal of Applied Probability **21** (1984), 558–566. DOI: 10.2307/3213617.
3. T. Huillet, *Random covering of the circle: the size of the connected components*, Advances in Applied Probability **35** (2003), 563–582. DOI: 10.1239/aap/1059486818.
4. A. Durand, *On randomly placed arcs on the circle*, arXiv:0806.0880v1 (first submitted 2008-06-05), primary MSC 60D05; studies a different, infinite-coverage question.
