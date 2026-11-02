# Sharp golden-ratio exponent for the mean residual of exhaustive Peres extraction

## Finding

Let \(S_N\) be uniformly distributed on all binary strings of length \(N\). Apply the exhaustive Peres transform as defined below, and let \(R_N\) be its residual bit string. Put
\[
\varphi=\frac{1+\sqrt5}{2},\qquad \alpha=\log_2\varphi=0.694241913630\ldots.
\]
**Theorem.** For every integer \(N\ge1\), without asymptotic qualifications,
\[
\boxed{\frac{N^\alpha}{10}+\frac9{10}\ \le\ \mathbb E|R_N|\ \le\ 3N^\alpha-2},
\qquad
\boxed{\mathbb E\operatorname{wt}(R_N)=\frac12\mathbb E|R_N|}.
\]
In particular \(\mathbb E|R_N|=\Theta(N^\alpha)\), so the expected-residual growth exponent exists and equals \(\alpha\). A deterministic consequence is that for every \(N\ge1\), **some** binary input of length \(N\) has at least \(N^\alpha/20+9/20\) residual ones. These are statements about the fair-input mean and an existential consequence, not an upper bound of order \(N^\alpha\) for the maximum.

## Assumptions and scope

The alphabet is \(\{0,1\}\). The input is an independent fair-bit string of fixed nonnegative integer length \(m\). For \(m\le1\), the exhaustive transform returns no extracted bits and the entire input as residual. Otherwise, writing \(m=2n+\rho\), \(\rho\in\{0,1\}\), partition the first \(2n\) bits into ordered adjacent pairs. Define \(u\) of length \(n\) by the XOR of each pair. Define \(v\) by retaining the second bit of exactly the equal pairs, in their original order. Let \(r\) be the final unpaired bit if \(\rho=1\), or empty otherwise. Apply the same transform recursively to \(u\) and \(v\), and concatenate residuals as \(R(u)R(v)r\). The remaining extracted-bit stream plays no part in the theorem. The notation \(\operatorname{wt}(R)\) means the number of ones in \(R\). All averages are over the \(2^N\) equally likely inputs, and there are no random choices in the transform itself.

## Proof

**1. Exact recursion.** Define \(a_m=\mathbb E|R_m|\), \(b_m=\mathbb E\operatorname{wt}(R_m)\) and take \(a_0=b_0=0\), \(a_1=1\), \(b_1=1/2\). Conditional on the XOR vector \(u\), the equal-pair bits forming \(v\) are fair and independent; the number of equal pairs is \(B_n\sim\operatorname{Bin}(n,1/2)\). The unpaired bit is independent and fair. Thus, for \(n\ge1\) and \(\rho\in\{0,1\}\),
\[
 a_{2n+\rho}=a_n+\mathbb E a_{B_n}+\rho,\qquad
 b_{2n+\rho}=b_n+\mathbb E b_{B_n}+\rho/2.\tag{1}
\]
The initial values and (1) imply by strong induction that \(b_m=a_m/2\) for all \(m\ge0\).

**2. Characteristic exponent.** The positive number \(\alpha\) satisfies \(2^\alpha=\varphi=1+2^{-\alpha}\), equivalently
\[
 n^\alpha+(n/2)^\alpha=(2n)^\alpha.\tag{2}
\]
It is between \(1/2\) and \(1\). Concavity gives \(\mathbb E B_n^\alpha\le(n/2)^\alpha\).

**3. Binomial concavity deficit.** Set \(\mu=n/2\) and \(d_n=\mu^\alpha-\mathbb E B_n^\alpha\ge0\). We prove the uniform bound \(d_n<4\) for every \(n\ge1\). The tangent deficit
\[
 g(x)=\mu^\alpha+\alpha\mu^{\alpha-1}(x-\mu)-x^\alpha
\]
is nonnegative. On \(x\ge\mu/2\), Taylor's theorem, using \(|(x^\alpha)''|=\alpha(1-\alpha)x^{\alpha-2}\), yields
\[
 g(x)\le\tfrac12\alpha(1-\alpha)(\mu/2)^{\alpha-2}(x-\mu)^2.
\]
For \(0\le x<\mu/2\), the deficit decreases on \([0,\mu]\), and thus \(g(x)\le g(0)=(1-\alpha)\mu^\alpha\). Since \(\mathbb E(B_n-\mu)^2=n/4\) and the standard binomial lower-tail Chernoff inequality gives \(\Pr(B_n<n/4)\le e^{-n/16}\),
\[
 d_n\le \frac{\alpha(1-\alpha)}2(n/4)^{\alpha-1}
 +(1-\alpha)(n/2)^\alpha e^{-n/16}
 \le\frac12+\frac8e<4.\tag{3}
\]
Here the first inequality uses the two regions above. The last uses \(\alpha(1-\alpha)\le1/4\), \(1/2<\alpha<1\), \(n^{\alpha-1}\le1\), and \(n e^{-n/16}\le16/e\) for \(n\ge1\). These inequalities include the possible atom \(B_n=0\), because \(0^\alpha=0\).

