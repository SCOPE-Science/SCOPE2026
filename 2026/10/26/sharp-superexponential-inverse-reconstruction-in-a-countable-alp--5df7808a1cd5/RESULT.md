# Sharp superexponential inverse reconstruction in a countable-alphabet cellular automaton

## Finding
Let \(B=\mathbb N_0\times\mathbb F_2\), with discrete alphabet topology, and define the one-sided nearest-neighbor cellular automaton \(T:B^{\mathbb Z}\to B^{\mathbb Z}\) by
\[
 T(r,u)_i=\bigl(r_i,\,u_i\oplus {\bf1}_{\{r_i=r_{i+1}+1\}}u_{i+1}\bigr).
\]
The map is bijective, but its inverse has no finite memory set. Give the ranks \((r_i)\) any iid law \(p=(p_n)_{n\ge0}\) and the input data bits independent fair Bernoulli laws. Then \(T\) preserves this product probability measure. Among **all** maps that reconstruct the inverse data bit at site zero from the output symbols in the symmetric window \([-R,R]\), for every integer \(R\ge0\), the smallest possible error probability is
\[
 e_R^*(p)=\frac12\sum_{n=R+1}^{\infty}\prod_{j=0}^{R+1}p_{n-j}.
\]
A cellular-automaton truncation of the inverse attains this infimum. In particular, for the canonical geometric rank law \(p_n=(1-q)q^n\), \(0<q<1\),
\[
 \boxed{e_R^*(q)=\frac{(1-q)^{R+2}q^{(R+1)(R+2)/2}}{2(1-q^{R+2})}},
 \qquad
 \lim_{R\to\infty}\frac{\log e_R^*(q)}{R^2}=\frac12\log q<0.
\]
Thus the inverse is not a finite-memory cellular automaton, and no finite window reconstructs it almost surely under a full-support geometric law; nevertheless its **optimal** fixed-window reconstruction error decays superexponentially. For the canonical truncation, the almost-sure spatial frequency of reconstruction errors equals the displayed probability.

## Assumptions and scope
All configurations are indexed by \(\mathbb Z\), the rank alphabet is \(\mathbb N_0\), and addition \(\oplus\) is in \(\mathbb F_2\). A radius-\(R\) decoder may be any measurable function of the \(2R+1\) output symbols at indices \(-R,\ldots,R\); it need not itself be linear or a cellular automaton. Error is the probability that its predicted **data bit** differs from the data bit of \(T^{-1}\) at index zero when the output is sampled from the product law stated above. It is not an optimization over arbitrary joinings and is not asserted to equal Ornstein's \(\bar d\) distance. For arbitrary rank laws, zeros in \(p\) are permitted; the superexponential expression is specific to fixed \(0<q<1\).

## Proof
**1. Explicit inversion and nonuniformity.** Define \(a_i(r)={\bf1}_{\{r_i=r_{i+1}+1\}}\), and let \(L_i(r)\) be the largest \(k\ge0\) for which \(a_i\cdots a_{i+k-1}=1\), with an empty product equal to one. Each successful step reduces a nonnegative integer rank by exactly one, so \(0\le L_i\le r_i<\infty\). For \(T(r,u)=(r,v)\), repeated substitution (or cancellation of adjacent binary terms) gives the unique inverse
\[
 T^{-1}(r,v)_i=\left(r_i,\bigoplus_{j=0}^{L_i(r)}v_{i+j}\right).
\]
Indeed, the finite sum telescopes when \(v_j=u_j\oplus a_j u_{j+1}\), and conversely adjacent finite sums cancel to recover each \(v_i\). Inverse continuity holds pointwise for the product of discrete topologies: inspect the finite ranks through the first failure of the descending-rank condition and the data bits through the last successful site. However, for every \(R\) there are rank configurations with \((r_0,\ldots,r_{R+1})=(R+1,R,\ldots,0)\), so changing only \(v_{R+1}\) changes the inverse data bit at zero without changing the window \([-R,R]\). Hence no uniform finite memory exists.

**2. Invariance of the product probability.** Fix any rank configuration. On the compact data group \((\mathbb F_2)^{\mathbb Z}\), the data transformation \(u\mapsto v\) is a continuous group homomorphism with the continuous inverse just derived. It is therefore a compact-group automorphism, preserving its Haar measure, the iid fair-bit product. Since the ranks are unchanged, conditioning on arbitrary iid ranks shows that \(T\) preserves the joint product law. In particular, conditioned on ranks, all output data bits are independent and fair.

