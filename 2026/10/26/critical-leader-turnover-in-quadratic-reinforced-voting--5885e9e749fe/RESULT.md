# Critical leader turnover in quadratic reinforced voting

## Finding

Consider the following voting chain, with a fixed integer population size \(n\ge 2\). Initially each of the \(n\) labeled candidates holds one vote: \(X_0=(1,\ldots,1)\). Conditional on \(X_{t-1}\), the vector \(X_t\) is multinomial with \(n\) trials and probabilities
\[
 p_{t,i}=\frac{(X_{t-1}^{(i)})^2}{\sum_{j=1}^{n}(X_{t-1}^{(j)})^2},\qquad 1\le i\le n.
\]
Let \(M_n=\max_iX_1^{(i)}\), let \(\mathcal L_1=\{i:X_1^{(i)}=M_n\}\), and let \(\mathcal L_2=\{i:X_2^{(i)}=\max_jX_2^{(j)}\}\), retaining **all** maximizers in case of ties. Then, along the entire integer sequence \(n\to\infty\),
\[
 \boxed{\Pr\!\left(\max_{i\in\mathcal L_1}X_2^{(i)}
       <\max_{i\notin\mathcal L_1}X_2^{(i)}\right)\longrightarrow 1.}
\]
In particular, \(\Pr(\mathcal L_1\cap\mathcal L_2=\varnothing)\to1\).

The source study of this voting chain states, for this boundary parameter, that the eventual unanimous winner \(\mathcal W\) belongs to \(\mathcal L_2\) with probability \(1-o(1)\) [1, Section 1.3]. **Combined with that published containment statement**, the strict-turnover theorem gives
\[
 \boxed{\Pr(\mathcal W\in\mathcal L_1)\longrightarrow0.}
\]
This addresses the first critical reinforcement exponent (quadratic reinforcement), for which the published open-problem discussion leaves first-round winner containment unresolved [1, Section 1.3].

## Assumptions and scope

All rounds use simultaneous multinomial resampling and fixed population size \(n\). Every candidate initially has one vote. The reinforcement exponent is **exactly** \(2\); there are no mutations, exogenous arrivals or candidate-specific weights. The assertions concern probability under the whole chain, not conditioning on a unique first-round leader; ties are handled as sets. The strict-turnover theorem is proved directly below. The winner statement imports only the specific second-round containment statement identified in [1]. No rate of convergence uniform in a varying reinforcement exponent is claimed.