**4. Universal lower bound.** Let \(c=1/10\) and \(K=9/10\). The assertion \(a_m\ge c m^\alpha+K\) holds at \(m=1\); the case \(m=0\) is treated separately. Assume the assertion at every strictly smaller positive length. Since \(\Pr(B_n>0)=1-2^{-n}\), (1)--(3) give
\[
 a_{2n+\rho}\ge c(2n)^\alpha+K+K(1-2^{-n})-c d_n+\rho.
\]
For \(\rho=0\), the surplus above \(c(2n)^\alpha+K\) is greater than \((9/10)(1/2)-(1/10)4=1/20\). For \(\rho=1\), also use \((2n+1)^\alpha-(2n)^\alpha\le1\); the extra \(\rho=1\) exceeds the required increment \(c\), and the surplus remains positive. This proves the lower bound by induction for every positive length.

**5. Universal upper bound.** At \(m=1\), \(a_1=3(1)^\alpha-2=1\). Assume \(a_j\le3j^\alpha-2\) for all smaller positive \(j\), while \(a_0=0\). Jensen's inequality and the atom \(B_n=0\) give
\[
 a_{2n+\rho}\le3n^\alpha-2+3(n/2)^\alpha-2(1-2^{-n})+\rho
 =3(2n)^\alpha-4+2^{1-n}+\rho
 \le3(2n+\rho)^\alpha-2,
\]
where \(n\ge1\) and \(\rho\in\{0,1\}\). This closes the induction. Combining the bounds, \(\log a_N/\log N\to\alpha\) as \(N\to\infty\). Finally \(\max_{s\in\{0,1\}^N}\operatorname{wt}(R(s))\ge b_N=a_N/2\), proving the pointwise existential statement.

## Verification

The accompanying self-contained program `verify.py` implements the recursive transform directly, and separately implements rational binomial recurrences for both moments in (1). It exhaustively enumerates every binary input through length 12, checking the exact mean residual length and number of ones against the rational recurrences, including odd lengths. It then computes exact rational recurrences through length 90 and checks the displayed global inequalities numerically at those sizes. The recorded output is in `verification-output.txt`. The proof of (3), both inductions, and the all-length claim are mathematical and do not rely on exhaustive sampling or floating-point computation.

## Relationship to prior work

Garivier's *The Exhaustive Peres Transform: Extraction and Universal Coding*, first publicly posted October 19, 2026, defines and studies this residual transform; its discussion of the residual-weight growth problem gives the **same mean recursion** and explains the exponent \(\log_2\varphi\) **heuristically** (Section 8, open problem (i)), while proving a larger deterministic upper exponent for the worst-case number of residual ones (Appendix A). The contribution here is a proved, all-length two-sided mean bound with the sharp exponent and a consequent worst-case lower exponent. Peres (1992) and Pae (2018) establish extraction and recursive structure but do not state this finite-length sharp mean law. Prasitsupparote, Konno, and Shikata (2018) analyze finite-length rates and give a conditional lower bound for a different maximum-redundancy statistic; it does not imply the sharp fair-source mean theorem here.

## Limitations

This is an expectation under independent fair inputs. It does not prove an \(O(N^\alpha)\) bound for the **maximum** number of residual ones, a limit of \(a_N/N^\alpha\), a universal exponent for biased sources, or an optimal numerical prefactor. The 2026 paper's maximum-residual conjecture therefore remains open. The numeric checks are finite supporting tests and not an independent proof of asymptotic behavior; publication priority remains subject to further human literature review.

## References

1. A. Garivier, *The Exhaustive Peres Transform: Extraction and Universal Coding*, arXiv:2610.26396, first submitted 2026-10-19, Section 2, Section 8 and Appendix A. https://arxiv.org/abs/2610.26396
2. Y. Peres, *Iterating von Neumann's Procedure for Extracting Random Bits*, Annals of Statistics 20 (1992), 590–597, DOI:10.1214/aos/1176348543. https://doi.org/10.1214/aos/1176348543
3. S.-I. Pae, *Peres-Style Recursive Algorithms*, arXiv:1805.04610, first submitted 2018-05-11. https://arxiv.org/abs/1805.04610
4. A. Prasitsupparote, N. Konno, and J. Shikata, *Numerical and Non-Asymptotic Analysis of Elias's and Peres's Extractors with Finite Input Sequences*, Entropy 20 (2018), 729, DOI:10.3390/e20100729. https://doi.org/10.3390/e20100729
