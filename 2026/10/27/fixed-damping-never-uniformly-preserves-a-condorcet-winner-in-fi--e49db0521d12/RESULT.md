# Fixed damping never uniformly preserves a Condorcet winner in five-alternative BallotRank

## Finding
For every real damping parameter \(0<d<1\), there is a finite profile of strict rankings of **five alternatives** possessing a unique strict Condorcet winner \(A\) for which the BallotRank score of another alternative \(B\) is strictly greater than that of \(A\). This holds for the self-loop normalization of Todd and Volić's BallotRank, not merely for ordinary PageRank.

More precisely, the explicit \((24k+1)\)-voter profile below, for integers \(k\ge1\), has \(A\) beating all four opponents by **exactly one vote**. Let \(s_k(d)\) be its BallotRank vector with candidate order \((A,B,C,D,E)\). For each fixed \(0<d<1\),
\[
\lim_{k\to\infty}s_{k,A}(d)=\frac15,
\qquad
\lim_{k\to\infty}s_{k,B}(d)=
\frac{d^3+5d^2+6d+4}{5(d^3+4d^2+4d+4)},
\]
so that
\[
\boxed{\lim_{k\to\infty}\bigl(s_{k,B}(d)-s_{k,A}(d)\bigr)=
\frac{d(d+2)}{5(d^3+4d^2+4d+4)}>0.}
\]
Consequently, for every fixed \(0<d<1\) there is an integer \(k_0(d)\) such that \(B\) strictly outscores the Condorcet winner for all \(k\ge k_0(d)\).

At the conventional damping \(d=17/20\), the explicitly generated \(601\)-voter profile with \(k=25\) already satisfies
\[
 s_{25,B}(17/20)-s_{25,A}(17/20)
 =\frac{2462202045070872571152}{1625203582777781791390465}>0.
\]
For each **fixed** \(k\), however, \(\lim_{d\uparrow1}s_k(d)=(1,0,0,0,0)\). Therefore the high-damping and large-electorate limits do not commute: the limiting score of \(A\) is respectively \(1\) or \(1/5\), depending on the order of limits.

## Assumptions and scope
Every ballot is a complete strict linear ordering of \(\{A,B,C,D,E\}\). For distinct alternatives \(X,Y\), let \(m(X,Y)\) be the number of ballots ranking \(X\) above \(Y\) minus the number ranking \(Y\) above \(X\). Write \(w(X,Y)=\max\{m(X,Y),0\}\) for \(X\ne Y\), \(W_X=\sum_{Y\ne X}w(X,Y)\), and \(W=\sum_X W_X\). Add the **BallotRank-specific self-loop** \(w(X,X)=W_X/W\). Define the column-stochastic matrix \(L\) by
\[
L_{XY}=\frac{w(X,Y)}{\sum_Z w(Z,Y)}.
\]
All columns of the constructed profiles have strictly positive denominators. For \(0<d<1\), the BallotRank vector is the unique solution
\[
 s(d)=\frac{1-d}{5}\mathbf1+dLs(d)
 =\frac{1-d}{5}(I-dL)^{-1}\mathbf1.
\]
The statement concerns fixed positive damping strictly below one and finite ranked electorates of unrestricted size. It does **not** assert a universal finite electorate bound or failure at \(d=1\).

The construction uses the following six strict majority orientations among the four runners:
\[
B\succ C,\quad B\succ D,\quad E\succ B,\quad
C\succ D,\quad C\succ E,\quad D\succ E.
\]
For each oriented pair \(X\succ Y\), list the other two runners as \(Z_1,Z_2\), and take the pair of ballots
\[
X\succ Y\succ Z_1\succ Z_2,
\qquad
Z_2\succ Z_1\succ X\succ Y.
\]
Repeat this two-ballot gadget \(k\) times for each of the six orientations. For **each** of these \(12k\) four-runner ballots \(\sigma\), include both \(A\succ\sigma\) and \(\sigma\succ A\). Finally add one ballot \(A\succ B\succ C\succ D\succ E\). The result has \(24k+1\) voters.

## Proof
**1. Exact majority margins.** The two-ballot gadget for \(X\succ Y\) creates a margin of \(2\) on that pair and zero margins on all other runner pairs; this is verified by reversing the order of the two remaining alternatives in the second ballot. Adding \(A\) at opposite ends of every paired copy doubles all runner margins and cancels every comparison with \(A\). The final ballot makes \(A\) beat each runner by one vote. Each of the six listed runner victories then has margin \(4k+1\), except \(E\succ B\), whose margin is \(4k-1\). In particular, every margin is strict for \(k\ge1\), and \(A\) is the unique strict Condorcet winner.

