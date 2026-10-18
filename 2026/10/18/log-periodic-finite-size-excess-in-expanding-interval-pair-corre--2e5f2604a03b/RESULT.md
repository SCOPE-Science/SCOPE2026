# Log-periodic finite-size excess in expanding-interval pair correlations

## Finding
Fix an integer \(b\ge 2\) and a real \(s>0\). For \(N>s\), let \(r=s/N\), let \(T_b:[0,1)\to[0,1)\) be \(T_b(x)=bx\pmod 1\), and define the ordered, diagonal-free **Euclidean** pair-correlation statistic
\[
R_{N,b}(s;x)=\frac1N\sum_{0\le i\ne j<N}\mathbf1\bigl\{|T_b^i x-T_b^j x|\le r\bigr\}.
\]
Expectation below is for Lebesgue-uniform \(x\in[0,1)\). The benchmark from \(N\) independent uniform interval points is
\[
I_N=(N-1)(2r-r^2).
\]
For \(0<r<1\) and an integer \(B\ge2\), set \(u=Br\), \(v=\{u\}\), and
\[
p_B(r)=2r-r^2+\frac{Br(1-r)-v(1-v)}{B(B-1)}.
\]
The exact finite-sample law is
\[
\boxed{\quad \mathbb E R_{N,b}(s)=\frac2N\sum_{k=1}^{N-1}(N-k)p_{b^k}(r).\quad}
\]

