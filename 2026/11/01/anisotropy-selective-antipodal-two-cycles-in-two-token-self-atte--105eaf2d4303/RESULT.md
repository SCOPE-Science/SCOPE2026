# Anisotropy-selective antipodal two-cycles in two-token self-attention

## Finding
For two spherical tokens with unmasked softmax attention and a symmetric negative-definite value operator, an antipodal eigenvector pair may be an **exponentially attracting genuine period-two orbit**, although the corresponding isotropic value operator cannot support an exponentially attracting antipodal eigencycle. The complete necessary-and-sufficient local stability criterion has two distinct spectral edges.

Let \(d\ge 2\), \(\alpha>0\), \(\eta>0\), and let the real symmetric negative-definite matrix \(V\) have an orthonormal eigenbasis \((e_j)_{j=1}^{d}\) with \(Ve_j=-s_j e_j\), where
\[
s_1>s_2\ge\cdots\ge s_d>0.
\]
For two states \(x_1,x_2\in\mathbb S^{d-1}\), define the full self-inclusive attention weights and normalized residual map by
\[
A_{i\ell}(x)=\frac{\exp(\alpha\langle x_i,x_\ell\rangle)}{\exp(\alpha\langle x_i,x_1\rangle)+\exp(\alpha\langle x_i,x_2\rangle)},\qquad
F_i(x)=\frac{x_i+\eta V\sum_{\ell=1}^{2}A_{i\ell}(x)x_\ell}{\left\|x_i+\eta V\sum_{\ell=1}^{2}A_{i\ell}(x)x_\ell\right\|},
\]
wherever the denominator is nonzero. Put \(t=\tanh\alpha\in(0,1)\).

For every eigendirection \(e_j\) with \(\eta s_jt>1\), the pair \(P_j=(e_j,-e_j)\) is an exact labeled period-two orbit:
\[
F(P_j)=(-e_j,e_j),\qquad F^2(P_j)=P_j.
\]
Its nontrivial one-step tangent eigenvalues, for every \(k\ne j\), are
\[
q_{j,k}^{\mathrm{com}}=\frac{1-\eta s_k}{\eta s_jt-1},\qquad
q_{j,k}^{\mathrm{dif}}=\frac{1-\eta s_kt}{\eta s_jt-1}.
\]
The complete two-step Floquet spectrum consists of their squares (one of each for every \(k\ne j\)).

**Sharp two-edge criterion.** Among all such antipodal eigenvector cycles, an exponentially attracting cycle can exist only on the unique most negative eigendirection \(e_1\). The cycle \(P_1\) is exponentially attracting if and only if
\[
\boxed{\tanh\alpha>\frac{s_2}{s_1}
\quad\text{and}\quad
\eta>\frac{2}{(s_1+s_d)\tanh\alpha}.}
\]
If the first inequality is strictly reversed, every existing antipodal eigencycle is linearly unstable for all gains. If it is an equality, \(P_1\) has a unit-modulus Floquet multiplier and is not exponentially attracting. Under the strict spectral-gap inequality, at gain equality a multiplier is \(+1\) and the cycle is nonhyperbolic; below the gain boundary, every existing such cycle is unstable. No assertion about nonlinear attraction at either equality is made.

Thus the second strongest negative mode controls whether stable flipping is possible at all, while the weakest negative mode controls the precise gain onset. This difference between the two spectral edges is nontrivial when \(d\ge3\).

For instance, take
\[
V=\operatorname{diag}(-8,-2,-1),\quad \alpha=\tfrac12\log3,\quad\eta=\tfrac12.
\]
Then \(t=1/2\), the exact orbit \((e_1,-e_1)\leftrightarrow(-e_1,e_1)\) is attracting, and its full two-step tangent multipliers are
\[
\boxed{\{0,\tfrac14,\tfrac14,\tfrac9{16}\}.}
\]
Here the exact gain threshold is \(\eta_*=4/9\), whereas the orbit begins to exist at \(\eta>1/4\). For this matrix no choice of gain can make the orbit exponentially attracting if \(\alpha\le\operatorname{artanh}(1/4)\).

## Assumptions and scope
The state space is the product of two real unit spheres, with dimension \(d\ge2\) and two *labeled* tokens. Scores include each token's own score; there is no diagonal attention mask. The query and key operators may be realized as \(Q=K=\sqrt\alpha I\), while the value matrix is symmetric negative definite. The step \(\eta>0\) is unrestricted except for the nonvanishing of the normalization denominator along the studied orbit. The statements concern *these antipodal eigenvector cycles* and local dynamics, not all possible periodic orbits or global basins.

The descending ordering \(s_1>s_2\ge\cdots\ge s_d>0\) is assumed for the sharp two-edge formula. For a repeated largest magnitude there can be no exponentially attracting antipodal eigencycle, as follows from the more general eigenvalue formula.

## Proof
At \(P_j=(e_j,-e_j)\), each token gives its own direction weight \(p=e^\alpha/(e^\alpha+e^{-\alpha})=(1+t)/2\) and the opposite direction weight \(1-p=(1-t)/2\). The attention messages are \(te_j\) and \(-te_j\). Accordingly, the unnormalized residuals are \((1-\eta s_jt)e_j\) and \(-(1-\eta s_jt)e_j\). If \(\eta s_jt>1\), normalizing swaps both signs, establishing the exact least-period-two orbit. The map is locally smooth at both orbit points because the pre-normalization norm there equals \(R=\eta s_jt-1>0\).

