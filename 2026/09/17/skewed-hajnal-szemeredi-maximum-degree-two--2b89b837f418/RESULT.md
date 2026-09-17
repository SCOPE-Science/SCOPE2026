# Skewed Hajnal--Szemerédi colorings at maximum degree two

## Statement

A **color vector** is a vector of positive integers
\[
\vec n=(n_1,\ldots,n_d),\qquad \sum_{i=1}^d n_i=n.
\]
An \(\vec n\)-coloring of an \(n\)-vertex graph is a proper vertex coloring whose \(i\)-th color class has exactly \(n_i\) vertices.

Birken conjectured the following strengthening of his prescribed-coloring version of the Hajnal--Szemerédi theorem. If
\[
n=s(r+1)+m,\qquad m\in[r],
\]
then every \(n\)-vertex graph of maximum degree at most \(r\) should admit every prescribed coloring for which at most \(m\) classes have size \(s+1\) and all remaining classes have size at most \(s\).

We prove the first nontrivial maximum-degree case.

**Theorem 1.** Let \(G\) be an \(n\)-vertex graph with \(\Delta(G)\le 2\), and write
\[
n=3s+m,\qquad m\in\{1,2\}.
\]
Let \(\vec n=(n_1,\ldots,n_d)\) be a color vector such that at most \(m\) coordinates equal \(s+1\) and every other coordinate is at most \(s\). Then \(G\) has an \(\vec n\)-coloring.

Thus Conjecture 5 of Birken, *A Hajnal--Szemerédi theorem for skewed colorings* (arXiv:2609.18629v1), holds for \(r=2\).

The proof uses two auxiliary facts. The first is an exact prescribed-coloring theorem for bipartite graphs of maximum degree two.

## Exact flexibility for bipartite maximum-degree-two graphs

**Theorem 2.** Let \(H\) be a finite bipartite graph with \(\Delta(H)\le2\), and let \(\vec c=(c_1,\ldots,c_d)\) be positive integers summing to \(|V(H)|\). Then \(H\) has a proper coloring with color-class sizes exactly \(c_1,\ldots,c_d\) if and only if
\[
\boxed{\max_i c_i\le \alpha(H).}
\]

Necessity is immediate because every color class is independent.

For sufficiency, write the connected components of \(H\) as \(H_1,\ldots,H_t\). Each \(H_j\) is a path or an even cycle. Put
\[
h_j=|V(H_j)|,\qquad q_j=\alpha(H_j).
\]
Thus \(q_j=\lceil h_j/2\rceil\) for a path and \(q_j=h_j/2\) for an even cycle, and
\[
\sum_j q_j=\alpha(H).
\]

We first distribute each prescribed color among the components. Consider the integral flow network with a source joined to color vertex \(i\) by an edge of capacity \(c_i\), every color vertex \(i\) joined to every component vertex \(j\) by an edge of capacity \(q_j\), and component vertex \(j\) joined to the sink by an edge of capacity \(h_j\).

For a set \(A\) of color vertices, the only nontrivial max-flow cut condition is
\[
\sum_{i\in A}c_i
 \le \sum_j \min\{h_j,|A|q_j\}.
\tag{1}
\]
If \(|A|=1\), the right side is
\[
\sum_j q_j=\alpha(H),
\]
so (1) follows from \(\max_i c_i\le\alpha(H)\). If \(|A|\ge2\), then \(2q_j\ge h_j\) for every component, so the right side of (1) is \(\sum_jh_j=|V(H)|\), and (1) is automatic. Hence an integral max flow of value \(|V(H)|\) exists. Let \(a_{ij}\) be the resulting amount of color \(i\) assigned to component \(H_j\). Then
\[
\sum_j a_{ij}=c_i,\qquad
\sum_i a_{ij}=h_j,\qquad
0\le a_{ij}\le q_j.
\tag{2}
\]

It remains to realize the local multiplicities in each path or even cycle. We use the elementary arrangement facts:

- multiplicities \(b_1,\ldots,b_k\) summing to \(L\) can be arranged on a cycle with no equal adjacent symbols whenever
  \[
  \max_i b_i\le\lfloor L/2\rfloor;
  \]
- they can be arranged on a path with no equal adjacent symbols whenever
  \[
  \max_i b_i\le\lceil L/2\rceil.
  \]

For completeness, the cyclic statement follows by taking a loopless connected Eulerian multigraph on symbol set \([k]\) with degree sequence \(2b_1,\ldots,2b_k\). Such a loopless multigraph exists because the largest degree does not exceed the sum of the others; disconnected components can be joined by degree-preserving 2-switches. Reading the successive vertices of an Euler circuit gives the desired cyclic word, with symbol \(i\) appearing \(b_i\) times. The path statement follows by adding one dummy symbol, applying the cyclic statement to length \(L+1\), and deleting the dummy occurrence.

Now (2) gives exactly the required local bound: \(q_j=\lceil h_j/2\rceil\) for paths and \(q_j=h_j/2\) for even cycles. Hence every component can be colored with its assigned multiplicities, and the component colorings combine to an \(\vec c\)-coloring of \(H\). This proves Theorem 2. \(\square\)

