# Strict arithmetic-progression/run anticorrelation in uniform fixed-size random sets

## Finding

Let \(S\) be a uniformly chosen \(k\)-element subset of \([n]=\{1,\ldots,n\}\). For each integer \(\ell\ge3\), let \(X_\ell\) count the \(\ell\)-term arithmetic progressions of positive common difference wholly contained in \(S\). Let \(R\) count the maximal nonempty intervals of consecutive integers in \(S\) (occupied runs), and let \(Y\) count its adjacent occupied pairs. For **every** \(n\ge4\) and \(3\le\ell\le k\le n-1\),

\[
\operatorname{Cov}(X_\ell,Y)>0,\qquad
\operatorname{Cov}(X_\ell,R)=-\operatorname{Cov}(X_\ell,Y)<0.
\]

There is an exact finite formula for these covariances, involving only \(n,\ell,k\), and a manifestly positive endpoint interpolation (below). For \(k<\ell\) or \(k=n\), both covariances are zero. Negative covariance here **does not** imply decreasing conditional regression: for every \(n\ge5\) and \(k=\ell=3\), the three feasible conditioned means \(\mathbb E[X_3\mid R=r]\) have the form positive, zero, positive as \(r=1,2,3\).

## Assumptions and scope

All \(n,\ell,k\) are integers. The sampling model is a *uniform fixed-cardinality* set, not independent Bernoulli site percolation. Arithmetic progressions are sets of \(\ell\) distinct elements \(a,a+d,\ldots,a+(\ell-1)d\) with integer \(d\ge1\) and final term at most \(n\); they are not taken modulo \(n\). The run statistic counts runs of *selected* integers only, excluding runs of unselected integers. Define

\[
q=\left\lfloor\frac{n-1}{\ell-1}\right\rfloor,\qquad
T=qn-\frac{(\ell-1)q(q+1)}2,
\]

where \(T\) is the number of \(\ell\)-term progressions. For \(s\in\{0,\ldots,n\}\), write

\[
p_s=\frac{(k)_{\underline s}}{(n)_{\underline s}}=\frac{\binom{n-s}{k-s}}{\binom nk}\quad(s\le k),\qquad p_s=0\quad(s>k).
\]

For \(n\ge\ell+2\), also write

\[
D=n(n-\ell+1)-\ell T,\qquad E=\ell T-nq.
\]

## Proof

**1. Hypergeometric overlap identity.** There are \(T\) progression sets and \(n-1\) adjacent pairs. Let \(N_j\) be the number of ordered (progression, adjacent-pair) choices with exactly \(j\in\{0,1,2\}\) shared vertices. An adjacent pair can be contained in a progression only when the common difference is \(1\), giving

\[
N_2=(\ell-1)(n-\ell+1).
\]

The sum of the path degrees of all progression vertices is \(2\ell T-2q\), because each of the two endpoints of \([n]\) belongs to exactly \(q\) progressions. An adjacent pair sharing two vertices contributes twice to this sum, so

\[
N_1=2\ell T-2q-2N_2,\qquad N_0=(n-1)T-N_1-N_2.
\]

For any specified \(s\)-set, its inclusion probability is \(p_s\). Consequently the **exact** covariance is

\[
C_{n,\ell,k}:=\operatorname{Cov}(X_\ell,Y)
=N_2p_\ell+N_1p_{\ell+1}+N_0p_{\ell+2}
-(n-1)Tp_\ell p_2.
\tag{1}
\]

Since each occupied run of length \(b\) contains exactly \(b-1\) occupied adjacent pairs, the identity \(R=k-Y\) holds on every sample, yielding \(\operatorname{Cov}(X_\ell,R)=-C_{n,\ell,k}\).

**2. Two positive endpoint values control every sample size.** Suppose \(n\ge\ell+2\), and \(\ell\le k\le n-1\). Since \(p_\ell>0\), use

\[
\frac{p_{\ell+1}}{p_\ell}=\frac{k-\ell}{n-\ell},\quad
\frac{p_{\ell+2}}{p_\ell}=\frac{(k-\ell)(k-\ell-1)}{(n-\ell)(n-\ell-1)},\quad
p_2=\frac{k(k-1)}{n(n-1)}.
\]

Substituting into (1) makes \(F(k):=C_{n,\ell,k}/p_\ell\) a polynomial in \(k\) of degree at most two. At \(k=n\) all chosen sets are deterministic, so \(F(n)=0\), hence \(G(k)=F(k)/(n-k)\) is affine. Direct substitution at its two endpoints gives

\[
G(\ell)=\frac{(\ell-1)D}{n(n-\ell)},\qquad
G(n-1)=\frac{2E}{n(n-\ell)}.
\]

It follows for the entire domain that

\[
\boxed{
C_{n,\ell,k}=p_\ell\frac{n-k}{n-\ell-1}
\left[(n-1-k)\frac{(\ell-1)D}{n(n-\ell)}
+(k-\ell)\frac{2E}{n(n-\ell)}\right].}
\tag{2}
\]

To establish strict positivity of both endpoints, divide \(n\) by \(\ell-1\) as

\[
n=(\ell-1)q+r,\qquad 1\le r\le\ell-1.
\]

Substituting the expression for \(T\), with exact integer arithmetic, gives

\[
D=\frac{(\ell-2)(q-1)((\ell-1)q+2)}2
+(r-1)\bigl[r+(\ell-2)(q-1)\bigr],
\]

