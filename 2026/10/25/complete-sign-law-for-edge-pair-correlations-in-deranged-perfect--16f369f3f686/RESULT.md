# Complete sign law for edge-pair correlations in deranged perfect matchings

## Finding
Let \(n\ge2\), fix a perfect matching \(F\) of the complete graph on \(2n\) vertices, and choose a perfect matching \(R\) of \(G_n=K_{2n}\setminus F\) uniformly. For each allowed edge \(e\), put \(I_e=\mathbf 1_{\{e\in R\}}\). The \(n\) edges of \(F\) define the **original pairs**.

**Theorem (complete edge-pair covariance sign law).** Every allowed edge has inclusion probability \(p_n=1/[2(n-1)]\). For two *distinct* allowed edges \(e,f\):

- If they meet, then \(\operatorname{Cov}(I_e,I_f)=-p_n^2<0\).
- If they are vertex-disjoint and their four endpoints occupy precisely **two** original pairs (the two crossing edges between those pairs), then the covariance is **positive** for \(n=2\) and \(n=4\), and **negative** for \(n=3\) and every \(n\ge5\).
- If they are disjoint and their four endpoints occupy exactly **three** original pairs (possible for \(n\ge3\)), their covariance is **strictly positive**.
- If they are disjoint and their four endpoints occupy exactly **four** original pairs (possible for \(n\ge4\)), their covariance is **strictly positive**.

These are all possible edge-pair configurations. In particular, from \(n=5\) onward **two disjoint allowed edges are negatively correlated if and only if they connect the same two original pairs.** The exceptional positive sign at \(n=4\) is genuine.

Here are exact formulas. Set \(D_0=1,D_1=0\) and \(D_m=2(m-1)(D_{m-1}+D_{m-2})\) for \(m\ge2\), and write
\[
p=\frac1{2(n-1)},\qquad c=\frac{2(n-1)D_{n-2}}{D_n}.
\]
For disjoint edges occupying two, three, or four original pairs, respectively, the covariances are
\[
\begin{aligned}
\gamma_2(n)&=p(c-p)=\frac{D_{n-2}}{D_n}-p^2,\\
\gamma_3(n)&=p\left(\frac{1-c}{2(n-2)}-p\right),\qquad n\ge3,\\
\gamma_4(n)&=p\left(\frac{n-3+c}{2(n-2)(n-3)}-p\right),\qquad n\ge4.
\end{aligned}
\]
The negative and positive cases have sharply different scales:
\[
\gamma_2(n)\sim-\frac1{16n^4},\qquad
\gamma_3(n)\sim\frac1{8n^3},\qquad
\gamma_4(n)\sim\frac1{4n^3}.
\]

## Assumptions and scope
All graphs are finite and simple. A perfect matching consists of disjoint edges covering every vertex. Original pairs are the forbidden edges \(F\); hence an allowed edge always connects two different original pairs. The random matching is uniform **among perfect matchings of \(G_n\)**, not among all matchings of the complete graph. All covariance signs are strict, and the cases refer to distinct *edge indicators* (not two occurrences of the same edge). At \(n=2\), only the meeting and two-pair cases exist; at \(n=3\), the four-pair case does not exist.

