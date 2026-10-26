# Opposed-part consensus in zero-temperature bipartite Glauber dynamics: an exact beta race and a Gaussian reversal window

## Finding
Consider continuous-time zero-temperature ferromagnetic Glauber dynamics with independent unit-rate vertex update clocks on the complete bipartite graph \(K_{m,n}\), where \(m=2u+1\ge3\) and \(n=2v+1\ge3\) are odd. Initially exactly \(a\in\{u+1,\ldots,m\}\) spins in the first part are positive and exactly \(b\in\{v+1,\ldots,n\}\) spins in the second part are negative. Thus the two parts have strictly opposed majorities.

Write \(T_+\) for the event that the system ultimately reaches unanimous positive spin. With \(\mathrm B\) denoting Euler's beta function, the **exact finite-size consensus probability** is
\[
\boxed{\mathbb P(T_+)=\frac{1}{\mathrm B(v+1,b-v)}\sum_{j=u+1}^{a}\binom aj\mathrm B(v+1+j,b-v+a-j).}
\]
Equivalently, for two independent beta random variables
\[
X\sim\mathrm{Beta}(u+1,a-u),\qquad Y\sim\mathrm{Beta}(v+1,b-v),
\]
we have \(\mathbb P(T_+)=\mathbb P(Y>X)\). Here \(\mathrm{Beta}\) is the probability distribution, whereas \(\mathrm B\) denotes the beta integral.

**Exact polarization symmetry:** If both parts are initially uniformly but oppositely polarized, \(a=m\) and \(b=n\), then \(\mathbb P(T_+)=1/2\) for all odd \(m,n\), even if their sizes differ arbitrarily.

**Consensus transition and critical window:** For a sequence of odd part sizes \(m,n\to\infty\) with \(n/m\to\kappa\in(0,\infty)\), suppose the initial positive fraction \(p_m=a/m\) in the first part and initial negative fraction \(q_n=b/n\) in the second converge to \(p,q>1/2\). Then \(\mathbb P(T_+)\to1\) when \(p>q\), while \(\mathbb P(T_+)\to0\) when \(p<q\). More precisely, if both converge to the same \(p\in(1/2,1]\) and \(\sqrt m(p_m-q_n)\to\delta\in\mathbb R\), then
\[
\boxed{\mathbb P(T_+)\longrightarrow\Phi\!\left(\frac{\delta}{\sqrt{p(2p-1)(1+1/\kappa)}}\right),}
\]
where \(\Phi\) is the standard normal distribution function.

This phase decision need not agree with the global initial spin majority. For \(K_{31,101}\), with \(25\) first-part positive spins and \(61\) second-part negative spins, there are only \(65\) initial positive spins among \(132\) vertices, yet the exact formula yields \(\mathbb P(T_+)\approx0.978685744676395\). More strongly, choose asymptotic sizes in ratio \(n/m\to4\) with \(p_m\to0.8\) and \(q_n\to0.6\). The initial global majority is negative, but positive consensus has probability tending to one.

## Assumptions and scope
A spin \(\sigma_w\in\{-1,+1\}\) occupies every vertex. The ferromagnetic energy is \(H=-J\sum_{\{i,j\}\in E}\sigma_i\sigma_j\) with \(J>0\). At each update a spin is set equal to the sign of the sum of its neighbors, a deterministic zero-temperature energy-minimizing heat-bath rule; update clocks are independent exponential rate-one processes. Since both part sizes are odd, the local field can never be zero, so no tie-breaking convention is needed. Initial configurations are deterministic subject only to the two stated counts; permutations within parts do not change any probability. The dynamics is run until one unanimous spin configuration is reached. All probability assertions concern this exact process, not a noisy voter model or positive-temperature dynamics.

## Proof
**1. Coupling to a race.** Until one of the part majorities reverses, each positive vertex in the first part sees a strictly negative local field and flips to negative at its first rate-one update, while each negative vertex in the second part sees a strictly positive local field and flips to positive at its first update. The other vertices already agree with the opposite-part local field and retain their spin when updated. Therefore the initially \(a\) positive first-part spins and the initially \(b\) negative second-part spins have independent unit-rate exponential lifetimes throughout this phase. Let \(\tau_A\) be the time when the first-part positive count first reaches \(u\); let \(\tau_B\) be the time when the second-part negative count first reaches \(v\). These two times are independent and finite almost surely.

If \(\tau_B<\tau_A\), then the second part has acquired a strict positive majority while the first still has a strict positive majority, so from that instant the only possible future spin changes are negative to positive, and unanimous positive spin is reached almost surely. Conversely, if \(\tau_A<\tau_B\), both parts have strict negative majorities and the system converges almost surely to unanimous negative spin. Independent continuous clocks make exact equality probability zero. Hence \(\mathbb P(T_+)=\mathbb P(\tau_B<\tau_A)\).

**2. Beta representation and finite formula.** Conditional on time \(t\), each original first-part positive spin survives without updating with probability \(e^{-t}\). Thus the threshold \(\tau_A\) has the same distribution as the arrival time at which an independent sample of \(a\) unit exponentials has exactly \(u\) survivors. Under the monotone map \(x=e^{-t}\), \(X=e^{-\tau_A}\) is the \((u+1)\)-st largest of \(a\) independent uniform \((0,1)\) variables; it has law \(\mathrm{Beta}(u+1,a-u)\). Likewise \(Y=e^{-\tau_B}\sim\mathrm{Beta}(v+1,b-v)\), independently. Since earlier time corresponds to larger \(e^{-t}\), \(\mathbb P(T_+)=\mathbb P(Y>X)\).