## An independent odd-cycle transversal of prescribed size

**Lemma 3.** If \(\Delta(G)\le2\) and \(G\) has \(n\) vertices, then \(G\) has an independent set \(S\) of size
\[
\left\lceil\frac n3\right\rceil
\]
such that \(G-S\) is bipartite.

**Proof.**
Every component of \(G\) is a path or a cycle. Choose one vertex from every odd-cycle component. Any chosen vertex of an odd cycle belongs to a maximum independent set of that component. Therefore there is a maximum independent set \(I\) of \(G\) containing all chosen odd-cycle representatives.

Every path or cycle \(C\) satisfies
\[
\alpha(C)\ge |V(C)|/3,
\]
so
\[
|I|=\alpha(G)\ge \left\lceil\frac n3\right\rceil.
\]
The number of odd-cycle components is at most \(\lfloor n/3\rfloor\). Hence one may choose a subset
\[
S\subseteq I,\qquad |S|=\left\lceil\frac n3\right\rceil,
\]
that still contains one selected vertex from each odd cycle. Deleting \(S\) destroys every odd cycle, while paths and even cycles create no odd cycle after vertex deletion. Thus \(G-S\) is bipartite. \(\square\)

## Proof of Theorem 1

The cases \(n\le2\) are immediate, so assume \(s\ge1\).

Call a prescribed class **large** if its size is \(s+1\).

### No large class

If every \(n_i\le s=\lfloor n/3\rfloor\), Theorem 1 of Birken directly supplies the prescribed coloring for every graph with maximum degree at most \(2\).

### Exactly one large class

Suppose, after relabeling, that
\[
n_1=s+1.
\]
By Lemma 3, choose an independent set \(S\) of size \(s+1=\lceil n/3\rceil\) whose deletion leaves a bipartite graph. Color \(S\) with color \(1\), and put
\[
H=G-S.
\]
Then \(\Delta(H)\le2\) and \(H\) is bipartite.

If \(m=1\), then \(|V(H)|=2s\); if \(m=2\), then \(|V(H)|=2s+1\). All remaining prescribed sizes are at most \(s\). Since any bipartite graph on \(N\) vertices has independence number at least \(\lceil N/2\rceil\),
\[
\max_{i\ge2}n_i\le s\le\alpha(H).
\]
Theorem 2 therefore colors \(H\) with the remaining prescribed class sizes, completing the coloring of \(G\).

### Two large classes

This can occur only when \(m=2\). The Hajnal--Szemerédi theorem gives an equitable \(3\)-coloring of \(G\), whose class sizes are
\[
s+1,\quad s+1,\quad s.
\]
Assign the two classes of size \(s+1\) to the two large prescribed colors. The third class is independent and has size \(s\); partition it arbitrarily into the remaining prescribed color classes, whose sizes sum to \(s\). Every resulting class remains independent, so this is the desired prescribed coloring.

The three cases exhaust all permitted color vectors. \(\square\)

## Context and originality boundary

Kuchukova, Perkins and Povill formulated the prescribed-coloring conjecture asserting existence whenever every prescribed class has size at most
\[
\left\lfloor\frac{n}{\Delta+1}\right\rfloor.
\]
Birken proved that conjecture in arXiv:2609.18629v1. In the future-work section of the same paper, Birken proposed the sharper nondivisible-order statement reproduced above as Conjecture 5 and supplied the extremal example
\[
sK_{r+1}\sqcup K_m.
\]

Theorem 1 resolves that explicit conjecture for \(r=2\). Theorem 2 is a stronger structural ingredient for the bipartite maximum-degree-two case: it characterizes exactly which prescribed class-size vectors are realizable using only the independence-number obstruction.

Searches for the exact conjecture, its maximum-degree-two specialization, and synonymous formulations involving prescribed, bounded, capacitated, skewed, path, and cycle colorings did not locate a previous theorem implying either Theorem 1 or Theorem 2. Because Birken's conjecture appeared only in September 2026, very recent or not-yet-indexed parallel work remains a residual originality risk. Older bounded-coloring literature is broad and uses varied terminology, so an equivalent formulation of the auxiliary Theorem 2 cannot be ruled out with certainty.

## Limitations

The result settles Birken's Conjecture 5 only for \(r=2\); no claim is made for \(r\ge3\).

Theorem 2 is restricted to bipartite graphs of maximum degree at most two. Its simple independence-number criterion need not extend to larger maximum degree.

The originality assessment is to the best of our knowledge. No independent validation is asserted.

## References

1. Mathis Birken, *A Hajnal--Szemerédi theorem for skewed colorings*, arXiv:2609.18629v1 (2026). https://arxiv.org/abs/2609.18629
2. Aiya Kuchukova, Will Perkins, Xavier Povill, *Sampling Colorings with Fixed Color Class Sizes*, ICALP 2026; arXiv:2603.08259 (2026). https://arxiv.org/abs/2603.08259
3. András Hajnal, Endre Szemerédi, *Proof of a conjecture of P. Erdős*, in *Combinatorial Theory and its Applications* (1970), 601--623.
