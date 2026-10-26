# Parity-split mobility crossover for annihilating walks on finite stars

## Finding
Let \(S_m=K_{1,m}\) have one hub and \(m\ge1\) leaves. Each occupied leaf carries one particle which jumps to the hub at rate one; a particle at the hub jumps at total rate \(\nu>0\), selecting a uniformly random leaf. Whenever a jump lands on an occupied vertex, both particles annihilate. No new particles are introduced. Let \(T\) be the first time the process has at most one particle.

For each possible initial configuration, the exact expectation \(\mathbb E T\) depends only on the number \(k\) of occupied leaves and whether the hub is occupied. Write \(H_j=\sum_{i=1}^j 1/i\), with \(H_0=0\), and set
\[
 t=\frac{m}{m+\nu},\qquad c=\frac{m\nu}{m+\nu},\qquad d=\frac{\nu(m+1)}{m+\nu}.
\]
If the hub is occupied, write \(a_k=\mathbb E T\). Then \(a_0=0\) and, for every \(1\le k\le m\),
\[
 a_k=\begin{cases}
 cH_{k/2}+(1-d)(H_k-1)-\dfrac{d}{k+1},&k\text{ even},\\[2mm]
 (t+c)H_k-cH_{(k-1)/2}-\dfrac{d}{k+1},&k\text{ odd}.
 \end{cases}
\]
If the hub is vacant, \(b_0=b_1=0\) and \(b_k=1/k+a_{k-1}\) for \(2\le k\le m\).

For the fully occupied star, write \(E_m(\nu)=a_m\). Its exact parity formulas are
\[
 E_m(\nu)=\begin{cases}
 c(1+H_{m/2}-H_m)+t(H_m-1)-\dfrac{\nu}{m+\nu},&m\text{ even},\\[2mm]
 c(H_m-H_{(m-1)/2})+tH_m-\dfrac{\nu}{m+\nu},&m\text{ odd}.
 \end{cases}
\]
For fixed \(\nu>0\), letting \(m\) tend to infinity through either parity and denoting Euler's constant by \(\gamma_{\rm E}\),
\[
 E_m(\nu)=\begin{cases}
 \log m+\gamma_{\rm E}+\nu(1-\log2)-1+o(1),&m\text{ even},\\
 \log m+\gamma_{\rm E}+\nu\log2+o(1),&m\text{ odd}.
 \end{cases}
\]
The odd-minus-even asymptotic constant is \(1+\nu(2\log2-1)>0\). More generally, for any positive sequence \(\nu_m=o(m)\),
\[
 E_m(\nu_m)=\log m+\nu_m C_{\mathrm{parity}}+o(\log m+\nu_m),\quad
 C_{\mathrm{even}}=1-\log2,\quad C_{\mathrm{odd}}=\log2.
\]
Thus hub mobility on the scale \(\nu_m\asymp\log m\) changes the leading logarithmic coefficient. At the larger scale \(\nu_m/m\to\theta\in(0,\infty)\),
\[
 \lim_{\substack{m\to\infty\\m\text{ even}}}\frac{E_m(\nu_m)}m
 =\frac{\theta}{1+\theta}(1-\log2),\qquad
 \lim_{\substack{m\to\infty\\m\text{ odd}}}\frac{E_m(\nu_m)}m
 =\frac{\theta}{1+\theta}\log2.
\]
The two parity classes therefore have different, explicitly controlled linear-time limits under hub mobility proportional to the number of leaves.

## Assumptions and scope
The star has labeled leaves but permutations of the leaves are symmetries. Initially every vertex is either empty or singly occupied; subsequent instantaneous annihilations preserve this. The hub jump rate \(\nu\) is the **total** departure rate from the occupied hub, not the rate per incident edge. Leaf jump rates are one. Independent exponential clocks and almost-surely separated jumps define the continuous-time chain. The stopping time is first arrival in the set with zero or one particle, whether or not its remaining particle later moves. For \(m=1\) the formulas still apply. The parity asymptotics use a fully occupied initial state and do not claim a limit for configurations with other occupancies.

## Proof
Write \(A_k\) for configurations with the hub and \(k\) leaves occupied, and \(B_k\) for configurations with the hub vacant and \(k\) leaves occupied. Since leaf permutations act transitively on each class, the expected hitting times \(a_k,b_k\) are well-defined. States \(A_0,B_0,B_1\) already have at most one particle and have expectation zero.

