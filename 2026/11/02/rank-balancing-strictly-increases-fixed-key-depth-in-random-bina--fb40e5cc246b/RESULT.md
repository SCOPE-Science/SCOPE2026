# Rank balancing strictly increases fixed-key depth in random binary search trees

## Finding
Let \(D_{n,i}\) be the edge depth of key \(i\) in a uniformly random permutation-built binary search tree with \(n\ge3\) keys. For every integer \(1\le i<n/2\),
\[
\Pr\{D_{n,i+1}\ge t\}>\Pr\{D_{n,i}\ge t\}\qquad(2\le t\le n-1).
\]
At thresholds \(t=0,1,n\), the tail probabilities agree. The laws are symmetric under \(i\mapsto n+1-i\), and for even \(n\) the two central laws coincide. Thus moving a searched key one rank toward the center strictly increases every nontrivial upper tail of its search depth. The exact adjacent transport distance, for \(1\le i\le\lfloor n/2\rfloor\), is
\[
W_1\bigl(\mathcal L(D_{n,i}),\mathcal L(D_{n,i+1})\bigr)
=\frac1{i+1}-\frac1{n+1-i}.
\]
The identity includes the central equality when \(n\) is even.

## Assumptions and scope
The keys are exactly \(1,\ldots,n\). All \(n!\) insertion orders are equiprobable. Depth counts tree edges from the root, so the root has depth zero. The statement concerns a fixed *key rank*, not a uniformly sampled node or insertion-time rank. All comparisons are exact for finite \(n\); no asymptotic or independence assumption on the depths of different keys is made. Define \(C_r\), for \(r\ge0\), as the number of lower records of a uniform permutation of \(r\) values, with \(C_0=0\). Its probability generating polynomial is
\[
\mathbb E[z^{C_r}]=\prod_{j=1}^{r}\frac{z+j-1}{j}.
\]
Independent copies of \(C_r\) can be realized using independent Bernoulli variables with success probabilities \(1,1/2,\ldots,1/r\).

## Proof
**Priority–record representation.** Assign independent continuous uniform priorities \(U_1,\ldots,U_n\) and insert in increasing priority order. Condition on \(U_i=u\) where \(0<u<1\). There are \(a=i-1\) keys on the left and \(b=n-i\) on the right. Among them the numbers with priorities below \(u\) are independent \(X\sim\operatorname{Bin}(a,u)\) and \(Y\sim\operatorname{Bin}(b,u)\). Scanning keys away from \(i\), a key is an ancestor of \(i\) precisely if its priority is below \(u\) and is a record minimum among the intervening keys. Conditional on \((X,Y)=(x,y)\), the two sides give independent record counts with distributions \(C_x\) and \(C_y\). Therefore
\[
D_{n,i}\mid U_i=u\ \overset d=\ C_X+C_Y.
\]
This also gives the exact finite generating function by integrating binomial factors:
\[
\mathbb E[z^{D_{n,i}}]=\frac1{n!}\sum_{r=0}^{a}\sum_{s=0}^{b}\binom ar\binom bs(r+s)!(n-1-r-s)!\,\mathbb E[z^{C_r}]\mathbb E[z^{C_s}].
\]

**Adjacent-rank comparison.** Fix an integer \(i\le n/2\). In a common construction conditional on \(u\), take independent \(X\sim\operatorname{Bin}(a,u)\), \(Y\sim\operatorname{Bin}(b-1,u)\), and \(Z\sim\operatorname{Bernoulli}(u)\). The laws for ranks \(i\) and \(i+1\) are \(C_X+C_{Y+Z}\) and \(C_{X+Z}+C_Y\), respectively. If \(Z=0\) they agree. If \(Z=1\), the record increment identity \(C_{r+1}\overset d=C_r+B_{r+1}\), with \(B_{r+1}\sim\operatorname{Bernoulli}(1/(r+1))\) independent, shows that, conditional on \(X=x,Y=y\), the difference in the expectation of any increasing real function \(f\) (new rank minus old rank) is
\[
\left(\frac1{x+1}-\frac1{y+1}\right)q_f(x,y),\qquad
q_f(x,y)=\mathbb E[f(C_x+C_y+1)-f(C_x+C_y)]\ge0.
\]
The nonnegative term \(q_f\) is symmetric in \(x,y\). Write \(p_a(x)=\Pr\{\operatorname{Bin}(a,u)=x\}\). For \(a\le b-1\), a binomial family has monotone likelihood ratios in its number-of-trials parameter, so
\[
p_a(x)p_{b-1}(y)-p_a(y)p_{b-1}(x)\ge0\qquad(x<y).
\]
Indeed, on their common support the ratio \(p_{b-1}(r)/p_a(r)\) is nondecreasing in \(r\), as its successive ratio is \((b-1-r)/(a-r)\ge1\). Terms outside the smaller support are handled by zero binomial masses. Pairing summands indexed by \((x,y)\) and \((y,x)\), every pair contributes a nonnegative value; hence for every increasing \(f\), \(\mathbb E f(D_{n,i+1})\ge\mathbb E f(D_{n,i})\).

