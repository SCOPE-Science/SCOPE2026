# Bessel cluster crossover and strict finite-size transport deficit in tandem exclusion

## Finding
Consider the continuous-time tandem exclusion process on a periodic ring of \(N\ge4\) sites with \(K\) particles and \(Z=N-K\) vacancies, where \(K,Z\ge2\). The moves \(110\to101\) and \(101\to011\) have rates \(\alpha>0\) and \(\beta>0\), respectively; write \(q=\beta/\alpha\). In its dynamically active class, denote by \(J_{N,K}(q)\) the mean clockwise particle current across a fixed bond. Then, for every finite \(q>0\),
\[
0<J_{N,K}(q)<\alpha\frac K N,
\]
and \(J_{N,K}(q)\to \alpha K/N\) as \(q\to\infty\) at fixed \(N,K\). The strict deficit has an explicit nonnegative cluster representation below.

There is an exact singular finite-size crossover. If \(N\to\infty\), \(K_N/N\to\rho\in(0,1)\), and \(q_N/N^2\to c\in(0,\infty)\), put \(t=\rho(1-\rho)/c\). The number \(R_N\) of circular occupied runs obeys
\[
\lim_{N\to\infty}\mathbb P(R_N=r)=\frac{t^{r-1}}{r!(r-1)!\,W(t)},\qquad
W(t)=\sum_{s=0}^\infty\frac{t^s}{s!(s+1)!}=\frac{I_1(2\sqrt t)}{\sqrt t},\quad r=1,2,\ldots,
\]
where \(I_\nu\) denotes the modified Bessel function. Moreover,
\[
\boxed{\lim_{N\to\infty}N\left(\frac{K_N}{N}-\frac{J_{N,K_N}(q_N)}{\alpha}\right)
=\frac{\rho}{1-\rho}\sqrt t\,\frac{I_2(2\sqrt t)}{I_1(2\sqrt t)}.}
\]
The limit is strictly positive for \(\rho,c\in(0,1)\times(0,\infty)\), and describes a finite-volume transport lag absent from a fixed-parameter thermodynamic current law.

## Assumptions and scope
All configurations have exactly \(K\) occupied sites. A *run* is a maximal cyclic string of occupied sites; its count \(R\) is between \(1\) and \(\min(K,Z)\). The *active class* consists of configurations with at least one allowed transition. Configurations without either of the two allowed triples are absorbing and are excluded. The source establishes that the active stationary distribution gives configuration \(\eta\) probability proportional to \(q^{H(\eta)}\), where \(H\) is the number of occupied nearest-neighbour pairs. For a configuration with \(r\) runs, \(H=K-r\). Current is the stationary expected number of allowed particle hops per unit time divided by \(N\). The result uses the source's continuous-time update convention, not a discrete-time synchronous dynamics.

## Proof
**Cyclic run census.** The number of labelled ring configurations with exactly \(r\) occupied runs is
\[
A_{N,K,r}=\frac{N}{r}\binom{K-1}{r-1}\binom{Z-1}{r-1}.
\]
To see this, choose \(r\) positive occupied-run lengths totaling \(K\), choose \(r\) positive vacancy-run lengths totaling \(Z\), then mark a cyclic run beginning. Each configuration has exactly \(r\) choices of that marked beginning among its \(N\) labelled sites.

Every frozen configuration contains no consecutive occupied pair: if an occupied pair occurs, the following maximal occupied run ends in \(110\); if all occupied runs have length one, a vacancy run of length one produces \(101\). Thus frozen configurations are exactly those with all occupied runs of length one and all vacancy runs of length at least two. Their number is
\[
F_{N,K}=\begin{cases}\displaystyle\frac NK\binom{N-2K-1}{K-1},&N\ge3K,\\[2pt]0,&N<3K.\end{cases}
\]
The active partition function is therefore
\[
\mathcal Z^a_{N,K}(q)=\sum_{r=1}^{\min(K,Z)} A_{N,K,r}q^{K-r}-F_{N,K}>0.
\]