\[
E=\frac{(\ell-1)q}{2}\bigl[(\ell-2)(q-1)+2(r-1)\bigr].
\]

These are nonnegative sums, and both are **strictly** positive whenever \(n\ge\ell+2\), because either \(q\ge2\) or \(r>1\); the excluded pair \((q,r)=(1,1)\) would give \(n=\ell\). Thus the two endpoint values of affine \(G\) are positive, so (2) is strictly positive for every intermediate integer \(k\).

**3. The narrow boundary \(n=\ell+1\).** Here necessarily \(k=\ell\). The only \(\ell\)-term progressions are the two consecutive intervals omitting one endpoint. A random \(\ell\)-set is obtained by deleting one uniformly chosen vertex: \(X_\ell=1\) only when an endpoint is deleted, whereas \(Y=n-2\) in those cases and \(Y=n-3\) otherwise. Therefore

\[
C_{\ell+1,\ell,\ell}=\frac{2(\ell-1)}{(\ell+1)^2}>0.
\]

This completes the proof of strict signs for all allowed parameters. If \(k<\ell\) then \(X_\ell=0\) identically; if \(k=n\) the entire sample is deterministic, so each covariance is zero.

**4. Sharp limit of conditional interpretation.** Take \(k=\ell=3\) and \(n\ge5\). Exactly three selected consecutive positions (\(R=1\)) always form one progression, whereas exactly one adjacent pair (\(R=2\)) prevents any 3-term progression. If \(R=3\), the three sites are mutually nonadjacent; the number of such sets is \(\binom{n-2}{3}\), and the number that are 3-term progressions is \(\lfloor(n-1)^2/4\rfloor-(n-2)>0\). Thus

\[
\mathbb E[X_3\mid R=1]=1,\quad
\mathbb E[X_3\mid R=2]=0,\quad
\mathbb E[X_3\mid R=3]=
\frac{\lfloor(n-1)^2/4\rfloor-(n-2)}{\binom{n-2}{3}}>0.
\]

The negative unconditional covariance therefore cannot be strengthened to a monotonically decreasing conditional mean for every fixed \(k\).

## Verification

The self-contained Python 3 verifier `verify_ap_runs.py` independently (i) exhaustively enumerates all \(k\)-subsets for \(n\le13\), (ii) constructs every progression and its intersections with every adjacent pair, (iii) calculates rational covariances directly, (iv) checks both exact formulae (1) and (2), (v) checks the integer positivity decompositions, and (vi) checks the three-run conditional example. Command:

```
python verify_ap_runs.py --max-n 13
```

Observed output: `PASS: 806 exact assertions (n through 13).` These finite computations are corroboration only; all-size correctness rests on the overlap count and affine-endpoint proof given above.

## Relationship to prior work

Benjamini, Yadin and Zeitouni [1] study extreme-value laws of longest arithmetic progressions in **independent fair Bernoulli subsets**, comparing their marginal scale with longest runs. Their full manuscript's stated main theorems and argument concern extremes and dependence between progression events, not the present exact fixed-cardinality cross-covariance.

Barhoumi-Andréani, Koch and Liu [2] study joint fluctuations of counts of **two progression lengths at least three** in sparse independent Bernoulli subsets. Their bivariate covariance is not a progression-count/adjacent-pair covariance in a uniform fixed-size subset. Fiz Pontiveros, Griffiths, Secco and Serra [3], and Griffiths, Koch and Secco [4], obtain tail bounds for **one** progression count in fixed-size random subsets; these bounds do not specify the joint covariance with occupied runs or imply its strictly negative sign. The general hypergeometric overlap formula is standard counting; the arithmetic-specific overlap numbers and strict uniform positivity are the distinguishing conclusions claimed here.

## Limitations

The result applies to ordinary progressions in an initial integer interval under uniform sampling of a **fixed** number of selected sites, not to progression counts on cyclic groups, nonuniform sampling, independently selected sites or arbitrary hypergraphs. The sign generally need not hold for a single arbitrary 3-set: for \(n=6\), \(k=3\), the indicator of complete containment of \(\{1,3,5\}\) has *negative* covariance with occupied adjacent-pair count. The theorem proves a covariance sign and exact expression, **not** stochastic domination, association of all statistics, or monotone conditional expectation. Finite checking alone does not prove the universal statement; priority may be implicit in wider hypergraph moment treatments not exhaustively available for inspection.

## References

[1] I. Benjamini, A. Yadin and O. Zeitouni, *Maximal Arithmetic Progressions in Random Subsets*, first publicly submitted July 26, 2007; https://arxiv.org/abs/0707.3888 ; complete manuscript https://cims.nyu.edu/~zeitouni/pdf/Arit2407.pdf .

[2] Y. Barhoumi-Andréani, C. Koch and H. Liu, *Bivariate fluctuations for the number of arithmetic progressions in random sets*, 2019; https://arxiv.org/abs/1902.04176 ; full text https://arxiv.org/html/1902.04176v1 .

[3] G. Fiz Pontiveros, S. Griffiths, M. Secco and O. Serra, *Deviation probabilities for arithmetic progressions and other regular discrete structures*, 2019; https://arxiv.org/abs/1910.12835 .

[4] S. Griffiths, C. Koch and M. Secco, *Deviation probabilities for arithmetic progressions and irregular discrete structures*, 2020; https://arxiv.org/abs/2012.09280 .
