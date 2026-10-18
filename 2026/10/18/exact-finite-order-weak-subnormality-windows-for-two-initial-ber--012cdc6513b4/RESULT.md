# Exact finite-order weak-subnormality windows for two initial Bergman-shift weights

## Finding

Let \(u,v>0\). On \(\ell^2(\mathbb N_0)\), define the unilateral weighted shift
\[
W_{u,v}e_0=\sqrt u\,e_1,\qquad W_{u,v}e_1=\sqrt v\,e_2,\qquad
W_{u,v}e_j=\sqrt{\frac{j+1}{j+2}}\,e_{j+1}\quad(j\ge2).
\]
Set \(c=3uv>0\), \(d=u-c/2\). For every integer \(k\ge1\), put \(N=k+1\). **The shift is \(k\)-hyponormal if and only if both**
\[
 d\ge -\frac{2c}{N^2(N+1)^2}
\tag{H1}
\]
and
\[
\left(d+\frac{6c}{N^2(N^2-1)}\right)^2
\le \frac{12c}{N^2(N^2-1)^2}
\left(1-c+\frac{4c}{N^2}\right).
\tag{H2}
\]
For every integer \(n\ge1\), **the shift is \(n\)-contractive (has positive \(n\)-th Agler defect) if and only if**
\[
-\frac{c}{(n+1)(n+2)}\le d\le \frac1n-\frac{c}{n+1}.
\tag{C}
\]
These criteria cover all positive \(u,v\), including parameters outside the contractive region (for which the displayed inequalities can simply fail).

For \(0<c\le1\), (H1)--(H2) are precisely the single interval \(d_-(N,c)\le d\le d_+(N,c)\), where
\[
 d_-(N,c)=-\frac{2c}{N^2(N+1)^2},\qquad
 d_+(N,c)=-\frac{6c}{N^2(N^2-1)}+
 \frac{\sqrt{12c(1-c+4c/N^2)}}{N(N^2-1)}.
\tag{W}
\]
At each fixed \(0<c<1\), the sharp endpoints satisfy
\[
 d_-(N,c)=-2cN^{-4}+O_c(N^{-5}),\qquad
 d_+(N,c)=\sqrt{12c(1-c)}\,N^{-3}-6cN^{-4}+O_c(N^{-5}).
\tag{A}
\]
At the critical mass \(c=1\), instead,
\[
 d_-(N,1)=-\frac{2}{N^2(N+1)^2},\qquad
 d_+(N,1)=\frac{4\sqrt3-6}{N^2(N^2-1)}.
\tag{B}
\]
Thus both sides now shrink at fourth order. By contrast, the exact \(n\)-contractivity interval (C) has lower and upper widths of orders \(n^{-2}\) and \(n^{-1}\) for fixed \(0<c<1\), and both of order \(n^{-2}\) at \(c=1\). The two finite-order subnormality tests therefore approach the same limiting locus at different, side-dependent rates.

Finally, the following are equivalent: \(W_{u,v}\) is subnormal; it is \(k\)-hyponormal for every \(k\ge1\); it is \(n\)-contractive for every \(n\ge1\); and \(d=0\), \(c\le1\). In this case its Berger probability measure is \(c\,dt+(1-c)\delta_0\) on \([0,1]\).

## Assumptions and scope

All weights are positive and real, with \(u,v\) denoting **squared** first and second weights. For each \(k\ge1\), \(k\)-hyponormality is the standard positivity of \(([W^{*j},W^i])_{1\le i,j\le k}\), equivalently of all \((k+1)\)-square shifted Hankel moment matrices. For each \(n\ge1\), the Agler defect is \(\sum_{j=0}^n(-1)^j\binom njW^{*j}W^j\). Positivity is non-strict throughout, so all boundary cases are included. The order symbols in (A) are for fixed \(c\), not uniform as \(c\to1\).

## Proof

**1. Moment reduction.** With \(\gamma_0=1\) and \(\gamma_m=\|W_{u,v}^{m}e_0\|^2\), direct telescoping of the unchanged Bergman tail gives
\[
\gamma_1=u=\frac c2+d,\qquad \gamma_m=\frac c{m+1}\quad(m\ge2).
\tag{1}
\]
For every starting index \(r\ge2\), the Hankel moment matrix \((\gamma_{r+i+j})\) is strictly positive, being the Gram matrix of monomials for the strictly positive density \(ct^{r}dt\) on \([0,1]\). Thus the only nonautomatic Hankel conditions occur at starting indices \(r=0\) and \(r=1\).

