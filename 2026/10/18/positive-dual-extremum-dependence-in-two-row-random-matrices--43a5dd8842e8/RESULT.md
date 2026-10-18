# Positive dual-extremum dependence in two-row random matrices

## Finding
Let \(A\) be an independent, identically distributed continuous \(2\times n\) random array, \(n\ge2\). Define \(K_+\) and \(K_-\) to be the numbers of cells that are, respectively, simultaneously a strict maximum and a strict minimum in both their row and their column. Set
\[
p_n=\frac{n-1}{n+1},\qquad q_n=\frac{((n-1)!)^2}{(2n)!},\qquad
C_n=\frac{4(n^2+4n+1)}{n(n-1)(n+1)^2(n+2)}-\frac{2n(n+1)}{n-1}q_n.
\]
Then both counts belong to \(\{1,2\}\); their full joint law is
\[
\begin{array}{c|cc}
 & K_-=1 & K_-=2\\ \hline
K_+=1 & (1-p_n)^2+C_n & p_n(1-p_n)-C_n\\
K_+=2 & p_n(1-p_n)-C_n & p_n^2+C_n
\end{array}
\]
In particular, \(\operatorname{Cov}(K_+,K_-)=C_n>0\) for every \(n\ge2\), while
\[
\operatorname{Cov}(K_+,K_-)=\frac4{n^3}(1+O(n^{-1})),\qquad
\operatorname{Corr}(K_+,K_-)=\frac2{n^2}(1+O(n^{-1})).
\]
The marginal law is included for orientation, not claimed as new. The contribution is the precise joint dependence and its strictly positive, decaying correlation.

## Assumptions and scope
The entries are independent and identically distributed from any continuous distribution; only their relative ranks matter. Rows are labeled and there are exactly two; the number of columns is an arbitrary integer \(n\ge2\). All comparisons are strict almost surely. The formula does not extend without separate analysis to nonidentically distributed entries or three or more rows. A cell counted by \(K_+\) is a common-best-response pure equilibrium in the associated common-payoff matrix game; \(K_-\) is the same after payoff reversal.

## Proof
By the probability integral transform and absence of ties, use independent uniform entries on \((0,1)\). A global maximum is a row/column maximum, and at most one maximum occurs per row, hence \(K_+\in\{1,2\}\). Likewise for minima. A fixed cell is the largest among its row/column union, which contains \(n+1\) cells, and so \(\mathbb E K_+=\mathbb E K_-=2n/(n+1)\). Consequently both indicators \(K_+-1\) and \(K_--1\) are Bernoulli with success probability \(p_n\). These marginals also follow from Roberts's general coordination-matrix formula.

For the cross moment select a cell \(u\) counted by \(K_+\) and a distinct cell \(v\) counted by \(K_-\). They cannot coincide. Write \(x\) for the value at \(u\) and \(y\) at \(v\); necessarily \(0<y<x<1\). There are three relative positions. If they share a row, the probability of their joint event is
\[
S_r=\int_0^1\int_0^x x(1-y)(x-y)^{n-2}\,dy\,dx
=\frac{n^2+n-1}{(n-1)n(n+1)(n+2)}.
\]
If they share a column, it is
\[
S_c=\int_0^1\int_0^x x^{n-1}(1-y)^{n-1}\,dy\,dx
=\frac1{n^2}-q_n.
\]
If they share neither, the two crossed cells must both have values strictly between \(y\) and \(x\); the remaining entries of the two relevant rows yield
\[
D_n=\int_0^1\int_0^x x^{n-2}(1-y)^{n-2}(x-y)^2\,dy\,dx.
\]
Expanding \((1-y)^{n-2}\) gives the independently evaluable finite sum
\[
D_n=\sum_{j=0}^{n-2}\frac{2(-1)^j\binom{n-2}{j}}{(j+1)(j+2)(j+3)(n+j+2)}.
\]
Ordinary beta-integral simplification gives
\[
D_n=\frac1{(n+1)(n-1)}-\frac2{(n-1)n^2}
+\frac2{(n-1)^2n(n+1)}-\frac{2q_n}{(n-1)^2}.
\]
There are \(2n(n-1)\) ordered maximum/minimum cell pairs sharing a row, \(2n\) sharing a column, and \(2n(n-1)\) sharing neither. Hence
\[
\mathbb E[K_+K_-]=2n\{(n-1)S_r+S_c+(n-1)D_n\}.
\]
Substitution and subtraction of \((2n/(n+1))^2\) give the displayed covariance \(C_n\). Since both counts are Bernoulli shifts, the covariance and marginal probabilities determine the full \(2\times2\) probability table.

For strict positivity, note \(q_n=1/(n^2\binom{2n}{n})\). The inequality \(C_n>0\) is equivalent to
\[
\binom{2n}{n}>\frac{(n+1)^3(n+2)}{2(n^2+4n+1)}.
\]
For \(n\ge2\), \(\binom{2n}{n}\ge(n+1)(n+2)/2\), initially equal at \(n=2\), then following by induction from the ratios \(\binom{2n+2}{n+1}/\binom{2n}{n}=2(2n+1)/(n+1)\). The latter lower bound is strictly larger than the required right side because \(n^2+4n+1>(n+1)^2\). This proves positivity uniformly.

Finally, \(q_n\) is exponentially small by the central-binomial bound or Stirling's formula. The rational term is \(4n^{-3}(1+O(n^{-1}))\); dividing by \(p_n(1-p_n)=2(n-1)/(n+1)^2\) establishes the correlation asymptotic.

## Verification
The standalone `verify_joint_extrema.py` enumerates the rank permutations of all arrays of dimensions \(2\times n\) for \(n=2,3,4\), and compares their exact joint probabilities to the formula. It also uses independent rational beta-binomial expansions of each pair-event integral to test the symbolic closed form through \(n=44\), and tests positivity and probability-table bounds through \(n=149\). The script completed with 351 exact assertions. The finite checks do not replace the unrestricted proof above.

## Relationship to prior work
Roberts (2005), *Pure Nash Equilibria of Coordination Matrix Games*, supplies the complete **marginal** law for the number of row-and-column maxima in a uniform-rank random matrix; applying it to negated entries supplies the minima marginal. Its formulas and payoff-ranking results do not specify the joint distribution of the two counts. Bhamidi, Dey and Nobel (first arXiv submission November 10, 2012) study local maximizers of Gaussian submatrix **row/column sums** and count their local optima. In their \(1\times1\) special case local optimality resembles a simultaneously maximal cell; their results neither concern the dual minimum count nor the exact two-row bivariate distribution. Thus no coverage by the cited claims has been identified, but priority is not independently certified.

## Limitations
Only two rows are covered. No corresponding general rectangular joint law, higher-dimensional limit, or inference procedure is asserted. Earlier work might encode the bivariate formula implicitly; historical priority has not been exhaustively certified. The existence of positive covariance does not imply positive association of all functions of the underlying array.

## References
1. D. P. Roberts, *Pure Nash Equilibria of Coordination Matrix Games*, Economics Letters 89 (2005), 7–11, doi:10.1016/j.econlet.2005.01.024. An author-prepublication version is available from the University of Minnesota Morris Digital Well, https://digitalcommons.morris.umn.edu/mathematics/19/ .
2. S. Bhamidi, P. S. Dey, and A. B. Nobel, *Energy Landscape for large average submatrix detection problems in Gaussian random matrices*, arXiv:1211.2284v1, first posted November 10, 2012, https://arxiv.org/abs/1211.2284 .
