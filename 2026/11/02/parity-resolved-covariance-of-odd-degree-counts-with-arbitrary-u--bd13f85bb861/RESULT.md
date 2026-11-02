# Parity-resolved covariance of odd-degree counts with arbitrary uniform random graph motifs

## Finding

Let \(G\sim G(n,p)\), where \(n\ge2\) and \(0<p<1\). Let \(O\) be the number of vertices of odd degree and \(X_H\) the number of *non-induced*, unlabeled copies of a fixed finite simple graph \(H\) with \(v\) vertices, \(e\ge1\) edges, and **no isolated vertices**, where \(2\le v\le n\). With \(d_H(u)\) the degree of vertex \(u\) in \(H\), set \(s=1-2p\) and \(M_H=(n)_v/|\operatorname{Aut}(H)|\), the number of possible copies. Then the exact covariance is

\[
\operatorname{Cov}(O,X_H)
=-\frac{M_Hp^e}{2}\sum_{u\in V(H)}
\left[(-1)^{d_H(u)}s^{n-1-d_H(u)}-s^{n-1}\right].
\tag{1}
\]

If all degrees of \(H\) are positive and even, the covariance is strictly negative for \(0<p<1/2\); for \(1/2<p<1\), it is strictly positive when \(n\) is even and strictly negative when \(n\) is odd. If all degrees are odd, the covariance is strictly positive for \(0<p<1/2\); for \(1/2<p<1\), it is strictly positive when \(n\) is even and strictly negative when \(n\) is odd. Thus, in the odd-degree class the sign is **independent of the motif**, apart from the ambient vertex-parity rule; in the even-degree class the same universal rule holds with one sign reversed.

More sharply, assume all degrees of \(H\) have the same parity and write \(\Delta=\max_{u\in V(H)}d_H(u)\), \(q=n-1-\Delta\), and \(m=|\{u:d_H(u)=\Delta\}|\). As \(p\to1/2\),

\[
\operatorname{Cov}(O,X_H)
=\varepsilon_H\,\frac{mM_H}{2^{e+1}}(1-2p)^q
+O\!\left(|1-2p|^{q+1}\right),
\tag{2}
\]

where \(\varepsilon_H=-1\) in the all-even-degree case and \(\varepsilon_H=+1\) in the all-odd-degree case. Hence \(p=1/2\) is the **only possible interior zero**, and its precise multiplicity is \(n-1-\Delta\). When \(q=0\), the covariance is nonzero at \(p=1/2\) with value \(\varepsilon_HmM_H/2^{e+1}\).

## Assumptions and scope

Each unordered vertex pair of \(G\) is an edge independently with probability \(p\). A copy counted by \(X_H\) specifies the image of exactly the edges of \(H\); additional edges between image vertices are allowed. Thus \(X_H\) is **not** an induced-subgraph count. The graph \(H\) may be disconnected, but has no isolated vertices. Formula (1) holds for mixed-parity motifs as well; the sign and multiplicity theorem concerns motifs all of whose degrees have the same parity. At \(s=0\), products with exponent zero are evaluated as empty products, i.e., \(s^0=1\).

## Proof

For each vertex \(w\) of \(G\), write \(\chi_w=(-1)^{\deg_G(w)}\). The parity identity gives

\[
O=\frac12\left(n-\sum_{w=1}^{n}\chi_w\right),
\qquad \mathbb E[\chi_w]=s^{n-1}.
\tag{3}
\]

Fix one possible unlabeled copy \(F\) of \(H\), and let \(A_F\) be the event that every edge of \(F\) is present. Then \(\mathbb P(A_F)=p^e\). If \(w\) is outside the copy, no incident edge at \(w\) is forced by \(A_F\), so \(\mathbb E[\chi_w\mid A_F]=s^{n-1}\). If \(w\) represents a vertex \(u\) of \(H\), exactly \(d_H(u)\) of its incident edges are forced present and all other \(n-1-d_H(u)\) incident edges remain independent. Consequently

\[
\mathbb E[\chi_w\mid A_F]
=(-1)^{d_H(u)}s^{n-1-d_H(u)}.
\tag{4}
\]

Writing \(X_H=\sum_F\mathbf1_{A_F}\), and combining equations (3) and (4), yields

\[
\operatorname{Cov}(O,\mathbf1_{A_F})
=-\frac{p^e}{2}\sum_{u\in V(H)}
\left[(-1)^{d_H(u)}s^{n-1-d_H(u)}-s^{n-1}\right].
\]

