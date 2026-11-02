# Three-phase optimal sampling for two-cluster correlated Kaczmarz systems

## Finding

Let \(2\le p<q\) be integers, let \(0\le c<1\), and put
\[
s=1-c,\qquad a=c+\frac{s}{p},\qquad b=c+\frac{s}{q}.
\]
For \(0\le d<\sqrt{ab}\), consider \(p+q\) real unit-norm rows whose Gram matrix is
\[
G=\begin{pmatrix}
sI_p+c\mathbf1_p\mathbf1_p^{\mathsf T}&d\mathbf1_p\mathbf1_q^{\mathsf T}\\
d\mathbf1_q\mathbf1_p^{\mathsf T}&sI_q+c\mathbf1_q\mathbf1_q^{\mathsf T}
\end{pmatrix}.
\]
For independent stationary randomized Kaczmarz with arbitrary row-selection probabilities \(\pi_i\ge0\), \(\sum_i\pi_i=1\), let \(\mu(\pi)\) be the **sharp worst-direction one-step conditional expected squared-error decrease**. Define
\[
d_*=\frac{\sqrt{s^2+4q^2ac}-s}{2q}.
\]
Then \(c<d_*<\sqrt{ab}\) whenever \(c>0\); for \(c=0\), \(d_*=0\). The unique globally optimal distribution, including among all independently chosen *asymmetric* probabilities, is uniform within each cluster: each row in the first cluster gets probability \(\alpha=t/p\), and each row in the second gets probability \(\beta=(1-t)/q\), where
\[
t=\begin{cases}
\dfrac{p}{p+q},&0\le d\le c,\\[5pt]
\dfrac{pR}{pR+q},\quad R=\dfrac{cs}{p(ca-d^2)},&c<d<d_*,\\[8pt]
\dfrac{b+d}{a+b+2d},&d_*\le d<\sqrt{ab}.
\end{cases}
\]
The exact largest possible decrease is
\[
\boxed{\mu_* =
\begin{cases}
\dfrac{s}{p+q},&0\le d\le c,\\[5pt]
\dfrac{s(ca-d^2)}{q(ca-d^2)+cs},&c<d<d_*,\\[8pt]
\dfrac{ab-d^2}{a+b+2d},&d_*\le d<\sqrt{ab}.
\end{cases}}
\]
The formulas agree continuously at both phase boundaries. The corresponding sharp one-step worst-direction squared-error contraction factor is \(1-\mu_*\). The middle regime represents a new *cluster-contrast versus coupled-mode* balance between a uniform optimum and an unconstrained coupled-mode optimum; it exists for every \(c>0\) and \(p<q\).

For example, for \((p,q,c)=(2,5,3/10)\), the threshold is \(d_*=(\sqrt{1999}-7)/100\). The choices \(d=1/4,1/3,2/5\) fall in the three respective regimes and yield \((t,\mu_*)=(2/7,1/10),(378/1133,1057/11330),(4/9,1/15)\).

## Assumptions and scope

All vectors are real; the \(p+q\) rows are linearly independent in an ambient Euclidean space of dimension \(p+q\), their norms equal one, and the system is consistent. The stated Gram matrix is positive definite: its within-cluster contrast eigenvalues equal \(s>0\) and its two-dimensional common-mode Gram block is positive definite exactly when \(d<\sqrt{ab}\). Therefore every parameter in the stipulated range is realizable by a real square row matrix. Exactly one row is chosen independently at every step, using the same fixed probability vector. No nonstationary or adaptive rule, block projection, inconsistent system, or exact long-run mean-square exponent is claimed.

## Proof

**1. Sharp criterion and symmetry.** Let \(U\) be any square realization of the unit rows. For an error vector \(e\) and a selected row \(u_i\), orthogonal projection changes squared error by \(-|u_i^{\mathsf T}e|^2\). Consequently
\[
\mathbb E[\|e_+\|^2\mid e]=\|e\|^2-e^{\mathsf T}U^{\mathsf T}\operatorname{diag}(\pi)Ue,
\qquad
\mu(\pi)=\lambda_{\min}\bigl(U^{\mathsf T}\operatorname{diag}(\pi)U\bigr).
\]
The last eigenvalue equals that of \(G^{1/2}\operatorname{diag}(\pi)G^{1/2}\), an affine function of \(\pi\), so \(\mu\) is concave. Conjugating this matrix by any permutation within either cluster leaves its eigenvalues unchanged. Averaging over \(S_p\times S_q\) therefore cannot decrease \(\mu\). Thus some global optimizer assigns respective common row probabilities \(\alpha=t/p\), \(\beta=(1-t)/q\), with \(0\le t\le1\).