**2. Limiting transition matrix.** The outgoing win total \(W_X\) is nonnegative, and \(0\le w(X,X)\le1\) for each candidate. Every runner has one or two incoming runner victories of magnitude \(4k+O(1)\), whereas its incoming loss margin to \(A\) is just \(1\) and its self-loop weight is at most \(1\). Thus, as \(k\to\infty\), each runner column sends asymptotically equal mass to the runner candidates that beat it; its transition to \(A\) and its self-loop vanish. The column of \(A\) is **exactly** \(e_A\) for every \(k\), because \(A\) has no pairwise defeats and has a positive self-loop. In order \((A,B,C,D,E)\), therefore,
\[
L_k\longrightarrow
L_\infty=\begin{pmatrix}
1&0&0&0&0\\
0&0&1&1/2&0\\
0&0&0&1/2&1/2\\
0&0&0&0&1/2\\
0&1&0&0&0
\end{pmatrix}.
\]
Its lower-right \(4\times4\) block \(P\) is column-stochastic.

**3. Exact damped limit.** Since every \(L_k\) and \(L_\infty\) is column-stochastic and nonnegative, their induced matrix \(1\)-norm equals \(1\). Thus \(I-dL\) is invertible for all \(0<d<1\), with inverse \(\sum_{r\ge0}d^rL^r\), and inversion is continuous as \(k\to\infty\). The limiting BallotRank vector solves
\[
 s_\infty=\frac{1-d}{5}\mathbf1+dL_\infty s_\infty.
\]
Its \(A\)-coordinate is \(1/5\). Setting \(t=(1-d)/5\) and denoting the other coordinates by \(b,c,f,e\), the remaining equations are
\[
 b=t+d(c+f/2),\quad
 c=t+d(f+e)/2,\quad
 f=t+de/2,\quad
 e=t+db.
\]
Elementary elimination gives
\[
 b=\frac{d^3+5d^2+6d+4}{5(d^3+4d^2+4d+4)}.
\]
Subtracting \(1/5\) yields the strictly positive gap stated above. Continuity implies eventual **strict** inequality for every fixed \(d\in(0,1)\).

**4. Reversed limits.** For every finite \(k\), every runner has a positive transition directly to \(A\), while \(A\) is absorbing. Hence the \(d=1\) chain has the unique stationary distribution \(e_A\) and \(L_k^r\mathbf1/5\to e_A\). Its Abel means, namely \((1-d)\sum_{r\ge0}d^rL_k^r\mathbf1/5\), also converge to \(e_A\) as \(d\uparrow1\). In the other order, the limiting \(A\)-coordinate was shown to be \(1/5\) for every \(d<1\). This proves the noncommutativity.

## Verification
The standalone file `verify_ballotrank.py` reconstructs every ballot from the six pair gadgets, computes majority margins, adds precisely the self-loop weights of BallotRank, column-normalizes, and solves the damped stationary system using exact rational Gaussian elimination. Execute `python verify_ballotrank.py` using Python 3 with no third-party packages. Its exact assertions include all specified majority margins for seven values of \(k\), the \(601\)-voter witness at \(d=17/20\), five additional damping/witness pairs, and the rational limiting gap identity. These are finite corroborations; the general universal quantifier and noncommuting limits are proved above by matrix convergence and absorbing-state arguments.

## Relationship to prior work
Todd and Volić (2026, arXiv:2601.14015) define the specific self-loop-weighted BallotRank matrix used here, establish Condorcet consistency at undamped \(d=1\), and report successful empirical identification at positive damping. They explicitly note that positive damping does not come with a general guarantee and propose analyzing extremal examples at fixed damping. The present result supplies a uniformly parameterized constructive answer for **every** \(d<1\), with only five alternatives, an exact limiting gap, and noncommuting limits. Their qualitative caution is prior context, not claimed as novel.

Bana, Jamroga, Naccache, and Ryan (2021, arXiv:2102.01995) define convergence voting with a different comparison-weighted transition matrix, which can fail to choose a Condorcet winner. That failure does not imply the exact counterexample for the different BallotRank self-loop normalization. The paired-ballot isolation idea is a standard McGarvey-style gadget and is used only as a construction ingredient, not claimed as a new technique.

## Limitations
This construction gives no smallest voter count for failure at any chosen \(d\), no claim about how frequently the phenomenon appears in observed elections, and no proof that five alternatives are the minimum necessary. Its worst-case margin pattern makes \(A\)'s victories narrow and runner-to-runner margins large; these may not represent typical electoral data. Independent validation and exhaustive historical priority checking have not been performed.

## References
1. J. D. Todd and I. Volić, *BallotRank: A Condorcet Completion Method for Graphs*, arXiv:2601.14015, first submitted 20 January 2026. https://arxiv.org/abs/2601.14015 ; full text https://arxiv.org/html/2601.14015v2 .
2. G. Bana, W. Jamroga, D. Naccache, and P. Y. A. Ryan, *Convergence Voting: From Pairwise Comparisons to Consensus*, arXiv:2102.01995, 2021. https://arxiv.org/abs/2102.01995 .
3. D. C. McGarvey, *A Theorem on the Construction of Voting Paradoxes*, Econometrica 21 (1953), 608–610, DOI:10.2307/1907926.