All \(M_H=(n)_v/|\operatorname{Aut}(H)|\) possible copies give the same expression, proving (1). There is no assumption of independence among copy indicators.

If all \(d_H(u)\) are even, rewrite each bracket as

\[
s^{n-1-d_H(u)}\left(1-s^{d_H(u)}\right).
\]

If all degrees are odd, each bracket is

\[
-s^{n-1-d_H(u)}\left(1+s^{d_H(u)}\right).
\]

For \(0<|s|<1\), both factors \(1-s^{d_H(u)}\) for even \(d_H(u)\) and \(1+s^{d_H(u)}\) for odd \(d_H(u)\) are strictly positive. The exponents \(n-1-d_H(u)\) have the same parity across vertices of a fixed pure-parity motif. Every summand therefore has the same strict sign: the even-degree covariance has sign \(-\operatorname{sgn}(s)^{n-1-\Delta}\), and the odd-degree covariance has sign \(+\operatorname{sgn}(s)^{n-1-\Delta}\). This proves the full strict sign classification away from \(p=1/2\), with no possibility of cancellation.

To treat \(p=1/2\), let \(q=n-1-\Delta\ge0\). Factoring \(s^q\) in the appropriate sum, exactly the \(m\) maximum-degree vertices contribute a nonzero constant to the remaining factor at \(s=0\). In addition \(M_Hp^e=M_H2^{-e}(1+O(s))\). This gives (2), with nonvanishing leading coefficient. In particular \(q\) is the exact order of vanishing for \(q>0\), and for \(q=0\) the value at \(p=1/2\) is the indicated nonzero value. There are no other interior zeros by strict sign away from the midpoint.

For orientation, the two smallest pure-parity examples have the closed forms

\[
\operatorname{Cov}(O,X_{K_2})
=n(n-1)p(1-p)(1-2p)^{n-2},
\]

\[
\operatorname{Cov}(O,X_{K_3})
=-(n)_3p^4(1-p)(1-2p)^{n-3},
\]

where \(X_{K_2}\) is the edge count, and \(X_{K_3}\) is the triangle count. Their midpoint orders are respectively \(n-2\) and \(n-3\).

## Verification

The standalone standard-library program `parity_motif_verify.py` enumerates every labeled graph with \(2\le n\le5\) vertices at five rational edge probabilities and independently counts odd-degree vertices and copies of eight graph motifs, including connected and disconnected examples and both parity classes. It compares exact rational covariance sums against (1), checks strict sign claims and midpoint cases, and independently verifies the edge and triangle formulas for sample sizes through \(30\). It reports 338 passing exact-rational identities and sign checks. This enumeration checks finite cases only; the proof above establishes the assertions for arbitrary admissible \(n\), \(p\), and \(H\).

## Relationship to prior work

The mod-two degree boundary and random even subgraphs are classical objects. Grimmett and Janson's *Random even graphs* develops even-subgraph laws conditioned on all vertex degrees being even, together with random-cluster representations; their *Random graphs with forbidden vertex degrees* studies degree-restricted random graph distributions and their asymptotic structure. The present result instead concerns **unconditioned** Bernoulli random graphs and the covariance of odd-degree vertex count with an arbitrary non-induced motif count, including exact all-parameter sign and zero-multiplicity classifications. These inspected papers do not state that covariance or its motif-uniform classification. The calculation uses elementary parity characters and is not claimed as a new general Fourier method.

## Limitations

The result does not cover induced motif counts, dependent-edge random graph models, or a fixed-edge-number random graph. A mixed-degree-parity motif satisfies formula (1), but may exhibit cancellation not addressed by the sign classification. At \(p=0\) or \(p=1\), deterministic degeneracies occur, so the strict sign statements deliberately assume \(0<p<1\). Although no equivalent result was identified in the inspected sources, a classical parity-generating-function identity might already imply this theorem; historical priority is not independently established.

## References

- G. Grimmett and S. Janson, *Random even graphs*, arXiv:0709.3039, initial public version 19 September 2007, https://arxiv.org/abs/0709.3039 .
- G. Grimmett and S. Janson, *Random graphs with forbidden vertex degrees*, arXiv:0712.0270, initial public version 3 December 2007, https://arxiv.org/abs/0712.0270 .
