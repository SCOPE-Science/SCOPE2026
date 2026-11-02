# Strict Palm hierarchy for leaf bouquets in uniform Cayley trees

## Finding

Consider a uniformly sampled labelled tree \(T_n\) on \([n]=\{1,\ldots,n\}\), with \(n\ge4\). Write \(L_n\) for its total number of leaves (degree-one vertices), \(\ell_v\) for the number of leaf neighbors of vertex \(v\), and
\[
S_{k,n}=\sum_{v=1}^{n}\binom{\ell_v}{k},\qquad 1\le k\le n-1.
\]
The statistic \(S_{k,n}\) counts bouquets consisting of a specified center with \(k\) selected incident leaves. This does **not** require the center to have degree \(k+1\): additional neighbors are allowed. Thus \(S_{1,n}=L_n\), while \(S_{2,n}\) counts unordered pairs of leaf siblings at a common center.

Set
\[
p_m=\left(\frac{m-1}{m}\right)^{m-2},\quad H(m)=(m-1)p_m\quad(m\ge2),\qquad H(1)=0.
\]
**Theorem.** For \(1\le k\le n-1\), the mean-normalized covariance is exactly
\[
\Delta_{n,k}:=\frac{\operatorname{Cov}(L_n,S_{k,n})}{\mathbb E S_{k,n}}
=k+H(n-k)-np_n.
\]
It satisfies the sharp hierarchy
\[
0<\Delta_{n,1}<\Delta_{n,2}<\cdots<\Delta_{n,n-2}=\Delta_{n,n-1}.
\]
Consequently every \(S_{k,n}\) has strictly positive covariance with \(L_n\); normalized dependence increases strictly with bouquet size, except for one forced terminal equality between the two largest sizes. In addition, for every fixed \(k\ge1\), as \(n\to\infty\),
\[
\operatorname{Cov}(L_n,S_{k,n})
=\frac{n e^{-k}}{k!}\left(k-\frac{k+1}{e}\right)+O_k(1).
\]
The coefficient is positive for every \(k\ge1\).

There is also an exact finite-size **Palm leaf-count law**. Fix a center \(c\) and distinct other labels \(A\subset[n]\setminus\{c\}\) with \(|A|=k\). Let \(B(A,c)\) be the event that every label in \(A\) is a degree-one neighbor of \(c\). Put \(m=n-k\). For \(m\ge2\),
\[
\mathbb E[z^{L_n}\mid B(A,c)]
=z^k\sum_{j=0}^{m-1}\binom{m-1}{j}(z-1)^j
\left(\frac{m-j}{m}\right)^{m-2}.
\]
For \(m=1\), the conditional generating function is \(z^k\). Thus the conditional law depends only on \(n\) and \(k\), not on the chosen center or leaf labels.

## Assumptions and scope

Trees are finite, unrooted, simple, and labeled. They are sampled uniformly from the \(n^{n-2}\) Cayley trees. Bouquet labels are selected distinct leaves sharing a specified common center, and other neighbors of that center are permitted. Conditional laws require the indicated event, which has strictly positive probability for every \(1\le k\le n-1\). Statements about strict covariance and hierarchy require \(n\ge4\). For \(n=3\) the leaf count is deterministic, so the strict part is false. The asymptotics keep \(k\) fixed as \(n\) grows.

## Proof

**1. Pruning a marked bouquet.** Given \(B(A,c)\), delete the \(k\) marked pendant vertices, retaining the center \(c\). If \(m=n-k\ge2\), this bijects trees satisfying \(B(A,c)\) with all labeled trees on the \(m\) remaining labels, by reversibly attaching the marked leaves to \(c\). Consequently the residual tree is uniform and \(\mathbb P(B(A,c))=m^{m-2}/n^{n-2}\). For \(m=1\), one tree is possible and \(\mathbb P(B(A,c))=1/n^{n-2}\). Define \(\tau(1)=1\), \(\tau(m)=m^{m-2}\) when \(m\ge2\). By summing over \(n\binom{n-1}{k}\) possible marked bouquets,
\[
\mathbb E S_{k,n}=n\binom{n-1}{k}\frac{\tau(n-k)}{n^{n-2}}>0.
\]

**2. Conditional law.** For \(m\ge2\), a residual vertex different from \(c\) is a leaf precisely when it does not occur in the uniform length-\(m-2\) Prüfer word. A leaf at \(c\) in the residual tree ceases to be a leaf after the marked pendant attachments (and for \(k\ge1\) the augmented center is not a leaf, except the forbidden \(n=2\) case). Hence
\[
L_n=k+\sum_{u\ne c}\mathbf1_{\{u\text{ absent from residual Prüfer word}\}}
\quad\text{conditional on }B(A,c).
\]
For each fixed \(j\)-subset of the \(m-1\) labels other than \(c\), the probability all its members are absent is \(((m-j)/m)^{m-2}\). Expanding the generating function in the elementary symmetric indicators proves the stated exact Palm law. In particular,
\[
\mathbb E[L_n\mid B(A,c)]=k+(m-1)p_m=k+H(m).
\]
If \(m=1\) it is \(k\), agreeing with \(H(1)=0\). Unconditionally each vertex is a leaf iff it is missing from a uniformly sampled length-\(n-2\) Prüfer word, so \(\mathbb E L_n=np_n\).

