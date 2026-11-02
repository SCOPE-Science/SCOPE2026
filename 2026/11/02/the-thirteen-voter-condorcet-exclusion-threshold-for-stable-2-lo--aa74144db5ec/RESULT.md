# The thirteen-voter Condorcet exclusion threshold for stable \(2\)-lotteries

## Finding

Let \(C=\{A,B,C\}\) be three alternatives with strict rankings from \(n\ge1\) voters. A *stable \(2\)-lottery* is a minimizer of the standard two-defender/one-attacker Condorcet game defined below, with independent defender draws and the uniform-copy convention for tied alternative names. Then:

1. If \(n\le12\), every stable \(2\)-lottery assigns **positive probability** to any strict Condorcet winner.
2. At \(n=13\), a strict Condorcet winner can receive probability zero. Indeed, the profile consisting of one \(A\succ C\succ B\) ballot, six \(B\succ A\succ C\) ballots, and six \(C\succ A\succ B\) ballots has strict Condorcet winner \(A\) by margins \(7\) to \(6\) against both opponents. Its **unique** stable \(2\)-lottery is

\[
D(A)=0,\qquad D(B)=\frac5{13},\qquad D(C)=\frac8{13}.
\]

Thus thirteen is the sharp electorate threshold for a three-alternative stable \(2\)-lottery to exclude a strict Condorcet winner from its support. The sharp threshold, not the qualitative possibility of exclusion, is the contribution: an earlier symmetric construction already yields exclusion with eighteen voters.

## Assumptions and scope

There are exactly three named alternatives, \(n\) equally weighted voters, and a complete strict ranking for each voter. Write \(D\in\Delta(C)\) for a probability vector. The defender draws two alternatives independently from \(D\); the attacker chooses an alternative. Following the continuous-rank convention for stable lotteries, duplicates of the same alternative are treated as independent uniformly positioned copies within that alternative's probability interval. The attacker wins when its copy is preferred by a uniformly drawn voter to both defender copies. These tie semantics are essential; replacing them by literal strict comparison of repeated alternative *names* defines another game.

For voter \(v\) and attacker \(x\), put \(z=D(x)\) and \(L_v(x)=\sum_{y: x\succ_v y}D(y)\). The attacker's expected winning probability is

\[
H_x(D)=\frac1n\sum_{v=1}^{n}F(L_v(x),z),\qquad
F(\ell,z)=\ell^2+\ell z+\frac{z^2}{3}.
\]

The formula holds also at \(z=0\). A stable \(2\)-lottery minimizes \(\max_{x\in C}H_x(D)\). The standard fixed-point existence theorem for stable lotteries implies that the minimum is \(1/3\). The proof below also gives the elementary lower bound \(1/3\) directly.

A strict Condorcet winner is an alternative preferred to each other alternative by strictly more than half the voters. The assertion concerns support of **every** minimizer at small electorates, rather than merely existence of one minimizer supporting the winner.

## Proof

**1. Payoff identity and minimax level.** Place the alternatives' probability masses as ordered consecutive intervals along each voter's unit rank line, with less-preferred candidates first. A uniform copy of attacker \(x\) has rank \(r\) uniformly in its interval \([\ell,\ell+z]\). It beats two independent defender samples with probability \(r^2\), whose average is \(F(\ell,z)=z^{-1}\int_\ell^{\ell+z}r^2\,dr\), with continuous extension at \(z=0\). Consequently, for every \(D\),

\[
\sum_{x\in C}D(x)H_x(D)=\int_0^1 r^2\,dr=\frac13,
\]

hence \(\max_xH_x(D)\ge1/3\). The standard stable-lottery minimax theorem (Cai et al., 2026, Theorem 3, or its general \(g\)-stable form Theorem 4) supplies a \(D\) with all \(H_x(D)\le1/3\). Thus \(D\) is stable exactly when all three payoffs are at most \(1/3\). Any supported candidate then has payoff exactly \(1/3\) by the weighted identity.

