# Degree-doubling logarithmic isometric defects of finite Blaschke harmonic Bergman Toeplitz operators

## Finding

For every finite Blaschke product \(B\) of degree \(m\ge1\), compression of multiplication by \(B\) to the complex harmonic Bergman space has a positive compact isometric defect \(D_B\) whose singular-value sums satisfy
\[
\lim_{N\to\infty}\frac{1}{\log N}\sum_{j=1}^N s_j(D_B)=2m.
\]
It belongs to \(\mathcal S_p\) for every \(p>1\), but not \(\mathcal S_1\). In particular its Dixmier trace is uniquely \(2m\). The integer coefficient counts both analytic and anti-analytic harmonic tails and depends only on the degree of \(B\), not the locations of its zeros.

## Assumptions and scope

Let \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), with normalized area \(dA=dx\,dy/\pi\). The Hilbert space \(H=L_h^2(\mathbb D,dA)\) consists of complex-valued square-integrable harmonic functions. Denote the orthogonal harmonic projection by \(P_h\), and define \(T_B=P_h M_B|_H\). Let
\[
B(z)=\xi\prod_{\nu=1}^{m}\frac{z-a_\nu}{1-\overline{a_\nu}z},\qquad |\xi|=1,\quad a_\nu\in\mathbb D,\quad m\ge1.
\]
Write \(D_B=I_H-T_B^*T_B\). For any positive compact operator \(K\), write \(s_1(K)\ge s_2(K)\ge\cdots\) for eigenvalues with multiplicity. A Dixmier trace of a positive weak-trace-class operator is normalized using \(\sum_{j\le N}s_j/\log(N+1)\). No statement concerns unrestricted inner functions, individual asymptotics of \(s_N(D_B)\), or arbitrary weighted Bergman spaces.

## Proof

**1. Positive compression plus a trace-class correction.** Set \(h=1-|B|^2\ge0\), \(A=P_hM_h|_H\), and \(H_B=(I-P_h)M_B|_H\). Orthogonal decomposition of \(M_B f\) gives, for every \(f\in H\),
\[
\langle D_Bf,f\rangle=\int_{\mathbb D}(1-|B|^2)|f|^2\,dA+\|H_Bf\|_2^2,
\qquad D_B=A+H_B^*H_B.
\]
Both terms are positive. We prove \(H_B\) is Hilbert–Schmidt. The normalized orthonormal basis of \(H\) is \(e_0=1\) and \(e_{\pm j}=\sqrt{j+1}\,z^j,\sqrt{j+1}\,\overline z^j\), respectively, for \(j\ge1\). For a monomial symbol \(z^q\), \(q\ge1\), the Hankel term vanishes on the analytic half. For its anti-analytic input \(e_{-j}\), orthogonality of angular frequencies gives
\[
\|H_{z^q}e_{-j}\|_2^2=
\begin{cases}
\displaystyle\frac{j+1}{j+q+1}-\frac{(j+1)(q-j+1)}{(q+1)^2},&1\le j<q,\\[5pt]
\displaystyle\frac{q^2}{(j+1)(j+q+1)},&j\ge q.
\end{cases}
\]
The first \(q-1\) summands lie in \([0,1]\); the tail has sum at most \(q\), since \(\sum_{j\ge q}q^2/((j+1)(j+q+1))=q\sum_{k=q+1}^{2q}1/k\le q\). Thus \(\|H_{z^q}\|_{\mathcal S_2}^2\le2q\). A finite Blaschke product extends holomorphically beyond the closed disk, hence has Taylor coefficients \(b_q\) with \(\sum_{q\ge1}|b_q|\sqrt q<\infty\). The Hilbert–Schmidt triangle inequality proves \(H_B=\sum_{q\ge1}b_qH_{z^q}\in\mathcal S_2\), and therefore \(R=H_B^*H_B\in\mathcal S_1\).

**2. Weak-trace estimate for the positive Toeplitz term.** Smooth extension and unit boundary modulus imply \(0\le h(z)\le C_B(1-|z|^2)\). Consequently, in the operator order,
\[
0\le A\le C_B\,P_hM_{1-|z|^2}|_H.
\]
The right-hand operator is diagonal in the displayed basis, with eigenvalues \(1/(|j|+2)\), counting both signs and the constant. Compactness and the min–max principle imply \(s_N(A)=O(N^{-1})\), and in particular \(A\in\mathcal S_p\) for all \(p>1\).

**3. Boundary winding fixes the diagonal trace.** For \(\zeta=e^{it}\), the radial boundary expansion is uniform:
\[
1-|B(r\zeta)|^2=2(1-r)g(t)+O((1-r)^2),\qquad
 g(t)=|B'(e^{it})|=\sum_{\nu=1}^m\frac{1-|a_\nu|^2}{|e^{it}-a_\nu|^2}.
\]
Each Poisson kernel has circular mean one, so \((2\pi)^{-1}\int_0^{2\pi}g(t)\,dt=m\). The radial angular mean therefore satisfies \(\overline h(r)=2m(1-r)+O((1-r)^2)\). For either sign of \(j\ge1\),
\[
\langle Ae_{\pm j},e_{\pm j}\rangle
=2(j+1)\int_0^1r^{2j+1}\overline h(r)\,dr
=\frac{m}{j+1}+O((j+1)^{-2}).
\]
Indeed, \(2(j+1)\int_0^1r^{2j+1}(1-r)\,dr=1/(2j+3)\), giving the displayed leading term after multiplication by \(2m\). Let \(Q_M\) project onto the first \(M\) vectors ordered \(e_0,e_1,e_{-1},e_2,e_{-2},\ldots\). Summing both diagonal tails yields
\[
\operatorname{Tr}(Q_M A Q_M)=2m\log M+O(1).
\]