**2. The matrix starting at one.** Its \((k+1)\)-square version equals \(cH'_N+dE_{00}\), where \((H'_N)_{ij}=1/(i+j+2)\) for \(0\le i,j<N\). Orthogonal polynomials for the measure \(t\,dt\) are the shifted Jacobi polynomials \(P_j^{(0,1)}(2t-1)\), with squared norm \(1/[2(j+1)]\) and absolute endpoint value \(j+1\). Consequently the squared norm of evaluation at zero on degrees below \(N\) is
\[
(H_N'^{-1})_{00}=2\sum_{j=1}^{N}j^3=\frac{N^2(N+1)^2}{2}.
\]
The rank-one positivity criterion for \(cH'_N+dE_{00}\) is exactly (H1).

**3. The matrix starting at zero.** Set \((H_N)_{ij}=1/(i+j+1)\), and let \(e_j\) denote the coordinate basis of \(\mathbb R^N\). Its perturbed moment matrix is
\[
 cH_N+(1-c)e_0e_0^T+d(e_0e_1^T+e_1e_0^T).
\tag{2}
\]
The inverse of \(H_N\), restricted to its first two coordinates, is
\[
G_N=N^2\begin{pmatrix}
1&-(N^2-1)/2\\
-(N^2-1)/2&(N^2-1)^2/3
\end{pmatrix}.
\tag{3}
\]
For completeness, the orthonormal shifted Legendre polynomials are \(\sqrt{2j+1}P_j(2t-1)\). Their endpoint values and first derivatives give (3) from the sums \(\sum_{j<N}(2j+1)=N^2\), \(\sum_{j<N}(2j+1)j(j+1)=N^2(N^2-1)/2\), and \(\sum_{j<N}(2j+1)j^2(j+1)^2=N^2(N^2-1)^2/3\).

Schur-complementing the strictly positive block on coordinates \(2,\ldots,N-1\) in (2) produces the \(2\times2\) matrix
\[
 S_N=\begin{pmatrix}
1-c+4c/N^2 & d+6c/[N^2(N^2-1)]\\
 d+6c/[N^2(N^2-1)] &12c/[N^2(N^2-1)^2]
\end{pmatrix}.
\tag{4}
\]
For \(N=2\), this is the full matrix itself. The lower-right entry is positive because \(c>0\), so \(S_N\) is positive semidefinite exactly when its determinant is nonnegative. This is (H2). Together with Step 2 and the shifted-moment criterion, this proves the entire \(k\)-hyponormality equivalence for all \(k\ge1\).

**4. Exact interval and critical scaling.** When \(0<c\le1\), the upper root of (H2) is \(d_+(N,c)\), and the lower root lies below (H1)'s bound. To verify the latter, set \(d=d_-(N,c)\) in (4). Its off-diagonal entry is \(4c(N+2)/[N^2(N-1)(N+1)^2]\). The ratio of its square to the product of the diagonal entries is
\[
\frac{4c(N+2)^2}{3N^2(N+1)^2(1-c+4c/N^2)}
\le\frac{(N+2)^2}{3(N+1)^2}<1
\quad(N\ge2).
\]
Also, (H2)'s upper root is positive because \(1-c+4c/N^2\ge4c/N^2\) and \(4\sqrt3>6\). This proves (W). Expanding its explicit endpoints proves (A), while inserting \(c=1\) gives (B) exactly.

**5. The Agler defects.** On \(e_r\), the \(n\)-th defect is multiplication by \(\sum_{j=0}^n(-1)^j\binom nj\gamma_{r+j}/\gamma_r\). For \(r\ge2\), positivity is automatic from
\[
\sum_{j=0}^n(-1)^j\binom nj\gamma_{r+j}
=c\int_0^1t^r(1-t)^n\,dt>0.
\]
For \(r=0,1\), the unnormalized alternating sums using (1) are respectively
\[
1-nd-\frac{nc}{n+1},\qquad
 d+\frac{c}{(n+1)(n+2)}.
\tag{5}
\]
Both must be nonnegative, which is exactly (C). The asymptotic rate comparison follows by direct expansion of (C).

**6. The all-order locus.** As \(k\to\infty\), (H2) first forces \(c\le1\) and then forces \(d=0\); conversely \(c\le1,d=0\) makes (1) the moment sequence of \(c\,dt+(1-c)\delta_0\). This positive probability measure proves subnormality and, in particular, every finite Hankel test. Likewise, the two inequalities (C) for arbitrarily large \(n\) force \(d=0,c\le1\), and this representing measure ensures all Agler defects are positive. This completes the proof.

## Verification

The standalone file `weighted_shift_checker.py` reconstructs the moment matrices directly and checks (H1)--(H2), (C), the explicit Hilbert and Jacobi inverse-Gram identities, and the limiting coefficients. It also recovers the published fixed-first-weight, \(k=2\) slice \((63-\sqrt{129})/80\le v\le24/35\) when \(u=1/2\). Execute with `python weighted_shift_checker.py` using SymPy. Finite computations test algebra and sample parameters, but the quantified infinite-order theorem follows from the proof above.

## Relationship to prior work

Curto and Lee's 2005 paper proves that a noninitial finite-rank perturbation of a subnormal weighted shift cannot remain subnormal, and its Example 3.1 analyzes precisely the slice \(u=1/2\), \(k=2\), determining the stated interval in \(v\). The above result recovers that exact interval but studies all \(u,v>0\), every finite \(k\), and every \(n\)-contractivity condition, with sharp asymptotic widths transversal to the subnormal locus. Adams and Exner's work on Agler-type shifts gives complete order thresholds for perturbation of only the first weight of a subnormal model, and compares the two hierarchies. Their one-parameter results also follow from the slice \(v=2/3\), but do not determine the off-slice \(d\)-windows. The moment-positivity and Hilbert/Jacobi machinery used here are classical; the claim of contribution concerns the joint exact two-parameter criteria and side-dependent finite-order collapse, not those tools.

## Limitations

No claim is made for simultaneous perturbations at later weights, other base shifts, weak polynomial hyponormality, or uniform asymptotics as \(c\) approaches \(1\) with \(k\). The exact formulas do allow such variable-parameter exploration, but it is not asserted here. Historical papers under different terminology might contain an equivalent joint phase diagram; bibliographic priority needs independent confirmation. The numerical checker is not an independent audit or an infinite-dimensional certificate.

## References

1. R. E. Curto and W. Y. Lee, *k-Hyponormality of finite rank perturbations of unilateral weighted shifts*, arXiv:math/0507065, first public 2005-07-04; especially Theorem 2.1 and Example 3.1.
2. G. T. Adams and G. R. Exner, *k-Hyponormality and n-contractivity for Agler-type shifts*, Journal of Operator Theory 71 (2014), 585–600, DOI:10.7900/jot.2012aug08.1965; especially Theorem 2.6 and Section 3.
