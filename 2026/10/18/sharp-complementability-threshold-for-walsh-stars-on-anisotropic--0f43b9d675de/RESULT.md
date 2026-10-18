# Sharp complementability threshold for Walsh stars on anisotropic Hamming cubes

## Finding

For each integer \(m\ge2\) and each real weight \(w>0\), let \(M=\{-1,1\}^{m+1}\) with the weighted Hamming path metric
\[
d_w(x,y)=w\mathbf1_{x_0\ne y_0}+\sum_{j=1}^{m}\mathbf1_{x_j\ne y_j}.
\]
Fix any basepoint \(o\in M\), and give the real Banach space \(X_w=\operatorname{Lip}_0(M,d_w)\) its Lipschitz norm. Put \(\chi_{0j}(x)=x_0x_j\) and let \(Y\subseteq X_w\) be the span of the \(m\) functions \(\chi_{0j}-\chi_{0j}(o)\), for \(1\le j\le m\). If \(\lambda(Y,X_w)\) is the infimum of norms of all bounded linear projections from \(X_w\) onto \(Y\), then, writing \(S_m=\varepsilon_1+\cdots+\varepsilon_m\) for independent uniform signs, one has
\[
\boxed{\lambda(Y,X_w)=\max\!\left\{1,\frac{\mathbb E[|S_m|\min\{|S_m|,w\}]}{w}\right\}}
=\max\!\left\{1,\frac{1}{2^mw}\sum_{k=0}^m\binom{m}{k}|m-2k|\min\{|m-2k|,w\}\right\}.
\]
The ordinary Walsh Fourier projection onto the indicated spectrum attains this infimum over **all** projections. In particular, for \(m\ge3\), this spectral subspace is the range of a norm-one projection if and only if \(w\ge m\). For \(m=2\), the projection norm equals one for every \(w>0\). In dimension four (\(m=3\)), the constant is \(3/2\) for \(0<w\le1\), \(3(w+1)/(4w)\) for \(1\le w\le3\), and one for \(w\ge3\). The same minimum projection norm holds for the adjoint projection onto its range in the finite-dimensional real Lipschitz-free space \(\mathcal F(M)\).

## Assumptions and scope

All scalars are real; \(m\) is an arbitrary finite integer at least two, \(w\) is an arbitrary positive real number, and the other \(m\) edge weights are exactly one. Basepoint changes do not alter the projection constant. The norm \(\|f\|_{\operatorname{Lip}}\) equals the maximum of the absolute difference quotients on the \((m+1)2^m\) individual coordinate edges: the metric is their shortest-path metric. The projection invariant is relative to \(\operatorname{Lip}_0(M,d_w)\), not the absolute projection constant of \(Y\).

## Proof

**1. Reduction to the Fourier projection.** Regard Lipschitz functions modulo constants as the translation-invariant finite-dimensional Banach space \(X_w\). For a group element \(a\in M\) let \(U_a f(x)=f(ax)-f(ao)\). Each \(U_a\) is an isometry, and \(Y\) is invariant under all \(U_a\). Averaging an arbitrary projection \(R:X_w\to Y\) over conjugates \(U_a^{-1}RU_a\) yields a projection of no larger norm commuting with translations. The nonconstant Walsh characters form distinct one-dimensional simultaneous eigenspaces of the translations; consequently the only commuting projection onto \(Y\) is \(Q\), the Fourier multiplier retaining exactly the characters \(\chi_{0j}\), followed by subtraction of the value at \(o\). Thus \(\lambda(Y,X_w)=\|Q\|\).

**2. The light-coordinate bounds.** For each coordinate \(j\ge1\), write \(x^{(j)}\) for the vertex with that coordinate flipped. The difference \(Qf(x)-Qf(x^{(j)})\) receives contributions from only the term \(\chi_{0j}\). Since Fourier projection onto a single Walsh character is a contraction in the supremum norm,
\[
\sup_x |Qf(x)-Qf(x^{(j)})|\le \sup_x |f(x)-f(x^{(j)})|\le\|f\|_{\operatorname{Lip}}.
\]
Hence each light-coordinate Lipschitz quotient of \(Qf\) is at most \(\|f\|_{\operatorname{Lip}}\).

**3. The heavy-coordinate variational problem.** The antisymmetrizer in the heavy coordinate, \(Af=(f-f\circ\tau_0)/2\), is a contraction in the Lipschitz seminorm, and \(QAf=Qf\). After dropping an irrelevant constant, write \(Af(x_0,y)=x_0g(y)\) for \(y\in\{-1,1\}^m\). The condition \(\|Af\|_{\operatorname{Lip}}\le1\) is equivalent to the following two families of inequalities:
\[
|g(y)|\le w/2,\qquad |g(y)-g(y^{(j)})|\le1\quad(1\le j\le m).
\]
Conversely every such \(g\) produces a unit-Lipschitz function after subtracting its value at \(o\). Write \(P_1g=\sum_{j=1}^m\widehat g(\{j\})y_j\). Then \(Q(x_0g)(x_0,y)=x_0P_1g(y)\), and the maximal heavy-edge quotient is \(2\|P_1g\|_\infty/w\).

