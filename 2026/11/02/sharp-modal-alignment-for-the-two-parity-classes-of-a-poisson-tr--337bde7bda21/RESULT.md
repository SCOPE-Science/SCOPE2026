# Sharp modal alignment for the two parity classes of a Poisson-trinomial sum

## Finding
Let \(X_1,\ldots,X_n\) be independent random variables taking values in \(\{0,\frac12,1\}\), where \(n\ge1\). Suppose both events \(X:=\sum_iX_i\in\mathbb Z\) and \(X\in\mathbb Z+\frac12\) have positive probability. Let \(m_E\) and \(m_O\) be **arbitrary** modes of the respective conditional laws. Then
\[
\boxed{|m_E-m_O|\le\frac32.}
\]
This constant is sharp, including the choice of modes when ties occur. If every summand assigns strictly positive probability to **each** of its three possible outcomes, the stronger sharp identity holds:
\[
\boxed{|m_E-m_O|=\frac12.}
\]
Thus under strictly positive three-point probabilities, every pair of parity-conditional modes consists of adjacent points in the combined half-integer lattice. At the probability-simplex boundary, the best uniform upper bound increases to \(3/2\).

## Assumptions and scope
Write \(L_i=\Pr(X_i=0)\), \(T_i=\Pr(X_i=\frac12)\), \(W_i=\Pr(X_i=1)\), where these nonnegative probabilities sum to one. No identical-distribution assumption is made. Modes are **all** maximizers of the relevant probability mass functions, including ties. Define
\[
G(w)=\prod_{i=1}^{n}(L_i+T_iw+W_iw^2)=P(w^2)+wQ(w^2),
\]
where \(P(z)=\sum_{k\ge0}p_kz^k\) and \(Q(z)=\sum_{k\ge0}q_kz^k\), with \(p_k=\Pr(X=k)\), \(q_k=\Pr(X=k+\frac12)\). The modes of these unnormalized coefficient sequences equal the conditional modes because conditional normalization does not change their maximizers. The theorem makes no claim if either parity probability is zero.

