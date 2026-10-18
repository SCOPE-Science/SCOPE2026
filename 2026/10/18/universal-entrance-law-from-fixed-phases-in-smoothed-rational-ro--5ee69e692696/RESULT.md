# Universal entrance law from fixed phases in smoothed rational rotations

## Finding

Let \(n\ge2\) and \(1\le k<n\) be coprime integers, and consider the real Euler–Osipov–Söderbacka map
\[
 F_a(x)=x+\frac{k}{n}-\frac{1}{1+e^{-ax}},\qquad a>0.
\]
Put \(h=1/(2n)\), \(q_a=e^{-ah}\), and \(R_a=F_a^{\,n}\). Fix **any** initial phase \(x_0\in(0,1/n)\setminus\{h\}\), independent of \(a\). For \(\tau\ge0\), let
\[
 m_a(\tau)=\left\lfloor\frac{\tau}{a q_a}\right\rfloor.
\]
Then, uniformly for \(\tau\) in every compact subset of \((0,\infty)\),
\[
\boxed{\lim_{a\to\infty} a\bigl(R_a^{m_a(\tau)}(x_0)-h\bigr)
=\operatorname{sgn}(x_0-h)\log\coth\tau.}
\]
The limiting profile has no dependence on the rotation numerator \(k\) or on the magnitude of the initial offset \(|x_0-h|\); only its side matters. More quantitatively, for any fixed \(0<\theta<1\), define the first-return entrance time
\[
H_a(\theta)=\min\left\{m\ge0:\exp\bigl(-a|R_a^m(x_0)-h|\bigr)\ge\theta\right\}.
\]
For sufficiently large \(a\) it is finite and obeys the **sharp first-passage law**
\[
\boxed{\lim_{a\to\infty}a e^{-a/(2n)}H_a(\theta)=\operatorname{artanh}\theta.}
\]
Thus the time required to come within a prescribed inverse-steepness neighborhood of the selected half-grid is \(\asymp e^{a/(2n)}/a\) full returns, even when the initial phase is a fixed positive distance from that grid. The full physical iterate count equals \(nH_a(\theta)\).

## Assumptions and scope

The integer pair \((n,k)\), the initial \(x_0\), and the threshold \(\theta\) are fixed before sending \(a\to+\infty\). The result is a deterministic limit for the dynamics of \(F_a\) on the real line, restricted to initial phases \(x_0\in(0,1/n)\). It does not assert uniformity as \(n\to\infty\), nor for starting phases tending to a bin endpoint as \(a\to\infty\). The convergence of the displayed phase profile excludes \(\tau=0\), where its limit diverges for an initially noncentral fixed phase.

## Proof

**1. The return displacement on an entire fixed interior interval.** Fix \(0<d<h\), and let \(K=[d,1/n-d]\). Set
\[
 G(x)=x+\frac{k}{n}-\mathbf1_{\{x>0\}},
 \qquad p_a(z)=\frac{1}{1+e^{az}}\quad(z>0).
\]
For any \(t\in K\), the \(n\) points of the discontinuous reference itinerary \(G^j(t)\), \(0\le j<n\), are precisely the grid points \(t+\ell/n\), where \(\ell\) runs through the integers \(k-n,\ldots,k-1\). In particular, the two closest grid sites to zero are \(t\) and \(t-1/n\). The former is visited at time zero; the latter exactly once later in the period. All other grid sites have absolute value at least \(1/n+d\).

For large \(a\), direct induction along this finite itinerary shows that \(F_a^j(t)\) stays within \(C_{n,d}e^{-ad}\) of \(G^j(t)\), retains all strict signs, and encounters the same branch labels. The exact error \(F_a-G\) equals \(+p_a(x)\) at positive \(x\) and \(-p_a(-x)\) at negative \(x\). Before visiting the negative nearest site \(t-1/n\), the sole possible leading correction is the first positive-site correction \(p_a(t)\); every other preceding correction has magnitude \(O_{n,d}(e^{-a(1/n+d)})\). Thus the argument of the negative-site correction differs from \(t-1/n\) by \(p_a(t)+O_{n,d}(e^{-a(1/n+d)})\).

