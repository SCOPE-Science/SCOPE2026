# Power-weighted interval counterexample to the doubling-only Campanato criterion
## Finding
Let \(\beta>0\), \(p\in[1,\infty)\), and \(1<Q<\beta+1\). Equip
\[
X=[0,1]
\]
with the Euclidean metric and the measure
\[
d\mu_\beta(x)=x^\beta\,dx.
\]
For every \(Q<\lambda<Q+p\), set
\[
\alpha=\frac{\lambda-Q}p\in(0,1).
\]
Then \(\mu_\beta\) is Borel regular and doubling, but it is not lower \(Q\)-regular, and
\[
L_C^{p,\lambda}(X,\mu_\beta)\hookrightarrow C^{0,\alpha}(X)
\quad\Longleftrightarrow\quad
\lambda>p+1.
\]
More precisely, when \(\lambda>p+1\), every Campanato element is almost everywhere constant, so the embedding is automatic and continuous. When \(Q<\lambda\le p+1\), choose
\[
\max\left\{0,\frac{\lambda-\beta-1}p}\right\}<\delta<\alpha.
\]
Then
\[
f_\delta(x)=x^\delta
\]
belongs to \(L_C^{p,\lambda}(X,\mu_\beta)\) but has no representative in \(C^{0,\alpha}(X)\).

In particular, the doubling-only equivalence proposed in Question 5 of Górka--Stępień is false. Indeed, because \(Q>1\), the interval
\[
\max\{Q,p+1\}<\lambda<Q+p
\]
is always nonempty; throughout that interval the Campanato embedding holds although \(\mu_\beta\) is not lower \(Q\)-regular.

## Assumptions and scope
The Campanato norm is the radius-normalized norm used by Górka--Stępień,
\[
\|f\|_{L_C^{p,\lambda}}
=
\|f\|_{L^p(\mu_\beta)}+
\sup_{x\in X,\,r>0}
\left(
\frac1{r^\lambda}
\int_{B(x,r)}|f-f_{B(x,r)}|^p\,d\mu_\beta
\right)^{1/p}.
\]
Here \(f_B\) denotes the \(\mu_\beta\)-average over \(B\). The Hölder norm is the usual bounded \(C^{0,\alpha}\) norm.

The interval \([0,1]\) is compact, connected, and hence uniformly perfect. The measure \(\mu_\beta\) is a finite Radon measure, hence Borel regular. Its ball masses are differences of powers,
\[
\mu_\beta([a,b])=\frac{b^{\beta+1}-a^{\beta+1}}{\beta+1},
\]
which gives a finite doubling constant depending only on \(\beta\). At the endpoint \(0\),
\[
\mu_\beta(B(0,r))=\frac{r^{\beta+1}}{\beta+1},
\]
so
\[
\frac{\mu_\beta(B(0,r))}{r^Q}
=\frac{r^{\beta+1-Q}}{\beta+1}\longrightarrow0
\]
as \(r\downarrow0\). Thus lower \(Q\)-regularity fails exactly for the reason needed here.

## Proof
First suppose \(\lambda>p+1\), and put
\[
s=\frac{\lambda-1}p>1.
\]
Fix a compact interval \([a,b]\subset(0,1)\). On this interval the density \(x^\beta\) is bounded above and below by positive constants. Let \(I\) and \(J\) be adjacent intervals of equal length \(h\), contained in \([a,b]\), and let \(U=I\cup J\). If \(K=[f]_{L_C^{p,\lambda}}\), then the Campanato estimate on the ball \(U\) gives
\[
\int_U|f-f_U|^p\,d\mu_\beta\le K^p h^\lambda.
\]
Since \(\mu_\beta(I),\mu_\beta(J)\ge a^\beta h\), Hölder's inequality yields
\[
|f_I-f_U|+|f_J-f_U|
\le 2K a^{-\beta/p}h^s,
\]
and therefore
\[
|f_I-f_J|\le 2K a^{-\beta/p}h^s.
\]
Take two \(\mu_\beta\)-Lebesgue points \(x<y\) in \([a,b]\), partition \([x,y]\) into \(N\) equal intervals, and telescope the weighted averages of adjacent pieces. With \(h=(y-x)/N\),
\[
|f(x)-f(y)|
\le 2K a^{-\beta/p}(y-x)^s N^{1-s}
\longrightarrow0.
\]
Thus \(f\) is almost everywhere constant on every compact subinterval of \((0,1)\), hence almost everywhere constant on \(X\). If that constant is \(c\), then
\[
|c|\le \mu_\beta(X)^{-1/p}\|f\|_{L^p(\mu_\beta)}
=(\beta+1)^{1/p}\|f\|_{L^p(\mu_\beta)}.
\]
The constant representative has zero Hölder seminorm, proving a continuous embedding into \(C^{0,\alpha}(X)\).

