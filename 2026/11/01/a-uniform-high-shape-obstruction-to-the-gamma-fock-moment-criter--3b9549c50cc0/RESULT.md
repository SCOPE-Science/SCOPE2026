# A uniform high-shape obstruction to the Gamma Fock moment criterion

## Finding
Let \(\kappa\ge 144\) be an arbitrary **real** number, and put
\[
 m_j=\frac{\Gamma(\kappa+j)}{\Gamma(\kappa)}
 \qquad(j=0,1,2,\ldots).
\]
There is **no** Borel probability measure \(\nu\) supported on \([\kappa,\infty)\) satisfying simultaneously, for every integer \(j\ge1\),
\[
 \int t^j\,d\nu(t)\ge m_j,
 \qquad
 \kappa\int t^{j-1}\,d\nu(t)\le m_j.
 \tag{1}
\]
Consequently the moment-duality sufficient criterion of Wikström (2026, Theorem 1.2) cannot certify the upper-bound radius \(\sqrt{\kappa}\) for the Gamma-weighted Fock Hilbert space with normalized radial weight
\[
 W_\kappa(t)=\frac{t^{\kappa-1}e^{-t}}{\Gamma(\kappa)},\qquad t>0.
\]
The conclusion holds on an **entire real half-line**, not merely at isolated integer shapes. It concerns feasibility of a sufficient moment certificate, **not** failure of Korenblum's domination principle.

## Assumptions and scope
The shape \(\kappa\) is any real number at least \(144\); the measure is nonnegative and has total mass one. Its support is restricted to \([\kappa,\infty)\). The moments \(m_j\) are the moments of a Gamma random variable of shape \(\kappa\) and unit scale. In the associated Fock norm,
\[
 \|f\|^2=\frac{1}{\pi}\int_{\mathbb C}|f(z)|^2W_\kappa(|z|^2)\,dA(z),
\]
this choice corresponds to \(\alpha=1\), \(\beta=\kappa-1\) in the power-Gaussian family. The standard scaling reduces arbitrary \(\alpha>0\) to this normalization. No statement is made for \(0<\kappa<144\).

## Proof
Suppose that \(\nu\) exists. Let \(X\) have law \(\nu\), and set \(Y=X-\kappa\ge0\). Since \(m_1=\kappa\) and \(m_2=\kappa(\kappa+1)\), the second inequality in (1), with \(j=2\), gives
\[
 0\le \mathbb E Y=\mathbb E X-\kappa\le1. \tag{2}
\]
By nonnegativity and monotone convergence, the two infinite families of moment inequalities imply, for every \(0\le u<1\),
\[
 (1-u)^{-\kappa}\le \mathbb E e^{uX}
 \le(1-u)^{-\kappa-1}. \tag{3}
\]
Indeed, the first bound follows by summing \(\mathbb E X^j\ge(\kappa)_j\) (with equality at \(j=0\)); the second follows by summing \(\mathbb E X^j\le(\kappa)_{j+1}/\kappa\). The corresponding Gamma moment-generating functions are exactly the two binomial series displayed in (3). In particular, \(\mathbb E e^{uX}\) is finite for \(u<1\).

Write \(M(u)=\mathbb E e^{uY}\), and let \(\lambda=3/(4\sqrt\kappa)\). Because \(\kappa\ge144\),
\[
 0<\lambda\le\frac1{16},\qquad 2\lambda\le\frac18.
\]
Applying (3) first at \(u=\lambda\), then at \(u=2\lambda\), yields
\[
 M(\lambda)\ge \exp\!\bigl(\kappa[-\lambda-\log(1-\lambda)]\bigr)
 \ge e^{9/32}, \tag{4}
\]
\[
 M(2\lambda)\le\frac{1}{1-2\lambda}
 \exp\!\bigl(\kappa[-2\lambda-\log(1-2\lambda)]\bigr)
 \le\frac87 e^{9/7}. \tag{5}
\]
For (4) use \(-v-\log(1-v)\ge v^2/2\); for (5) use \(-v-\log(1-v)\le v^2/[2(1-v)]\), both valid for \(0\le v<1\). The last bounds use \(\kappa\lambda^2=9/16\).

