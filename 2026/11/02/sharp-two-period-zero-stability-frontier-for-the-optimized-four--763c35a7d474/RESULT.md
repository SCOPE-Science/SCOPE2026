# Sharp two-period zero-stability frontier for the optimized four-step BDF-like integrator

## Finding
For the variable-step, second-order BDFL four-step formula of Jensen, Ketcheson, and Lóczi, consider a positive periodic grid whose consecutive step lengths alternate between \(h\) and \(rh\), with arbitrary \(h>0\) and \(r>0\). Applied to the zero differential equation, the method is uniformly zero-stable on this grid **if and only if**
\[
 R^{-1}\le r\le R,\qquad R=4.222826044904903\ldots.
\]
All three parasitic modes decay geometrically per pair exactly when the inequalities are strict. At either endpoint one parasitic two-step Floquet multiplier is \(-1\), while the other two have modulus less than one. Outside this interval a real multiplier is strictly below \(-1\).

The threshold has a closed algebraic description. Put
\[
 A_*=\frac{65-82\sqrt2}{23},\qquad B_*=3-\frac{179\sqrt2}{23},\qquad
 s_* =\frac{-A_*+\sqrt{A_*^2-4(B_*-2)}}2,
 \qquad R=\frac{s_*+\sqrt{s_*^2-4}}2.
\]
An individual frozen-coefficient step can be unstable while the alternating scheme is geometrically stable. For example, at \(r=4\) one frozen difference-state companion has determinant \((1093-86\sqrt2)/779>1\), but the complete two-step Floquet matrix has all three parasitic multipliers strictly inside the unit circle. Thus frozen-coefficient stability is not a necessary condition for stability of this prescribed periodic step sequence.