**2. Exact eigenvalue reduction.** For a cluster-invariant allocation, the within-cluster contrast eigenvalues are \(s\alpha\) with multiplicity \(p-1\), and \(s\beta\) with multiplicity \(q-1\). The two remaining eigenvalues are those of
\[
H(t)=\begin{pmatrix}at&d\sqrt{t(1-t)}\\d\sqrt{t(1-t)}&b(1-t)\end{pmatrix}.
\]
Writing \(\ell(t)=\lambda_{\min}(H(t))\), the objective is
\[
\mu(t)=\min\{s t/p,\ s(1-t)/q,\ \ell(t)\}.
\]
Let \(\kappa=ab-d^2>0\). The trace of \(H(t)\) is \(b+(a-b)t\) and its determinant is \(\kappa t(1-t)\). Its eigenvalues also equal those of the *affine* pencil \(t vv^{\mathsf T}+(1-t)ww^{\mathsf T}\), with \(v=(\sqrt a,0)^{\mathsf T}\) and \(w=(d/\sqrt a,\sqrt{b-d^2/a})^{\mathsf T}\). Hence \(\ell\) is concave.

Put
\[
t_0=\frac{b+d}{a+b+2d},\qquad L_0=\frac{\kappa}{a+b+2d}.
\]
Direct expansion gives the exact **coupled-mode certificate**
\[
\det\bigl(H(t)-L_0I_2\bigr)=-\kappa(t-t_0)^2.
\]
Therefore \(\ell(t)\le L_0\) everywhere and equality holds exactly at \(t=t_0\), where \(L_0\) is the smaller eigenvalue. Concavity and this unique maximum show that \(\ell\) is strictly increasing before \(t_0\) and strictly decreasing afterward (including the piecewise-linear case \(d=0\)).

**3. Uniform and mixed regimes.** Write \(N=p+q\) and \(t_u=p/N\). If \(d\le c\), the two-dimensional block at uniform sampling satisfies \(H(t_u)\succeq (s/N)I_2\): equivalently, the shifted unweighted common-mode Gram block has determinant \(pq(c^2-d^2)\ge0\). Thus \(\mu(t_u)=s/N\). For any \(t\), the two contrast values imply \(\mu(t)\le s\min\{t/p,(1-t)/q\}\le s/N\), with equality in the second bound only at \(t=t_u\). Hence uniform sampling uniquely optimizes among invariant allocations for \(d\le c\).

Assume \(d>c\). At \(t_u\), the coupled eigenvalue is strictly below \(s/N\). Also \(t_0>t_u\), because
\[
(p+q)(b+d)-p(a+b+2d)=(q-p)(c+d)>0.
\]
Consequently no \(t<t_u\) is optimal; on \([t_u,1]\) the smaller contrast value is \(s(1-t)/q\). As \(t\) increases from \(t_u\) toward \(t_0\), the coupled eigenvalue increases and this contrast value decreases. At \(t_0\) their difference has the sign of
\[
q(ab-d^2)-s(a+d)=qac-qd^2-sd.
\]
This expression is strictly decreasing with \(d\ge0\), and its unique nonnegative zero is \(d_*\). For \(c<d<d_*\), the optimum is the unique crossing strictly before \(t_0\); for \(d\ge d_*\), the optimum is \(t_0\). At a crossing, the characteristic polynomial of \(H(t)\) evaluated at \(s\beta\) gives
\[
(ca-d^2)\alpha=\frac{cs}{p}\beta,
\quad\text{or}\quad
\frac{\alpha}{\beta}=\frac{cs}{p(ca-d^2)}=R.
\]
Solving \(p\alpha+q\beta=1\) yields the middle formula; inserting \(t=t_0\) yields the last formula. The definition of \(d_*\) and positivity of \(s,a,b\) show \(d_*>c\) for \(c>0\). Indeed, \(qac-qd^2-sd\) is positive at \(d=c\), namely \(cs(q/p-1)>0\), and negative at \(d=\sqrt{ab}\), namely \(-s(a+\sqrt{ab})<0\). This establishes the strict ordering of the phases.

