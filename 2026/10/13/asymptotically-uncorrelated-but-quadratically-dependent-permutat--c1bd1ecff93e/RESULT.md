# Asymptotically uncorrelated but quadratically dependent permutation writhe and inversions

## Finding

Let \(m=2r+1\) be odd, with \(r\ge1\), and let \(\pi\) be uniform on permutations of \(\{1,\ldots,m\}\). Set
\[
I_m=\sum_{1\le i<j\le m}\mathbf1\{\pi(i)>\pi(j)\},
\qquad
W_m=\sum_{1\le i<j\le m}a_{ij}\operatorname{sgn}(\pi(j)-\pi(i)),
\]
where \(a_{ij}=1\) when \(j-i\le r\), and \(a_{ij}=-1\) otherwise. This is the circular permutation writhe of Even-Zohar, with the clockwise orientation fixed by the displayed formula. Write
\[
X_m=W_m/m,\qquad
Z_m=(I_m-m(m-1)/4)/m^{3/2}.
\]

**Theorem.** At every odd \(m\ge3\),
\[
\operatorname{Cov}(W_m,I_m)=-\frac{(m-1)^2}{24},
\qquad
\operatorname{Corr}(W_m,I_m)=-\frac{\sqrt3(m-1)}{2m\sqrt{2m+5}}.
\]
Nonetheless, the joint weak limit \((X_m,Z_m)\Rightarrow(Q,G)\) exists; \(G\) is centered Gaussian with variance \(1/36\), \(\operatorname{Var}(Q)=1/6\), and \(\operatorname{Cov}(Q,G)=0\), **but \(Q\) and \(G\) are not independent**. Specifically,
\[
\boxed{\lim_{m\to\infty,\ m\ \mathrm{odd}}\operatorname{Cov}(X_m^2,Z_m^2)
=\operatorname{Cov}(Q^2,G^2)=\frac1{1080}>0.}
\]
Using the established fourth moment of the marginal writhe limit, the correlation between the two squared statistics converges to the explicit positive constant
\[
\boxed{\lim_{m\to\infty,\ m\ \mathrm{odd}}\operatorname{Corr}(X_m^2,Z_m^2)=\frac{\sqrt{35}}{70}.}
\]
The covariance of squares is the substantive joint finding; neither marginal limit alone determines it.

## Assumptions and scope

All permutations are uniformly distributed, \(m\) ranges through odd integers at least three, and \(\operatorname{sgn}\) is \(+1\) for a positive argument and \(-1\) for a negative one. Expectations and covariances refer to this same permutation, not independent copies. The stated asymptotic normalization uses \(m\), the actual number of entries. The result is distribution-free under the equivalent representation by ranks of independent atomless observations.

For an explicit description of the joint limit, let \(\mathfrak H\) be the real Hilbert space of square-integrable functions \(f(t,u)\) on \([0,1]^2\) with \(\int_0^1f(t,u)\,du=0\) for almost every \(t\). Let \(\mathcal G\) be an isonormal Gaussian process on \(\mathfrak H\). Denote its first and symmetric second Wiener integrals by \(I_1\) and \(I_2\), normalized by \(\mathbb E I_2(K)^2=2\|K\|^2\). For \(s\ne t\), define \(A(t,s)=1\) if the clockwise difference \((s-t)\bmod1\) lies in \((0,1/2)\), and \(A(t,s)=-1\) if it lies in \((1/2,1)\); its boundary values are immaterial. Define
\[
h(u,v)=\operatorname{sgn}(v-u)+2u-2v,
\quad K((t,u),(s,v))=\tfrac12 A(t,s)h(u,v),
\quad g(t,u)=-\tfrac12(2t-1)(2u-1).
\]
The kernel \(K\) is symmetric on two copies of \(\mathfrak H\) because both factors are antisymmetric. The joint limit is \((Q,G)=(I_2(K),I_1(g))\).

## Proof

**1. Exact decomposition and finite covariance.** Draw independent \(U_1,\ldots,U_m\) uniformly on \((0,1)\) and replace \(\pi\) by their relative ranks. Put \(v_i=2U_i-1\) and \(h_{ij}=h(U_i,U_j)\). Then \(h\) is canonical: its conditional expectation given either argument is zero. Furthermore \(\mathbb E h(U_1,U_2)^2=1/3\).