**4. Exact logarithmic singular-sum coefficient without invoking a spectral asymptotics theorem.** Let \(S_N(A)=\sum_{j=1}^Ns_j(A)\). The Ky Fan maximum principle gives the lower estimate \(S_N(A)\ge\operatorname{Tr}(Q_N A Q_N)=2m\log N+O(1)\). For the upper bound, take any rank-\(N\) orthogonal projection \(P\) and put \(X=A^{1/2}PA^{1/2}\). Then \(0\le X\le A\), \(\operatorname{rank}(X)\le N\), and \(\operatorname{Tr}(PA)=\operatorname{Tr}(X)\). Splitting the trace along \(Q_M\oplus(I-Q_M)\), and using both positivity and the rank bound, gives
\[
\operatorname{Tr}(X)\le\operatorname{Tr}(Q_M A Q_M)+N\|(I-Q_M)A(I-Q_M)\|.
\]
The operator-order estimate in step 2 gives \(\|(I-Q_M)A(I-Q_M)\|\le C'_B/M\). Take \(M=\lceil N\log N\rceil\) for \(N\ge3\). Uniformly in \(P\),
\[
\operatorname{Tr}(PA)\le2m\log N+O(\log\log N)+O(1).
\]
The supremum over all rank-\(N\) projections proves \(\lim_{N\to\infty}S_N(A)/\log N=2m\).

**5. Trace-class invariance and endpoints.** Since \(0\le A\le D_B=A+R\) with \(R\ge0\) trace class, Ky Fan sums obey
\[
S_N(A)\le S_N(D_B)\le S_N(A)+\operatorname{Tr}(R).
\]
Therefore \(S_N(D_B)/\log N\to2m\). Positive logarithmic divergence excludes trace class for \(m\ge1\). The compactness and Schatten membership from step 2, together with \(R\in\mathcal S_1\), give the other claims. The ordinary limit of normalized singular sums forces every Dixmier trace, independently of any generalized limiting functional, to equal \(2m\).

## Verification

The standalone Python standard-library file `check.py` carries out finite checks of the exact monomial Hankel-residual coefficients, the diagonal monomial defect weights, and angular means, derivative integrals and asymptotic normalized diagonal coefficients for explicit non-monomial products \(B(z)=(z^m-a)/(1-az^m)\) with selected degrees and parameters. It reports 22425 passing finite assertions when run as `python check.py`. These tests are supplementary and are not used to deduce any infinite-dimensional or all-degree statement. The analytical verification is supplied by the preceding five steps.

## Relationship to prior work

Huang–Wang–Zhao (2026) establish a spectral description for harmonic Bergman Toeplitz operators with polynomial analytic symbols, including Weyl-type properties; their analysis does not supply the positive non-isometry defect or its degree-dependent logarithmic coefficient for rational inner symbols. Choe–Koo–Lee (2008) prove general Schatten criteria for positive harmonic Bergman Toeplitz operators, which can locate integrability classes but are not an exact coefficient for the *Toeplitz isometric defect*. Engliš–Guo–Zhang (2007) calculate Dixmier traces for analytic Bergman Toeplitz/Hankel operator settings; this relates to an analytic contribution but does not establish the anti-analytic contribution or trace-class reduction on complex harmonic Bergman space. El-Fallah–El Ibbaoui (2021) give trace/spectral comparisons for positive Bergman Toeplitz operators rather than this exact harmonic Blaschke-defect constant. Lv (2012/2013) provides harmonic Schatten–Herz membership criteria; only an abstract was available for direct comparison, leaving some residual priority uncertainty.

## Limitations

No pointwise asymptotic \(s_N(D_B)\sim c/N\) is asserted; only logarithmically normalized Ky Fan sums are proved. The theorem requires finite Blaschke products on the normalized, unweighted complex harmonic Bergman space. Its originality conclusion is a best-knowledge comparison, not a formal proof that every earlier equivalent formulation has been excluded. No independent mathematical audit or publication-priority determination has been performed.

## References

1. M. Huang, J. Wang, X. Zhao, *The spectral structure of Toeplitz operators with polynomial symbols on the harmonic Bergman space* (2026), arXiv:2610.09638, first submitted October 7, 2026, https://arxiv.org/abs/2610.09638.
2. B. R. Choe, H. Koo, Y. J. Lee, *Positive Schatten class Toeplitz operators on the ball*, Studia Math. 189 (2008), 65–90, doi:10.4064/sm189-1-6.
3. M. Engliš, K. Guo, G. Zhang, *Toeplitz and Hankel operators and Dixmier traces on the unit ball of \(\mathbb C^n\)* (2007), arXiv:0707.2025, https://arxiv.org/abs/0707.2025.
4. O. El-Fallah, M. El Ibbaoui, *Trace estimates of Toeplitz operators on Bergman spaces and applications to composition operators* (2021), arXiv:2101.12268, https://arxiv.org/abs/2101.12268.
5. X. Lv and Z. Hu, *Schatten-Herz class Toeplitz operators on harmonic Bergman spaces of smooth domains*, Math. Nachr. 286 (2013), 248–259, doi:10.1002/mana.201100062, online 2012.
