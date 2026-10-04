# A polynomial strong-monotonicity tail in Fast Fixed-Point acceleration
## Finding
Consider the scalar monotone inclusion
\[
0\in G(x)+T(x),\qquad G(x)=\lambda x,\qquad T=0,\qquad \lambda>0,
\]
which is the optimality condition for the condition-number-one strongly convex quadratic \(f(x)=\lambda x^2/2\). Apply the FFP2 iteration of Nguyen-Trung, Necoara, and Tran-Dinh with its prescribed initialization \(x_0=y_0=z_0\ne0\), parameters \(r>1\), \(t_k=t_0+k\), \(0<\eta\lambda<1\), and
\[
0<\nu<(r-1)\eta,
\]
with \(t_0\) satisfying the source theorem's lower bound. Then, with \(s=\nu/\eta\),
\[
\lim_{k\to\infty}\frac{\log|z_k|}{\log k}=-s,
\qquad
\lim_{k\to\infty}\frac{\log|x_k|}{\log k}
=
\lim_{k\to\infty}\frac{\log|y_k|}{\log k}=-(1+s).
\]
More precisely,
\[
\lim_{k\to\infty}t_k\frac{|x_k|}{|z_k|}=\frac{r(1-\eta\lambda)}{\eta\lambda},
\qquad
\lim_{k\to\infty}t_k\frac{|y_k|}{|z_k|}=\frac{r}{\eta\lambda}.
\]
Consequently \(\lim_{k\to\infty}|x_k|^{1/k}=1\): this admissible unmodified FFP2 run is not R-linearly convergent even though the underlying quadratic is strongly convex with condition number one.

## Assumptions and scope
The source defines, in its cocoercive setting,
\[
G_\eta(x)=\frac{x-J_{\eta T}(x-\eta Gx)}{\eta}
\]
and FFP2 by
\[
y_k=\frac{t_k-r}{t_k}x_k+\frac r{t_k}z_k,
\qquad
x_{k+1}=y_k-\eta G_\eta(y_k),
\]
\[
z_{k+1}=z_k-\frac{\nu_k}{r}G_\eta(y_k),
\qquad
\nu_k=\nu\frac{t_k-1}{t_k},
\qquad
t_{k+1}=t_k+1.
\]
It requires \(r>1\), \(0<\nu<(r-1)\eta\), and an explicit lower bound on \(t_0\). Here \(T=0\), so \(J_{\eta T}=I\) and therefore \(G_\eta=G\). The map \(G(x)=\lambda x\) is \(1/\lambda\)-cocoercive and \(\lambda\)-strongly monotone. The additional restriction \(0<\eta\lambda<1\) is imposed only for the elementary positivity argument below; no claim is made for all admissible source stepsizes.

The conclusion concerns the unmodified FFP2 recurrence. It is not a complexity lower bound for algorithms that restart, retune parameters using strong monotonicity, precondition, or otherwise alter the recurrence.

## Proof
Set
\[
a=\eta\lambda,\qquad s=\frac\nu\eta,
\qquad c=\frac{\nu\lambda}{r}=\frac{as}{r}.
\]
The parameter assumptions give \(0<c<a<1\). By linearity it suffices to take \(x_0=z_0>0\); a negative initialization has the same absolute-value dynamics. For \(t=t_k\), define
\[
q_k=\frac{x_k}{z_k},
\qquad
h_k=\frac{y_k}{z_k}.
\]
The scalar recurrence is
\[
h_k=\left(1-\frac rt\right)q_k+\frac rt,
\qquad
x_{k+1}=(1-a)y_k,
\]
\[
z_{k+1}=z_k\left[1-c\left(1-\frac1t\right)h_k\right].
\]
Initially \(q_0=1\). If \(0<q_k\le1\) and \(t_k\ge r\), then \(0<h_k\le1\), and
\[
q_{k+1}
=
\frac{(1-a)h_k}{1-c(1-1/t_k)h_k}.
\]
The denominator is positive. Moreover, because \(c(1-1/t_k)<a\), the denominator exceeds \((1-a)h_k\). Hence \(0<q_{k+1}<1\). Induction gives positive \(x_k,y_k,z_k\) and \(0<q_k\le1\) for all \(k\).