**3. The optimal local Bayes decision.** Given \((r_j,v_j)_{-R\le j\le R}\), use the truncated parity
\[
 D_R(r,v)=\bigoplus_{j=0}^{\min\{L_0(r),R\}}v_j.
\]
This is computable from the window: run the successive rank tests through index \(R\), stopping at the first observed failure or at \(R\). If \(L_0\le R\), the target bit is exactly \(D_R\). If \(L_0\ge R+1\), the target is \(D_R\oplus v_{R+1}\oplus\) a parity of possibly further bits. Conditional on the ranks and all observations in \([-R,R]\), the unseen \(v_{R+1}\) is an independent fair bit; hence on the continuation event the target is unbiased. The continuation probability conditional on the local observations is between zero and one and depends only on the ranks: it is zero if the observed descending path has already terminated, and otherwise equals \(p_{r_R-1}\) if \(r_R\ge1\). Thus the conditional probability that the true inverse bit differs from \(D_R\) is exactly half the conditional continuation probability, at most \(1/2\). No alternative local decision rule can decrease the conditional error. Consequently
\[
 e_R^*(p)=\mathbb P(D_R\ne T^{-1}(r,v)_0^{\rm bit})=\frac12\mathbb P(L_0\ge R+1).
\]
For each fixed rank sequence, a discrepancy can arise only after an unseen independent fair bit, which also proves the displayed equality without invoking any approximation to the infinite inverse.

**4. Exact rank tail.** The event \(L_0\ge k\) is the disjoint union, over integers \(n\ge k\), of the events \(r_0=n,r_1=n-1,\ldots,r_k=n-k\). By independence,
\[
 \mathbb P(L_0\ge k)=\sum_{n=k}^\infty\prod_{j=0}^k p_{n-j}.
\]
For \(p_n=(1-q)q^n\), summing the resulting geometric series yields
\[
 \mathbb P(L_0\ge k)=\frac{(1-q)^{k+1}q^{k(k+1)/2}}{1-q^{k+1}}.
\]
Take \(k=R+1\) to obtain the claimed sharp error. Its logarithm is \(\tfrac12(R+1)(R+2)\log q+(R+2)\log(1-q)-\log[2(1-q^{R+2})]\), proving the limit. For each fixed geometric law, the error is strictly positive at every finite radius.

**5. Spatial error frequency.** Both the original product law and the output product law are Bernoulli shifts; the latter is shift-ergodic. The sitewise disagreement of \(D_R\) and the true inverse is a bounded measurable shift-covariant observable. Birkhoff's ergodic theorem gives an almost-sure limiting frequency equal to its expectation \(e_R^*(p)\). This is a statement about the canonical truncation, not an assertion of pointwise optimization for every individual output realization.

## Verification
The standalone script `CHECK.py` verifies by exhaustive exact binary operations the forward/inverse identities on \(32{,}768\) five-site rank/data configurations with ranks at most three. It independently checks exact finite-support descending-rank tail formulas for three rational geometric parameters and multiple depths. It also computes exact Bayesian posterior masses, enumerating all input rank and fair output-bit configurations on four sites for radius zero, one, and two; the computed optimal errors agree with half the independently evaluated continuation probabilities. The recorded output is `CHECK_OUTPUT.txt` and ends in `CHECKS_PASS`. The general theorem rests on the mathematical proof, not these finite enumerations.

## Relationship to prior work
The rank-decreasing, pointwise-nilpotent triangular construction is a one-dimensional specialization of the mechanism in Jiang Yang, *A Reversibility Characterization of Locally Finite Groups by Cellular Automata* (arXiv:2606.29958, first public version June 29, 2026), especially Section 4. **The bijectivity, the finite pointwise inverse formula, and nonreversibility are not asserted to be new.** The contribution here is the sharp stochastic fixed-window inverse reconstruction law, its geometric-rank closed form and superexponential scale, and the optimality over nonlinear and two-sided decoders. Earlier work of Ceccherini-Silberstein and Coornaert provides infinite-dimensional linear nonreversible examples, without this Bernoulli-rank inverse-risk calculation. General finitary-coding literature addresses existence and coding-radius tails in other models, not this exact Bayes-optimal formula.

## Limitations
The result considers fair independent data bits and independent ranks. It does not establish an optimal rate for biased, correlated or spatially dependent data, and does not claim a universal bound across all nonreversible cellular automata or distributions. It is an exact same-input prediction theorem, not a \(\bar d\) transport theorem. Priority under alternative finitary-coding terminology requires further independent literature assessment. No independent scientific validation has been performed.

## References
1. J. Yang, *A Reversibility Characterization of Locally Finite Groups by Cellular Automata*, arXiv:2606.29958 (first public June 29, 2026), Section 4. https://arxiv.org/abs/2606.29958
2. T. Ceccherini-Silberstein and M. Coornaert, *On the reversibility and the closed image property of linear cellular automata*, arXiv:0910.0863, Theoretical Computer Science 412 (2011), 300–306, especially Section 5. https://arxiv.org/abs/0910.0863
3. J. Campos, N. Romero and R. Vivas, *On the image set and reversibility of shift morphisms over discrete alphabets*, Revista de la Unión Matemática Argentina 63 (2022), doi:10.33044/revuma.1795.
4. N. Harvey, A. E. Holroyd, Y. Peres and D. Romik, *Universal finitary codes with exponential tails*, Proceedings of the London Mathematical Society 94 (2007), 475–496, doi:10.1112/plms/pdl018.
