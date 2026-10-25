# Universal normalized dynamics of positive permutation evolution algebras

## Finding
For every strictly positive weighted permutation evolution algebra, the normalized nonlinear squaring dynamics admits a weight-removing diagonal conjugacy. Every simplex trajectory approaches a uniquely selected finite periodic orbit at a superexponential rate; all periodic points, their least periods, their basins, and their stability are explicitly determined by the permutation. In particular, the weighted directed-cycle case has a binary-necklace orbit census.

## Assumptions and scope
Fix an integer \(n\ge1\), a permutation \(\pi\in S_n\) acting on \(\{0,\ldots,n-1\}\), and arbitrary real coefficients \(a_i>0\). Define a real commutative evolution algebra \(E\) by
\[
e_ie_j=0\quad(i\ne j),\qquad e_i^2=a_i e_{\pi(i)}.
\]
All statements below concern the **nonnegative normalized square map**, not the unnormalized quadratic map or the linear basis evolution operator. On the closed simplex \(\Delta=\{x\in\mathbb R_{\ge0}^{n}:\sum_i x_i=1\}\), it is
\[
T(x)_{\pi(i)}=\frac{a_ix_i^2}{\sum_j a_jx_j^2}.
\]
The denominator is strictly positive. The weighted permutation matrix is invertible, so \(E\) is perfect. If \(\pi\) is a single cycle, the directed graph is strongly connected and the evolution algebra is simple.

For a permutation cycle \(C=(i,\pi(i),\ldots,\pi^{\ell-1}(i))\), set
\[
\gamma_i=\left(\prod_{j=0}^{\ell-1}a_{\pi^j(i)}^{2^{\ell-1-j}}\right)^{1/(2^\ell-1)},
\quad \gamma_{\pi(i)}=\gamma_i^2/a_i,
\]
and use this prescription separately for each cycle. The positive quantities \(\gamma_i\) are uniquely characterized by \(\gamma_{\pi(i)}a_i=\gamma_i^2\). Put
\[
H(x)_i=\frac{\gamma_i x_i}{\sum_j\gamma_jx_j},\qquad
U(y)_{\pi(i)}=\frac{y_i^2}{\sum_j y_j^2}.
\]
For each nonempty subset \(I\subseteq\{0,\ldots,n-1\}\), let \(u_I=|I|^{-1}\mathbf1_I\) and \(p_I=H^{-1}(u_I)\). Explicitly, \((p_I)_i=\gamma_i^{-1}/\sum_{j\in I}\gamma_j^{-1}\) for \(i\in I\), and zero elsewhere. Write \(\operatorname{ord}(\pi)=L\) and let \(c(\sigma)\) denote the number of cycles of a permutation \(\sigma\), including fixed points.

## Proof
**1. Gauge and conjugacy.** Iterating the recurrence \(\gamma_{\pi(i)}=\gamma_i^2/a_i\) around a cycle of length \(\ell\) forces
\[
\gamma_i^{2^\ell-1}=\prod_{j=0}^{\ell-1}a_{\pi^j(i)}^{2^{\ell-1-j}}.
\]
The strictly positive root is unique, and propagation satisfies the last equation on the closing edge as well. Therefore every edge satisfies \(\gamma_{\pi(i)}a_i=\gamma_i^2\). Applying \(H\) after \(T\), the coordinate at \(\pi(i)\) is proportional to \(\gamma_{\pi(i)}a_ix_i^2=\gamma_i^2x_i^2\). This proves \(H\circ T=U\circ H\). The inverse is the same positive diagonal normalization with reciprocal weights; hence \(H\) is a simplex homeomorphism.

**2. Iteration and asymptotic phase.** The permutation action and coordinatewise normalized squaring commute. Inductively, for every integer \(t\ge0\),
\[
U^t(y)_{\pi^t(i)}=\frac{y_i^{2^t}}{\sum_j y_j^{2^t}}.
\]
For \(y=H(x)\), let \(M=\max_i y_i>0\), \(I=\{i:y_i=M\}\), \(k=|I|\), and let \(\rho\in[0,1)\) be the largest ratio \(y_j/M\) over \(j\notin I\), taking \(\rho=0\) when the complement is empty. Dividing numerator and denominator by \(M^{2^t}\) yields
\[
\left\|U^t(y)-u_{\pi^t(I)}\right\|_1\le \frac{2(n-k)}{k}\rho^{2^t}.
\]
Because \(H^{-1}\) is Lipschitz on the compact simplex, the same order of convergence holds after conjugating back. Consequently \(T^t(x)\) shadows the explicitly phased periodic orbit \(p_{\pi^t(I)}\). Its basin with that phase is precisely the stratum of points where \(I\) is the set of maximizers of \(\gamma_ix_i\); no genericity or interior assumption is needed.

