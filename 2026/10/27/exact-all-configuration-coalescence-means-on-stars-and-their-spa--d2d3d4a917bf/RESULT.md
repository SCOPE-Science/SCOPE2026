# Exact all-configuration coalescence means on stars and their sparse-versus-complete comparison

## Finding

For any integer \(m\ge1\), let \(G=K_{1,m}\) be the simple star with central vertex \(o\) and \(m\) leaves. Put one random walker at each vertex of an initially occupied set. At rate one per extant walker, it jumps to a uniformly chosen neighboring vertex; walkers meeting at a vertex instantly merge and thereafter evolve as one walker. Let \(T\) be the first time that only one walker remains. For \(k\) initially occupied leaves, define \(a_k=\mathbb E[T\mid o\text{ occupied}]\) and \(b_k=\mathbb E[T\mid o\text{ vacant}]\). Set \(H_0=0\) and \(H_k=\sum_{j=1}^k1/j\).

**Exact all-configuration law.** For \(1\le k\le m\),
\[
a_k=\frac{m}{m+1}(H_k+1)-\frac{1}{k+1}.
\]
For \(2\le k\le m\),
\[
b_k=\frac{m}{m+1}(H_{k-1}+1).
\]
The one-particle boundary conditions are \(a_0=b_1=0\). These expressions depend only on the number of occupied leaves, not their identities. In particular, starting from all \(m+1\) occupied sites gives
\[
\boxed{\mathbb E T_{\mathrm{star}}=\frac{mH_m+m-1}{m+1}.}
\]
For \(m\ge2\) and \(2\le k\le m\), the difference between occupying and leaving vacant the central vertex, with the same \(k\) occupied leaves, is
\[
a_k-b_k=\frac{m-k}{(m+1)k(k+1)}.
\]
It is positive except at \(k=m\), where it is exactly zero. The latter equality concerns means and does not assert equality of the hitting-time distributions.

**Sharp comparison at fixed graph order.** Under the same per-particle total jump rate, the fully occupied complete graph on \(m+1\) vertices has
\[
\mathbb E T_{\mathrm{complete}}=\frac{m^2}{m+1}.
\]
The means coincide for \(m=1,2\), but \(\mathbb E T_{\mathrm{star}}<\mathbb E T_{\mathrm{complete}}\) for every \(m\ge3\). As \(m\to\infty\), the star mean is \(\log m+\gamma+1+O((\log m)/m)\), versus the complete-graph mean of order \(m\); their ratio is asymptotic to \(m/\log m\). Sparse hub structure can therefore substantially accelerate coalescence compared with a clique when particle activity, rather than activity per edge, is normalized.

## Assumptions and scope

The graph is a finite simple star with \(m\ge1\). Each extant walker carries an independent exponential clock of rate one, chooses a neighbor uniformly on jumping, and merges immediately when the destination is already occupied. All rates are measured in this per-walker normalization; multiplying all jump rates by \(c>0\) divides every reported mean by \(c\). The process is continuous-time and asynchronous. It is not the discrete-time synchronous lazy-walk process. The initial occupied set has at least one vertex, and \(T=0\) when it has exactly one. Coalescence occurs almost surely because the finite interacting Markov chain has an accessible singleton class from every nonsingleton configuration.

## Proof

Write \(A_k\) for the configuration class with occupied center and \(k\) occupied leaves, and \(B_k\) for the class with vacant center and \(k\) occupied leaves. Symmetry makes the expected remaining time depend only on class. Put \(a_0=b_1=0\). Every nonabsorbed \(B_k\) has \(k\) independently moving leaf particles, and each jump reaches the vacant center; hence its holding time is exponential of mean \(1/k\), followed by \(A_{k-1}\):
\[
b_k=\frac1k+a_{k-1}\qquad(2\le k\le m).
\]
In a nonabsorbed \(A_k\), exactly \(k\) occupied leaves jump to the center, each at rate one, producing \(A_{k-1}\). The occupied center jumps at rate one, choosing an occupied leaf with probability \(k/m\) (producing \(B_k\)) or a vacant leaf with probability \((m-k)/m\) (producing \(B_{k+1}\)). The backward equation is therefore
\[
(k+1)a_k=1+ka_{k-1}+\frac{k}{m}b_k+\frac{m-k}{m}b_{k+1}\qquad(1\le k\le m),
\]
where the final term is interpreted as zero for \(k=m\), so \(b_{m+1}\) is not needed. When \(k=1\), \(b_1=0\). Substituting the first equation at \(k=1\), or directly using the degenerate two-vertex case \(m=1\), gives
\[
a_1=\frac{3m-1}{2(m+1)}.
\]
For every \(2\le k\le m\), the two backward equations simplify to
\[
a_k-a_{k-1}=\frac{2m+1}{(m+1)k}-\frac1{k+1}
=\frac1k+\frac{m-k}{(m+1)k(k+1)}.
\]
Summing this telescoping first difference from \(1\) through \(k\), using the displayed value of \(a_1\), gives
\[
a_k=\frac{m}{m+1}(H_k+1)-\frac1{k+1}.
\]
The formula for \(b_k\) follows from \(b_k=1/k+a_{k-1}\); subtracting proves the center-occupancy identity. At \(k=m\) the difference is zero.

