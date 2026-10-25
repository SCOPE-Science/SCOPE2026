# Any odd jury size can be uniquely optimal under positively correlated, individually competent votes

## Finding

Consider infinitely many exchangeable binary votes about a binary question with a designated correct answer. Conditionally on a common latent task-specific competence \(P\), votes are mutually independent and each is correct with probability \(P\). Write \(J_m\) for the probability that a simple majority of \(2m+1\) voters is correct, for every integer \(m\ge0\).

**Exact two-environment theorem.** Suppose \(P=p\) with probability \(w\in(0,1)\), and \(P=q\) otherwise, with \(\frac12<p<1\), \(0<q<\frac12\), and \(p+q>1\). Set
\[
 s=p(1-p),\quad t=q(1-q),\quad r=t/s>1,\quad H=\frac{w(2p-1)}{(1-w)(1-2q)}>0.
\]
For every integer \(m\ge0\), the sign of \(J_{m+1}-J_m\) is positive, zero, or negative exactly when \(r^{m+1}<H\), \(r^{m+1}=H\), or \(r^{m+1}>H\), respectively. In particular, majority success is either strictly decreasing, or increases to a finite maximum (attained at one odd size or, in the equality case, at two consecutive odd sizes) and then strictly decreases. The limiting accuracy is \(w\).

**Every odd optimum is possible.** For each integer \(j\ge0\), take \(p=9/10\), \(q=2/5\), \(r=8/3\), \(H_j=(r^j+r^{j+1})/2\), and \(w_j=H_j/(H_j+4)\). Then \(J_j\) is strictly greater than \(J_m\) for every \(m\ne j\); hence the unique optimal odd group size is \(2j+1\). At every size each individual voter is marginally competent (strictly better than a fair coin), and every pair of voter correctness indicators has strictly positive correlation.

**Identical pairwise laws, opposite group-size decisions.** Compare the latent laws \(P\in\{9/10,2/5\}\), with respective probabilities \(7/10,3/10\), and \(P\in\{24/25,1/2\}\), with respective probabilities \(25/46,21/46\). Both have individual mean competence \(3/4\), pairwise correctness-indicator covariance \(21/400\), correlation \(7/25\), and therefore *identical complete joint distributions for any two voters*. Under the first law, the unique optimal odd size is five, with success probability \(19731/25000\). Under the second, success probability is strictly increasing along all odd sizes, with no finite optimum. Thus mean competence and the entire two-voter law do not determine whether to enlarge a jury or even whether a finite optimal size exists.

## Assumptions and scope

The common latent \(P\) is drawn once per task, not independently per voter. The designated correct answer is fixed for that task. Given \(P\), each correctness indicator is an independent Bernoulli variable with success probability \(P\). The same latent law governs all jury sizes, and only odd sizes use unweighted simple majority, eliminating tie-breaking. All probabilities are population probabilities, not sampling estimates. The inequalities concern every integer \(m\ge0\) and all stated admissible real parameters; the explicit constructions have exact rational parameters.

## Proof

For \(u\in(0,1)\) put \(B_m(u)=\Pr(\operatorname{Binomial}(2m+1,u)\ge m+1)\). Couple a \(2m+3\)-voter jury with a \(2m+1\)-voter jury by adding two conditionally independent votes. The decision changes from incorrect to correct precisely when the first \(2m+1\) votes have exactly \(m\) correct and both additions are correct. It changes from correct to incorrect precisely when the first group has exactly \(m+1\) correct and both additions are incorrect. Binomial probabilities give
\[
 B_{m+1}(u)-B_m(u)=\binom{2m+1}{m}[u(1-u)]^{m+1}(2u-1).
\]
Taking expectations over \(P\) proves the master identity
\[
 J_{m+1}-J_m=\binom{2m+1}{m}\mathbb E[(P(1-P))^{m+1}(2P-1)].
\]
For a two-atom law, the expectation is
\[
 w(2p-1)s^{m+1}-(1-w)(1-2q)t^{m+1}
 =(1-w)(1-2q)s^{m+1}(H-r^{m+1}).
\]
Because \(t-s=(p-q)(p+q-1)>0\), one has \(r>1\). The factor outside parentheses is positive. Its sign therefore changes at most once, from positive to negative, with equality at at most one integer. This proves the exact sign law and global maximizer statement. The conditional law of large numbers gives \(\lim_{m\to\infty}J_m=w\), since \(p>1/2>q\).