**4. Global uniqueness, without imposing symmetry.** Let \(\pi\) be any optimal probability vector. Its within-cluster average equals the *unique* invariant optimum \(\pi_*\) found above. Each group permutation of \(\pi\) is also optimal, so each matrix \(G^{1/2}\operatorname{diag}(P\pi)G^{1/2}-\mu_*I\) is positive semidefinite, and their average is \(G^{1/2}\operatorname{diag}(\pi_*)G^{1/2}-\mu_*I\). If \(z\) belongs to the minimum-eigenvalue space of the latter matrix, its quadratic form vanishes on the average and hence on every individual positive-semidefinite summand, including that of \(\pi\). Subtracting the eigen-equations and multiplying by \(G^{-1/2}\) gives
\[
(\pi_i-\pi_{*,i})(G^{1/2}z)_i=0\qquad\text{for every row index }i.
\]
For \(d\le c\), this minimum-eigenvalue space contains each cluster's entire nontrivial contrast subspace (both have at least two rows), so for every index some \(z\) has a nonzero indicated component. For \(d>c\), the minimum-eigenvalue space contains a coupled common-mode vector whose image \(G^{1/2}z\) is nonzero and constant on each cluster: its two components cannot vanish separately because \(d>0\) and both optimal cluster probabilities are positive. Thus in either case all \(\pi_i=\pi_{*,i}\). This proves unrestricted uniqueness.

## Verification

Run `python verify.py` from a directory containing `verify.py`. The code requires Python 3, NumPy, SciPy, and SymPy but no internet, hidden data, or other artifacts. It symbolically proves the coupled-block determinant identity, verifies exact-rational full-Gram characteristic polynomials and objective values in all three regimes, independently maximizes over the one-dimensional invariant design, and tests many unrestricted asymmetric probability vectors. Recorded results are in `verification_output.txt`. Numerical tests are not substitutes for the all-parameter analytical proof above.

## Relationship to prior work

Strohmer and Vershynin established randomized Kaczmarz convergence with norm-proportional row selection. Dai, Soltanalian, and Pelckmans formulated optimization of the sharp one-step worst-direction contraction as a semidefinite program, and Gower and Richtárik gave the general discrete-sampling convex formulation. The present result does not claim those optimization principles; it supplies a **closed three-regime solution, a sharp second transition, and unrestricted uniqueness** for the stated two-population equicorrelation family. Agaskar, Wang, and Lu target an *exact multi-step annealed* error exponent, not the one-step worst-direction rate optimized here.

A system with one exceptional row has only one nontrivial transverse cluster mode; it does not reduce to the two-cluster system here, in which both groups have transverse eigenmodes and the two-level coupling creates three distinct bottleneck regimes. General-purpose E-optimal-design equivalence theorems and SDP formulations do not by themselves state the present closed allocation or phase boundary. The inspected mathematical records and published literature contained no explicit matching statement; searches alone cannot establish universal publication priority.

## Limitations

The result applies only to positive-semidefinite, nonsingular unit-row Gram matrices of the displayed two-cluster form with nonnegative within- and between-cluster coherence, square consistent systems, and iid static row selection. It optimizes the exact one-step worst-direction expected squared-error factor and the corresponding iterative bound, not the exact infinite-time mean-square exponent or computation-time cost. It does not assert optimality for adaptive sampling, inconsistent systems, block Kaczmarz, arbitrary unequal within-cluster correlations, negative coherence, or a singular Gram boundary. General prior E-optimal-design mathematics may yield alternative derivations; specialized prior exact coverage and independent audit remain open scientific risks.

## References

1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, arXiv:math/0702226, first publicly posted February 8, 2007. https://arxiv.org/abs/math/0702226
2. L. Dai, M. Soltanalian, and K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, arXiv:1402.2863, first publicly posted February 12, 2014. https://arxiv.org/pdf/1402.2863
3. A. Agaskar, C. Wang, and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, GlobalSIP 2014. https://dash.harvard.edu/server/api/core/bitstreams/7312037d-8b4a-6bd4-e053-0100007fdf3b/content
4. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296, first publicly posted June 10, 2015. https://arxiv.org/html/1506.03296v5