For strictness assume \(i<n/2\), so \(a<b-1\), and choose \(f(d)=\mathbf1\{d\ge t\}\). The factor \(q_f(x,y)=\Pr(C_x+C_y=t-1)\) is positive whenever \(t-1\) lies in its attainable support. For \(t=2\), the pair \((x,y)=(0,1)\) works. For \(3\le t\le n-1\), if \(a=0\), use \((0,t-1)\); if \(a\ge1\), use \((a,b-1)\), because \(C_a+C_{b-1}\) has positive mass at every integer from \(2\) to \(n-2\). In each case the paired binomial mass inequality is strict and all factors are positive for every \(u\in(0,1)\). Integrating over \(u\) proves the stated strict tail inequalities.

Reflection reverses the key order without changing tree law, giving \(D_{n,i}\overset d=D_{n,n+1-i}\). If \(n\) is even and \(i=n/2\), the two binomial trial counts match and hence the laws coincide. Tails at \(t=0,1,n\) also agree: probabilities are one, \((n-1)/n\), and zero respectively (since every key is the root with probability \(1/n\)).

**Exact transport.** The known mean-depth identity, also following by summing ancestor probabilities, is \(\mathbb ED_{n,i}=H_i+H_{n+1-i}-2\), where \(H_m=\sum_{j=1}^m1/j\). Stochastic dominance on the real line makes the 1-Wasserstein distance equal to the difference of expectations; subtracting the harmonic numbers gives \(1/(i+1)-1/(n+1-i)\), as claimed.

## Verification
The standalone Python 3 script `verify_bst_rank_depth.py` uses exact rational arithmetic. It compares three independently specified formulas: a root-decomposition recurrence, a mixed binomial/record generating function, and exhaustive insertion permutations. The checked range is all rank and adjacent-tail comparisons through \(n=24\), the mixed formula through \(n=12\), and full enumeration through \(n=8\). It checks the exact transport formula and boundary equalities and finishes with 6,500 passed assertions. These finite checks test the proof's statements; the pairing argument above proves the all-size theorem.

## Relationship to prior work
Grübel and Stefanoski (2005), Theorem 1, established an exact hypergeometric/record-count description of the fixed-key depth law, and reproduced the classical expectation \(H_i+H_{n+1-i}-2\). That exact representation, its marginal and its asymptotic Poisson approximations are not new here. The contribution is a simultaneous *cross-rank*, finite-sample, strict first-order stochastic comparison for all nontrivial depth thresholds, with an exact transport consequence, proved by coupling and antisymmetric binomial likelihood-ratio pairing. Devroye and Hwang (2006) analyze random BST profile widths rather than fixed-key rankwise stochastic ordering. Related earlier recursive-call/variance analyses are acknowledged as possible historical overlap risks.

## Limitations
The theorem addresses random permutation-built BSTs, not arbitrary search-tree distributions, weighted keys, or the joint depth vector. It does not claim likelihood-ratio ordering of the resulting depth laws, nor a positive almost-sure coupling of depths within one common tree. Stronger prior work outside the inspected sources could imply the ordering; no claim of independently verified historical priority is made.

## References
- R. Grübel and N. Stefanoski, *Mixed Poisson approximation of node depth distributions in random binary search trees*, Annals of Applied Probability 15 (2005), 279–297. [arXiv:math/0503738v1](https://arxiv.org/abs/math/0503738), first posted 2005-03-31; DOI: 10.1214/105051604000000611.
- L. Devroye and H.-K. Hwang, *Width and mode of the profile for some random trees of logarithmic height*, Annals of Applied Probability 16 (2006), 886–918. [arXiv:math/0607119v1](https://arxiv.org/abs/math/0607119), first posted 2006-07-05; primary MSC 60C05.
- P. Kirschenhofer and H. Prodinger, *Comparisons in Hoare's Find algorithm*, Combinatorics, Probability and Computing 7 (1998), 111–120. DOI: 10.1017/S0963548397003325. Publisher abstract reviewed; complete text unavailable in this examination.
