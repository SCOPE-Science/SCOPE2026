# Five-step dwell is the sharp small-stepsize stabilization threshold for sign-switched reflected gradient

## Finding

For a linear monotone variational inequality with two alternating, sign-opposite planar rotations, the stability of a reflected-gradient algorithm changes at an exact integer switching-dwell threshold. Write
\[
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad F_+(z)=LJz,\qquad F_-(z)=-LJz,\qquad L>0.
\]
Fix an integer \(m\ge1\). Apply \(F_+\) for \(m\) consecutive updates, then \(F_-\) for \(m\) consecutive updates, and repeat this block schedule indefinitely. With \(a=hL>0\), perform the *current-operator reflected-point* recurrence
\[
z_{k+1}=z_k-hF_{s_k}(2z_k-z_{k-1}),\qquad s_k\in\{+,-\}.
\]
The following dichotomy is exact:

1. For every \(m\in\{1,2,3,4\}\) and **every** \(a>0\), the \(2m\)-step monodromy has spectral radius greater than one. There exist real initial pairs whose errors grow exponentially at complete periods.
2. For each fixed integer \(m\ge5\), there exists \(\varepsilon_m>0\) such that for every \(0<a<\varepsilon_m\) and **every** pair of real initial states, the iterates converge exponentially to the common equilibrium \(z=0\).

For each integer \(m\ge2\), the two eigenvalues of the complexified period map, labeled so that \(\lambda_+(0)=1\) and \(\lambda_-(0)=0\), satisfy
\[
\lambda_+(a)=1+(4-m)a^2+O_m(a^4),\qquad \lambda_-(a)=O(a^{2m}).
\]
At the delicate boundary \(m=4\), the sharper result is \(\lambda_+(a)=1+2a^4+O(a^8)\). When \(m=1\), it is \(\lambda_+(a)=1+3a^2+O(a^4)\). Thus \(m=5\) is the **minimal dwell for small-step stabilization** within this precisely specified balanced switching family.

## Assumptions and scope

The state space is \(\mathbb R^2\), the initial pair \((z_{-1},z_0)\) is unrestricted, arithmetic is exact, \(L\) is any strictly positive constant and the fixed stepsize \(h\) has normalized value \(a=hL\). The operators \(F_+\) and \(F_-\) are each monotone, \(L\)-Lipschitz and share exactly the root \(0\), because \(J^\mathsf T=-J\), \(J^2=-I\), and \(\det J=1\). Switching takes place after equal blocks of exactly \(m\) updates; the sign changes instantly and cyclically. The operator at step \(k\) acts on **both** current and reflected past iterates. This differs from the usual time-varying optimistic rule with a *previous-operator* past-gradient term.

Convergence means exponential decay of the entire two-state recurrence for all initial pairs. Instability means an expanding period-map eigenvalue and therefore the existence of exponentially growing real initial pairs; it does not mean that every initial pair grows. The stability threshold for \(m\ge5\) is asymptotic in \(a\) at each *fixed* \(m\), not uniform in unbounded \(m\).

## Proof

**1. Two-dimensional transfer matrix.** Identify \(\mathbb R^2\) with \(\mathbb C\), so \(J\) becomes multiplication by \(i\). For sign \(s\in\{+1,-1\}\), the update becomes
\[
w_{k+1}=(1-2isa)w_k+isa\,w_{k-1}.
\]
Its state transfer matrix and one complete period matrix are
\[
T_s(a)=\begin{pmatrix}1-2isa&isa\\1&0\end{pmatrix},\qquad M_m(a)=T_{-1}(a)^mT_{+1}(a)^m.
\]
The real four-dimensional state transfer is the realification of this complex matrix. In particular, its spectral radius equals that of \(M_m\). A complex eigenpair of \(M_m\) yields a real eigenpair or a real invariant plane with the same exponential growth modulus.

**2. Exact characteristic polynomial.** Put \(u_0=0\), \(u_1=1\), and
\[
u_{j+1}=(1-2ia)u_j+ia\,u_{j-1}\qquad (j\ge1).
\]
Direct induction gives
\[
T_{+1}(a)^m=\begin{pmatrix}u_{m+1}&ia\,u_m\\u_m&ia\,u_{m-1}\end{pmatrix}.
\]
Since \(T_{-1}(a)=\overline{T_{+1}(a)}\), the trace of their product is **real**:
\[
\tau_m(a)=\operatorname{tr}M_m(a)=|u_{m+1}|^2+a^2|u_{m-1}|^2.
\]
Also \(\det T_{+1}=-ia\) and \(\det T_{-1}=ia\), hence
\[
\det M_m(a)=a^{2m},\qquad
p_m(\lambda)=\lambda^2-\tau_m(a)\lambda+a^{2m}.
\]
No assertion of normality or commutation of differently signed transfers is needed.

**3. The four short dwell lengths are always unstable.** Expanding the finite polynomial recurrence gives the following *exact*, not asymptotic, values:
\[
\begin{array}{c|l}
m&p_m(1)\\\hline
1&-3a^2\\
2&-a^2(2+15a^2)\\
3&-a^2(1+4a^2+63a^4)\\
4&-a^4(2+255a^4)
\end{array}
\]
Every entry is strictly negative for \(a>0\). As \(p_m\) is a real monic quadratic and \(p_m(\lambda)\to+\infty\) as real \(\lambda\to+\infty\), it has a real zero greater than \(1\). Therefore the period map has spectral radius \(>1\), proving the first assertion for all \(a>0\), including arbitrarily small stepsizes.

