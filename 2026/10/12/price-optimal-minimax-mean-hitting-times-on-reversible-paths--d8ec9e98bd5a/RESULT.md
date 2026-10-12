# Price-optimal minimax mean hitting times on reversible paths

## Finding

**Theorem (exact worst-pair hitting-time design).** Fix an integer \(n\geq3\), a strictly positive probability vector \((\pi_1,\ldots,\pi_n)\), and strictly positive unit-conductance prices \((c_1,\ldots,c_{n-1})\). Among all strictly positive edge conductances \((w_1,\ldots,w_{n-1})\) satisfying \(\sum_{i=1}^{n-1}c_iw_i=1\), consider the continuous-time nearest-neighbor reversible chain with jump rates \(q_{i,i+1}=w_i/\pi_i\) and \(q_{i+1,i}=w_i/\pi_{i+1}\). Write \(H_{ab}\) for its expected first hitting time of state \(b\) from state \(a\). Its robust design objective is \(\mathcal{M}(w)=\max_{a\ne b}H_{ab}\).

Define \(P_i=\sum_{j=1}^{i}\pi_j\), \(a_i(\lambda)=(1-\lambda)(1-P_i)+\lambda P_i\), and
\[
 S(\lambda)=\sum_{i=1}^{n-1}\sqrt{c_i a_i(\lambda)},\qquad
 G(\lambda)=\sum_{i=1}^{n-1}\frac{\sqrt{c_i}(2P_i-1)}{\sqrt{a_i(\lambda)}}
 \quad(0\leq\lambda\leq1).
\]
The function \(G\) is strictly decreasing. Set \(\lambda_*\) to zero if \(G(0)\leq0\), to one if \(G(1)\geq0\), and otherwise to the unique root of \(G(\lambda_*)=0\) in \((0,1)\). Then the unique global minimizer and the exact optimal worst-pair hitting time are
\[
 \boxed{w_i^*=\frac{\sqrt{a_i(\lambda_*)/c_i}}{S(\lambda_*)},\qquad
 \min_w\mathcal{M}(w)=S(\lambda_*)^2.}
\]
The maximum over all ordered pairs is always attained by at least one of the two oppositely directed endpoint pairs. If \(0<\lambda_*<1\), the two endpoint expectations coincide; in a boundary case, the indicated active endpoint expectation alone determines the maximum (the other may also tie at equality).

**Stationary-mass cancellation.** If \(\sum_{i=1}^{n-1}\sqrt{c_i}(2P_i-1)=0\), then \(\lambda_*=1/2\),
\[
 \boxed{w_i^*=\frac{1}{\sqrt{c_i}\sum_{k=1}^{n-1}\sqrt{c_k}},\qquad
 \min_w\mathcal{M}(w)=\frac12\left(\sum_{k=1}^{n-1}\sqrt{c_k}\right)^2.}
\]
In particular this holds whenever the stationary masses and edge prices are both reflection-symmetric. Thus the optimum in this substantial family is independent of the individual stationary masses, even though the generator rates depend on them.

**Exact three-state price frontier.** For \(n=3\), \((\pi_1,\pi_2,\pi_3)=(1/4,1/2,1/4)\), and \(c_1,c_2>0\), let \(r=c_1/c_2\). When \(1/3\leq r\leq3\), the unique optimal conductances are \(w_1=w_2=1/(c_1+c_2)\) and the optimal worst hitting time equals \(c_1+c_2\). If \(r>3\), the optimum equals \((\sqrt{3c_1}+\sqrt{c_2})^2/4\); if \(r<1/3\), it equals \((\sqrt{c_1}+\sqrt{3c_2})^2/4\). Outside the central regime, the two conductances are unequal and are specified by the general formula with a boundary \(\lambda_*\). The transition at each endpoint of this interval is continuous.

## Assumptions and scope

The chain is a finite, irreducible, *continuous-time* birth-and-death chain on the path \(1-2-\cdots-n\). Its stationary law \(\pi\) is prescribed independently of the conductance design. The rates are normalized by \(q_{i,i+1}=w_i/\pi_i\), so detailed balance holds exactly and no discrete-time holding probabilities or row-stochastic restrictions are imposed. Prices \(c_i\) multiply conductances linearly, with total price-weighted conductance exactly one. Mean hitting time measures physical continuous time, not number of jumps, commute time, mean stationary-target time, spectral relaxation time, or cover time. A zero conductance would disconnect the path and make some hitting time infinite, hence cannot minimize; the theorem permits only positive optimal edges. The exclusion of \(n=2\) avoids a degenerate nonunique scalar dual parameter; the conductance optimizer is still trivial in that case but is not part of the claim.

