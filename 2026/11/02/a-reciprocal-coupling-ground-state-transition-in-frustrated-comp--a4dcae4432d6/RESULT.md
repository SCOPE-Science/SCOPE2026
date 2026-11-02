# A reciprocal-coupling ground-state transition in frustrated complete-graph XY dimers

## Finding

Let \(m\ge2\). Put a classical planar unit spin \(s_j=(\cos\theta_j,\sin\theta_j)\) at each vertex of the complete graph on \(2m\) vertices. All edges have ferromagnetic energy \(-s_j\cdot s_k\), except a fixed perfect matching of \(m\) disjoint edges: the matched edge \((2i-1,2i)\) instead has antiferromagnetic energy \(K_i s_{2i-1}\cdot s_{2i}\), where \(K_i>0\). Define

\[
a_i=1+K_i,\qquad S=\sum_{i=1}^m\frac1{a_i},\qquad
\mathcal H=-\sum_{\substack{1\le j<k\le2m\\\{j,k\}\text{ not matched}}}s_j\cdot s_k
+\sum_{i=1}^m K_i s_{2i-1}\cdot s_{2i}.
\]

The complete zero-temperature ground-state classification is as follows, with \(M=\left|\sum_{j=1}^{2m}s_j\right|/(2m)\).

**Subcritical reciprocal sum \(S<1\).** Every minimizing matched pair consists of antiparallel spins. Pair orientations are independent, all minima have \(M=0\), and the minimum energy is \(E_0=m-\sum_i a_i\).

**Critical reciprocal sum \(S=1\).** In addition to all antiparallel-pair states, the minima with nonzero magnetization are precisely those whose pair midpoint vectors \(u_i=(s_{2i-1}+s_{2i})/2\) all point in one common direction and obey

\[
|u_i|=\frac{t}{a_i},\qquad 0<t\le\min_i a_i.
\]

The ground-state normalized magnetization fills the complete interval \([0,(\min_i a_i)/m]\), and the minimum energy remains \(E_0=m-\sum_i a_i\).

**Supercritical reciprocal sum \(S>1\).** There is exactly one \(t_*\in(\min_i a_i,m]\) solving

\[
 t_*=\sum_{i=1}^m\min\!\left(1,\frac{t_*}{a_i}\right).
\]

All ground states have aligned nonzero midpoint vectors with the unique lengths

\[
 |u_i|=\min\!\left(1,\frac{t_*}{a_i}\right),\qquad M=\frac{t_*}{m}.
\]

The two spins in a pair are symmetric around its midpoint direction, independently permitting either reflection. The exact energy is

\[
 E_0=m-\sum_{i=1}^m a_i+2\sum_{i:a_i\le t_*}(a_i-t_*).
\]

Thus the reciprocal sum \(\sum_i(1+K_i)^{-1}=1\) is the exact collective-frustration threshold, not a condition on any single frustrated bond. Along any continuous coupling path crossing the surface from \(S>1\) to \(S<1\), the one-sided ordered magnetization tends to \((\min_i a_i)/m>0\) while the disordered side has zero magnetization; this is a discontinuous **zero-temperature ground-state switch** (not a claim of a positive-temperature phase transition for fixed finite \(m\)).

For equal couplings \(K_i=K\), the result becomes especially sharp: all spins align when \(K<m-1\), every matched pair is antiparallel when \(K>m-1\), and at \(K=m-1\) the full range \(0\le M\le1\) consists of ground-state magnetizations. For two dimers with unequal couplings the critical equation is simply \(K_1K_2=1\).

## Assumptions and scope

The results hold for each finite integer \(m\ge2\), all strictly positive real \(K_i\), all planar unit-spin configurations, and exactly the complete-graph matching pattern specified above. The ferromagnetic coupling on other edges is the unit of energy; multiplying all couplings by one positive constant leaves the classification unchanged. The result is deterministic and concerns global zero-temperature minimizers only. At each prescribed set of pair midpoint lengths, each pair of unit spins realizing the midpoint exists because \(0\le|u_i|\le1\).

## Proof

**1. Exact reduction.** Let \(U=\sum_i u_i\) and \(x_i=|u_i|\in[0,1]\). The total spin vector is \(2U\), and \(s_{2i-1}\cdot s_{2i}=2x_i^2-1\). Restoring the \(m\) matched edges to a fictitious all-ferromagnetic complete graph gives, identically,

\[
\mathcal H=m-\sum_i a_i+2\sum_i a_i x_i^2-2|U|^2.
\]

For fixed \(x_i\), the triangle inequality gives \(|U|\le\sum_i x_i\), with equality attainable by aligned pair midpoints. Consequently the global minimum reduces **exactly** to minimizing

\[
 Q(x)=\sum_{i=1}^m a_i x_i^2-\left(\sum_{i=1}^m x_i\right)^2,
 \qquad x\in[0,1]^m.
\]

If the optimum has positive total midpoint length, equality in the triangle inequality forces all nonzero midpoints to align.

**2. Reciprocal-sum threshold.** The weighted Cauchy–Schwarz inequality yields

\[
\left(\sum_i x_i\right)^2\le
\left(\sum_i a_i x_i^2\right)\left(\sum_i a_i^{-1}\right)=S\sum_i a_i x_i^2.
\]

If \(S<1\), \(Q(x)>0\) for every nonzero \(x\); the unique midpoint lengths are \(x=0\), with arbitrary antiparallel orientations. If \(S=1\), equality holds precisely for \(x_i=t/a_i\) with \(0\le t\le\min_i a_i\); for \(t>0\), the aligned-midpoint requirement completes the description. These cases have minimum \(Q=0\).

