# Universal cooperative metastability entropy and fluctuations in random ferromagnetic chains

## Finding
Consider an open ferromagnetic Ising chain on \(N\ge3\) sites, with energy
\[H(\sigma)=-\sum_{j=1}^{N-1}J_j\sigma_j\sigma_{j+1},\qquad J_j>0,\quad\sigma_j\in\{-1,+1\}.\]
Assume the couplings are pairwise distinct. For \(r\ge1\), call a configuration \(r\)-stable when flipping **any** set of at most \(r\) spins cannot lower the energy. Let \(B_{N,r}\) be the number of such configurations.

Define the radius-\(r\) record-minimum set of bonds
\[\mathcal V_{N,r}=\left\{j\in\{1,\ldots,N-1\}:r<j<N-r,\ J_j<J_k\text{ for every }k\ne j\text{ with }1\le k\le N-1\text{ and }|k-j|\le r\right\}.\]
Write \(M_{N,r}=|\mathcal V_{N,r}|\). The following exact deterministic identity holds **for every pairwise-distinct positive coupling vector** and every \(r\ge1\):
\[\boxed{B_{N,r}=2^{M_{N,r}+1}.}\]
More precisely, the domain walls of an \(r\)-stable spin configuration form an arbitrary subset of \(\mathcal V_{N,r}\); for each subset there are exactly two globally opposite spin configurations.

If the couplings are independent and identically distributed with any atomless probability law supported on \((0,\infty)\), then for each fixed \(r\ge1\), almost surely
\[\boxed{\lim_{N\to\infty}\frac{\log B_{N,r}}{N}=\frac{\log2}{2r+1}.}\]
The fluctuations obey
\[\boxed{\frac{\log B_{N,r}-\frac{N\log2}{2r+1}}{\sqrt N}\ \Longrightarrow\ \mathcal N\!\left(0,(\log2)^2v_r\right),}\]
where the positive, exactly evaluated variance density is
\[\boxed{v_r=\frac4{2r+1}\sum_{d=r+1}^{2r}\frac1{2r+1+d}-\frac{2r}{(2r+1)^2}>0.}\]
For example, \(v_1=2/45\) and \(v_2=13/450\). In particular, any fixed positive cooperative budget leaves extensive metastable-state entropy, decreasing exactly as \((2r+1)^{-1}\), with universal Gaussian sample-to-sample fluctuations.

There is also an exact macroscopic-budget regime. If \(N\le3r+2\), write \(K=\max\{N-2r-1,0\}\). If \(K>0\) the random variable \(M_{N,r}\) is Bernoulli with parameter \(K/(2r+1)\); if \(K=0\), it vanishes identically. In particular, for \(r/N\to\alpha\in(1/3,1/2)\), \(B_{N,r}\) converges in distribution to \(4\) with probability \((1-2\alpha)/(2\alpha)\), and to \(2\) otherwise. This explicitly separates finite cooperative budgets from budgets proportional to chain length.

## Assumptions and scope
All spin flips are **simultaneous** flips of arbitrary subsets, not only connected blocks. Energy-neutral moves are allowed; the definition excludes strictly energy-decreasing moves. The deterministic classification assumes all \(J_j\) strictly positive and pairwise distinct, and includes cases where \(r\ge N\). The probabilistic statements assume iid atomless positive bond laws, with a fixed integer \(r\) for the entropy and central-limit assertions. The Bernoulli statement applies to arbitrary integer \(N,r\) in its indicated range. No time-evolution or quench distribution is assumed.

## Proof
Put \(\tau_j=\sigma_j\sigma_{j+1}\), so a domain wall is a bond with \(\tau_j=-1\). Flipping a contiguous spin interval changes only its boundary-bond terms. If the interval lies strictly inside the chain and its two boundary bonds are \(i<j\), with \(j-i\) spins flipped, the energy change is
\[\Delta H=2(J_i\tau_i+J_j\tau_j).\]
If the interval touches an endpoint, it has one boundary bond \(j\), with \(\Delta H=2J_j\tau_j\). Flipping an arbitrary set decomposes into disjoint maximal contiguous spin intervals, and the resulting energy changes add exactly, because their changed boundary-bond sets are disjoint. Thus stability for *every* flip of at most \(r\) sites is equivalent to stability under every contiguous interval flip of length at most \(r\).

Suppose \(\tau_j=-1\) in an \(r\)-stable configuration. A prefix or suffix interval reaching bond \(j\) would decrease energy if its length were at most \(r\). Hence \(r<j<N-r\). For any other bond \(k\) with \(|k-j|\le r\), flip the intervening spin interval of length \(|k-j|\). If \(\tau_k=-1\), the energy change is \(-2(J_j+J_k)<0\), a contradiction. Thus \(\tau_k=+1\), and \(\Delta H=2(J_k-J_j)\ge0\); by distinctness, \(J_k>J_j\). Therefore every wall belongs to \(\mathcal V_{N,r}\).