**2. Consequences of omitting the Condorcet winner.** Suppose \(A\) is a strict Condorcet winner and a stable \(D\) has \(D(A)=0\). Both \(B,C\) must have positive mass: otherwise \(H_A(D)\) is the proportion preferring \(A\) over the sole supported candidate, which exceeds \(1/2\). Put \(D(B)=x\in(0,1)\), \(D(C)=1-x\). Let \(u\) be the integer number of voters ranking \(B\) above \(C\). The payoff formula gives

\[
H_B(D)=\frac un(1-x)+\frac{x^2}{3}.
\]

Since both supported payoffs equal \(1/3\), one obtains

\[
(x-1)\left(x-\frac{3u-n}{n}\right)=0,
\qquad\text{hence}\qquad x=\frac{3u-n}{n}.
\]

For odd \(n\), integrality of \(u\) therefore forces \(\lvert x-1/2\rvert\ge3/(2n)\). For even \(n\), the weaker \(\lvert x-1/2\rvert\ge0\) suffices.

**3. Universal lower bounds on the omitted winner's payoff.** Let \(k=\lfloor n/2\rfloor+1\), \(t\) be the number of ballots ranking \(A\) first, \(b\) the number ranking \(B\succ A\succ C\), and \(c\) the number ranking \(C\succ A\succ B\). Condorcet victories imply \(t+b\ge k\), \(t+c\ge k\). As \(t+b+c\le n\), necessarily \(t\ge2k-n\). Since \(D(A)=0\),

\[
H_A(D)=\frac{t+b(1-x)^2+cx^2}{n}.
\]

If \(t\ge k\), this already exceeds \(1/3\). Otherwise, since \(b,c\ge k-t\) and \(h=x^2+(1-x)^2\le1\),

\[
H_A(D)\ge\frac{t+(k-t)h}{n}\ge\frac{(2k-n)+(n-k)h}{n}.
\]

For even \(n\ge2\), \(2k-n=2\), \(h\ge1/2\), and hence

\[
H_A(D)\ge\frac{n+6}{4n}\quad\text{(even }n\text{)}.
\]

For odd \(n\ge3\), \(2k-n=1\) and the integer grid constraint above yields \(h\ge1/2+9/(2n^2)\), giving

\[
H_A(D)\ge\frac{n+3}{4n}+\frac{9(n-1)}{4n^3}
\quad\text{(odd }n\text{)}.
\]

For even \(n\le12\), the first bound is at least \(3/8>1/3\). For odd \(n\le11\), the second is at least \(446/1331>1/3\) (the right side decreases for integers \(n\ge3\)); the single-voter case is immediate. Thus an excluded strict Condorcet winner contradicts stability whenever \(n\le12\).

**4. A thirteen-voter example.** For the stated profile and \(D_0=(0,5/13,8/13)\), direct substitution gives

\[
H_A(D_0)=\frac{703}{2197}<\frac13,
\qquad H_B(D_0)=H_C(D_0)=\frac13.
\]

The payoff identity and minimax threshold prove \(D_0\) stable, while \(A\) beats each opponent on seven of thirteen ballots.

**5. Uniqueness at that profile.** Let an arbitrary stable distribution have weights \(D=(1-b-c,b,c)\) with \(0\le b,c\), \(b+c\le1\). For these ballots the exact formulas are

\[
H_B(D)=\frac6{13}(1-b)+\frac{b^2}{3},\qquad
H_C(D)=\frac1{13}\left(6-6c+b^2+bc+\frac{13c^2}{3}\right).
\]

The inequality \(H_B(D)\le1/3\) is equivalent to \((b-1)(13b-5)\le0\), so \(b\ge5/13\). On the feasible region with this restriction,

\[
\frac{\partial H_C}{\partial c}=\frac{-6+b+26c/3}{13}
\le\frac{8-23b}{39}<0.
\]

