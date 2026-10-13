# Exact first-arrival frontier and the \(e/4\) interference crossover for the Grover walk on the hypercube
## Finding
Fix \(n\ge 2\). Consider the standard discrete-time Grover-coined quantum walk on the Boolean hypercube \(Q_n\). The walk starts at \(0^n\) with the uniform coin state, and one step is Grover diffusion followed by the coordinate shift. For any vertex \(x\) with Hamming weight \(w\in\{1,\ldots,n}\), the first time at which \(x\) can be reached is \(t=w\), and its point probability at that time is
\[
P_{\rm q}(x,w)=\frac{w!(w-1)!4^{w-1}}{n^{2w-1}}.
\]
For the simple classical walk on the same hypercube, choosing one coordinate uniformly at every step,
\[
P_{\rm cl}(x,w)=\frac{w!}{n^w},
\qquad
\frac{P_{\rm q}(x,w)}{P_{\rm cl}(x,w)}=\frac{4^{w-1}(w-1)!}{n^{w-1}}.
\]
If \(w_n/n\to\rho\in(0,1]\), then
\[
\lim_{n\to\infty}\frac1n\log\frac{P_{\rm q}(x,w_n)}{P_{\rm cl}(x,w_n)}
=\rho\log\!\left(\frac{4\rho}e\right).
\]
Hence the quantum first-arrival point mass is exponentially smaller than the classical one for \(0<\rho<e/4\), and exponentially larger for \(e/4<\rho\le1\). The normalized Hamming radius \(e/4\) is therefore the exact exponential crossover on the ballistic frontier.

At the antipode \(w=n\),
\[
P_{\rm q}(1^n,n)=\left(\frac{2^{n-1}(n-1)!}{n^{n-1}}\right)^2
=\frac{\pi n}2\left(\frac4{e^2}\right)^n\left(1+\frac1{6n}+O(n^{-2})\right).
\]
This gives a concrete lower bound on the maximum vertex probability at the first time the antipode becomes reachable.

## Assumptions and scope
The quantum walk is exactly the walk defined in arXiv:2201.11735: the coin space has directions \(i\in\{1,\ldots,n}\), the Grover coin has diagonal entry \(-(n-2)/n\) and off-diagonal entry \(2/n\), the shift flips the coordinate named by the coin, and the initial coin state is uniform. The classical comparison is the ordinary simple random walk that chooses each coordinate with probability \(1/n\) independently at every step; it is not the direction-memory chain produced by measuring the quantum coin after each step.

The exact formula concerns only the earliest reachable time \(t=w\). It makes no claim about later-time probabilities, mixing, hitting-time optimality, or measurement-modified walks.

## Proof
The graph distance from \(0^n\) to a vertex of Hamming weight \(w\) is \(w\), so \(t=w\) is the earliest possible arrival time. A length-\(w\) path from \(0^n\) to such an \(x\) must flip each of the \(w\) coordinates in the support of \(x\) exactly once and no other coordinate. Thus the contributing direction words are precisely the \(w!\) permutations of those coordinates.

The uniform initial coin vector is a \(+1\) eigenvector of the Grover diffusion. Therefore the amplitude of the first chosen direction is \(1/\sqrt n\). Along a shortest direction word every subsequent direction differs from the preceding one, so every later coin transition uses the off-diagonal Grover entry \(2/n\). Every shortest word consequently has the same positive amplitude
\[
n^{-1/2}\left(\frac2n\right)^{w-1}.
\]
Fix the final coin direction \(j\) in the support of \(x\). Exactly \((w-1)!\) shortest words end in \(j\), and their phases agree. The final amplitude in that coin sector is therefore
\[
(w-1)!\,n^{-1/2}\left(\frac2n\right)^{w-1}.
\]
There are \(w\) orthogonal possible final coin sectors. Summing their squared moduli gives
\[
P_{\rm q}(x,w)
=w\bigl((w-1)!\bigr)^2\frac1n\left(\frac4{n^2}\right)^{w-1}
=\frac{w!(w-1)!4^{w-1}}{n^{2w-1}}.
\]

For the simple classical walk, the same earliest-arrival event consists of the \(w!\) shortest coordinate permutations, each of probability \(n^{-w}\). This gives \(P_{\rm cl}(x,w)=w!/n^w\) and the exact ratio above.

Put \(m=w_n-1\). Stirling's formula \(\log(m!)=m\log m-m+O(\log m)\) yields
\[
\frac1n\log\left(\frac{4^m m!}{n^m}\right)
=\frac mn\left(\log4+\log\frac mn-1\right)+o(1)
\longrightarrow\rho\log\!\left(\frac{4\rho}e\right).
\]
The sign changes exactly at \(\rho=e/4\). For \(w=n\), the exact probability can be written as \(4^{n-1}(n!)^2/n^{2n}\); the displayed antipodal expansion follows from the standard two-term Stirling expansion.

## Verification
The accompanying `verify.py` uses exact rational arithmetic after scaling all quantum amplitudes by \(\sqrt n\). It explicitly evolves the full coined walk for \(2\le n\le7\) and checks the formula for every \(1\le w\le n\). It separately checks the exact quantum/classical ratio. These finite calculations corroborate the algebra but are not used to prove the quantified statement.

## Relationship to prior work
Kokainis, Prūsis, Vihrovs, Kashcheyevs and Ambainis define exactly this discrete Grover walk and prove strong pointwise dispersion at a time near \(0.8663n\), with numerical optimization near \(0.849n\). Their paper also develops Hamming-shell recurrences and a factorial inequality relating shell mass to return probability. It does not state the exact earliest-arrival shell law or the quantum/classical crossover at \(e/4\).

Kempe studies one-shot and concurrent hitting of the opposite corner. Her Eq. (2) gives an exact spectral expression for the opposite-corner amplitude at arbitrary time and her theorem identifies a near-unit hitting window around \(\pi n/2\). That covers a much later antipodal regime and supplies a general spectral tool; it does not state the all-Hamming-weight first-arrival profile or the \(e/4\) crossover. The antipodal specialization here is included as a boundary corollary, not as the originality-bearing part of the finding.

Moore and Russell establish linear-time mixing for the discrete hypercube walk and exact uniform mixing for the continuous-time walk. Their mixing statements do not determine the shortest-time point probability profile used here.

## Limitations
The crossover is an exponential-rate statement. No claim is made for the fine critical window where \(w/n\) approaches \(e/4\) at a rate that affects subexponential factors. The classical comparator is the simple coordinate walk, not a repeatedly measured Grover walk. Later-time quantum amplitudes include paths with repeated directions and sign changes and are outside this result.

## References
1. M. Kokainis, K. Prūsis, J. Vihrovs, V. Kashcheyevs, A. Ambainis, *Strong dispersion property for the quantum walk on the hypercube*, arXiv:2201.11735v1; DOI:10.1088/1751-8121/aca6b9.
2. J. Kempe, *Quantum Random Walks Hit Exponentially Faster*, arXiv:quant-ph/0205083v1.
3. C. Moore, A. Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137v1.
