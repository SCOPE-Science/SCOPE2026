# Sharp endpoint Rényi comparison for one-exceptional-weight Bernoulli sums

## Finding

Let \(n\ge1\) be an integer, let \(B_1,\ldots,B_{n+1}\) be independent fair Bernoulli variables, and let \(a\in\mathbb R\). Write
\[
S_{n,a}=B_1+\cdots+B_n+aB_{n+1},\qquad
K_{n,a}=|\operatorname{supp}(S_{n,a})|,\qquad
M_{n,a}=\max_t\Pr(S_{n,a}=t).
\]
For **every** such \(n,a\),
\[
\boxed{K_{n,a}M_{n,a}^{2}<1.}
\]
Equivalently, the endpoint Rényi entropies satisfy the strict conjectured inequality
\[
\boxed{H_0(S_{n,a})<2H_\infty(S_{n,a}).}
\]
The exponent \(2\) cannot be replaced by any smaller uniform exponent on this family: setting \(a=0\) and letting \(n\to\infty\) gives \(H_0(S_{n,0})/H_\infty(S_{n,0})\to2\).

## Assumptions and scope

The Bernoulli variables have probabilities \(\Pr(B_i=0)=\Pr(B_i=1)=1/2\) and are mutually independent. The first \(n\) coefficients are identical and nonzero; scaling the whole sum by a common nonzero constant leaves both entropy orders unchanged, so their common coefficient is normalized to \(1\). The final coefficient \(a\) is an arbitrary real number, including zero, negative, integers and nonintegers. The inequality is strict for each finite \(n\), but no fixed multiplicative gap in the entropy inequality is asserted. The maximum is over the finite set of atoms. The primary subject is concentration and finite convolutions of independent variables (MSC 60E15).

## Proof

**1. Central binomial estimates.** Put
\[
p_n(j)=2^{-n}\binom nj\quad(0\le j\le n),\qquad
c_n=\max_jp_n(j)=2^{-n}\binom n{\lfloor n/2\rfloor}.
\]
We use the two inequalities, for every integer \(n\ge1\),
\[
(n+1)c_n^2\le\frac34,
\qquad
\left(n+\left\lfloor\frac n2\right\rfloor+1\right)c_n^2\le1.
\tag{1}
\]
For even \(n=2m\), define \(F_m=(3m+1)c_{2m}^2\). Direct binomial cancellation gives
\[
F_1=1,\quad
\frac{F_{m+1}}{F_m}=
\frac{3m+4}{3m+1}\left(\frac{2m+1}{2m+2}\right)^2\le1
\quad(m\ge1),
\]
because
\[
(3m+1)(2m+2)^2-(3m+4)(2m+1)^2=m>0.
\]
Thus the second inequality of (1) is strict for even \(n\ge4\); at \(n=2\) equality holds in this auxiliary bound. For odd \(n=2m+1\), the identity \(c_{2m+1}=c_{2m+2}\) and the even case yield
\[
(3m+2)c_{2m+1}^2<(3m+4)c_{2m+2}^2\le1.
\]
For the first inequality of (1), at even \(n=2m\ge2\) the ratio between consecutive values of \((2m+1)c_{2m}^2\) is
\[
\frac{(2m+3)(2m+1)}{(2m+2)^2}<1,
\]
with initial value \(3c_2^2=3/4\). For odd \(n\), again use \(c_{2m+1}=c_{2m+2}\) and \(2m+2<2m+3\). This proves (1), including \(n=1\).

**2. Support decomposition.** Replacing \(a\) by \(-a\) only translates the distribution: \(-aB_{n+1}\) has the same law as \(aB_{n+1}-a\). We may therefore assume \(a\ge0\). If \(a=0\), the support has size \(n+1\) and the largest atom is \(c_n\), so (1) gives \(K_{n,0}M_{n,0}^2\le3/4<1\). If \(a\) is not an integer, or if \(a\) is an integer exceeding \(n\), the sets of atoms \(\{0,\ldots,n\}\) and \(\{a,\ldots,a+n\}\) are disjoint. Thus \(K_{n,a}=2(n+1)\) and \(M_{n,a}=c_n/2\), whence
\[
K_{n,a}M_{n,a}^2=\frac{n+1}{2}c_n^2\le\frac38<1.
\]
It remains to handle integer \(a=k\), where \(1\le k\le n\). In this case \(K_{n,k}=n+k+1\), and for each integer \(j\),
\[
\Pr(S_{n,k}=j)=\frac{p_n(j)+p_n(j-k)}2,
\tag{2}
\]
where \(p_n\) is extended by zero outside \(\{0,\ldots,n\}\).

**3. Small shifts.** If \(k\le\lfloor n/2\rfloor\), (2) gives \(M_{n,k}\le c_n\), hence by the second estimate in (1)
\[
K_{n,k}M_{n,k}^2\le
\left(n+\left\lfloor\frac n2\right\rfloor+1\right)c_n^2\le1.
\]
The upper bound is strict for odd \(n\) and even \(n\ge4\). The only remaining even case is \(n=2,k=1\), where \(S_{2,1}\) is \(\operatorname{Bin}(3,1/2)\) and \(K_{2,1}M_{2,1}^2=9/16<1\).

