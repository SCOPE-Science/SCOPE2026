# Optimal noisy leaders on a clique with one exceptional link

## Finding

Let \(n\geq3\) and \(1\leq q\leq n\) be integers, let \(\kappa>0\), and let \(w>0\). Start with the complete graph on \(n\) vertices, give the edge \(\{1,2\}\) conductance \(w\), and give every other edge conductance \(1\). For each set \(S\) of exactly \(q\) leaders, all having the same finite feedback gain \(\kappa\), minimize
\[
J(S)=\operatorname{tr}\!\left((L_{n,w}+\kappa D_S)^{-1}\right),
\]
where \(D_S\) is the diagonal indicator of \(S\). The optimal sets are characterized **completely and with ties included** by the count \(j=|S\cap\{1,2\}|\):

1. When \(w=1\), every feasible leader set is optimal.
2. When \(0<w<1\), select neither exceptional-edge endpoint if \(q=1\), and select both endpoints if \(2\leq q\leq n\).
3. When \(w>1\), select exactly one endpoint if \(q=1\) or \(q=n-1\); select both if \(q=n\). For \(2\leq q\leq n-2\), define
\[
\begin{aligned}
a&=\frac1n, &c&=\frac1{n+\kappa},\\
r_0&=2a, &s_0&=2a^2,\\
r_1&=a+c+\frac{a-c}{q},
&s_1&=c^2\left(1-\frac1q\right)
       +a^2\left(1+\frac1q+\frac n{q^2}\right),\\
D&=s_1-s_0, &H&=s_1r_0-s_0r_1.
\end{aligned}
\]
Then every optimal set has \(j=1\) when \(D+(w-1)H>0\), has \(j=0\) when that expression is negative, and may have either \(j=0\) or \(j=1\) when it vanishes. Every set with an indicated count is optimal, and no set with another count is optimal.

In particular, for \((n,q,\kappa)=(5,3,10)\), the reinforced-edge placement changes at the **exact** weight \(w=27/22\): no exceptional endpoint is selected for \(1<w<27/22\), one is selected for \(w>27/22\), and both types tie at \(27/22\). Thus a single altered edge induces a sharp leader-placement transition even in an otherwise complete network.

## Assumptions and scope

Conductances and feedback gains are strictly positive and finite. Distinct leaders are selected without replacement; all nodes, including leaders, receive independent unit-intensity additive white disturbances. The grounded consensus drift matrix \(L_{n,w}+\kappa D_S\) is positive definite for every nonempty \(S\), since the underlying weighted graph is connected. Its stationary covariance is one-half of its inverse. The factor of one-half is irrelevant to the optimizing set, so \(J\) is the unscaled total variance.

The theorem covers all real \(w>0\), including edge weakening, reinforcement, and the unperturbed clique; it does not take a zero-edge or infinite-gain limit. The count \(j\) is feasible precisely when \(0\leq j\leq2\), \(j\leq q\), and \(q-j\leq n-2\). The cases in the statement respect these constraints.

## Proof

**1. Two rank-one inversions.** Write \(\mathbf1\) for the all-ones vector, \(b=e_1-e_2\), and
\[
B=nI-\mathbf1\mathbf1^{\mathsf T}+\kappa D_S,
\qquad
L_{n,w}+\kappa D_S=B+(w-1)bb^{\mathsf T}.
\]
Put \(a=1/n\), \(c=1/(n+\kappa)\), and \(v_i=c\) for \(i\in S\), \(v_i=a\) otherwise. Since
\[
B=\operatorname{diag}(v_1^{-1},\ldots,v_n^{-1})-
\mathbf1\mathbf1^{\mathsf T},\qquad
1-\sum_i v_i=q(a-c)>0,
\]
the matrix inversion lemma gives
\[
B^{-1}=\operatorname{diag}(v_1,\ldots,v_n)
+\frac{vv^{\mathsf T}}{q(a-c)}.
\]
In particular,
\[
J_{\mathrm{clique}}=
\operatorname{tr}(B^{-1})
=qc+(n-q)a+\frac{qc^2+(n-q)a^2}{q(a-c)}
\]
is independent of the **locations** of the leaders. Let \(r=b^{\mathsf T}B^{-1}b\) and \(s=b^{\mathsf T}B^{-2}b=\|B^{-1}b\|_2^2\). Applying the matrix inversion lemma once more yields the exact identity
\[
J(S)=J_{\mathrm{clique}}
+\frac{(1-w)s}{1-(1-w)r}.
\tag{1}
\]
Every denominator is positive: \(B+(w-1)bb^{\mathsf T}\) is positive definite, while \(r\leq 2/n<1\) also directly suffices when \(0<w<1\).

**2. The three possible endpoint orbits.** The pair \((r,s)\) depends only on \(j=|S\cap\{1,2\}|\). With neither endpoint selected, \(B^{-1}b=ab\), hence \((r_0,s_0)=(2a,2a^2)\). With both selected, \(B^{-1}b=cb\), hence \((r_2,s_2)=(2c,2c^2)\). With exactly one selected, interchange the endpoints if necessary so that \(1\in S\), \(2\notin S\). Then
\[
B^{-1}b=ce_1-ae_2-\frac{v}{q}.
\]
Taking its inner product with \(b\) and its squared norm gives
\[
\begin{aligned}
r_1&=a+c+\frac{a-c}{q},\\
s_1&=c^2\left(1-\frac1q\right)
+a^2\left(1+\frac1q+\frac n{q^2}\right).
\end{aligned}
\]
This proves formula (1) for each feasible count with no numerical approximations.