Extend the coefficients to a skew-symmetric matrix \(A_{ij}\), with \(A_{ij}=a_{ij}\) for \(i<j\). Every row of this circular-tournament matrix sums to zero. Hence all first-order terms cancel exactly:
\[
W_m=\sum_{i<j}A_{ij}h_{ij},\qquad
I_m-\mathbb EI_m=-\tfrac12(L_m+H_m),
\]
where \(H_m=\sum_{i<j}h_{ij}\), \(L_m=\sum_i b_i v_i\), and \(b_i=2i-m-1\). The variance of \(W_m\) is \(m(m-1)/6\). Canonicality makes \(W_m\) orthogonal to \(L_m\), and two different pair kernels have zero covariance. Therefore
\[
\operatorname{Cov}(W_m,I_m)
=-\tfrac16\sum_{i<j}a_{ij}
=-\tfrac16 r^2=-\frac{(m-1)^2}{24}.
\]
The usual inversion variance is \(m(m-1)(2m+5)/72\); combining the two variances gives the displayed correlation.

**2. Exact leading mixed fourth moment.** Uniform boundedness of \(h\) and its canonicality imply \(\mathbb EW_m^4=O(m^4)\) and \(\mathbb EH_m^4=O(m^4)\): in the four-edge expansion, a nonzero expectation can involve at most four distinct vertices. Independence similarly gives \(\mathbb EL_m^4=O(m^6)\). By Cauchy--Schwarz,
\[
\operatorname{Cov}(W_m^2,(L_m+H_m)^2)
=\operatorname{Cov}(W_m^2,L_m^2)+O(m^{9/2}).
\]
In \(\operatorname{Cov}(W_m^2,L_m^2)\), the only contributions of order \(m^5\) come from two different edges sharing one vertex, with the two factors of \(L_m\) attached to the other endpoints. Same-edge contributions have order at most \(m^4\); all other diagrams either cancel against the product of expectations or vanish by conditional centering. For fixed common vertex, the contraction is
\[
F(u)=\int_0^1 h(u,v)(2v-1)\,dv=2u(1-u)-\tfrac13,
\qquad \int_0^1F(u)^2du=\tfrac1{45}.
\]
Counting both orderings of the two edges and both orderings of the two linear factors gives
\[
\operatorname{Cov}(W_m^2,L_m^2)
=\frac4{45}\sum_i\sum_{\substack{j<k\\j,k\ne i}}A_{ij}A_{ik}b_jb_k+O(m^4)
=\frac2{45}\sum_i\left(\sum_{j\ne i}A_{ij}b_j\right)^2+O(m^4).
\]
The omitted diagonal correction has order \(m^4\), since \(\sum_jb_j^2=O(m^3)\).

Let \(t_i=i/m\). The Riemann limit of \(m^{-2}\sum_{j\ne i}A_{ij}b_j\) is \(R(t_i)\), where
\[
R(t)=\int_0^1 A(t,s)(2s-1)\,ds
=\begin{cases}2t-1/2,&0\le t\le1/2,\\3/2-2t,&1/2\le t\le1.\end{cases}
\]
Consequently \(m^{-5}\sum_i(\sum_{j\ne i}A_{ij}b_j)^2\to\int_0^1R(t)^2dt=1/12\), and
\[
\lim_{m\to\infty,\ m\ \mathrm{odd}}\frac{\operatorname{Cov}(W_m^2,L_m^2)}{m^5}=
\frac2{45}\cdot\frac1{12}=\frac1{270}.
\]
The factor \(1/4\) from the centered inversion identity proves \(\lim_{m\to\infty,\ m\ \mathrm{odd}}\operatorname{Cov}(X_m^2,Z_m^2)=1/1080\). This argument computes the limit directly, without using finite experiments as a substitute for a proof.