From \(B_k\), for \(k\ge2\), any of the \(k\) leaf particles moves to the empty hub, at total rate \(k\), producing \(A_{k-1}\). Thus
\[
 b_k=\frac1k+a_{k-1}.
\]
From \(A_k\), with \(k\ge1\), a leaf jump collides with the hub at total rate \(k\). A hub jump chooses an occupied leaf with probability \(k/m\), colliding at rate \(\nu k/m\), or an empty leaf with probability \((m-k)/m\), reaching \(B_{k+1}\) at rate \(\nu(m-k)/m\). First-step conditioning therefore gives
\[
 (k+\nu)a_k=1+k\left(1+\frac\nu m\right)b_{k-1}
 +\frac{\nu(m-k)}m b_{k+1}.
\]
The last summand vanishes when \(k=m\). Otherwise \(b_{k+1}=1/(k+1)+a_k\), and substitution followed by cancellation yields for *all* \(1\le k\le m\)
\[
 a_k=b_{k-1}+\frac{t+c}{k}-\frac{d}{k+1},
 \qquad t+c=\frac{m(1+\nu)}{m+\nu},\quad d=c+1-t.
\]
For \(k=1,2\) use \(b_0=b_1=0\). For \(k\ge3\), using \(b_{k-1}=1/(k-1)+a_{k-2}\) gives
\[
 a_k-a_{k-2}=\frac1{k-1}+\frac{t+c}{k}-\frac{d}{k+1}.
\]
Summing over odd or even indices, using \(\sum_{j=1}^h(2j)^{-1}=H_h/2\) and \(\sum_{j=1}^h(2j-1)^{-1}=H_{2h}-H_h/2\), gives exactly the two closed formulas for \(a_k\). All transient configurations can reach a collision in finitely many jumps with positive probability; finiteness of the state space and absence of nonabsorbing closed classes imply a finite mean and uniqueness of these backward-equation solutions.

Setting \(k=m\), and simplifying with \(d/(m+1)=\nu/(m+\nu)\), yields the displayed full-occupancy formulas. The elementary estimates
\[
 H_m=\log m+\gamma_{\rm E}+O(m^{-1}),\quad
 H_{m/2}-H_m=-\log2+O(m^{-1})\ \ (m\text{ even}),
\]
\[
 H_m-H_{(m-1)/2}=\log2+O(m^{-1})\ \ (m\text{ odd})
\]
prove the fixed-\(\nu\) results on using \(t\to1\) and \(c\to\nu\). If \(\nu_m=o(m)\), then \(t=1+O(\nu_m/m)\) and \(c=\nu_m+O(\nu_m^2/m)\); errors are \(o(\log m+\nu_m)\), giving the uniform intermediate regime. Finally, if \(\nu_m/m\to\theta\in(0,\infty)\), then \(c/m\to\theta/(1+\theta)\), while \(tH_m/m\to0\) and \(\nu_m/((m+\nu_m)m)\to0\). The harmonic differences yield the two linear-time limits. No finite enumeration is used for these infinite statements.

## Verification
The standalone program `verify_annihilation.py` uses only the Python standard library. It independently enumerates every occupancy subset on stars with one through eight leaves and five positive rational hub rates per size. It checks the exact full-generator Poisson equations for all 4,840 transient states so generated. For stars with up to four leaves, it additionally solves independent exact-rational linear systems over the full labeled-state generator and compares 210 transient state values. It checks 12 fixed-speed large-size approximations and six linearly scaled mobility approximations, at explicit finite test sizes and tolerances. Execution produced PASS on all four groups. These finite comparisons are corroboration; the full-range result is proved above.

## Relationship to prior work
Athreya and Swart (arXiv:1203.6477, first public 2012-03-29) establish general branching/annihilation/coalescence constructions and dualities, and explicitly classify their subject primarily under 82C22. Their results do not evaluate the finite-star absorption expectation or its site-dependent hub-rate scaling.

Cristali et al. (arXiv:1908.03218, first public 2019-08-08) study two-color annihilation on complete and star graphs. Their Proposition 1 already exactly describes the **one-color discrete step count**, starting with particles on an even number of leaves and the center vacant, at homogeneous movement speeds. That prior special case is not claimed to be new. Their later asymmetry changes *particle-color* speeds in a two-type model, not the *location-dependent* hub clock of the present single-type model. Its full-occupancy all-rate parity crossover and all-initial-state continuous-time means do not follow from that published proposition as stated.

Krapivsky, Ben-Naim, and Redner (arXiv:cond-mat/9406109, first public 1994-06-27) develop heterogeneous single-species annihilation kinetics with particle-dependent diffusivities on extended systems, rather than this finite star with a different rate at its hub. The relevant foundation is credited; no priority over more general unlocated star-specific formulas is asserted.

## Limitations
The results are restricted to independent exponential jump clocks, instantaneous pair annihilation, one occupied particle per vertex, and a star with identical unit-rate leaves and a uniform destination choice at the hub. They concern means, not complete extinction-time laws, spatially varying leaf clocks, branching, or multi-species annihilation. The exact all-state formula is elementary once the symmetry reduction is recognized; the main additional information is the quantitative mobility/parity scaling. Exhaustive bibliographic novelty is not asserted. External independent verification remains unperformed.

## References
1. S. Athreya and J. M. Swart, *Systems of branching, annihilating, and coalescing particles*, Electronic Journal of Probability **17** (2012), article 80; arXiv:1203.6477 (first submitted 2012-03-29). https://arxiv.org/abs/1203.6477
2. I. Cristali, Y. Jiang, M. Junge, R. Kassem, D. Sivakoff, G. York, *Two-type annihilating systems on the complete and star graph*, arXiv:1908.03218 (2019-08-08). https://arxiv.org/abs/1908.03218
3. P. L. Krapivsky, E. Ben-Naim, S. Redner, *Kinetics of heterogeneous single-species annihilation*, Physical Review E **50** (1994), 2474–2481; arXiv:cond-mat/9406109 (1994-06-27). https://arxiv.org/abs/cond-mat/9406109
