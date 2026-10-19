# Additive-lag third-cumulant law for burst-deletion diversity

## Finding

Let \(q\ge 2\) and \(n\ge 3\) be integers, and let \(X=(X_0,\ldots,X_{n-1})\) have independent uniformly distributed letters from an alphabet of size \(q\). For \(1\le b<n\), let \(D_b(X)\) be the number of **distinct** words of length \(n-b\) obtainable by deleting exactly \(b\) consecutive letters, with the deletion starting anywhere from position \(0\) through \(n-b\). Put

\[
Z_b=D_b(X)-1-(n-b)(1-1/q).
\]

**Theorem.** For any three pairwise distinct burst lengths, relabeled \(1\le a<b<c<n\), the exact mixed third central moment is

\[
\mathbb E[Z_aZ_bZ_c]=
\begin{cases}
-\dfrac{2(n-c)(q-1)}{q^3},&a+b=c,\\[3pt]
0,&a+b\ne c.
\end{cases}
\]

Moreover, distinct burst-length diversity counts are pairwise uncorrelated:

\[
\operatorname{Cov}(D_a,D_b)=0\quad (a\ne b).
\]

These counts need not be independent. Thus the first mixed cumulant involving **three different burst lengths** has an exact arithmetic resonance: it is negative precisely when the largest length is the sum of the other two. The mean and marginal distribution used below are known consequences of the classical burst-deletion ball count, not claims of novelty.

## Assumptions and scope

All words are finite; positions use zero-based indexing. Exactly one *consecutive* deletion burst of prescribed positive length is allowed. Outputs are compared as words, so coincident outputs obtained from different deletion locations are counted once. The alphabet is arbitrary of finite cardinality \(q\ge 2\), with uniform independent symbols; no field structure is required. The moment formula applies to pairwise distinct lengths \(a,b,c\), not to repeated-index third moments or nonuniform sources.

## Proof

**1. Reduction to lag-disagreements (known ball-size identity).** Let \(Y_i\) denote the word produced by deleting positions \(i,\ldots,i+b-1\) from \(X\), for \(0\le i\le n-b\). For \(i<j\), direct comparison of their common prefix and suffix shows that \(Y_i=Y_j\) precisely when \(X_t=X_{t+b}\) for every \(i\le t<j\). In particular, if two deletion locations yield equal words, every intervening adjacent pair of locations does also. Consequently the distinct outputs are the consecutive constant runs of the list \(Y_0,\ldots,Y_{n-b}\), and

\[
D_b(X)=1+\sum_{i=0}^{n-b-1}{\bf1}\{X_i\ne X_{i+b}\}.\tag{1}
\]

This is the lag form of the classical run-array formula for burst-deletion ball size; it is background, not the asserted new contribution.

For an unordered position-pair \(e=\{i,j\}\), define its centered disagreement variable

\[
H_e={\bf1}\{X_i\ne X_j\}-(1-1/q).
\]

Then \(\mathbb E H_e=0\), and (1) gives

\[
Z_b=\sum_{i=0}^{n-b-1}H_{\{i,i+b\}}.\tag{2}
\]

**2. Forest vanishing.** Let \(e_1,\ldots,e_s\) be distinct edges on the positions \(\{0,\ldots,n-1\}\). If their graph is a forest, the corresponding indicators \({\bf1}\{X_u=X_v\}\) are mutually independent Bernoulli variables with success probability \(1/q\): choose a root in each tree and reveal the new independent uniform letter at each leaf in an outward traversal. Conditional on all previously revealed letters, an unexposed leaf agrees with its parent with probability exactly \(1/q\), independently of the preceding edge outcomes. In particular, a forest of three edges satisfies

\[
\mathbb E[H_{e_1}H_{e_2}H_{e_3}]=0.\tag{3}
\]

For two distinct edges the same argument gives zero covariance. Edges from different positive lags cannot coincide, so expanding (2) yields \(\operatorname{Cov}(D_a,D_b)=0\) for \(a\ne b\).

**3. The only surviving three-edge graph.** Three distinct edges have a cycle only if they form a triangle. If a triangle has ordered vertices \(i<j<k\), its edge lengths are \(j-i\), \(k-j\), and \(k-i=(j-i)+(k-j)\). Therefore, with pairwise distinct \(a<b<c\), a triangle whose three edge lengths are \(a,b,c\) exists if and only if \(a+b=c\).

