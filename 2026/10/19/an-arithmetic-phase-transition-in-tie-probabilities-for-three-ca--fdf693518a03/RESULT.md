# An arithmetic phase transition in tie probabilities for three-candidate Thiele committees

## Finding

Three candidates compete for two committee positions, with \(n\) independently sampled voters. Each voter independently approves each candidate with probability \(1/2\). For a committee, a voter contributes \(0\) if neither selected candidate is approved, \(1\) if exactly one is approved, and \(1+\alpha\) if both are approved, for a fixed \(\alpha\in[0,1]\). Winning committees are all maximizers of the sum. Let \(T_n(\alpha)\) be the probability that more than one two-person committee is winning.

**Theorem (exact arithmetic tie asymptotics).** For any fixed rational \(\alpha=a/b\in[0,1]\) in lowest terms with integers \(a\ge0\), \(b\ge1\),
\[
\lim_{n\to\infty}\sqrt n\,T_n(\alpha)=\frac{3}{\sqrt{2\pi(a^2+b^2)}}.
\]
For any fixed irrational \(\alpha\in(0,1)\),
\[
\lim_{n\to\infty}nT_n(\alpha)=\frac3\pi.
\]
Thus exact tied-winning-committee probability has a rational/irrational decay-exponent transition. For the standard Chamberlin--Courant (\(\alpha=0\)), proportional approval (\(\alpha=1/2\)), and ordinary approval (\(\alpha=1\)) scoring rules, the respective limits of \(\sqrt n\,T_n\) are \(3/\sqrt{2\pi}\), \(3/\sqrt{10\pi}\), and \(3/(2\sqrt\pi)\).

## Assumptions and scope

Candidates are \(A,B,C\). Every vote is a triple of independent fair Bernoulli variables \((A_i,B_i,C_i)\). Voters are independent. Committees are \(AB,AC,BC\), exactly two seats are filled, weights are fixed as \(n\to\infty\), and exact real-number equality determines a tie; there is no tie-breaking. The score for zero, one, or two approved committee members is respectively \(0\), \(1\), or \(1+\alpha\). This is a two-seat Thiele rule with second marginal \(\alpha\); a fixed irrational marginal is allowed mathematically although standard implementations generally use rational weights.

## Proof

Write \(S_{AB},S_{AC},S_{BC}\) for the three total scores. For a single vote define integer variables
\[
U_0=(B_i-C_i)(1-A_i),\quad U_1=(B_i-C_i)A_i,
\]
\[
V_0=(A_i-C_i)(1-B_i),\quad V_1=(A_i-C_i)B_i.
\]
Using the voter-score definition directly, the two committee score differences are
\[
S_{AB}-S_{AC}=\sum_{i=1}^n(U_0+\alpha U_1),\qquad
S_{AB}-S_{BC}=\sum_{i=1}^n(V_0+\alpha V_1).
\]
The one-voter vector \((U_0,U_1,V_0,V_1)\) has mean zero and covariance
\[
\Sigma=\frac18
\begin{pmatrix}2&0&1&0\\0&2&0&1\\1&0&2&0\\0&1&0&2\end{pmatrix}.
\]
Its support generates the full lattice \(\mathbb Z^4\): the ballot types \(010\), \(101\), \(100\), and \(011\) supply four independent unit steps, while ballot \(000\) supplies the zero step. Hence the standard strongly aperiodic multivariate lattice local central limit theorem applies; every covariance matrix subsequently used is nonsingular.

**Rational marginal.** Suppose \(\alpha=a/b\) in lowest terms. Set
\[
D=\sum_{i=1}^n(bU_0+aU_1),\qquad
E=\sum_{i=1}^n(bV_0+aV_1).
\]
Then \(S_{AB}=S_{AC}\) iff \(D=0\), and \(S_{AB}>S_{BC}\) iff \(E>0\). One-voter \(D\)-increments are \(\pm b\), \(\pm a\), each with probability \(1/8\), and zero with the remaining probability (when \(a=0\) or \(a=b\), coincident increments are combined). The lattice span is one because \(\gcd(a,b)=1\), and a zero step is possible; the increment variance is \((a^2+b^2)/4\). The lattice local central limit theorem gives
\[
\Pr(D=0)=\frac{2+o(1)}{\sqrt{2\pi(a^2+b^2)n}}.
\]
The covariance of a one-voter \((D,E)\) is \((a^2+b^2)\begin{psmallmatrix}1/4&1/8\\1/8&1/4\end{psmallmatrix}\), with positive determinant. Conditional local-CLT summation over \(E\) gives \(E/\sqrt n\mid D=0\) a centered nondegenerate normal limit of variance \(3(a^2+b^2)/16\). In particular,
\[
\Pr(D=0,E>0)=\left(\frac12+o(1)\right)\Pr(D=0).
\]
A two-dimensional local-CLT upper bound gives \(\Pr(D=E=0)=O(n^{-1})\). The three committee-score vectors are exchangeable. The event that at least two committees maximize is the disjoint union of the three possible exactly-two-at-top events and the all-three-tied event. Therefore
\[
T_n(\alpha)=3\Pr(D=0,E>0)+\Pr(D=E=0),
\]
which yields the rational formula.

