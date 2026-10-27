# Sharp triple crossing and reentrant angular order in first-Landau-level Fock annuli

## Finding
On the first true-polyanalytic Gaussian Fock space, concentration on a centered annulus can reverse the ordering of **two adjacent angular modes three times** as its outer radius increases. This count is sharp, and all inner-radius regimes are classified exactly.

For every integer \(k\ge1\), put
\[
H_k(t)=\frac{e^{-t}t^k(t-k)(t-k-1)}{(k+1)!}\qquad(t>0).
\]
There are exactly three positive critical points \(0<u_k<k<v_k<k+1<w_k\) of \(H_k\). The outer positive maximum is strictly higher than the inner positive maximum: \(H_k(w_k)>H_k(u_k)>0\).

Let \(N_k(a)\) be the number of **distinct** outer squared radii \(b>a\) at which the annular concentration eigenvalues for angular orders \(k-1\) and \(k\) coincide. Then
\[
N_k(a)=\begin{cases}
3,&0<a<u_k,\\
2,&u_k\le a<k,\\
1,&a=k,\\
1,&k<a<v_k,\\
0,&v_k\le a\le k+1,\\
1,&k+1<a<w_k,\\
0,&a\ge w_k.
\end{cases}
\]
Every counted crossing is simple in \(b\). When \(0<a<u_k\), the ordering changes three times, realizing a genuine reentrant three-crossing pattern.

## Assumptions and scope
Use \(d\gamma(z)=\pi^{-1}e^{-|z|^2}\,dA(z)\). The first true-polyanalytic Gaussian Fock space \(\mathcal F_{(2)}\) has orthonormal basis \(\Phi_0(z)=\bar z\) and \(\Phi_k(z)=z^{k-1}(|z|^2-k)/\sqrt{k!}\), \(k\ge1\). For \(0<a<b<\infty\), define \(A_{a,b}=\{z\in\mathbb C:a<|z|^2<b\}\), and the positive contraction \(T_{a,b}=P_{\mathcal F_{(2)}}M_{\mathbf1_{A_{a,b}}}P_{\mathcal F_{(2)}}|_{\mathcal F_{(2)}}\). The eigenvalue \(\Lambda_k(a,b)=\langle T_{a,b}\Phi_k,\Phi_k\rangle\) corresponds to angular order \(k-1\) for \(k\ge1\). The theorem concerns adjacent indices \(k\) and \(k+1\), not arbitrary nonadjacent modes or higher polyanalytic levels.

## Proof
Rotation invariance and the distinct angular frequencies diagonalize \(T_{a,b}\) in this basis. Polar integration gives, for \(k\ge1\),
\[
\Lambda_k(a,b)=\frac1{k!}\int_a^b e^{-t}t^{k-1}(t-k)^2\,dt,
\qquad\Lambda_0(a,b)=\int_a^b te^{-t}\,dt.
\]
Direct differentiation yields the exact boundary identity
\[
\Lambda_k(a,b)-\Lambda_{k+1}(a,b)=H_k(b)-H_k(a).
\tag{1}
\]
Moreover,
\[
H_k'(t)=\frac{e^{-t}t^{k-1}}{(k+1)!}Q_k(t),\quad
Q_k(t)=-t^3+(3k+3)t^2-(3k^2+4k+1)t+k^3+k^2.
\tag{2}
\]
The values \(H_k(0)=H_k(k)=H_k(k+1)=\lim_{t\to\infty}H_k(t)=0\), with \(H_k\) positive on \((0,k)\) and \((k+1,\infty)\), and negative on \((k,k+1)\). Rolle's theorem gives a critical point in each of the first two bounded intervals. Decay from positivity to zero supplies one in the outer interval. As \(Q_k\) is cubic, these are its only roots, each simple, with signs \(+,-,+,-\) for \(H_k'\). Write these roots \(u_k,v_k,w_k\).

