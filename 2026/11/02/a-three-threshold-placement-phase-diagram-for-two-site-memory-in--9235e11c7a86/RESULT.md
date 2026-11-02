# A three-threshold placement phase diagram for two-site memory in a ten-state reversible ring

## Finding

For the ten-state continuous-time reversible Markov network with jumps of lengths one and three, the integrated stationary autocovariance of a two-site binary readout admits a complete, sharp ranking over **every pair of distinct readout sites**, for all positive relative edge rates. The ranking changes at exactly three algebraic parameter values. In particular, the optimal pair lies across a length-one edge when that edge type has the larger rate, and across a length-three edge when the length-three rate is larger; an antipodal pair is uniquely worst for every parameter. Two further thresholds change the order of the nonoptimal geometries.

Write the ratio of length-three to length-one rates as \(\rho>0\). Let \(T_d(\rho)\) denote the integrated stationary covariance of the indicator of the two vertices at cyclic separation \(d\in\{1,2,3,4,5\}\), with length-one rate normalized to one. The three thresholds are
\[
\rho_- =\frac{\sqrt{13}-1}{6},\qquad \rho_0=1,\qquad \rho_+=\frac{1+\sqrt{13}}{2}.
\]
The strict order from largest to smallest is

| Relative rate | Complete ranking |
|---|---|
| \(0<\rho<\rho_-\) | \(T_1>T_2>T_3>T_4>T_5\) |
| \(\rho_-<\rho<1\) | \(T_1>T_3>T_2>T_4>T_5\) |
| \(1<\rho<\rho_+\) | \(T_3>T_1>T_4>T_2>T_5\) |
| \(\rho>\rho_+\) | \(T_3>T_4>T_1>T_2>T_5\) |

At \(\rho_-\), only \(T_2=T_3\); at \(1\), exactly \(T_1=T_3\) and \(T_2=T_4\); at \(\rho_+\), only \(T_1=T_4\). All other comparisons remain strict at these values. The two-site output always has stationary mean \(1/5\) and variance \(4/25\), regardless of placement, so these are differences in temporal memory rather than equal-time fluctuations or readout prevalence.

## Assumptions and scope

The state space is \(\mathbb Z/10\mathbb Z\). At state \(i\), the chain jumps to each of \(i\pm1\) at rate \(u>0\) and to each of \(i\pm3\) at rate \(v>0\). Set \(\rho=v/u\). The chain is irreducible and reversible with uniform stationary probability \(\pi_i=1/10\). For distinct readout vertices \(i,j\), define \(f_{ij}(k)=\mathbf 1_{\{k=i\}}+\mathbf 1_{\{k=j\}}\) and the (unnormalized) integrated equilibrium autocovariance
\[
\mathcal T(i,j;u,v)=\int_0^\infty\operatorname{Cov}_\pi\bigl(f_{ij}(X_0),f_{ij}(X_t)\bigr)\,dt.
\]
The integral converges because the chain is finite and irreducible. Translation, reflection and cyclic interchange of the two readout vertices reduce all distinct pairs to the five separations \(d=1,2,3,4,5\). Time rescaling gives \(\mathcal T(i,j;u,v)=T_d(\rho)/u\). In the setting of Chen and Limmer (2026), this integral is the output memory susceptibility in the near-equilibrium lag-error/entropy-production inequality; the result concerns the susceptibility, not an assertion of actual protocol error or of global nonlinear accuracy.

## Proof

Let \(L\) be the positive graph Laplacian associated with the normalized generator, with entries obtained from
\[
(Lg)(i)=2(1+\rho)g(i)-g(i+1)-g(i-1)-\rho g(i+3)-\rho g(i-3).
\]
Its nonconstant Fourier eigenvalues are
\[
\lambda_k=2\bigl(1-\cos(2\pi k/10)\bigr)+2\rho\bigl(1-\cos(6\pi k/10)\bigr)>0,
\qquad k=1,\ldots,9.
\]
Writing \(\bar f=f_{0d}-1/5\), spectral integration yields the absolutely convergent finite expression
\[
T_d(\rho)=\frac1{100}\sum_{k=1}^{9}\frac{2+2\cos(2\pi kd/10)}{\lambda_k}.
\tag{1}
\]
Equivalently, with \(J=\mathbf 1\mathbf 1^{\mathsf T}/10\) and \(Q=(L+J)^{-1}-J\), one has \(LQ=QL=I-J\), \(Q\mathbf1=0\), and \(T_d=(Q_{00}+Q_{0d})/5\). These identities eliminate any spectral-normalization ambiguity. If \(R_d=2(Q_{00}-Q_{0d})\) denotes the electrical effective resistance between the two selected vertices, then \(T_d=2Q_{00}/5-R_d/10\). Thus the full readout-memory ranking is equivalently the reverse effective-resistance ranking of this positively weighted two-range circulant graph.

