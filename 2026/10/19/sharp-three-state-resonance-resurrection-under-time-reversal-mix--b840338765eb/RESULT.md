# Sharp three-state resonance resurrection under time-reversal mixing

## Finding

Let \(\Pi=\frac13\mathbf1\mathbf1^{\mathsf T}\), and let \(P\ne\Pi\) be any nonnegative doubly stochastic \(3\times3\) matrix satisfying \(P^2=\Pi\). Set \(\sigma=\|P-\Pi\|_2\), and for \(p\in[0,1]\) form the time-reversal mixture
\[
Q_p=pP+(1-p)P^{\mathsf T},\qquad c_p=\sigma^2p(1-p).
\]
Here \(P^{\mathsf T}\) is the reversal of \(P\) with respect to the common uniform stationary distribution. The nonstationary eigenvalues of \(Q_p\) are exactly \(\pm\sqrt{c_p}\), and for every integer \(m\ge0\),
\[
Q_p^{2m}=\Pi+c_p^m(I-\Pi),\qquad
Q_p^{2m+1}=\Pi+c_p^m(Q_p-\Pi).
\]
At \(c_p=0\), the convention \(c_p^0=1\) is used. For every nonconstant real-valued state observable \(f\) with zero uniform mean, its stationary annealed normalized autocorrelation at every even lag is exactly \(c_p^m\). Each deterministic endpoint chain, however, has identically zero centered correlations at all lags \(n\ge2\). Thus every genuine mixture \(0<p<1\) creates a nonzero correlation tail from two systems with exact two-step decorrelation.

**Sharp universal bound and realization.** Every such \(P\) satisfies
\[
0<\sigma\le\sqrt3-1.
\]
Consequently the largest possible modulus of a nonstationary annealed eigenvalue is
\[
\boxed{(\sqrt3-1)\sqrt{p(1-p)}}.
\]
The bound is attained for every \(p\in[0,1]\) by the same explicit stochastic matrix
\[
P_* =
\begin{pmatrix}
\frac12-\frac{\sqrt3}{6}&\frac12+\frac{\sqrt3}{6}&0\\
\frac{\sqrt3-1}{2}&\frac12-\frac{\sqrt3}{6}&1-\frac{\sqrt3}{3}\\
1-\frac{\sqrt3}{3}&0&\frac{\sqrt3}{3}
\end{pmatrix}.
\]
For strictly positive entries, the bound is a nonattained supremum, approached by replacing \(P_*\) with \(\Pi+t(P_*-\Pi)\) as \(t\uparrow1\).

Three states are necessary for this mechanism: with one or two states, any doubly stochastic matrix satisfying \(P^2=\Pi\) already equals \(\Pi\). Both \(P_*\) and its transpose admit realizations as Lebesgue-preserving, piecewise-affine uniformly expanding Markov maps of the unit interval; hence the sharp resonance effect occurs within explicit one-dimensional random dynamical systems on their common three-cell observable subspace.

## Assumptions and scope

Matrices act on column state observables on \(\{1,2,3\}\); probabilities are row vectors. \(\Pi\) is the uniform-state averaging projection. The norm \(\|\cdot\|_2\) is the Euclidean operator norm; \(\sigma>0\) by \(P\ne\Pi\). The probability \(p\) selects \(P\) independently at each step, and \(1-p\) selects its transpose. Annealed correlations average both the stationary initial uniform state and the independent map choices. For \(f\ne0\) with \(\mathbf1^{\mathsf T}f=0\), the normalized autocorrelation is
\[
\mathcal C_f(n)=\frac{f^{\mathsf T}Q_p^nf}{f^{\mathsf T}f}.
\]
The same formulas hold for a pair of explicit interval maps when \(f\) is constant on each of their three common Markov cells. No assertion is made that correlations of arbitrary fine-scale observables vanish after two deterministic steps, nor that the displayed eigenvalues exhaust the entire transfer-operator spectrum of the interval maps.

## Proof

