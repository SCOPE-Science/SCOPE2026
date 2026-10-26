# Sharp subcritical-moment logarithmic growth at the critical weighted-shift boundary

## Finding

Fix \(1\le p<\infty\) and \(0<q<p\). On the weighted sequence space defined below, let \(B\) be the backward shift. Its optimal finite-horizon \(q\)-moment operator-orbit constant satisfies
\[
\lim_{N\to\infty}\frac{C_{p,q}(N)}{(\log N)^{1/p}}
=\left(1-\frac qp\right)^{(p-q)/(pq)}.
\]
This coefficient is strictly below one. An explicit asymptotically maximizing family has diffuse, increasing coordinate energy, rather than a single-coordinate concentration. The theorem includes \(0<q<1\), when the averaged moment is a quasi-moment rather than a norm. In contrast, normalized coordinate basis vectors have uniformly bounded finite-horizon \(q\)-moments, so they do not witness this logarithmic growth.

## Assumptions and scope

Let \(\mathbb K\) be \(\mathbb R\) or \(\mathbb C\), let \(1\le p<\infty\), and let \(0<q<p\). Define
\[
 X_p=\left\{x=(x_i)_{i\ge1}:\sum_{i\ge1}\frac{|x_i|^p}{i}<\infty\right\},\qquad
 \|x\|_{p,w}^p=\sum_{i\ge1}\frac{|x_i|^p}{i},\qquad (Bx)_i=x_{i+1}.
\]
Then \(B\) is bounded, because \(\|Bx\|_{p,w}^p\le2\|x\|_{p,w}^p\). For integers \(N\ge2\), put
\[
 C_{p,q}(N)=\sup_{\|x\|_{p,w}=1}
 \left(\frac1N\sum_{k=0}^{N-1}\|B^kx\|_{p,w}^q\right)^{1/q}.
\]
Let \(r=q/p\in(0,1)\) and \(a=r/(1-r)\). One asymptotically optimal family is
\[
 Z_N=\sum_{j=1}^N \frac{(j/N)^a}{1-r},\quad
 |x_i^{(N)}|^p=\frac{i(i/N)^a}{(1-r)Z_N}\ (1\le i\le N),\quad
 x_i^{(N)}=0\ (i>N).
\]
These are unit vectors; the phases of their nonzero coordinates may be chosen arbitrarily.

## Proof

**Reduction to positive coordinate energies.** For any unit vector set \(u_i=|x_i|^p/i\). Then \(u_i\ge0\), \(\sum_i u_i=1\), and
\[
 F_k=\|B^kx\|_{p,w}^p
 =\sum_{i>k}\frac{i}{i-k}u_i.
\]
Conversely every probability vector \(u\) is realized by a unit vector, with \(|x_i|^p=i u_i\). Consequently, if
\[
 J_N=\frac1N\sup_{u_i\ge0,\,\sum u_i=1}\sum_{k=0}^{N-1}F_k^r,
\]
then \(C_{p,q}(N)=J_N^{1/q}\). We prove
\[
 \lim_{N\to\infty}\frac{J_N}{(\log N)^r}=(1-r)^{1-r}.
\]

**Uniform upper estimate.** Let \(0<\delta<1\) and \(m=\lfloor\delta N\rfloor\ge1\). For every coordinate \(i\ge1\),
\[
 \sum_{0\le k<m,\,k<i}\frac{i}{i-k}\le mH_m,
 \qquad H_m=\sum_{j=1}^m\frac1j.
\]
For \(i\le m\), the left side equals \(iH_i\le mH_m\); for \(i>m\), each summand \(i/(i-k)\) is nonincreasing in \(i\), so its sum is at most the value \(mH_m\) at \(i=m\). Averaging over \(u\) gives \(\sum_{k<m}F_k\le mH_m\). By concavity,
\[
 \frac1N\sum_{k<m}\left(\frac{F_k}{\log N}\right)^r
 \le \left(\frac mN\right)^{1-r}
 \left(\frac{mH_m}{N\log N}\right)^r
 \longrightarrow\delta.
\]

For \(k\ge m\), let \(b_k=c(k/N)^{1/(1-r)}\) for a fixed \(c>0\). The tangent-line inequality for the concave function \(t\mapsto t^r\) is
\[
 t^r\le rb_k^{r-1}t+(1-r)b_k^r\qquad(t\ge0).
\]
Its first term is controlled by the identity
\[
 \frac{i}{k(i-k)}=\frac1k+\frac1{i-k}
\]
and the estimate, uniform in probability vectors,
\[
\begin{aligned}
\sum_{k=m}^{N-1}\frac{F_k}{k}
 &=\sum_i u_i\sum_{k=m}^{\min\{N-1,i-1\}}\frac{i}{k(i-k)}\\
 &\le H_{N-1}-H_{m-1}+H_N.
\end{aligned}
\]
Indeed, the first reciprocal sum is at most \(H_{N-1}-H_{m-1}\), while the second runs through at most \(N\) consecutive positive reciprocal denominators and is at most \(H_N\). For fixed \(\delta\), division by \(\log N\) has limit at most one. Further,
\[
 \lim_{N\to\infty}\frac1N\sum_{k=m}^{N-1}
 (k/N)^{r/(1-r)}=\int_\delta^1 s^{r/(1-r)}\,ds\le 1-r.
\]
Thus, uniformly over all unit vectors,
\[
 \limsup_{N\to\infty}\frac{J_N}{(\log N)^r}
 \le \delta+rc^{r-1}+(1-r)^2c^r.
\]
The rightmost two terms attain their minimum at \(c=(1-r)^{-1}\), with minimum \((1-r)^{1-r}\). Let \(\delta\downarrow0\) to obtain the desired upper bound.