**Current and a positive deficit certificate.** Uniform compositions of the \(K\) occupied sites into \(r\) runs have on average \(r(K-r)/(K-1)\) runs of length at least two. Uniform compositions of \(Z\) vacancies into \(r\) runs have on average \(r(r-1)/(Z-1)\) vacancy runs of length one. These count \(110\) and \(101\) moves, respectively. Set \(w_r=A_{N,K,r}q^{K-r}\) and \(m=\min(K,Z)\). Then
\[
\frac{NJ_{N,K}(q)}\alpha=\frac1{\mathcal Z^a_{N,K}(q)}\sum_{r=1}^m w_r\left(\frac{r(K-r)}{K-1}+q\frac{r(r-1)}{Z-1}\right).
\]
By the exact ratio identity
\[
q\,r(r-1)w_r=(K-r+1)(Z-r+1)w_{r-1}\qquad(r\ge2),
\]
the numerator rewrites as \(\sum_{r=1}^m w_r g_{K,Z}(r)\), with
\[
g_{K,Z}(r)=(K-r)\left(\frac r{K-1}+\frac{Z-r}{Z-1}\right).
\]
For frozen configurations the corresponding \(r=K\) and \(g_{K,Z}(K)=0\), so subtracting them does not change this sum. Thus, averaging over the *active* stationary run law,
\[
N\left(\frac KN-\frac{J_{N,K}(q)}\alpha\right)=\mathbb E_a[\Delta_{K,Z}(R)],\qquad
\Delta_{K,Z}(r)=K-g_{K,Z}(r)=\frac{(r-1)[K(K-r-1)+Zr]}{(K-1)(Z-1)}.
\]
The expression is zero at \(r=1\) and positive for \(2\le r\le m\). Since \(K,Z\ge2\), the active state space includes configurations with \(r=2\) of strictly positive weight. Hence the deficit is strictly positive. Current is strictly positive because active states permit jumps. As \(q\to\infty\), the unique leading stationary run count is \(r=1\), and its deficit vanishes, proving the fixed-size limit.

**Double scaling.** Dividing all \(w_r\) by \(w_1=Nq^{K-1}\), the relative weights are exactly
\[
\frac{w_r}{w_1}=\frac1r\binom{K-1}{r-1}\binom{Z-1}{r-1}q^{-(r-1)}.
\]
For each fixed \(r\) they converge to \(t^{r-1}/[r!(r-1)!]\). Uniformly in sufficiently large \(N\), \(KZ/q\) is bounded, giving a summable dominating series \(C^{r-1}/[r!(r-1)!]\), including when extended by zero beyond \(m\). The frozen contribution divided by \(w_1\) vanishes: \(F_{N,K}\le2^N\) and \(q^{K-1}\) grows faster than exponentially because \(K/N\to\rho>0\) and \(q\asymp N^2\). Thus the run law converges to the displayed Bessel law.

For \(\rho\) bounded away from 0 and 1, the exact \(\Delta_{K,Z}(r)\) is bounded by \(C_\rho (r-1)\) on the whole permitted range, and for fixed \(r\) it converges to \(\rho(r-1)/(1-\rho)\). Dominated convergence applies to the deficit expectation. Differentiating the absolutely convergent defining series gives \(tW'(t)/W(t)=\sqrt t I_2(2\sqrt t)/I_1(2\sqrt t)\), proving the stated crossover.

## Verification
The included standalone `verify.py` uses exact rational arithmetic to compare the run-census current with exhaustive configuration enumeration for every \(4\le N\le11\), \(2\le K\le N-2\), and four rational values of \(q\). It separately verifies the full weighted Markov-generator stationarity equations over 11,433 checked state-parameter pairs with three rational values of \(q\). A decimal-series calculation checks the Bessel crossover against finite-size values at five independent pairs of density and scaling parameter, with increasing ring sizes. These finite checks do not replace the proof for arbitrary size.

## Relationship to prior work
Nguyen Ngoc, Lam Thi Nhung and Huynh Anh Thi establish the Gibbs active stationary measure and transfer-matrix thermodynamic current for this exact tandem dynamics. The present result uses that stationary measure, but computes the active finite-ring run-weighted current, a strict all-parameter finite-volume deficit, and a joint \(q/N^2\) scaling limit; the original fixed-\(q\) thermodynamic law alone cannot be used after exchanging limits. Denisov and Hänggi study domains in the equilibrium Ising chain with **free** boundary conditions; their domain enumeration does not imply the active-sector irreversible current. Antal, Droz and Rácz investigate a low-temperature finite-size Ising magnetization law, without the specified transport observable. Previously obtained thermodynamic density-optimizer asymptotics for tandem exclusion use a different \(q\to\infty\) limit and do not imply this fixed-density finite-size lag.

## Limitations
The active-sector restriction is essential: the full chain has frozen absorbing classes when sufficiently dilute, so no unique stationary measure across all classes. The two-vacancy and two-particle assumptions are essential to the given uniform statement; with one vacancy, the current obeys a different formula. The Bessel limit requires \(K/N\to\rho\in(0,1)\) and \(q/N^2\to c\in(0,\infty)\); no assertion is made for more extreme windows or open boundaries. The originality assessment cannot exclude unindexed earlier derivations or implications of general canonical finite-size scaling results.

## References
1. N. P. Nguyen Ngoc, L. T. Nhung and H. A. Thi, *Tandem Exclusion Process*, arXiv:2606.01568v1 (first public June 1, 2026), especially Theorems 2 and 4 and the active/frozen decomposition.
2. S. I. Denisov and P. Hänggi, *Domain statistics in a finite Ising chain*, Phys. Rev. E 71, 046137 (2005); arXiv:cond-mat/0603417v1 (2006).
3. T. Antal, M. Droz and Z. Rácz, *Probability distribution of magnetization in the one-dimensional Ising model: effects of boundary conditions*, arXiv:cond-mat/0308442 (2003).