Now suppose \(Q<\lambda\le p+1\). Because \(Q<\beta+1\), the interval
\[
\left(\max\left\{0,\frac{\lambda-\beta-1}p}\right\},\frac{\lambda-Q}p\right)
\]
is nonempty. Choose \(\delta\) in it and set \(f(x)=x^\delta\). Then
\[
p\delta+\beta+1>\lambda.
\]
For a metric ball \(B=B(x,r)\), use
\[
\int_B|f-f_B|^p\,d\mu_\beta
\le 2^p\inf_{c\in\mathbb R}\int_B|f-c|^p\,d\mu_\beta.
\]
If \(x\le2r\), take \(c=0\). Since \(B\subset[0,3r]\) up to the harmless large-radius truncation at \(1\),
\[
\int_B|f|^p\,d\mu_\beta
\le C r^{p\delta+\beta+1}
\le C r^\lambda.
\]
If \(x>2r\), take \(c=x^\delta\). Because \(0<\delta<\alpha<1\), the mean-value theorem gives
\[
|t^\delta-x^\delta|\le C r x^{\delta-1}
\qquad(t\in B),
\]
and \(\mu_\beta(B)\le C r x^\beta\). Hence
\[
\int_B|f-x^\delta|^p\,d\mu_\beta
\le C r^{p+1}x^{p(\delta-1)+\beta}.
\]
Write
\[
A=p+1-\lambda\ge0,
\qquad
E=p(\delta-1)+\beta.
\]
Then
\[
A+E=p\delta+\beta+1-\lambda>0.
\]
If \(E\ge0\), the quotient by \(r^\lambda\) is bounded by \(Cr^A x^E\le C\). If \(E<0\), the condition \(x>2r\) gives \(x^E\le(2r)^E\), so the same quotient is at most \(Cr^{A+E}\le C\). Therefore \(f\in L_C^{p,\lambda}(X,\mu_\beta)\).

On the other hand, \(\delta<\alpha\), and
\[
\frac{|f(x)-f(0)|}{x^\alpha}=x^{\delta-\alpha}\longrightarrow\infty
\]
as \(x\downarrow0\). Thus \(f\notin C^{0,\alpha}(X)\). Any continuous representative agreeing with \(f\) almost everywhere must equal \(f\) on \((0,1]\), because \(\mu_\beta\) has positive density there and the equality set is dense; continuity then fixes the value at \(0\) as well. Hence no Hölder representative exists. This proves failure of the embedding for \(Q<\lambda\le p+1\) and completes the phase diagram.

## Verification
The two critical thresholds are independent and were checked symbolically. The endpoint defect of lower \(Q\)-regularity is governed by \(\beta+1-Q>0\). Membership of the explicit obstruction is governed by
\[
p\delta+\beta+1-\lambda>0,
\]
while failure of the target Hölder regularity is exactly \(\delta<\alpha\). These two inequalities are simultaneously feasible because
\[
\alpha-\frac{\lambda-\beta-1}p=\frac{\beta+1-Q}p>0.
\]
For the constant-space branch, the local oscillation exponent is \((\lambda-1)/p\), which is greater than \(1\) exactly when \(\lambda>p+1\); subdivision then forces constancy.

No numerical experiment or finite enumeration is used. The proof covers \(p=1\), the critical point \(\lambda=p+1\) on the nonembedding side when it lies above \(Q\), and every \(\lambda\) in the source's open range \(Q<\lambda<Q+p\).

## Relationship to prior work
Górka--Stępień prove that lower \(Q\)-regularity is equivalent to the Campanato-to-Hölder embedding under doubling for \(Q<\lambda\le p\), and ask whether the equivalence remains true for the full interval \(Q<\lambda<Q+p\). They also give a cusp-domain example where failure of lower regularity can coexist with an embedding at and beyond the outer endpoint \(\lambda=Q+p\). The present power-weighted interval moves this phenomenon strictly inside their open interval and gives the exact transition \(\lambda=p+1\).

A previously established reverse-doubling extension gives necessity on a window \(\lambda<p+\kappa\), where \(\kappa\) is a global reverse-doubling exponent. It does not cover the present positive-embedding branch. Indeed, at every interior point of the weighted interval, ball mass is asymptotically linear in the radius, so no global reverse-doubling power exponent greater than \(1\) can hold; the regime \(\lambda>p+1\) lies beyond that mechanism.

Classical Campanato theory explains the local threshold: on a one-dimensional region with measure comparable to Lebesgue measure, radius-normalized Campanato spaces become constant once \(\lambda>p+1\). Stempak records this Euclidean triviality threshold in the global theory. The new point is to combine that local one-dimensional collapse with an endpoint power weight whose lower regularity dimension is strictly larger than the chosen \(Q\), thereby producing a doubling counterexample to the specific lower-regularity criterion.

## Limitations
The result is a counterexample family, not a classification of all doubling metric-measure spaces. It uses an absolutely continuous power weight on a compact interval and exploits the coexistence of one-dimensional interior scaling with higher-order vanishing of measure at the endpoint. It does not decide what additional nondegeneracy assumptions, beyond doubling and uniform perfectness, restore the equivalence in the remaining parameter range.

## References
1. P. Górka and Z. Stępień, *Optimal Embeddings of Campanato and Morrey Spaces*, arXiv:2610.04622v1 (2026), especially Theorems 3.10--3.11, Example 3.8, and Question 5.
2. E. Nakai, *The Campanato, Morrey and Hölder spaces on spaces of homogeneous type*, Studia Mathematica 176 (2006), 1--19, DOI: 10.4064/sm176-1-1.
3. K. Stempak, *Local Morrey and Campanato Spaces on Quasimetric Measure Spaces*, Journal of Function Spaces 2014 (2014), Article 172486, DOI: 10.1155/2014/172486.
