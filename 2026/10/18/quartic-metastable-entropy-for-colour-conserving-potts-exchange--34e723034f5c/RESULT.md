# Quartic metastable entropy for colour-conserving Potts exchange on a ring

## Finding

Consider a periodic chain of \(N\ge4\) sites, each carrying one of \(q\ge2\) labelled colours. The ferromagnetic Potts energy is \(H(\sigma)=J\sum_{i=0}^{N-1}\mathbf1_{\sigma_i\ne\sigma_{i+1}}\), with \(J>0\) and indices modulo \(N\). Only swaps of adjacent unequal colours that **strictly decrease** \(H\) are allowed; swaps with unchanged energy are not performed. Let \(B_{N,q}\) be the total number of configurations admitting no such swap, across all colour populations.

Define the \(q^3\times q^3\) zero-one matrix \(T_q\), indexed by triples \((u,a,b)\) from \(\{0,\ldots,q-1\}^3\). Set \(T_q[(u,a,b),(a,b,v)]=1\) if either \(a=b\), or
\[
\mathbf1_{u=a}+\mathbf1_{b=v}\ge\mathbf1_{u=b}+\mathbf1_{a=v},
\]
and set all other entries to zero. Then the **exact finite-volume blocked count** is
\[
 B_{N,q}=\operatorname{tr}(T_q^N)\quad(N\ge4).
\]

Let \(\lambda_q\) be the largest positive eigenvalue of
\[
M_q=\begin{pmatrix}
1&q-1&0&0&0\\
0&0&1&1&q-2\\
0&0&0&1&0\\
1&q-1&0&0&0\\
0&0&0&1&q-2
\end{pmatrix}.
\]
For \(q=2\) the last row and column, representing three distinct colours, are omitted. For each fixed integer \(q\ge2\),
\[
B_{N,q}=\lambda_q^N(1+O(\theta_q^N)),\qquad 0\le\theta_q<1,
\]
for some \(\theta_q\) depending on \(q\). The strict-descent metastable entropy per site is exactly \(s_q=\log\lambda_q\), and the characteristic identity is
\[
\det(tI-M_q)=t\bigl(t^4+(1-q)t^3-t^2+(1-q)t+(q-1)(q-2)\bigr)
\]
when \(q\ge3\); deleting the unavailable orbit for \(q=2\) gives the tribonacci cubic \(t^3-t^2-t-1\) times \(t\). Numerically, \(s_2=0.609377863436\ldots\) and \(s_3=0.945178226717\ldots\). For comparison, \(\lambda_2=1.839286755214\ldots\) and \(\lambda_3=2.573271963535\ldots\).

The count distinguishes multicolour states structurally: the cyclic three-colour sequence \(012012\) has no strictly lowering neighbour exchange, although its two-colour alternating analogue \(0101\) does.

## Assumptions and scope

Every statement concerns finite labelled periodic rings with \(q\ge2\), \(N\ge4\), uniform positive nearest-neighbour coupling, and swaps of adjacent unequal colours only. An exchange with zero energy change is forbidden by the dynamics; allowing neutral moves changes the absorbing-state set. The enumeration sums over all conserved colour-count sectors and does not claim that dynamical trajectories sample terminal configurations uniformly. The growth limit is taken at fixed \(q\), then \(N\to\infty\).

## Proof

**Local criterion.** Fix an adjacent pair \((a,b)\) with external neighbours \(u,v\). Its energy-contributing exterior bonds initially contribute \(J(\mathbf1_{u\ne a}+\mathbf1_{b\ne v})\), and after exchanging the pair contribute \(J(\mathbf1_{u\ne b}+\mathbf1_{a\ne v})\). The interior bond \((a,b)\) is unchanged. Hence a strictly decreasing swap exists precisely when \(\mathbf1_{u=a}+\mathbf1_{b=v}<\mathbf1_{u=b}+\mathbf1_{a=v}\). This proves the four-site condition, including repeated external colours and the case \(N=4\).

**Finite count.** Every closed walk of length \(N\) in the directed triple-context graph of \(T_q\) corresponds bijectively, with specified site origin, to a cyclic word of length \(N\), with the final-to-initial overlap restoring the cyclic four-site condition. Thus the count equals the trace of \(T_q^N\).