**Irrational marginal.** If \(\alpha\) is irrational, the integers \(\sum U_0\) and \(\sum U_1\) must both vanish whenever their weighted sum vanishes. The two-dimensional random walk \((\sum U_0,\sum U_1)\) has independent-coordinate covariance \(\frac14 I_2\), full span, and a zero step. Its lattice local central limit theorem gives
\[
\Pr(S_{AB}=S_{AC})=\Pr\left(\sum U_0=\sum U_1=0\right)
=\frac{2+o(1)}{\pi n}.
\]
The full four-dimensional local central limit theorem gives, conditioned on \(\sum U_0=\sum U_1=0\), a centered bivariate normal limit for \((\sum V_0,\sum V_1)/\sqrt n\), with conditional covariance \(\frac3{16}I_2\). Thus the conditional probability that \(\sum(V_0+\alpha V_1)>0\) tends to \(1/2\). The all-three-equal event forces all four integer sums to vanish and has probability \(O(n^{-2})\). Exchangeability and the same exactly-two-plus-triple decomposition give \(nT_n(\alpha)\to3/\pi\).

For an independent check on the irrational pair-equality constant, conditioning on the number \(K\sim\operatorname{Bin}(n,1/2)\) of votes with \(A_i=0\) yields the exact formula
\[
\Pr(S_{AB}=S_{AC})=\sum_{k=0}^{n}{n\choose k}2^{-n}
\frac{{2k\choose k}}{4^k}\frac{{2(n-k)\choose n-k}}{4^{n-k}},
\]
whose central-binomial asymptotic is \(2/(\pi n)\). This completes the proof.

## Verification

The standalone file `verification/check_ties.py` computes exact score-difference distributions for rational \(\alpha\), exact four-coordinate distributions for irrational \(\alpha=\sqrt2-1\), and directly enumerates complete ballot profiles through four voters. Independent enumerations coincide with the exact distributions, including for \(n=4\): \(T_4(1/2)=1147/4096\) and \(T_4(\sqrt2-1)=1075/4096\). Further checks compare the finite-\(n\) pair-tie expressions to the asymptotic constants at \(n=100,400,1000\). The analytical proof, not these finite tests, establishes the asymptotics for all \(n\).

## Relationship to prior work

Janeczko and Faliszewski (2023) introduce computational tie-detection and tie-counting results for Thiele and other approval-based committee rules and report substantial simulated tie rates, but give neither these asymptotic constants nor the irrational-marginal classification in their inspected full text. Xia (2025), Theorem 14 and Appendix D.1, already proves a \(\Theta(n^{-1/2})\) irresoluteness rate for **integer** Thiele scores under identical per-candidate approval probabilities; consequently the rational-order statement here is not claimed as a new order theorem. The new statements are the exact constants for every rational second marginal and the distinct \(3/(\pi n)\) regime for fixed irrational marginals. Xia (2020) develops general tie-rate methods for integer generalized scoring rules; those methods inform the comparison but do not supply these constants or the irrational comparison. No independent priority assessment is implied.

## Limitations

The results concern three candidates, two seats, fair independent approvals, fixed exact weights, and exact equality. They do not quantify numerical near-ties, resolve elections under empirical or correlated vote cultures, or give rates uniform as an irrational weight approaches a rational one. In particular, using a floating-point approximation of an irrational parameter changes the exact lattice and therefore changes the limiting regime. The value of the result is an analytical baseline and a precise caution about the dependence of exact ties on score arithmetic.

## References

1. Ł. Janeczko and P. Faliszewski, *Ties in Multiwinner Approval Voting*, arXiv:2305.01769 (first public preprint 2023-05-02), https://arxiv.org/abs/2305.01769 .
2. L. Xia, *A Linear Theory of Multi-Winner Voting*, arXiv:2503.03082 (2025), Theorem 14 and Appendix D.1, https://arxiv.org/abs/2503.03082 .
3. L. Xia, *How Likely Are Large Elections Tied?*, arXiv:2011.03791 (2020), https://arxiv.org/abs/2011.03791 .
