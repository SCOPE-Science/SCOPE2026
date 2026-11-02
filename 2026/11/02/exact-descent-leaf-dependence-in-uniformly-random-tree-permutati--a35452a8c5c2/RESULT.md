# Exact descent–leaf dependence in uniformly random tree permutations

## Finding
For every integer \(n\ge3\), choose uniformly a permutation \(\pi\) of \(\{1,\dots,n\}\) whose inversion graph is a tree. Let \(D\) be its number of **adjacent** descents (indices \(i\) with \(\pi_i>\pi_{i+1}\)) and let \(L\) be the number of degree-one vertices in its inversion graph. Set \(T=n-1-L\). Then \(T\sim\operatorname{Bin}(n-3,1/2)\), and, for every \(t\in\{0,\ldots,n-3\}\),
\[
\Pr(D=d\mid T=t)=\begin{cases}
1,&t\text{ even and }d=1+t/2,\\
1/2,&t\text{ odd and }d=(t+1)/2\text{ or }d=(t+3)/2,\\
0,&\text{otherwise}.
\end{cases}
\]
In particular, the integer \(2D+L-n-1\) lies in \(\{-1,0,1\}\) for **every** such permutation. More precisely, under the standard binary insertion code \((b_1,\dots,b_{n-2})\),
\[
2D+L-n-1=b_{n-2}-b_1.
\]
The entire finite joint law is therefore determined. In particular,
\[
\mathbb ED=\frac{n+1}{4},\quad\mathbb EL=\frac{n+1}{2},\quad
\operatorname{Cov}(D,L)=-\frac{n-3}{8},\quad
\operatorname{Var}(L)=\frac{n-3}{4}.
\]
For \(n\ge4\), \(\operatorname{Var}(D)=(n-1)/16\) and
\[
\operatorname{Corr}(D,L)=-\sqrt{\frac{n-3}{n-1}}\longrightarrow-1.
\]
Moreover, if \(Z\sim N(0,1)\),
\[
\left(\frac{D-(n+1)/4}{\sqrt n},\frac{L-(n+1)/2}{\sqrt n}\right)
\xrightarrow{\mathrm d}(Z/4,-Z/2).
\]

## Assumptions and scope
An inversion graph has a vertex for each *position* and an edge between positions \(i<j\) exactly when \(\pi_i>\pi_j\). A tree permutation has a connected acyclic inversion graph. Probability is uniform over all such permutations of a fixed size \(n\ge3\); no other permutations enter the sample space. There are exactly \(2^{n-2}\) such permutations by the insertion bijection of Acan–Hitczenko [1]. The number \(L\) counts graph leaves, not leaves of any associated non-ambiguous tableau. At \(n=3\), both statistics are deterministic, so the correlation is undefined. All stated asymptotics concern integer \(n\to\infty\).

## Proof
**The published coding theorem.** Start at permutation \((2,1)\). For each \(k=2,\ldots,n-1\), choose one of two operations: \(I_1\), insert the new largest entry \(k+1\) immediately before the current last entry; or \(I_2\), replace the current largest entry \(k\) by \(k+1\) and append \(k\). Acan–Hitczenko [1, Section 2] establish that these operations give each tree permutation exactly once. Put \(b_{k-1}=1\) for \(I_1\) and \(0\) for \(I_2\). Thus the \(m=n-2\) code bits are independent fair Bernoulli variables under uniform sampling.

**Descent identity.** Initially the final comparison in \((2,1)\) is a descent. An \(I_2\) operation does not change any earlier comparison and appends an ascent: the old maximum is appended to a final entry smaller than that maximum. An \(I_1\) operation replaces the current last comparison by an ascent followed by a descent: its new largest element is placed before the last entry. Hence \(I_1\) increases the descent number by one exactly when the preceding final comparison was an ascent, equivalently when the immediately preceding bit was \(0\). The first \(I_1\) after the initial permutation adds no descent. Consequently,
\[
D=1+N_{01},\qquad N_{01}:=\sum_{j=2}^m\mathbf1_{\{b_{j-1}=0,b_j=1\}}.
\]
This deduction is direct from the two insertion operations, not a result asserted in [1].

**Leaf identity.** The degree formula in [1, Lemma 8] and its leaf-count simplification [1, Lemma 12] show that the graph has \(n-r\) leaves, where \(r\) is the number of maximal constant runs of the insertion word \((b_1,\dots,b_m)\). Since \(r=1+N_{01}+N_{10}\), writing \(N_{10}\) for the number of \(1\)-to-\(0\) changes gives
\[
L=n-1-(N_{01}+N_{10}),\qquad T=N_{01}+N_{10}.
\]
The identity \(N_{01}-N_{10}=b_m-b_1\) telescopes, proving \(2D+L-n-1=b_m-b_1\) exactly.

