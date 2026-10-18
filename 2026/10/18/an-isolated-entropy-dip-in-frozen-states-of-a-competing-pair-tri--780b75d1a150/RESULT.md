# An isolated entropy dip in frozen states of a competing pair–triplet Ising ring

## Finding
Consider a periodic Ising ring with ferromagnetic nearest-neighbor pair coupling and a competing consecutive-triplet coupling. The exact number of strictly blocked configurations has a transfer-matrix formula and five entropy regimes. The surprising feature is **an isolated entropy dip at the precise coupling ratio \(r=2\)**: at that ratio, strictly blocked configurations are exponentially rarer than at nearby couplings on either side.

Let \(\alpha>1\), \(\beta>1\), \(\gamma>1\), and \(\delta>1\) be the following roots:
\[
\begin{aligned}
\alpha^3-\alpha-1&=0,&\alpha&=1.324717957244746\ldots,\\
\beta^{10}-\beta^9-\beta^7-\beta^5+\beta^4+\beta+1&=0,&\beta&=1.457502196508113\ldots,\\
\gamma^9-\gamma^6-\gamma^5-\gamma^3-\gamma^2-\gamma-1&=0,&\gamma&=1.390588979719943\ldots,\\
\delta^3-\delta^2-1&=0,&\delta&=1.465571231876768\ldots.
\end{aligned}
\]
In the second line, \(\beta\) denotes the **largest positive real root**. Then the strict-blocked-state entropy per spin is
\[
 s(r)=\lim_{N\to\infty}\frac{\log B_N(r)}{N}=
 \begin{cases}
 0,&r=0,\\
 \log\alpha,&0<r\le2/3,\\
 \log\beta,&2/3<r<2,\\
 \log\gamma,&r=2,\\
 \log\delta,&r>2.
 \end{cases}
\]
In particular \(\log\gamma<\log\beta<\log\delta\), while \(\log\gamma<\log\delta\). The entropy increases abruptly at arbitrarily weak triplet coupling, at \(2/3\) from the right, and at \(2\) from the right; exactly at \(2\) it falls below *both* one-sided values.

## Assumptions and scope
For integer \(N\ge5\), let \(s_i\in\{-1,+1\}\), with indices modulo \(N\), and define
\[
 H_N(s)=-J\sum_{i=0}^{N-1}s_i s_{i+1}+K\sum_{i=0}^{N-1}s_i s_{i+1}s_{i+2},
 \qquad J>0,\quad K\ge0,\quad r=K/J.
\]
A configuration is **strictly blocked** if \(H_N(s^{(i)})>H_N(s)\) for every site \(i\), where \(s^{(i)}\) differs from \(s\) by reversing spin \(i\). Thus ties are **not** blocked. This corresponds to zero-temperature single-spin Glauber dynamics in which energy-neutral flips are allowed; it is not the weaker nondecreasing-energy local-minimum convention.

## Proof
**Local inequality.** Direct cancellation of the five terms touching site \(i\) gives
\[
 H_N(s^{(i)})-H_N(s)=2J s_i \left[(s_{i-1}+s_{i+1})-r(s_{i-2}s_{i-1}+s_{i-1}s_{i+1}+s_{i+1}s_{i+2})\right].
\]
For a five-site word \((a,b,c,d,e)\in\{-1,+1\}^5\), write
\[
 F_r(a,b,c,d,e)=c\{b+d-r(ab+bd+de)\}.
\]
The word is admissible at its center exactly when \(F_r>0\). The possible nonzero coefficients \(b+d\in\{-2,0,2\}\) and \(ab+bd+de\in\{-3,-1,1,3\}\), together with direct inspection of the \(32\) words, show that the admissible-word set changes only at \(r=0,2/3,2\). Equality cases are excluded by the strict inequality.

**Exact transfer representation.** Index the rows and columns of \(M_r\) by the \(16\) four-spin words. Its sole possible nonzero entries are
\[
 (M_r)_{(a,b,c,d),(b,c,d,e)}=
 \mathbf1\{F_r(a,b,c,d,e)>0\},\quad e\in\{-1,+1\}.
\]
All other entries vanish. A length-\(N\) closed walk corresponds bijectively to an indexed periodic spin configuration of length \(N\), each of whose centered five-site words passes the strict inequality. Therefore, **for each \(N\ge5\)**,
\[
 B_N(r)=\operatorname{tr}(M_r^N).
\]

**Exact characteristic polynomials.** Enumerating the \(32\) admissible five-site words and expanding the \(16\times16\) determinants gives the following fully reproducible list. The symbol \(x\) denotes the characteristic-polynomial variable, not a coupling.
\[
\begin{array}{c|l}
\text{parameter range}&\det(xI-M_r)\\\hline
r=0 &x^{14}(x-1)^2\\
0<r<2/3 &x^{10}(x-1)(x^2-x+1)(x^3-x-1)\\
r=2/3 &x^{11}(x^2-x+1)(x^3-x-1)\\
2/3<r<2 &x^6(x^{10}-x^9-x^7-x^5+x^4+x+1)\\
r=2 &x^6(x-1)(x^9-x^6-x^5-x^3-x^2-x-1)\\
r>2 &x^4(x^3-x^2-1)(x^9-x^3-1).
\end{array}
\]
This is a finite exact calculation, not a numerical fit. The accompanying `verify.py` recomputes the transfer matrix and all six determinants from the defining inequality without using the displayed factors to construct the matrices.