**3. Supercritical case.** If \(S>1\), a small vector \(x_i=\varepsilon/a_i\) has \(Q(x)=\varepsilon^2 S(1-S)<0\). Thus any global minimizer of \(Q\) is nonzero. Writing \(t=\sum_i x_i>0\), a minimizer cannot have \(x_i=0\), since increasing that coordinate decreases \(Q\) to first order by \(2t\). For an interior coordinate the first-order stationarity condition is \(a_i x_i=t\); a saturated coordinate \(x_i=1\) requires \(a_i\le t\) from the one-sided derivative. Hence each coordinate must obey \(x_i=\min(1,t/a_i)\), and \(t\) solves the displayed scalar equation.

For \(0<t\le a_{\min}\), the equation's right side divided by \(t\) equals \(S>1\). Above \(a_{\min}\), the function

\[
 F(t)=\sum_i\min\!\left(\frac1t,\frac1{a_i}\right)
\]

is continuous and strictly decreasing; \(F(a_{\min})=S>1\) and \(F(m)\le1\). Therefore precisely one positive root \(t_*\in(a_{\min},m]\) exists. Since any global minimizer must have this same root and midpoint lengths, those lengths are the unique minimizing ones. For the energy, let \(B=\{i:a_i\le t_*\}\). The fixed-point identity gives \(t_*=|B|+t_*\sum_{i\notin B}1/a_i\); substituting \(x_i=\min(1,t_*/a_i)\) into \(Q\) reduces it to \(Q=\sum_{i\in B}(a_i-t_*)\).

**4. Sharp jump.** On a continuous path with \(S>1\to1\), the ordered solution satisfies \(t_*>a_{\min}\). At the critical limiting couplings, \(F(t)=1\) on \((0,a_{\min}]\) but is strictly below \(1\) for every \(t>a_{\min}\). Compactness of \([0,m]\), continuity of \(F\) away from zero, and \(t_*>a_{\min}\) force \(t_*\to a_{\min}\). For \(S<1\), \(t=0\). This proves the discontinuity. With equal \(a_i=1+K\), the scalar root is \(t_*=m\) for \(a_i<m\); for \(a_i=m\), the critical continuum has equal \(x_i=t/m\); for \(a_i>m\), the antiparallel state is unique in midpoint lengths. For \(m=2\), elementary rearrangement of \(1/(1+K_1)+1/(1+K_2)=1\) gives \(K_1K_2=1\).

## Verification

The standalone `checker.py` reconstructs ground-state configurations, evaluates the original pairwise Hamiltonian independently of the reduced quadratic expression, and compares the predicted minimum against bounded differential-evolution optimizations. It also checks a critical continuum, both sides of equal-coupling thresholds, and an unequal-coupling critical crossing. Execute `python checker.py` with NumPy and SciPy available. The recorded execution passed 198 checks; the maximum absolute discrepancy between the predicted minimum and the independent optimizations was below \(1.6\times10^{-8}\). These finite numerical tests are not the proof of the all-size theorem; the argument above supplies that proof.

For instance, at \(m=3\) with \((K_1,K_2,K_3)=(0.2,0.5,4)\), the scalar equation gives \(t_*=2.5\), the midpoint lengths are \((1,1,0.5)\), the normalized magnetization is \(5/6\), and the minimum energy is \(-9.3\).

## Relationship to prior work

Classical frustrated XY exchange models and exact ground-state phase diagrams are established subjects. Hayden, Kaplan and Mahanti (2010) treat classical frustrated exchange with biquadratic couplings on local two-dimensional lattices. Andreanov and Fistul (2019) derive a frustrated kagome XY ground-state transition and nontrivial degeneracy of local triangle patterns. Björnberg, Fröhlich and Ueltschi (2019) analyze **quantum** ferromagnetic complete-graph spin models, without the heterogeneous negative-edge matching here. These works motivate investigation of how interaction signs and connectivity govern zero-temperature order, but the particular reciprocal-sum threshold and the complete finite-graph matching classification are not stated in their inspected text.

The rank-one quadratic reduction uses elementary linear algebra; novelty is claimed only for the stated physical matching model's full critical surface, minimizing configurations, and finite-size order-parameter jump, subject to historical-priority uncertainty. No claim is made that general Cauchy–Schwarz, mean-field minimization or signed-graph techniques are new.

## Limitations

This theorem is for zero temperature and finite all-to-all networks; it does not establish positive-temperature thermodynamic singularities, fluctuation selection on the degenerate critical set, dynamics, quantum-spin results, or arbitrary patterns of overlapping antiferromagnetic edges. Its historical priority remains to be independently assessed, especially against older signed-complete-graph and Josephson-array literature. All global-minimum assertions are proved mathematically; no independent external scientific audit has been performed.

## References

1. L. X. Hayden, T. A. Kaplan and S. D. Mahanti, *Frustrated classical Heisenberg and XY models in 2 dimensions with nearest-neighbor biquadratic exchange: exact solution for the ground-state phase diagram*, first public arXiv submission 2010-03-29, https://arxiv.org/abs/1003.5622.
2. A. Andreanov and M. V. Fistul, *Frustration induced highly anisotropic magnetic patterns in classical XY model on kagome lattice*, arXiv first submission 2019-12-13, https://arxiv.org/abs/1912.06397.
3. J. E. Björnberg, J. Fröhlich and D. Ueltschi, *Quantum Spins and Random Loops on the Complete Graph*, Communications in Mathematical Physics 375 (2020), first journal publication 2019-11-27, https://doi.org/10.1007/s00220-019-03634-x.
4. E. Granato and J. M. Kosterlitz, *Frustrated XY model with unequal ferromagnetic and antiferromagnetic bonds*, Journal of Physics C 19 (1986), https://doi.org/10.1088/0022-3719/19/3/001 (abstract only inspected; exact first-public day not verified).
