# Sharp Cesàro Lyapunov oscillation and logarithmic regularization on wandering rectangles

## Finding

The two-dimensional piecewise expanding maps of Nakano, Soma and Yamamoto (2022) admit positive-Lebesgue-measure wandering rectangles on which ordinary finite-time Lyapunov exponents have nontrivial accumulation intervals. For either coordinate-axis tangent vector, their *arithmetic time averages* of finite-time Lyapunov exponents likewise have a nondegenerate, but strictly narrower, accumulation interval. Its exact endpoints, intermediate geometric-time profile and a contrasting convergent logarithmic average are determined below.

Fix the notation and hypotheses of the next section. Put
\[
c=\frac{\log\lambda_1+\log\lambda_2}{2},\qquad d=\frac{\log\lambda_1-\log\lambda_2}{2}>0,
\]
\[
D_\gamma=\frac{\gamma-1}{\gamma+1}-\frac{2\gamma\log\gamma}{(\gamma+1)^2},\qquad
R_\gamma=\frac{2\gamma^{\gamma/(\gamma+1)}}{\gamma+1}-1.
\]
The constants satisfy \(0<D_\gamma<R_\gamma<(\gamma-1)/(\gamma+1)\). For either \(v=e_1\) or \(v=e_2\), define
\[
L_n(x,v)=\frac{\log\|DF^n(x)v\|}{n},\qquad
B_N(x,v)=\frac1N\sum_{n=1}^NL_n(x,v).
\]
**Theorem.** For every \(x\) in the full-Lebesgue-measure set \(R(0,m)'\) of the paper's wandering rectangle and each coordinate axis \(v\in\{e_1,e_2\}\),
\[
\omega\big((B_N(x,v))_{N\ge1}\big)
=\big[c-dR_\gamma,\ c+dR_\gamma\big].
\]
The axis exponents themselves have the larger accumulation interval \([c-d(\gamma-1)/(\gamma+1),\,c+d(\gamma-1)/(\gamma+1)]\), proved in the source paper. Thus arithmetic Cesàro smoothing narrows but **does not remove** the observable Lyapunov irregularity.

More precisely, set \(T_j=\gamma^m(\gamma^j-1)/(\gamma-1)\) and
\[
H_\gamma(z)=\frac{D_\gamma-1+z+\frac{2}{\gamma+1}\log(1/z)}{z},
\qquad \frac1\gamma\le z\le1.
\]
Uniformly on that entire interval as \(j\to\infty\),
\[
B_{\lfloor zT_j\rfloor}(x,e_1)
=c+(-1)^{j-1}d H_\gamma(z)+o(1),
\]
with the opposite sign of the correction for \(e_2\). In particular \(B_{T_j}(x,e_1)=c+(-1)^{j-1}dD_\gamma+o(1)\). The profile's unique minimum occurs at \(z_*=\gamma^{-\gamma/(\gamma+1)}\), and \(H_\gamma(z_*)=-R_\gamma\). The minimum is what enlarges the final Cesàro cluster range beyond the two block-end values.

A different averaging scheme *does* restore convergence:
\[
Q_N(x,v)=\frac{\displaystyle\sum_{n=1}^N L_n(x,v)/n}
{\displaystyle\sum_{n=1}^N1/n}
=c+O\big((\log N)^{-1}\big),\qquad N\to\infty.
\]
The logarithmic average tends to \(c\) along both coordinate axes.

## Assumptions and scope

Use the published family \(F=F_\sigma:D\longrightarrow D\), \(D=(0,1)\times(-1,1)\), from Nakano--Soma--Yamamoto, arXiv:2206.09508v1, Section 2, equations (2.2)--(2.5), and Section 3. Explicitly, \(r\ge1\) is an integer, \(\gamma>r\) is an integer, \(0<\varepsilon_2<\varepsilon_1<\gamma^{-3}(2-r^{-1})^2\log2\), \(\lambda_i=e^{\varepsilon_i}\), and \(\sigma=1-\varepsilon_2/\varepsilon_1\). Choose the sufficiently large integer \(m>M\) for which the source constructs the nonempty wandering rectangle \(R(0,m)\). Let \(R(0,m)'\) denote the subset whose entire forward orbit avoids the switching boundaries; the source proves this subset has full relative Lebesgue measure.

The result is asserted for the *original two coordinate vectors* only, not arbitrary tangent vectors. It uses the actual map's derivative sequence on its wandering rectangles; a geometric signed sequence by itself would not imply the presence of a positive-area dynamical realization. All limits are taken along positive integers in ordinary physical iteration time, not along abstract symbolic time. The initial integer \(m\) does not affect the asymptotic constants.

## Proof

**1. Exact two-symbol derivative reduction.** Equation (3.2) and the immediately preceding derivative formulas in the source show that along every \(x\in R(0,m)'\), the exponents of the original \(e_1\) direction are \(\log\lambda_1\) for \(\gamma^m\) iterations, then \(\log\lambda_2\) for \(\gamma^{m+1}\) iterations, then \(\log\lambda_1\) for \(\gamma^{m+2}\) iterations, and so on. The original \(e_2\) direction has the opposite assignment. The coordinate swaps at block transitions are included in this statement: they are why one follows the original tangent vector rather than an instantaneous coordinate axis.

Write \(\sigma_t=(-1)^j\) for \(T_j\le t<T_{j+1}\), \(j\ge0\), and \(S_n=\sum_{t=0}^{n-1}\sigma_t\). Hence exactly, not just asymptotically,
\[
L_n(x,e_1)=c+d\frac{S_n}{n},\qquad
L_n(x,e_2)=c-d\frac{S_n}{n},\qquad
S_{T_j}=\gamma^m\frac{1-(-\gamma)^j}{1+\gamma}.
\]
The last expression follows from the finite geometric sum of signed block lengths.

**2. Self-similar signed-walk profile.** On \(0<t\le1\), define the continuous, bounded-by-\(t\) function \(\Phi_\gamma\) by
\[
\Phi_\gamma(t)=(-1)^k\left(t-\frac{2\gamma^{-k}}{\gamma+1}\right)
\quad\text{if }\gamma^{-k-1}\le t\le\gamma^{-k},\ k=0,1,\ldots.
\]
The adjacent definitions agree at every boundary. The geometric-sum identity above and the exact slope \(\sigma_t\) on each block imply, for every \(\delta>0\),
\[
\sup_{\delta\le t\le1}
\left|\frac{S_{\lfloor tT_j\rfloor}}{T_j}-(-1)^{j-1}\Phi_\gamma(t)\right|\longrightarrow0.
\]
Indeed the normalized terminal times satisfy \(T_{j-k}/T_j\to\gamma^{-k}\) for each fixed \(k\), and on each resulting compact interval the signed walk is affine with slope \((-1)^{j-1+k}\). Finite many intervals cover \([\delta,1]\), which gives the uniform statement.

**3. Integrating the finite-time exponent.** The summands \(S_n/n\) are uniformly bounded in magnitude by one. Thus the uniform convergence away from zero, followed by a \(\delta\downarrow0\) truncation, yields *uniformly* for \(1/\gamma\le z\le1\),
\[
\frac1{\lfloor zT_j\rfloor}
\sum_{n=1}^{\lfloor zT_j\rfloor}\frac{S_n}{n}
=(-1)^{j-1}\frac1z\int_0^z\frac{\Phi_\gamma(t)}t\,dt+o(1).
\]
Over a complete geometric subinterval the signed integral is
\[
\int_{\gamma^{-k-1}}^{\gamma^{-k}}\frac{\Phi_\gamma(t)}t\,dt
=(-1)^k\gamma^{-k}\left(1-\gamma^{-1}-\frac{2\log\gamma}{\gamma+1}\right).
\]
Summing this convergent geometric series proves
\[
\int_0^1\frac{\Phi_\gamma(t)}t\,dt
=\frac{\gamma-1}{\gamma+1}-\frac{2\gamma\log\gamma}{(\gamma+1)^2}=D_\gamma.
\]
Within the last scaled block \(1/\gamma\le z\le1\), one has \(\Phi_\gamma(t)=t-2/(\gamma+1)\). Subtracting the integral from \(z\) to one yields precisely \(H_\gamma(z)=z^{-1}\int_0^z\Phi_\gamma(t)/t\,dt\), proving the claimed phase law.

**4. Sharp extrema and the complete cluster set.** Direct differentiation gives
\[
H_\gamma'(z)=\frac{2}{(\gamma+1)z^2}
\left(\log z+\frac{\gamma\log\gamma}{\gamma+1}\right).
\]
It changes sign exactly once, from negative to positive, at \(z_*=\gamma^{-\gamma/(\gamma+1)}\). Substitution yields \(H_\gamma(z_*)=-R_\gamma\), while \(H_\gamma(1)=D_\gamma\) and \(H_\gamma(1/\gamma)=-D_\gamma\). The strict inequalities \(0<D_\gamma<R_\gamma<(\gamma-1)/(\gamma+1)\) follow respectively from \(\gamma-\gamma^{-1}>2\log\gamma\) for \(\gamma>1\), the strict interior minimum, and \(\gamma^{\gamma/(\gamma+1)}<\gamma\). Positivity of \(R_\gamma\) follows because \(\log(2\gamma^{\gamma/(\gamma+1)}/(\gamma+1))\) vanishes at \(\gamma=1\) and has strictly positive derivative \(\log\gamma/(\gamma+1)^2\) thereafter.

For each large \(N\) there is a unique \(j\) with \(T_{j-1}<N\le T_j\), so \(N/T_j\in[1/\gamma+o(1),1]\). Every accumulation value is consequently in the union of the odd-phase image \([-R_\gamma,D_\gamma]\) and its negative \([-D_\gamma,R_\gamma]\). Conversely every point in both images is attained as a subsequential limit by choosing \(N=\lfloor zT_j\rfloor\) for a suitable \(z\) and parity of \(j\). Their union is exactly \([-R_\gamma,R_\gamma]\), establishing the theorem for both axes.

**5. The logarithmic average.** Exchanging the finite sums and using \(\sum_{n=t+1}^N n^{-2}=1/(t+1)-1/N+O((t+1)^{-2})\), uniformly for \(0\le t<N\), gives
\[
\sum_{n=1}^N\frac{S_n}{n^2}
=\sum_{t=0}^{N-1}\frac{\sigma_t}{t+1}-\frac{S_N}{N}+O(1).
\]
Since \(|S_N/N|\le1\), it remains to bound the alternating harmonic blocks. For \(j\ge1\),
\[
\sum_{t=T_j}^{T_{j+1}-1}\frac1{t+1}
=\log\gamma+O(\gamma^{-j}).
\]
Their signs alternate, so complete blocks have bounded partial sums; an incomplete block contributes at most \(\log\gamma+O(1)\). Therefore \(\sum_{n=1}^N S_n/n^2=O(1)\), whereas \(\sum_{n=1}^N1/n=\log N+O(1)\). Substituting the exact axis formulas proves \(Q_N(x,e_i)=c+O((\log N)^{-1})\) as claimed. This completes the proof.

## Verification

The accompanying standalone Python standard-library file `verify.py` checks the exact signed block totals using integer arithmetic, compares independent coordinate-expansion counts to the signed-walk formula, and performs finite-time quadrature checks for \(\gamma=2,3,4\). It verifies phase boundary values, extrema and strict parameter inequalities for several integer bases. Its successful finite results support arithmetic consistency but do not constitute the proof of the infinite-time limits; the analytical argument above supplies that proof.

## Relationship to prior work

Nakano, Soma and Yamamoto, arXiv:2206.09508v1 (2022), Theorem 3.1 determines the accumulation intervals of the **unaveraged** finite-time Lyapunov exponent and equation (3.2) provides the exact geometric-block derivative products that serve as the starting point here. Their statement is fully credited. The new calculation targets the second-order arithmetic Cesàro averages, their exact log-periodic limit profile and extreme values, and the distinct logarithmically weighted limit. These facts are not stated in the inspected paper. The older work of Tsujii supplies the underlying wandering-rectangle construction with conformal derivative on the relevant orbit; the strict split between the two axis exponents used here belongs to the modified nonconformal family. Related examples of observable Lyapunov irregularity in Kiriki--Li--Nakano--Soma concern different systems and do not contain this explicit averaging law.

## Limitations

The theorem is restricted to the original two coordinate directions in the source's specified wandering rectangles, with \(0<\varepsilon_2<\varepsilon_1\). It does not determine averages for arbitrary mixed tangent vectors, and it does not assert ergodic behavior with respect to an invariant probability on those wandering rectangles. The new asymptotic law is deduced from the primary paper's already published exact derivative-block construction, not from a new map construction. The priority comparison was limited to the accessible primary text and indexed mathematical literature; an unindexed equivalent could exist. No independent scientific audit has been carried out.

## References

1. Y. Nakano, T. Soma and K. Yamamoto, *Observable Lyapunov irregular sets for planar piecewise expanding maps*, arXiv:2206.09508v1, first publicly posted 2022-06-19, especially §2 equations (2.3)--(2.5) and §3 Theorem 3.1/equation (3.2). https://arxiv.org/html/2206.09508v1
2. S. Kiriki, M.-C. Li, Y. Nakano and T. Soma, *Abundance of observable Lyapunov irregular sets*, arXiv:2110.11727, 2021. https://arxiv.org/abs/2110.11727
3. M. Tsujii, *Piecewise expanding maps on the plane with singular ergodic properties*, Hokkaido Mathematical Journal, preprint dated 1998; available via Hokkaido University repository. https://eprints.lib.hokudai.ac.jp/repo/huscap/all/69165/re415.pdf