For every \(y\ge0\) the elementary inequality
\[
 (e^{\lambda y}-1)^2
 \le \frac{\lambda y}{2}(e^{2\lambda y}-1) \tag{6}
\]
holds: after dividing by \(e^{2\lambda y}-1\), it is just \(\tanh(\lambda y/2)\le\lambda y/2\), with the zero case by continuity. Cauchy–Schwarz, (2), and (6) imply
\[
 [M(\lambda)-1]^2
 \le\frac\lambda2\,\mathbb E Y\,[M(2\lambda)-1]
 \le\frac1{32}\left(\frac87 e^{9/7}-1\right). \tag{7}
\]
The lower bound (4), however, gives
\[
 [M(\lambda)-1]^2\ge(e^{9/32}-1)^2.
\]
These inequalities contradict one another by **strict rational bounds**. First, the first three positive terms of the exponential series give
\[
 (e^{9/32}-1)^2>
 \left(\frac9{32}+\frac{81}{2048}\right)^2
 =\frac{431649}{4194304}.
\]
Second, for \(v=9/7\), after its quadratic Taylor polynomial the remainder is bounded by a geometric series of ratio \(v/4<1\), giving
\[
 e^{9/7}\le1+\frac97+\frac{(9/7)^2}{2}
 +\frac{(9/7)^3}{6(1-9/28)}
 =\frac{6767}{1862}<\frac{15}{4}.
\]
Thus the right-hand side of (7) is strictly smaller than
\[
 \frac1{32}\left(\frac87\cdot\frac{15}4-1\right)
 =\frac{23}{224}
 <\frac{431649}{4194304},
\]
where the final difference equals \(6887/29360128>0\). This is impossible and proves the theorem. \(\square\)

## Verification
All probabilistic inequalities are analytic and uniform in real \(\kappa\ge144\). The supplied `verify_bounds.py` checks the exact rational Taylor majorant and the final strictly positive rational gap using Python's standard-library `fractions.Fraction`; no floating-point tolerance or finite sampling enters the proof. A finite checker cannot substitute for the infinite-moment argument, which is fully proved above.

## Relationship to prior work
Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space* (first submitted September 30, 2026), Theorem 1.2, introduces the moment sufficient criterion (1). Proposition 7.3 proves nonexistence at the single shape \(\kappa=50\) by a finite polynomial dual certificate; its discussion gives additional **discrete** verified shapes, including \(200,300,500,1000,3000,10000\), but explicitly states that nonexistence for all sufficiently large shapes is not proved there. The present exponential-generating-function argument supplies a uniform ray \(\kappa\ge144\), without numerical linear programming or shape-by-shape certificates.

The same paper's Corollary 1.4 constructs a feasible measure for \(0<\kappa\le6.4475869\ldots\). There is no contradiction: the two results address disjoint shape ranges. Earlier work of Wee and Le on weighted Fock Korenblum constants provides upper-radius estimates, and Wikström's earlier moment-duality paper addresses Bergman-space estimates; neither cited claim implies the present uniform infeasibility statement.

## Limitations
The cutoff \(144\) is an explicit sufficient threshold for **infeasibility of this particular moment criterion**, not an asserted optimal phase-transition value. A different certificate or an argument not using this moment criterion might still prove domination at the radius \(\sqrt\kappa\); no counterexample pair of entire functions is constructed. Smaller shapes, including the suspected threshold near \(43.6\), are not classified. Historical priority requires further independent literature review.

## References
1. F. Wikström, *The sharp radius in Korenblum's maximum principle for the Fock space*, arXiv:2609.39622 (first public version 2026-09-30), especially Theorem 1.2, Corollary 1.4, Proposition 7.3, and Section 7.1. https://arxiv.org/abs/2609.39622
2. F. Wikström, *Moment duality and an improved lower bound for Korenblum's constant*, arXiv:2607.17748 (2026). https://arxiv.org/abs/2607.17748
3. J. Wee and L. H. Khoi, *Korenblum constants for various weighted Fock spaces*, Complex Variables and Elliptic Equations 68 (2023), 1385–1406. https://doi.org/10.1080/17476933.2022.2052862