For the proof write \(U_j=\#\{i:X_1^{(i)}=j\}\), \(Q=\sum_i(X_1^{(i)})^2\), and choose the unique integer \(m=m(n)\) with \(m!\le n<(m+1)!\). Put \(u=n/m!\), so \(1\le u<m+1\), and \(m\to\infty\).

## Proof

**Step 1: Uniform occupancy near the largest load.** The first vote vector comes from placing \(n\) independent uniform balls in \(n\) labeled boxes. For every integer \(j=O(m)\), uniformly in the range \(m-2\le j\le m+1\),
\[
 \begin{aligned}
 \mathbb E U_j&=n{n\choose j}n^{-j}(1-1/n)^{n-j}
   =\frac{n}{e\,j!}\bigl(1+O(m^2/n)\bigr),\\
 \mathbb E(U_j)_2&=n(n-1)\frac{n!}{j!^2(n-2j)!}
   n^{-2j}(1-2/n)^{n-2j}
   =\left(\frac{n}{e\,j!}\right)^2\bigl(1+O(m^2/n)\bigr).
 \end{aligned}
\]
Here \((a)_2=a(a-1)\); the error estimates follow by finite-product expansion, since \(m^2/n\to0\). Consequently \(\operatorname{Var}(U_j)/(\mathbb E U_j)^2\le (\mathbb E U_j)^{-1}+O(m^2/n)\), so \(U_j/\mathbb E U_j\to1\) in probability whenever its mean diverges.

In particular, simultaneously with probability \(1-o(1)\),
\[
 U_{m-1}\ge \frac{um}{3e},\qquad
 U_{m-2}\ge \frac{um(m-1)}{3e},\qquad
 U_j\le\frac{n\log m}{j!}\quad(m-2\le j\le m+1).
\]
The lower bounds use the divergent means; the upper bounds follow by Markov and a union bound. Furthermore, by the binomial factorial-moment inequality,
\[
 \Pr(M_n\ge m+2)\le \frac{n}{(m+2)!}\le\frac1{m+2}\longrightarrow0.
\]
Thus \(M_n\in\{m-1,m,m+1\}\) with high probability. If \(u<\sqrt m\), then \(\Pr(U_{m+1}>0)\le\mathbb E U_{m+1}=O(u/m)=o(1)\). If \(u\ge\sqrt m\), the same factorial-moment estimate gives \(U_m\ge u/(3e)\) with high probability. These conclusions hold uniformly over the possible dependence of \(u\) on \(n\).

Let \(M=M_n\), \(R=U_M\) and \(S=U_{M-1}\). The three cases \(M=m-1,m,m+1\) in the preceding bounds give, for an absolute \(c_0>0\),
\[
 1\le R,\quad S\ge \frac{c_0m}{\log m}R,
 \qquad R+S\le m^4
 \tag{1}
\]
with probability \(1-o(1)\). For the last case \(M=m+1\), use the lower bound on \(U_m\) when \(u\ge\sqrt m\); the other regime has vanishing probability of \(M=m+1\). Notice that (1) does **not** assume the top load is unique.

**Step 2: Normalization and independent Poisson approximation.** Writing \(C=\sum_{1\le a<b\le n}\mathbf1\{\text{balls }a,b\text{ have the same destination}\}\), we have \(Q=n+2C\). The indicators in \(C\) are pairwise independent even when the ball pairs overlap, and each has mean \(1/n\). Therefore
\[
 \mathbb EQ=2n-1,\qquad
 \operatorname{Var}(Q)=4{n\choose2}\frac1n\left(1-\frac1n\right)=O(n),
\]
so \(Q/n\to2\) in probability. Conditional on the first-round vector, the second-round count of candidate \(i\) has multinomial cell weight \((X_1^{(i)})^2/Q\).

Let \(J=\{i:X_1^{(i)}\in\{M,M-1\}\}\). On the high-probability event (1), its total vote probability \(p_J\) satisfies
\[
 p_J\le\frac{(R+S)M^2}{n}\le\frac{(m+1)^2m^4}{n}.
\]
The conditional second-round cell-count vector indexed by \(J\) differs in total variation from **independent** Poisson variables with respective means \(n(X_1^{(i)})^2/Q\) by at most \(np_J^2\). This follows by conditioning both laws on their total over \(J\): those totals are respectively \(\operatorname{Bin}(n,p_J)\) and \(\operatorname{Poi}(np_J)\), and the conditional allocation to cells agrees. The elementary Poisson approximation bound gives the stated estimate, which is \(O(m^{12}/n)=o(1)\).

The approximating variables for the \(R\) leading first-round candidates have mean
\[
 \mu=\frac{nM^2}{Q},
\]
while the \(S\) candidates one first-round vote behind have mean
\[
 \nu=\frac{n(M-1)^2}{Q}.
\]
On the same high-probability event, \(\mu,\nu\asymp m^2\), \(\mu-\nu=O(m)\), and \(\mu/\nu=1+O(1/m)\).

**Step 3: The crowd of runners-up overtakes the original leaders.** Conditional on the first round, set
\[
 L=\log R+\tfrac14\log m,\qquad
 T=\left\lceil\mu+\sqrt{2\mu L}\right\rceil.
\]
By (1), \(\tfrac14\log m\le L\le\tfrac{17}{4}\log m\). The standard Poisson Chernoff inequality gives, uniformly under these conditions,
\[
 R\Pr\bigl(\operatorname{Poi}(\mu)\ge T\bigr)
 \le R\exp\bigl(-L+o(1)\bigr)
 =m^{-1/4+o(1)}\longrightarrow0. \tag{2}
\]
Here the uniform \(o(1)\) in the exponent follows by expanding the Poisson rate function: \(\sqrt{\mu L}=O(m\sqrt{\log m})\) and \(L^{3/2}/\sqrt\mu=o(1)\).

For the lower group, put \(z=(T-\nu)/\sqrt\nu\). The relations above yield \(z=\sqrt{2L}+O(1)\) uniformly. A Poisson moderate-deviation **lower** bound, derived directly from Stirling's formula by summing \(\lfloor\sqrt\nu/(1+z)\rfloor\) consecutive masses beginning at \(T\), gives
\[
 q:=\Pr\bigl(\operatorname{Poi}(\nu)\ge T\bigr)
 \ge \exp\bigl(-L-O(\sqrt{\log m})\bigr). \tag{3}
\]
For completeness, Stirling gives each mass in this short interval a lower bound \(c\nu^{-1/2}\exp(-z^2/2-O(1))\), uniformly because \(z=O(\sqrt{\log m})=o(\nu^{1/6})\); multiplying by the interval length establishes (3), with its logarithmic prefactor absorbed into \(O(\sqrt{\log m})\).

Combining (1) and (3),
\[
 Sq\ge\frac{c_0mR}{\log m}
 \exp\left(-\log R-\tfrac14\log m-O(\sqrt{\log m})\right)
 =m^{3/4-o(1)}\longrightarrow\infty. \tag{4}
\]
For the independent Poisson approximation, (2) says every original leader is **below** \(T\) with probability \(1-o(1)\), while (4) says at least one candidate from the \(M-1\) group is **at or above** \(T\) with probability \(1-o(1)\). The vanishing conditional total-variation error transfers these statements to the true multinomial second round. Removing the high-probability conditioning events proves the strict-turnover limit.

Finally, a strict second-round victory by some candidate outside \(\mathcal L_1\) implies \(\mathcal L_1\cap\mathcal L_2=\varnothing\). The stated winner corollary follows by the union bound with \(\Pr(\mathcal W\notin\mathcal L_2)=o(1)\) from [1, Section 1.3]. \(\square\)

## Verification

Run the self-contained standard-library script `verify.py` with Python 3. It checks exact occupancy means and factorial second moments by exhaustive labeled-ball enumeration for \(2\le n\le5\), checks the conditional quadratic multinomial formula by finite exact fractions for \(2\le n\le4\), and evaluates selected finite Poisson-tail comparisons. The infinite statement is established by the occupancy, Poissonization and moderate-deviation arguments above, **not** by these finite checks. An illustrative finite case is \(\Pr(\max_{X_1=M-1}X_2>\max_{X_1=M}X_2)=26/375\) for \(n=3\); finite probabilities need not yet be close to one.

## Relationship to prior work

Benjamini, Cai, Chen, Gong and Li [1] introduced this chain, proved winner predictability away from the boundary exponents, and explicitly singled out the critical exponent \(\alpha=2^{1/k}\) as an open winner-identification regime. Their Section 1.3 states a second-round winner-containment consequence at the critical value \(\alpha=2\) and conjectures loss of first-round winner containment. The strict second-round turnover proved here is not implied by the off-critical theorem: it exploits a competition between the size of the first-round near-maximal occupancy **class** and its order-statistic fluctuations after quadratic resampling. The proof additionally handles first-round ties and every integer population size rather than a special factorial subsequence.

Published works on nonlinear urn reinforcement and strong-selection Wright–Fisher models [2,3] concern different reinforcement timing or allele-selection structures. Their abstract-level statements do not imply this strict two-round comparison. The exact novelty assessment is limited by possible earlier results expressed as extrema of reweighted occupancy fields.

## Limitations

The result is asymptotic with no practical finite-size onset guarantee; the convergence can be extremely slow as \(n\to\infty\). It treats only exponent \(2\), not the other critical exponents \(2^{1/k}\), and does not prove uniqueness of a second-round leader. The winner corollary relies on the second-round containment conclusion **stated** by [1] and does not reconstruct that study's whole proof. No independent audit or external validation has been performed.

## References

[1] I. Benjamini, Z. Cai, G. Chen, S. Gong, Z. Li, *The Conclave Process*, arXiv:2607.22324, first public version 24 July 2026, especially Definition 1.1, Theorem 1.6 and Section 1.3 (critical-exponent discussion). https://arxiv.org/abs/2607.22324 ; https://arxiv.org/html/2607.22324

[2] M. Costa and J. Jordan, *Phase transitions in non-linear urns with interacting types*, Bernoulli 28 (2022), 2546–2562. https://eprints.whiterose.ac.uk/id/eprint/193934/

[3] F. Boenkost, A. González Casanova, C. Pokalyuk and A. Wakolbinger, *Haldane's formula in Cannings models: The case of moderately weak selection*, arXiv:1907.10049 (2019). https://arxiv.org/abs/1907.10049
