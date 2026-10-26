# Later completion favors rarer final coupons in strict likelihood-ratio order

## Finding

Let \(m\ge2\) distinct coupon types be sampled independently with fixed probabilities \(p_1,\ldots,p_m>0\), \(\sum_i p_i=1\). Write \(N\) for the first draw index at which every type has occurred and \(L\) for the type first seen at draw \(N\). For any two different types \(i,j\) with \(p_i<p_j\), the posterior odds
\[
R_{ij}(n)=\frac{\Pr(L=i\mid N=n)}{\Pr(L=j\mid N=n)}
=\frac{\Pr(N=n,L=i)}{\Pr(N=n,L=j)}
\]
are **strictly increasing** for every integer \(n\ge m\):
\[
R_{ij}(n+1)>R_{ij}(n),\qquad R_{ij}(m)=1.
\]
For \(p_i=p_j\), the odds are identically one. Equivalently, the conditional completion time \(N\mid L=i\) is strictly larger than \(N\mid L=j\) in monotone likelihood-ratio order when \(p_i<p_j\). Consequently the corresponding usual stochastic ordering holds. The assertion has no restriction on the other probabilities.

## Assumptions and scope

Draws are iid categorical on exactly \(m\) categories, all masses strictly positive and fixed across time. The first-appearance process stops when all categories have been seen once; the last draw is the first appearance of exactly one type. The statement concerns the discrete-time draw count \(N\), not a Poissonized continuous-time completion clock, coupon multiplicities, or dependent draws. Both conditional laws have strictly positive mass at each integer \(n\ge m\).

## Proof

**Exact joint law.** Define \(g_q(z)=e^{qz}-1\). If the final newly observed type is \(i\) at draw \(n\), the first \(n-1\) draws must avoid \(i\) and include all other types. Weighted multinomial enumeration gives
\[
J_i(n):=\Pr(N=n,L=i)
=p_i(n-1)![z^{n-1}]\prod_{h\ne i}g_{p_h}(z),\qquad n\ge m.
\]
Every factor has positive coefficients from degree one onward, so \(J_i(n)>0\). At \(n=m\) each of the \((m-1)!\) orders of the other types contributes \(\prod_h p_h\); thus \(J_i(m)=(m-1)!\prod_h p_h\), independent of \(i\).

**Log-concavity lemma.** A nonnegative sequence supported on an integer interval is log-concave when \(c_k^2\ge c_{k-1}c_{k+1}\). Equivalently, its infinite Toeplitz matrix \(T_c(r,s)=c_{r-s}\), with coefficients set to zero off support, has every \(2\)-by-\(2\) minor nonnegative. To see the equivalence, ratios of consecutive positive coefficients decrease, which gives every such minor; adjacent minors give the converse. Products of Toeplitz matrices correspond to sequence convolution. The Cauchy--Binet expansion of any two-row minor of a product is a finite sum of products of nonnegative minors (all relevant coefficient sums are locally finite). Therefore convolution preserves log-concavity and interval support. Each sequence \(\bigl(q^k/k!\bigr)_{k\ge1}\), extended by zero for \(k<1\), is log-concave because its successive ratio is \(q/(k+1)\). Hence for fixed distinct \(i,j\), the coefficient sequence
\[
 c_t=[z^t]\prod_{h\notin\{i,j\}}g_{p_h}(z)
\]
is nonnegative, log-concave, zero below \(r=m-2\), and strictly positive at every \(t\ge r\). For \(m=2\), interpret the empty product as \(c_0=1\), \(c_t=0\) otherwise.

**Likelihood-ratio comparison.** Suppose \(p_i<p_j\). Write \(a_u=p_j^u/u!\) and \(b_u=p_i^u/u!\) for \(u\ge1\), zero otherwise; then \(a_u/b_u=(p_j/p_i)^u\) increases strictly in \(u\). Put \(A_k=(c*a)_k\) and \(B_k=(c*b)_k\), for \(k\ge m-1\). The joint formula gives \(J_i(k+1)/J_j(k+1)=(p_i/p_j)A_k/B_k\). Expanding and pairing the terms with \(u>v\) gives the exact determinant identity
\[
A_{k+1}B_k-A_kB_{k+1}=
\sum_{u>v\ge1}(a_u b_v-a_v b_u)
\bigl(c_{k+1-u}c_{k-v}-c_{k-u}c_{k+1-v}\bigr).
\]
All sums are finite because \(c\) vanishes at negative indices. The first factor is positive. The second is nonnegative by the decreasing-ratio characterization of log-concavity of \(c\), including support-boundary cases. Thus \(A_{k+1}/B_{k+1}\ge A_k/B_k\).

