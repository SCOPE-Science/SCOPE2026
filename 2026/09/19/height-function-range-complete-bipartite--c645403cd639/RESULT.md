# Exact range laws for integer height functions on complete bipartite graphs

Let \(K_{a,b}\) be the complete bipartite graph with \(a,b\ge 1\), and pin one vertex to height zero. A **standard height function** is a map \(f:V(K_{a,b})\to\mathbb Z\) satisfying \(|f(u)-f(v)|=1\) on every edge. A **lazy height function** satisfies \(|f(u)-f(v)|\le 1\) on every edge. In either case write
\[
R(f)=\max_v f(v)-\min_v f(v).
\]
The rooted counts and range distributions below are independent of which vertex is pinned, because rerooting by subtracting the new root value is a range-preserving bijection.

## Theorem

For the standard model, the total number of rooted functions is
\[
N_H(a,b)=2^a+2^b-2,
\]
and the complete range law is
\[
\#\{f:R(f)=1\}=2,
\qquad
\#\{f:R(f)=2\}=2^a+2^b-4.
\]
Consequently
\[
\boxed{\widehat h(K_{a,b})=2-\frac{2}{2^a+2^b-2}}.
\]

For the lazy model, the total number of rooted functions is
\[
\boxed{
N_L(a,b)=3^a+3^b+2^{a+b}-2^{a+1}-2^{b+1}+1,
}
\]
and the complete range law is
\[
\#\{f:R(f)=0\}=1,
\]
\[
\#\{f:R(f)=1\}=2^{a+b}-2,
\]
\[
\#\{f:R(f)=2\}=N_L(a,b)-2^{a+b}+1.
\]
Hence
\[
\boxed{h(K_{a,b})=2-\frac{2^{a+b}}{N_L(a,b)}}.
\]

Equivalently, the range enumerators are
\[
2z+(2^a+2^b-4)z^2
\]
for the standard model and
\[
1+(2^{a+b}-2)z+(N_L(a,b)-2^{a+b}+1)z^2
\]
for the lazy model.

## Fixed-order extremizers

Fix \(n=a+b\ge2\). Up to exchanging the two parts, both \(\widehat h(K_{a,b})\) and \(h(K_{a,b})\) are uniquely maximized by the star \(K_{1,n-1}\), and uniquely minimized by the most balanced complete bipartite graph
\[
K_{\lfloor n/2\rfloor,\lceil n/2\rceil}.
\]

For the lazy model this yields an asymptotic separation:
\[
h(K_{1,n-1})=2-3\left(\frac23\right)^n\longrightarrow2,
\]
whereas
\[
h\!\left(K_{\lfloor n/2\rfloor,\lceil n/2\rceil}\right)\longrightarrow1.
\]
In contrast, the standard expected range tends to \(2\) at both extremal shapes.

## Proof

Let the bipartition be \(A\sqcup B\), with \(|A|=a\), \(|B|=b\), and pin a vertex of \(A\) to zero.

### Standard model

Every vertex of \(B\) has height \(\pm1\). If the vertices of \(B\) use both signs, then every vertex of \(A\) must have height zero. This gives \(2^b-2\) functions. If \(B\) is constantly \(+1\), then every non-root vertex of \(A\) can independently have height \(0\) or \(2\), giving \(2^{a-1}\) functions. If \(B\) is constantly \(-1\), the analogous choices are \(0\) or \(-2\), again giving \(2^{a-1}\) functions. Thus
\[
N_H(a,b)=(2^b-2)+2^a=2^a+2^b-2.
\]
Exactly two functions have range one: the two functions constant on each side with values \((0,1)\) or \((0,-1)\). Every other standard function has range two, proving the first distribution and expectation formula.

### Lazy model

Now every vertex of \(B\) has height in \(\{-1,0,1\}\). Classify functions by the exact set of values used on \(B\).

If \(B\) is constant, there are three possible constant values and, in each case, every non-root vertex of \(A\) has three available heights. This contributes \(3^a\).

If the image of \(B\) is exactly \(\{-1,0\}\) or exactly \(\{0,1\}\), there are \(2(2^b-2)\) choices for the assignment on \(B\), and each non-root vertex of \(A\) then has two possible heights. This contributes
\[
2(2^b-2)2^{a-1}.
\]

