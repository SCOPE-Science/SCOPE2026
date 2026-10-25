# A sharp asymptotic covariance barrier for two-layer signed-order polytopes

## Finding
For integers \(p\ge3\), \(q\ge2\), write \(n=p+q\) and consider the full-dimensional polytope
\[
K_{p,q}=\left\{(x,y)\in[-1,1]^p\times[-1,1]^q:\ x_i+x_j\ge0\ (i<j),\ y_j\ge|x_i|\ (1\le i\le p,1\le j\le q)\right\}.
\]
It is a signed order polytope of type \(B\): take the positive-linear closure within the type-\(B\) roots of \(\{e_i+e_j:i<j\le p\}\cup\{e_{p+j}\pm e_i:i\le p,j\le q\}\). The vector with all bottom coordinates \(\varepsilon\) and all top coordinates \(2\varepsilon\), for sufficiently small positive \(\varepsilon\), verifies that the closure contains no root and its negative and that the polytope is full-dimensional.

Let \((X,Y)\) be uniformly distributed by ordinary \(n\)-dimensional Euclidean volume on \(K_{p,q}\). Its volume is
\[\operatorname{Vol}_n(K_{p,q})=\frac{2p!q!}{(p+q)!}.\]
Define
\[
\mu=\frac{(p-1)(p+2)}{2p(p+1)},\qquad
c_{\perp}=\frac{p^3+3p^2+14p+48}{12p(p+1)(p+2)},\qquad
c_{\parallel}=\frac{p^4+4p^3-7p^2+26p+24}{12p(p+1)^2(p+2)},
\]
\[
R=\frac{p+1}{n+1},\quad S=\frac{(p+1)(p+2)}{(n+1)(n+2)},\quad V=\frac{(p+1)q}{(n+1)^2(n+2)}.
\]
The covariance of \((X,Y)\) has an eigenvalue \(S c_{\perp}\) on the \((p-1)\)-dimensional bottom zero-sum subspace, an eigenvalue
\[d=\frac{(q+1)(q+2)}{12(n+1)(n+2)}\]
on the \((q-1)\)-dimensional top zero-sum subspace, and the two eigenvalues of the symmetric matrix
\[
M_{p,q}=\begin{pmatrix}
S c_{\parallel}+p\mu^2 V&\sqrt{pq}\,\mu\dfrac{q+1}{2q}V\\[4pt]
\sqrt{pq}\,\mu\dfrac{q+1}{2q}V&\dfrac{(q+1)^2(p+1)}{4(n+1)^2(n+2)}+\dfrac{(q-1)(q+1)}{12(n+1)(n+2)}
\end{pmatrix}.
\]
The matrix is expressed in the orthonormal directions \(p^{-1/2}(\mathbf1_p,0)\) and \(q^{-1/2}(0,\mathbf1_q)\). The coordinate means are \(\mathbb E X_i=\mu R\) and \(\mathbb E Y_j=(2p+q+1)/(2(n+1))\).

Let \(\kappa_{p,q}\) denote the ratio of largest to smallest covariance eigenvalue. If \(p,q\to\infty\) and \(p/(p+q)\to a\in(0,1)\), write \(b=1-a\), \(t=ab\), and
\[\Lambda_+(t)=\frac{1+t+\sqrt{1+2t-15t^2}}2.\]
Then
\[
\boxed{\lim\kappa_{p,q}=\frac{\Lambda_+(ab)}{\min\{a^2,b^2\}}\quad\ge4,\qquad \text{with equality precisely when }a=b=\tfrac12.}
\]
In addition, along any sequence \(p+q\to\infty\) with \(p\ge3,q\ge2\) and \(p/(p+q)\to0\) or \(1\), one has \(\kappa_{p,q}\to\infty\). Consequently \(\liminf_{p+q\to\infty}\kappa_{p,q}\ge4\) for arbitrary parameter sequences, and \(\kappa_{p,q}\to4\) if and only if the bottom fraction tends to \(1/2\).