In that case, for each leftmost position \(0\le i<n-c\), there are exactly two triangles, with middle positions \(i+a\) and \(i+b\), respectively. They are different because \(a\ne b\). Therefore the expansion of \(\mathbb E[Z_aZ_bZ_c]\) has precisely \(2(n-c)\) potentially nonzero terms in the additive case and none otherwise.

**4. Exact triangular contribution.** For one triangle with edges \(e_1,e_2,e_3\), set \(J_e={\bf1}\{\text{the two endpoint letters agree}\}\), and \(t=1/q\). Since \(H_e=-(J_e-t)\), every single-edge expectation equals \(t\), each two-edge agreement event has probability \(t^2\), and all three agreements simultaneously also have probability \(t^2\). Expanding the centered product gives

\[
\begin{aligned}
\mathbb E[H_{e_1}H_{e_2}H_{e_3}]
&=-\bigl(t^2-3t^3+3t^3-t^3\bigr)\\
&=-t^2+t^3=-\frac{q-1}{q^3}.
\end{aligned}
\]

Multiplication by the number \(2(n-c)\) of triangles proves the stated mixed third central moment; (3) removes every other term. There is no limiting argument.

**5. Marginal context.** For a fixed lag \(b\), the graph with edges \(\{i,i+b\}\) for \(0\le i<n-b\) consists of \(b\) disjoint paths. Hence all the individual disagreement indicators in (1) are independent Bernoulli variables with probability \(1-1/q\). Thus, as an already-motivated context for the theorem,

\[
D_b(X)-1\sim\operatorname{Binomial}(n-b,1-1/q),
\]

and \(\operatorname{Var}(D_b)=(n-b)(q-1)/q^2\). Pairwise orthogonality of the count spectrum therefore coexists with a strictly negative mixed third cumulant whenever \(a+b=c\).

## Verification

The standalone file `verify.py` constructs every word for \(q\in\{2,3\}\) and \(3\le n\le 7\). It first calculates each deletion-ball cardinality *directly* as the number of distinct output tuples and compares it with (1). It then computes full marginal histograms, all distinct-lag covariances, and all triples of distinct lags using exact integer arithmetic. In the triple test the integer-scaled centered variable is \(W_b=q(D_b-1)-(n-b)(q-1)\), so the required total over the \(q^n\) words equals \(-2(n-c)(q-1)q^n\) when \(a+b=c\), and zero otherwise. Execution reports `VERIFY_OK` for all ten complete parameter sets. These finite tests are consistency checks; the preceding graph argument is the all-parameter proof.

## Relationship to prior work

The run-array size of a prescribed-length burst-deletion ball was established in classical deletion coding and is explicitly used in Schoeny, Wachter-Zeh, Gabrys, and Yaakobi (2016), Section IV, equation (2). That paper also gives the exact **binary marginal ball-size distribution** in its Appendix A. Consequently neither (1), the marginal binomial identity nor its one-lag variance is asserted as new. The present theorem instead compares the *joint* diversity of deletion bursts of three different lengths and identifies its first nonzero mixed interaction and exact additive-lag criterion.

Xi, Sun, and Ge (2025) treat the larger equal-length-output ball obtained by a deletion burst followed by an insertion burst, including expectation and concentration; that is not the same random variable as the deletion-only diversity \(D_b\). Its background discussion of deletion balls does not supply this joint different-length moment formula. The graph-cycle reduction explains why single-lag enumerations and covariance alone do not imply the asserted interaction value without further analysis.

## Limitations

The theorem is for i.i.d. **uniform** inputs and three **distinct** deletion-burst lengths. It does not give full multivariate distributions, independent-component decompositions across lags, higher-order cumulants, nonuniform-alphabet formulas, or burst insertion/deletion compound-channel statistics. General graph-indexed equality-indicator moment machinery might imply the triangle calculation in other language, so discovery of an equivalent generic lemma remains a literature-overlap risk; the specific exact deletion-spectrum identification was not found in the inspected sources.

## References

1. C. Schoeny, A. Wachter-Zeh, R. Gabrys, and E. Yaakobi, *Codes Correcting a Burst of Deletions or Insertions*, arXiv:1602.06820, first public 22 February 2016; especially Section IV, equation (2), and Appendix A. https://arxiv.org/abs/1602.06820 and https://arxiv.org/pdf/1602.06820
2. Y. Xi, Y. Sun, and G. Ge, *On the Fixed-Length-Burst Levenshtein Ball with Unit Radius*, arXiv:2506.07817, first public 9 June 2025. https://arxiv.org/abs/2506.07817 and https://arxiv.org/pdf/2506.07817