## Proof

**Step 1: Exact directional first-passage sums.** Fix adjacent vertices \(i\) and \(i+1\). Let \(h_j\) denote the expected hitting time of \(i+1\) from vertex \(j\leq i+1\), with \(h_{i+1}=0\). The first-step Poisson equations \(-Qh=1\) on \(j\leq i\), multiplied by the stationary masses and summed over \(j=1,\ldots,i\), telescope all internal edge fluxes. Their sole boundary flux is \(w_i(h_i-h_{i+1})\), so \(H_{i,i+1}=P_i/w_i\). Starting from the other side and summing over \(j=i+1,\ldots,n\) likewise gives \(H_{i+1,i}=(1-P_i)/w_i\). Strong Markov decomposition at successive intervening states yields, for \(a<b\),
\[
 H_{ab}=\sum_{i=a}^{b-1}\frac{P_i}{w_i},\qquad
 H_{ba}=\sum_{i=a}^{b-1}\frac{1-P_i}{w_i}.
\]
All terms are strictly positive. Consequently the largest hitting time among all ordered pairs is exactly
\[
 \mathcal{M}(w)=\max\left\{\sum_{i=1}^{n-1}\frac{P_i}{w_i},\;
 \sum_{i=1}^{n-1}\frac{1-P_i}{w_i}\right\},
\]
with endpoint pairs realizing its two arguments. These identities can also be viewed as the path specialization of the classical electrical-network hitting-time relations cited below; the continuous-time normalization here follows directly from the Poisson equation.

**Step 2: A sharp lower bound for every multiplier.** For any \(\lambda\in[0,1]\) and feasible \(w\), the maximum of the two endpoint quantities is at least their \(\lambda\)-weighted average. Weighted Cauchy–Schwarz then gives
\[
 \mathcal{M}(w)\geq\sum_{i=1}^{n-1}\frac{a_i(\lambda)}{w_i}
 \geq\frac{\big(\sum_{i=1}^{n-1}\sqrt{c_i a_i(\lambda)}\big)^2}{\sum_{i=1}^{n-1}c_iw_i}=S(\lambda)^2.
\]
For each \(\lambda\) the equality condition in this strictly positive Cauchy–Schwarz inequality forces the unique feasible vector
\[
 w_i(\lambda)=\frac{\sqrt{a_i(\lambda)/c_i}}{S(\lambda)}.
\]

**Step 3: The unique dual maximizer and exact attainment.** Every \(P_i\) lies strictly between zero and one, so \(a_i(\lambda)>0\). Direct differentiation gives
\[
 2S'(\lambda)=G(\lambda),\qquad
 G'(\lambda)=-\frac12\sum_{i=1}^{n-1}\frac{\sqrt{c_i}(2P_i-1)^2}{a_i(\lambda)^{3/2}}<0.
\]
Strictness holds because \(n\geq3\), \(P_1<P_2\), and thus not all \(P_i\) equal \(1/2\). Hence \(S\) is strictly concave and is maximized at the uniquely specified \(\lambda_*\). For the Cauchy–Schwarz equality vector \(w(\lambda)\), write \(F(\lambda)=H_{1n}\) and \(B(\lambda)=H_{n1}\). Substitution gives
\[
 F(\lambda)-B(\lambda)=S(\lambda)G(\lambda)=\frac{d}{d\lambda}S(\lambda)^2.
\]
If \(\lambda_*\in(0,1)\), this difference is zero, so \(F=B=S(\lambda_*)^2\). At \(\lambda_*=0\), the one-sided maximizing condition is \(G(0)\leq0\), hence \(F\leq B=S(0)^2\); at \(\lambda_*=1\), \(G(1)\geq0\), hence \(B\leq F=S(1)^2\). In every case \(w(\lambda_*)\) attains the universal lower bound in Step 2 and is therefore globally optimal.

**Step 4: Uniqueness, mass cancellation, and the three-state frontier.** If another feasible vector attained the same minimax value, it would attain equality in Step 2 at \(\lambda_*\), whose strictly positive Cauchy equality condition forces \(w=w(\lambda_*)\). At \(\lambda=1/2\), each \(a_i=1/2\), so \(G(1/2)=\sqrt{2}\sum_i\sqrt{c_i}(2P_i-1)\). Under the displayed cancellation condition it vanishes and the formulas simplify as stated; reflection symmetry pairs \(P_i\) with \(1-P_{n-i}\) and \(c_i\) with \(c_{n-i}\). In the specified three-state example \(P_1=1/4\), \(P_2=3/4\), and the interior stationary equation reduces to \(\lambda_*=(3c_2-c_1)/(2(c_1+c_2))\). This belongs to \([0,1]\) exactly when \(1/3\leq c_1/c_2\leq3\); in that region equality of \(a_1/c_1\) and \(a_2/c_2\) yields the equal conductances. Outside it, insert \(\lambda_*=0\) or \(1\) into the sharp bound to obtain the two stated square-root formulas. This completes the proof.