## Assumptions and scope
All volumes and covariances use the fixed standard coordinate Euclidean metric; no affine normalization is applied. The condition number is the ratio of covariance eigenvalues, not the ratio of ellipsoid semiaxis lengths. Parameters are integers \(p\ge3\), \(q\ge2\). The asymptotic assertions refer to actual sequences of such integers, including oscillatory rank proportions for the last liminf statement. Neither a rate of convergence for general varying proportions nor a finite-dimensional bound \(\kappa_{p,q}\ge4\) is asserted.

## Proof
**1. The base sector formula.** Let
\[B_p=\{z\in[-1,1]^p:z_i+z_j\ge0\text{ for all }i<j\}.\]
Up to zero-volume boundaries this consists of the positive unit cube and \(p\) sectors indexed by one negative coordinate \(z_i=-u\), \(0<u<1\), with all remaining coordinates between \(u\) and \(1\). Every negative sector has volume
\[\int_0^1(1-u)^{p-1}\,du=\frac1p,\]
so \(\operatorname{Vol}_p(B_p)=2\). The positive cube has half the uniform probability; the union of the negative sectors has the other half. In the latter case the negative index is uniform and its magnitude has density \(p(1-u)^{p-1}\); conditionally the other coordinates are independent uniform variables on \([u,1]\). Direct integration of the first and mixed second moments gives
\[
\mathbb EZ_i=\mu,\quad \mathbb EZ_i^2=\frac13,\quad
\operatorname{Cov}(Z_i,Z_j)=-\frac{2p^2+3p+2}{p^2(p+1)^2(p+2)}\ (i\ne j).
\]
Here \(Z\) is uniform in \(B_p\). The permutation-invariant covariance therefore has eigenvalues \(c_{\perp}\) in the zero-sum subspace and \(c_{\parallel}\) along the normalized all-ones vector, as displayed. For an independently reproducible calculation, all sector integrals reduce to
\[\int_0^1u^r(1-u)^{p-1}\,du=\frac{r!(p-1)!}{(p+r)!}\qquad(r=0,1,2).\]
These calculations also give \(c_{\perp}-c_{\parallel}=(2p^2+3p+2)/(p(p+1)^2(p+2))>0\).

**2. Exact disintegration.** For fixed \(y\in[0,1]^q\) put \(T=\min_j y_j\). The bottom slice is precisely \(TB_p\), of Euclidean volume \(2T^p\). Thus
\[
\operatorname{Vol}_n(K_{p,q})=2q\int_0^1u^p(1-u)^{q-1}du
=\frac{2p!q!}{n!}.
\]
Under normalized uniform volume \(T\) has the beta law with shape parameters \(p+1,q\). Conditionally on \(T=u\), its minimizing coordinate index \(J\) is uniform among the \(q\) top indices, all other top coordinates are independent uniform on \([u,1]\), and \(X=uZ\) for an independent uniform \(Z\) on \(B_p\). Thus \(\mathbb ET=R\), \(\mathbb ET^2=S\), \(\operatorname{Var}T=V\), and
\[\mathbb E(1-T)^2=\frac{q(q+1)}{(n+1)(n+2)}.\]

**3. Covariance diagonalization.** Conditional on \(T=u\),
\[
\mathbb E[Y_j\mid T=u]=\frac{q-1}{2q}+\frac{q+1}{2q}u,\qquad
\operatorname{Var}\Bigl(\sum_{j=1}^qY_j\bigm|T=u\Bigr)=\frac{q-1}{12}(1-u)^2.
\]
By top-coordinate exchangeability,
\[
\frac12\mathbb E[(Y_i-Y_j)^2\mid T=u]
=\frac{q+2}{12q}(1-u)^2\quad(i\ne j).
\]
The law of total covariance yields the top transverse eigenvalue \(d\) and the top longitudinal entry of \(M_{p,q}\). Independently, \(X=TZ\) yields the bottom transverse eigenvalue \(Sc_{\perp}\) and bottom longitudinal entry \(Sc_{\parallel}+p\mu^2V\). Finally, the normalized bottom and top block sums have covariance \(\sqrt{pq}\,\mu(q+1)V/(2q)\), giving the off-diagonal entry. Since the body is full-dimensional, its covariance is positive definite and these are all \(p+q\) eigenvalues.

