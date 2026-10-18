# Sharp minority relaxation and a polynomial dissent cascade in incremental voter dynamics

## Finding

For the Cao–Gong mean-field incremental voter model with an integer opinion radius \(k\geq1\), suppose a non-consensus initial probability profile converges to the upper extreme opinion \(+k\). Put \(a_k=1-1/(2k)\). Then there is a profile-dependent constant \(C\in(0,\infty)\) such that
\[
\lim_{t\to\infty}e^{a_kt}p_{k-1}(t)
=\lim_{t\to\infty}e^{a_kt}(1-p_k(t))
=\lim_{t\to\infty}e^{a_kt}(k-m(t))=C.
\]
Here \(m(t)=\sum_{j=-k}^k j p_j(t)\). For \(k\geq2\), there is another profile-dependent constant \(B\in(0,\infty)\) such that, simultaneously for every integer \(2\leq d\leq2k\),
\[
\lim_{t\to\infty}\frac{e^t p_{k-d}(t)}{t^{2k-d}}
=\frac{B}{(2k-d)!},\qquad
B=\lim_{t\to\infty}e^t p_{-k}(t).
\]
For the exceptional three-opinion case \(k=1\), the far-opposite tail instead obeys the resonant law
\[
\lim_{t\to\infty}\frac{e^t p_{-1}(t)}{t}=\frac{C^2}{2}.
\]
All assertions reflect under \(j\mapsto-j\) for trajectories converging to the lower consensus. The constants are positive and finite, not unspecified rates in upper bounds. In particular the slow decay exponent \(a_k\) is exact and the entire spectrum of residual opinions has a sharply resolved polynomial-exponential hierarchy.

## Assumptions and scope

For \(k\in\mathbb N\), consider probability vectors \((p_{-k},\ldots,p_k)\) on the \(2k+1\) discrete opinions with the evolution in Cao and Gong, *The incremental voter model: mean-field analysis and convergence to equilibrium*, equation (2.1): upward transition rate \(u=(k+m)/(2k)\) and downward transition rate \(v=(k-m)/(2k)\), both with reflecting endpoints. Explicitly,
\[
\begin{aligned}
\dot p_{-k}&=v p_{-k+1}-u p_{-k},\\
\dot p_j&=v p_{j+1}+u p_{j-1}-p_j\quad(-k<j<k),\\
\dot p_k&=u p_{k-1}-v p_k,
\end{aligned}
\]
where the interior indices follow the usual increasing opinion order. The upper-consensus result assumes \(p_k(t)\to1\) and \(p(0)\ne\delta_k\); it does not claim a complete basin classification. A verifiable sufficient initial condition is \(m(0)>k-1\), under which the motivating paper's Theorem 3 (and Proposition 3.2 for \(k=1\)) proves the required convergence. The mirrored sufficient condition is \(m(0)<1-k\). We work with the deterministic mean-field ODE, not the finite-agent chain, and with the time normalization of equation (2.1).

## Proof

**1. Deficit coordinates.** For \(0\leq d\leq2k\), set \(b_d(t)=p_{k-d}(t)\), so \(b_0=1-\sum_{d=1}^{2k}b_d\). Write
\[
\delta(t)=k-m(t)=\sum_{d=1}^{2k}d b_d(t),\qquad
v=\frac\delta{2k},\qquad u=1-v.
\]
The equations become exactly
\[
\begin{aligned}
\dot b_0&=u b_1-vb_0,\\
\dot b_d&=u b_{d+1}+v b_{d-1}-b_d\quad(1\leq d<2k),\\
\dot b_{2k}&=v b_{2k-1}-u b_{2k}.
\end{aligned}
\]
Because the trajectory converges to \(\delta_k\), the vector \(b=(b_1,\ldots,b_{2k})\) tends to zero. The interior of the probability simplex is instantaneously entered by every initial profile that is neither consensus, as long as \(0<u,v<1\); convergence to the upper consensus excludes the opposite absorbing point. Thus all \(b_d(t)>0\) for \(t>0\), and \(\delta(t)>0\) at finite times.

