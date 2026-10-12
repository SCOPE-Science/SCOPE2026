# A quadratic cost frontier for minimax randomized Kaczmarz sampling on simplex frames

## Finding

Let \(d\ge2\) be an integer and let \(v_0,\ldots,v_d\in\mathbb R^d\) be unit vectors satisfying \(v_i^{\mathsf T}v_j=-1/d\) for distinct indices. For independent, with-replacement randomized Kaczmarz on a consistent system having these normalized row normals, assign row-selection probabilities \(p_i\ge0\), \(\sum_{i=0}^d p_i=1\). A projection onto row \(0\) costs \(t>0\); a projection onto any other row costs one unit. Optimize the guaranteed worst-initialization, **single-step expected squared-error decrement divided by the single-step expected cost**:
\[
\eta(p)=\frac{\lambda_{\min}\!\left(\sum_{i=0}^d p_iv_iv_i^{\mathsf T}\right)}{tp_0+\sum_{i=1}^d p_i}.
\]
Then the optimum and its complete set of attaining probability distributions are
\[
\boxed{\eta^*(d,t)=\begin{cases}
\dfrac{d+1}{d(d+t)},&0<t\le d^2,\\[4pt]
\dfrac1{d^2},&t\ge d^2.
\end{cases}}
\]
For \(0<t<d^2\), the optimizer is unique and uniform: \(p_i=1/(d+1)\) for all \(i\). For \(t>d^2\), it is unique and drops the expensive row: \(p_0=0\), \(p_i=1/d\) for \(1\le i\le d\). At \(t=d^2\), **every** optimizer has
\[
\boxed{p_0=r,\qquad p_i=\frac{1-r}{d}\ (1\le i\le d),\qquad 0\le r\le\frac1{d+1}.}
\]
No asymmetric optimizers exist, even though asymmetric distributions are allowed. In particular, the sampling of a single row remains exactly uniform until its relative cost reaches the quadratic threshold \(d^2\), and then that row becomes unnecessary above the threshold.

## Assumptions and scope

All rows are normalized, the linear equations are exactly consistent, and projections are unrelaxed. Probabilities are chosen afresh and independently at every step; zero probabilities are allowed. The \(d\) inexpensive vectors themselves span \(\mathbb R^d\), so deleting row \(0\) does not destroy solvability or positive contraction. Costs are strictly positive and measured per selected projection. The objective is **precisely** \(\eta(p)\), not wall-clock exponential convergence, an asymptotic annealed Lyapunov exponent, or a finite-horizon cost-minimization objective.

For error vector \(e\), the exact conditional identity for an orthogonal Kaczmarz projection is
\[
\mathbb E\bigl[\|e_{\mathrm{new}}\|^2\mid e\bigr]
=\|e\|^2-e^{\mathsf T}\left(\sum_{i=0}^d p_iv_iv_i^{\mathsf T}\right)e.
\]
Taking the infimum over nonzero \(e\) gives the numerator of \(\eta(p)\), so this is a genuine sharp one-step worst-case guarantee.

## Proof

**1. Homogenization.** Write \(C(p)=tp_0+\sum_{i=1}^dp_i>0\) and \(w_i=p_i/C(p)\). Then \(w_i\ge0\), \(tw_0+\sum_{i=1}^dw_i=1\), and
\[
\eta(p)=\lambda_{\min}\!\left(\sum_{i=0}^dw_iv_iv_i^{\mathsf T}\right).
\]
The converse is \(p_i=w_i/(\sum_jw_j)\), a bijection between the two feasible sets. The inverse optimal value is equivalently the minimum cost of the positive-semidefinite covering problem
\[
\min_{z\ge0}\left(tz_0+\sum_{i=1}^dz_i\right)
\quad\text{subject to}\quad
\sum_{i=0}^dz_iv_iv_i^{\mathsf T}\succeq I_d.
\tag{P}
\]
Indeed, any feasible \(w\) with positive least eigenvalue \(\lambda\) gives a covering vector \(z=w/\lambda\) of cost \(1/\lambda\); conversely, dividing any covering vector by its total price gives a feasible \(w\) whose least eigenvalue is at least the reciprocal price. The optimizing value is positive because the simplex vectors span.

