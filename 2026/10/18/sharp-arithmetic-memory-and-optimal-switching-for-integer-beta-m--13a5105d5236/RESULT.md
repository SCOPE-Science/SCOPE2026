# Sharp arithmetic memory and optimal switching for integer beta maps

## Finding

Consider independent random compositions of integer beta transformations. Their stationary correlations for the centered indicator of a rational left-endpoint cell admit an exact finite-state rational generating function. There is a sharp arithmetic criterion for the entire observable covariance to vanish after finitely many steps. For switching between the doubling and tripling maps, the first-sixth-cell covariance instead decays exponentially at an exactly optimizable rate: the unique best switching probability is \(2/5\), giving correlation rate \(1/5\), strictly faster than either deterministic map.

More precisely, let \(S\subset\{2,3,\ldots\}\) be finite and nonempty and assign positive probabilities \(\pi_b\) summing to one. Independently sample \(B_t\in S\) and \(X_0\) uniformly from \([0,1)\), and set \(X_{t+1}=\{B_tX_t\}\). Fix an integer \(q\ge2\) and put
\[
H_q(x)={\bf1}_{[0,1/q)}(x)-1/q,\qquad C_q(n)=\mathbb E[H_q(X_0)H_q(X_n)],\quad n\ge0.
\]
Define the \(q\times q\) matrix \(L\), indexed by residues \(r,s\in\{0,\ldots,q-1\}\), and column \(d\) by
\[
L_{r,s}=\sum_{\substack{b\in S\\ br\equiv s\pmod q}}\frac{\pi_b}{b},\qquad d_0=0,\quad d_r=q-r\quad(1\le r<q).
\]
With \(e_1\) the row selector at residue one, the complete covariance generating function is
\[
\boxed{\sum_{n\ge0}C_q(n)z^n=\frac1{q^2}e_1(I-zL)^{-1}d.}
\]
Every \(C_q(n)\) is nonnegative. It is zero exactly when \(q\) divides every length-\(n\) product from \(S\). For each prime \(\ell\mid q\), write \(a_\ell=v_\ell(q)\) and \(m_\ell=\min_{b\in S}v_\ell(b)\). If some \(m_\ell=0\), then \(C_q(n)>0\) for every \(n\ge0\). Otherwise the **least** vanishing time is
\[
\boxed{N_q=\max_{\ell\mid q}\left\lceil\frac{a_\ell}{m_\ell}\right\rceil,\qquad C_q(n)>0\ (n<N_q),\quad C_q(n)=0\ (n\ge N_q).}
\]
For the two maps \(T_2,T_3\) with selection probability \(p\) for \(T_2\), \(1-p\) for \(T_3\), and \(q=6\), write \(\alpha_n=4\) for odd \(n\) and \(\alpha_n=2\) for even \(n\). For every \(p\in[0,1]\) and integer \(n\ge1\),
\[
\boxed{C_6(n)=\frac{\alpha_n(p/2)^n+3((1-p)/3)^n}{36},\qquad C_6(0)=\frac5{36}.}
\]
For all \(p\in[0,1]\), the limit \(\rho(p)=\lim_{n\to\infty}C_6(n)^{1/n}\) exists and satisfies
\[
\boxed{\rho(p)=\max\{p/2,(1-p)/3\},\qquad \min_{0\le p\le1}\rho(p)=\rho(2/5)=1/5.}
\]
The minimizer is unique. At the optimum, \(C_6(n)=(\alpha_n+3)5^{-n}/36\) for \(n\ge1\). These claims concern this specified observable, not the mixing rate or independence of the entire process.

## Assumptions and scope

Lebesgue measure is normalized on \([0,1)\). The map choices are independent of each other and the initial point; expectations include both sources of randomness (annealed correlations). Integer multiplication is taken modulo one. Cell-boundary conventions are irrelevant because the starting state is absolutely continuous. In the general cutoff theorem all listed bases have strictly positive selection probabilities; the explicit two-base formula also allows endpoint probabilities by dropping the zero-probability map from the support.

## Proof

**Stationarity and reduction to one product.** Every integer map \(T_b:x\mapsto\{bx\}\), \(b\ge2\), preserves Lebesgue measure: the preimage of a measurable cell consists of \(b\) scaled translates. Composition of the selected maps equals \(T_{P_n}\), where \(P_n=\prod_{t=0}^{n-1}B_t\), with \(P_0=1\). Thus the process is stationary and \(C_q(n)=\mathbb E[J_q(P_n)]\) where \(J_q(B)=\int H_q(x)H_q(\{Bx\})\,dx\).