**3. Complete periodic-point classification.** Suppose \(y\) is periodic under \(U\), with some period \(r\). Since \(\pi^L=\operatorname{id}\), the same point is fixed by \(U^{Lr}\), which acts as pure normalized coordinatewise \(2^{Lr}\)-th power. On the positive support, the fixed-point equation implies that every nonzero coordinate has the same positive \((2^{Lr}-1)\)-st power; hence all positive coordinates are equal. Thus \(y=u_I\) for a nonempty \(I\). Conversely \(U(u_I)=u_{\pi(I)}\), so every such \(u_I\) is periodic, with least period the least positive \(r\) satisfying \(\pi^r(I)=I\), necessarily dividing \(L\). Conjugation gives exactly \(2^n-1\) periodic points for \(T\).

A nonempty subset is fixed under \(\pi^r\) precisely if it is a union of cycles of \(\pi^r\). Hence
\[
\#\operatorname{Fix}(T^r)=2^{c(\pi^r)}-1.
\]
For every divisor \(r\mid L\), Möbius inversion on the divisibility lattice now gives the exact number \(A_r\) of orbits with least period \(r\):
\[
A_r=\frac1r\sum_{d\mid r}\mu(r/d)\bigl(2^{c(\pi^d)}-1\bigr).
\]
The total number of orbits is also \(L^{-1}\sum_{t=0}^{L-1}(2^{c(\pi^t)}-1)\) by Burnside's lemma. For a single directed \(n\)-cycle, \(L=n\) and \(c(\pi^t)=\gcd(n,t)\). The standard totient grouping yields
\[
\frac1n\sum_{d\mid n}\varphi(d)2^{n/d}-1,
\]
exactly the number of nonempty binary necklaces of length \(n\).

**4. Stability.** Each singleton support \(\{i\}\) has a strict-maximizer neighborhood \(\{y:y_i>y_j\text{ for every }j\ne i\}\). Successive normalized squaring strictly shrinks all ratios to that coordinate, so the orbit of the corresponding vertices of \(\Delta\) is asymptotically stable (indeed superattracting). If \(|I|>1\), take points arbitrarily close to \(u_I\) that make one element of \(I\) uniquely maximal; their orbits approach a vertex orbit a positive distance away from the original periodic orbit. Thus every larger-support orbit is unstable. All trajectories converge to single points precisely when every vertex is fixed by \(\pi\), equivalently \(\pi\) is the identity; otherwise a moved vertex gives a nonconstant periodic orbit.

## Verification
A standalone Python checker using only the standard library independently enumerates every permutation of orders \(1\) through \(6\) (\(873\) permutations) and every nonempty subset, reconstructs its rotation orbit, and compares exact least-period counts against the fixed-set and permutation-cycle formulas. It independently constructs the positive cycle gauges, tests diagonal conjugacy and the explicit iteration formula at sample positive states, and checks a tied-maxima example. Run `python3 verify.py`. The observed result was `VERIFY_OK`. The finite checks support, but do not replace, the universal proof.

## Relationship to prior work
Kaygorodov, Martín González, and Viruel explicitly ask in Question 48 of their 2026 survey for graph- and structure-matrix descriptions of convergence and periodic-orbit stability for normalized squaring in nonnegative real evolution algebras. Their Example 2 also highlights oriented-cycle algebras. The theorem above settles the complete question for the natural class of **positive weighted permutation graphs**, including all directed cycles, without claiming to answer it for general graphs.

Giacomelli's 2026 expander evolution-algebra work studies graph growth, a **linear** basis evolution operator and spectral gaps; it does not assert the normalized nonlinear cycle and basin formulas. Jamilov's 2022 paper analyzes a different **polynomial quadratic stochastic operator** involving a distinguished coordinate and cross terms, unlike the state-dependent-rational denominator here. Rozikov and Velasco investigate a six-coordinate mosquito model with a different polynomial map and associated algebra. Classical Burnside and Möbius inversion are used only after the new dynamical reduction and are not claimed as new results.

## Limitations
The theorem requires all \(a_i>0\), a permutation structure matrix, real nonnegative initial states, and normalization by coordinate sum. It does **not** address zero or negative weights, arbitrary non-monomial evolution structures, unnormalized trajectories, perturbation robustness beyond the stated class, or other dynamical normalizations. The convergence is to a periodic orbit in a phase-matched sense; an actual pointwise limit need not exist. The error-rate constant depends on the initial state and weights, and no uniform-in-state convergence rate is asserted. Closely related unindexed projective-monomial dynamics could constitute prior coverage; publication novelty has not been independently established.

## References
1. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1 (first public 2026-10-15), especially Example 2 and Question 48, https://arxiv.org/abs/2610.22248.
2. P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1 (2026-05-12), Sections 4–5, https://arxiv.org/abs/2605.12672.
3. U. U. Jamilov, *A family of non-Volterra quadratic operators corresponding to permutations*, arXiv:2210.05107v2 (2022), Section 3, https://arxiv.org/abs/2210.05107.
4. U. A. Rozikov, M. V. Velasco, *A discrete-time dynamical system and an evolution algebra of mosquito population*, arXiv:1803.01503v1 (2018), https://arxiv.org/abs/1803.01503.
