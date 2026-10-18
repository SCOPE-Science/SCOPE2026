# Critical \(n^{4/3}\) consensus law at the biased two-choices threshold

## Finding
Consider the asynchronous binary-opinion model on a complete graph of \(n\ge3\) agents, in which one uniformly selected agent updates at each integer time. With probability \(\alpha=1/9\), it adopts the superior opinion \(1\). Otherwise it samples two distinct-index neighbors **with replacement** and adopts the majority among those two opinions and its own. Let \(K_t\) be the number of superior opinions, and \(\tau_n=\inf\{t:K_t=n\}\). All times count **individual updates**, not parallel rounds.

Set \(a=32/9\) and, for real \(s\),
\[
F(s)=8\int_s^\infty\int_{-\infty}^{u}
\exp\!\left[-a(u^3-v^3)\right] \,dv\,du.
\]
These integrals are finite and strictly positive. For every fixed real \(s\) and every sequence of integers \(k_n\in\{0,\ldots,n\}\) satisfying \((k_n-n/4)/n^{2/3}\to s\),
\[
\lim_{n\to\infty}n^{-4/3}\,\mathbb E_{k_n}[\tau_n]=F(s).
\]
For every fixed initial fraction \(0\le p<1/4\), with \(k_n=\lceil pn\rceil\),
\[
\lim_{n\to\infty} n^{-4/3}\,\mathbb E_{k_n}[\tau_n]
=C=\frac83\sqrt{\frac{3\pi}{32}}\left(\frac98\right)^{1/6}\Gamma\!\left(\frac16\right)
=8.21528406648\ldots .
\]
For \(p=1/4\), the corresponding limit is \(F(0)\), strictly between zero and \(C\). For each fixed \(1/4<p<1\),
\[
\mathbb E_{\lceil pn\rceil}[\tau_n]\sim n\log n.
\]
Thus the equality case of the bias threshold has a polynomial critical bottleneck, of order \(n^{4/3}\), rather than either of the two previously established off-critical regimes.

## Assumptions and scope
The network is the complete *simple* graph; a regular update samples neighbors, excluding the updating agent, with replacement. Opinion \(1\) is imposed by a biased update, not by a fair random mutation. The bias parameter is fixed **exactly** at \(1/9\); initial states depend on the number of superior opinions only. The asymptotic results hold along all integers \(n\to\infty\), and there is no claim here about random-graph topologies, parallel updates, or bias approaching the critical value at an \(n\)-dependent rate.

## Proof
**1. Exact reduction and hitting-time identity.** From any nonabsorbed count \(0\le k<n\), write \(\lambda_{n,k}=\Pr(K_{t+1}=k+1\mid K_t=k)\) and \(\mu_{n,k}=\Pr(K_{t+1}=k-1\mid K_t=k)\). Direct conditioning on the chosen agent and on two replacement samples yields
\[
\lambda_{n,k}=\frac{n-k}{9n}\left(1+8\frac{k^2}{(n-1)^2}\right),\qquad
\mu_{n,k}=\frac{8k}{9n}\frac{(n-k)^2}{(n-1)^2}.
\]
(The latter vanishes at \(k=0\).) The probability of remaining at \(k\) is the complement. Absorption occurs almost surely because every nonabsorbed state can reach the top by a positive-probability sequence of biased updates.

Put \(H_{n,k}=\mathbb E_k\tau_n\), \(H_{n,n}=0\), and \(d_{n,k}=H_{n,k}-H_{n,k+1}\). The first-step equations are equivalent to
\[
\lambda_{n,k}d_{n,k}-\mu_{n,k}d_{n,k-1}=1,
\quad d_{n,0}=\lambda_{n,0}^{-1}=9.
\]
Hence, with \(r_{n,\ell}=\mu_{n,\ell}/\lambda_{n,\ell}\), exactly
\[
d_{n,k}=\sum_{j=0}^{k}\frac{1}{\lambda_{n,j}}
\prod_{\ell=j+1}^{k}r_{n,\ell},\qquad
H_{n,k}=\sum_{h=k}^{n-1}d_{n,h}.
\tag{1}
\]
Empty products equal one. This identity holds for the *original neighbor-only model*, without passing through a surrogate chain.