**Exact overlap lemma.** For integer \(B\ge1\), partition \([0,1)\) into the \(B\) branches \([j/B,(j+1)/B)\). In each branch the preimage of \([0,1/q)\) has length \(1/(qB)\). The intersection with \([0,1/q)\) comprises \(\lfloor B/q\rfloor\) full pieces, and, if \(B\not\equiv0\pmod q\), one further full preimage piece. Writing \(r=B\bmod q\), the resulting centered overlap is
\[
J_q(B)=\begin{cases}0,&r=0,\\[2pt](q-r)/(q^2B),&1\le r<q.\end{cases}
\]
At \(B=1\), this gives \(J_q(1)=(q-1)/q^2\), the variance of the indicator. The branch counting includes the boundary case \(q\mid B\) and requires no asymptotics.

**Finite-state formula.** Let \(v_n(r)=\mathbb E[P_n^{-1}{\bf1}_{\{P_n\equiv r\pmod q\}}]\). The independence of the next multiplier gives \(v_{n+1}=v_nL\) and \(v_0=e_1\). Therefore \(C_q(n)=q^{-2}v_nd=q^{-2}e_1L^nd\). Each row sum of \(L\) equals \(\sum_b\pi_b/b\le1/2\), so the geometric matrix series converges near zero (indeed for \(|z|<2\)), yielding the resolvent formula.

**Sharp cutoff.** By the overlap lemma and strict positivity of all word probabilities, \(C_q(n)=0\) if and only if all length-\(n\) base products are divisible by \(q\). If \(m_\ell=0\), repeating a base whose \(\ell\)-adic valuation is zero gives a word not divisible by \(q\) at every time. If all minima are positive, any word of length \(n\) has \(\ell\)-adic valuation at least \(n m_\ell\), hence is divisible by \(q\) for \(n\ge N_q\). Conversely, for \(n<N_q\), choose \(\ell\) with \(n m_\ell<a_\ell\) and repeat a base attaining that minimum; its product is not divisible by \(q\). This proves both the asserted least time and strict positivity beforehand.

**Two-base exact profile and optimum.** Fix \(q=6\). A product containing both a factor two and a factor three is divisible by six and contributes zero. For \(n\ge1\), the only contributing words are the all-two word, with probability \(p^n\) and product \(2^n\), and the all-three word, with probability \((1-p)^n\) and product \(3^n\). The remainder of \(2^n\) modulo six alternates between two and four, whereas the remainder of \(3^n\) is always three. The overlap lemma yields exactly the displayed \(C_6(n)\). Its two terms have strictly positive bounded periodic coefficients whenever their probabilities are positive, so the \(n\)-th root tends to the larger of \(p/2\) and \((1-p)/3\), including endpoint cases. The maximum of a strictly increasing and strictly decreasing affine function has its unique minimum at their crossing \(p/2=(1-p)/3\), namely \(p=2/5\) and \(\rho=1/5\). Nothing about the full observable space is inferred from this one correlation profile.

## Verification

The included `verify.py` performs exact-rational branch integration for 1,300 \((q,B)\) pairs, 220 independent word-versus-residue-matrix comparisons, 72 direct two-base comparisons, ten finite cutoff checks, and 208 preimage-measure checks. It prints the category counts and raises an exception on any mismatch. These finite checks support the formulas, but the proofs above—not the tests—establish all quantifiers and sharp boundaries.

## Relationship to prior work

Suzuki's 2023 preprint introduced and studied the same i.i.d. random beta-transformation family, including noninteger bases; it establishes invariant-density formulas and parameter-response results, not the displayed arithmetic cell-observable covariance, sharp decorrelation cutoff or switching-rate minimizer. Aimino–Nicol–Vaienti explicitly treat random integer beta maps in Example 7.3 and derive quenched central limit statements via a spectral gap; their stated result does not evaluate the present cell covariance or its optimized exponential rate. General random expanding-map correlation-decay estimates supply context, not the particular exact rational/arithmetical phase classification. The overlap-counting argument and finite-state matrix technique are elementary; the claim of contribution concerns their complete observable-specific classification and the sharp switching contrast, not invention of these techniques.

## Limitations

The covariance is annealed and pertains only to the centered indicator of \([0,1/q)\). Vanishing of that covariance does not imply independent observations, finite memory of the symbolic process, or zero correlation for every observable. The optimal \(p=2/5\) is specific to the first-sixth-cell indicator of the doubled/tripled system; it is not a general optimum for random-map mixing. Historical priority remains subject to further specialist literature review, particularly potential equivalent Fourier/transfer-operator calculations.

## References

1. Shintaro Suzuki, *Absolutely continuous invariant measures for random dynamical systems of beta-transformations*, arXiv:2303.17521, first public version 30 March 2023, later *Nonlinearity* **37** (2024), 065013. https://arxiv.org/abs/2303.17521
2. Romain Aimino, Matthew Nicol, and Sandro Vaienti, *Annealed and quenched limit theorems for random expanding dynamical systems*, arXiv:1310.4359, Example 7.3, https://arxiv.org/abs/1310.4359.
3. W. Bahsoun, C. Bose, and Y. Duan, *Decay of correlation for random intermittent maps*, 2013 (related qualitative random-map decay theory; a different class of intermittency-driven dynamics).