**Conditional law.** The transformation
\[
(b_1,b_2,\dots,b_m)\mapsto\bigl(b_1,z_2,\dots,z_m\bigr),\qquad z_j=\mathbf1_{\{b_j\ne b_{j-1}\}},
\]
is a bijection of binary strings. Hence \(b_1,z_2,\dots,z_m\) are independent fair bits and \(T=\sum_{j=2}^m z_j\sim\operatorname{Bin}(m-1,1/2)\). With \(T=t\) fixed, the first bit remains a fair coin and the last bit is \(b_1\) for even \(t\) and \(1-b_1\) for odd \(t\). Substitute in \(D=1+(t+b_m-b_1)/2\) to obtain the displayed exact conditional distribution. Thus the unconditional joint probabilities for \(L=n-1-t\) are \(\binom{n-3}{t}2^{-(n-3)}\) at \(D=1+t/2\) if \(t\) is even, or half of that at each \(D=(t+1)/2,(t+3)/2\) if \(t\) is odd. This also gives \(\Pr(D=d)=\binom{n-1}{2d-1}/2^{n-2}\) on its feasible support.

**Moments, correlation, and limit.** From the conditional law, \(\mathbb E(D\mid T)=1+T/2\), and \(\operatorname{Var}(D\mid T)\) is \(0\) for even \(T\) and \(1/4\) for odd \(T\). Since \(T\sim\operatorname{Bin}(n-3,1/2)\), the mean, leaf variance and covariance displayed above follow. When \(n\ge4\), the parity of \(T\) is fair, so the law of total variance gives \(\operatorname{Var}(D)=(n-3)/16+1/8=(n-1)/16\). The correlation formula follows by division. Finally, \(D=1+T/2+(b_m-b_1)/2\) and \(L=n-1-T\); the endpoint correction is bounded. Apply the ordinary binomial central limit theorem and Slutsky's theorem to get the singular bivariate Gaussian limit.

## Verification
The standalone standard-library program `verify_tree_permutation_dependence.py` enumerates all \(2^{n-2}\) insertion words for \(3\le n\le13\), checks the decoded permutations, tree membership, exact pair counts and moment formulas, and independently compares with all permutations for \(3\le n\le8\). Running `python verify_tree_permutation_dependence.py` gives `PASS 16499 exact assertions; 4094 coded trees; 126 independently brute-classified trees`. Finite enumeration is a check of the identities; the proof covers every integer \(n\ge3\).

## Relationship to prior work
Acan and Hitczenko [1] established the binary insertion bijection, the exact leaf count in terms of code runs, and marginal graph statistics. The present theorem **uses those published facts**; it does not claim the binary model, the tree-permutation enumeration or marginal leaf law as new. Janson [2] studied classical (not necessarily consecutive) pattern occurrences in random tree permutations and derived limit laws; the adjacent-descent/graph-leaf *joint distribution* considered here is different. Selig and Zhu [3] linked permutations associated with exactly one complete non-ambiguous tree to a natural permutation-graph class and studied descents for another bijection on upper-diagonal objects; their treatment does not give the displayed conditional graph-leaf law. The specifically new claim is the precise *cross-statistic* identity, full conditional distribution, covariance and asymptotically singular dependence. These follow from [1]'s encoding together with the new descent analysis; implicit derivability from [1] is a significant priority risk.

## Limitations
This theorem applies only to uniformly chosen permutations whose inversion graph is a tree. It does not extend automatically to forest permutations, weighted insertion models, or arbitrary permutation classes. The limit is a degenerate bivariate Gaussian, not a nondegenerate two-dimensional normal. Its originality is conditional on no earlier paper having worked out the same joint law; the known code makes it algorithmically recoverable, and independent historical-priority review is still needed. No independent mathematical audit has been performed.

## References
[1] H. Acan and P. Hitczenko, *On random trees obtained from permutation graphs*, arXiv:1406.3958 (public June 16, 2014), particularly the insertion construction in Section 2 and leaf formula in Lemma 12. https://arxiv.org/abs/1406.3958

[2] S. Janson, *The number of occurrences of patterns in a random tree or forest permutation*, arXiv:2203.04182 (public March 8, 2022), especially Definitions 1.1 and Section 3. https://arxiv.org/abs/2203.04182

[3] T. Selig and H. Zhu, *Complete non-ambiguous trees and associated permutations: new enumerative results*, arXiv:2303.15756v1 (public March 28, 2023); see later public revision Section 4.1 for permutations associated with a unique CNAT. https://arxiv.org/abs/2303.15756
