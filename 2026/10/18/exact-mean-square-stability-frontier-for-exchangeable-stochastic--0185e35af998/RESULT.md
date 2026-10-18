# Exact mean-square stability frontier for exchangeable stochastic competition linearizations

## Finding

**Theorem.** Let \(s\geq2\) be an integer and let \(\alpha>0\), \(\beta>c\geq0\), and \(D,H\geq0\). Set
\[
L=\beta+(s-1)c,\qquad B=\beta+(s-2)c,\qquad r=\frac{\alpha}{L},\qquad \delta=D+(s-1)H.
\]
Let \(E_{ij}\) be the standard matrix units and \(\{W_{ij}:1\leq i,j\leq s\}\) independent standard Brownian motions. For the real Itô system
\[
 dX=-r[(\beta-c)I_s+c\mathbf1\mathbf1^{\mathsf T}]X\,dt
 -r\sqrt{2D}\sum_{i=1}^{s}E_{ii}X\,dW_{ii}
 -r\sqrt{2H}\sum_{i\ne j}E_{ij}X\,dW_{ij},
\]
the zero solution is uniformly exponentially stable in mean square (that is, there are \(C,\kappa>0\) such that \(\mathbb E\|X(t)\|^2\leq C e^{-\kappa t}\|X(0)\|^2\) for all deterministic initial vectors and \(t\geq0\)) **if and only if**
\[
\boxed{\alpha\,[D+(s-1)H]\,[\beta+(s-2)c] < (\beta-c)[\beta+(s-1)c]^2.}\tag{1}
\]
At equality there is no mean-square decay for all initial vectors; when the inequality is reversed, some deterministic initial vector has exponentially growing second moment. More precisely, the sharp uniform second-moment growth exponent is
\[
\boxed{\lambda_+=r\!\left[-\beta-B+r\delta+
 \sqrt{(B-\beta+r\delta)^2+4c^2(s-1)}\right].}\tag{2}
\]
Here “sharp exponent” means
\[
\lim_{t\to\infty}\frac1t\log\left(
\sup_{\|x\|=1}\mathbb E\|X(t;x)\|^2\right)=\lambda_+.
\]
For \(c>0\), condition (1) permits a strictly larger noise range than the bound \(\alpha\delta/L<\beta-c\) given as necessary and sufficient in Eq. (11) of Zheng et al. (2026). The respective critical values of \(\delta\) differ by the exact factor \(L/B>1\).

**An admissible two-species distinction.** Take \(s=2\), \(\alpha=1\), \(\beta=2\), \(c=1\), \(D=0\), \(H=4\). The published inequality fails because \(4/3>1\), whereas (1) holds, since \(8<9\). The actual second-moment eigenvalues are \((-8\pm2\sqrt{13})/9\), both negative; the remaining antisymmetric second-moment eigenvalue is \(-20/9\). Thus the printed criterion excludes an exponentially mean-square stable two-species system. In the source's critical-diversity parameter regime, its Eq. (12) yields \(s_c=5/3\), whereas the exact positive real transition is \(s_c=1+2\sqrt3/3\); hence the two-species system is stable and the three-species system unstable.

## Assumptions and scope

This is an exact statement about the homogeneous linear **Itô** SDE in Eq. (10) of Zheng et al., with the independent diagonal and off-diagonal Brownian channels printed there. Their notation corresponds to \(c=C\gamma\), \(D=\mathcal D\), \(H=\mathcal H\), and \(r=n^*\). Parameters can have zero noise strengths and \(c=0\); only \(\beta>c\), \(s\ge2\), \(\alpha>0\) are required. The integer \(s\) counts species, not sample paths. The theorem does not identify stability for a nonlinear stochastic Lotka–Volterra model, does not assert existence or nonexistence of its stationary probability measures, and does not apply to Stratonovich reinterpretations or correlated Brownian channels.

## Proof