**2. Exact linear spectrum and an explicitly positive slow projection.** Expansion at \(b=0\) gives
\[
\dot b=L b+R(b),\qquad \lVert R(b)\rVert\leq K_k\lVert b\rVert^2
\]
for small \(b\). The first row of \(L\) is
\[
L_{1j}=\frac{j}{2k}+\mathbf1_{\{j=2\}}-\mathbf1_{\{j=1\}},
\]
while for \(2\leq d\leq2k\) its row has \(L_{dd}=-1\) and, when \(d<2k\), \(L_{d,d+1}=1\); all other entries vanish. Thus the eigenvalues are \(-a_k\) (simple) and \(-1\) (algebraic multiplicity \(2k-1\)). An explicit strictly positive left eigenvector \(c\) for \(-a_k\), normalized by \(c_1=1\), is
\[
c_1=1,\qquad c_d=2k\,c_{d-1}+d\quad(2\leq d\leq2k).
\]
Define \(H=\sum_{d=1}^{2k}c_d b_d>0\). Exact substitution shows
\[
\dot H=-a_kH+E(t),\qquad |E(t)|\leq K_k\delta(t)^2,
\]
and \(\delta\leq H\leq C_k\delta\). Exponential stability of the Hurwitz matrix \(L\), a variation-of-constants estimate, and the quadratic bound on \(R\) give, for each sufficiently small \(\varepsilon>0\),
\[
\lVert b(t)\rVert\leq A_\varepsilon e^{-(a_k-\varepsilon)t}
\quad(t\geq0).
\]
For clarity, choose a matrix-semigroup bound \(\lVert e^{Lt}\rVert\leq M e^{-(a_k-\varepsilon/2)t}\); take a late time at which the quadratic Lipschitz term is less than \(\varepsilon/(2M)\), and apply convolution Grönwall to the Duhamel formula. In particular \(H\) and \(\delta\) are integrable over \([0,\infty)\). Therefore
\[
\left|\frac{d}{dt}\log(e^{a_kt}H(t))\right|
=\frac{|E(t)|}{H(t)}\leq K_k\delta(t)
\]
is integrable. It follows that \(e^{a_kt}H(t)\to C\in(0,\infty)\). Strict positivity follows because the logarithm converges to a finite real value, rather than merely being bounded above.

**3. Far-opposite edge for \(k\geq2\).** Fix \(\varepsilon>0\) small enough that \(2(a_k-\varepsilon)>1\), possible precisely when \(k\geq2\). The previous decay estimate implies
\[
\int_0^\infty e^t v(t)\sum_{d=1}^{2k}b_d(t)\,dt<\infty.
\]
The last deficit equation yields the *exact* integrating-factor identity
\[
\frac{d}{dt}\big(e^tb_{2k}(t)\big)
=e^tv(t)\big(b_{2k-1}(t)+b_{2k}(t)\big)\geq0.
\]
It has a finite limit \(B\); the instantaneous positivity from Step 1 makes \(B>0\). For each \(2\leq d<2k\), similarly,
\[
\frac{d}{dt}(e^tb_d)
=e^t b_{d+1}+e^t v(b_{d-1}-b_{d+1}).
\]
The last term belongs to \(L^1([0,\infty))\) uniformly for each fixed \(d\). Starting from \(e^tb_{2k}\to B\) and integrating these identities successively downwards proves by induction
\[
e^tb_d(t)=\frac{B}{(2k-d)!}\,t^{2k-d}+o(t^{2k-d})
\quad(2\leq d\leq2k).
\]
In particular every \(b_d\), \(d\geq2\), is \(o(e^{-a_kt})\); hence \(H=b_1+o(e^{-a_kt})\), \(\delta=b_1+o(e^{-a_kt})\), and \(1-b_0=b_1+o(e^{-a_kt})\). Step 2 now supplies all three sharp slow-coordinate limits.

