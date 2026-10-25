# Exact optimal randomized row sampling with a pooled measurement in an augmented star system

## Finding
For every integer \(m\ge2\) and \(0<c\le c_m\), where
\[
c_m=\sqrt{\frac{3m+2+m\sqrt5}{2(m^2+3m+1)}},\qquad s=\sqrt{1-c^2},\quad \Delta=(m+1)s^2+2\sqrt m\,cs,
\]
consider the \(m+2\) unit measurement rows in \(\mathbb R^{m+1}\)
\[
a_0=e_0,\qquad a_i=ce_0+se_i\ (1\le i\le m),\qquad b=m^{-1/2}\sum_{i=1}^m e_i.
\]
For randomized Kaczmarz on any **consistent** system with these rows, the maximum, over all fixed independent row-selection distributions \(p\), of the sharp worst-direction single-step conditional expected squared-error decrease is
\[
\max_p\lambda_{\min}\left(\sum_jp_j a_ja_j^{\mathsf T}\right)
=\frac{s^2}{\Delta}.
\]
A globally optimal distribution is
\[
 p_0=\frac{1-(m+1)c^2+\sqrt m\,cs}{\Delta},\qquad
 p_i=\frac1\Delta\ (1\le i\le m),\qquad
 p_b=\frac{\sqrt m\,cs}{\Delta}.
\]
The displayed distribution is the **unique optimal distribution invariant under permutations of the \(m\) leaves**. It assigns positive probability to the pooled measurement for every \(c>0\), and assigns zero probability to the direct hub measurement precisely at the right-hand endpoint \(c=c_m\). No assertion is made for \(c>c_m\) or about uniqueness among all nonsymmetric optimizers.

## Assumptions and scope
Fix an integer \(m\ge2\). The coefficient \(c\) is real and obeys \(0<c\le c_m<1\); the rows have Euclidean norm one, and the right-hand sides are assumed mutually consistent. Each Kaczmarz projection is onto one row hyperplane, chosen independently with fixed probabilities, allowing probabilities zero. The objective is the **uniform one-step conditional mean-square contraction factor**, not the exact finite-horizon MSE or an asymptotic annealed/quenched exponent. For a current error \(z\),
\[
\mathbb E(\|z^+\|_2^2\mid z)=\|z\|_2^2-z^{\mathsf T}F(p)z,\qquad F(p)=\sum_jp_ja_ja_j^{\mathsf T}.
\]
The sharp uniform multiplicative upper bound is \(1-\lambda_{\min}(F(p))\), with equality in the worst eigendirection.

## Proof
**1. Symmetrization.** Permuting the leaf indices conjugates \(F\) by an orthogonal permutation. Since the least eigenvalue is concave in a symmetric matrix, averaging an arbitrary feasible sampling vector over this finite group cannot decrease the least eigenvalue. Thus a maximizer exists with \(p_0=u\), equal local probabilities \(p_i=t\), and pooled probability \(p_b=v\), where \(u,v,t\ge0\) and \(u+mt+v=1\).

**2. Spectrum.** Write \(r=s^2\). On the \((m-1)\)-dimensional leaf-difference subspace, \(F\) acts by \(rt\). In the orthonormal basis consisting of the hub vector \(e_0\) and the pooled unit vector \(b\), its remaining block is
\[
Q=\begin{pmatrix}u+mtc^2&\sqrt m\,tcs\\\sqrt m\,tcs&v+tr\end{pmatrix}.
\]
Using \(u+mt+v=1\), its trace equals \(1-(m-1)rt\). The elementary two-by-two eigenvalue formula gives
\[
\lambda_{\min}(Q)
=\frac{\operatorname{tr}Q}{2}
-\sqrt{\left(\frac{Q_{11}-Q_{22}}2\right)^2+mt^2c^2s^2}
\le\frac{1-(m-1)rt}{2}-\sqrt m\,tcs.
\]
Equality holds exactly when the two diagonal entries of \(Q\) coincide.

**3. Global upper bound.** The eigenvalue decomposition yields, for every permutation-invariant allocation,
\[
\lambda_{\min}(F)\le\min\left\{rt,\ \frac{1-(m-1)rt}{2}-\sqrt m\,tcs\right\}.
\]
The first expression strictly increases in \(t\) and the second strictly decreases. Their unique intersection occurs at \(t_*=1/\Delta\), so their minimum never exceeds \(r/\Delta\). Symmetrization extends this upper bound to **every**, including asymmetric, feasible distribution.