Conversely, distinct bonds in \(\mathcal V_{N,r}\) are more than \(r\) apart: otherwise each would have smaller coupling than the other. Select any subset of this set as domain walls. A block of at most \(r\) spins touching an endpoint meets no domain wall at its boundary. An interior block of such length has either no boundary wall, giving positive energy change, or exactly one, say \(j\), giving \(2(J_k-J_j)>0\) by the radius-\(r\) record condition. It cannot have two boundary walls. Consequently all allowed flips are non-decreasing. Each wall subset determines two globally reversed spin assignments, proving the exact classification and \(B_{N,r}=2^{M_{N,r}+1}\).

For iid atomless couplings, each eligible \(j\in\{r+1,\ldots,N-r-1\}\) is the unique minimum of \(2r+1\) exchangeable variables with probability \(p=1/(2r+1)\). Therefore
\[\mathbb E M_{N,r}=\frac{(N-2r-1)_+}{2r+1},\]
where \((x)_+=\max\{x,0\}\). Extend the iid sequence to the integer line and denote by \(I_j\) the indicator of a radius-\(r\) local minimum. The stationary sequence \((I_j)\) is \(2r\)-dependent and bounded, so the ergodic theorem yields \(N^{-1}M_{N,r}\to p\) almost surely.

For the fluctuation constant put \(m=2r+1\). Two centers at separation \(1\le d\le r\) cannot both be minima. Centers at distance \(d>2r\) use disjoint windows and are independent. If \(r<d\le2r\), condition on the two independent center values \(x,y\), taken as independent uniform \((0,1)\) after a probability-integral transform. For \(x\le y\), the \(d-1\) neighbors exclusively in the first window must exceed \(x\), while all \(m-1\) neighbors in the second window (including the overlap) must exceed \(y\). Integrating both orderings gives
\[\mathbb P(I_0=I_d=1)=\frac2d\int_0^1(1-y)^{m-1}\bigl(1-(1-y)^d\bigr)\,dy=\frac2{m(m+d)}.\]
Hence the stationary asymptotic variance per bond is
\[\begin{aligned}v_r&=p(1-p)+2\sum_{d=1}^{2r}(\mathbb E I_0I_d-p^2)\\&=-\frac{2r}{m^2}+\frac4m\sum_{d=r+1}^{2r}\frac1{m+d}.\end{aligned}\]
It is strictly positive because the sum exceeds \(r/(4r+1)\), giving \(v_r>2r/[m^2(4r+1)]>0\). The standard central-limit theorem for bounded stationary finitely dependent sequences applies to the centered sum; removing the fixed number of end terms does not change the limit. Multiplying by \(\log2\) proves the stated normal limit for \(\log B_{N,r}\).

Finally, for \(N\le3r+2\), the eligible interval contains \(K=(N-2r-1)_+\) bond positions, with any two positions at distance at most \(r\). Thus at most one position can be a radius-\(r\) minimum. The expectation formula makes its indicator Bernoulli with parameter \(K/m\). Under \(r/N\to\alpha\in(1/3,1/2)\) this tends to the stated mixture, completing the proof.

## Verification
The standalone file `verify.py` recomputes the original Hamiltonian for all spin configurations and all flip sets of size at most \(r\) for chain lengths \(3\le N\le10\), for deterministic independent randomized permutations of distinct positive couplings and \(1\le r\le\min\{4,N\}\). It checks the exact wall classification and full counts. It also enumerates all rank orders of overlapping windows for representative \(r\in\{1,2\}\) and verifies the derived joint probabilities. It is executable with Python's standard library using `python verify.py`. These finite tests are not substitutes for the unrestricted proof.

## Relationship to prior work
Masui, Southern and Jacobs (1989) investigated counts and energy/magnetization profiles of **single-spin-flip** metastable states for disordered Ising chains and strips. Lefevre and Dean (2000) derived annealed metastable counts for random thin graphs, with a one-spin-flip definition. Waclaw and Burda (2008) developed methods for counting single-spin-stable states with Gaussian couplings. These works establish the statistical-physics importance of metastable-state complexity. The present statement concerns stability against **all arbitrary simultaneous flips of up to \(r\) spins** in an iid *positive-bond* chain, an exact radius-minimum classification, and universal quenched entropy, variance and macroscopic-budget crossover. It does not claim novelty of ordinary local-minimum order statistics or of general finite-dependence central-limit theorems.

## Limitations
No annealed exponential-growth rate, large-deviation principle, relaxation dynamics, barrier-height distribution, or CLT with \(r\to\infty\) is asserted. The iid atomless assumption is needed for the exact universal probabilities and excludes tied couplings; correlated, non-identically distributed, or sign-changing couplings need separate analysis. Secondary literature might contain the same cooperative-stability reduction under different terminology; originality is assessed against the specifically inspected sources, not independently certified.

## References
- S. Masui, B. W. Southern and A. E. Jacobs, “Metastable states of Ising spin glasses and random ferromagnets,” *Physical Review B* **39**, 6925 (1989), DOI 10.1103/PhysRevB.39.6925.
- A. Lefevre and D. S. Dean, “Metastable states of a ferromagnet on random thin graphs,” *European Physical Journal B* **21**, 121–128 (2001), arXiv:cond-mat/0011265 (initial preprint 15 November 2000).
- B. Waclaw and Z. Burda, “Counting metastable states of Ising spin glasses on arbitrary graphs,” *Physical Review E* **77**, 041114 (2008), arXiv:0801.1224 (initial preprint 8 January 2008).