**Existence and identification of entropy.** In each open/threshold regime the nonnegative transfer graph has a unique recurrent strongly connected component of maximal spectral radius. For \(r=0\) there are two one-vertex loops; in the five positive-\(r\) regimes in table order, the maximal components have \(6,6,11,10,12\) vertices respectively. Each has a self-loop, so it is primitive. The remaining recurrent components, if any, have strictly smaller spectral radii (in the first positive regime there is a separate \(1\)-eigenvalue). Perron–Frobenius theory therefore yields
\[
 B_N(r)=\rho(M_r)^N(c_r+o(1))
\]
for a positive constant \(c_r\) in each fixed regime, and hence \(s(r)=\log\rho(M_r)\). The exact polynomial factorizations identify these spectral radii as \(1,\alpha,\alpha,\beta,\gamma,\delta\), respectively. The \(x^9-x^3-1\) factor in the final regime has strictly smaller positive root than \(\delta\).

**Strict isolated drop.** The transfer graph at \(r=2\) is a proper subgraph of the graph throughout either adjacent open regime. The dominant recurrent components are all primitive; the threshold's ten-vertex component sits properly in each neighboring dominant component (eleven vertices to the left; twelve to the right). Strict Perron–Frobenius monotonicity for proper irreducible nonnegative extensions yields \(\gamma<\beta\) and \(\gamma<\delta\). At \(r=2/3\), the lost all-positive-spin loop has spectral radius one and does not affect the dominant \(\alpha\) component; immediately to the right, its proper recurrent graph extension yields \(\beta>\alpha\). At \(r=0\), only the two uniform configurations are blocked, while every positive sufficiently small \(r\) has the six-vertex primitive component with \(\alpha>1\). This proves the complete phase diagram and the isolated entropy dip.

## Verification
Run `python verify.py` with Python, SymPy and NetworkX installed. It independently constructs every transfer matrix, checks all six characteristic polynomials symbolically, identifies the recurrent strongly connected components and their self-loops, and compares transfer traces with **direct full-Hamiltonian spin-flip enumeration** for all sizes \(5\le N\le11\) at six representative exact rational couplings. All **42 count comparisons**, six polynomial identities and recurrent-component checks passed. These finite tests are cross-checks; the proof above establishes every size and asymptotic regime.

## Relationship to prior work
Kisker, Rieger and Schreckenberg (1994) derive metastable states and the exponential growth constant for the **pure** consecutive three-spin interaction. Their pure model is recovered as the large-ratio limiting local inequality here, so its leading entropy \(\log\delta\) is **not** claimed as novel. Their Hamiltonian has only a three-spin term and does not imply the three finite mixed-coupling thresholds.

De Smedt, Godrèche and Luck (2002) study constrained zero-temperature dynamics in paramagnetic and pair-interaction Ising chains. Their constrained dynamics and pair-only Hamiltonian differ from the unconstrained zero-temperature flip rule under a simultaneous pair and triplet interaction. Their blocked-state enumeration does not cover the mixed-coupling transfer graph.

Frøyen, Sudbø and Hemmer (1976) discuss pair and triplet coupling in a **mean-field** triangular-lattice equilibrium setting; that framework does not imply strict single-spin-flip blocked-state counts on a periodic one-dimensional ring.

## Limitations
The counting measure on all strictly blocked configurations is not the nonequilibrium distribution reached from a random quench. No claim is made about kinetics, metastable lifetimes, thermodynamic finite-temperature phase transitions or universality beyond the precisely stated Hamiltonian and update convention. Near the thresholds the noncommutation between coupling and volume limits matters. Primary literature and result-record searches did not find an exact equivalent, but unindexed or differently formulated treatments remain a bibliographic risk. The two previously established pure limiting regimes are explicitly separated from the new mixed-coupling classification.

## References
1. J. Kisker, H. Rieger and M. Schreckenberg, *Escape from Metastability via Aging: Non-Equilibrium Dynamics in a One-Dimensional Ising Model*, 1994, arXiv:cond-mat/9408060, https://arxiv.org/abs/cond-mat/9408060 .
2. G. De Smedt, C. Godrèche and J. M. Luck, *Jamming, freezing and metastability in one-dimensional spin systems*, 2002, arXiv:cond-mat/0202465, https://arxiv.org/abs/cond-mat/0202465 .
3. S. Frøyen, Aa. S. Sudbø and P. C. Hemmer, *Ising models with two- and three-spin interactions: Mean field equation of state*, Physica A 85 (1976), 399–408, DOI:10.1016/0378-4371(76)90058-3 .
