# A unique epidemic-duration crossover when a contact path is closed into a cycle

## Finding
For every integer \(n\ge3\), begin with the path on vertices \(0,1,\ldots,n-1\), with the single initial infection at the endpoint \(0\). At every integer generation, each newly infected individual independently infects each still-susceptible neighbor with probability \(p\in(0,1)\), then permanently recovers. Add the one missing contact \(\{0,n-1\}\), making a cycle. Let \(T_P\) and \(T_C\) be the last generations at which a new infection occurs (initial infection at generation zero; hence \(T=0\) if no secondary infections occur). Then
\[
\boxed{\mathbb E T_C-\mathbb E T_P=p\left(\sum_{j=0}^{\lfloor n/2\rfloor-1}p^{2j}-(n-1)p^{n-1}\right).}
\]
There is a **unique** \(p_n\in(0,1)\) at which the difference vanishes: the added contact increases expected epidemic duration for \(0<p<p_n\), and decreases it for \(p_n<p<1\). Nevertheless, the same added contact strictly increases expected total infections throughout \(0<p<1\):
\[
\boxed{\mathbb E Z_C-\mathbb E Z_P=\sum_{j=1}^{n-1}p^j-(n-1)p^n>0.}
\]
The crossover has the exact large-population scale
\[
\boxed{\lim_{n\to\infty}n(1-p_n)=\gamma=1.2564312086261696\ldots,\qquad e^\gamma=1+2\gamma,\quad\gamma>0.}
\]
The positive equation has exactly one solution \(\gamma>0\).

## Assumptions and scope
The contact networks are the simple path \(P_n\) and the simple cycle \(C_n\), on the *same labeled vertices*; the sole difference is adding \(\{0,n-1\}\). The source \(0\) is fixed, not random. Contacts are independent with common transmission probability \(p\), each infectious period lasts exactly one generation, and recovered persons are never reinfected. A newly infected person makes independent transmission attempts only to neighbors not previously infected. The quantity \(T\) excludes the initial infection generation; including the initial infectious generation adds one to both durations and leaves every comparison unchanged. \(Z\) counts all distinct individuals ever infected, including the source. The theorem covers every integer \(n\ge3\) and every real \(0<p<1\), with exact endpoint identities at \(p=0,1\) obtained by continuity.

## Proof
**Percolation coupling.** Give each undirected contact edge an independent Bernoulli-\(p\) open indicator. The epidemic infects a vertex precisely when it lies in the root's open-edge component, and its first infection generation is the shortest open-path distance from the root. This follows inductively from one-generation infectiousness and independent edge attempts: an edge can first be relevant only when exactly one endpoint is infected; marking its success in advance preserves its law. Thus \(T\) is the largest finite open-path distance from \(0\), and \(Z\) is the size of that component.

**The path.** On \(P_n\), the event \(T_P\ge t\) means that the first \(t\) consecutive contacts from \(0\) are open. Therefore
\[
\Pr(T_P\ge t)=p^t\quad(1\le t\le n-1),\qquad
\mathbb E T_P=\sum_{t=1}^{n-1}p^t.
\]

**The cycle.** Fix \(1\le t\le n-1\). If \(t\le\lfloor n/2\rfloor\), then \(T_C\ge t\) exactly when at least one of the two opposite \(t\)-edge arms from the root is open. The arms are edge-disjoint, giving
\[
\Pr(T_C\ge t)=2p^t-p^{2t}.
\]
If \(t>\lfloor n/2\rfloor\), then a path of length \(t\) from the root reaches a vertex at distance \(t\) precisely if that arm is open *and the whole cycle is not open*: the alternative, shorter root-to-vertex route would require every remaining edge. Both long-arm events are disjoint once the all-open outcome is excluded. Hence
\[
\Pr(T_C\ge t)=2(p^t-p^n).
\]
Summing these tail probabilities, subtracting the path expectation, and collecting odd powers yields
\[
\mathbb E T_C-\mathbb E T_P
=\sum_{j=0}^{\lfloor n/2\rfloor-1}p^{2j+1}-(n-1)p^n,
\]
which is the claimed polynomial identity.

**Exactly one crossover.** Divide the parenthesized expression by \(p^{n-1}\). This gives
\[
H_n(p)=\sum_{j=0}^{\lfloor n/2\rfloor-1}p^{2j-(n-1)}-(n-1).
\]
All exponents in the sum are strictly negative, so \(H_n\) is continuous and strictly decreasing on \((0,1]\). It tends to \(+\infty\) at zero, whereas \(H_n(1)=\lfloor n/2\rfloor-(n-1)<0\). The intermediate value theorem yields a unique \(p_n\in(0,1)\) and the asserted strict signs.