**1. Nilpotent normal form.** Doubly stochasticity yields \(P\Pi=\Pi P=\Pi\). For \(N=P-\Pi\), the hypothesis \(P^2=\Pi\) is therefore equivalent to \(N^2=0\). Also \(N\mathbf1=0\) and \(\mathbf1^{\mathsf T}N=0\). On the two-dimensional real plane \(H=\mathbf1^\perp\), a nonzero square-zero operator has rank one. Consequently there are orthonormal vectors \(u,v\in H\) with \(v^{\mathsf T}u=0\) and
\[
N=\sigma uv^{\mathsf T},\qquad \sigma>0.
\]
This also proves that \(\sigma\) is the unique nonzero singular value of \(N\).

**2. Exact mixture powers and correlations.** Write \(M=Q_p-\Pi=\sigma[puv^{\mathsf T}+(1-p)vu^{\mathsf T}]\). The rank-one products imply
\[
M^2=\sigma^2p(1-p)(uu^{\mathsf T}+vv^{\mathsf T})
=c_p(I-\Pi).
\]
Because \(M\Pi=\Pi M=0\), multiplication gives the asserted formulas for every \(m\ge0\). On the ordered orthonormal basis \((u,v)\) of \(H\), the matrix of \(M\) is \(\sigma\begin{psmallmatrix}0&p\\1-p&0\end{psmallmatrix}\). This proves the eigenvalue statement, including the nilpotent endpoint cases. Since \(f\in H\), the even-power formula yields \(f^{\mathsf T}Q_p^{2m}f=c_p^mf^{\mathsf T}f\). At either endpoint, \(Q_p=P\) or \(P^{\mathsf T}\) has square \(\Pi\), so every centered correlation vanishes at all lags at least two. For \(0<p<1\), \(c_p>0\), so all even-lag correlations remain strictly positive. The odd-lag formula is also exact; because \(f\) is real, it can be written
\[
\mathcal C_f(2m+1)=c_p^m\frac{f^{\mathsf T}(P-\Pi)f}{f^{\mathsf T}f}.
\]

**3. Optimal singular-value bound.** Any orthonormal pair \(u,v\in H\) is, up to simultaneously changing their signs and reversing cyclic orientation, of the form
\[
u_i=\sqrt{\frac23}\cos\left(\theta+\frac{2\pi(i-1)}3\right),\qquad
v_i=\sqrt{\frac23}\sin\left(\theta+\frac{2\pi(i-1)}3\right),\qquad i=1,2,3.
\]
For the three cyclic pairs \((i,i-1)\), where indices are interpreted modulo three,
\[
u_iv_{i-1}=\frac13\sin\left(2\theta+\frac{4\pi(i-1)}3-\frac{2\pi}3\right)-\frac{\sqrt3}{6}.
\]
Among three sines with arguments separated by \(2\pi/3\), at least one is at most \(-1/2\). Indeed, their three arguments cannot all be strictly inside the open arc on which \(\sin x>-1/2\), whose length is \(4\pi/3\); any open arc containing three equally spaced points must be longer than \(4\pi/3\). Hence for some ordered pair \((i,j)\),
\[
u_iv_j\le-\frac{\sqrt3+1}{6}.
\]
If the orthonormal orientation is reversed, the same conclusion follows using pairs \((i,i+1)\). Entrywise nonnegativity of \(P=\Pi+\sigma uv^{\mathsf T}\) implies
\[
0\le\frac13+\sigma u_iv_j\le\frac13-\sigma\frac{\sqrt3+1}{6},
\]
so \(\sigma\le 2/(\sqrt3+1)=\sqrt3-1\). In the displayed middle inequality, only the single pair with the bounded negative product is considered.

For equality, take
\[
u=\left(\frac{3+\sqrt3}{6},\frac{\sqrt3-3}{6},-\frac1{\sqrt3}\right)^{\mathsf T},\quad
v=\left(\frac{\sqrt3-3}{6},\frac{3+\sqrt3}{6},-\frac1{\sqrt3}\right)^{\mathsf T}.
\]
These vectors are orthonormal and lie in \(H\). The matrix \(\Pi+(\sqrt3-1)uv^{\mathsf T}\) is exactly \(P_*\) above, with nonnegative entries and both row and column sums one. Its square is \(\Pi\) by the rank-one argument. Every positive entry is less than one. For \(t\in(0,1)\), \(\Pi+t(P_*-\Pi)\) is strictly positive, its squared matrix remains \(\Pi\), and its nonzero centered singular value is \(t(\sqrt3-1)\). This proves optimality and the strict-positivity approximation.

