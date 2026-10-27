# Zero condensation and a single theta outlier for two-step radial Bergman kernels

## Finding
Fix real \(0<q<1\) and \(1<\tau<q^{-1}\). For each integer \(N\ge1\), define a positive two-level radial weight on the unit disk by
\[
\omega_N(z)=1+\tau q^{-(N+1)}\mathbf1_{\{|z|^2\le q\}}.
\]
Use area measure \(dA/\pi\). The reproducing kernel is \(K_N(z,w)=\mathcal K_N(z\overline w)\), where
\[
\mathcal K_N(s)=\sum_{n=0}^{\infty}\frac{(n+1)s^n}{1+\tau q^{n-N}}\quad(|s|<1).
\]
For **every fixed** \(r\in(q,1)\) with \(r\ne\tau^{-1}\), there is \(N_0(q,\tau,r)\) such that, for all integers \(N\ge N_0\), the number of zeros of \(\mathcal K_N\) in \(|s|<r\), with multiplicities, is **exactly**
\[
\boxed{N+\mathbf1_{\{r>\tau^{-1}\}}.}
\]
Moreover there is a unique simple zero \(s_N\) in every sufficiently small fixed disk about \(-\tau^{-1}\), for all sufficiently large \(N\), and \(s_N\to-\tau^{-1}\). For each sufficiently small fixed \(\varepsilon>0\) (in particular, \(q+\varepsilon<\tau^{-1}\)), exactly \(N\) zeros lie in \(q-\varepsilon<|s|<q+\varepsilon\), eventually; none lie in \(|s|\le q-\varepsilon\). Thus \(N\) zeros condense on the radial jump circle while one separated outlier converges to an explicitly movable negative-real location.

## Assumptions and scope
The pair \((q,\tau)\) is fixed as \(N\to\infty\). The scalar variable \(s=z\overline w\) ranges over the open unit disk, and a zero at \(s\) is realized by some \(z,w\in\mathbb D\). The circle \(|s|=\tau^{-1}\) is excluded from the exact-radius count. The assertion is eventually exact for each fixed radius, **not** a uniform count for radii depending on \(N\), and makes no claim about zeros near \(|s|=1\) or an exact total number in the whole disk.

## Proof
**Step 1: moments and kernel.** Orthogonality of monomials for any radial weight, followed by \(u=|z|^2\), gives
\[
\|z^n\|_{L^2(\omega_N dA/\pi)}^2
=\int_0^1u^n[1+\tau q^{-(N+1)}\mathbf1_{u\le q}]\,du
=\frac{1+\tau q^{n-N}}{n+1}.
\]
These are positive. Taking reciprocals yields the displayed kernel series, converging absolutely and locally uniformly for \(|s|<1\).

**Step 2: a bilateral limit.** For \(q<|s|<1\), set
\[
F_N(s)=\frac{\mathcal K_N(s)}{(N+1)s^N}
=\sum_{k=-N}^{\infty}\frac{1+k/(N+1)}{1+\tau q^k}s^k.
\]
On each compact subannulus \(q<r_0\le|s|\le r_1<1\), the positive-index summands are bounded by \((1+k)r_1^k\). For \(k=-\ell<0\), using \((1+\tau q^{-\ell})^{-1}\le\tau^{-1}q^\ell\) and \(0\le1-\ell/(N+1)\le1\) when \(\ell\le N\), the absolute summands are bounded by \(\tau^{-1}(q/r_0)^\ell\). Therefore \(F_N\) converges locally uniformly on that annulus to the bilateral meromorphic Laurent series
\[
H_{q,\tau}(s)=\sum_{k\in\mathbb Z}\frac{s^k}{1+\tau q^k}.
\]

**Step 3: explicit zero structure.** Write \((a;q)_\infty=\prod_{j\ge0}(1-aq^j)\). The classical Ramanujan bilateral summation \({}_1\psi_1\) [R4], specialized to \(a=-\tau,b=-\tau q,z=s\), together with \((a;q)_k/(aq;q)_k=(1-a)/(1-aq^k)\), gives
\[
H_{q,\tau}(s)=
\frac{(q;q)_\infty^2(-\tau s;q)_\infty(-q/(\tau s);q)_\infty}{(-\tau;q)_\infty(-q/\tau;q)_\infty(s;q)_\infty(q/s;q)_\infty}.
\]
All denominator factors are nonzero for \(q<|s|<1\). The factor \((-q/(\tau s);q)_\infty\) has zeros only at \(s=-q^{j+1}/\tau\), whose moduli are \(<q\). The factor \((-\tau s;q)_\infty\) has zeros at \(s=-q^{-j}/\tau\), \(j\ge0\). Since \(1<\tau<1/q\), exactly one belongs to \(q<|s|<1\), namely the **simple** zero \(s_*=-1/\tau\). Hence \(H\) has no other zeros in this annulus.

