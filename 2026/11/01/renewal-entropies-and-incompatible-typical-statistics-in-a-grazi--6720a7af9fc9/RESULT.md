# Renewal entropies and incompatible typical statistics in a grazing-sliding border-collision family

## Finding
For each integer \(m\geq2\), consider the continuous piecewise-affine map
\[
F_m(x,y)=\begin{cases}(-mx+y-1,0),&x\leq0,\\(x+y-1,0),&x\geq0.\end{cases}
\]
This is the \(\tau_L=-m\), \(\tau_R=1\) specialization of the grazing-sliding normal form in [1, Eq. (4.1)]. Every finite initial point reaches the compact invariant interval \(I_m=[-1,m-1]\times\{0\}\) after finitely many iterations. On that interval the system has a unique absolutely continuous invariant probability \(\mu_m\), which is physical for Lebesgue-almost-every planar initial point. With cells \(J_j=[j-1,j]\times\{0\}\), \(0\leq j<m\), its densities and metric entropy are
\[
\frac{d\mu_m}{dx}\bigg|_{J_j}=\frac{2(m-j)}{m(m+1)},\qquad
h_{\mu_m}(F_m)=\frac{2\log m}{m+1}.
\]
Let \(\beta_m\in(1,2)\) be the unique root of
\[
\sum_{r=1}^{m}\beta_m^{-r}=1.
\]
Then \(h_{\mathrm{top}}(F_m|_{I_m})=\log\beta_m\); the unique maximal-entropy invariant probability \(\nu_m\) has first-return lengths \(r\in\{1,\ldots,m\}\) distributed as \(\Pr_{\nu_m}(r)=\beta_m^{-r}\), while the corresponding distribution for \(\mu_m\) is uniform. More precisely, with \(M_m=\sum_{r=1}^m r\beta_m^{-r}\),
\[
\nu_m(J_j)=\frac{\sum_{r=j+1}^{m}\beta_m^{-r}}{M_m}.
\]
Consequently \(h_{\mu_m}(F_m)\to0\) although \(h_{\mathrm{top}}(F_m|_{I_m})\to\log2\) as \(m\to\infty\). Under the physical measure, the normalized cell index \(j/m\) converges to the density \(2(1-t)\) on \([0,1]\); under the maximal-entropy measure it converges in probability to \(0\), with each fixed-cell mass converging to \(2^{-j-1}\). The two invariant statistics therefore separate at macroscopic excursion scales.

## Assumptions and scope
The parameter \(m\) is an integer at least \(2\), not a continuous bifurcation parameter. Entropies and measures concern the compact invariant interval \(I_m\); the whole plane is noncompact and is not assigned a topological entropy here. The map is the exact two-dimensional piecewise-affine normal form, not a nonlinear Filippov flow with neglected terms. Cell boundaries have zero mass for all stated measures; individual boundary orbits need not obey typical statistical assertions.

## Proof
**1. Finite entry and a Markov tower.** The second coordinate becomes zero in one step. On its invariant horizontal line, the first coordinate obeys
\[
f_m(x)=\begin{cases}-mx-1,&x\leq0,\\x-1,&x\geq0.\end{cases}
\]
If \(x>m-1\), successive translations \(x\mapsto x-1\) reach \([-1,m-1]\); if \(x<-1\), the next point is \(-mx-1>m-1\) and then translations enter. On \(I_m\), \(f_m(J_0)=I_m\) and \(f_m(J_j)=J_{j-1}\) for \(1\le j<m\). Thus the Markov transition matrix has its first row all ones and its remaining nonzero entries at \((j,j-1)\). It is primitive.

**2. Complete first-return branches.** Every point enters \(J_0\) within at most \(m-1\) translations. The first-return map \(R_m:J_0\to J_0\) has, up to endpoints, exactly \(m\) branches indexed by return time \(r\in\{1,\dots,m\}\):
\[
K_r=\left[-\frac{r}{m},-\frac{r-1}{m}\right],\qquad
R_m(x)=-mx-r\quad(x\in K_r),
\]
where the formula follows from the first negative-slope step \(-mx-1\) followed by \(r-1\) unit translations. Each branch maps its entire domain onto \([-1,0]\), with derivative \(-m\) and length \(1/m\). Therefore normalized Lebesgue measure on \(J_0\) is invariant, exact and ergodic for the induced map: its branch labels are independent and uniformly distributed on \(\{1,\ldots,m\}\). Its average return time is \((m+1)/2\). The return tower consequently defines the unique absolutely continuous invariant probability of \(f_m\): if an invariant probability has an absolutely continuous component, its induced first-return probability is absolutely continuous and must be the unique such measure of \(R_m\).