Conditioning on \(Y=y\), the event \(X<y\) means that at least \(u+1\) of the \(a\) underlying uniforms lie below \(y\). Consequently
\[
\mathbb P(X<y)=\sum_{j=u+1}^{a}\binom aj y^j(1-y)^{a-j}.
\]
Integrate this polynomial against the \(\mathrm{Beta}(v+1,b-v)\) density to obtain the claimed finite beta-function sum. All beta arguments are positive integers.

**3. Equal fully opposed polarization.** If \(a=m=2u+1\), then \(X\sim\mathrm{Beta}(u+1,u+1)\) is symmetric about \(1/2\); similarly \(Y\sim\mathrm{Beta}(v+1,v+1)\). The independent difference \(Y-X\) is symmetric in distribution, since \((X,Y)\) and \((1-X,1-Y)\) have identical laws. It has a continuous density, hence \(\mathbb P(Y>X)=1/2\), regardless of unequal part sizes.

**4. Law of large numbers and Gaussian critical window.** For first-part survivor number \(A_t\sim\mathrm{Binomial}(a,e^{-t})\), the majority threshold is reached where its deterministic mean equals \(m/2\). As \(p_m=a/m\to p>1/2\), this occurs at \(t=\log(2p_m)+O(m^{-1})\). Standard binomial central-limit convergence, or the quantile delta method applied to the beta order statistic, gives
\[
\sqrt m\bigl(\tau_A-\log(2p_m)\bigr)\Rightarrow N\!\left(0,\frac{2p-1}{p}\right).
\]
The same argument gives \(\sqrt n(\tau_B-\log(2q_n))\Rightarrow N(0,(2q-1)/q)\), independently. This follows directly by linearizing the mean survivor count \(a e^{-t}\) at its threshold: the binomial variance is asymptotic to \(m(2p-1)/(4p)\), and the magnitude of the mean time derivative is \(m/2\). Both statements remain valid at the endpoint \(p=1\).

When \(p\ne q\), the threshold times converge in probability to their distinct constants \(\log(2p)\) and \(\log(2q)\), proving the step transition. When \(p=q\) and \(\sqrt m(p_m-q_n)\to\delta\), the deterministic time difference satisfies
\[
\sqrt m\bigl[\log(2p_m)-\log(2q_n)\bigr]\to\delta/p.
\]
The independent centered fluctuations of \(\sqrt m(\tau_A-\tau_B)\) converge to a normal law of variance \((2p-1)(1+1/\kappa)/p\). Since positive consensus is equivalent to \(\tau_A>\tau_B\), the displayed \(\Phi\)-profile follows.

**5. Global-majority reversal.** In the numerical witness, initial positive count equals \(25+(101-61)=65\) against \(67\) negatives, while exact-rational evaluation of the proved beta sum gives the quoted probability. In the asymptotic example, the limiting proportion of global positive spins is \((0.8+4(1-0.6))/5=0.48<1/2\), whereas \(p=0.8>q=0.6\), so positive consensus probability tends to one.

## Verification
The accompanying self-contained program `verify.py` independently evaluates the beta-function sum in exact rational arithmetic and the finite pure-death two-population first-step recursion. It compares all \(196\) admissible initial-majority pairs on \(K_{m,n}\) with \(m,n\in\{3,5,7,9\}\), checks equal-full-polarization symmetry, evaluates the global-minority reversal witness, and numerically compares finite-size probabilities against the limiting Gaussian crossover. Run `python3 verify.py` with Python 3.10 or later. Finite checks support the proof but do not replace its all-sizes argument.

## Relationship to prior work
Spirin, Krapivsky and Redner (2001) study zero-temperature Ising freezing and coarsening on Euclidean lattices and discuss a fully connected comparison. That work is not an evaluated exact consensus race for two opposing bipartite parts. Castellano and Pastor-Satorras (2006) study zero-temperature Glauber evolution on complex networks and degree-distribution effects, rather than finite exact bipartite absorbing probabilities. Kim (2021) studies complete multipartite Ising Glauber mixing at high temperature, where the Markov chain is not absorbing in the present zero-temperature sense. Krapivsky and Redner (2021) investigate majority-rule dynamics with homophilous group updates, a different update mechanism. The same bipartite graph may occur in other models, but finite beta threshold competition and its critical polarization window are not implied by those inspected statements. No exhaustive priority claim is made.

## Limitations
Both part sizes must be odd and at least three, and the initial part majorities must be strictly opposite. The dynamics uses exactly zero temperature, symmetric positive couplings, and independent unit-rate single-spin updates; no arbitrary-temperature, tied-field, multi-community, or arbitrary-edge-weight statement is asserted. The theorem determines terminal sign probabilities but not the complete post-threshold absorption-time distribution. A specialized unlocated result could cover the particular beta race; independent literature review remains appropriate.

## References
1. V. Spirin, P. L. Krapivsky, S. Redner, *Freezing in Ising Ferromagnets*, arXiv:cond-mat/0105037 (initial public submission 2001-05-02).
2. C. Castellano, R. Pastor-Satorras, *Zero temperature Glauber dynamics on complex networks*, arXiv:cond-mat/0602315 (2006).
3. H. Kim, *Cutoff phenomenon for the Glauber dynamics on complete multipartite graphs in the high temperature regime*, arXiv:2102.05279 (2021).
4. P. L. Krapivsky, S. Redner, *Divergence and Consensus in Majority Rule*, arXiv:2103.04248 (2021).