**Five-pattern reduction.** Permuting the \(q\) colour labels acts on triple contexts and commutes with \(T_q\). For \(q\ge3\), there are precisely five orbit types: AAA, AAB, ABA, ABB, ABC, in which different letters denote different colours. In this order, counting admissible appended colours produces exactly the five-by-five matrix \(M_q\) displayed above. The ABC orbit is absent when \(q=2\), so the leading four-by-four block is used. Direct determinant expansion gives the displayed quartic characteristic identity (and its binary specialization).

**Perron eigenvalue and exact asymptotic prefactor.** The full triple-context graph is primitive. Indeed, from any \((u,a,b)\), append colour \(b\) twice to reach \((b,b,b)\): the first step is always admissible by the local inequality, and the second has equal middle symbols. From \((b,b,b)\) append any target colour \(c\) three times to reach \((c,c,c)\). From \((c,c,c)\) append \(v,w\) to reach any target triple \((c,v,w)\); the first step has equal middle symbols and the second is permitted because its first two symbols coincide. The graph is therefore strongly connected and has a self-loop on every all-equal state. Thus it is primitive.

The Perron eigenvector of this primitive nonnegative matrix is unique and strictly positive. Colour permutations preserve it, so it is constant on each orbit type; the Perron eigenvalue of \(T_q\) is consequently the Perron eigenvalue of \(M_q\) (or the reduced binary matrix). All other eigenvalues of \(T_q\) have strictly smaller modulus, and the Perron eigenvalue is simple. As \(B_{N,q}=\operatorname{tr}(T_q^N)\), its leading term is **exactly** \(\lambda_q^N\) with coefficient one. Taking logarithms proves the entropy law. The quoted root values are numerical evaluations only, not premises of the proof.

## Verification

The standalone standard-library program `artifacts/verify.py` checks the local swap-energy inequality against independent energy recomputation for all words with \(q=2,3,4\) and the stated finite-size ranges, and checks the count against the trace of the full labelled triple transfer matrix. It also reconstructs the quotient transitions and validates the characteristic polynomial with exact integer determinants at six distinct values of \(q\) and nine of \(t\). Since both sides have degree at most five in either argument, these evaluations also establish the symbolic polynomial identity by interpolation. The program does not replace the analytic primitivity and trace-asymptotic proof.

## Relationship to prior work

De Smedt, Godrèche and Luck studied the binary zero-temperature Kawasaki Ising chain, explicitly separating energy-lowering exchanges from energy-neutral diffusion and identifying the restricted no-diffusion blocked words. Their result provides the \(q=2\) kinetic baseline; **the binary case and the transfer-matrix method are not claimed as new**. Here the additional claim is the all-\(q\) labelled-colour classification together with its universal five-pattern quotient and explicit quartic entropy law. Dhar's earlier one-dimensional Potts discussion includes an antiferromagnetic three-colour Kawasaki regime; its full text was not accessible for a decisive formulation-level comparison. Searches did not establish an identical published all-colour ferromagnetic strict-descent law, but non-detection cannot prove novelty.

## Limitations

Energy-neutral Kawasaki moves are suppressed, so this is not a description of terminal states under unconstrained zero-temperature Kawasaki dynamics. Neither finite-time blocking distributions nor per-sector (fixed colour populations) entropies are determined. The current bibliographic comparison does not rule out a differently formulated precursor.

## References

1. G. De Smedt, C. Godrèche, and J. M. Luck, *Metastable states of the Ising chain with Kawasaki dynamics*, arXiv:cond-mat/0210477v1 (first posted 2002-10-22), https://arxiv.org/abs/cond-mat/0210477 . In particular §§1–3 and Table 1 distinguish the no-diffusion and diffusion regimes.
2. D. Dhar, *The relaxation to equilibrium in one-dimensional Potts models*, Journal of the Indian Institute of Science **75** (1995), 297–304; bibliographic catalogue https://repository.ias.ac.in/view/year/1995.html . The text was not obtained; comparisons to its specific Kawasaki statements are limited to publicly indexed excerpts.
