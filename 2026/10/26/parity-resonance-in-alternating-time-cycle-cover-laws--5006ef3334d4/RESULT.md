# Parity resonance in alternating-time cycle cover laws

## Finding
Let \(X_0=0\) be a nearest-neighbor walk on the labeled cycle \(C_n\). At even step times it moves clockwise with probability \(p\in(0,1)\), and at odd step times clockwise with probability \(q=1-p\), with independent choices. Let \(L\) be the unique noninitial vertex discovered last. For every odd \(n=2m+1\ge3\), the law is exactly
\[
\Pr(L=k)=\begin{cases}q/m,&k\text{ odd},\\p/m,&k\text{ even},\end{cases}\quad(1\le k\le2m).
\]
Thus \(\Pr(L\text{ odd})=q\), and the conditional location is uniform within either label-parity class. With \(U\) uniform on the \(n-1\) noninitial vertices,
\[
\|\mathcal L(L)-U\|_{\rm TV}=|p-1/2|,
\]
independently of odd cycle length. This quantifies a persistent last-discovery parity bias despite the exactly zero average directional drift per two steps.

For comparison, on every even \(n=2m\ge4\) the law admits the explicit affine formula in the proof, and along even orders
\[
\lim_{m\to\infty}\|\mathcal L(L)-U\|_{\rm TV}=|p-1/2|/2.
\]
The even-order formula is included to establish the sharp order-parity contrast; it is also obtainable as a specialization of pre-existing stationary weighted-cycle hitting formulas. No independent novelty is claimed for that specialization.

## Assumptions and scope
The integers satisfy \(n\ge3\); clockwise is increasing label modulo \(n\); \(X_0=0\); \(0<p<1\), \(q=1-p\); clockwise increments at absolute time \(t\) have probability \(p\) for even \(t\) and \(q\) for odd \(t\), independent across steps. The cover time is almost surely finite because an uninterrupted run of \(n\) clockwise steps has probability at least \(\min(p,q)^n>0\) in each nonoverlapping block of \(n\) steps. The last newly discovered vertex \(L\) is therefore defined almost surely and never equals \(0\). The uniform comparator places mass \(1/(n-1)\) on each \(1\le k\le n-1\).

## Proof
Fix a candidate \(k\in\{1,\ldots,n-1\}\). Delete \(k\), and label the remaining path clockwise from \(k+1\) as \(x=1,\ldots,n-1\), with absorbing copies of \(k\) at \(x=0,n\). The start is \(s=n-k\). Until absorption the parity relation \(x-s\equiv t\pmod2\) holds, because every step changes position parity on the unwrapped path. Consequently the probability of stepping to the right from \(x\) is \(c_x=p\) when \(x\equiv s\pmod2\), otherwise \(c_x=q\), and the probability of stepping left is \(c_{x-1}\). Set the positive edge resistances \(r_i=1/c_i\), \(0\le i\le n-1\). These time-inhomogeneous transition probabilities become a static reversible, conductance-weighted *path up to this candidate's absorption*, regardless of whether the original cycle admits a globally consistent static representation.

A vertex \(k\) is last discovered exactly when both neighbors of \(k\), corresponding to path positions \(1,n-1\), have been visited before either absorbing copy is hit. Write \(R_{a:b}=\sum_{i=a}^b r_i\). Standard one-dimensional harmonicity with constant edge current shows that the probability of hitting \(1\) before \(n-1\) from \(s\) is \(u=R_{s:n-2}/R_{1:n-2}\). Starting from \(1\), the probability of reaching \(n-1\) before \(0\) is \(r_0/R_{0:n-2}\); starting from \(n-1\), the probability of reaching \(1\) before \(n\) is \(r_{n-1}/R_{1:n-1}\). The strong Markov property thus gives the exact general identity
\[
\Pr(L=k)=u\,\frac{r_0}{R_{0:n-2}}+(1-u)\,\frac{r_{n-1}}{R_{1:n-1}}.\tag{1}
\]
This resistance identity is a standard hitting-probability argument; the claimed new content is its temporal parity specialization and asymptotic consequence.

If \(n=2m+1\), then \(n-1\) is even and \(r_0=r_{n-1}\). Each denominator in (1) contains exactly \(m\) occurrences each of \(1/p\) and \(1/q\), so the two conditional contributions coincide, canceling \(u\). Therefore \(\Pr(L=k)=r_0/[m(1/p+1/q)]\). When \(k\) is odd, \(s=n-k\) is even and \(r_0=1/p\), yielding \(q/m\); when \(k\) is even, \(r_0=1/q\), yielding \(p/m\). Each parity class has \(m\) noninitial sites. Summing deviations from \(1/(2m)\) yields the stated exact total-variation formula.