**4. Small steps when the dwell is at least five.** From the recursion, by induction for every integer \(n\ge3\),
\[
u_n=1-ina-\left(\frac{n(n+1)}2-2\right)a^2+O_n(a^3).
\]
For \(m\ge2\), substituting this into the trace formula yields
\[
|u_{m+1}|^2=1+(3-m)a^2+O_m(a^4),\qquad
\tau_m(a)=1+(4-m)a^2+O_m(a^4).
\]
The remainder is even because \(u_n(-a)=\overline{u_n(a)}\) for real \(a\). At \(a=0\), the polynomial \(p_m\) has distinct roots \(1\) and \(0\). Elementary analytic perturbation of these simple roots gives
\[
\lambda_+(a)=1+(4-m)a^2+O_m(a^4),\qquad
\lambda_-(a)=a^{2m}/\lambda_+(a)=O(a^{2m}).
\]
For each fixed \(m\ge5\), the first root is strictly less than \(1\) and remains positive when \(a>0\) is sufficiently small; the second root also lies in \((0,1)\). The spectral radius is therefore strictly below one, proving exponential convergence of the real recurrence for all real initial pairs. At \(m=4\), the exact trace \(\tau_4=1+2a^4+256a^8\) and determinant \(a^8\) instead give \(\lambda_+=1+2a^4+O(a^8)\); at \(m=1\), \(\tau_1=1+4a^2\) and determinant \(a^2\) give \(\lambda_+=1+3a^2+O(a^4)\).

The two conclusions together show the integer threshold \(m=5\) is both necessary and sufficient for the *existence of a small positive fixed-stepsize stability interval* within this balanced sign-switching family. \(\square\)

## Verification

A standalone `check.py` uses exact integer-polynomial arithmetic to independently construct the recurrence and period traces, verify every displayed polynomial for \(m=1,2,3,4\), and check the \(a^2\) trace coefficient for \(m=2,\ldots,20\). It also computes 4-by-4 real period matrices by realification and checks representative Floquet eigenvalues numerically for dwell lengths \(m=1,\ldots,12\) and small step values. The analytical proof, rather than those finite computations, establishes the infinite-parameter statements.

## Relationship to prior work

Nguyen, Trinh and Vuong established an optimal constant-operator stepsize bound \(h<1/(\sqrt3L)\) for unconstrained Popov/reflected-gradient iteration and explicitly give the reflected-point form of the recurrence (their equation (7)). That theorem fixes a *single* operator; it does not imply any stability of products involving alternately signed operators. Here each frozen operator belongs to their convergent regime for sufficiently small \(a\), but the switching system diverges for dwell \(m\le4\).

Feng and collaborators analyzed periodic zero-sum games with extra-gradient and *time-varying optimistic gradient*, including a period-two divergence example. In the time-varying setting, the past term in their optimistic update uses the **previous** game operator, while the present theorem uses the **current** game operator on the reflected point, so neither their algorithmic recurrence nor their period-two claim entails the all-dwell classification proved here.

Chen and Yu's 2026 work on reflected and optimistic algorithms in time-varying games does state that reflected gradient can diverge in some periodic examples. That establishes a broad qualitative precedent for switching failures. The explicit dichotomy for **every** positive stepsize at all four short dwell lengths versus existence of a convergent small-stepsize regime for **each** longer dwell length, with the exact threshold five, is more specific than this inspected abstract. The paper's complete text was not accessible during the comparison; a possible unlocated equivalent theorem remains a publication-overlap risk.

## Limitations

The theorem is not a convergence guarantee for arbitrary monotone-operator switching or general periodic games; the matrices are exactly opposite planar rotations, the two dwell blocks have equal integer length, and the same step is used throughout. It does not characterize the largest stable step when \(m\ge5\), numerical rounding effects, bounded constrained games, or nonlinear operators. The usual optimistic-gradient algorithm with a past-operator term is a different update on a changing game. Full inspection of one highly related 2026 manuscript was unavailable, and equivalent older switched-system formulations may exist.

## References

1. N. H. Nguyen, T. Q. Trinh, and P. T. Vuong, *The Popov's Algorithm with Optimal Bounded Stepsize for Generalized Monotone Variational Inequalities*, arXiv:2603.06442, first submitted 2026-03-06; v2 of 2026-10-13, equation (7), https://arxiv.org/html/2603.06442v2 .
2. Y. Feng, H. Fu, Q. Hu, P. Li, I. Panageas, B. Peng, and X. Wang, *On the Last-iterate Convergence in Time-varying Zero-sum Games: Extra Gradient Succeeds where Optimism Fails*, NeurIPS 2023, arXiv:2310.02604, https://arxiv.org/abs/2310.02604 .
3. Y. Chen and J. Yu, *Similarity and Separation of Last-Iterate Convergence between Optimism and Reflected Algorithms in Time-Varying Games*, ICLR 2026, public abstract and inaccessible full text, https://openreview.net/forum?id=AxhWmQBRRg .