## Proof
**Step 1: a positive partial-fraction representation.** Every factor \(L_i+T_iw+W_iw^2\) has all its zeros in the closed left half-plane: this follows from its nonnegative coefficients for degree one and, for degree two, from nonnegative product and nonpositive sum of its roots. Hence \(G\) is weakly Hurwitz stable. The weak Hermite--Biehler theorem for even/odd parts yields nonpositive real zeros of \(P,Q\), with \(Q\) weakly interlacing \(P\) in the oriented sense. The elementary partial-fraction consequence is
\[
\frac{Q(z)}{P(z)}=c+\sum_{j}\frac{a_j}{z+x_j},\qquad c\ge0,\quad a_j\ge0,\quad x_j\ge0,
\]
where the \(-x_j\) are zeros of \(P\). To verify signs directly, first cancel common factors. The remaining simple poles and intervening zeros alternate, so the residues \(Q(-x_j)/P'(-x_j)\) have the same nonnegative sign; repeated or coincident roots follow by cancellation/limits. Since \(\deg Q\le\deg P\), there is at most the displayed nonnegative constant \(c\). If \(P\) is constant, this reduces to \(Q=cP\). Consequently,
\[
Q(z)=cP(z)+\sum_j a_jR_j(z),\qquad R_j(z):=\frac{P(z)}{z+x_j}.
\]
All the polynomials in this sum have nonnegative coefficients and only nonpositive real zeros, so their coefficient sequences are unimodal, with at most two adjacent modes (including deterministic/monomial cases).

**Step 2: a deletion-mode lemma.** Let \(P(z)=(z+x)R(z)\) with \(x\ge0\) and \(R\) real-rooted with nonpositive zeros and nonnegative coefficients. Extend its coefficient sequence \(r_j\) by zero outside its support. If index \(k\) is any coefficient mode of \(P\), then for \(x>0\) every coefficient mode of \(R\) belongs to \(\{k-1,k\}\). Indeed, if \(R\) had a mode at or below \(k-2\), unimodality and absence of three consecutive modes give \(r_{k-2}\ge r_{k-1}\ge r_k\), with at least one strict inequality, so
\[
[z^{k-1}]P-[z^k]P=x(r_{k-1}-r_k)+(r_{k-2}-r_{k-1})>0,
\]
contradicting maximality at \(k\). A mode of \(R\) at or above \(k+1\) similarly gives
\[
[z^{k+1}]P-[z^k]P=x(r_{k+1}-r_k)+(r_k-r_{k-1})>0.
\]
If \(x=0\), then \(P=zR\), so every mode of \(R\) is a mode of \(P\) shifted left by one. Because the modes of \(P\) number at most two and are adjacent, every mode of \(R\) lies in \(\{k-2,k-1,k\}\).

**Step 3: universal bound.** Fix any mode index \(k\) of \(P\). By Step 2, every \(R_j\) in Step 1 has all modes in \([k-2,k]\). The component \(P\) has all its modes in \([k-1,k+1]\). A nonnegative sum of unimodal coefficient sequences whose modes all lie in one common integer interval also has all its modes there: every summand rises before that interval and falls after it. Thus every mode index \(\ell\) of \(Q\) satisfies
\[
k-2\le\ell\le k+1.
\]
Since the actual corresponding parity modes are \(k\) and \(\ell+\frac12\), their separation is at most \(3/2\).

**Step 4: strictly positive case.** If \(L_i,T_i,W_i>0\) for every \(i\), the total polynomial has degree \(2n\) with strictly positive leading and constant coefficients. Therefore \(\deg P=n\), \(\deg Q=n-1\), so \(c=0\), and \(P(0)=\prod_iL_i>0\), so every \(x_j>0\). The stronger deletion lemma implies all modes of \(Q\) belong to \(\{k-1,k\}\) for each mode \(k\) of \(P\). Hence every separation equals \(1/2\), not merely at most \(1/2\), because one mode is integer and the other half-integer.

**Step 5: sharpness.** For the universal bound, take two independent variables with unnormalized generating factors \(1+w\) and \(1+w^2\): the first equals zero or one half with probability one half each, and the second equals zero or one with probability one half each. Then
\[
G(w)=\frac14(1+w)(1+w^2)=\frac14(1+w+w^2+w^3).
\]
Both \(0,1\) are integer-conditional modes, while both \(\frac12,\frac32\) are half-integer-conditional modes. Selecting \(0\) and \(\frac32\) attains the universal bound. For the strictly positive regime, a single summand with \(L=T=W=1/3\) already has integer-conditional modes \(0,1\) and half-integer-conditional mode \(\frac12\), attaining the sharp value \(1/2\).

## Verification
Run `python3 verify_modes.py` to reproduce exact integer convolution tests. The checker enumerates multisets of independent three-point factors (including zero probabilities), verifies the two inequalities for **every choice of tied modes**, exercises larger strictly positive random integer factors, and checks both sharpness examples. Its recorded output is in `verify_output.txt`: 125439 admissible cases passed. Finite checks corroborate, but do not prove, the all-dimensional claims; the proof is Steps 1--5 above.

## Relationship to prior work
Broadie and Petkova (arXiv:2603.09019v1, Theorem 1) prove the two parity-conditional laws are Poisson-binomial and that their modes are separated by at most \(5/2\), obtained through comparison with conditional means. Their Section 3 proves real-rootedness using Hermite--Biehler, but does not use the *oriented interlacing* to sharpen modal proximity. The present theorem sharpens their constant from \(5/2\) to \(3/2\) without additional assumptions, and to the adjacent-lattice value \(1/2\) when every three-point probability is positive. The weak Hermite--Biehler theorem and real-rooted coefficient unimodality are classical and are not claimed here as new results. Yang and Zhang's 2022 article states the oriented weak interlacing theorem; Gnedin's 2024 work concerns modal stability of extended Bernoulli sums, a related but different setting. The new claim is the quantitative **joint parity-mode** conclusion and its sharp boundary distinction.

## Limitations
The theorem concerns modes of conditional parity distributions, not the unconditional modes or optimal sports matchups. It requires independent summands with support contained in \(\{0,1/2,1\}\); dependent variables and larger alphabets are not covered. Degenerate parity classes are excluded because their conditional modes do not exist. The modal bound is sensitive to zero component probabilities; the stronger \(1/2\) conclusion is not asserted under arbitrary boundary degeneracy. Historical originality remains subject to independent comparison with generalized interlacing/total-positivity literature; the statements and evidence here do not constitute independent certification.

## References
1. Mark Broadie and Ina Petkova, *On the structure of the Poisson trinomial distribution*, arXiv:2603.09019v1 (first public 2026-03-09), especially Theorem 1 and Sections 2--3. https://arxiv.org/html/2603.09019
2. Arthur L. B. Yang and Philip B. Zhang, *Descent generating polynomials and the Hermite--Biehler theorem*, Journal of Algebraic Combinatorics 56 (2022), 117--152, DOI:10.1007/s10801-021-01101-2 (weak Hermite--Biehler interlacing).
3. Alexander Gnedin, *Cross Modality of the Extended Binomial Sums*, arXiv:2408.06477v1 (2024), related mode-stability literature; direct comparison limited to the accessible abstract and indexed excerpts.
4. Robert Angarone, *Weakly interlacing polynomials and totally nonnegative Hurwitz matrices*, arXiv:2312.09385 (2023), related weak-interlacing framework (abstract inspected).