## Proof
**1. Deranged-matching enumerator.** The number of perfect matchings avoiding \(F\) is, by inclusion–exclusion,
\[
D_m=\sum_{j=0}^{m}(-1)^j\binom mj(2(m-j)-1)!!,
\]
where \((-1)!!=1\). Its exponential generating function is
\[
\sum_{m\ge0}\frac{D_m}{m!}z^m=e^{-z}(1-2z)^{-1/2}.
\]
Writing \(H(z)=\sum_{m\ge0}D_m z^m/m!\), differentiation gives \((1-2z)H'(z)=2zH(z)\), hence \(D_0=1,D_1=0\) and the displayed recurrence. In particular \(D_m>0\) for \(m\ge2\).

**2. Conditioning on one allowed edge.** Vertex transitivity and edge transitivity of \(G_n\) imply that the probability of an individual allowed edge is \(p=1/[2(n-1)]\). Fix an allowed edge \(e\) joining two different original pairs, say \(A\) and \(B\). After conditioning on \(e\in R\), one vertex remains from each of \(A\) and \(B\), and \(n-2\) complete original pairs remain. The two remaining vertices of \(A,B\) are matched together with probability
\[
c=\frac{\Pr(e,f\in R)}{\Pr(e\in R)}
=\frac{D_{n-2}/D_n}{p}
=\frac{2(n-1)D_{n-2}}{D_n},
\]
where \(f\) is their connecting edge; the numerator counts matchings after prescribing both crossed edges.

The conditional inclusion probabilities of allowed edges in the other two disjoint-edge orbits follow by symmetry. Given \(e\), each of the \(2(n-2)\) edges from a specified leftover vertex of \(A\) or \(B\) to a vertex in an intact original pair has conditional probability \((1-c)/[2(n-2)]\). Among the \(2(n-2)(n-3)\) allowed edges joining two different intact original pairs, the conditional expected number of chosen edges is \(n-2\) if the two leftover vertices are matched together and \(n-3\) otherwise; thus each such edge has conditional inclusion probability \((n-3+c)/[2(n-2)(n-3)]\). Multiplying these conditional probabilities by \(p\) and subtracting \(p^2\) yields all three displayed formulas. Meeting edges cannot co-occur, yielding covariance \(-p^2\).

**3. Sign classification.** For \(n\ge3\), the recurrence implies \(D_{n-1}>(n-2)D_{n-2}\): check \(n=3\) directly and apply \(D_{n-1}=2(n-2)(D_{n-2}+D_{n-3})\) for \(n\ge4\). This inequality is equivalent to \(c<1/(n-1)\). Consequently,
\[
\gamma_3(n)=\frac{1-(n-1)c}{4(n-1)^2(n-2)}>0.
\]
Likewise, for \(n\ge4\),
\[
\gamma_4(n)=\frac{(n-3)+(n-1)c}{4(n-1)^2(n-2)(n-3)}>0.
\]
For the two-original-pair configuration, \(\gamma_2(2)=1/4\) and \(\gamma_2(3)=-1/16\). For \(n\ge4\), substituting the recurrence three times gives the exact sign identity
\[
\gamma_2(n)=\frac{(n-3)D_{n-4}-D_{n-3}}{(n-1)D_n}.
\]
At \(n=4\), the numerator is \(D_0-D_1=1\), so \(\gamma_2(4)=1/180>0\). For \(n\ge5\), the numerator equals
\[
(5-n)D_{n-4}-2(n-4)D_{n-5},
\]
which is strictly negative: at \(n=5\) its second term is \(-2D_0<0\); at \(n=6\) its first term is \(-D_2<0\); for \(n\ge7\), both terms are nonpositive and at least the first is negative. This completes the strict finite-size classification.

**4. Asymptotics.** The established deranged-matching count asymptotic \(D_n\sim e^{-1/2}(2n-1)!!\) implies, for each fixed positive integer \(j\), \(D_{n-j}/D_n\sim (2n)^{-j}\). Hence \(c\sim1/(2n)\). Substitution into the positive-case expressions proves the stated \(n^{-3}\) asymptotics. For the negative type, the exact sign identity yields \(\gamma_2(n)\sim -1/(16n^4)\), because \((n-3)D_{n-4}/D_n\sim1/(16n^3)\) and \(D_{n-3}/D_n\sim1/(8n^3)\).

## Verification
The standalone `deranged_matching_edge_covariance_check.py` uses exact rational arithmetic and independently enumerates all perfect matchings on \(2n\) vertices for \(2\le n\le7\), discarding those containing an original pair. It checks the matching counts, all individual edge probabilities, all distinct edge-pair covariance formulas and strict signs, including meeting edges. Separate integer/rational checks test the count recurrence and algebraic signs for \(2\le n\le300\). The program returns **19,267 exact assertions passed**. Enumeration through size seven checks examples, not the theorem for arbitrarily large \(n\); unrestricted validity is from the preceding proof.

## Relationship to prior work
Earlier work on deranged matchings already established their enumeration and asymptotic probability, as reviewed by Johnston, Kayll and Palmer (2022); those counts and the limiting \(e^{-1/2}\) factor are prior work. Spiro and Surya (2022) proved a more general Poisson law for coincidences with a fixed matching. Granet and Joos (2023) proved asymptotic single-edge uniformity and overlap laws for random perfect matchings in robustly expanding regular graphs. Deng (2025) extended certain sparse-overlap Poisson approximations to multiple subgraphs. The present theorem is only the **exact finite-size, two-edge covariance orbit and sign classification** under the excluded-matching conditioning. In particular, a Poisson approximation without sign-sensitive error control does not provide an \(n^{-4}\) covariance sign; the known enumeration is used as an input, not claimed as a discovery.

## Limitations
No claim is made about general forbidden subgraphs, weighted perfect matchings, higher-order association, or all edge correlations of other balanced multipartite graphs. The signs for fixed pairs do not establish global negative association or independence. Although the originating counts and symmetry imply some two-edge identities, the present complete sign classification and isolated four-pair exception were not identified in the sources examined; historical priority has not been definitively determined. Independent validation has not been performed.

## References
1. D. Johnston, P. M. Kayll, C. Palmer, *Deranged matchings: proofs and conjectures*, arXiv:2209.11319 (first posted September 22, 2022), https://arxiv.org/abs/2209.11319.
2. S. Spiro, E. Surya, *Counting Deranged Matchings*, arXiv:2211.01872 (first posted November 3, 2022), https://arxiv.org/abs/2211.01872.
3. B. Granet, F. Joos, *Random perfect matchings in regular graphs*, arXiv:2301.10131 (first posted January 24, 2023), https://arxiv.org/abs/2301.10131.
4. B. Deng, *Deranged Perfect Matchings on complete graph and balanced complete r-partite graph*, arXiv:2505.13799 (first posted May 20, 2025), https://arxiv.org/abs/2505.13799.