The logistic derivative at a point \(z<0\) satisfies \(|(F_a-G)'(z)|\le C a e^{-a|z|}\). The mean-value theorem bounds the resulting change in the negative-site contribution by
\[
 C_{n,d}a\,e^{-a(1/n-t)}\,e^{-at}=C_{n,d}a e^{-a/n}.
\]
The total contribution of all other grid sites is \(O_{n,d}(e^{-a(1/n+d)})\). Summing one full period, using \(G^n(t)=t\), and writing \(q_a=e^{-a/(2n)}\), gives the **uniform global-inside-the-bin estimate**
\[
\boxed{R_a(t)-t=p_a(t)-p_a(1/n-t)+E_a(t),
\quad \sup_{t\in K}|E_a(t)|\le C_{n,d}a q_a^2.}\tag{1}
\]
The estimate holds for fixed phases throughout \(K\), not just for a shrinking neighborhood of \(h\).

**2. The return iterates stay in one compact interior interval.** The derivative is
\[
 F_a'(x)=1-\frac{a e^{-ax}}{(1+e^{-ax})^2}.
\]
All points visited in the itineraries starting in \(K\) stay at least \(d/2\) from zero when \(a\) is large. Hence every branch derivative lies strictly between zero and one, so \(0<R_a'(t)<1\) on \(K\); consequently \(R_a(t)-t\) is strictly decreasing there. By (1), the return displacement is positive at \(d\) and negative at \(1/n-d\), so the return has a unique fixed point \(t_a^*\in K\). For each fixed \(c>0\), (1) at \(t=h\pm c/a\) yields
\[
R_a(h\pm c/a)-(h\pm c/a)=q_a(e^{\mp c}-e^{\pm c})+O_{n,d}(a q_a^2).
\]
Its signs are opposite; thus \(a|t_a^*-h|<c\) eventually. Since \(c\) was arbitrary,
\[
 a(t_a^*-h)\longrightarrow0.\tag{2}
\]
Choose \(d<\min\{x_0,1/n-x_0,h\}\). For all large \(a\), the orbit \(t_m=R_a^m(x_0)\) is monotone between \(x_0\) and \(t_a^*\), because \(R_a\) is increasing and its displacement is strictly decreasing. It therefore stays in the fixed interval \(K\) for every \(m\ge0\).

**3. A phase coordinate with a uniform Euler approximation.** Put \(\sigma=\operatorname{sgn}(x_0-h)\) and
\[
 y_m=\exp[-\sigma a(t_m-h)].
\]
By monotonicity, the initial value \(y_0=e^{-a|x_0-h|}\to0\), and (2) implies \(0<y_m\le 1+o(1)<2\) for all \(m\). Let \(s_a=a q_a\). In (1) substitute
\[
 e^{-at_m}=q_a\,y_m^{\sigma},\qquad
 e^{-a(1/n-t_m)}=q_a\,y_m^{-\sigma}.
\]
Because \(t_m\in K\), both exponentials are at most \(e^{-ad}\). Taylor expansion of the logistic denominator and of \(\exp[-\sigma a(R_a(t_m)-t_m)]\) gives, **uniformly over all orbit times**,
\[
 \frac{y_{m+1}-y_m}{s_a}=1-y_m^2+\rho_{a,m},
 \qquad \sup_{m\ge0}|\rho_{a,m}|\le C_{n,d}(a e^{-ad}+a q_a)\longrightarrow0.\tag{3}
\]
For completeness, the quadratic remainder in the exponential contributes after division by \(s_a\) at most \(C a e^{-ad}\): if \(u=e^{-at_m}\), \(v=e^{-a(1/n-t_m)}\), then \(uv=q_a^2\), and \(y_m a^2(u+v)^2/(a q_a)\le C a e^{-ad}\) using \(y_m\le2\) and the relevant sign orientation. The \(O(a q_a^2)\) error in (1) contributes at most \(C a q_a\), and the logistic-denominator errors contribute \(O(e^{-ad})\). This proves (3).

Equation (3) is the explicit Euler scheme, with vanishing step \(s_a\), for the Lipschitz ODE
\[
 \dot y=1-y^2,\qquad y(0)=0.
\]
Its unique solution is \(y(\tau)=\tanh\tau\). Standard discrete Gronwall estimates (applied on \(0\le y\le2\)) yield
\[
 \sup_{0\le\tau\le T}\left|
y_{\lfloor\tau/s_a\rfloor}-\tanh\tau\right|\to0
 \quad\text{for every finite }T.\tag{4}
\]
Since \(\tanh\tau>0\) for \(\tau>0\), taking logarithms in (4) on compact positive-time intervals, and using \(a(t_m-h)=-\sigma\log y_m\), gives the claimed signed \(\log\coth\tau\) profile.

**4. First-passage limit.** On the approach to \(t_a^*\), the sequence \(y_m\) is nondecreasing, while \(\exp[-a|t_m-h|]\) differs from \(y_m\) by \(o(1)\) at most after a possible crossing of \(h\), by (2). Given \(0<\theta<1\), the strictly increasing limiting function \(\tanh\tau\) reaches \(\theta\) at \(\tau=\operatorname{artanh}\theta\). Uniform convergence (4), a bracket by times just before and after this crossing, and monotonicity imply \(s_a H_a(\theta)\to\operatorname{artanh}\theta\). This concludes the proof.

## Verification

The standalone standard-library script `check_eos_entry.py` evaluates exact iterates of the original smooth map for four coprime pairs, both sides of the reference half-grid, and two steepness values. It checks convergence to the explicit \(\log\coth\tau\) profile and to the normalized first-passage clock, and checks the complete-return expansion independently. These are finite diagnostic tests, not proofs of the quantified limits. The proof above supplies the uniform errors and limiting arguments.

## Relationship to prior work

Bielawski et al. [1] prove almost-everywhere convergence to a rational-rotation-like attracting orbit for sufficiently steep EOS maps and give a qualitative explanation of similar behavior across different numerators. They do not quantify the complete entrance time for a fixed starting phase.

A published quantitative EOS result [2] proves the selected half-grid orbit, its first positional correction, and the local period multiplier \(1-2a e^{-a/(2n)}+O(a^2e^{-a/n})\). It also derives a return displacement expansion on a neighborhood whose width **shrinks exponentially to zero** with \(a\). Those facts motivate the slow time but do not establish the present entrance law from an initial phase at a fixed nonzero distance, which requires the uniform estimate (1) on a full interior compact interval. In particular, the fixed-phase entrance profile is not obtained merely by linearizing at the attracting periodic orbit.

Earlier sigmoid game-map papers [3,4] study periodicity, chaos, and global attraction, rather than the precise fixed-phase, inverse-steepness first-passage asymptotic. Standard Euler convergence is a proof technique used after a model-specific displacement estimate; its use alone is not the novelty claim.

## Limitations

The theorem treats one full-return phase bin \((0,1/n)\) and fixed \(n,k,x_0\). The exact transition of a starting phase that itself approaches \(0\), \(1/n\), or \(h\) with \(a\) may have different entrance scales. No uniform estimate for growing \(n\), no all-real-line basin-entry law, and no optimal finite-\(a\) constants are asserted. Independent mathematical and bibliographic validation has not been performed.

## References

[1] J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Interval maps mimicking circle rotations*, arXiv:2411.01495v1, first public version November 3, 2024, Sections 2–5. https://arxiv.org/abs/2411.01495

[2] *Singular half-grid selection and exponentially weak attraction in rational EOS maps*, mathematical research record, October 2026. Published research record available under this title in https://github.com/published-finding corpus/2026

[3] T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831v1, 2018. https://arxiv.org/abs/1807.06831

[4] J. Bielawski, T. Chotibut, F. Falniowski, M. Misiurewicz, G. Piliouras, *Unpredictable dynamics in congestion games: memory loss can prevent chaos*, arXiv:2201.10992 (2022), accessible manuscript precursor to *Memory loss can prevent chaos in games dynamics*, *Chaos* 34, 013146 (2024), DOI:10.1063/5.0184318.