**1. Exact moment lift.** For a deterministic initial \(x\) let \(K(t)=\mathbb E[X(t)X(t)^{\mathsf T}]\), and write \(A=-r[(\beta-c)I_s+c\mathbf1\mathbf1^{\mathsf T}]\). Itô's product formula and independence of all noises give the closed, deterministic matrix equation
\[
\dot K=AK+KA^{\mathsf T}
+2r^2\operatorname{diag}_{1\le i\le s}
 \left(DK_{ii}+H\sum_{j\ne i}K_{jj}\right).
\tag{3}
\]
Here \(\operatorname{diag}_i(a_i)\) is the diagonal matrix with entries \(a_i\). Identity (3) follows from \(E_{ij}KE_{ij}^{\mathsf T}=K_{jj}E_{ii}\). It is not an approximation to this linear Itô system.

**2. Permutation-invariant reduction.** Introduce the positive linear second-moment flow \(\Phi_t\) associated to (3). Since every \(X(t;x)X(t;x)^{\mathsf T}\) is positive semidefinite, \(\Phi_t\) preserves the positive-semidefinite cone. Moreover, \(\Phi_t\) commutes with simultaneous coordinate permutations. Hence for the initial covariance \(K(0)=I_s\), the solution has one common diagonal entry \(u(t)\), one common off-diagonal entry \(v(t)\), with \((u(0),v(0))=(1,0)\). Substitution in (3) gives exactly
\[
\begin{pmatrix}\dot u\\\dot v\end{pmatrix}
=2r\begin{pmatrix}
-\beta+r\delta&-c(s-1)\\
-c&-B
\end{pmatrix}\begin{pmatrix}u\\v\end{pmatrix}.
\tag{4}
\]
This two-dimensional system suffices for **all** deterministic initial vectors: since \(xx^{\mathsf T}\preceq\|x\|^2I_s\), positivity yields
\[
0\leq\mathbb E\|X(t;x)\|^2\leq\|x\|^2\operatorname{tr}\Phi_t(I_s)=s u(t)\|x\|^2.
\tag{5}
\]
Conversely \(\operatorname{tr}\Phi_t(I_s)=\sum_{i=1}^s\mathbb E\|X(t;e_i)\|^2\). Thus uniform mean-square exponential stability is equivalent to exponential decay of \(u(t)\), not merely to a sufficient norm-drift bound.

**3. Sharp spectral frontier.** The matrix in (4) has real eigenvalues, whose larger value is (2). For \(c>0\), its larger eigenvalue strictly exceeds both diagonal entries, and its smaller eigenvalue lies strictly below both. The initial vector \((1,0)\) has a strictly positive coefficient along the larger eigenmode, as may be seen by writing
\[
u(t)=a_+e^{\lambda_+t}+(1-a_+)e^{\lambda_-t},\qquad
 a_+=\frac{2r(-\beta+r\delta)-\lambda_-}{\lambda_+-\lambda_-}\in(0,1).
\]
For \(c=0\), the equation for \(u\) decouples and \(u(t)=e^{(-2r\beta+2r^2\delta)t}\), which is also (2). The squared-norm operator \(Q_t\), defined by \(x^{\mathsf T}Q_t x=\mathbb E\|X(t;x)\|^2\), has \(\operatorname{tr}Q_t=s u(t)\). Its largest eigenvalue lies between \(u(t)\) and \(s u(t)\), proving the sharp exponent assertion.

The determinant of the matrix in (4), after removal of the positive common factor \((2r)^2\), is
\[
 B(\beta-r\delta)-c^2(s-1)
=\frac{(\beta-c)L^2-\alpha\delta B}{L}.
\tag{6}
\]
When (6) is positive, the upper-left entry is negative and the trace is strictly negative, so \(\lambda_+<0\). When (6) vanishes, \(\lambda_+=0\); when negative, \(\lambda_+>0\). Equations (5) and (6) prove (1), its boundary assertions, and (2).

