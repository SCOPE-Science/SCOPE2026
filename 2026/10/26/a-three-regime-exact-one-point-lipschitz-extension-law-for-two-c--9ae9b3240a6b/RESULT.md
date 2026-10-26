# A three-regime exact one-point Lipschitz extension law for two-cluster ultrametrics

## Finding
Let \(A\) and \(B\) be disjoint sets of respective cardinalities \(p,q\ge2\). On \(X=A\sqcup B\), put distance \(s\in(0,1]\) between distinct elements of \(A\), distance \(t\in(0,1]\) between distinct elements of \(B\), and distance \(1\) across the two clusters. Adjoin one point \(o\) with common distance \(R>0\) to every point of \(A\), and common distance \(U>0\) to every point of \(B\). Assume precisely the metric compatibility conditions
\[
 2R\ge s,\qquad 2U\ge t,\qquad |R-U|\le1\le R+U.
\]
Define the two mean intracluster distances
\[
 k=s\left(1-\frac1p\right),\qquad \ell=t\left(1-\frac1q\right),
\]
so \(0<k,\ell<1\). The sharp least constant sufficient to extend **every** Lipschitz map \(f:X\to E\), for **every real Banach space** \(E\), to \(X\cup\{o\}\), equals the least norm of a real-linear, constant-preserving scalar Lipschitz extension. This common constant is
\[
 \boxed{\Lambda=\max\{1,T\}},\qquad
 T=\begin{cases}
 \ell/U,&U\le R\ell,\\[2pt]
 \dfrac{1-k\ell}{U(1-k)+R(1-\ell)},&R\ell\le U\le R/k,\\[7pt]
 k/R,&U\ge R/k.
 \end{cases}
\]
The formulas agree at the two boundaries. In particular, an optimal operator has **nonnegative coefficients** although the optimization permits arbitrary signed coefficients. Set
\[
 a_*=\min\!\left\{1,\max\!\left\{0,
 \frac{U-R\ell}{U(1-k)+R(1-\ell)}\right\}\right\}.
\]
For every real Banach target the pointwise prescription
\[
 (Ef)(o)=\frac{a_*}{p}\sum_{x\in A} f(x)
          +\frac{1-a_*}{q}\sum_{x\in B}f(x),
 \qquad (Ef)|_X=f,
\]
is optimal. The selected optimal interpolation assigns weight solely to \(B\) when \(U\le R\ell\), to both clusters when \(R\ell<U<R/k\), and solely to \(A\) when \(U\ge R/k\). When \(\Lambda>1\), this choice is the unique optimal one **among cluster-permutation-invariant operators**; no uniqueness assertion is made for arbitrary unsymmetrized operators.

The exact nonexpansivity criterion is
\[
 \boxed{
 \max\!\left\{0,\frac{1-R}{1-k}\right\}
 \le \min\!\left\{1,\frac{U-\ell}{1-\ell}\right\}.}
\]
This is necessary and sufficient for \(\Lambda=1\). Thus the formula determines both the sharp constant and the complete three-regime support transition. The genuinely two-level case \(s<1\) or \(t<1\) is not determined by formulas restricted to equilateral source metrics.

## Assumptions and scope
All metrics and Banach spaces are real. The distance conditions displayed above are necessary and sufficient for \(X\cup\{o\}\) to be a metric space: the original two-cluster metric satisfies the triangle inequality because \(s,t\le1\); two source vertices of a given cluster impose \(s\le2R\) or \(t\le2U\); a source vertex from each cluster imposes \(|R-U|\le1\le R+U\). Cardinalities \(p,q\) may differ, and \(s,t,R,U\) vary continuously subject to these conditions.

For a metric space \(Z\), \(\operatorname{Lip}(f)\) is the least Lipschitz constant of \(f\). We define the universal one-point extension factor as the infimum of \(C\ge1\) such that for every real Banach space \(E\) and every Lipschitz \(f:X\to E\) some extension \(F:X\cup\{o\}\to E\) satisfies \(\operatorname{Lip}(F)\le C\operatorname{Lip}(f)\). The scalar linear extension constant is the infimum of operator norms, measured in Lipschitz seminorm modulo constants, of constant-preserving real-linear extensions. The theorem proves these infima coincide for this family; it does not assume that nonlinear extensions must be linear.

