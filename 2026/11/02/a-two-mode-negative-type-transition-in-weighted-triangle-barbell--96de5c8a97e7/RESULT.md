# A two-mode negative-type transition in weighted triangle barbells

## Finding
Let \(X_t\) be the six-vertex metric obtained by joining two copies of the unit-edge triangle \(K_3\) at designated vertices with one bridge of length \(t\ge 1\). The distance \(d_t\) is the weighted shortest-path distance on **all six vertices**. For real \(p\in[1,2]\), set
\[
 A=t^p,\quad B=(t+1)^p,\quad C=(t+2)^p,\quad L=\frac32,\quad T=A-2B+C,
\]
\[
 W_t(p)=L-T,\qquad Z_t(p)=A(L+T)-(1+A-B)^2.
\]
Then \((X_t,d_t)\) has \(p\)-negative type **if and only if** both \(W_t(p)\ge0\) and \(Z_t(p)\ge0\). The function \(W_t\) has exactly one zero \(p_W(t)\in(1,2)\). Let \(p_Z(t)\) be the smallest zero of \(Z_t\) in \((1,2)\). The exact supremal negative-type exponent is
\[
 \wp(X_t)=\min\{p_W(t),p_Z(t)\}.
\]
Both modes genuinely occur as the *first* obstruction: the \(W\)-mode is first for \(t=1\), while the \(Z\)-mode is first for \(t=10\). Consequently, at least one \(t_*\in(1,10)\) satisfies
\[
 W_{t_*}(\wp(X_{t_*}))=Z_{t_*}(\wp(X_{t_*}))=0.
\]
At any such bridge length, the centered Gram matrix of \(d_{t_*}^{\wp(X_{t_*})}\) has rank exactly \(3\), instead of rank \(5\) at every smaller positive exponent. Thus the minimum Euclidean embedding dimension of \(d_{t_*}^{p/2}\) drops from \(5\) to \(3\) at the critical exponent. When only one margin vanishes at the endpoint, its rank is \(4\). No uniqueness of \(t_*\) is claimed.

## Assumptions and scope
The graph has hubs \(h_1,h_2\), two peripheral vertices \(a_1,a_2\) incident to \(h_1\), and two peripheral vertices \(b_1,b_2\) incident to \(h_2\). Each triple \(\{h_1,a_1,a_2\}\) and \(\{h_2,b_1,b_2\}\) is a unit-length triangle. The unique inter-triangle edge \(h_1h_2\) has length \(t\ge1\). Effective resistance is *not* used. \(p\)-negative type means \(\sum_{x,y\in X_t}\alpha_x\alpha_y d_t(x,y)^p\le0\) whenever \(\sum_x\alpha_x=0\), and strictness means equality only for all-zero coefficients. The supremum ranges over all \(p\ge0\).

## Proof
**1. Exact quadratic decomposition.** Fix real coefficients \(h_1,h_2,a_1,a_2,b_1,b_2\) with zero total. Define
\[
 X=a_1+a_2,\quad Y=b_1+b_2,\quad u=h_1+X=-(h_2+Y),\quad z=(X-Y)/\sqrt2,\quad w=(X+Y)/\sqrt2.
\]
Distances between the two hubs, a hub and an opposite peripheral, and opposite peripherals have respective values \(t,t+1,t+2\). Distances between distinct vertices in the same triangle equal \(1\). Direct expansion, using \(h_1=u-X\) and \(h_2=-u-Y\), gives the **exact** identity
\[
\begin{split}
 Q_p:=\sum_{x,y}\alpha_x\alpha_y d_t(x,y)^p
 ={}&-\frac{(a_1-a_2)^2+(b_1-b_2)^2}{2}\\
 &-2Au^2+2\sqrt2(1+A-B)uz\\
 &-(L+T)z^2-W_t(p)w^2.
\end{split}
\]
The two difference modes are strictly negative. The remaining \((u,z)\)-block has upper-left entry \(-2A<0\), and is negative semidefinite exactly when its determinant, \(2[A(L+T)-(1+A-B)^2]=2Z_t(p)\), is nonnegative. The independent \(w\)-block is nonpositive exactly when \(W_t(p)\ge0\). This proves the asserted equivalence, without approximations, for every \(p\ge0\) and \(t>0\). At \(p=1\), the two margins are \(W_t(1)=3/2\) and \(Z_t(1)=3t/2\), so strict \(1\)-negative type holds. At \(p=2\), they are \(W_t(2)=-1/2\) and \(Z_t(2)=-t^2/2\), so \(2\)-negative type fails.

**2. The unique radial zero.** The second difference has the integral formula, for \(1\le p\le2\),
\[
 T=t^p-2(t+1)^p+(t+2)^p
 =\int_0^1\!\int_0^1 p(p-1)(t+r+s)^{p-2}\,dr\,ds.
\]
For \(t\ge1\) the integrand is strictly increasing with \(p\in[1,2]\) away from the endpoint, since \(p(p-1)\) increases and \(t+r+s\ge1\) makes its exponent factor nondecreasing. Thus \(T\) grows strictly from \(0\) to \(2\), so \(W_t\) has precisely one zero \(p_W(t)\in(1,2)\), depending continuously on \(t\). Continuity, the endpoint signs for \(Z_t\), and the intermediate value theorem ensure at least one \(Z\)-zero in \((1,2)\) for each \(t\). The interval property of negative type (Li–Weston, reference 1) shows that its first loss is at the smaller of these roots, and that negative type is strict below the endpoint and absent above it. In fact, at any positive critical endpoint the whole equality space is exactly the nullspace identified by the displayed decomposition.

