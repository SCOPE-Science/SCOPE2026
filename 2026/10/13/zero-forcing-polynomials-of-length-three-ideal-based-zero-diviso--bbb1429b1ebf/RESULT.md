# Zero forcing polynomials of length-three ideal-based zero-divisor graphs

## Finding

Let \(R\) be a finite commutative ring, let \(I\subsetneq R\), and assume \(S=R/I\) is a finite chain ring with residue-field order \(q\), maximal ideal \(\mathfrak m\), and nilpotency length exactly \(3\). Put \(s=|I|\), \(a=s(q-1)\), \(b=sq(q-1)\), and \(N=a+b=s(q^2-1)\). Then \(\Gamma_I(R)\cong K_a\vee\overline K_b\) and \[\mathcal Z(\Gamma_I(R);u)=u^{N-2}(u+a)(u+b).\] Consequently \(Z(\Gamma_I(R))=M(\Gamma_I(R))=N-2\), the real symmetric minimum rank is \(2\), and the minimum zero forcing sets are exactly the complements of one vertex from each valuation layer, so there are \(ab=s^2q(q-1)^2\) of them. Within this length-three chain-quotient class, the polynomial recovers \(q\) and \(|I|\): its two nonzero root magnitudes are \(a<b\), hence \(q=b/a\) and \(s=a/(q-1)\).

## Assumptions and scope

Let \(R\) be a finite commutative ring with identity, \(I\subsetneq R\), and \(S=R/I\) a finite chain ring with maximal ideal \(\mathfrak m=(\pi)\),
\[
\mathfrak m^3=0,\qquad \mathfrak m^2\ne0,
\]
and residue field \(S/\mathfrak m\cong\mathbb F_q\). Write \(s=|I|\).

The ideal-based zero-divisor graph \(\Gamma_I(R)\) has as vertices the elements \(x\in R\setminus I\) for which \(xy\in I\) for some \(y\in R\setminus I\); distinct vertices are adjacent when their product lies in \(I\).

## Proof

A length-three finite chain ring has
\[
|S|=q^3,\qquad |\mathfrak m|=q^2,\qquad |\mathfrak m^2|=q.
\]
Its nonzero zero-divisors split into the two valuation layers
\[
A_0=\mathfrak m^2\setminus\{0\},\qquad B_0=\mathfrak m\setminus\mathfrak m^2,
\]
with
\[
|A_0|=q-1,\qquad |B_0|=q(q-1).
\]
If \(x,y\in A_0\), or \(x\in A_0\) and \(y\in B_0\), then \(xy=0\). If \(x,y\in B_0\), write \(x=\pi u\), \(y=\pi v\) with \(u,v\) units. Then
\[
xy=\pi^2uv\ne0.
\]
Thus the zero-divisor graph of \(S\) is
\[
K_{q-1}\vee\overline K_{q(q-1)}.
\]

Each residue class modulo \(I\) has exactly \(s\) lifts, and
\[
xy\in I\Longleftrightarrow (x+I)(y+I)=0\text{ in }S.
\]
Therefore
\[
\Gamma_I(R)\cong K_a\vee\overline K_b,
\qquad
a=s(q-1),\quad b=sq(q-1).
\]

The \(a\)-vertex clique is a true-twin class and the \(b\)-vertex independent set is a false-twin class. Hence a zero forcing set can leave at most one white vertex in either class. Conversely every such profile forces. With one white clique vertex, a blue independent-set vertex forces it. With one white independent-set vertex, a blue clique vertex forces it. With one white vertex in each class, a blue independent-set vertex first forces the white clique vertex, and then a blue clique vertex forces the remaining white vertex.

Thus the two classes contribute independently:
\[
\mathcal Z(\Gamma_I(R);u)
=
(u^a+a u^{a-1})(u^b+b u^{b-1})
=
u^{N-2}(u+a)(u+b).
\]
Therefore
\[
Z(\Gamma_I(R))=N-2,
\]
and the number of minimum zero forcing sets is
\[
ab=s^2q(q-1)^2.
\]