**4. Attainment and domain boundary.** Set \(t=1/\Delta\), \(v=\sqrt m\,cs/\Delta\), and \(u=[1-(m+1)c^2+\sqrt m\,cs]/\Delta\). Direct substitution verifies \(u+mt+v=1\) and \(Q_{11}=Q_{22}=(r+\sqrt m\,cs)/\Delta\). The two eigenvalues of \(Q\) are therefore \(r/\Delta\) and \((r+2\sqrt m\,cs)/\Delta\); the leaf-difference eigenvalues also equal \(r/\Delta\). Thus the upper bound is attained.

For feasibility, \(u\ge0\) is equivalent to \(1-(m+1)c^2+\sqrt m\,c\sqrt{1-c^2}\ge0\). If equality holds, then \((m+1)c^2-1=\sqrt m\,c\sqrt{1-c^2}\ge0\); squaring gives
\[
(m^2+3m+1)c^4-(3m+2)c^2+1=0.
\]
Its only root satisfying \(c^2\ge1/(m+1)\) is \(c_m^2=(3m+2+m\sqrt5)/[2(m^2+3m+1)]\). Continuity and the positive value at \(c=0\) establish \(u>0\) for \(0<c<c_m\), with \(u=0\) precisely at \(c_m\). Both \(t\) and \(v\) remain strictly positive. The intersection of the two strictly monotone upper bounds fixes \(t=t_*\) at any symmetric optimum, and equality in the two-by-two bound then forces \(Q_{11}=Q_{22}\), determining \(u,v\) uniquely. This proves uniqueness within the symmetric class.

## Verification
Execute `python verify.py` with Python 3, NumPy, and SymPy installed. The script checks all assembled row norms, spectral eigenvalue identities, probability normalization, and random asymmetric alternatives for \(m=2,\ldots,12\). It also checks symbolic block identities for \(m=4\) and \(c=3/5\). The reproducible output is included as `verification_output.txt`. Finite tests do not establish the theorem; the argument above proves all integer \(m\ge2\) in the specified parameter range.

## Relationship to prior work
Dai, Soltanalian, and Pelckmans (2014, arXiv:1402.2863, Section II) formulate optimization of the uniform Kaczmarz contraction as a semidefinite program for arbitrary normalized measurement rows. The present statement is a closed-form solution for a specific *overcomplete* star-plus-pooled measurement family; the general SDP does not directly give the probabilities or the activation boundary. Agaskar, Wang, and Lu (2014, GlobalSIP) analyze exact multi-step MSE and its asymptotic exponents, which are distinct objectives. A previous closed form for inverse-positive **square** coordinate-descent Hessians concerns an invertible Gram formulation and does not imply this augmented \((m+2)\)-by-\((m+1)\) frame formula. The pooled row is not a renaming of one of the local rows, and its positive optimum probability is forced within the symmetric class.

## Limitations
The theorem is intentionally restricted to \(0<c\le c_m\), consistent linear systems, unit normalized rows, and fixed iid sampling. It gives the globally best sharp **single-step worst-direction bound**; it does not optimize all finite-horizon or asymptotic MSE metrics, noisy inconsistent systems, adaptive schemes, or parameters beyond \(c_m\). General optimal-design theory might contain an equivalent special case under a change of variables; specialized historical coverage cannot be ruled out by finite searches. Independent mathematical audit remains unperformed.

## References
1. Liang Dai, Mojtaba Soltanalian, Kristiaan Pelckmans, *On the Randomized Kaczmarz Algorithm* (first public arXiv submission 2014-02-12), arXiv:1402.2863, https://arxiv.org/abs/1402.2863 .
2. Ameya Agaskar, Chuang Wang, Yue M. Lu, *Randomized Kaczmarz Algorithms: Exact MSE Analysis and Optimal Sampling Probabilities*, GlobalSIP (2014), doi:10.1109/GlobalSIP.2014.7032145, lawful full text: https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content .
3. *Closed-form optimal coordinate sampling for inverse-positive SPD quadratics* (indexed mathematical finding, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/9/20/SCOPE-inverse-positive-optimal-coordinate-sampling--82c9d23eb995 .