Let
\[
\theta=\frac{1-a}{1-c}<1.
\]
Since \(h_k\le q_k+r/t_k\),
\[
q_{k+1}\le \theta q_k+\frac{\theta r}{t_k}.
\]
Iterating this stable scalar inequality and splitting the convolution into indices before and after \(k/2\) gives \(q_k=O(1/t_k)\). Thus \(p_k=t_kq_k\) is bounded. Because
\[
t_kh_k=p_k+r-\frac{rp_k}{t_k},
\]
the exact ratio recurrence, together with \(q_k=O(1/t_k)\), yields
\[
p_{k+1}=(1-a)(p_k+r)+o(1).
\]
The limiting affine map has slope \(1-a\in(0,1)\), so
\[
p_k\longrightarrow d,
\qquad
d=(1-a)(d+r)=\frac{r(1-a)}a.
\]
Consequently
\[
t_kh_k\longrightarrow d+r=\frac ra.
\]
This proves the two ratio limits.

Now set
\[
\delta_k=c\left(1-\frac1{t_k}\right)h_k.
\]
The preceding limit gives
\[
t_k\delta_k\longrightarrow c\frac ra=s,
\qquad
\delta_k=O(1/t_k).
\]
Since \(z_{k+1}=z_k(1-\delta_k)\) and \(0<\delta_k<1\),
\[
\log z_{k+1}-\log z_k
=
-\delta_k+O(\delta_k^2).
\]
The series \(\sum_k\delta_k^2\) converges, while harmonic summation and \(t_k\delta_k\to s\) imply
\[
\sum_{j<k}\delta_j=s\log k+o(\log k).
\]
Therefore
\[
\log z_k=-s\log k+o(\log k),
\]
which is the claimed exponent for \(z_k\). Since \(h_k\sim r/(a t_k)\), one obtains
\[
y_k=h_kz_k=k^{-(1+s)+o(1)},
\]
and \(x_{k+1}=(1-a)y_k\) gives the same exponent for \(x_k\). Finally, any sequence of the form \(k^{-\alpha+o(1)}\) with \(\alpha>0\) has \(k\)-th root tending to one, proving the failure of R-linear convergence for this run.

## Verification
The proof is analytic. A bundled standard-library replay evaluates an admissible instance
\[
\lambda=1,\quad \eta=\tfrac12,\quad r=3,\quad \nu=\tfrac12,\quad t_0=10.
\]
Here \(a=1/2\) and \(s=1\), so the predicted limits are
\[
t_kx_k/z_k\to3,
\qquad
t_ky_k/z_k\to6,
\qquad
t_k\left(1-z_{k+1}/z_k\right)\to1.
\]
The replay checks the source parameter inequalities, positivity of the invariant cone, and these three limits numerically at a large finite index. This computation is only a consistency check; the infinite asymptotic statements follow from the proof above.

## Relationship to prior work
Nguyen-Trung, Necoara, and Tran-Dinh prove general FFP2 convergence in the cocoercive setting and an \(O(1/k^2)\) bound for squared residual quantities, equivalent to an \(O(1/k)\) residual-norm guarantee at that level of generality. Their theorem does not state the exact scalar exponent above or an automatic R-linear improvement under strong monotonicity for the same unmodified recurrence.

Nearby strongly-monotone work such as the NOD method of Lee, Ryu, and Yun obtains accelerated linear complexity by using a different algorithm and assumptions tailored to strong monotonicity. Maingé's earlier inertial generalized forward-backward method is also algorithmically distinct. The present result therefore identifies a boundary of this particular anchored FFP2 recurrence rather than a limitation of strongly-monotone optimization itself.

Targeted searches for the exact FFP2 scalar law, strong-monotonicity specialization, restart interpretation, and equivalent polynomial-tail formulations did not identify a source implying this statement. A residual literature risk remains that an older inertial recurrence, written in different notation, may admit an equivalent scalar asymptotic calculation.

## Limitations
The proof uses the one-dimensional linear case, \(T=0\), and the additional range \(0<\eta\lambda<1\). It establishes exact logarithmic exponents and ratio limits, but not a full asymptotic constant for \(z_k\). It does not analyze distributed network coupling, stochasticity, nonlinear strongly monotone maps, or FFP2 variants with restart or parameter modification. The originality comparison is based on the inspected source texts and targeted searches and is not a proof of absence from all literature.

## References
1. N. Nguyen-Trung, I. Necoara, Q. Tran-Dinh, *Distributed Fast Fixed-Point Algorithms for Composite Monotone Inclusions over Networks*, arXiv:2609.14953v1, first public 2026-09-14.
2. J. Lee, E. K. Ryu, S. Yun, *NOD: Accelerating the Optimization of Smooth Strongly Monotone Operators*, arXiv:2604.11105v1, 2026.
3. P.-E. Maingé, *Accelerated proximal algorithms with a correction term for monotone inclusions*, arXiv:2107.10107v1, 2021.