**3. A certified radial-first bridge.** For \(t=1\) and \(p_0=47/25\), exact integer-power outward bounds (reproducible in the accompanying Python checker) give
\[
 -0.026882<W_1(p_0)<-0.026880,\qquad
 0.201958<Z_1(p_0)<0.201960.
\]
To show that the \(Z\)-mode has not already failed before \(p_0\), set \(s=2^p\), \(\alpha=\log_2 3\). Then
\[
 Z_1(p)=s^\alpha-s^2+2s-\frac32.
\]
For \(s\ge2\), its second derivative is \(\alpha(\alpha-1)s^{\alpha-2}-2<0\), since \(1<\alpha<2\). Thus \(Z_1\), viewed as a function of \(s\), is concave on \([2,2^{p_0}]\); it is positive at both ends (at \(p=1\), the value is \(3/2\)), hence throughout. Since \(W_1\) is strictly decreasing and negative at \(p_0\), its zero occurs first. Accordingly \(H(1)>0\) for \(H(t):=Z_t(p_W(t))\).

**4. A certified antisymmetric-first bridge.** For \(t=10\), at \(p_1=48/25\), the same outward integer-power certificates give
\[
 0.041845<W_{10}(p_1)<0.041847,\qquad
 -0.522135<Z_{10}(p_1)<-0.522133.
\]
Thus \(p_1<p_W(10)\), but \(p_1\)-negative type already fails via \(Z\). Necessarily \(H(10)<0\): if \(H(10)\ge0\), both margins would be nonnegative at \(p_W(10)\), yielding negative type there and, by downward heredity, at \(p_1\), a contradiction.

**5. A genuine codimension-two critical point.** The function \(H(t)\) is continuous for \(t\in[1,10]\), because \(Z_t(p)\) is jointly continuous and \(p_W(t)\) is uniquely defined by a strictly monotone continuous equation. Since \(H(1)>0>H(10)\), there exists \(t_*\in(1,10)\) with \(H(t_*)=0\). At \(p=p_W(t_*)\), *both* margins vanish and the decomposition proves \(p\)-negative type. It is the critical exponent, because \(W_t\) is negative above its zero. The independent \(w\)-mode and the one-dimensional nullspace of the \((u,z)\) determinant-zero block provide exactly two zero-sum equality directions. Together with two strictly negative peripheral fluctuation directions and one strictly negative \((u,z)\) direction, this gives rank \(3\) for \(-\frac12 J(d_t(x,y)^p)J\). At every smaller positive \(p\), strict negative type and six distinct metric points give rank \(5\). Schoenberg's squared-Euclidean characterization converts these ranks to the claimed minimum Euclidean embedding dimensions.

## Verification
Run `python verify_weighted_triangle_barbell.py` with Python 3 (standard library only). It independently enumerates all simple paths to rebuild the six-point weighted distance matrix; tests the quadratic decomposition with exact rational arithmetic for \(640\) cases; and computes the two rational-exponent sign witnesses using enclosing intervals justified by integer-power comparisons. The checker also supplies noncertifying floating-point diagnostics near the mode crossing. The sign certificates, not those diagnostics, support the existence proof. Finite verification alone is not a proof for every real \(p\) or \(t\); the preceding analytic argument supplies that proof.

## Relationship to prior work
Li–Weston establish downward propagation and strictness of negative type (reference 1); Sánchez develops a general distance-matrix method for computing supremal negative type of finite metrics (reference 2). Aalipour and coauthors (reference 3, Section 5, Theorems 5.1–5.2) determine determinants and inertia of *ordinary unweighted* distance matrices of generalized barbells. None of those inspected results states the two-variable powered-distance margins or the simultaneous two-mode criticality at a variable bridge length. The unweighted unit-bridge metric is a special limiting parameter value, not the mode-crossing result; ordinary distance-matrix inertia is not equivalent to the powered-distance Euclidean rank theorem. Existing general matrix criteria alone do not provide the evaluated threshold comparison or prove a bridge-length transition.

## Limitations
The theorem covers only two unit-edge triangles with a single bridge of length \(t\ge1\), all six vertices and weighted shortest-path distances; not arbitrary clique sizes, other edge lengths, electrical metrics, or graphs with multiple bridges. Existence, not uniqueness, of a simultaneous critical bridge length is proved; the crossing is not assigned a rigorously certified decimal value. The computed examples are corroboration, not an all-parameter exhaustive certificate. Equivalent coverage in unindexed mathematical literature remains a publication-priority risk; no independent scientific audit has been performed.

## References
1. Hanfeng Li and Anthony Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695, first publicly posted 2009-01-06, https://arxiv.org/abs/0901.0695 .
2. Stephen Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451, first publicly posted 2011-08-02, https://arxiv.org/abs/1108.0451 .
3. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196, first publicly posted 2015-09-03, https://arxiv.org/abs/1509.01196 .
