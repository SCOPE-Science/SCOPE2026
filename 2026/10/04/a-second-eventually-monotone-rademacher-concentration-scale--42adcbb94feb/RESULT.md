# A second eventually monotone Rademacher concentration scale
## Finding
For independent Rademacher variables \(\varepsilon_1,\varepsilon_2,\ldots\), let \(S_N=\sum_{i=1}^N\varepsilon_i\). Following Hendriks and van Zuijlen, define
\[
n_k=2\left\lceil\frac{k^2/\xi^2-k}{2}\right\rceil+k-1,
\qquad R_k=\Pr\{|S_{n_k-1}|\le k-2\}.
\]
At \(\xi=\sqrt5/2\), the sequence is eventually strictly increasing. If \(r\equiv k\pmod{10}\), then
\[
R_{k+1}-R_k=\frac{\xi\phi(\xi)}{k^2}\left(L_r+O(k^{-1})\right),
\]
where
\[
(L_0,\ldots,L_9)=\left(\frac74,\frac54,\frac34,\frac{11}4,\frac94,\frac74,\frac54,\frac{13}4,\frac{11}4,\frac94\right).
\]
Every leading constant is positive, so \(R_{k+1}>R_k\) for all sufficiently large \(k\). This supplies a second explicit \(\xi>1\) and refutes the source paper's stated belief, not a theorem, that \(\sqrt2\) is the only such value.

## Assumptions and scope
The variables \(\varepsilon_i\) are independent with \(\Pr(\varepsilon_i=1)=\Pr(\varepsilon_i=-1)=1/2\). The claim is exactly about the sequence \(P_{n_k-1}(k-2)\) discussed in Section 4 of the source, specialized to \(\xi=\sqrt5/2\). It is only an eventual statement: no least monotonicity index and no classification of all \(\xi>1\) is claimed.

## Proof
Put \(c=\xi^2\) and \(m_k=n_k+1\). Then \(m_k\) is the least integer at least \(k^2/c\) having the same parity as \(k\). Define
\[
\delta_k=m_k-\frac{k^2}{c},\qquad e_k=\delta_k-2,\qquad N_k=m_k-2.
\]
Thus \(R_k=\Pr\{|S_{N_k}|\le k-2\}\), with bounded \(e_k\).

We need a lattice central-limit expansion. If \(N\to\infty\), \(h\equiv N\pmod2\), and \(b=(h+1)/\sqrt N\) remains in a fixed compact subset of \((0,\infty)\), Stirling's formula uniformly for \(s=O(\sqrt N)\) gives
\[
\Pr\{S_N=s\}=\frac2{\sqrt N}\phi(x)\left[1-\frac{x^4-6x^2+3}{12N}+O(N^{-2})\right],\qquad x=\frac{s}{\sqrt N}.
\]
Summing over \(s=-h,-h+2,\ldots,h\) by the composite midpoint rule, whose mesh is \(2/\sqrt N\), yields
\[
\Pr\{|S_N|\le h\}=2\Phi(b)-1+\frac{(b^3-b)\phi(b)}{6N}+O(N^{-2}).
\]
Indeed the midpoint correction is \(b\phi(b)/(3N)\); adding it to the integrated fourth-Hermite term changes \((b^3-3b)/(6N)\) into \((b^3-b)/(6N)\).

Apply this with \(N=N_k\), \(h=k-2\), and \(b_k=(k-1)/\sqrt{N_k}\). Since \(N_k=k^2/c+e_k\), Taylor expansion at \(\xi=\sqrt c\), uniformly in bounded \(e_k\), gives
\[
R_k=2\Phi(\xi)-1-\frac{2\xi\phi(\xi)}k+\frac{\xi^3\phi(\xi)}{k^2}\left[-e_k+\frac{c-7}{6}\right]+O(k^{-3}).
\]
Therefore
\[
R_{k+1}-R_k=\frac{\xi\phi(\xi)}{k^2}\left(2-c(e_{k+1}-e_k)+O(k^{-1})\right)
=\frac{\xi\phi(\xi)}{k^2}\left(2k+3-c(m_{k+1}-m_k)+O(k^{-1})\right).
\]
For \(c=5/4\), the parity ceiling is periodic modulo \(10\). For residues \(0,1,\ldots,9\), respectively,
\[
\delta_k=\left(0,\frac15,\frac45,\frac95,\frac65,1,\frac65,\frac95,\frac45,\frac15\right).
\]
Substitution gives exactly the ten displayed \(L_r\). Their minimum is \(3/4>0\), so the uniform \(O(k^{-1})\) remainder is eventually too small to change the sign. Hence \(R_{k+1}>R_k\) for all sufficiently large \(k\).

## Verification
The standalone `verify.py` reconstructs the parity ceiling, checks the ten exact residue phases and rational coefficients, and exhaustively computes exact binomial probabilities for \(2\le k\le80\), where it finds no decrease. That finite computation is only a stress test; the infinite claim follows from the analytic asymptotic and positive minimum coefficient \(3/4\).

## Relationship to prior work
Hendriks and van Zuijlen define the same \(n_k\) and sequence. Their theorem proves monotonicity for \(0<\xi\le1\). In Section 4 they explain that the regime \(\xi>1\) is irregular, prove eventual monotonicity for \(\xi=\sqrt2\), and explicitly state their belief that this is the only \(\xi>1\) with asymptotically increasing \(P_{n_k-1}(k-2)\). The present result addresses that exact statement and gives a counterexample at \(\xi=\sqrt5/2\).

Pinelis studies supremal tails of normalized Rademacher sums, and Hollom--Portier later determine global anti-concentration infima over arbitrary coefficient vectors. Those results optimize different objects and do not imply eventual monotonicity of this parity-ceiling sequence.

## Limitations
The result does not identify the first monotonicity index and does not classify all parameters above one. The literature comparison is strongest against the full lead source and targeted Rademacher-tail searches; unindexed or inaccessible work could contain the same residue-class counterexample.

## References
H. Hendriks and M. C. A. van Zuijlen, “Sharp Concentration Inequalities for Deviations from the Mean for Sums of Independent Rademacher Random Variables,” *Annals of Combinatorics* 21 (2017), 281–291. DOI: 10.1007/s00026-017-0351-3.

I. Pinelis, “On the supremum of the tails of normalized sums of independent Rademacher random variables,” *Statistics & Probability Letters* 99 (2015), 131–134. DOI: 10.1016/j.spl.2015.01.010.

L. Hollom and J. Portier, “Tight Anti-Concentration of Rademacher Sums,” *Random Structures & Algorithms* 67 (2025), e70024. DOI: 10.1002/rsa.70024.