## Verification

The standalone Python standard-library file `verify.py` performs separate exact-rational Poisson-system solves for finite cases, checking that the maximum across all ordered hitting times equals the two endpoint formulas. It also checks the one-parameter optimum, budget, equalization or endpoint regime, and feasible random perturbations. The check performed before compilation produced: `VERIFY_OK 220 independent exact generator/hitting-time cases; 5940 ordered hitting entries; 800 arbitrary-mass/price optimizer cases; 8000 feasible perturbations; eight exact three-state phase probes`. A checker is a finite consistency test, not a proof of the theorem for every \(n\), price vector, or stationary distribution; those quantifiers follow from Steps 1–4. Reproduce with `python3 verify.py` from an extraction of the embedded files.

## Relationship to prior work

The exact fixed-chain hitting-time identities, electrical viewpoints and birth-and-death formulations are antecedents, not new claims. In particular, Palacios–Gómez–Del Río (2014), Corollary 6, treats hitting times of a given linear-graph random walk via voltages; Palacios–Quiroz (2016), Theorem 1 and Sections 2–4, computes stationary distributions and hitting times for prescribed finite-tree walks. Aldous–Fill discusses extremal hitting/commute-time characterizations for fixed reversible chains. Ghosh–Boyd–Saberi (2008) optimizes total effective resistance, equivalently an averaged commute-time objective, and lists minimum maximum *effective resistance* as another convex program; its conference-version path allocation and objectives are not the maximum **directed** hitting time under independently fixed stationary masses and nonuniform prices. Their objectives differ from the present choice of *conductances*, at *fixed independently prescribed stationary masses and prices*, to *minimize the largest directed mean hitting time*, including the boundary-balanced dual formula and exact three-state price transition. The classical fixed-chain formulas are entirely compatible with—and used as background for—the present reduction. The related 1996 paper of Palacios–Tetali could only be checked through its abstract and secondary citations; its full text has not been cleared for complete comparison. A matching older specialization elsewhere is possible.

## Limitations

The result is restricted to paths, prescribed positive stationary masses, unconstrained continuous-time jump rates, positive linear edge prices, and the worst *mean* directed hitting time. It does not optimize discrete-time chains with per-state departure-rate bounds, general trees or graphs, worst hitting-time tails, commute-time objectives, or spectral gaps. No claim of exhaustive historical novelty, independent auditing, or universal computational certification is made. Full-text inspection of one closely related 1996 source was unavailable; the residual prior-art risk should be reassessed before external priority claims.

## References

1. J. L. Palacios, E. Gómez and M. Del Río, “Hitting Times of Walks on Graphs through Voltages,” *Journal of Probability* (2014), article 852481, first published 2014-05-20, DOI 10.1155/2014/852481. Full article: https://onlinelibrary.wiley.com/doi/full/10.1155/2014/852481.
2. J. L. Palacios and D. Quiroz, “Birth and death chains on finite trees: computing their stationary distribution and hitting times,” *Methodology and Computing in Applied Probability* 18 (2016), 487–498, DOI 10.1007/s11009-014-9436-1. Author-accepted full text: https://eprints.lse.ac.uk/66937/1/Quiroz_Birth%20and%20death.pdf.
3. D. Aldous and J. Fill, *Reversible Markov Chains and Random Walks on Graphs*, unfinished monograph, particularly Chapters 3, 4 and 5; https://www.stat.berkeley.edu/~aldous/RWG/book.pdf.
4. J. L. Palacios and P. Tetali, “A Note on Expected Hitting Times for Birth and Death Chains,” *Statistics & Probability Letters* 30 (1996), 119–125, DOI 10.1016/0167-7152(95)00209-X. Full text not inspected.

5. A. Ghosh, S. Boyd and A. Saberi, “Minimizing Effective Resistance of a Graph,” *SIAM Review* 50 (2008), 37–66, DOI 10.1137/050645452, published online 2008-02-01. Earlier conference version: https://web.stanford.edu/~boyd/papers/pdf/eff_res_mtns06.pdf; see its Sections I, VI and VII (total resistance, examples on paths, and maximum effective resistance as a separate extension).