Therefore \(H_C(b,c)\ge H_C(b,1-b)\), and

\[
H_C(b,1-b)-\frac13=\frac{b(13b-5)}{39}\ge0.
\]

The requirement \(H_C(b,c)\le1/3\) forces equality throughout: \(b=5/13\), \(c=1-b=8/13\), and \(D(A)=0\). Thus \(D_0\) is the unique stable lottery. \(\square\)

## Verification

Run `python3 verify.py` from this extracted package. It uses exact Python integer and rational arithmetic, checks the rank-interval payoff identities on a rational simplex grid, evaluates all anonymous strict three-alternative profiles with up to thirteen voters, and confirms the thirteen-voter witness. In the exhaustive finite check, among anonymous profiles with \(A\) a strict Condorcet winner, exactly two thirteen-voter profiles (related by swapping the last two rankings of the single top-\(A\) ballot) admit a stable lottery excluding \(A\), and none of the smaller electorates do. In the thirteen-voter case, \(2688\) anonymous profiles have \(A\) as strict Condorcet winner and \(1288\) give an interior two-candidate stationary solution before the attacker-\(A\) inequality is applied.

The universal theorem is proved in Sections 1–5, not inferred from finite enumeration. The verifier also reconstructs the earlier symmetric eighteen-voter example discussed below.

## Relationship to prior work

Cai, Charikar, Hastings, Ramakrishnan, Wang and Ye (2026) define the precise minimax and rank-copy conventions for stable \(k\)-lotteries and establish universal existence, stationarity, and distortion guarantees. Their Appendix A, specialized to two alternatives outside the excluded candidate and \(k=2\), **already gives qualitative Condorcet exclusion**: one can take eighteen voters with one \(A\succ B\succ C\), one \(A\succ C\succ B\), eight \(B\succ A\succ C\), and eight \(C\succ A\succ B\); then \((0,1/2,1/2)\) is stable and \(A\) wins both pairwise contests. The present result does not claim that the existence of such an exclusion is new. It adds an exact lower bound on the number of voters, a thirteen-voter example, and uniqueness of its stable lottery, none of which are derived in that Appendix.

Charikar, Ramakrishnan, Tan and Wang (2025) develop stable lotteries and their representation in the context of tournament voting and metric distortion, without the three-alternative sharp finite Condorcet-support threshold. Cheng, Jiang, Munagala and Wang (2019/2020) introduce lottery stability for committee selection under a different committee-distribution formulation. The independent-sampling/rank-copy convention here follows the later paper; conflating these models could invalidate an equivalence claim.

## Limitations

The sharp electorate cutoff is proved for exactly three alternatives, strictly ranked ballots and the independent-draw stable \(2\)-lottery minimax model with uniform rank copies. It need not apply to four or more alternatives, other activation functions, or stable lotteries over distinct two-element committees without replacement. The exact-exclusion example concerns probability support, not metric distortion or manipulation. Equivalence to unindexed prior work remains a publication-priority risk. This is an analytical proof with supplementary exact finite checks; no independent audit has been performed.

## References

1. Z. Cai, M. Charikar, J. Hastings, P. Ramakrishnan, K. Wang and Q. Ye, *Stable Voting Rules on the Edge of Optimal Metric Distortion*, arXiv:2609.08259v1 (first public September 8, 2026), Sections 3 and 5, Appendix A. https://arxiv.org/html/2609.08259v1
2. M. Charikar, P. Ramakrishnan, Z. Tan and K. Wang, *Metric Distortion for Tournament Voting and Beyond*, arXiv:2505.13630v1 (May 19, 2025), Sections 5.1–5.2. https://arxiv.org/pdf/2505.13630
3. Y. Cheng, Z. Jiang, K. Munagala and K. Wang, *Group Fairness in Committee Selection*, arXiv:1905.04438 (first public May 11, 2019), Sections 1–2. https://arxiv.org/abs/1905.04438