**2. Critical cubic potential.** The ratio is
\[
r_{n,k}=\frac{8k(n-k)}{(n-1)^2+8k^2}.
\]
Compare it with the modified self-sampling ratio \(f(x)=8x(1-x)/(1+8x^2)\):
\[
1-f(x)=\frac{(4x-1)^2}{1+8x^2},\quad
f(k/n)\le r_{n,k}\le\left(\frac{n}{n-1}\right)^2f(k/n).
\tag{2}
\]
In particular the ratio is close to one only near \(k=n/4\). For fixed bounded real \(v\le u\), uniformly over indices in bounded rescaled intervals, using \(k= n/4+n^{2/3}u+O(1)\), \(j=n/4+n^{2/3}v+O(1)\),
\[
\sum_{\ell=j+1}^{k}\log r_{n,\ell}
\longrightarrow-\frac{32}{9}(u^3-v^3),
\qquad \lambda_{n,j}\longrightarrow\frac18.
\tag{3}
\]
Indeed, on that window \(\log r_{n,\ell}=-(32/3)(\ell-n/4)^2/n^2+O(n^{-1})+o(n^{-2/3})\), uniformly on bounded rescaled intervals. The sum is a Riemann sum, and the \(O(n^{-1})\) perturbation from excluding the updating agent contributes only \(O(n^{-1/3})\).

**3. Global domination and integrability.** As \(1-f(x)\ge(16/9)(x-1/4)^2\), (2) gives absolute constants \(c_0,C_0>0\) such that
\[
\prod_{\ell=j+1}^{k}r_{n,\ell}
\le C_0\exp\!\left[-\frac{c_0}{n^2}
\sum_{\ell=j+1}^{k}(\ell-n/4)^2\right].
\tag{4}
\]
For \(m=k-j\), the square sum is at least \((m^3-m)/12\). Moreover, if \(u=|k-n/4|\), it is at least \(mu^2\) when \(k\le n/4\), and at least \(mu^2/4\) when \(k>n/4\) and \(m\le u/2\). Splitting remaining terms at \(m=u/2\), the cubic bound controls their tail. Therefore, for \(k\le n/2\), noting that \(\lambda_{n,j}\ge1/18\) for \(j\le k\),
\[
d_{n,k}\le\frac{C_1 n^{2/3}}{1+\bigl((k-n/4)/n^{2/3}\bigr)^2}.
\tag{5}
\]
For \(k\ge n/2\), all ratios with \(\ell\ge3n/8\) are uniformly below a constant \(q<1\) for sufficiently large \(n\). Terms beginning below \(3n/8\) contain at least order \(n\) such factors and are exponentially small; the other terms form a geometric sum. Thus
\[
d_{n,k}\le C_2\frac{n}{n-k}+O(nq^{cn}),
\qquad \sum_{k\ge n/2}d_{n,k}=O(n\log n)=o(n^{4/3}).
\tag{6}
\]
All constants in these bounds are independent of \(n\). Bound (5) is integrable on the rescaled spatial line and makes the tails outside an arbitrarily large bounded rescaled interval negligible after division by \(n^{4/3}\).

**4. The finite-size limit.** With \(h=n^{2/3}\), applying (3) to the inner sum of (1), then using (4) to bound its tails, gives for every finite real \(u\),
\[
\frac{d_{n,\lfloor n/4+hu\rfloor}}h
\longrightarrow 8\int_{-\infty}^u
\exp\!\left[-\frac{32}{9}(u^3-v^3)\right]dv.
\]
Now (5)–(6) justify dominated Riemann summation of the second identity in (1). If \((k_n-n/4)/h\to s\), this proves convergence to \(F(s)\). If \(k_n\le(1/4-\epsilon)n\) for a fixed \(\epsilon>0\), the rescaled lower limit tends to minus infinity; the same tail bounds give the full-line limit \(C\).