**3. Physical statistics and metric entropy.** A return block of length \(r\) visits exactly \(J_0,J_{r-1},\ldots,J_1\), each once, up to shared endpoints. Hence the probability of being in \(J_j\) under the invariant tower is
\[
\mu_m(J_j)=\frac{\Pr(r>j)}{\mathbb E(r)}=\frac{2(m-j)}{m(m+1)}.
\]
The density is constant on each cell because the first-return branches are affine and the excursion translations preserve lengths. By Abramov's return-entropy identity, \(h_{\mu_m}(f_m)=h_{\mathrm{Leb}}(R_m)/\mathbb E(r)=2\log m/(m+1)\). Birkhoff's theorem gives typical time averages for Lebesgue-a.e. point in \(I_m\); the basin has full planar Lebesgue measure because each branch of the one-step map sends planar null transverse preimages to sets of planar measure zero, and every planar orbit enters \(I_m\).

**4. Topological entropy and maximal-entropy law.** The characteristic equation for the primitive Markov matrix is \(\lambda^m=\sum_{k=0}^{m-1}\lambda^k\). Its Perron root \(\beta_m\) lies strictly between \(1\) and \(2\). The partition is generating: every itinerary of length \(n\) includes at least \(\lfloor n/m\rfloor\) visits to the branch of absolute slope \(m\), so cylinder diameters tend uniformly to zero. Standard finite-state Markov coding therefore gives \(h_{\mathrm{top}}(f_m|_{I_m})=\log\beta_m\); endpoint identifications are confined to a finite orbit and its preimages and cannot alter the entropy.

For a return-invariant probability with return-symbol marginal \(q=(q_1,\ldots,q_m)\), denote its return-time mean by \(\bar r=\sum r q_r\). Its induced entropy is at most \(H(q)=-\sum q_r\log q_r\), with equality only for an independent return-symbol process. The elementary relative-entropy inequality and \(\sum\beta_m^{-r}=1\) give
\[
H(q)\leq(\log\beta_m)\bar r,
\]
with equality exactly when \(q_r=\beta_m^{-r}\). Abramov's identity then gives a unique maximizing induced Bernoulli measure; all original invariant probabilities lift from the return section because each orbit visits it at least every \(m\) steps. Its tower occupation formula is the stated formula for \(\nu_m(J_j)\). The countable set of boundary itineraries supports no competing positive-entropy measure.

**5. Divergent physical and maximizing-entropy scales.** The root identity also reads \(2-\beta_m=\beta_m^{-m}\), forcing \(\beta_m\uparrow2\). Thus \(h_{\mathrm{top}}\to\log2\), while \(2\log m/(m+1)\to0\). The physical masses form Riemann sums tending to the triangular density \(2(1-t)\) for \(t=j/m\). Since \(\beta_m^{-r}\to2^{-r}\) with a geometric uniform bound for all large \(m\), dominated convergence yields \(M_m\to2\), and each fixed cell mass converges to \(2^{-j-1}\). Geometric tails uniformly bound the maximal-entropy cell index, hence that index divided by \(m\) converges in probability to \(0\).

## Verification
The independent executable `check.py` verifies exact finite-parameter cell-balance identities and return-branch affine formulas using rational arithmetic; checks Perron identities and entropy formulas numerically for every \(2\le m\le12\) and \(m\in\{32,128,512\}\); and confirms the maximal-entropy tower probabilities. `verification_output.txt` is the corresponding actual program output. These checks do not replace the analytical proof for all \(m\).

## Relationship to prior work
Simpson [1, Eq. (4.1)] introduces the two-parameter piecewise-affine model as a grazing-sliding normal form and provides numerical attractor classifications, not the present explicit invariant probabilities or entropic separation. The earlier skew-tent analysis [2, §2] covers qualitative behavior of the underlying one-dimensional family. Simpson [3, Theorem 2.3] develops a different first-return regime requiring \(\delta_R>1\), which does not apply to \(\delta_R=0\) here. General invariant-density formulas for piecewise-affine interval maps [4] may recover the density component upon specialization, and standard finite-state symbolic dynamics supplies the general entropy tools; the claim is the combined exact classification and singular physical-versus-maximal-entropy comparison for this natural parameter family, not novelty of those general tools.

## Limitations
The theorem is exact for the normal-form map and integral \(m\), not for arbitrary nearby parameters or the original continuous-time Filippov dynamics. Earlier general formulas for invariant densities and Markov shifts may imply individual constituent equations. The priority assessment is based on inspected sources and searches and is not exhaustive; [4] was accessible at abstract level only. Finite test cases do not establish infinite-parameter claims. Independent mathematical review has not been performed.

## References
[1] D. J. W. Simpson, *Boundary Hopf bifurcations in three-dimensional Filippov systems*, arXiv:2604.06570v1 (first public 2026-04-08), §4 and Eq. (4.1), https://arxiv.org/html/2604.06570v1.

[2] D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790v1 (2024), §2, https://arxiv.org/html/2408.04790v1.

[3] D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, *Qualitative Theory of Dynamical Systems* (2026), Theorem 2.3, https://doi.org/10.1007/s12346-026-01576-z.

[4] P. Góra, *Invariant densities for piecewise linear maps of the unit interval*, *Ergodic Theory and Dynamical Systems* (2009), abstract available at https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/abs/invariant-densities-for-piecewise-linear-maps-of-the-unit-interval/97E6074A0AC5A757F3A68F7C0B3B6063.