It remains to prove the non-obvious global comparison \(H_k(w_k)>H_k(u_k)\). For \(k\ge3\), write \(m=k+1\ge4\). Any \(x\in(0,k)\) has representation \(x=m-y\) with \(1<y<m\). Its reflected point \(m+y>k+1\) satisfies
\[
\frac12\log\frac{H_k(m+y)}{H_k(m-y)}
=(m-1)\operatorname{artanh}(y/m)-y+\operatorname{artanh}(1/y).
\]
For \(0<q<1\), \(\operatorname{artanh}q>q+q^3/3\) and \(\operatorname{artanh}q>q\). Hence the last expression is strictly greater than
\[
\frac1y\left(1-v+\frac{m-1}{3m}v^2\right),\qquad v=y^2/m.
\]
The quadratic in parentheses is nonnegative for every real \(v\), since its discriminant is \((4-m)/(3m)\le0\). Thus \(H_k(m+y)>H_k(m-y)\), and applying this to \(x=u_k\) proves the strict maxima inequality.

For \(k=1\), on \(0<x<1\), \(H_1(x)<x(1-x)(2-x)/2\le1/(3\sqrt3)<1/5\), whereas \(H_1(4)=12e^{-4}>1/5\) (using \(e<11/4\)). For \(k=2\), on \(0<x<2\), \(e^{-x}\le1/(1+x)\) and
\[
1+x-x^2(2-x)(3-x)=(x-1)^2(1+3x-x^2)\ge0,
\]
so \(H_2(x)\le1/6\). But \(H_2(6)=72e^{-6}>1/6\) (using \(e<137/50\)). Thus the maxima inequality holds for all indices.

Equation (1) reduces crossings to the future level set \(H_k(b)=H_k(a)\). The four strictly monotone segments separated by \(u_k,v_k,w_k\), the zeros at \(k,k+1\), and the strict inequality between maxima give the seven cases in the statement by counting level-set intersections for \(b>a\). At boundary values, the level set touching the current point is not counted. Any future intersection occurs away from critical points (the larger outer maximum precludes a tangency from an earlier inner positive level), so every counted crossing is simple and changes sign. The two outer positive branches account for the two additional reversals when \(a<u_k\). This proves all assertions.

## Verification
`annular_spectral_checker.py` independently checks the differentiated boundary polynomial symbolically, three real critical-point locations and maximal-height inequality, annular quadrature against the boundary identity, and the seven level-set counts for indices \(1\le k\le14\). It reports 182 checks passed. These finite checks corroborate, but do not replace, the all-index proof above.

## Relationship to prior work
Maximenko and Tellería-Romero (2019) provide radial-operator diagonalization for polyanalytic Fock spaces; Fulsche and Hagger (2023) develop the broader polyanalytic Fock Toeplitz setting. A previously established disk eigenvalue difference already gives the one-boundary factor \(H_k\). The new result does **not** claim that diagonalization or that disk formula as novel: it establishes the complete annular level-set bifurcation and proves the strict outer-versus-inner hump inequality needed to realize exactly three reversals for every index. Available related records do not state this complete annular classification; equivalent older formulas remain possible.

## Limitations
The theorem is for centered radial annuli in the first true-polyanalytic layer and adjacent angular indices \(k\ge1\). It does not treat \(\Phi_0\) versus \(\Phi_1\), arbitrary annular nonadjacent-mode coincidence counts, higher levels, or full operator-norm maximizers. Priority is best knowledge, not independently established.

## References
- E. A. Maximenko and A. M. Tellería-Romero, *Radial operators on polyanalytic Bargmann–Segal–Fock spaces*, arXiv:1905.00978 (first posted 2019-05-02), especially the radial diagonalization and Laguerre integrals.
- R. Fulsche and R. Hagger, *Quantum harmonic analysis for polyanalytic Fock spaces*, arXiv:2308.11292 (first posted 2023-08-22), on polyanalytic Fock localization and Toeplitz operators.