For the prescribed optimum construction, \(s=9/100\), \(t=6/25\), \(r=8/3\) and \(w_j(2p-1)/((1-w_j)(1-2q))=4w_j/(1-w_j)=H_j\). By construction \(r^j<H_j<r^{j+1}\), so \(J_{m+1}>J_m\) for \(m<j\) and \(J_{m+1}<J_m\) for \(m\ge j\). As \(H_j>1\), \(w_j>1/5\) and the marginal competence \(\mathbb E[P]=2/5+w_j/2>1/2\). For two distinct votes \(X_i,X_k\), conditional independence implies \(\operatorname{Cov}(X_i,X_k)=\operatorname{Var}(P)=w_j(1-w_j)/4>0\). Their correlation is positive because the Bernoulli marginal variance is positive. This proves the arbitrarily prescribed unique optimum.

For the two moment-matched laws, direct rational arithmetic yields in both cases \(\mathbb E[P]=3/4\) and \(\operatorname{Var}(P)=21/400\). The joint distribution of any ordered pair of binary correctness indicators is determined by \(\Pr(X_1=X_2=1)=\mathbb E[P^2]=123/200\), \(\Pr(X_1=1,X_2=0)=\Pr(X_1=0,X_2=1)=27/200\), and \(\Pr(X_1=X_2=0)=23/200\). The first law has \(H=28/3\), and \((8/3)^2<28/3<(8/3)^3\); hence its unique optimum is \(m=2\). Its exact accuracy there is \(J_2=19731/25000\). For the second law, the latent values \(1/2\) and \(24/25\) yield a zero increment and a strictly positive increment, respectively, in the master identity for every \(m\), so \(J_{m+1}>J_m\) always. Its limiting accuracy equals \(21/92+25/46=71/92\). No part of the pairwise-law argument asserts equality of three-voter or higher-order joint distributions.

## Verification

The standalone `verify.py` computes all conditional binomial tails with exact rational arithmetic and verifies the master gain identity for 720 two-atom parameter/size configurations. It also verifies both moment-matched laws and their initial majority probabilities, and checks 1,886 sign comparisons across 41 prescribed-optimum designs. Run `python verify.py`; standard output must equal `certificate.json` after removal of its terminal newline. These finite tests corroborate, but do not replace, the general proof above.

## Relationship to prior work

Condorcet jury theory with exchangeable/correlated decisions already recognizes that vote independence and pairwise correlations alone are insufficient to describe collective competence. In particular, the Bahadur-expansion analysis of Kaniovski and Zaigraev (2009/2011) explicitly acknowledges higher-order dependence, but its main explicit homogeneous-jury formulas assume vanishing higher-order Bahadur coefficients; positive allowable second-order correlation consequently shrinks with group size. It does not imply this exact two-environment geometric single-switch law or arbitrary finite optimal sizes at fixed positive correlation.

Dietrich and Spiekermann (2010/2013) prove a majority-improvement theorem under a distributional tendency toward task-specific competence; that condition is stronger than marginal competence. The finite-optimum construction here has a latent incompetent environment and does not satisfy their pointwise reflected-tail competence dominance. Berend and Sapir (2007) analyze dependent heterogeneous juries and conditions for beneficial enlargement, not the stated two-atom formula and moment-matched opposite behaviors. These relationships concern precise implications, not disjoint vocabularies; novelty is not certified by an unsuccessful search.

## Limitations

This is a population probability result under a single common latent environment and conditional independence. It is not a statement about strategic voting, empirical juries, arbitrary correlated binary vectors, or optimality when voter costs or weighted voting are included. Identical means and covariances do not mean identical full multi-voter laws. The basic fact that higher-order dependence matters was previously established; the claimed contribution is the exact two-environment size-optimization phase law, its unrestricted finite optimum realization, and the explicit moment-matched monotonicity separation. Independent bibliographic review remains unperformed, and alternative equivalent formulations may exist in the literature.

## References

- Kaniovski, S., and Zaigraev, A. (2009 preprint; 2011 journal). *Optimal Jury Design for Homogeneous Juries With Correlated Votes*. `https://www.lse.ac.uk/cpnss/assets/documents/voting-power-and-procedures/workshops/2011/Kaniovski-Paper.pdf`; DOI `10.1007/s11238-009-9170-2`.
- Kaniovski, S. (2009). *An Invariance Result for Homogeneous Juries with Correlated Votes*. *Mathematical Social Sciences* 57, 213–222. DOI `10.1016/j.mathsocsci.2008.09.002`.
- Dietrich, F., and Spiekermann, K. (2010 working paper; 2013 journal). *Epistemic Democracy with Defensible Premises*. `https://mpra.ub.uni-muenchen.de/40135/1/MPRA_paper_40135.pdf`; DOI `10.1017/S0266267113000096`.
- Berend, D., and Sapir, L. (2007). *Monotonicity in Condorcet's Jury Theorem with Dependent Voters*. *Social Choice and Welfare* 28, 507–528. DOI `10.1007/s00355-006-0179-y`.