For \(n=2m\), define \(a=p/(m-q)\) and \(b=q/(m-p)\). Directly counting the alternating resistances in (1) gives, for \(1\le k\le2m-1\),
\[
\Pr(L=k)=w_k a+(1-w_k)b,\qquad
w_k=\begin{cases}
(k-1)/(2m-2),&k\text{ odd},\\
(2m-k-2q)/(2m-2),&k\text{ even}.
\end{cases}\tag{2}
\]
For clarity, (2) is the explicit even-order comparison, not a claim of a new general stationary conductance formula. With \(z=k/(2m)\), the expansions \(a=p/m+O(m^{-2})\), \(b=q/m+O(m^{-2})\), and \(w_k=z+O(m^{-1})\) on odd labels, \(w_k=1-z+O(m^{-1})\) on even labels, hold uniformly over all such \(k\). As \(1/(2m-1)=1/(2m)+O(m^{-2})\), the signed error relative to uniform is \((p-q)(z-1/2)/m+O(m^{-2})\) for odd labels and its negative for even labels. The sum of absolute errors is a two-parity Riemann sum, hence total variation converges to
\[
\frac{|p-q|}{2}\,2\int_0^1|z-1/2|\,dz=\frac{|p-q|}{4}=|p-1/2|/2.
\]
All error terms are uniform, so the Riemann-sum limit is justified without exchanging an uncontrolled infinite series.

## Verification
A standalone Python 3 checker, `verify.py`, independently constructs the finite-state absorbing Markov chain tracking current position, absolute-time parity and which of the two neighbors of a candidate have been reached. It uses exact rational Gaussian elimination, independent of the resistance proof. Running `python3 verify.py` yields: `PASS 60 independent exact-rational absorbing-chain comparisons; 690 states solved; odd-cycle total-variation identities PASS`. The comparisons cover all \(n=3,4,5,6,7\), \(p\in\{1/3,2/5,3/4\}\), and every noninitial target. Additional exact identities check odd-cycle total variation through \(n=29\); even-order numerical-rational convergence checks extend to \(n=320\). Finite checking is corroborative, not the proof of the statements for arbitrary \(n\).

## Relationship to prior work
Idnani and Salem (2026, arXiv:2610.15115v1) derive general time-dependent last-coverage formulas as an infinite series and analyze selected varying biases. Their displayed results and text do not give the alternating complementary-phase finite closed form, its exact odd-order total-variation invariant, or the odd/even asymptotic discrepancy. Buchanan, Horn and Rombach (2022/2023, arXiv:2209.08079) address the last-new-vertex question on static finite graphs. Panny and Prodinger (2015/2016) study two-periodic walks and extremal ranges rather than this cycle last-coverage law. Mosbah and Saheb (2000) treat stationary weighted cycles; their framework, and an earlier exact weighted-cycle last-coverage calculation, cover the even-order static interpretation and the standard resistance mechanism, not the genuinely time-dependent odd-cycle parity resonance. The full text of Mosbah and Saheb was not available for direct comparison, leaving an explicit residual priority risk. A closed form derivable by a specialized substitution in general earlier formulas is possible and would reduce the claim's originality; no uniqueness or independence certification is asserted.

## Limitations
The theorem covers only nearest-neighbor cycles with exactly complementary alternating step probabilities and a fixed labeled start. It does not cover arbitrary time-periodic forcing, laziness, multiple starting sites, random environments, or cover-time expectations. The discovery-order law is asymmetric in label parity, not in the long-run one-time marginal, and the contrast is not a claim about stochastic drift or mixing. Comparison to inaccessible earlier weighted-cycle full text is incomplete. Independent scientific audit has not been performed.

## References
1. K. Idnani and J. Salem, *Last-Coverage Probabilities of Random Walks on Cycle Graphs for Symmetric, Biased, and Time-Dependent Walks*, arXiv:2610.15115v1 (first public October 10, 2026).
2. A. Buchanan, P. Horn and P. Rombach, *The last new vertex visited by a random walk in a directed graph*, arXiv:2209.08079 (2022 preprint; 2023 journal version).
3. C. Panny and H. Prodinger, *A combinatorial study of two-periodic random walks*, 2015/2016.
4. M. Mosbah and N. Saheb, *Formal rational fractions and random walks on cycles*, Discrete Mathematics (2000), DOI 10.1016/S0012-365X(99)00269-1.