**4. Large shifts in all large dimensions.** Define the modal set \(D_n=\{\lfloor n/2\rfloor,\lceil n/2\rceil\}\) and the integer distance \(d_n(j)=\min_{r\in D_n}|j-r|\). The following elementary Gaussian bound holds for all integers \(j\):
\[
p_n(j)\le c_n\exp\left(-\frac{d_n(j)^2}{n}\right).
\tag{3}
\]
Indeed, for even \(n=2m\), the ratio at displacement \(r\ge0\) from the mode is
\[
\frac{p_n(m+r)}{c_n}=
\prod_{i=1}^{r}\frac{m-i+1}{m+i}\le
\exp\left(-\sum_{i=1}^{r}\frac{2i-1}{m+i}\right)
\le\exp(-r^2/n).
\]
For odd \(n=2m+1\), moving \(r\) places rightward from the right-hand mode gives
\[
\frac{p_n(m+1+r)}{c_n}=
\prod_{i=1}^{r}\frac{m+1-i}{m+1+i}
\le\exp\left(-\sum_{i=1}^{r}\frac{2i}{m+1+i}\right)
\le\exp(-r^2/n).
\]
Symmetry covers the other side, and the bound is automatic outside the support.

Because the modal set has diameter at most \(1\), for indices \(j\) and \(j-k\) separated by \(k\), at least one of their two distances \(d_n\) is at least \((k-1)/2\). Hence (2) and (3) imply
\[
M_{n,k}\le\frac{c_n}{2}\left(1+
\exp\left(-\frac{(k-1)^2}{4n}\right)\right).
\tag{4}
\]
If \(n\ge20\) and \(k>\lfloor n/2\rfloor\), then \((k-1)^2/(4n)\ge1\). To verify the last statement, write \(n=2m\) or \(2m+1\) and use \(m\ge10\), so \(m^2\ge4(2m+1)\). Since \(e^{-1}<1/2\), equations (1) and (4), together with \(K_{n,k}\le2(n+1)\), yield
\[
K_{n,k}M_{n,k}^{2}
<2(n+1)\left(\frac{3c_n}{4}\right)^2
\le\frac{27}{32}<1.
\]

**5. Exhaustive finite bridge.** For \(1\le n\le19\) and \(1\le k\le n\), define the integers
\[
A_{n,k}(j)=\binom nj+\binom n{j-k}\qquad(0\le j\le n+k),
\]
with out-of-range binomial coefficients set to zero. The standalone exact-integer checker `verify_one_outlier.py` computes every one of the \(190\) pairs \((n,k)\), checking *every* one of their \(3990\) possible positive atoms, and verifies
\[
(n+k+1)\left(\max_{0\le j\le n+k}A_{n,k}(j)\right)^2<4^{n+1}.
\tag{5}
\]
This is a finite exhaustive lemma, not statistical sampling. Equation (5) exactly equals the desired strict inequality via (2). It fills the large-shift cases at small \(n\), completing the universal proof.

**6. Sharpness of the entropy exponent.** With \(a=0\), we have \(K_{n,0}=n+1\) and \(M_{n,0}=c_n\). The central binomial asymptotic \(c_n\sim\sqrt{2/(\pi n)}\) gives
\[
\frac{H_0(S_{n,0})}{H_\infty(S_{n,0})}
=\frac{\log(n+1)}{-\log c_n}\longrightarrow2.
\]
This shows optimality of the exponent \(2\) for uniform entropy comparisons, although the strict inequality holds at each finite sample size.

## Verification

Execute `python3 verify_one_outlier.py` from the directory containing this file. It requires only the Python standard library and prints a PASS confirmation after \(190\) complete finite cases, \(3990\) atom-position checks and separate exact central-binomial tests. These computations certify (5); steps (1), (3), (4), and the infinite tail argument are analytical proofs and are not inferred from finite tests. All binomial identities use exact integers and all ratios use exact rational arithmetic.

## Relationship to prior work

Jiange Li, *Multiplicative comparisons of Rényi entropies for weighted Bernoulli sums* (arXiv:2609.01529, first posted 1 September 2026), states the conjecture \(H_0(S_w)\le2H_\infty(S_w)\) for arbitrary fair-Bernoulli weighted sums. Its positive-order comparison at order at least \(1/2\) and its general logarithmic endpoint coefficient do not establish the conjectured endpoint coefficient \(2\) on this one-exceptional-weight family. The earlier work of Jain, Sah, and Sawhney, *Anticoncentration versus the Number of Subset Sums* (arXiv:2101.07726), obtains a weaker size-versus-concentration relation and identifies the sharper problem; it does not supply (5) or the all-real-exceptional-weight endpoint conclusion. The new statement is a structured infinite subfamily of the conjecture, not a claim to settle the general case.

## Limitations

No conclusion is established for two or more independent exceptional coefficients relative to the common block, or for biased/unequal Bernoulli probabilities. The finite part of the proof is an exact exhaustive computation rather than a purely symbolic estimate for \(n\le19\). The exponent \(2\) is asymptotically optimal but no exact universal numerical maximum of \(K_{n,a}M_{n,a}^2\) across all \(n,a\) is claimed. Existing equivalent results under a different terminology remain a possibility.

## References

1. Jiange Li, *Multiplicative comparisons of Rényi entropies for weighted Bernoulli sums*, arXiv:2609.01529 (first public posting 1 September 2026), https://arxiv.org/abs/2609.01529; full text https://arxiv.org/html/2609.01529v2.
2. Vishesh Jain, Ashwin Sah, and Mehtaab Sawhney, *Anticoncentration versus the Number of Subset Sums*, arXiv:2101.07726 (2021), https://arxiv.org/html/2101.07726v2.
