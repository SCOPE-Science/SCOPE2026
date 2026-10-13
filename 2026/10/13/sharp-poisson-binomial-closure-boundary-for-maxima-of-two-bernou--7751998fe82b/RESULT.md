# Sharp Poisson-binomial closure boundary for maxima of two Bernoulli sums

## Finding

Suppose \(X\) is a finite sum of independent Bernoulli random variables and \(X'\) is an independent copy. Denote \(M=\max(X,X')\). A *Poisson-binomial law* is the distribution of a finite sum of independent (not necessarily identically distributed) Bernoulli variables; success probabilities \(0\) and \(1\) are permitted.

**Theorem.** (i) If \(X\) has at most two Bernoulli summands, with arbitrary success probabilities in \([0,1]\), then \(M\) is Poisson-binomial.

(ii) For every integer \(m\ge3\) there exists \(\varepsilon_m>0\) such that if \(X,X'\) are independent \(\operatorname{Bin}(m,p)\) variables, \(0<p<\varepsilon_m\), their maximum is not Poisson-binomial.

(iii) At the minimal non-preserving size \(m=3\), there is an exact phase transition: for \(0<p<1\), the maximum is Poisson-binomial exactly for \(p\ge p_*\), where \(p_*\) is the unique root in \((0,1)\) of
\[
R(p)=4p^6+8p^3+3p^2+6p-1=0,
\qquad p_*\approx0.150732465335916.
\]
At \(p=0\) and \(p=1\), the maximum is degenerate and is Poisson-binomial.

## Assumptions and scope

All Bernoulli variables defining \(X\) are mutually independent, and \(X'\) is independent and identically distributed with \(X\). The theorem concerns the *maximum of two copies*, not the sum, not an arbitrary order statistic of a larger sample, and not the maximum of dependent copies. In part (i) the Bernoulli success probabilities need not be equal. In parts (ii) and (iii) they are all equal to \(p\). A discrete probability law on \(\{0,\ldots,m\}\) with polynomial probability-generating function (PGF) \(G(z)\) is Poisson-binomial if and only if all zeros of \(G\) are real and nonpositive. Indeed a Bernoulli PGF is \(1-\theta+\theta z\), and conversely a PGF with nonnegative coefficients, \(G(1)=1\), and only nonpositive real zeros factors into normalized Bernoulli PGFs, with zero roots corresponding to deterministic successes. This elementary equivalence is used throughout.

## Proof

**CDF-square identity.** Put \(F(k)=\Pr\{X\le k\}\), with \(F(-1)=0\). Independence gives
\[
\Pr\{M=k\}=F(k)^2-F(k-1)^2.
\tag{1}
\]
Thus the PGF can be tested directly for real nonpositive zeros.

**Part (i): two summands.** Let \(X=B_p+B_r\), with independent Bernoulli variables of success probabilities \(p,r\in[0,1]\). Set \(u=(1-p)(1-r)\) and \(v=pr\). By (1), the PGF coefficients \(b_0,b_1,b_2\) are
\[
 b_0=u^2,\qquad b_1=(1-v)^2-u^2,\qquad b_2=1-(1-v)^2.
\]
Direct expansion factors the quadratic discriminant as
\[
\begin{aligned}
 b_1^2-4b_0b_2&=A\bigl(A+4(1-p)(1-r)\bigr),\\
 A&=(p-r)^2+2pr(1-p)(1-r)\ge0.
\end{aligned}
\tag{2}
\]
Therefore the discriminant is nonnegative. All coefficients are nonnegative; hence all real zeros of the PGF are nonpositive. Degenerate degrees (zero or unit Bernoulli parameters) reduce to the same conclusion, or follow by continuity. The PGF factorization criterion proves the claim. The one-summand case is immediate from the Bernoulli identity \(\Pr(M=1)=1-(1-p)^2\); the zero-summand case is deterministic.

**Part (ii): minimal obstruction and all higher sizes.** Fix \(m\ge3\) and let \(X\sim\operatorname{Bin}(m,p)\). Writing \(b_k(p)=\Pr\{M=k\}\), for each fixed \(1\le k\le m\),
\[
 b_k(p)=\binom mk p^k(1-p)^{m-k}\bigl(F(k)+F(k-1)\bigr),
 \qquad \lim_{p\downarrow0}\frac{b_k(p)}{p^k}=2\binom mk.
\]
Also \(b_0(p)=(1-p)^{2m}\to1\). Consequently the degree-\(m\) rescaled PGF has coefficientwise convergence
\[
G_{m,p}(u/p)=\sum_{k=0}^m\frac{b_k(p)}{p^k}u^k
\longrightarrow H_m(u)=2(1+u)^m-1.
\tag{3}
\]
The roots of \(H_m\) are
\[
u_j=2^{-1/m}\exp(2\pi i j/m)-1,\qquad j=0,\ldots,m-1.
\]
They are all simple, and at least one is nonreal for every integer \(m\ge3\). By continuity of the roots of fixed-degree polynomials (equivalently, disjoint small circles and Rouché's theorem), a nonreal root remains nonreal in \(G_{m,p}(u/p)\) for all sufficiently small positive \(p\). The scaling \(z=u/p\) is real and positive, so \(G_{m,p}(z)\) also has a nonreal root; it cannot be the PGF of a sum of independent Bernoulli variables.

**Part (iii): exact three-trial phase.** For \(m=3\), use (1) to obtain, in ascending polynomial order,
\[
\begin{aligned}
 b_0&=(1-p)^6,\\
 b_1&=3p(1-p)^4(p+2),\\
 b_2&=3p^2(1-p)^2(2+2p-p^2),\\
 b_3&=p^3(2-p^3).
\end{aligned}
\tag{4}
\]
For a cubic \(b_3z^3+b_2z^2+b_1z+b_0\), its discriminant is
\[
\Delta=b_2^2b_1^2-4b_3b_1^3-4b_2^3b_0-27b_3^2b_0^2+18b_3b_2b_1b_0.
\]
Substitution and exact expansion of (4) yield
\[
\Delta=108p^6(1-p)^{12}R(p),\qquad
R(p)=4p^6+8p^3+3p^2+6p-1.
\tag{5}
\]
For \(0<p<1\), all four coefficients in (4) are strictly positive. A real cubic has three real zeros counted with multiplicity if and only if its discriminant is nonnegative; if it is negative there is a nonreal conjugate pair. In the nonnegative case, the polynomial has no zero in \([0,\infty)\) by positivity of its coefficients, so all three real zeros are negative. Finally, \(R(0)=-1\), \(R(1)=20\), and
\[
R'(p)=24p^5+24p^2+6p+6>0\quad(0\le p\le1).
\]
Thus \(R\) has exactly one root \(p_*\in(0,1)\), and (5) plus the PGF criterion establishes the asserted sharp threshold, including the repeated-root boundary \(p=p_*\). The endpoints \(p=0,1\) give deterministic maxima.

## Verification

`verify.py` is a standalone Python 3 standard-library reproducibility script. Run `python3 verify.py` in a directory containing the extracted files. It evaluates (1) with exact rational arithmetic on independent test sets, checks the factorizations (2), (4), and (5) at specified rational parameters, and brackets the unique root of \(R\). These finite checks corroborate the explicit algebraic identities but are not substitutes for their symbolic expansions, the root-continuity argument, or the proof for arbitrary parameters. The symbolic identities can be independently re-expanded using elementary polynomial multiplication and the displayed cubic discriminant formula.

## Relationship to prior work

Jakimiuk, Murawski, Nayar, and Słobodianiuk (first public arXiv posting 2022-05-09, primary MSC 60E15) study discrete log-concavity and inequalities within ultra-log-concave laws; their results do not characterize Poisson-binomial preservation under sample maxima. Badiella, del Castillo, and Puig (publicly available 2023-06-26) prove that order statistics preserve log-concavity and *ultra* log-concavity (Theorem 2). That is a weaker property than being Poisson-binomial (having a PGF with only real nonpositive roots), and their proof does not imply preservation of the stronger property. The present classification distinguishes these levels and gives the exact three-trial phase transition. Tang and Tang survey Poisson-binomial laws and their polynomial characterization, but do not derive this maximum transformation's threshold. These are statement-level comparisons, not a claim that all possible equivalent work has been ruled out.

## Limitations

Part (i) guarantees preservation only for maxima of two independent, identically distributed Bernoulli sums with at most two summands. Part (ii) supplies non-preservation for each larger fixed trial count in a non-explicit interval close to zero; it does not classify all values of \(p\) when \(m\ge4\), nor maxima of three or more copies. Part (iii) covers the homogeneous three-trial binomial family, not arbitrary heterogeneous three-trial parameters. Any equivalent result under Pólya-frequency or total-positivity terminology would qualify the originality assessment.

## References

1. J. Jakimiuk, D. Murawski, P. Nayar, S. Słobodianiuk, “Log-concavity and discrete degrees of freedom,” arXiv:2205.04069, first posted 2022-05-09, https://arxiv.org/abs/2205.04069.
2. L. Badiella, J. del Castillo, P. Puig, “Ultra log-concavity of discrete order statistics,” *Statistics & Probability Letters* 201 (2023), 109900; doi:10.1016/j.spl.2023.109900, open manuscript https://ddd.uab.cat/pub/artpub/2023/283158/StaProLet_a2023v201n109900.pdf.
3. W. Tang and F. Tang, “The Poisson binomial distribution—Old & New,” arXiv:1908.10024 (2019), https://arxiv.org/abs/1908.10024.