**2. Dual witnesses.** The semidefinite dual of (P) is
\[
\max_{Z\succeq0}\operatorname{tr}Z
\quad\text{subject to}\quad v_0^{\mathsf T}Zv_0\le t,
\quad v_i^{\mathsf T}Zv_i\le1\ (1\le i\le d).
\tag{D}
\]
Weak duality follows by multiplying the matrix inequality in (P) by \(Z\succeq0\) and taking the trace. The simplex identities are
\[
\sum_{i=0}^dv_i=0,
\qquad\sum_{i=0}^dv_iv_i^{\mathsf T}=\frac{d+1}{d}I_d.
\tag{1}
\]
For \(0<t<d^2\), define
\[
\alpha=\frac{d^2-t}{d^2-1},\qquad
\beta=\frac{d^2(t-1)}{d^2-1},\qquad
Z=\alpha I_d+\beta v_0v_0^{\mathsf T}.
\]
The eigenvalues of \(Z\) are \(t\) along \(v_0\) and \(\alpha>0\) on its orthogonal complement, so \(Z\) is positive definite, including when \(\beta<0\). Direct use of \(v_0^{\mathsf T}v_i=-1/d\) yields \(v_0^{\mathsf T}Zv_0=t\) and \(v_i^{\mathsf T}Zv_i=1\) for every \(i\ge1\). Its trace is
\[
\operatorname{tr}Z=\frac{d(d+t)}{d+1}.
\tag{2}
\]
The covering vector \(z_i=d/(d+1)\) for all indices makes (P)'s matrix exactly \(I_d\) by (1), and has cost equal to (2). Both sides are therefore optimal.

For \(t\ge d^2\), take instead \(Z=d^2v_0v_0^{\mathsf T}\). It is dual-feasible because \(v_0^{\mathsf T}Zv_0=d^2\le t\), and for \(i\ge1\), \(v_i^{\mathsf T}Zv_i=1\). Its trace is \(d^2\). The covering vector \(z_0=0\), \(z_i=d\) for \(i\ge1\), has cost \(d^2\) and satisfies
\[
\sum_{i=1}^d d\,v_iv_i^{\mathsf T}-I_d\succeq0:
\]
the left side has eigenvalue zero along \(v_0\) and eigenvalue \(d\) with multiplicity \(d-1\) on \(v_0^\perp\). Thus the optimum covering price is \(d^2\) in this regime. Reciprocating (2) and this value establishes the stated objective formula, including agreement at \(t=d^2\).

**3. All equality cases, without symmetrizing variables.** For \(0<t<d^2\) the exhibited dual matrix is positive definite. Equality in weak duality requires the positive-semidefinite covering slack to be zero, that is, \(\sum_i z_iv_iv_i^{\mathsf T}=I_d\). The \(d+1\) symmetric matrices \(v_iv_i^{\mathsf T}\) are linearly independent: their Frobenius Gram matrix has diagonal entries one and off-diagonal entries \(1/d^2\), hence eigenvalues \(1-1/d^2>0\) (multiplicity \(d\)) and \(1+1/d>0\) (multiplicity one). Therefore \(z_i=d/(d+1)\) is the **only** covering optimum, yielding unique uniform \(p\).

For \(t\ge d^2\), complementary slackness against \(Z=d^2v_0v_0^{\mathsf T}\) implies the covering slack annihilates \(v_0\):
\[
\left(\sum_i z_iv_iv_i^{\mathsf T}-I_d\right)v_0=0.
\]
Using \(v_0=-\sum_{i=1}^dv_i\), and the linear independence of \(v_1,\ldots,v_d\), gives exactly
\[
 z_i=d(1-z_0)\quad(1\le i\le d).
\tag{3}
\]
The covering slack is zero along \(v_0\) and has common orthogonal eigenvalue \((d+1)(1-z_0)-1\). Thus feasibility is **equivalent** to \(0\le z_0\le d/(d+1)\). For \(t>d^2\), the expensive-row dual constraint is slack, forcing \(z_0=0\), and the covering optimum is unique. At \(t=d^2\), all \(z_0\) in this interval attain cost \(d^2\). Dividing \(z\) by \(\sum_jz_j\) recovers the stated one-parameter family \(0\le p_0\le1/(d+1)\). This also proves that no nonsymmetric or otherwise unlisted optimum exists.