## Proof
**1. A positive candidate and its exact norm.** For \(0\le a\le1\), let \(E_a\) fix all source values and set
\[
 (E_a f)(o)=\frac a p\sum_{x\in A}f(x)
              +\frac{1-a}{q}\sum_{x\in B}f(x).
\]
If \(f\) has Lipschitz constant at most \(1\), for each \(x\in A\) the triangle inequality gives
\[
 \|(E_a f)(o)-f(x)\|
 \le\frac a p(p-1)s+(1-a)=1-(1-k)a.
\]
For each \(y\in B\), the corresponding bound is \(a+\ell(1-a)\). Source-to-source distances are unchanged, so
\[
 \|E_a\|\le
 \max\left\{1,\frac{1-(1-k)a}{R},
                 \frac{\ell+(1-\ell)a}{U}\right\}.
\]
In the scalar case, both new-point bounds are exact: for each chosen source vertex \(x\), the function \(z\mapsto d(z,x)\) on \(X\) is \(1\)-Lipschitz, and its barycentric difference at \(o\) is exactly the displayed sum of weighted distances. Thus the inequality is equality for the operator norm of \(E_a\).

**2. An unrestricted Banach-valued lower bound.** Let \(\mathcal F(X)\) be the real Lipschitz-free space over \(X\), with its canonical isometric embedding \(\delta:X\to\mathcal F(X)\). Choose any base vertex \(x_0\) and set \(\delta(x_0)=0\). The vectors \(\delta(x)\), modulo this basepoint, form a basis of \(\mathcal F(X)\), so every \(z\in\mathcal F(X)\) is uniquely an affine expression \(z=\sum_{x\in X}\alpha_x\delta(x)\), where \(\sum_x\alpha_x=1\).

Any extension of the particular \(1\)-Lipschitz source map \(\delta\) into \(\mathcal F(X)\) must choose a value \(z\) at \(o\); its Lipschitz factor is at least
\[
 \Phi(z)=\max\!\left\{1,
 \max_{x\in A}\frac{\|z-\delta(x)\|}{R},
 \max_{y\in B}\frac{\|z-\delta(y)\|}{U}\right\}.
\]
The group \(G=\mathfrak S(A)\times\mathfrak S(B)\) acts on the affine space \(\mathcal F(X)\) by isometries sending \(\delta(x)\) to \(\delta(gx)\). The function \(\Phi\) is convex and \(G\)-invariant, and averaging over \(G\) cannot increase it. Consequently its unrestricted infimum is attained among invariant affine combinations. Such combinations have the form
\[
 z_a=\frac a p\sum_{x\in A}\delta(x)
       +\frac{1-a}{q}\sum_{y\in B}\delta(y),\qquad a\in\mathbb R.
\]
This averaging is valid for arbitrary positive or negative coefficients. It proves that the universal Banach-valued extension factor is at least \(\inf_{a\in\mathbb R}\Phi(z_a)\).

**3. Signed weights cannot help.** For \(a<0\), use two concrete \(1\)-Lipschitz scalar test potentials. First take the potential equal to \(0\) on \(A\) and \(1\) on \(B\); evaluating at a selected \(x\in A\) gives
\[
 \|z_a-\delta(x)\|\ge1-a.
\]
Second, fix \(y\in B\), take potential \(0\) on \(A\cup\{y\}\) and \(t\) on \(B\setminus\{y\}\); it is Lipschitz because \(t\le1\), and gives
\[
 \|z_a-\delta(y)\|\ge(1-a)\ell.
\]
Hence \(\Phi(z_a)\ge\Phi(z_0)\) when \(a<0\). For \(a>1\), the potentials \(s\) on \(A\setminus\{x\}\) and \(0\) elsewhere, and \(1\) on \(A\) and \(0\) on \(B\), give
\[
 \|z_a-\delta(x)\|\ge ak,
 \qquad \|z_a-\delta(y)\|\ge a.
\]
Thus \(\Phi(z_a)\ge\Phi(z_1)\) when \(a>1\). No signed invariant operator improves over some \(a\in[0,1]\). In this interval Step 1 and its distance-function witnesses prove the exact identity
\[
 \Phi(z_a)=\max\left\{1,
 \frac{1-(1-k)a}{R},\frac{\ell+(1-\ell)a}{U}\right\}.
\]
Together these observations are a lower bound on **all** (even nonlinear and Banach-valued) extensions, and \(E_a\) gives the matching upper bound.