For minimum rank, assign vector \((0,1)\) to every clique vertex and \((1,0)\) to every independent-set vertex, using the symmetric bilinear form
\[
H=
\begin{pmatrix}
0&1\\
1&1
\end{pmatrix}.
\]
The resulting symmetric matrix has nonzero off-diagonal entries exactly on the graph edges and rank \(2\). Hence \(\operatorname{mr}\le2\). The standard inequality \(M(G)\le Z(G)\) gives
\[
\operatorname{mr}(\Gamma_I(R))
=
N-M(\Gamma_I(R))
\ge N-Z(\Gamma_I(R))
=
2.
\]
So
\[
\operatorname{mr}(\Gamma_I(R))=2,\qquad M(\Gamma_I(R))=Z(\Gamma_I(R))=N-2.
\]

Finally the two nonzero roots are \(-a\) and \(-b\). Since \(b=qa>a\),
\[
q=\frac ba,\qquad s=\frac{a}{q-1}.
\]
Thus the polynomial itself recovers \(q\) and \(|I|\) inside this length-three class.

## Verification

The accompanying `verify.py` was read from its packaged path before replay. It constructs representative rings
\[
R=\mathbb Z/(p^3)\times\mathbb Z/s\mathbb Z
\]
with \(I=\{0\}\times\mathbb Z/s\mathbb Z\), derives the graph directly from multiplication, exhaustively enumerates every vertex subset in the tested cases, checks the closed polynomial, and verifies the rank-two witness by exact rational row reduction.

Exact replay output:

```text
q=2, s=1: a=1, b=2, polynomial={1: 2, 2: 3, 3: 1}, witness_rank=2
q=2, s=2: a=2, b=4, polynomial={4: 8, 5: 6, 6: 1}, witness_rank=2
q=2, s=3: a=3, b=6, polynomial={7: 18, 8: 9, 9: 1}, witness_rank=2
q=3, s=1: a=2, b=6, polynomial={6: 12, 7: 8, 8: 1}, witness_rank=2
PARAMETER_RECOVERY_OK
VERIFY_OK
```

The finite checks corroborate but do not replace the arbitrary-prime-power proof.

## Relationship to prior work

Redmond introduced the ideal-based zero-divisor graph. Anderson and Shirinkam later studied structural relationships with ordinary zero-divisor graphs and complete or complete-bipartite cases; their article lists \(13A15\) first in its Mathematics Subject Classification.

A published same-object reconstruction result shows that, for finite chain-ring quotients of nilpotency length at least three, the graph itself recovers the quotient length, residue-field order, and \(|I|\). That graph-level recovery is prior coverage. General zero forcing polynomial theory supplies the counting invariant and standard extremal tools.

Targeted literature and semantic-database searches did not locate the complete standard zero forcing polynomial, all minimum sets, exact real minimum rank, or direct recovery of \(q\) and \(|I|\) from the polynomial in the length-three ideal-based family. The most relevant exact-object publisher pages did not expose inspectable full text in this run, so that access limitation remains an originality risk.

## Limitations

The theorem assumes nilpotency length exactly \(3\). Longer chain quotients have additional valuation layers and are not covered. The polynomial recovers \(q\) and \(|I|\), not the isomorphism types of \(R\), \(I\), or \(R/I\). Minimum rank is over real symmetric graph-pattern matrices. Graph-level parameter recovery has broader prior coverage.

## References

1. S. P. Redmond, “An Ideal-Based Zero-Divisor Graph of a Commutative Ring,” *Communications in Algebra* 31 (2003), 4425–4443. DOI: 10.1081/AGB-120022801. Published online 1 February 2007.
2. D. F. Anderson and S. Shirinkam, “Some Remarks on the Graph \(\Gamma_I(R)\),” *Communications in Algebra* 42 (2014), 545–562. DOI: 10.1080/00927872.2012.718021. Published online 18 October 2013.
3. K. Boyer et al., “The zero forcing polynomial of a graph,” arXiv:1801.08910; *Discrete Applied Mathematics* 258 (2019), 35–48.
4. AIM Minimum Rank — Special Graphs Work Group, “Zero forcing sets and the minimum rank of graphs,” *Linear Algebra and its Applications* 428 (2008), 1628–1648.