**3. A weakened link.** The exact inequalities
\[
r_2<r_1\leq r_0,
\quad s_2<s_0,
\quad s_1-s_2=(a^2-c^2)\left(1+\frac1q\right)+\frac{a^2n}{q^2}>0
\]
follow from \(0<c<a\). For \(0<w<1\), minimizing (1) is equivalent to minimizing \(s_j/[1-(1-w)r_j]\), an expression strictly increasing with either positive argument. Thus \(j=2\) beats every other feasible orbit when \(q\geq2\). When \(q=1\), the only feasible counts are \(0,1\), and \(r_1=r_0\), while \(s_1=(n+2)a^2>s_0=2a^2\); hence \(j=0\) is uniquely optimal as a count.

**4. A reinforced link.** Put \(u=w-1>0\). Then (1) reads \(J(S)=J_{\mathrm{clique}}-u s_j/(1+ur_j)\); we must **maximize** \(s_j/(1+ur_j)\). For \(j=1\) versus \(j=2\), both comparison coefficients are positive:
\[
\begin{aligned}
s_1-s_2
&=(a^2-c^2)\left(1+\frac1q\right)+\frac{a^2n}{q^2}>0,\\
s_1r_2-s_2r_1
&=2c\left[a(a-c)\left(1+\frac1q\right)+\frac{a^2n}{q^2}\right]>0.
\end{aligned}
\]
Consequently \(s_1/(1+ur_1)>s_2/(1+ur_2)\) for every \(u>0\) whenever count \(1\) is feasible. For \(q=1\), \(r_0=r_1\) and \(s_1>s_0\), so count \(1\) beats count \(0\). For \(q=n-1\), only counts \(1,2\) are feasible, so count \(1\) wins. For \(q=n\), only count \(2\) is feasible.

It remains to compare counts \(0,1\) for \(2\leq q\leq n-2\). Their exact difference has the sign of
\[
\frac{s_1}{1+ur_1}-\frac{s_0}{1+ur_0}
=\frac{(s_1-s_0)+u(s_1r_0-s_0r_1)}{(1+ur_1)(1+ur_0)}
=\frac{D+uH}{(1+ur_1)(1+ur_0)}.
\]
All denominators are strictly positive, so the three indicated sign cases give *all* minimizing leader sets, including boundary ties. This also shows that, for fixed \(n,q,\kappa\), reinforcement can produce at most one transition in optimal count. The proof is complete.

**5. Exact transition.** Substituting \((n,q,\kappa)=(5,3,10)\) into the displayed formulas gives \(D=-1/675\) and \(H=22/3375\). Thus \(D+(w-1)H=(22w-27)/3375\), proving the stated threshold.

## Verification

The accompanying standalone standard-library script `verification.py` reconstructs each grounded matrix directly and inverts it using rational Gaussian elimination. It tests every subset of \(q\) leaders for \(3\leq n\leq8\), every \(1\leq q\leq n\), three exact positive gains and five exact positive edge weights, independently recomputes the rank-one formula, and compares the complete minimizing-orbit set with the theorem. It checks \(495\) parameter instances and \(7470\) leader subsets; it also reproduces the exact transition \(27/22\). The infinite-range assertion follows from the proof, not from this finite computation.

## Relationship to prior work

Lin, Fardad, and Jovanović (2013, arXiv:1302.0450) formulate the finite-gain stochastic leader-selection problem and develop relaxation and greedy algorithms. Fitch and Leonard (2014, arXiv:1407.1569) give graph-theoretic centrality formulas and explicit one- and two-leader cases on selected graphs. Patterson, McGlohon, and Dyagilev (2014, arXiv:1412.6595) give polynomial-time algorithms for one-dimensional noise-free-leader graphs. Patterson, Yi, and Zhang (2017, arXiv:1708.06873) give general resistance representations and solve several specific paths, cycles, and trees.

Those formulas and algorithms motivate this question but do not themselves state or imply an exact all-\(q\), finite-gain, single-weighted-edge clique optimizer classification: the three endpoint orbits, the weak-link cardinality reversal, and the sharp reinforced-link sign boundary require their own comparison. A search for equivalent wording and rank-one/reliability formulations did not identify an exact prior classification. General matrix inverse identities are standard and are not claimed as new.

## Limitations

The result is restricted to one exceptional edge in an otherwise unit-conductance complete graph, identical positive gains, exactly \(q\) leaders, and independent equal-intensity disturbances. It does not address heterogeneous gains, several altered edges, sparse ambient topologies, or discrete-time dynamics. A general theory of stochastic leader selection already exists; the contribution is the exact structural optimizer classification for this natural perturbed family, rather than the general objective or the inversion lemma. The bibliographic comparison cannot rule out every unindexed or differently named previous treatment.

## References

1. F. Lin, M. Fardad, M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450 (first public 2013-02-03), https://arxiv.org/abs/1302.0450.
2. K. E. Fitch, N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (first public 2014-07-07), https://arxiv.org/abs/1407.1569.
3. S. Patterson, N. McGlohon, K. Dyagilev, *Efficient, Optimal k-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (first public 2014-12-20), https://arxiv.org/abs/1412.6595.
4. S. Patterson, Y. Yi, Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (first public 2017-08-23), https://arxiv.org/abs/1708.06873.