## Assumptions and scope
Work in real exact arithmetic. The differential equation is \(y'(t)=0\). The mesh is periodic with step lengths \(h,rh,h,rh,\dots\). The method is precisely the variable-step BDFL four-step, order-two construction in Section 6.2 and Appendix A of arXiv:2610.22685v1, not classical BDF4. In its normalized stencil
\[
 \sum_{j=0}^{4}\alpha_{j,n}y_{n-3+j}=h_n\beta_{4,n} f_{n+1},
 \qquad \alpha_{4,n}=1,
\]
all earlier right-hand-side coefficients vanish and the fixed coefficients are
\[
 \alpha_2=\frac{2(1+12\sqrt2)}{41},\qquad
 \alpha_3=-\frac{2(18+11\sqrt2)}{41}.
\]
The remaining coefficients satisfy the paper's degree-two order conditions for the actual local time nodes. With \(f=0\), only the \(\alpha_j\) enter. "Uniformly zero-stable" here means that for every fixed \(r\) in the stated interval the homogeneous propagators, over any number of steps and independently of the overall scale \(h\), have bounded operator norm. This is not a claim of stability on arbitrary nonperiodic grids, or of absolute stability when \(f\ne0\).

## Proof
**1. Reconstruct both phases.** Write \(d_n=y_n-y_{n-1}\). Order-zero consistency gives \(\sum_{j=0}^4\alpha_j=0\), hence each step obeys
\[
 d_{n+1}=p\,d_n+q\,d_{n-1}+w_n d_{n-2},\quad
 p=\frac{-5+22\sqrt2}{41},\quad q=\frac{-7-2\sqrt2}{41},
\]
where \(w_n=\alpha_{0,n}\). To reconstruct this coefficient independently of any computer implementation, set the local nodes \(c_j=(t_{n-3+j}-t_{n-3})/h_n\). Second-order consistency implies
\[
 \alpha_1(c_1^2-2c_4c_1)
 =-\sum_{j=2}^{4}\alpha_j(c_j^2-2c_4c_j),\qquad
 \alpha_0=-1-\alpha_1-\alpha_2-\alpha_3.
\]
For a step of length \(rh\), the nodes are \(0,1/r,(r+1)/r,(r+2)/r,2(r+1)/r\). For the following step of length \(h\), they are \(0,r,r+1,2r+1,2r+2\). Substitution yields the two coefficients
\[
 u(r)=\frac{(62+6\sqrt2)r^2+(24-40\sqrt2)r+5-22\sqrt2}{41(4r+3)},
 \qquad v(r)=u(1/r).
\]

**2. Reduce to a cubic Floquet polynomial.** On \((d_n,d_{n-1},d_{n-2})^{\mathsf T}\), a phase has matrix
\[
 C(w)=\begin{pmatrix}p&q&w\\1&0&0\\0&1&0\end{pmatrix}.
\]
The two-period matrix is \(P=C(u)C(v)\), or the reverse product, which has the same characteristic polynomial. Direct multiplication gives
\[
 \chi_r(z)=z^3-Tz^2+E(r)z-V(r),\qquad
 T=p^2+2q=\frac{419-384\sqrt2}{1681},\quad
 E=q^2-p\,[u(r)+v(r)],\quad V=u(r)v(r).
\]
Writing \(s=r+r^{-1}\ge2\), the symmetric coefficients are
\[
 u+v=\frac{82[(93+9\sqrt2)s^2+(170-92\sqrt2)s-75-244\sqrt2]}{1681(12s+25)},
\]
\[
 V=\frac{(46-1334\sqrt2)s^2+(2888-3064\sqrt2)s+8593+1272\sqrt2}{1681(12s+25)}.
\]
The full four-dimensional recurrence has an additional, simple constant-solution multiplier \(1\) as long as the cubic has no multiplier \(1\).

**3. Establish the sharp open stability interval.** For a real monic cubic \(z^3-Tz^2+Ez-V\), the Schur inequalities are
\[
 |V|<1,\quad 1-T+E-V>0,\quad 1+T+E+V>0,\quad 1-E+TV-V^2>0.
\]
Algebraic factorization gives
\[
 1+T+E+V=
 \frac{184-5336\sqrt2}{1681r(3r+4)(4r+3)}
 \big[r^4+A_*r^3+B_*r^2+A_*r+1\big].
\]
The bracket equals \(r^2[s^2+A_*s+B_*-2]\). Its quadratic factor has exactly one root \(s_*>2\), with \(2<s_*<9/2\), and is negative for \(2\le s<s_*\). Since the prefactor is negative, the third Schur inequality above holds precisely for \(s<s_*\).

For completeness the other inequalities do not cut down this interval. In fact
\[
 1-T+E-V=
 \frac{(92-2668\sqrt2)(r+1)^2[r^2-(2+98\sqrt2/23)r+1]}
 {1681r(3r+4)(4r+3)}>0
\]
whenever \(2\le s\le9/2\), since \(2+98\sqrt2/23>9/2\). Differentiating the displayed rational expressions in \(s\) shows that \(u+v\) increases and \(V\) decreases for \(s\ge2\): their derivative numerators respectively have only positive and only negative coefficients. Evaluating at \(s=2\) and \(s=9/2\) therefore gives
\[
 u+v>0,\qquad -\frac13<V<\frac1{100}
 \qquad (2\le s\le9/2).
\]
Also \(p>0\), \(q^2<1/10\), and \(-1/10<T<0\). Hence
\[
 1-E+TV-V^2
 =1-q^2+p(u+v)+TV-V^2
 >1-\frac1{10}-\frac1{30}-\frac19>0.
\]
Thus \(|V|<1\) and the remaining Schur conditions also hold. Therefore all parasitic multipliers satisfy \(|z|<1\) exactly for \(s<s_*\), equivalently \(R^{-1}<r<R\).

**4. Boundaries and instability.** At \(s=s_*\), \(\chi_r(-1)=0\). The strict remaining Schur inequalities imply that this root is simple and the other two lie strictly inside the disk; the constant root \(1\) is distinct. Hence every propagator is power bounded at both boundary ratios. For \(s>s_*\), \(1+T+E+V<0\), so \(\chi_r(-1)>0\). Since \(\chi_r(z)\to-\infty\) as \(z\to-\infty\), a real eigenvalue lies below \(-1\); consequently perturbations grow exponentially along the periodic grid. This proves both necessity and sufficiency.

**5. Frozen versus periodic.** At \(r=4\), \(u(4)=(1093-86\sqrt2)/779>1\). Because \(\det C(w)=w\), its frozen companion must have an eigenvalue of modulus greater than one. But \(4<R\), so the periodic product strictly damps every parasitic mode. This phenomenon is not inferred from the two separate frozen spectra; it follows from their noncommuting product.

## Verification
Run `python verify.py` with the dependencies in `requirements.txt`. The checker independently reconstructs the alternating-grid coefficients using second-order order conditions; verifies exact symbolic characteristic-polynomial and rational-function identities; and performs finite eigenvalue comparisons on prescribed ratios. Its successful run reported 278 checks, with \(R=4.222826044904903\ldots\). The decisive continuum signs and endpoint cases are established analytically in the proof, not by the numerical scan.

## Relationship to prior work
Jensen, Ketcheson, and Lóczi (arXiv:2610.22685v1, first posted 15 October 2026), Sections 6.2–6.3 and Appendix A, prescribe the variable-step coefficients. Their stability study explicitly considers **frozen coefficients** rather than products of changing companion matrices and does not give this two-period monodromy frontier. The periodic-product question is therefore not answered by their frozen root-condition region. General theory of variable-grid zero-stability, including Söderlind–Fekete–Faragó (2018), applies a different smooth-grid regime; the alternating ratio here remains fixed away from one as the global step scale decreases. Li–Liao (2022) addresses classical BDF2 and BDF3, not this optimized four-step BDF-like formula. Exact coincidence with an unlocated older special-case calculation cannot be ruled out without a broader historical audit.

## Limitations
The theorem holds only for the named four-step second-order method, for scalar zero dynamics and exactly alternating positive mesh increments. Zero-stability does not by itself guarantee nonlinear solver accuracy, convergence for arbitrary adaptive controllers, positivity, or finite-precision robustness. The parity of the first step affects the order of the factors but not their characteristic polynomial. There is no independent audit, and complete historical priority is not certified.

## References
1. T. Jensen, D. I. Ketcheson, and L. Lóczi, *Optimized linear multistep methods for stiff problems*, arXiv:2610.22685v1, 15 October 2026, especially Sections 6.2–6.3 and Appendix A. https://arxiv.org/html/2610.22685v1
2. G. Söderlind, I. Fekete, and I. Faragó, *On the zero-stability of multistep methods on smooth nonuniform grids*, BIT Numerical Mathematics 58 (2018), 1125–1143. https://doi.org/10.1007/s10543-018-0716-y
3. Z. Li and H.-L. Liao, *Stability of Variable-Step BDF2 and BDF3 Methods*, SIAM Journal on Numerical Analysis 60 (2022), 2253–2272. https://doi.org/10.1137/21M1462398
4. Y. Hadjimichael, D. I. Ketcheson, L. Lóczi, and A. Németh, *Strong stability preserving explicit linear multistep methods with variable step size*, SIAM Journal on Numerical Analysis 54 (2016), 2799–2832; arXiv:1504.04107. https://arxiv.org/abs/1504.04107
