# A strict likelihood-ratio shift in the identity of the first repeated value

## Finding
Let \(m\ge2\) be an integer and let \(p_1,\ldots,p_m\) be strictly positive probabilities summing to one. Draw \(X_1,X_2,\ldots\) independently from these probabilities. Let \(T\) be the index of the first observation that repeats an earlier value and let \(R=X_T\) denote that repeated label. Define \(e_k(v)\) to be the degree-\(k\) elementary symmetric polynomial in the entries of \(v\), with \(e_0(v)=1\). Write \(p_{-i}\) for the vector omitting \(p_i\).

For every label \(i\) and every integer \(2\le t\le m+1\),
\[
\Pr(T=t,R=i)=(t-1)!\,p_i^2e_{t-2}(p_{-i}). \tag{1}
\]
For any labels \(i,j\) with \(p_i<p_j\), the posterior odds
\[
\frac{\Pr(R=i\mid T=t)}{\Pr(R=j\mid T=t)}
\]
are **strictly increasing** at every successive time \(t=2,\ldots,m+1\). Equal-probability labels have posterior odds identically equal to one. At the two endpoints,
\[
\Pr(R=i\mid T=2)=\frac{p_i^2}{\sum_jp_j^2},\qquad
\Pr(R=i\mid T=m+1)=p_i. \tag{2}
\]

Thus, ordering labels from least probable to most probable, the family of conditional laws of \(R\) given \(T=t\) moves strictly toward rarer labels in monotone likelihood-ratio order. In particular, for any \(a\) for which both \(\{i:p_i\le a\}\) and \(\{i:p_i>a\}\) are nonempty, \(\Pr(p_R\le a\mid T=t)\) strictly increases with \(t\). If the probability vector is not uniform, \(\mathbb E[p_R\mid T=t]\) strictly decreases with \(t\); in the uniform case all these conditional laws are identical.

## Assumptions and scope
The alphabet is finite, of size \(m\ge2\); all category probabilities are positive and sum to one. Draws are independent and identically distributed; no null outcome or unequal sampling at different times is included. Because the first \(m+1\) draws cannot all be distinct, \(2\le T\le m+1\) almost surely. Every time in this range and every label have positive joint probability. No asymptotic approximation or unverified extension to infinite alphabets is asserted.

## Proof
Fix \(t\) and \(i\). On the event \(\{T=t,R=i\}\), the first \(t-1\) draws contain \(i\) and \(t-2\) other *distinct* labels, in any of \((t-1)!\) orders, and the last draw is \(i\). Summing the products of the probabilities of the distinct other labels proves (1). All joint probabilities are strictly positive.

Fix distinct \(i,j\), put \(r=m-2\), and set \(E_k=e_k(p_{-\{i,j\}})\). Use the conventions \(E_{-1}=0\), \(E_{r+1}=0\), \(E_0=1\). For \(k=0,\ldots,r+1\),
\[
\frac{\Pr(T=k+2,R=i)}{\Pr(T=k+2,R=j)}
=\frac{p_i^2}{p_j^2}\,
\frac{E_k+p_jE_{k-1}}{E_k+p_iE_{k-1}}. \tag{3}
\]
For \(0<k<r+1\), \(E_k>0\) when \(k\le r\). The ratios \(u_k=E_{k-1}/E_k\), extended by \(u_0=0\) and \(u_{r+1}=+\infty\), are strictly increasing: for \(1\le k\le r-1\), Newton's inequalities for positive elementary symmetric sums imply \(E_k^2>E_{k-1}E_{k+1}\); the first and last inequalities follow from positivity. For \(r=0\), only the endpoints occur and the conclusion is immediate. The function \(u\mapsto(1+p_ju)/(1+p_iu)\) has strictly positive derivative whenever \(p_i<p_j\). Hence (3) is strictly increasing as \(k\), and thus \(t\), increases. When \(p_i=p_j\), (3) is identically one.

At \(t=2\), (1) is \(p_i^2\). At \(t=m+1\), it is \(m!p_i\prod_jp_j\), because every label must appear once in the first \(m\) draws. Summing over \(i\) proves (2).

Let \(\pi_t(i)=\Pr(R=i\mid T=t)\). For \(s>t\), the strict pairwise odds inequality implies \(\pi_s(i)\pi_t(j)>\pi_t(i)\pi_s(j)\) whenever \(p_i<p_j\). Summing over every \(i\) with \(p_i\le a\) and every \(j\) with \(p_j>a\) proves the asserted strict threshold-event ordering. Finally,
\[
\mathbb E[p_R\mid T=t]-\mathbb E[p_R\mid T=s]
=\sum_{i<j}(p_i-p_j)\bigl[\pi_t(i)\pi_s(j)-\pi_s(i)\pi_t(j)\bigr],
\]
where the indices \(i<j\) mean any once-for-all enumeration of unordered pairs. Each summand is nonnegative by the same odds inequality, and at least one is strictly positive if the \(p_i\) are not all equal. This proves the claimed conditional mean ordering.

## Verification
The script `verify_first_repeat.py` enumerates all sample words through the first possible collision for 16 exact-rational probability vectors with between two and five labels (84,056 enumerated words in total). It independently evaluates the event \(\{T=t,R=i\}\), checks (1) with elementary-symmetric computations, tests every pair of posterior odds at successive times, and verifies (2) and the conditional expected-probability ordering. It executed successfully with Python 3 and uses only the standard library. Finite checks corroborate the proof; the proof establishes the all-parameter statement.

## Relationship to prior work
Camarri and Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities* (1998 public technical report; 2000 journal article), derive exact laws for the first-repeat time and the set of labels observed at that time, notably formulas (1) and (13) of their paper. Their results supply the natural starting point for the birthday-process question; they do not themselves state the strict posterior likelihood-ratio shift of the repeated **label** conditional on each collision time. The new statement is not merely their marginal-time formula: its principal content is the pairwise inequality for all times and arbitrary strictly positive weights.

Fadnavis, *A generalization of the Birthday problem and the chromatic polynomial* (arXiv:1105.0698, first made public in 2011), establishes collision-free probability inequalities for nonuniform colors, including their extension to graph-constrained collisions. Its subject is a different (unlabelled and not time-conditioned) comparison. Newton's inequalities are classical; the claimed contribution is their application to the fully time-conditioned, repeated-label posterior in (3), not a new proof of Newton's inequalities. A more general, earlier likelihood-ratio theorem may contain this conclusion implicitly and has not been ruled out by all literature.

## Limitations
This is an exact finite-alphabet result. It makes no claim concerning dependent draws, infinite alphabets, or collision quotas greater than two. The exact joint probability identity follows by elementary counting, and strictness is obtained from the standard Newton inequalities. The conclusion is not independent verification, nor is exhaustive absence of equivalent earlier formulations claimed.

## References
1. M. Camarri and J. Pitman, *Limit distributions and random trees derived from the birthday problem with unequal probabilities*, University of California Berkeley Statistics Technical Report 523 (public 1998-06-01), *Electronic Journal of Probability* 5 (2000), Paper 2. https://statistics.berkeley.edu/tech-reports/523 ; full text: https://www.maths.tcd.ie/EMIS/journals/EJP-ECP/article/download/58/58-115-1-PB.pdf
2. S. Fadnavis, *A generalization of the Birthday problem and the chromatic polynomial*, arXiv:1105.0698 (first submitted 2011-05-03). https://arxiv.org/abs/1105.0698
3. Newton's inequalities for elementary symmetric polynomials (classical), used in the proof above.