Coordinate sign changes allow evaluation of \(P_1g\) at \(y=(1,\ldots,1)\), where \(P_1g(1,\ldots,1)=\mathbb E[S_mg]\), with \(S_m(y)=\sum_jy_j\). Permutation averaging and the norm-preserving operation \(g(y)\mapsto-g(-y)\) preserve this objective and the constraints; we may therefore suppose \(g\) depends only on the number \(k\) of negative coordinates, with values \(g_k=-g_{m-k}\).

For \(k<m/2\), choose vertices on levels \(k\) and \(m-k\) whose negative-coordinate sets are nested. They are joined by a path of length \(m-2k\); the light-edge constraints yield \(2|g_k|\le m-2k\). Together with the heavy-edge constraint this gives \(g_k\le\frac12\min\{w,m-2k\}\). Because the coefficient of \(g_k\) in \(\mathbb E[S_mg]\) is positive at these levels, symmetry and this pointwise bound imply
\[
\mathbb E[S_mg]\le\frac12\mathbb E[|S_m|\min\{|S_m|,w\}].
\]
The bound is attained simultaneously at every level by the explicit clipped affine function
\[
g_*(y)=\frac12\operatorname{sgn}(S_m(y))\min\{|S_m(y)|,w\},
\]
with value zero when \(S_m=0\). Indeed \(|g_*|\le w/2\), and flipping one light coordinate changes \(S_m\) by two, so the truncated map changes by at most one. This proves the exact maximal heavy-coordinate quotient \(\mathbb E[|S_m|\min\{|S_m|,w\}]/w\). Taking the maximum with the light-coordinate bound and with \(\|Q\|\ge1\) gives the asserted formula.

**4. Sharp norm-one threshold.** If \(w\ge m\), then \(|S_m|\le m\) and \(\mathbb E S_m^2=m\), so the heavy quotient is \(m/w\le1\). For \(m=2\), the absolute random sum takes only values zero and two, giving a quotient at most one at every weight. If \(m\ge3\), \(\mathbb E|S_m|>1\) (already \(3/2\) at \(m=3\) and nondecreasing thereafter). The heavy quotient is nonincreasing in \(w\), and for weights immediately below \(m\) it is strictly larger than one: the event \(|S_m|=m-2>0\) has positive probability and its contribution grows strictly when \(w\) decreases from \(m\). Hence it exceeds one for every \(0<w<m\). The displayed three-branch formula for \(m=3\) follows by evaluating the two nonzero magnitudes \(|S_3|=1,3\).

**5. Adjoint statement.** The finite-dimensional dual of \(\operatorname{Lip}_0(M)\) is \(\mathcal F(M)\). Adjoints preserve operator norms, and taking adjoints gives a one-to-one correspondence between projections onto \(Y\) and projections onto \(\operatorname{ran}(Q^*)\) that have the corresponding annihilator kernel; the norm of the explicit adjoint projection equals the minimum just proved. Conversely any projection onto \(\operatorname{ran}(Q^*)\) can be averaged under the dual group action and then must equal \(Q^*\), as its range consists of the corresponding Walsh eigenfunctionals. Hence the unrestricted minimum on this specified dual spectral subspace is the same.

## Verification

The proof above establishes the universal result without relying on a finite search. The accompanying standalone Python program independently constructs the Fourier projection matrix and the full weighted cube edge constraints, then solves a primal linear program for each of two symmetry-representative edge directions. It matched the formula on \(24\) full finite-dimensional instances for \(m=2,3,4,5\) and six weights per dimension (\(48\) edge-direction programs). The calculation uses floating-point optimization and is supplementary, not an exact or infinite certificate. Execute `python verify_weighted_walsh.py` with NumPy and SciPy available.

## Relationship to prior work

Theorem 8.1.1 in Defant–Galicer–Mansilla–Mastyło–Muro, *Projection constants for spaces of multivariate polynomials* (first available 12 August 2022), and Theorem 3.1 in their subsequent *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces* (first available 1 February 2023), determine Fourier projection constants under the **supremum norm** on the cube. Their formula does not change with a weighted Hamming metric and does not imply the current relative Lipschitz projection constants. The unit-weight slice of the displayed formula reduces to the classical Rademacher absolute first moment, but the new parameter dependence and the exact \(w=m\) contractive-complementability transition cannot be inferred from that slice alone. Hájek–Russo study Lipschitz polynomial projections on *continuous Banach balls*, with a different domain and different complementability assertions. The metric-edge constraint and its clipped extremizer supply the additional analysis here.

## Limitations

The theorem does not cover complex-valued Lipschitz functions, arbitrary unequal weights on the light coordinates, or general Fourier support families. No classification of all minimising projections is asserted; only their minimal norm and a canonical minimiser are proved. Finite computation cannot establish the universal quantifiers. Although targeted published-literature searches and direct full-text comparisons found no covering formula, equivalent results in unindexed literature remain possible. Independent review has not been performed.

## References

1. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Projection constants for spaces of multivariate polynomials*, arXiv:2208.06467, version 1 (2022-08-12), Chapter 8, Theorem 8.1.1. https://arxiv.org/abs/2208.06467
2. A. Defant, D. Galicer, M. Mansilla, M. Mastyło and S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233, version 1 (2023-02-01), Theorem 3.1. https://arxiv.org/abs/2302.00233
3. P. Hájek and T. Russo, *Projecting Lipschitz functions onto spaces of polynomials*, arXiv:2102.02778, version 1 (2021-02-04), Theorems A and B. https://arxiv.org/abs/2102.02778