**3. Joint weak limit and persistent dependence.** Approximate the Hilbert--Schmidt kernel \(K\) by finite-rank tensors in \(\mathfrak H\). For each fixed tensor, the associated off-diagonal quadratic sum is a polynomial in finitely many normalized sums of independent centered functions of \(U_i\) with deterministic time weights. The multivariate triangular-array CLT and its diagonal correction give the second Wiener integral. Canonicality bounds the normalized quadratic approximation error in \(L^2\) by twice the squared Hilbert--Schmidt approximation error, uniformly in the limit. Thus \(W_m/m\Rightarrow I_2(K)\), jointly with \(L_m/m^{3/2}\Rightarrow I_1((2t-1)(2u-1))\). The canonical remainder \(H_m/m^{3/2}\) vanishes in \(L^2\), establishing the displayed joint convergence.

We have \(\|K\|^2=1/12\), \(\|g\|^2=1/36\), and \(\mathbb E[I_2(K)I_1(g)]=0\) by orthogonality of Gaussian chaoses. The Wiener product identity gives \(\operatorname{Cov}(I_2(K)^2,I_1(g)^2)=8\|Kg\|^2\). Since \(Kg=-\tfrac14R(t)F(u)\), this equals \(8\cdot\tfrac1{16}\cdot\tfrac1{12}\cdot\tfrac1{45}=1/1080>0\), proving that the jointly convergent coordinates are dependent despite zero covariance.

For the final squared-correlation formula, Even-Zohar's fourth-moment result in the normalization \(W_m/r\) gives \(\mathbb EQ^4=19/180\); hence \(\operatorname{Var}(Q^2)=7/90\). Since \(G\) is Gaussian of variance \(1/36\), \(\operatorname{Var}(G^2)=1/648\). Bounded-kernel moment counting gives uniform bounds on all fixed normalized moments needed to pass fourth moments to the limit. Therefore
\[
\frac{1/1080}{\sqrt{(7/90)(1/648)}}=\frac{\sqrt{35}}{70}.
\]

## Verification

Run `python3 verify.py` using the Python 3 standard library. The script independently enumerates every permutation of odd lengths \(m=3,5,7,9\) (a total of \(368046\) permutations), checks the exact covariance and variance formulas with rational arithmetic, and checks each finite normalized covariance-of-squares value. It separately verifies the two polynomial integrals \(1/45\) and \(1/12\), their combination \(1/1080\), and the circular coefficient row balances. The expected terminal line is `VERIFY_OK`. These finite checks are not a proof of the limiting formula; the proof above is analytic.

## Relationship to prior work

Even-Zohar [1] introduced this circular writhe, obtained its non-Gaussian marginal limit, and evaluated its limiting fourth moment; those marginal results are not new here. The same work mentions the ordinary inversion statistic as a comparison but does not give this same-permutation mixed fourth moment. Janson [2] develops a general theory of cyclic and alternating order-two \(U\)-statistics. Its Section 9.1 explains how extensions to joint distributions could be studied, but does not state the explicit joint writhe/inversion law or the positive squared-covariance constant. Foata--Zeilberger [3] supply the older graphical inversion-statistic context; their published scope concerns Mahonian equidistributions, not the stated mixed fluctuation. The new mathematical content is the **same-sample nonlinear dependence certificate** and its exact asymptotic coefficient, not another derivation of the marginal writhe law.

## Limitations

The theorem concerns uniform permutations of odd size and the particular circular writhe orientation displayed. It does not assert independence, an explicit joint density, or any corresponding theorem under Mallows or other nonuniform laws. Existing general cyclic-statistic methods may allow alternative proofs; historical priority of the explicit joint mixed-moment constant has not been independently established. The squared-correlation limit uses the established marginal fourth moment in [1].

## References

[1] Chaim Even-Zohar, *The Writhe of Permutations and Random Framed Knots*, arXiv:1511.09469, first posted 2015-11-30, https://arxiv.org/abs/1511.09469 (especially Sections 1, 3.1, 4 and 5).

[2] Svante Janson, *Cyclic and alternating \(U\)-statistics*, arXiv:2510.12480, first posted 2025-10-14, https://arxiv.org/abs/2510.12480 (especially Example 8.5 and Section 9.1).

[3] Dominique Foata and Doron Zeilberger, *Graphical major indices*, Journal of Computational and Applied Mathematics 68 (1996), 79--101, DOI:10.1016/0377-0427(95)00254-5.