**4. Explicit minimization and support transitions.** The first variable term in the preceding maximum decreases strictly with \(a\) and the second increases strictly. Their intersection lies at
\[
 a_0=\frac{U-R\ell}{U(1-k)+R(1-\ell)}.
\]
Therefore the minimizer of their maximum over \([0,1]\) is \(a_*\), the clipping of \(a_0\) to \([0,1]\). The clipping changes regime at \(U=R\ell\) and \(U=R/k\), respectively. In the interior, substitution yields the common value
\[
 \frac{1-k\ell}{U(1-k)+R(1-\ell)}.
\]
At the endpoints the dominating values are respectively \(\ell/U\) and \(k/R\). Taking the maximum with \(1\) proves the three-part formula and existence of the positive optimal operator. Because both slopes are strict, its \(a\)-parameter is uniquely minimizing when the resulting factor exceeds \(1\) (within the invariant class).

Finally \(\Lambda=1\) precisely when some \(a\in[0,1]\) obeys both \(1-(1-k)a\le R\) and \(\ell+(1-\ell)a\le U\). Solving these two linear inequalities proves the displayed nonexpansivity condition.

## Verification
Three rational examples illustrate the **genuinely non-equilateral** source range. For \((p,q,s,t,R,U)=(3,5,4/5,4/5,1,1/2)\), the optimal \(a_*=0\) and \(\Lambda=32/25\). For \((4,3,4/5,4/5,1/2,6/5)\), the optimal \(a_*=1\) and \(\Lambda=6/5\). For \((3,3,4/5,4/5,3/5,3/5)\), the optimal \(a_*=1/2\) and \(\Lambda=23/18\). All three metrics satisfy the explicit compatibility inequalities.

The standalone checker `check_two_cluster.py` uses independent linear programming on the full source Lipschitz polytope, with **unrestricted signed coefficients** and separation of violated constraints. It matched the exact formula on \(29\) admissible test configurations with \(2\le p,q\le4\). The source proof above is exact and all-parameter; the finite checks support reproducibility and do not prove the universal theorem. Reproduce with `python3 check_two_cluster.py` after installing SciPy.

## Relationship to prior work
Cúth and Doucha, *Projections in Lipschitz-free spaces induced by group actions* (first public 23 April 2021), develop general invariant averaging and complementability for Lipschitz-free spaces. Their group-action results motivate the symmetry reduction, but do not determine the norm of adding an exterior point to a two-cluster ultrametric, the three threshold regimes, or the nonexpansivity boundary. Basso, *Absolute Lipschitz extendability and linear projection constants* (first public 29 April 2021), establishes general links between universal Banach Lipschitz extension and relative projection constants, and finite linear-programming methods. The specific rational closed formula above is not supplied by the compared theorems. Bruè, Di Marino and Stra (first public 23 January 2018) establish general linear extension bounds through random projections but do not specialize to an exact two-cluster one-point invariant.

The published finding *Sharp optimal projection constants for clustered finite metric free spaces* determines instead the relative projection constant **inside the source free space**, onto within-cluster fluctuation vectors. That is not the one-point relative extension problem \(\mathcal F(X)\subset\mathcal F(X\cup\{o\})\). The published *Exact Hilbert distortion of a balanced four-point ultrametric* calculates Euclidean Banach--Mazur distortion, also a distinct invariant. The published facet enumeration for independently shortened pairs concerns the number of dual extreme potentials, not the sharp one-point extension factor. A prior equilateral-source order-statistic formula covers the degenerate source endpoint \(s=t=1\), but not the family with \(s<1\) or \(t<1\). All claims of noncoverage refer to the stated, materially inspected results, not a proof of bibliographic uniqueness.

## Limitations
The result is for a one-point metric extension of a **two-cluster finite ultrametric source** with each intracluster distance at most the common cross distance. The new point need not produce an ultrametric. Arbitrary nonhomogeneous source metrics, more than two clusters, multiple added points, and quasi-Banach targets are not classified here. At \(\Lambda=1\) optimal interpolation may be nonunique even among invariant operators. Numerical linear-programming checks are finite corroboration only. The literature comparison leaves possible equivalents in unindexed finite-metric projection calculations. No independent mathematical audit has been performed.

## References
- M. Cúth and M. Doucha, *Projections in Lipschitz-free spaces induced by group actions*, arXiv:2104.11519, first public 2021-04-23, https://arxiv.org/abs/2104.11519.
- G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238, first public 2021-04-29, https://arxiv.org/abs/2104.14238.
- E. Bruè, S. Di Marino and F. Stra, *Linear Lipschitz and \(C^1\) extension operators through random projection*, arXiv:1801.07533, first public 2018-01-23, https://arxiv.org/abs/1801.07533.