## Verification

The accompanying standalone Python 3 program `check.py` uses only the standard library. Its rational ambient-space realization of the regular simplex checks all matrix identities, dual constraints, exact budget, complementary slack, and all principal minors of primal/dual positive-semidefinite certificates for \(2\le d\le8\) over eight rational prices per dimension (56 tests), including prices on both sides of and at the boundary. Its output is `VERIFY_OK 56 exact simplex primal-dual cases; all principal minors checked`. Finite cases are supporting checks, not a replacement for the preceding proof in arbitrary dimension and arbitrary real \(t>0\).

A concrete check: at \(d=3\) and \(t=4\), all four rows are sampled with probability \(1/4\), yielding \(\eta^*=4/21\); at \(d=3\) and \(t=12\), only the three inexpensive rows are sampled, each with probability \(1/3\), yielding \(\eta^*=1/9\). At \(t=9\), every distinguished-row probability in \([0,1/4]\) is optimal.

## Relationship to prior work

Strohmer and Vershynin developed the original randomized Kaczmarz rate analysis. Dai, Soltanalian, and Pelckmans derive the **general unpriced** semidefinite optimization of one-step randomized Kaczmarz sampling probabilities; in particular, their equations (15)–(17) optimize the same least-eigenvalue numerator with a single unit cost per row. Gower and Richtárik present a broader sketch-and-project optimal-sampling SDP, again without the heterogeneous per-row cost ratio in the stated formulation. Consequently, the SDP methodology and the unpriced uniform-simplex special case are **not** claimed as new. The contribution assessed here is the explicit price-dependent solution and complete equality classification for the minimal redundant simplex frame, including its sharp quadratic deletion threshold. A separate analysis of exact multistep mean-square decay can produce a different objective and is not inferred from this theorem.

## Limitations

The guarantee is for the sharp **single-step worst-initialization mean-square decrease per expected action cost**; it is not a proven optimal rate per realized wall time or a complete multistep performance comparison. The full result requires the unit regular-simplex row geometry and one exceptional row price, not arbitrary frames or many heterogeneously priced rows. The general convex formulation substantially predates this calculation; an overlooked explicit historical specialization remains possible. In particular, the full text of a relevant 2014 conference contribution on exact MSE and optimal sampling was not accessible, so no claim of its complete noncoverage is made. The analytical proof covers all real prices \(t>0\) and all integer dimensions \(d\ge2\); the executable checker covers only the stated finite rational cases.

## References

1. T. Strohmer and R. Vershynin, *A randomized Kaczmarz algorithm with exponential convergence*, arXiv:math/0702226v1, first version 2007-02-08. https://arxiv.org/html/math/0702226v1
2. L. Dai, M. Soltanalian, and K. Pelckmans, *On the Randomized Kaczmarz Algorithm*, arXiv:1402.2863v1, 2014-02-12, especially Section II, equations (15)–(17). https://arxiv.org/html/1402.2863v1
3. R. M. Gower and P. Richtárik, *Randomized Iterative Methods for Linear Systems*, arXiv:1506.03296, first version 2015-06-10, Section 5.1. https://arxiv.org/html/1506.03296v5
4. A. Agaskar, C. Wang, and Y. M. Lu, *Randomized Kaczmarz algorithms: Exact MSE analysis and optimal sampling probabilities*, 2014 IEEE GlobalSIP conference, DOI:10.1109/GlobalSIP.2014.7032145; complete paper not inspected.