**4. The limiting matrix and sharp barrier.** Put \(a=p/n\), \(b=q/n\). In the regime \(a\to a_0\in(0,1)\), \(b\to b_0=1-a_0\), the bottom/top transverse eigenvalues converge to \(a_0^2/12\) and \(b_0^2/12\). From \(\mu\to1/2\), \(c_{\perp},c_{\parallel}\to1/12\), and \(nV\to a_0b_0\), the longitudinal block converges to
\[
\frac1{12}G(a_0,b_0),\qquad
G(a,b)=\begin{pmatrix}a^2(1+3b)&3(ab)^{3/2}\\3(ab)^{3/2}&b^2(1+3a)\end{pmatrix}
=\operatorname{diag}(a^2,b^2)+3ab\,vv^{\mathsf T},
\]
where \(v=(\sqrt a,\sqrt b)\) is a unit vector. The matrix \(G\) dominates the diagonal matrix, so its smaller eigenvalue is at least \(\min\{a^2,b^2\}\); its larger eigenvalue dominates both transverse values. Since \(\operatorname{tr}G=1+ab\) and \(\det G=4a^2b^2\), its larger eigenvalue equals \(\Lambda_+(ab)\). Also \(v^{\mathsf T}Gv=1\), so \(\Lambda_+(ab)\ge1\). Meanwhile \(\min\{a^2,b^2\}\le1/4\), with equality only when \(a=b=1/2\). At that balanced point the eigenvalues of \(G\) are \(1,1/4\), giving exactly the threshold \(4\). Thus the minimum limiting condition number is precisely \(4\) and the minimizing proportion is unique.

If \(p/n\to0\), the bottom zero-sum eigenvalue \(Sc_{\perp}\to0\), while the top zero-sum eigenvalue tends to \(1/12\); if \(p/n\to1\), the reverse holds. Positivity and compactness of \([0,1]\), together with the interior limit just proved, yield the final uniform liminf statement and the necessary-and-sufficient balanced criterion for convergence to \(4\).

## Verification
The included `check.py` derives bottom moments independently by exact rational beta integrals and independently recomputes every rational covariance term. It compared \(440\) pairs \((p,q)\) in \(3\le p\le24\), \(2\le q\le21\), checking equality with the closed forms and positive definiteness. It separately evaluated the balanced and unbalanced limiting regimes numerically. The all-parameter and asymptotic assertions follow from the preceding proof, not from finite computation.

## Relationship to prior work
Beck–Hlavacek (2023) introduced the signed-poset order polytope construction, its signed-filter description, triangulations, Ehrhart series, and Gorenstein questions; their available complete article does not present the present uniform-volume covariance spectrum or its asymptotic optimization. Hamano–Hibi–Ohsugi (2016) study Ehrhart theory of fractional stable-set polytopes: the **bottom** polytope \(B_p\) is affinely related to the complete-graph fractional stable-set polytope, by \(z_i=1-2w_i\). That equivalence is explicitly acknowledged and supplies no novelty claim for the bottom object. The new claim concerns its coupling to a top antichain through simultaneous inequalities \(y_j\ge|x_i|\) and the resulting covariance spectrum and unique asymptotic optimum. Generic beta and total-covariance identities are standard tools, not claimed as original.

## Limitations
No claim of an exhaustive literature search or independent validation is made. Equivalent formulations might appear under generalized order-polytopes, signed graphs, fractional stable-set fibres, or conditional-beta geometry. This is an asymptotic conditioning result in a specified coordinate Euclidean realization; affine transformations can change the covariance condition number. The theorem does not assert an exact finite-dimensional minimizer over the integer parameters.

## References
1. M. Beck and M. Hlavacek, *Signed Poset Polytopes*, arXiv:2311.04409v1, first public 2023-11-08. https://arxiv.org/abs/2311.04409
2. G. Hamano, T. Hibi and H. Ohsugi, *Ehrhart Series of Fractional Stable Set Polytopes of Finite Graphs*, arXiv:1603.09613v1, first public 2016-03-31. https://arxiv.org/abs/1603.09613