**Step 4: winding and exact counts.** For \(q<r<1\), \(r\ne1/\tau\), \(H\) is nonvanishing on the circle \(|s|=r\). Its winding about zero equals \(\mathbf1_{\{r>1/\tau\}}\): all factors \(1+a/s\) with \(|a|<q<r\) have zero winding; all factors \(1-as\) with \(|a|\le1\) have no enclosed zero; exactly the \(j=0\) factor \(1+\tau s\) changes winding when \(r\) passes \(1/\tau\). Absolute uniform product convergence permits the factorwise count. By the preceding locally uniform convergence, \(F_N\) is nonzero on the circle and has the same winding for all large \(N\). On \(|s|=r\), \(\mathcal K_N(s)=(N+1)s^NF_N(s)\), so the argument principle gives the **exact number \(N+\mathbf1_{r>1/\tau}\)**. Hurwitz's theorem on a small disk around the sole simple zero of \(H\) gives a unique simple \(s_N\to s_*\).

**Step 5: excluding interior zeros.** For \(|s|<q\), one has
\[
\tau q^{-(N+1)}\mathcal K_N(s)\longrightarrow
\sum_{n\ge0}(n+1)q^{-(n+1)}s^n
=\frac{q^{-1}}{(1-s/q)^2},
\]
locally uniformly: each coefficient converges and is bounded by \((n+1)q^{-(n+1)}\). The limit is zero-free on \(|s|<q\), so every compact disk \(|s|\le q-\varepsilon\) is eventually zero-free. Choosing any \(q<q+\varepsilon<\tau^{-1}\) in Step 4 gives exactly \(N\) zeros within \(|s|<q+\varepsilon\), hence all \(N\) lie in the announced thin annulus. This completes the proof.

## Verification
The accompanying `check.py` computes weighted monomial norms and inverse coefficients independently, compares the bilateral series to Ramanujan's product at three nonreal points using 80-digit arithmetic, and performs Fourier-winding contour checks in nine finite parameter configurations on both sides of the outlier threshold. It reports 69 passing finite consistency assertions. The infinite-\(N\) statements follow from the preceding dominated-convergence, product-zero, Hurwitz, and argument-principle proof, **not** from finite computations.

## Relationship to prior work
Perälä [R1] studies weighted disk Bergman kernels with zeros and supplies general existence constructions; the present result concerns a specific positive **two-level radial** weight and gives eventual **exact linear zero counts** at each fixed interior radius, a sharp jump by one across the outlier, and a limiting q-hypergeometric formula. Boudreaux [R2] develops other zero-producing/equivalent-weight examples; the present family and radial-condensation classification are not among the statements inspected there. Zeytuncu [R3] concerns radial weighted Bergman kernels and zeros; its available abstract was compared, but a full-text implication comparison was not completed. The underlying bilateral summation identity [R4] is classical and **not** claimed as new. A stronger previously published radial-kernel zero theorem could subsume the conclusion; priority is not independently established.

## Limitations
The limiting bilateral-product identity is classical; novelty is claimed only for its application to this explicit changing sequence of positive weighted Bergman kernels and the exact zero-count/outlier law. The full-disk zero count, uniformity in moving radii, behavior as \(q\) or \(\tau\) vary with \(N\), and general piecewise radial weights are not determined. The source comparison is best knowledge and not an independent priority audit.

## References
- [R1] A. Perälä, *Vanishing Bergman kernels on the disk*, arXiv:1703.05976 (first publicly posted 2017-03-17), https://arxiv.org/abs/1703.05976.
- [R2] B. J. Boudreaux, *Equivalent Bergman Spaces With Inequivalent Weights*, arXiv:1802.01099 (2018), https://arxiv.org/abs/1802.01099.
- [R3] Y. Zeytuncu, *Weighted Bergman projections and kernels: Lp regularity and zeros*, arXiv:1009.2806 (2010), https://arxiv.org/abs/1009.2806.
- [R4] NIST Digital Library of Mathematical Functions, §17.8(ii), Ramanujan's bilateral summation (equation 17.8.2), https://dlmf.nist.gov/17.8.