**4. Minimality and expanding interval realization.** A nonzero square-zero linear operator cannot exist on the centered one-dimensional space of a two-state chain. Thus the two-state requirement \(P^2=\Pi\) forces \(P=\Pi\). The one-state case is immediate.

For the three-state realization, split \([0,1]\) into cells \(I_1,I_2,I_3\) of length \(1/3\), with endpoint choices made consistently. For a chosen nonnegative doubly stochastic transition matrix \(R\) equal to \(P_*\) or \(P_*^{\mathsf T}\), subdivide each source cell \(I_i\) into consecutive branches of lengths \(R_{ij}/3\) for those targets \(j\) with \(R_{ij}>0\). Map each branch affinely and increasingly onto the whole target cell \(I_j\). Every slope is \(1/R_{ij}>1\), so each map is uniformly expanding. The preimages of a target cell under each source branch contribute exactly \(R_{ij}\) times a target-cell density, and column sums of \(R\) are one; hence Lebesgue measure is invariant. Conditional on a uniform point in \(I_i\), the next cell is \(I_j\) with probability \(R_{ij}\), and its conditional location is again uniform. Iteration therefore induces exactly the Markov transition \(R\) on the coarse observables, even for alternating choices of the two maps. Independent map selection yields \(Q_p\) and the proved annealed coarse correlation identities. Piecewise-affine branch endpoint discontinuities are permitted; no smooth extension is asserted.

## Verification

The accompanying self-contained Python program `verify.py` uses exact arithmetic in \(\mathbb Q(\sqrt3)\). It checks both the radical extremal matrix and an independent strictly positive rational example
\[
\frac1{12}\begin{pmatrix}5&5&2\\3&3&6\\4&4&4\end{pmatrix},
\]
whose squared matrix is \(\Pi\) and whose centered singular value squared is \(1/12\). For six choices of \(p\) and eight even/odd power pairs it verifies the complete exact matrix identities and autocorrelations. It performs **345** exact assertions. The universal three-state and optimality claims are proved above, not inferred from finite testing.

## Relationship to prior work

Jain and Phalempin (2026, arXiv:2608.05649v1), in particular Section 3.1 and their block spectral formulas, already show that eigenvalues of annealed expanding-map operators need not be averages of component eigenvalues. Their general finite-matrix transfer-operator framework is not new here. Higham and Lin (2011) classify and study stochastic roots, including singular stochastic matrices. The result here isolates the additional **sharp** three-state optimization problem under the two-step exact-mixing and time-reversal constraints, the universal closed autocorrelation law, and its optimal expanding-map realization. Broad existing mixing-of-Markov-chains literature also warns that convex combinations may behave worse than their constituents. These general phenomena are acknowledged; the asserted contribution is only their precise extremal form in the stated natural class.

## Limitations

The optimal constant is only for the three-state, **uniform stationary**, two-step-exact, time-reversal mixing problem. It does not apply without the requirement \(P^2=\Pi\), to arbitrary pairs of Markov matrices, to larger state spaces, or to nonuniform stationary laws. The extremal matrix has two zero entries; the same value is only approached, not attained, among strictly positive matrices. Eigenvalues and decorrelation claims for the interval maps apply to their invariant three-cell observable sector, not necessarily to all observable spaces. The global literature search cannot exclude every implicit earlier equivalent classification; independent scientific priority review remains necessary.

## References

1. S. Jain and M. Phalempin, *Annealed Ruelle-Pollicott Resonances*, arXiv:2608.05649v1 (first posted 6 August 2026), especially Theorem 5, Section 3.1, and equations (30)–(31). https://arxiv.org/abs/2608.05649
2. N. J. Higham and L. Lin, *On pth Roots of Stochastic Matrices*, Linear Algebra and its Applications **435** (2011), 448–463, especially Sections 2–5. https://eprints.maths.manchester.ac.uk/1429/1/paper11.pdf
3. I. Bezakova and D. Stefankovic, *Convex Combinations of Markov Chains*, publicly available research colloquium abstract (full proof not inspected). https://www.cs.rit.edu/~spr/CLQABS/ib.html