**4. Source comparison and exact witness.** The published bound is \(\delta<(\beta-c)L/\alpha\), whereas (1) is \(\delta<(\beta-c)L^2/(\alpha B)\). Since \(L=B+c\), the first is strictly stronger whenever \(c>0\). For the stated two-species witness, the \((u,v)\) matrix is
\[
\begin{pmatrix}-4/9&-2/3\\-2/3&-4/3\end{pmatrix},
\]
with trace \(-16/9\), determinant \(4/27\), and eigenvalues \((-8\pm2\sqrt{13})/9\). The remaining antisymmetric moment mode decays with rate \(-20/9\). Finally, substitution into the sharp criterion gives the continuous boundary polynomial \(-3s^2+6s+1\), whose unique root exceeding one is \(1+2\sqrt3/3\), whereas direct substitution into the source's Eq. (12) gives \(5/3\). At integer \(s=2\), stable; at \(s=3\), unstable.

## Verification

Run `python verify.py` with Python's standard library. The executable checks 84 independently computed full-moment-lift identities against the exchangeable reduction using exact rational arithmetic; 632 additional trace/determinant stability comparisons; and the exact two-species rational witness, including its eigenvalues and the distinct diversity thresholds. These finite tests check arithmetic, not the infinite-dimensional-in-time claim. The theorem's general validity is established by (3)–(6).

## Relationship to prior work

Zheng et al. (arXiv:2608.30655v1, Eqs. (10)–(12)) explicitly formulate the same exchangeable linear Itô SDE and give \(\alpha\delta/L<\beta-c\) as an **if and only if** mean-square stability condition, then derive a diversity threshold from it. The present theorem identifies the exact missing stabilizing contribution of dynamically induced negative cross-covariance, proves a sharp replacement for their linear-system criterion, and supplies parameters for which the two predictions disagree at integer species count.

The general second-moment/lift approach for linear stochastic equations is classical; see Bishop and Del Moral and the literature on mean-square destabilization surveyed by Senosiain and Tocino. Those general tools motivate (3), but the concrete two-coordinate reduction, sharp closed boundary, and disagreement with this source's claimed necessity are not stated in the compared accessible material. Valenti et al. study a distinct spatial, time-correlated, two-species stochastic Lotka–Volterra setting, not the same independent matrix-Brownian linearization. An equivalent calculation in less easily searchable stochastic-stability literature cannot be excluded.

## Limitations

The claim is confined to the stochastic **linearization** (the homogeneous multiplicative Itô SDE), not the nonlinear population process. The Gaussian white-noise model may be an imperfect description of physical interactions at large noise strength. Nothing here establishes global ecological persistence, nonlinear equilibrium stability, or extinction probabilities. The sharp real-valued threshold in a species-number formula must be converted to allowed integer values with the strict inequality. Literature indexing is imperfect; the originality assessment is subject to independent expert priority review.

## References

1. X.-d. Zheng, C. Li, H. Zhang, H.-j. Qiao, S.-p. Wang, and Y. Tao, *Dimensionality-induced critical phase transition in stochastic Lotka–Volterra equation: From statistical averaging to systemic tipping point*, arXiv:2608.30655v1, first posted 2026-08-31. https://arxiv.org/abs/2608.30655
2. A. N. Bishop and P. Del Moral, *Stability Properties of Systems of Linear Stochastic Differential Equations with Random Coefficients*, arXiv:1804.09349v2. https://arxiv.org/html/1804.09349v2
3. M. J. Senosiain and A. Tocino, *A survey of mean-square destabilization of multidimensional linear stochastic differential systems with non-normal drift*, Numerical Algorithms (2023), DOI: 10.1007/s11075-022-01478-6.
4. D. Valenti, L. Schimansky-Geier, X. Sailer, B. Spagnolo, and M. Iacomi, *Moment equations in a Lotka–Volterra extended system with time correlated noise*, arXiv:cond-mat/0611358 (2006).