**Matching diffuse lower estimate.** Let \(f(s)=s^{r/(1-r)}/(1-r)\) for \(0\le s\le1\). Its integral over \([0,1]\) equals one, and the specified unit-vector family has coordinate energies \(u_{i,N}=f(i/N)/Z_N\), where \(Z_N=\sum_{i=1}^N f(i/N)\sim N\). For any fixed \(\delta\in(0,1/2)\), uniformly for integers \(\delta N\le k\le(1-\delta)N\),
\[
 \frac{F_k}{\log N}\longrightarrow\frac{k}{N}f(k/N).
\]
To verify the uniform assertion, write \(i=k+j\), so
\[
 F_k=\frac1{Z_N}\sum_{j=1}^{N-k}f((k+j)/N)
 +\frac{k}{Z_N}\sum_{j=1}^{N-k}\frac{f((k+j)/N)}j.
\]
The first term is uniformly bounded. Since \(f\) is uniformly continuous on \([0,1]\), split the second sum at \(j=\eta N\): for \(j\le\eta N\), replace \(f((k+j)/N)\) with \(f(k/N)\) at an error bounded by its modulus of continuity at \(\eta\) times \(H_{\lfloor\eta N\rfloor}\); for \(j>\eta N\), the harmonic sum is \(O_\eta(1)\). Divide by \(\log N\), take \(N\to\infty\), and then \(\eta\downarrow0\). Consequently,
\[
 \liminf_{N\to\infty}\frac{J_N}{(\log N)^r}
 \ge \int_\delta^{1-\delta}(sf(s))^r\,ds.
\]
Let \(\delta\downarrow0\). Direct integration gives
\[
 \int_0^1(sf(s))^r\,ds
 =(1-r)^{-r}\int_0^1s^{r/(1-r)}\,ds
 =(1-r)^{1-r}.
\]
This matches the upper bound and finishes the proof. Taking the \(1/q\)-power gives the theorem's displayed coefficient. To see why a single basis vector cannot be an asymptotic witness, take the unit vector whose sole nonzero energy is \(u_i=1\). Its averaged \(r\)-energy is
\[
\frac1N\sum_{0\le k<\min\{i,N\}}\left(\frac{i}{i-k}\right)^r.
\]
If \(i\le N\), this is at most \(N^{-1}i^r[1+i^{1-r}/(1-r)]\le1+1/(1-r)\); if \(i>N\), monotonicity of the individual summands in \(i\) bounds it by the case \(i=N\). Thus every normalized basis vector has uniformly bounded \(q\)-moment, while the optimal constant diverges.


## Verification

The key steps are analytic: the exact orbit/energy identity, the reciprocal-kernel bound uniform in every probability vector, the tangency optimization, and the uniform bulk harmonic approximation. No finite enumeration is used to infer the infinite limit. An accompanying standard-library computation checks the formula for the explicitly constructed unit vectors at several finite horizons and compares the normalized values with the proved limit; its checks are illustrative only.

## Relationship to prior work

Abbar, Arnold, and Coine analyze absolute Cesàro boundedness for weighted backward shifts, including the power-law example at the critical value \(\alpha=1/p\), and establish several boundary/non-boundedness criteria. Bernardes, Bonilla, and Pinto provide an exact reduction of the \(p\)-moment Cesàro bound for weighted shifts to single-coordinate tests. The present result is not a claim to rediscover boundary failure or the known sharp \(p\)-moment harmonic profile: it determines a strictly smaller, explicit leading coefficient for every fixed \(0<q<p\), and exhibits diffuse asymptotically sharp witnesses. A publicly indexed result describes an exact harmonic \(p\)-moment profile for an extremal weighted shift; the available summary does not establish that its operator is identical to the present critical shift, and it does not state the nonlinear lower-moment coefficient. Arnold's related 2026 self-improvement paper assumes absolute Cesàro boundedness when giving its logarithmic estimate; this assumption fails here. More extensive historical priority checking remains desirable.

## Limitations

The result concerns one canonical critical weight \(\omega_i=i^{-1/p}\) and one fixed pair \(p,q\), not arbitrary regularly varying weights or a uniform limit as \(q\uparrow p\). The asserted asymptotic gives the leading coefficient only; it does not classify all asymptotic extremizers, determine exact finite-horizon optimizers, or give a second-order term. The proof is an independent analytic derivation, not an external formal certification. Potential equivalent formulations in earlier nonlinear Hardy-operator literature are not excluded by search alone.

## References

1. A. Abbar, L. Arnold, and C. Coine, *On absolutely Cesàro bounded operators*, arXiv:2609.24601v1 (first public 2026-09-21), especially Theorem 3.4 and Example 3.10. https://arxiv.org/abs/2609.24601
2. L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1 (first public 2026-09-24), Sections 3–4. https://arxiv.org/html/2610.00271v1
3. N. C. Bernardes Jr., A. Bonilla, and J. V. A. Pinto, *On the dynamics of weighted composition operators*, arXiv:2506.04476v1 (first public 2025-06-04), especially Corollary 58. https://arxiv.org/html/2506.04476v1