Let \(u,v\in e_j^\perp\) be arbitrary first-order perturbations of the two tokens. The first derivatives of all score inner products vanish at an antipodal pair: for example, \(d\langle x_1,x_2\rangle=\langle u,-e_j\rangle+\langle e_j,v\rangle=0\). Thus the attention weights have zero first-order variation. At either orbit point, the derivative of spherical normalization restricted to \(e_j^\perp\) is division by \(R\). In the mode \(e_k\), \(k\ne j\), the tangent update is consequently
\[
\frac1R
\begin{pmatrix}
1-\eta s_kp&-\eta s_k(1-p)\\
-\eta s_k(1-p)&1-\eta s_kp
\end{pmatrix}.
\]
Its common-token and difference-token eigenvectors \((1,1)\) and \((1,-1)\) have eigenvalues \(q_{j,k}^{\mathrm{com}}\) and \(q_{j,k}^{\mathrm{dif}}\) as displayed above. The global sign symmetry \(F(-x_1,-x_2)=-F(x_1,x_2)\) implies that the Jacobian at the second orbit point is identical to the Jacobian at the first. Therefore the period-two Floquet multipliers are their squares, with no omitted tangent directions: their total multiplicity is \(2(d-1)\).

Write \(b=\eta s_j>1/t\) and \(r=s_k/s_j>0\). Then the two eigenvalues are \((1-br)/(bt-1)\) and \((1-brt)/(bt-1)\). The first lies strictly inside the unit disk exactly when \(r<t\) and \(b>2/(t+r)\). The second lies strictly inside the unit disk exactly when \(r<1\) and \(b>2/[t(1+r)]\). Under \(r<t<1\), the second gain threshold is the stronger one because \(t(1+r)<t+r\). Consequently the pair of modes is strictly stable exactly when
\[
r<t\quad\text{and}\quad b>\frac{2}{t(1+r)}.
\]
Taking all \(k\ne j\), strict stability requires \(\max_{k\ne j}s_k/s_j<t\), which forces \(j=1\) and a simple strongest negative eigenvalue. For \(j=1\), the maximum is \(s_2/s_1\), while the largest of the gain thresholds is attained at the smallest ratio \(s_d/s_1\), giving the boxed result. At a strict failure of the spectral gap the common-token eigenvalue lies below \(-1\); at gain below its threshold, the weakest-mode difference-token eigenvalue exceeds \(+1\). At either equality the corresponding eigenvalue has modulus one. Hyperbolic contraction of the two-step derivative implies local exponential attraction, and a multiplier of modulus greater than one implies local linear instability.

In the stated example, \(p=3/4\), \(R=1\), and the transverse modes \(s_k=2\) and \(s_k=1\) have one-step eigenvalues \((0,1/2)\) and \((1/2,3/4)\), respectively. Squaring gives precisely the reported spectrum. The gain threshold is \(2/[\tfrac12(8+1)]=4/9\).

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic for the example's attention weights, derivative blocks, Floquet multipliers, and threshold. It also evaluates the original normalized two-token map and finite-difference tangent derivatives, and tests the scalar stability equivalence over a finite grid. Execute with a standard Python 3 interpreter using `python verify.py`. These computational checks are reproducibility diagnostics; the proof for every dimension and all stated parameters is the preceding analytic argument, not an extrapolation of the checks.

## Relationship to prior work
Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers* (arXiv:2610.13518v1), introduces the self-inclusive normalized residual model and analyzes stationary consensus and bipartite equilibria. Its stability theorems assume a simple **positive** leading eigenvalue and do not cover the negative-definite, finite-gain antipodal two-cycle described here. This is a statement about a new cycle, not a rephrasing of stability of an existing equilibrium.

Gao, Yang, and Chen, *Nonequilibrium Phases of Repulsive Self-Attention* (arXiv:2609.28448v1), explicitly derive exchange and flip cluster orbits for an **isotropic negative** value map and a diagonally *masked* attention kernel. That work already establishes the existence of repulsive-attention period-two motion; existence of such motion alone is not claimed as new here. Its isotropic value matrix cannot meet the strict spectral gap of the present theorem, and its cluster Floquet formulas do not yield this two-edge anisotropic criterion.

Kuehn and Yoon, *Spectral Selection in Symmetric Self-Attention Dynamics* (arXiv:2604.26085v1), study **continuous-time** self-attention under a coupled score/value symmetry \(Q^\top K=V\), deriving sign-split equilibrium selection in the negative-definite case. That flow is not the discrete update examined here, which has positive isotropic score matrix \(Q^\top K=\alpha I\), independently of the negative-definite value matrix. Their global flow selection does not imply the present exact finite-step Floquet boundaries.

## Limitations
No global-basin or all-periodic-orbit classification is claimed; the map need not be defined at all possible configurations when a normalization denominator vanishes. At equality in either stability condition only neutral linear behavior is established; higher-order nonlinear dynamics is not classified. The result is local for two labeled tokens and a symmetric negative-definite value matrix with self-inclusive attention. The literature comparison supports the stated distinction from inspected results but does not establish exhaustive historical priority. Independent external validation has not been performed.

## References
1. C. Altafini, *Asymptotic Analysis of Discrete-Time Self-Attention Dynamics in Transformers*, arXiv:2610.13518v1 (first public October 9, 2026), https://arxiv.org/abs/2610.13518.
2. Q. Gao, Z. Yang, X. Chen, *Nonequilibrium Phases of Repulsive Self-Attention: Chaos, Attention Condensation, and Emergent Locality*, arXiv:2609.28448v1 (first public September 23, 2026), https://arxiv.org/abs/2609.28448.
3. C. Kuehn, J. Yoon, *Spectral Selection in Symmetric Self-Attention Dynamics*, arXiv:2604.26085v1 (first public April 28, 2026), https://arxiv.org/abs/2604.26085.
4. Mathematical Reviews, *MSC2020 classification 37C25: Fixed points and periodic points of dynamical systems; local dynamics*, https://mathscinet.ams.org/mathscinet/msc/msc2020.html?t=37C25.