For \(m\ge3\), put \(r=m-2\) and choose \(u=k-r+1\), \(v=1\) for any \(k\ge m-1=r+1\). Then \(u>v\), and the second factor is exactly \(c_r c_{k-1}>0\) because \(c_{r-1}=0\). This single term proves strict positivity of the whole determinant. For \(m=2\), \(A_k/B_k=a_k/b_k=(p_j/p_i)^k\), also strictly increasing. Equal probabilities yield \(a=b\), giving constant odds one by symmetry. This proves the stated pairwise posterior-odds theorem for every \(m\ge2\) and \(n\ge m\).

**Conditional likelihood-ratio order.** Write \(f_i(n)=\Pr(N=n\mid L=i)=J_i(n)/\Pr(L=i)\). The ratio \(f_i(n)/f_j(n)\) differs from \(R_{ij}(n)\) only by a positive constant, so it increases strictly. Standard summation or a single-crossing argument then implies the usual stochastic order for these conditional laws. No assertion of independence between \(N\) and \(L\) is made.

## Verification

A standalone `verify.py` evaluates the generating-function coefficient formula and, independently, a finite-state dynamic program enumerating draw histories. Both use Python exact rational arithmetic. It checks vectors \((1,2)\), \((1,2,5)\), \((1,1,3)\), \((1,2,3,5)\), \((1,1,3,10)\), \((2,3,4,7)\), and \((1,2,3,10,30)\), normalized to probabilities, for all supported \(n\le22\). Every exact mass comparison and all strict odds comparisons pass. For the probabilities \((1,2,5)/8\), the odds of type one rather than type two being last are \(R_{12}(3)=1\), \(R_{12}(4)=7/6\), and \(R_{12}(5)=88/67\). Run `python verify.py`. The infinite theorem depends on the preceding proof, not on these finite computations.

## Relationship to prior work

Boneh and Hofri's 1989 report treats the nonuniform coupon collector through generating functions and completion-time calculations. Brown, Peköz, and Ross (2008), Proposition 1(f), give an inclusion--exclusion formula for the joint law of completion time and final coupon, and Section 4 develops a simulation method for the conditional tail of \(N\) given \(L\). Aki and Hirano (2012 online; 2013 print), especially their Section 2 and equations (5), (8), derive joint waiting-time and arrival-rank laws; the likelihood-ratio *test* in that paper compares parameter hypotheses, not the monotone-likelihood-ratio *ordering* of completion times across last-coupon identities proved here. Anceaume, Busnel, and Sericola's 2014 preprint studies arbitrary-probability completion distributions using a Markov-chain representation. These works supply exact distributional foundations; the present assertion establishes the strict pairwise monotonicity of the conditional laws under every nonuniform probability vector, by using log-concavity of the positive-coefficient joint law. The formula in Brown et al. is compatible with the theorem, but without the structural convolution argument it does not state or immediately provide its global inequality.

## Limitations

This is a pairwise ordering of conditional discrete completion times, not a claim that every posterior probability \(\Pr(L=i\mid N=n)\) increases separately when there are more than two types. Because odds for a type relative to both rarer and commoner types move in opposite directions, the middle types can have nonmonotone marginal posteriors. The result requires strictly positive iid type probabilities and first-occurrence completion, and does not directly cover time-varying, reinforcement, group draws, or coupon quotas. Published formulae for the entire joint distribution overlap in ingredients; historical priority for the particular strict likelihood-ratio inequality has not undergone independent confirmation.

## References

- A. Boneh and M. Hofri, *The Coupon-Collector Problem Revisited*, Purdue Computer Science Technical Report 90-952, first public report dated 1989-05-01. https://docs.lib.purdue.edu/cstech/807/
- M. Brown, E. A. Peköz, and S. M. Ross, *Coupon Collecting*, Probability in the Engineering and Informational Sciences **22** (2008), 221--229, doi:10.1017/S0269964808000132. Full author-uploaded text: https://www.researchgate.net/publication/228916314_Coupon_collecting
- S. Aki and K. Hirano, *Coupon collector's problems with statistical applications to rankings*, Annals of the Institute of Statistical Mathematics **65** (2013), 571--587, online 2012-11-15, doi:10.1007/s10463-012-0382-9. https://www.ism.ac.jp/editsec/aism/pdf/10463_2012_Article_382.pdf
- E. Anceaume, Y. Busnel, and B. Sericola, *New Results on a Generalized Coupon Collector Problem Using Markov Chains*, arXiv:1402.5245, first submitted 2014-02-21. https://arxiv.org/abs/1402.5245