**3. Exact covariance.** Expand \(S_{k,n}\) as a sum of the event indicators \(\mathbf1_{B(A,c)}\) over all marked bouquets. Each event has identical probability and identical conditional leaf count. Multiplying by \(L_n\), averaging, and dividing by \(\mathbb E S_{k,n}\) gives
\[
\frac{\operatorname{Cov}(L_n,S_{k,n})}{\mathbb E S_{k,n}}
=\mathbb E[L_n\mid B(A,c)]-\mathbb E L_n=k+H(n-k)-np_n.
\]

**4. Sharp strict ordering.** Since \(S_{1,n}=L_n\),
\[
\Delta_{n,1}=\frac{\operatorname{Var}(L_n)}{\mathbb E L_n}>0
\]
for \(n\ge4\); stars and paths yield distinct leaf counts with nonzero probabilities.
For real \(x>2\), let \(p(x)=(1-1/x)^{x-2}\). Then
\[
\frac{d}{dx}\log p(x)
=\log(1-1/x)+\frac{x-2}{x(x-1)}
<-\frac1x+\frac{x-2}{x(x-1)}
=-\frac1{x(x-1)}<0.
\]
Thus \(p_m<p_{m-1}\le1\) for integers \(m\ge3\). Therefore
\[
H(m)-H(m-1)=(m-1)(p_m-p_{m-1})+p_{m-1}<1
\qquad(m\ge3),
\]
while \(H(2)-H(1)=1\). It follows directly that
\[
\Delta_{n,k+1}-\Delta_{n,k}=1-[H(n-k)-H(n-k-1)]
\]
is strictly positive until the final step \(k=n-2\), which is exactly zero. This proves the complete hierarchy.

**5. Asymptotics.** For any fixed integer \(k\), expanding \(\log p_m=(m-2)\log(1-1/m)\) gives \(p_m=e^{-1}(1+3/(2m)+O(m^{-2}))\). Hence
\[
\Delta_{n,k}=k-\frac{k+1}{e}+O_k(n^{-1}),\qquad
\mathbb E S_{k,n}=\frac{n e^{-k}}{k!}+O_k(1).
\]
Their product yields the stated covariance asymptotics. Positivity of its coefficient follows from \(e>2\) and \(k\ge1\), since \(k-(k+1)/e\ge1-2/e>0\).

## Verification

The independent finite enumeration file `verify.py` enumerates all length-\(n-2\) Prüfer words for \(3\le n\le8\), reconstructs each labeled tree, and checks the exact means, covariance identity, and sharp ordering with rational arithmetic (95 assertion groups passed). The enumeration is finite corroboration, not a substitute for the general proof above. The source file runs with Python 3 and only its standard library: `python verify.py`.

## Relationship to prior work

Cayley's count and the Prüfer code underpin the pruning argument; their general tree encoding is classical and not a new contribution. Lavault's Prüfer-like coding study [1] treats enumeration via encoding. Bernardi and Morales [2] develop multitype tree degree enumerators, providing a broader degree-counting context but not stating this leaf-neighbor Palm covariance hierarchy among the results inspected. Junk, Schmidt, and Weber [3] study pendant-neighbor *cherries* for quantum tree symmetries, with an extra degree-three condition on the center, and discuss classical work on random trees; their inspected results do not give this all-\(k\) size-biased conditional law or strict normalized covariance ordering. The novel claim is the specific joint covariance/Palm hierarchy, not the general Prüfer technique.

## Limitations

Historical priority cannot be certified by a bounded literature comparison. The result could be a previously unstated implication of a stronger multitype tree-statistic generating function or older cherry-count results. The theorem concerns uniform labeled Cayley trees, **not** random recursive trees, conditioned Galton–Watson trees, or rooted binary phylogenetic trees. No limit theorem for fluctuations of the entire bouquet vector is asserted. Strict increase applies only after normalizing covariance by mean bouquet count, and it has an unavoidable final equality.

## References

[1] Christian Lavault, *A note on Prüfer-like coding and counting forests of uniform hypertrees*, arXiv:1110.0204 (initial posting 2011-10-02), https://arxiv.org/abs/1110.0204 .

[2] Olivier Bernardi and Alejandro H. Morales, *Counting trees using symmetries*, arXiv:1206.0598 (initial posting 2012-06-04), https://arxiv.org/abs/1206.0598 .

[3] Luca Junk, Simon Schmidt, and Moritz Weber, *Almost all trees have quantum symmetry* (2020), https://doi.org/10.1007/s00013-020-01476-x .