Define \(F:(0,\infty)\to\mathbb R\) and a continuous, nonconstant, one-periodic function \(\Phi_b\) by
\[
F(u)=\frac{u-\{u\}(1-\{u\})}{u^2},\qquad
\Phi_b(t)=\sum_{j=1}^{\infty}F(b^{j-t})-t\quad(0\le t\le1),
\]
with periodic continuation. In particular \(\Phi_b(0)=\Phi_b(1)=1/(b-1)\) and \(\Phi_b'(0+)=-1\). As \(N\to\infty\) through integers with \(b,s\) fixed,
\[
\boxed{\quad
\frac{N^2}{2s^2}\bigl(\mathbb E R_{N,b}(s)-I_N\bigr)
=\log_b(N/s)+\Phi_b(\{\log_b(N/s)\})
+O_{b,s}\!\left(\frac{(\log N)^2}{N}\right).
\quad}
\]
Thus the mean excess over the exact independent-interval benchmark is of size \(2s^2\log_b(N/s)/N^2\), with an explicit nonvanishing oscillatory correction at its next scale.

## Assumptions and scope
The map is the integer-slope piecewise-linear expanding **interval** transformation, and differences in the statistic use ordinary absolute value, not shortest circular distance. The initial point has Lebesgue law, which is invariant under \(T_b\). Fix \(b\in\{2,3,\ldots\}\) and \(s\in(0,\infty)\) before sending \(N\to\infty\). The finite formula holds whenever the integer \(N\ge2\) obeys \(N>s\); no bound on the size of \(b^k\) is required. All pairs are ordered, and the diagonal is excluded. The periodic phase function is defined first on \([0,1]\), where its endpoint values coincide. No claim is made for a circular-distance statistic or a nonintegral expanding slope.

## Proof
**1. Exact one-lag collision probability.** By Lebesgue invariance, the law of \((T_b^i x,T_b^{i+k}x)\) is that of \((y,T_b^k y)\) with uniform \(y\). Put \(B=b^k\). The \(j\)-th affine branch is \(j/B\le y<(j+1)/B\) and has \(T_b^k y=By-j\). Its collision event is \(|(B-1)y-j|\le r\), whose interval length is
\[
\frac1{B-1}\left[\min\!\left(r,\frac jB\right)+\min\!\left(r,\frac{B-1-j}{B}\right)\right].
\]
Summing over \(j=0,\ldots,B-1\) gives, with \(m=\lfloor Br\rfloor\),
\[
\Pr\{|y-T_b^k y|\le r\}
=\frac2{B-1}\sum_{j=0}^{B-1}\min\!\left(r,\frac jB\right)
=\frac{m(m+1)/B+2(B-1-m)r}{B-1}.
\]
Algebra with \(Br=m+v\) gives precisely \(p_B(r)\). The probability is valid at branch endpoints because these form a null set. The ordered-pair identity follows by grouping both orientations of each index gap \(k\), of which there are \(N-k\).

**2. Separation from the independent benchmark.** Independent uniforms \(U,V\) on \([0,1]\) satisfy \(\Pr(|U-V|\le r)=2r-r^2\) for \(0<r<1\). Put
\[
\delta_B(r)=p_B(r)-(2r-r^2).
\]
Then \(\mathbb ER_{N,b}(s)-I_N=\frac2N\sum_{k=1}^{N-1}(N-k)\delta_{b^k}(r)\), so
\[
\frac{N^2}{2s^2}\bigl(\mathbb ER_{N,b}(s)-I_N\bigr)
=\sum_{k=1}^{N-1}\left(1-\frac{k}{N}\right)\frac{\delta_{b^k}(r)}{r^2}.
\]
For \(u=Br\) and \(v=\{u\}\), the exact scaled contribution is
\[
G_r(u)=\frac{\delta_B(r)}{r^2}
=\frac{u(1-r)-v(1-v)}{u(u-r)}.
\]
If \(u\le1\), branch counting gives \(p_B(r)=2r\), hence \(G_r(u)=1\). For \(u\ge1\), direct subtraction yields
\[
G_r(u)-F(u)=\frac{r\bigl[u-v(1-v)-u^2\bigr]}{u(u^2-ur)}.
\]
Once \(r\le1/2\), it follows that \(|G_r(u)-F(u)|\le2r/u\) for \(u\ge1\). Also \(0\le F(u)\le1/u\) in this range and \(F(u)=1\) for \(0<u\le1\).

**3. The logarithmic term and periodic phase.** For all sufficiently large \(N\), write
\[
L=\log_b(1/r),\qquad q=\lfloor L\rfloor,\qquad t=L-q\in[0,1).
\]
For every lag \(1\le k\le q\), the scaled contribution equals exactly one. For larger lags, write \(k=q+j\) so that \(b^k r=b^{j-t}>1\). The displayed bounds and a geometric series imply
\[
\sum_{k=1}^{N-1}\frac{\delta_{b^k}(r)}{r^2}
=q+\sum_{j=1}^{\infty}F(b^{j-t})+O_b(r+b^{-(N-q)}).
\]
The adjustment from the factors \(1-k/N\) costs at most
\[
\frac1N\sum_{k=1}^{q}k
+\frac{C_b}{N}\sum_{j\ge1}(q+j)b^{-(j-t)}
=O_b\!\left(\frac{(q+1)^2}{N}\right).
\]
Since \(q=L-t\), this establishes the stated expansion uniformly in the fractional phase.

**4. Nonconstancy and endpoint regularity.** On any interval between consecutive positive integers \(m\le u\le m+1\), the function \(F\) equals \(1-2m/u+m(m+1)/u^2\), and hence is continuous at integers. The series defining \(\Phi_b\) converges uniformly on \([0,1]\) because \(F(b^{j-t})\le b^{1-j}\). Its endpoint values are
\[
\Phi_b(0)=\sum_{j\ge1}b^{-j}=\frac1{b-1},\qquad
\Phi_b(1)=1+\sum_{j\ge1}b^{-j}-1=\frac1{b-1}.
\]
At an integer \(m\ge2\), the left derivative of \(F\) is zero. Therefore, as \(t\downarrow0\), each \(F(b^{j-t})\) has right derivative zero. Termwise differentiation is justified by the geometric majorant \(|\frac{d}{dt}F(b^{j-t})|\le C_b b^{-j}\) on each smooth subinterval. Consequently \(\Phi_b'(0+)=-1\), proving that the periodic correction is genuinely nonconstant.

## Verification
The standalone file `verify_pair_correlation.py` provides three exact-rational calculations of each branch probability, independently intersecting affine-branch intervals, summing clipped branch lengths, and evaluating the fractional-part expression. It reports agreement on 156 rational parameter cases. It also evaluates exact finite-sample means for \(b=2\), \(s=3\), and \(N\in\{50,100,200,400\}\); their normalized errors relative to the phase-corrected asymptotic decrease from approximately \(0.35819\) to \(0.09779\). A separate finite-series check confirms periodic endpoint agreement and nonconstancy for \(b\in\{2,3,5\}\). These checks corroborate, but do not replace, the general algebraic proof above. Execute `python verify_pair_correlation.py` in the directory containing the script; no third-party modules are required.

## Relationship to prior work
Baker and Todd's 2026 interval-map theorem establishes first-order almost-sure pair-correlation behavior under mixing and recurrence assumptions, but does not identify a sharp finite-\(N\) Euclidean expectation bias for the integer expanding family. Rudnick and Zaharescu's 1999 lacunary-sequence theorem treats the periodicized, circular-distance correlation; its mean is exactly the circle independent benchmark and therefore does not cover the endpoint-sensitive Euclidean excess. The published result *Sharp second-moment inflation for expanding circle-map pair correlations* gives a leading **variance** constant for the circular-distance statistic with zero mean excess, rather than the Euclidean first-moment law proved here. The distinction is in both the statistic (expectation versus variance) and the metric (interval versus circle); a first-order Poisson limit alone implies neither the logarithmic coefficient nor the nonconstant phase.

## Limitations
The result is an annealed finite-size mean statement, not a pointwise second-order law for typical orbits, a central limit theorem, or an optimal fluctuation bound. The correction is small compared with usual stochastic fluctuation scales. The constants in the remainder are not claimed uniform when \(b\) or \(s\) varies with \(N\). A further literature search could uncover earlier equivalent finite-size computations under lacunary-sequence or endpoint-recurrence terminology.

## References
1. S. Baker and M. Todd, *Pair correlation statistics for dynamical systems*, arXiv:2606.17880 (first public 16 June 2026), especially Introduction, the proof of the one-orbit limit, and the references to earlier lacunary results. https://arxiv.org/abs/2606.17880
2. Z. Rudnick and A. Zaharescu, *The distribution of spacings between fractional parts of lacunary sequences*, arXiv:math/9912103 (1999), Sections 1, 3, and 4. https://arxiv.org/abs/math/9912103
3. *Sharp second-moment inflation for expanding circle-map pair correlations*, publicly indexed mathematical result, record d5c688b954c6 (2026), specifically its finding, proof, and limitations.
