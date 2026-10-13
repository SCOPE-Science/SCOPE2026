# Exact negative Sackin–cherry covariance in Yule trees

## Finding

**Theorem.** In the standard Yule–Harding growth model, the covariance of the Sackin index and the number of cherries has the following exact finite-sample form:

\[
\operatorname{Cov}(S_n,C_n)=
\begin{cases}
0,&n=2,\\
-\dfrac n9+\dfrac{2}{3(n-1)},&n\ge3.
\end{cases}
\]

It vanishes at \(n=2,3\), is negative for every integer \(n\ge4\), and is asymptotic to \(-n/9\). This quantifies the dependence of two complementary measures of tree shape across every sample size, without a large-tree approximation.

## Assumptions and scope

Begin with a rooted full binary tree containing two leaves at depth one. To pass from \(n\) to \(n+1\) leaves, choose one of its \(n\) leaves uniformly and replace it with a binary parent having two new leaf children. All choices are repeated independently conditioned on the current tree. Let \(S_n\) be the sum of the edge depths of all extant leaves, measured from the binary root. Let \(C_n\) count internal nodes having two direct leaf children (cherries). All expectations and covariances use this random tree law, without conditioning on its shape or observed sampling times. The choice of leaf labels is irrelevant to these statistics. A planted root with one child shifts every depth by one, adding deterministic \(n\) to \(S_n\), so the covariance is unchanged.

For the proof define \(Q_n\) to be the sum of the depths of the \(2C_n\) leaves belonging to cherries. No lengths of chronological branches are used; these are topological edge counts.

## Proof

Condition on the entire current tree with \(n\) leaves. If the uniformly selected leaf has depth \(d\), and \(J\) indicates that it was part of a cherry, direct inspection of the split gives

\[
S_{n+1}=S_n+d+2,\qquad C_{n+1}=C_n+1-J.
\]

If \(J=1\), the selected leaf and its former cherry mate cease to form an old cherry and two new leaves form one cherry. Consequently \(Q_{n+1}-Q_n=2\). If \(J=0\), the newly created cherry contributes depth sum \(2(d+1)\), giving \(Q_{n+1}-Q_n=2(d+1)\). As exactly \(2C_n\) leaves belong to cherries and their depth sum is \(Q_n\), conditional averaging yields

\[
\begin{aligned}
\mathbb E[S_{n+1}\mid T_n]&=(1+1/n)S_n+2,\\
\mathbb E[C_{n+1}\mid T_n]&=(1-2/n)C_n+1,\\
\mathbb E[Q_{n+1}\mid T_n]&=(1-2/n)Q_n+2S_n/n+2.
\end{aligned}
\]

Multiplying the first two split identities **before** conditional averaging gives the critical mixed-moment recurrence:

\[
\mathbb E[S_{n+1}C_{n+1}\mid T_n]
=(1-1/n)S_nC_n+(1+1/n)S_n+(2-4/n)C_n-Q_n/n+2.
\]

Write \(s_n=\mathbb ES_n\), \(c_n=\mathbb EC_n\), \(q_n=\mathbb EQ_n\), and \(g_n=\operatorname{Cov}(S_n,C_n)\). The initial two-leaf tree has \((S_2,C_2,Q_2)=(2,1,2)\). In particular \((S_3,C_3,Q_3)=(5,1,4)\) deterministically. Solving the first three recurrences by induction gives, for every \(n\ge3\),

\[
\begin{aligned}
s_n&=2n(H_n-1),\\
c_n&=n/3,\\
q_n&=\frac{2n}{3}\left(2H_n-\frac53\right),
\qquad H_n=\sum_{j=1}^n\frac1j.
\end{aligned}
\]

Subtracting the product of the marginal means from the displayed mixed-moment recurrence produces

\[
\begin{aligned}
g_{n+1}&=(1-1/n)g_n+2s_nc_n/n^2-q_n/n\\
&=(1-1/n)g_n-2/9,\qquad n\ge3.
\end{aligned}
\]

Since \(g_3=0\), multiplication by \(n\) and telescoping from \(n=3\) gives \((n-1)g_n=-[n(n-1)-6]/9\), as asserted. For \(n\ge4\), \(n(n-1)>6\), so the sign is strictly negative. The asymptotic expression follows directly. At \(n=2\), both variables are deterministic and the covariance is zero. This exhausts every integer size.

## Verification

The standalone `verify.py` script uses only Python's standard library. Invoke `python3 verify.py`. It propagates the exact probability distribution of **unlabelled** full binary tree shapes under uniform tip splitting; canonically equivalent shapes are combined with rational weights. It independently recomputes the Sackin index, cherry count, the cherry-tip depth sum, their expectations, and their covariance for every \(2\le n\le10\). All nine cases agree exactly with the theorem and the marginal formulas. This finite check supports, but does not replace, the all-\(n\) proof above.

## Relationship to prior work

Sackin-index expectations and variances under Yule trees are classical. Cardona, Mir, and Rosselló (2012) compute Sackin and other imbalance-index variances and the covariance with the total cophenetic index; their symbol for Colless's index does **not** denote the cherry count. Dearlove and Frost (2015) explicitly study Sackin and cherry counts together in phylogenetic asymmetry tests and describe them as weakly correlated, but do not state the exact finite-size mixed moment. Wu and Choi (2015) obtain joint cherry–pitchfork distributions and covariances; pitchfork count differs from Sackin depth. Cardona and colleagues (2020) obtain other depth-related moments, not this cherry–Sackin covariance. The present result supplies the explicit sign and dependence law for that natural pair, not a new derivation of their individual marginal distributions.

## Limitations

The theorem applies only to the uniformly chosen-tip Yule–Harding tree **shape** model. It does not assert a formula for non-Yule tree models, pendant-branch time lengths, heterogeneous birth rates, or trees conditioned on unequal sampling times. It gives the mixed second moment but not a joint distribution or a monotone-coupling claim. Comparison with historical literature is literature-based rather than a guarantee of exhaustive priority. Independent review has not been performed.

## References

- Cardona, G., Mir, A., and Rosselló, F. (2012), *Exact formulas for the variance of several balance indices under the Yule model*. arXiv:1202.6573 (first public 2012-02-29). https://arxiv.org/abs/1202.6573
- Dearlove, B. L., and Frost, S. D. W. (2015), *Measuring Asymmetry in Time-Stamped Phylogenies*. PLOS Computational Biology 11, e1004312 (published 2015-07-06). https://doi.org/10.1371/journal.pcbi.1004312
- Wu, T., and Choi, K. P. (2015), *On joint subtree distributions under two evolutionary models*. arXiv:1508.03139 (first public 2015-08-13). https://arxiv.org/abs/1508.03139
- Mir, A., Rosselló, F., and collaborators (2020), *On Sackin’s original proposal: the variance of the leaves’ depths as a phylogenetic balance index*. BMC Bioinformatics. https://doi.org/10.1186/s12859-020-3405-1