To evaluate \(C\), put \(w=(u+v)/2\) and \(z=u-v>0\). Then \(u^3-v^3=3w^2z+z^3/4\); integrate the Gaussian in \(w\), then use \(\int_0^\infty z^{-1/2}e^{-az^3/4}dz=\Gamma(1/6)(4/a)^{1/6}/3\). This yields the stated gamma constant. The integral representation also shows that \(F(s)>0\) for every finite \(s\), \(F(s)\downarrow0\) as \(s\to\infty\), and \(F(s)\uparrow C\) as \(s\to-\infty\).

**5. Above-threshold initial fractions at critical bias.** Fix \(p>1/4\). For \(k\ge\lceil pn\rceil\), the ratios in (2) are uniformly bounded below one, apart from exponentially suppressed portions of products that start below \(pn\). Thus (1) gives \(d_{n,k}=O(n/(n-k))\), so \(H_{n,\lceil pn\rceil}=O(n\log n)\). For every fixed \(\delta>0\) and \(k\ge(1-\delta)n\), the up-step probability is \((n-k)/n\,[1+O(\delta+n^{-1})]\), and the products of ratios in (1) sum to \(1+O(\delta)\) (with exponentially suppressed remote terms). Consequently the final \(\delta n\) states contribute \((1+O(\delta))n\log n+O(n)\); the earlier states contribute at most \(O_\delta(n)\). Letting \(\delta\downarrow0\) proves \(H_{n,\lceil pn\rceil}\sim n\log n\).

## Verification
The standalone standard-library script `checker.py` constructs the *exact neighbor-only* transition probabilities, independently solves the finite absorbing-chain linear equations by rational Gaussian elimination, and checks the hitting-time difference recurrence for both the original model and the modified self-sampling comparison. It also prints finite-size values of \(n^{-4/3}\mathbb E_0\tau_n\), of the threshold-start scaling, and of the above-threshold coupon-collector scaling. The finite checks cannot establish the asymptotic theorem; Steps 1–5 above provide the proof.

## Relationship to prior work
Mukhopadhyay's 2022 preprint (and 2023-online/2024-volume journal article) gives the biased two-choices model and proves fast consensus for \(\alpha>1/9\) and an exponentially slow regime for \(\alpha<1/9\). Its stated main theorem omits the equality \(\alpha=1/9\). The present claim describes precisely that critical case, including the \(n^{2/3}\) initial-state window and the \(n^{4/3}\) expected-time scale. The source derives an absorbing birth-death reduction for a slightly modified chain; here we use exact transitions of the original neighbor-only process.

Cruciani, Mimun, Quattropani and Rizzo study **parallel/synchronous** majority updates with a different objective (maintaining an initial majority in the presence of biased communication); their critical bias values do not determine the individual-update full-consensus hitting-time law here. General birth-death methods support the recurrence, but no inspected source furnishes this model-specific critical scaling function or its gamma constant.

## Limitations
The result is an asymptotic theorem at the exact bias value, not a uniform assertion for parameters that vary with \(n\). It concerns expectation, not a full weak limit of the random absorption time. The limiting diffusion suggested by the integral is not asserted as a pathwise or distributional convergence theorem. No assertion of prior-art uniqueness is made; unindexed work on noisy voter/majority critical windows or on general saddle-node birth-death chains could contain an equivalent scaling statement. Numerical checks use finite \(n\) and do not replace the analytic bounds.

## References
1. Arpan Mukhopadhyay, *Phase Transitions in Biased Opinion Dynamics with 2-choices Rule*, first public arXiv version submitted 2022-08-25, arXiv:2208.12245, https://arxiv.org/abs/2208.12245 ; journal version *Probability in the Engineering and Informational Sciences* 38 (2024), 227–244, published online 2023-03-10, doi:10.1017/S0269964823000098.
2. Emilio Cruciani, Hlafo Alfie Mimun, Matteo Quattropani, Sara Rizzo, *Phase Transition of the k-Majority Dynamics in Biased Communication Models*, first public arXiv version 2020-07-30, arXiv:2007.15306, https://arxiv.org/abs/2007.15306 ; *Distributed Computing* (2023), doi:10.1007/s00446-023-00444-2.
