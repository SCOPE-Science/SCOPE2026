# Sharp logarithmic sensor-density frontier for Bergman shift orbit frames

## Finding
For every \(\alpha>-1\), put \(\beta=\alpha+1>0\) and let \(T=M_z\) act on the weighted Bergman Hilbert space \(A^2_\alpha(\mathbb D)\). For every strictly increasing sequence of nonnegative integers \(0=s_0<s_1<\cdots\), form the unit-norm monomial generators \(u_j=z^{s_j}/\|z^{s_j}\|_{A^2_\alpha}\) and the whole forward-orbit family \(\mathcal F_S=\{T^ku_j:j,k\ge0\}\). Put
\[
 h_m=\frac{\Gamma(m+\beta+1)}{\Gamma(\beta+1)\Gamma(m+1)},\qquad
 \Lambda_m=\frac{\sum_{s_j\le m}h_{s_j}}{h_m}.
\]
Then \(\mathcal F_S\) is a frame precisely when \(\inf_m\Lambda_m>0\) and \(\sup_m\Lambda_m<\infty\), and its optimal frame bounds are these two extremal values. For every such frame let
\[
 A_\infty=\liminf_{m\to\infty}\Lambda_m,\qquad
 B_\infty=\limsup_{m\to\infty}\Lambda_m,\qquad
 \kappa_\infty=B_\infty/A_\infty,
\]
and let \(N_S(R)=\#\{j:s_j\le R\}\). Necessarily \(\kappa_\infty>1\), and the sharp asymptotic density inequality is
\[
 \boxed{\displaystyle \liminf_{R\to\infty}\frac{N_S(R)}{\log R}
 \ge\frac{\beta}{\log\kappa_\infty}.}
\]
For each prescribed \(\kappa>1\), equality is attained by a geometric sequence of generator degrees \(s_0=0\) and \(s_j=\lceil r^{j+J}\rceil\) for \(j\ge1\), where \(r=\kappa^{1/\beta}\) and \(J\) is any sufficiently large integer ensuring strict increase. For these generators,
\[
 A_\infty=\frac1{r^\beta-1},\quad
 B_\infty=\frac{r^\beta}{r^\beta-1},\quad
 \kappa_\infty=r^\beta,\quad
 \lim_{R\to\infty}\frac{N_S(R)}{\log R}=\frac1{\log r}.
\]
As a fully explicit benchmark, when \(\alpha=0\) and \(s_j=2^j-1\), the optimal **global** frame bounds are \(A=1\) and \(B=2\), with \(N_S(R)=\lfloor\log_2(R+1)\rfloor+1\). This realizes the optimal density \(1/\log2\) at asymptotic condition ratio \(2\).

## Assumptions and scope
The normalized Bergman norm is
\[
 \|f\|_{A^2_\alpha}^2=\frac{\alpha+1}{\pi}\int_{\mathbb D}|f(z)|^2(1-|z|^2)^\alpha\,dA(z),
 \qquad \alpha>-1.
\]
The sequence of generator degrees consists of distinct integers, includes degree zero, and is infinite. Exactly one generator is placed at each selected degree, and each seed has norm one **before** applying powers of \(T\); the orbit vectors themselves are not independently renormalized. An orbit family is a Hilbert frame when its analysis energy lies between fixed positive constants times the squared input norm for every input. The asymptotic constants \(A_\infty\) and \(B_\infty\) describe the limiting high-degree diagonal entries and need not coincide with the global frame bounds. The logarithmic lower density is taken over real \(R\to\infty\), with \(R>1\).

## Proof
**Monomial normalization and exact frame spectrum.** Polar integration with the above normalization gives
\[
 \|z^m\|^2=\frac{\Gamma(\alpha+2)\Gamma(m+1)}{\Gamma(m+\alpha+2)}=h_m^{-1}.
\]
Thus \(e_m=\sqrt{h_m}\,z^m\) is an orthonormal basis and \(u_j=e_{s_j}\). For each \(j,k\ge0\),
\[
 T^ku_j=\sqrt{\frac{h_{s_j}}{h_{s_j+k}}}\,e_{s_j+k}.
\]
Every individual orbit vector therefore belongs to exactly one monomial coordinate. For any polynomial \(f=\sum_m c_m e_m\), grouping all vectors at the same output degree yields the exact nonnegative identity
\[
 \sum_{j,k\ge0}|\langle f,T^ku_j\rangle|^2
 =\sum_{m\ge0}\Lambda_m|c_m|^2.
\]
The identity extends in \([0,\infty]\) to arbitrary \(f\) by Tonelli and orthogonal expansion. Since the monomial basis is complete and \(s_0=0\), each \(\Lambda_m>0\). Consequently the family is a frame if and only if the displayed diagonal sequence has a positive infimum and finite supremum. Choosing \(f=e_m\) shows the bounds are optimal.

**Spectral jumps and necessity of a density.** Write \(s_j-1\) and \(s_j\) for the two adjacent degrees at each insertion, and note that \(h_m\) strictly increases because \(h_{m+1}/h_m=(m+\beta+1)/(m+1)\). Hence
\[
 \Lambda_{s_j}
 =1+\frac{h_{s_j-1}}{h_{s_j}}\Lambda_{s_j-1}.
\]
Every frame has bounded \(\Lambda_m\), and \(h_{s_j-1}/h_{s_j}\to1\), so
\(\Lambda_{s_j}-\Lambda_{s_j-1}\to1\). This forces
\(B_\infty-A_\infty\ge1\), and therefore \(\kappa_\infty>1\).

Between successive insertion degrees, the numerator of \(\Lambda_m\) is constant and the denominator is increasing. Its exact endpoint ratio is
\[
 \frac{\Lambda_{s_j}}{\Lambda_{s_{j+1}-1}}
 =\frac{h_{s_{j+1}-1}}{h_{s_j}}.
\]
Let \(\varepsilon>0\) be small enough that \(A_\infty-\varepsilon>0\). For all sufficiently large \(j\), both endpoint frame coefficients lie between \(A_\infty-\varepsilon\) and \(B_\infty+\varepsilon\); hence
\[
 \frac{h_{s_{j+1}-1}}{h_{s_j}}
 \le\frac{B_\infty+\varepsilon}{A_\infty-\varepsilon}.
\]
The gamma ratio formula implies \(h_m\sim m^\beta/\Gamma(\beta+1)\). Consequently, whenever \(a_j\to\infty\), \(b_j\ge a_j\), and \(h_{b_j}/h_{a_j}\) stays bounded, the ratio \(b_j/a_j\) stays bounded and
\(h_{b_j}/h_{a_j}=(b_j/a_j)^\beta(1+o(1))\). Applying this with \(a_j=s_j\), \(b_j=s_{j+1}-1\), and noting that adding one to \(b_j\) is negligible since \(s_{j+1}\to\infty\), gives
\[
 \limsup_{j\to\infty}\frac{s_{j+1}}{s_j}
 \le\left(\frac{B_\infty}{A_\infty}\right)^{1/\beta}
 =\kappa_\infty^{1/\beta}.
\]
Fix any \(q>\kappa_\infty^{1/\beta}\). For all large \(j\), \(s_{j+1}\le q s_j\), and so \(s_j\le Cq^j\) for a constant \(C\). Therefore all indices \(j\le(\log R-\log C)/\log q\) correspond to degrees at most \(R\), up to an inessential fixed initial index. It follows that
\(\liminf_{R\to\infty}N_S(R)/\log R\ge1/\log q\). Taking \(q\downarrow\kappa_\infty^{1/\beta}\) proves the asserted density inequality.

**Geometric attainment.** Set \(r=\kappa^{1/\beta}>1\); choose \(J\) sufficiently large and define \(s_0=0\), \(s_j=\lceil r^{j+J}\rceil\) for \(j\ge1\). Then \(s_j\sim r^{j+J}\), and
\(h_{s_j}\sim r^{\beta(j+J)}/\Gamma(\beta+1)\). Summing the resulting asymptotic geometric sequence shows
\[
 \lim_{j\to\infty}\Lambda_{s_j}
 =\lim_{j\to\infty}\frac{\sum_{i=0}^{j}h_{s_i}}{h_{s_j}}
 =\frac1{1-r^{-\beta}}=\frac{r^\beta}{r^\beta-1},
\]
whereas
\[
 \lim_{j\to\infty}\Lambda_{s_{j+1}-1}
 =\frac1{r^\beta-1}.
\]
Every \(\Lambda_m\) between two generator degrees decreases monotonically; these two endpoint limits therefore equal \(B_\infty\) and \(A_\infty\), respectively. Since the lower limit is strictly positive and the upper limit is finite, the family is a frame globally (finitely many initial degrees cause no obstruction). Finally \(s_j\sim r^{j+J}\) gives
\(N_S(R)=\log R/\log r+O(1)\), proving sharpness.

**Exact dyadic case.** For \(\alpha=0\), one has \(h_m=m+1\), and with \(s_j=2^j-1\), whenever \(2^J\le m+1<2^{J+1}\) the selected monomials have weight sum \(\sum_{j=0}^{J}2^j=2^{J+1}-1\). Hence
\[
 \Lambda_m=\frac{2^{J+1}-1}{m+1}.
\]
These values are at least one and strictly less than two; both limits one and two occur along degrees immediately before/at new generators. Thus the optimal global frame bounds are exactly \(1\) and \(2\), while the number of seeds of degree at most \(R\) is \(\lfloor\log_2(R+1)\rfloor+1\).

## Verification
The accompanying standard-library script `bergman_orbit_checker.py` independently recomputes finite-dimensional frame diagonals by (i) accumulating weights at selected degrees and (ii) explicitly summing all finite orbit vectors. It tests twelve combinations of Bergman weight and geometric spacing and checks all 4,095 dyadic coordinates through degree 4,094 against their closed formula. Command: `python bergman_orbit_checker.py`. The checks are finite diagnostics only; infinite-dimensional assertions, sharpness, and asymptotic limits are proved above.

## Relationship to prior work
Aguilera and Carando (arXiv:2606.00912, first publicly submitted May 30, 2026) characterize multiplication-operator orbit frames in Hardy spaces and finite-generator possibilities for finite Blaschke symbols. Their Hardy monomials have constant norm, unlike the strictly growing Bergman reciprocal monomial norms controlling the present density barrier; their results do not determine generator-degree density or an asymptotic conditioning frontier for \(M_z\) on weighted Bergman spaces.

Aguilera, Cabrelli, Negreira, and Paternostro (arXiv:2506.00567) determine general dynamical-frame indices, addressing the *cardinality* of possible generating families, not an optimal quantitative growth law for unit-norm monomial seeds. Gallardo-Gutiérrez and Partington (arXiv:2605.29671) analyze other orbit-frame constructions for multiplication operators, Jordan-type operators, and Carleson frames, without the stated Bergman diagonal density optimization. The present quantitative theorem concerns a restricted but canonical generator class; no claim is made to optimize over arbitrary nonmonomial generators.

## Limitations
All assertions require \(\alpha>-1\), strictly increasing generator degrees starting at zero, and unit-norm **initial** monomial sensors with all unnormalized forward iterates. The logarithmic bound need not hold for arbitrary linear-combination generators or other normalizations. The optimal global condition number may be influenced by finitely many initial degrees; the theorem optimizes the high-degree ratio \(\kappa_\infty\) instead. A general published theory of weighted-shift orbit-frame sparsity could potentially imply the result through a reduction not identified in the inspected sources; publication priority requires independent evaluation. 

## References
1. A. Aguilera and D. Carando, *Frames of orbits of multiplication operators on Hardy spaces*, arXiv:2606.00912v1 (first public date 2026-05-30), https://arxiv.org/abs/2606.00912 .
2. A. Aguilera, C. Cabrelli, F. Negreira, and V. Paternostro, *Optimal Dynamical Frames*, arXiv:2506.00567 (first public date 2025-05-31), https://arxiv.org/abs/2506.00567 .
3. E. A. Gallardo-Gutiérrez and J. R. Partington, *Frame constructions associated with operator orbits*, arXiv:2605.29671 (first public date 2026-05-28), https://arxiv.org/abs/2605.29671 .
