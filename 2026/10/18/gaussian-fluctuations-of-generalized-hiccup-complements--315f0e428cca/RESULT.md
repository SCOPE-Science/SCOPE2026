# Gaussian fluctuations of generalized hiccup complements

## Finding

Fix integers \(k\ge 2\) and \(x\ge 3\). Define the strictly increasing \((0,x,1,k+1)\)-hiccup sequence by \(g(1)=x\) and, for every integer \(n\ge2\),
\[
g(n)=g(n-1)+\begin{cases}1,&n\in\{g(1),\ldots,g(n-1)\},\\ k+1,&n\notin\{g(1),\ldots,g(n-1)\}.\end{cases}
\]
Let \(U(n)=\#(\{1,\ldots,n\}\setminus\operatorname{im}(g))\), and let \(T_N\) be uniform on \(\{1,\ldots,N\}\), for every integer \(N\ge2\). Write \(\log_k N=(\log N)/(\log k)\). Then the distributional limit, for fixed \(k,x\), is
\[
\boxed{\frac{kU(T_N)-(k-1)T_N-\left(x-2-\frac{k-1}{2}\right)\log_kN}{\sqrt{\frac{k^2-1}{12}\log_kN}}\ \xrightarrow[N\to\infty]{\mathcal D}\ \mathcal N(0,1).}
\]
Equivalently, for every real \(z\), the proportion of integers \(1\le n\le N\) for which the normalized expression is at most \(z\) tends to the standard normal distribution function at \(z\). Both constants are explicit: the logarithmic drift depends on \(x\), while the leading variance depends only on \(k\).

## Assumptions and scope

All quantities refer to positive integer indices, with \(k\ge2\) and \(x\ge3\) fixed as \(N\) grows. The random variable \(T_N\) expresses a uniform choice of an index; the hiccup sequence itself is deterministic. The statement is a weak limit, not pointwise normality at a single integer, a fixed-\(N\) Gaussian approximation with an error rate, or a uniform theorem in varying \(k,x\).

Set \(t=x-2\), let \(W_0=0\), and recursively define finite binary words \(W_{h+1}=W_h^{\,k}1\). The positions of zeros in the infinite binary word
\[
w=0\prod_{h=0}^{\infty}(W_h^{\,t}1)
\]
are exactly the complement of \(\operatorname{im}(g)\), by the tree/word identity in Cloitre's Proposition 4.3 [1]. Hence the number of zeros among the first \(n\) letters equals \(U(n)\). This exact, externally established combinatorial identity is the starting point of the proof; the fluctuation theorem below is proved from it.

## Proof

**1. Discrepancy on complete trees.** For a finite binary word \(v\), let \(Z(v)\) be the number of zeros and put \(\Delta(v)=kZ(v)-(k-1)|v|\). The letter \(0\) contributes \(1\), and \(1\) contributes \(-(k-1)\). Writing \(L_h=|W_h|\), induction in \(W_{h+1}=W_h^{\,k}1\) gives
\[
L_h=\frac{k^{h+1}-1}{k-1},\qquad Z(W_h)=k^h,\qquad \Delta(W_h)=1.
\]
Every nonempty prefix \(v\) of \(W_h\) satisfies
\[
1\le\Delta(v)\le 1+h(k-1). \tag{1}
\]
Indeed, a prefix of \(W_{h+1}\) preceding the last root consists of \(c\in\{0,\ldots,k-1\}\) whole copies of \(W_h\), followed by a nonempty prefix of another copy, and its discrepancy is \(c+\Delta(v)\). The final prefix has discrepancy \(1\). The assertions follow from the base word \(W_0=0\) by induction.

**2. Gaussian law inside one complete tree.** Let \(V_h\) be uniform on the \(L_h\) positions of \(W_h\), and write \(X_h=\Delta(W_h[1:V_h])\). Put \(r=\lfloor h^{1/3}\rfloor\). Descend from \(W_h\) toward \(W_r\) through its recursively ordered \(k\) child copies. Conditional on the current position not being the final root of \(W_j\), its child index is uniform on \(\{0,\ldots,k-1\}\), independently of the lower-level child position. The probability of encountering any root at levels \(j>r\) is at most
\[
\sum_{j=r+1}^{h}\frac{1}{L_j}=O_k(k^{-r}). \tag{2}
\]
Outside this event, the earlier whole child copies contribute their child indices because each has discrepancy \(1\). Thus \(X_h\) has a coupling with
\[
B_1+\cdots+B_{h-r}+R_r,
\]
where the \(B_i\) are independent and uniform on \(\{0,\ldots,k-1\}\) and the final prefix contribution satisfies \(1\le R_r\le1+r(k-1)\) by (1). The coupling fails with probability \(O_k(k^{-r})\). Each \(B_i\) has mean \(\mu=(k-1)/2\) and variance \(\sigma^2=(k^2-1)/12>0\). Because \(r=o(\sqrt h)\), the classical independent-summands central limit theorem and Slutsky's lemma imply
\[
\frac{X_h-\mu h}{\sigma\sqrt h}\xrightarrow[h\to\infty]{\mathcal D}\mathcal N(0,1). \tag{3}
\]
This use of independence is exact on the good descent event, not inferred from finite numerical data.

**3. From complete trees to a uniform index in the infinite complement.** Let \(H=\lfloor\log_kN\rfloor\) and \(m=H-\lfloor H^{1/3}\rfloor\), for sufficiently large \(N\). The length of stage \(W_j^{\,t}1\) is \(tL_j+1\). Consequently, the index \(J\) of the stage containing position \(N\) satisfies \(J=H+O_{k,t}(1)\), since the cumulative stage lengths are bounded above and below by fixed positive multiples of \(k^J\).

Within every stage \(j\ge m\), recursively partition its copies of \(W_j\) into disjoint *complete* copies of \(W_m\), together with the separating root letters. Do the same in the partially completed final stage, retaining only the completely contained copies of \(W_m\). Declare positions in these copies *good*. All stages with \(j<m\) together have \(O_{k,t}(k^m)\) positions. The separating roots in stages \(j\ge m\) occupy at most \(O_{k,t}(N/L_m+H)\) positions: the contracted ordered \(k\)-ary trees have one root per \(k\) child groups, and every full \(W_m\) has \(L_m\) letters. The last incomplete \(W_m\) contributes at most \(L_m\) further positions, and there are only \(O(H)\) outer stage roots. It follows that
\[
\frac{\#\{1\le n\le N:\ n\text{ is not good}\}}{N}
=O_{k,t}\!\left(\frac{k^m}{N}+\frac{1}{L_m}+\frac{H}{N}\right)=o(1). \tag{4}
\]
A uniformly selected good position lies in one of equal-length complete \(W_m\) copies. Its within-copy position \(V_m\) is therefore uniform on \(\{1,\ldots,L_m\}\), regardless of how the copies are distributed among the stages.

For such a copy in stage \(j\in\{m,\ldots,J\}\), all earlier *full* stages contribute \(j(t-(k-1))\) to discrepancy, and the initial letter contributes \(1\). Earlier whole copies of \(W_j\) contribute at most \(t-1\). On the branch down from \(W_j\) to this \(W_m\), the preceding sibling subtrees contribute the sum of at most \(j-m\) integers from \(\{0,\ldots,k-1\}\), by \(\Delta(W_\ell)=1\). No higher root precedes its own selected child subtree. Therefore for every good position \(n\), if \(v\) is its within-copy position,
\[
\Delta(w[1:n])=(t-k+1)H+\Delta(W_m[1:v])+O_{k,t}(H^{1/3}), \tag{5}
\]
with a deterministic uniform error bound, since \(j-H=O_{k,t}(1)\) and \(j-m=O(H^{1/3})\).

**4. Normalization.** Since \(\Delta(w[1:n])=kU(n)-(k-1)n\), equations (3)--(5) imply that for a uniform \(T_N\), with probability tending to one,
\[
kU(T_N)-(k-1)T_N=(t-k+1)H+X_m+O_{k,t}(H^{1/3}).
\]
Here \(m=H+O(H^{1/3})\); thus \(\mu m=\mu H+o(\sqrt H)\) and \(\sigma\sqrt m/(\sigma\sqrt H)\to1\). Applying (3), (4), and Slutsky's lemma yields centering \((t-k+1+\mu)H=(t-(k-1)/2)H\) and variance scale \(\sigma^2H\). Finally \(H=\log_kN+O(1)\), so replacing \(H\) with \(\log_kN\) changes neither limit. This is the displayed theorem. \(\square\)

## Verification

The standalone `certify.py` checks, for \(2\le k\le5\) and heights \(0\le h\le7\), the tree lengths, zero counts, total discrepancies, and **every** prefix bound in (1), using integer arithmetic. For nine distinct parameter pairs, including \(x<k+1\), \(x=k+1\), and \(x>k+1\), it independently constructs the hiccup sequence and the tree word and compares their first \(100\), \(2048\), and \(10000\) symbols exactly. Execute with `python3 certify.py`; the expected output is recorded in `VERIFICATION.md`.

The infinite weak limit is proved by the explicit multiscale coupling and classical i.i.d. central limit theorem, **not** by the finite tests or a statistical goodness-of-fit calculation. The word identity quoted from [1] is a published antecedent, not a newly reproved result.

## Relationship to prior work

Cloitre [1, Proposition 4.3 and Equation (4.5)] proves the exact tree-word representation and [1, Proposition 4.2] the nested recurrence for \(U\). Fokkink--Joshi [2] obtain morphic descriptions and related arithmetic-sequence structure. Deugau--Ruskey [3] study the associated complete \(k\)-ary trees and meta-Fibonacci counts. Ruskey--Deugau [5, Theorem 25] give an *exact base-\(k\) digit-sum formula* for the inverse occurrence positions in their meta-Fibonacci family, and [5, Theorem 28] deduce the first-order density \(U(n)\sim (k-1)n/k\) in the corresponding specialization \(x=k+1\). Thus the special case can also be approached through classical digit-sum fluctuations. Neither result states the full direct-index Gaussian limit with arbitrary \(x\), whose proof here controls the generalized stages. Erickson--Isgur--Jackson--Ruskey--Tanny [4] investigate Conolly-like nested recurrences, frequency sequences, and first-order asymptotic density constraints. These determine or describe the underlying deterministic sequences; the present result adds the distributional second-order logarithmic drift and Gaussian fluctuation theorem at a *uniformly sampled index*. A description of the entire word determines its finite-dimensional arithmetic data but does not itself state or prove the Gaussian limit. The proof requires an explicit treatment of recursive child digits and of stage-boundary effects.

## Limitations

The theorem concerns random-index empirical distributions for **fixed** \(k,x\). It does not claim almost-sure randomness of the deterministic sequence, pointwise fluctuations, a quantitative Berry--Esseen rate, independence between different sampled indices, uniformity in growing parameters, or a limit for the degenerate case \(k=1\) or \(x=2\). A separate literature search found no matching distributional theorem, but unindexed or differently formulated prior work cannot be categorically excluded. 

## References

[1] Benoît Cloitre, *Counting with Hiccup Sequences*, arXiv:2610.13908v1 (first publicly posted 2026-10-09), especially Propositions 4.2--4.3. https://arxiv.org/html/2610.13908v1

[2] Robbert Fokkink and Gandhar Joshi, *On Cloitre's hiccup sequences*, *Ramanujan Journal* 69 (2026), article 40, doi:10.1007/s11139-025-01305-1. https://link.springer.com/article/10.1007/s11139-025-01305-1

[3] Chris Deugau and Frank Ruskey, *Complete k-ary trees and generalized meta-Fibonacci sequences*, *Discrete Mathematics & Theoretical Computer Science* (2006). https://dmtcs.episciences.org/en/articles/3514/download

[4] Alejandro Erickson, Abraham Isgur, Bradley W. Jackson, Frank Ruskey, and Stephen M. Tanny, *Nested Recurrence Relations with Conolly-like Solutions*, *SIAM Journal on Discrete Mathematics* 26 (2012), 206--238, doi:10.1137/100795425. https://webhome.cs.uvic.ca/~ruskey/Publications/MetaFib/ConollyLikeMay14.pdf

[5] Frank Ruskey and Chris Deugau, *The Combinatorics of Certain k-ary Meta-Fibonacci Sequences*, *Journal of Integer Sequences* 12 (2009), article 09.4.3. https://cs.uwaterloo.ca/journals/JIS/VOL12/Ruskey/ruskey6.pdf