**4. The resonance at \(k=1\).** Now \(a_1=1/2\). Select \(0<\varepsilon<1/4\) in Step 2. The integrating-factor relation for \(b_2\) implies
\[
b_2(t)=O(e^{-(1-2\varepsilon)t})=o(e^{-t/2}),
\]
because the integrand \(e^tv(b_1+b_2)\) is \(O(e^{2\varepsilon t})\). Consequently \(b_1(t)\sim Ce^{-t/2}\) and \(v(t)=(b_1+2b_2)/2\sim(C/2)e^{-t/2}\). The same exact identity sharpens to
\[
\frac{d}{dt}(e^tb_2)=e^t v(b_1+b_2)\longrightarrow\frac{C^2}{2}.
\]
Integration (or Cesàro averaging) yields \(e^t b_2(t)/t\to C^2/2\). This is a genuine resonance: \(2a_1=1\), whereas \(2a_k>1\) for all \(k\geq2\).

**5. Reflection.** The source equations are invariant under replacing opinion \(j\) by \(-j\), which exchanges the two extreme consensuses. Every preceding step therefore applies to the lower consensus with the opinion indices reflected.

## Verification

The standalone file `verify_incremental_voter.py` reconstructs the ODE; for \(k=1,2,3,4,5\) it computes the Jacobian and the explicit positive left eigenvector with exact rational symbolic algebra, checks that the projected remainder has no constant or linear part, and tests the mass-conservation identity. It also integrates examples for \(k=1,2,3\) and reports the rescaled minority coordinates (including the resonant three-opinion normalization). The numerical trajectories are diagnostics only; the proof above establishes the infinite-time assertions for every integer \(k\geq1\). Run with `python verify_incremental_voter.py` after installing the public dependencies `numpy`, `sympy`, and `scipy`.

## Relationship to prior work

Cao and Gong (arXiv:2605.28984, Section 3) prove consensus selection for specified initial means and an \(e^{-t/8}\) *upper bound* for three opinions, and explicitly identify quantitative convergence rates for more than three opinions as an open direction (Section 4). Those results and the model equations are prerequisites, not claimed here. The present theorem gives the *exact* slow exponent \(1-1/(2k)\), positive asymptotic amplitudes, every remote-state polynomial prefactor, and the three-opinion nonlinear resonance. General finite-dimensional hyperbolic linearization explains the first exponent locally, but without the positive projection and integrating-factor analysis does not give the displayed strict amplitude limits and cascades. Earlier iterative persuasion–polarization (Cao–Reed) and continuous-valued fractal-opinion (Cao–Cortez) models have different update laws. This is not a theorem about those systems.

## Limitations

The theorem is conditional on attraction to an extreme consensus; it does not solve the source's complete basin problem for arbitrary higher-opinion initial profiles. Its constants \(C,B\) depend on the full initial state and are characterized by limits rather than closed elementary formulas. All conclusions are deterministic mean-field, not fixation times or fixation probabilities for finite agent populations. Finite numerical checks are not certification of the infinite-time laws; those follow from the proof. Historical priority beyond the inspected sources has not been independently confirmed.

## References

1. F. Cao and X. Gong, *The incremental voter model: mean-field analysis and convergence to equilibrium*, arXiv:2605.28984, first posted May 27, 2026. https://arxiv.org/abs/2605.28984
2. F. Cao and S. Reed, *The Iterative Persuasion-Polarization Opinion Dynamics and Its Mean-Field Analysis*, SIAM J. Appl. Math. 85 (2025), 1596–1620. https://doi.org/10.1137/24M1700661
3. F. Cao and R. Cortez, *Fractal Opinions among Interacting Agents*, SIAM J. Appl. Dyn. Syst. 24 (2025), 1529–1552. https://doi.org/10.1137/24M1682269