Define \(P=(\rho^2+3\rho+1)(\rho^2+7\rho+1)\). Exact evaluation of (1), or inversion of \(L+J\), gives
\[
\begin{aligned}
T_1&=\frac{(\rho+2)(3\rho^2+11\rho+3)}{25P},\\
T_2&=\frac{9\rho^4+74\rho^3+143\rho^2+90\rho+17}{100(\rho+1)P},\\
T_3&=\frac{(2\rho+1)(3\rho^2+11\rho+3)}{25P},\\
T_4&=\frac{17\rho^4+90\rho^3+143\rho^2+74\rho+9}{100(\rho+1)P},\\
T_5&=\frac{2(\rho+1)}{25(\rho^2+3\rho+1)}.
\end{aligned}
\tag{2}
\]
All denominators in (2) are strictly positive for \(\rho>0\). The comparisons responsible for all changes of order factor as
\[
\begin{aligned}
T_1-T_3&=\frac{(1-\rho)(3\rho^2+11\rho+3)}{25P},\\
T_2-T_3&=-\frac{3\rho^2+\rho-1}{20(\rho+1)(\rho^2+7\rho+1)},\\
T_2-T_4&=\frac{2(1-\rho)(\rho+1)^2}{25P},\\
T_1-T_4&=-\frac{\rho^2-\rho-3}{20(\rho+1)(\rho^2+7\rho+1)}.
\end{aligned}
\tag{3}
\]
Meanwhile the following differences have numerators with strictly positive coefficients and strictly positive denominators:
\[
\begin{aligned}
T_1-T_2&=\frac{3\rho^4+6\rho^3+25\rho^2+34\rho+7}{100(\rho+1)P},\\
T_3-T_4&=\frac{7\rho^4+34\rho^3+25\rho^2+6\rho+3}{100(\rho+1)P},\\
T_2-T_5&=\frac{\rho^4+2\rho^3+15\rho^2+18\rho+9}{100(\rho+1)P},\\
T_4-T_5&=\frac{9\rho^4+18\rho^3+15\rho^2+2\rho+1}{100(\rho+1)P}.
\end{aligned}
\tag{4}
\]
For completeness, \(T_1-T_5=(\rho^3+\rho^2+9\rho+4)/(25P)>0\) and \(T_3-T_5=(4\rho^3+9\rho^2+\rho+1)/(25P)>0\). Thus no other pairwise equalities occur. The unique positive roots of the two quadratics in (3) are respectively \(\rho_-\) and \(\rho_+\); the remaining crossings are at \(\rho=1\). Their signs yield exactly the four rankings in the finding, including the degeneracies at the three thresholds. The rate \(u\) multiplies all \(T_d\) by the same strictly positive factor \(u^{-1}\), and hence cannot change their ranking. This completes the proof.

## Verification

The standalone file `verify.py` builds the exact rational ten-state Laplacian, inverts the rank-one-regularized matrix, and checks \(LQ=QL=I-J\), \(Q\mathbf1=0\), all five formulae (2), all ten pairwise difference factorizations, three crossover identities, and four distinct sample-order regimes. An independent Fourier-series calculation checks all five placements at five rational positive rate ratios. It uses SymPy exact arithmetic for every identity and high-precision numerical evaluation only for the independent spectral comparison. Run `python verify.py` with SymPy installed. The analytical polynomial positivity and root signs, not those finite sample tests, prove the global parameter classification.

## Relationship to prior work

Chen and Limmer (2026), arXiv:2608.23764, derive the general reversible-chain output memory susceptibility as the integrated autocovariance and analyze a ten-state ring with first- and third-neighbor transitions and a two-state readout. Their general formula is used as prior theory. They do not state the all-pair rate-dependent placement ranking, its three algebraic rank-change thresholds, or the extremal placement classification in the material inspected. The specific homogeneous-rate subfamily analyzed here is contained in the network topology used in that work; the stochastic input-training experiments and heterogeneous rates in the paper are not covered by this classification.

Zhang and Yang (2007), DOI:10.1002/qua.21068, derive general spectral resistance-distance formulae for circulant graphs, supplying an alternative route to the Green-kernel representation. This is credited as pre-existing methodology, not a claimed new spectral identity. The present result is the explicit, quantitative, rate-dependent ranking of the physically motivated two-node memory observable on the ten-state two-range network, including exact interior rank reversals. General resistance formulae alone do not specify these ordering inequalities. The Zhang–Yang publisher abstract was available; its full manuscript was not accessible during this assessment, so a hidden overlapping special case remains a publication-priority risk.

## Limitations

This is a complete classification only for **two distinct selected states**, a **ten-state homogeneous reversible circulant network**, and **positive first- and third-neighbor rates**. It does not cover arbitrary node energies, heterogeneous barriers, other ring sizes, larger readout sets, driven transient observables, or nonlinear performance. A broad unlocated theorem on weighted circulant resistance ordering could subsume the result. The work has received a self-review but no independent mathematical or publication-priority audit.

## References

1. Songela W. Chen and David T. Limmer, *Entropy Production Bounds the Accuracy of Computation in Markov Networks*, arXiv:2608.23764, first posted 2026-08-24. https://arxiv.org/abs/2608.23764
2. Heping Zhang and Yujun Yang, *Resistance distance and Kirchhoff index in circulant graphs*, *International Journal of Quantum Chemistry* **107** (2007), 330–339; published online in 2006. https://doi.org/10.1002/qua.21068
3. Eric W. Weisstein, *Resistance Distance*, MathWorld. https://mathworld.wolfram.com/ResistanceDistance.html