For the complete graph \(K_{m+1}\), when \(j\ge2\) particles remain, each moves at rate one and meets another particle with probability \((j-1)/m\) per jump. Thus the rate of decrease from \(j\) to \(j-1\) particles is \(j(j-1)/m\), irrespective of configuration, and
\[
\mathbb E T_{\mathrm{complete}}
=\sum_{j=2}^{m+1}\frac{m}{j(j-1)}
=\frac{m^2}{m+1}.
\]
Equality with the star holds for \(m=1,2\). For \(m\ge3\), \(H_m<m-1+1/m\) (the displayed inequality is already strict for \(m\ge3\)); consequently \(mH_m+m-1<m^2\), establishing strict improvement. More simply, \(H_m<m-1\) holds for \(m\ge4\), and the order-four case \(m=3\) can be checked directly. Finally, the classical asymptotic expansion \(H_m=\log m+\gamma+O(m^{-1})\) yields the stated scale and ratio. All finite-sum and boundary identities remain valid at \(m=1\).

## Verification

The standalone program `verify.py` constructs the exact transient generator of the full occupied-subset Markov chain, **without using the two-class backward reduction**, and solves its first-passage equations by fraction-preserving Gaussian elimination. It compares every nonsingleton occupied configuration with the claimed formula for stars of orders two through seven (\(m=1,\ldots,6\)). All **219** exact-rational configuration identities passed. It separately checks the full-occupancy expression and the complete-graph comparison in that range. Run with Python 3 and no third-party dependencies:

```
python verify.py
```

This exhaustive finite-size verification is corroborative; the above backward-equation proof establishes the formulas for every integer \(m\ge1\).

## Relationship to prior work

Oliveira, *On the coalescence time of reversible random walks* (first public arXiv version September 3, 2010), proves general coalescence-time bounds in terms of worst-case hitting time, including arbitrary initial configurations. Those general bounds do not determine these exact star-configuration expectations or the sharp complete-graph comparison.

Cooper, Elsässer, Ono, and Radzik, *Coalescing random walks and voting on connected graphs* (first public arXiv version April 17, 2012), explicitly note the logarithmic coalescence-time **order** for a star, while treating a discrete-time lazy coalescing-walk model and proving general bounds. The \(\Theta(\log m)\) order and the general coalescing-walk framework are established prior work; the claim here is the evaluated continuous-time all-configuration formula, its exact constant, the saturated-hub equality, and the clique comparison under one specified rate normalization.

Athreya and Swart, *Systems of branching, annihilating, and coalescing particles*, concern the broader interacting-particle setting and supply a relevant primary MSC classification. Their publicly available abstract was inspected, not their full paper; no determination of detailed noncoverage follows from that abstract alone.

## Limitations

Only mean first-coalescence times are determined, not the complete hitting-time law, higher moments, or transient occupancy distribution. The graph family consists of stars and the comparison complete graphs only. Walkers have uniform total rate one and coalesce on contact. The proof does not establish corresponding formulas for edge-rate-one walks, branching, annihilation, voter-process majority consensus from finitely many opinions, asynchronous rate-heterogeneous walks, or general trees. Published work may contain an equivalent all-configuration star specialization not discovered by the source search; independent priority verification is still required.

## References

1. R. I. Oliveira, *On the coalescence time of reversible random walks*, arXiv:1009.0664, first submitted 2010-09-03. https://arxiv.org/abs/1009.0664
2. C. Cooper, R. Elsässer, H. Ono, and T. Radzik, *Coalescing random walks and voting on connected graphs*, arXiv:1204.4106, first submitted 2012-04-17. https://arxiv.org/abs/1204.4106
3. S. Athreya and J. Swart, *Systems of branching, annihilating, and coalescing particles*, arXiv:1203.6477, first submitted 2012-03-29; primary MSC 82C22. https://arxiv.org/abs/1203.6477
