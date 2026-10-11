# A maximal Crawford localization gap on complex coordinate spaces

## Finding
Let \(I\) be any index set with at least two elements, choose distinct \(p,q\in I\), and write \(X=c_0(I;\mathbb C)\), with the supremum norm; this includes \(\ell_\infty^n(\mathbb C)\) when \(|I|=n<\infty\). For every \(0<r<1\) put \(s=\sqrt{1-r^2}\) and define a diagonal surjective isometry \(U_r:X\to X\) by
\[
 (U_rx)_p=(r+is)x_p,\qquad (U_rx)_q=(r-is)x_q,\qquad (U_rx)_j=x_j\quad(j\notin\{p,q\}).
\]
The canonical coordinate family \((e_j,e_j^*)_{j\in I}\) has Lindenstrauss property \(\beta\) with cross-correlation constant \(0\). If
\[
 c(T)=\inf\{|f(Tx)|:\|x\|=\|f\|=f(x)=1\},\quad
 c_\beta(T)=\inf\{|e_j^*(Tx)|:\|x\|=1,\ e_j^*(x)=1,\ j\in I\},
\]
then the exact identity is
\[
 \boxed{\quad\|U_r\|=c_\beta(U_r)=1,\qquad c(U_r)=r.\quad}
\]
Therefore the coordinate-state reduction asked in Question 3.4 of Choi--Lee (2022) fails even for surjective isometries with **strictly positive** Crawford number. Among norm-one operators with prescribed Crawford number \(r\), the discrepancy \(c_\beta(T)-c(T)\) is at most \(1-r\), and \(U_r\) attains that ceiling. For every \(E\in\mathcal L(X)\),
\[
 c_\beta(U_r+E)-c(U_r+E)\ge 1-r-2\|E\|.
\]
In particular, any perturbation satisfying \(\|E\|<\min\{r,(1-r)/2\}\) still has positive Crawford number and a strictly positive coordinate-localization gap.

## Assumptions and scope
The scalar field is complex. For arbitrary \(I\), the space \(c_0(I;\mathbb C)\) consists of complex families vanishing at infinity. Its continuous dual is \(\ell_1(I;\mathbb C)\), with the standard complex-linear pairing \(f(x)=\sum_{j\in I}f_jx_j\). The definition of property \(\beta\) used here requires norm-one \(e_j,e_j^*\) with \(e_j^*(e_j)=1\), \(|e_i^*(e_j)|\le\rho<1\) for distinct indices, and \(\|x\|=\sup_j|e_j^*(x)|\). The canonical coordinates satisfy these conditions with \(\rho=0\).

The source question compares the full state-space infimum with the infimum restricted to the displayed property-\(\beta\) functionals. It does not require the operator to be non-attaining. The theorem concerns exactly this comparison; it makes no assertion about density of Crawford-number-attaining operators.

## Proof
**1. The canonical property-\(\beta\) witnesses and the restricted number.** Coordinate vectors and evaluations have norm one, satisfy \(e_i^*(e_j)=\delta_{ij}\), and recover the supremum norm. Each diagonal multiplier of \(U_r\) has modulus one, so \(U_r\) and its diagonal inverse are isometries. If \((x,e_j^*)\) is a state, then \(x_j=1\). Hence \(|e_j^*(U_rx)|=|\lambda_j|=1\) for every permitted coordinate state, showing \(c_\beta(U_r)=1\).

**2. All norming functionals, including non-coordinate ones.** Every \(f\in X^*=\ell_1(I)\) can be represented by coefficients \((f_j)\). For \(\|x\|=\|f\|=f(x)=1\), equality holds throughout
\[
 1=\left|\sum_j f_jx_j\right|\le\sum_j|f_j|\,|x_j|\le\sum_j|f_j|=1.
\]
Thus the products \(t_j=f_jx_j\) are nonnegative real numbers with \(\sum_jt_j=1\); all coefficients with \(f_j\ne0\) are supported on coordinates where \(|x_j|=1\). Consequently
\[
 f(U_rx)=\sum_jt_j\lambda_j
  =r(t_p+t_q)+(1-t_p-t_q)+is(t_p-t_q),
\]
where \(\lambda_p=r+is\), \(\lambda_q=r-is\), and all other \(\lambda_j=1\). Its real part is
\[
 \operatorname{Re}f(U_rx)=r+(1-r)(1-t_p-t_q)\ge r.
\]
Hence \(|f(U_rx)|\ge r\) for every state. With \(x=e_p+e_q\) and \(f=(e_p^*+e_q^*)/2\), both norms equal one, \(f(x)=1\), and \(f(U_rx)=r\). Therefore \(c(U_r)=r\) exactly, without any compactness or countability assumption on \(I\).

**3. Sharpness among norm-one operators.** For any bounded \(T\), \(0\le c(T)\le c_\beta(T)\le\|T\|\), since the coordinate states are a nonempty subset of all states. If \(\|T\|=1\) and \(c(T)=r\), then \(c_\beta(T)-c(T)\le1-r\), with equality for \(U_r\).

**4. Openness and the positive-Crawford boundary.** If \(\|E\|=\delta\), evaluating at unit states yields \(|c(U_r+E)-c(U_r)|\le\delta\) and \(|c_\beta(U_r+E)-c_\beta(U_r)|\le\delta\), because infima of functions changing pointwise by at most \(\delta\) change by at most \(\delta\). Thus the discrepancy is at least \(1-r-2\delta\) and \(c(U_r+E)\ge r-\delta\). Under the stated strict perturbation threshold both quantities remain positive.

## Verification
The proof is exact for every cardinality \(|I|\ge2\) and every real \(r\in(0,1)\). The companion `verify.py` independently checks rational phase examples (including the exact triple \(r=3/5\), \(s=4/5\)) on finite coordinate simplices. Those finite tests illustrate the inequalities; they are not used as a proof for infinitely many states or arbitrary index sets. The equality-chain argument supplies that proof.

## Relationship to prior work
Choi and Lee, *On the Crawford number attaining operators* (arXiv:2201.10031, first submitted 2022-01-25), define Crawford attainment, establish density results, and ask in their Question 3.4 whether a property-\(\beta\) norming family suffices for the Crawford infimum. The finite-dimensional attainment statement in their Proposition 2.1 does not imply the proposed restricted-family identity: both sides here are attained, but at different sets of states. Their Question 3.5 on density remains untouched. The convex-hull description of diagonal numerical ranges is classical; the point is the exact and sharp incompatibility with the **specified coordinate-restricted Crawford infimum**, including positive values and stability under perturbation.

## Limitations
The failure is proved for the canonical property-\(\beta\) witnesses on complex \(c_0(I)\); it does not rule out other, enlarged norming-state families or alternative approximation methods. No assertion is made about the real-scalar analogue or arbitrary Banach spaces. A literature search cannot eliminate the possibility of an unindexed prior observation of this elementary diagonal obstruction.

## References
1. G. Choi and H. J. Lee, *On the Crawford number attaining operators*, arXiv:2201.10031v1 (2022-01-25 UTC), revised v2 (2022-03-18); *Revista Matemática Complutense* 36 (2023), 841–857, DOI: 10.1007/s13163-022-00445-y. Definitions 1.1 and property \(\beta\); Questions 3.4 and 3.5.
2. The standard duality \(c_0(I)^*=\ell_1(I)\), equality in the triangle inequality, and the elementary convex-hull description of diagonal numerical ranges are used as classical facts, each proved directly in the relevant form above.