**Mean outbreak size.** For the path vertex at index \(j\), infection probability is \(p^j\). In the cycle there are two edge-disjoint routes from \(0\) to \(j\), of lengths \(j\) and \(n-j\). Its infection probability is \(p^j+p^{n-j}-p^n\). Summation over \(j=1,\ldots,n-1\) gives the stated difference. It is strictly positive since every one of the \(n-1\) terms \(p^j\), \(j<n\), exceeds \(p^n\).

**Crossover scaling.** Define \(p=e^{-z/n}\), with any fixed \(z>0\). Divide the defining crossover equation by \(n\). The two sides converge as \(n\to\infty\) to
\[
\int_0^{1/2}e^{-2zx}\,dx=\frac{1-e^{-z}}{2z}
\quad\text{and}\quad e^{-z},
\]
respectively. Their difference has the sign of \(e^z-1-2z\) for \(z>0\). The latter strictly convex function starts at zero with derivative \(-1\), reaches a negative minimum, then increases to infinity, so it has exactly one strictly positive root \(\gamma\). For every \(0<\varepsilon<\gamma\), the limiting signs at \(z=\gamma\pm\varepsilon\) are opposite, and the convergence at these two fixed points brackets the unique root \(p_n\). Thus \(-n\log p_n\to\gamma\) and \(n(1-p_n)\to\gamma\), using \(1-e^{-u}\sim u\) as \(u\downarrow0\).

## Verification
The accompanying standalone `verify_outbreak_duration.py` independently enumerates all \(2^{n-1}\) path and \(2^n\) cycle open-edge configurations for each \(3\le n\le10\). It computes shortest-path infection generations, expected epidemic duration, and final outbreak size, groups outcomes by their number of open edges, and checks the exact symbolic polynomial identities against both the theorem and a separate tail-sum derivation. It reports 32 independently constructed exact identities passing. This is a finite corroboration, not the all-\(n\) proof.

At \(n=5\), the duration difference equals \(1/2\) at \(p=1/2\) but \(-4581/6250\) at \(p=9/10\); the mean outbreak-size increases at both probabilities, by \(13/16\) and \(36657/50000\), respectively. Arbitrary-precision computations also illustrate convergence of \(n(1-p_n)\) to \(\gamma\); the limit itself was proved above.

## Relationship to prior work
The Reed–Frost/contact-network paradigm and its bond-percolation interpretation are standard. Sharkey, Kiss, Wilkinson, and Simon study exact time-dependent SIR equations on tree graphs, with continuous-time Markovian transmission and recovery, rather than the discrete one-generation root-specific path-to-cycle duration comparison. Lashari, Serafimović, and Trapman analyze large-graph SIR epidemic durations on configuration models, not this finite-network intervention law. Shivam, Bulchandani, and Sondhi treat network Reed–Frost models with recursive contact tracing and finite-size scaling, not the exact cycle-closure law. Alarcón González and Pérez provide a finite Markov-chain computation of expected epidemic duration for a population without fixed contact topology and identify extension to contact structure as future work. None of the inspected mathematical statements implies the present exact single-crossover polynomial, contrast with strictly increasing final outbreak size, or the constant \(\gamma\). An independently established equivalent formula under another network-percolation or graph-eccentricity name remains a bibliographic possibility.

## Limitations
This is a theorem about a deliberately minimal, homogeneous, synchronous SIR model, with a fixed endpoint seed and exactly one particular new contact. It does not claim that an arbitrary new edge shortens duration, or that duration changes stochastically in the same way as its mean. It does not model transmission times longer than one generation, changing contacts, heterogeneous contacts, or empirical epidemic interventions. The novelty assessment is literature-based rather than a claim of exhaustive worldwide bibliographic uniqueness; a closely equivalent elementary cycle-percolation identity could have appeared elsewhere.

## References
1. K. J. Sharkey, I. Z. Kiss, R. R. Wilkinson, P. L. Simon, *Exact equations for SIR epidemics on tree graphs*, first public preprint 2012-12-10, arXiv:1212.2172; journal DOI:10.1007/s11538-013-9923-5. https://arxiv.org/abs/1212.2172
2. A. A. Lashari, A. Serafimović, P. Trapman, *The duration of a supercritical SIR epidemic on a configuration model*, first posted 2018-05-14, arXiv:1805.05117. https://arxiv.org/abs/1805.05117
3. S. Shivam, V. B. Bulchandani, S. L. Sondhi, *Recursive contact tracing in Reed-Frost epidemic models*, arXiv:2103.06427. https://arxiv.org/abs/2103.06427
4. A. Alarcón González, G. A. Pérez, *Computation of Expected Epidemic Duration*, public preprint posted 2023-04-25, DOI:10.1101/2023.04.24.23289026. https://www.medrxiv.org/content/10.1101/2023.04.24.23289026v2.full