If the image is exactly \(\{-1,1\}\), there are \(2^b-2\) choices on \(B\), and all vertices of \(A\) are forced to zero. If all three values occur on \(B\), there are
\[
3^b-3\cdot2^b+3
\]
assignments on \(B\), again with all of \(A\) forced to zero. Summing gives
\[
N_L(a,b)
=3^a+3^b+2^{a+b}-2^{a+1}-2^{b+1}+1.
\]

Because \(K_{a,b}\) has diameter at most two, every lazy function has range at most two. The range-at-most-one functions are exactly those whose image lies in \(\{0,1\}\) or in \(\{-1,0\}\). Each family has \(2^{a+b-1}\) members and their intersection is the all-zero function. Hence there are \(2^{a+b}-1\) functions of range at most one, one of range zero, and \(2^{a+b}-2\) of range one. The stated range-two count and expectation follow.

### Extremizers at fixed order

For the standard model, \(\widehat h\) is strictly increasing in
\[
2^a+2^{n-a}-2.
\]
The function \(2^k\) is strictly discrete-convex, so the symmetric sum is minimized at the balanced split and maximized at the endpoints \(a=1,n-1\).

For the lazy model write
\[
N_L(a,n-a)=2^n+1+F(a)+F(n-a),
\qquad F(k)=3^k-2^{k+1}.
\]
Its second discrete difference is
\[
F(k+1)-2F(k)+F(k-1)=4\cdot3^{k-1}-2^k>0
\]
for every \(k\ge1\). Thus the same strict convexity argument gives the same unique extremizers up to swapping parts. Since \(h=2-2^n/N_L\), maximizing or minimizing \(N_L\) does the same to \(h\). The displayed asymptotics follow by direct substitution.

## Relation to recent work

Zhu's 2026 paper *Paths maximize the expected range of graph-indexed random walks* proves the path extremality conjecture for the standard model and derives the analogous lazy result. Its running example is \(K_{2,3}\): it records 10 standard rooted functions with expected range \(9/5\), and 45 lazy rooted functions with expected range \(58/45\). The formulas above specialize respectively to
\[
N_H(2,3)=10,\quad \widehat h(K_{2,3})=9/5,
\]
and
\[
N_L(2,3)=45,\quad h(K_{2,3})=58/45.
\]
The accessible full text does not state a general complete-bipartite formula.

The standard model goes back to Benjamini--Häggström--Mossel, while the lazy model was studied by Loebl--Nešetřil--Reed. The present claim is the exact complete-bipartite range law and its fixed-order extremal consequences, not the definitions or the general path bounds.

## Verification

`artifacts/verify.py` independently enumerates all rooted assignments for \(1\le a,b\le4\) directly from the edge constraints and checks both total counts and every range coefficient against the formulas. The recorded output is in `artifacts/verification.txt`. This finite computation supports but does not replace the proof.

## Limitations

The result concerns complete bipartite graphs and the two uniform height-function models above; it does not give corresponding formulas for arbitrary bipartite graphs. Originality is asserted only to the best of our knowledge. The full 2000 Benjamini--Häggström--Mossel article and the full 2003 Loebl--Nešetřil--Reed article were not both available for complete line-by-line inspection in the sources checked; their abstracts/indexed descriptions were inspected. An elementary complete-bipartite enumeration under different terminology in older literature therefore remains the main residual originality risk, along with very recent parallel work.

## References

1. Y. Zhu, *Paths maximize the expected range of graph-indexed random walks*, arXiv:2609.19728v1 (2026). https://arxiv.org/abs/2609.19728
2. I. Benjamini, O. Häggström, E. Mossel, *On Random Graph Homomorphisms into Z*, Journal of Combinatorial Theory, Series B 78 (2000), 86--114. https://doi.org/10.1006/jctb.1999.1931
3. M. Loebl, J. Nešetřil, B. Reed, *A note on random homomorphism from arbitrary graphs to Z*, Discrete Mathematics 273 (2003), 173--181. https://doi.org/10.1016/S0012-365X(03)00235-8
