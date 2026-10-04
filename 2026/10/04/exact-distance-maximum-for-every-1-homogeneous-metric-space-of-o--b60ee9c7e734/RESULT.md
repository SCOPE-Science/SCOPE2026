# Exact distance maximum for every 1-homogeneous metric space of order \(4k+2\)

## Finding

Let \(\Delta_1(n)\) denote the maximum number of distinct distances, including \(0\), in an \(n\)-point 1-homogeneous metric space. For every odd positive integer \(m\),
\[
\Delta_1(2m)=\frac{3m+1}{2}.
\]
Equivalently, for every \(k\ge 0\),
\[
\boxed{\Delta_1(4k+2)=3k+2.}
\]

Thus the prime hypothesis in Proposition 6.11 of Bargetz–Bartoš–Kubiś–Luggin is unnecessary. In particular,
\[
\Delta_1(18)=14,\qquad \Delta_1(30)=23,\qquad \Delta_1(42)=32.
\]

## Assumptions and scope

All metric spaces here are finite. A metric space is 1-homogeneous when its full isometry group is transitive on points. The quantity \(\delta(X)\) is the number of values in \(\operatorname{Dist}(X)\), including \(0\), and \(\Delta_1(n)\) is the maximum of \(\delta(X)\) over 1-homogeneous \(n\)-point metric spaces.

The theorem treats precisely the case \(n\equiv2\pmod4\). It does not settle the remaining even orders whose 2-adic valuation is at least \(2\).

## Proof

Fix an odd positive integer \(m\), let \(X\) be a 1-homogeneous metric space with \(|X|=2m\), and put \(G=\operatorname{Aut}(X)\). Let \(c\) be the number of \(G\)-orbits on unordered pairs of distinct points.

Every positive distance class is \(G\)-invariant, hence is a union of \(G\)-orbits on unordered pairs. Therefore
\[
\delta(X)-1\le c.
\]

For each pair-orbit \(O_i\), regard \(O_i\) as the edge set of a graph on \(X\). Transitivity of \(G\) makes this graph regular; write its valency as \(d_i\ge1\). Since the pair-orbits partition all edges of the complete graph,
\[
\sum_{i=1}^{c} d_i=2m-1.
\]
Let \(s\) be the number of pair-orbits with \(d_i=1\). Every remaining orbit has valency at least \(2\), so
\[
2m-1\ge s+2(c-s)=2c-s,
\]
and hence
\[
c\le \frac{2m-1+s}{2}. \tag{1}
\]

It remains to bound \(s\). A valency-one pair-orbit is a \(G\)-invariant perfect matching. Its mate map \(\tau\), sending each point to its unique matched partner, is a fixed-point-free involution. Invariance of the matching gives
\[
\tau g=g\tau\qquad(g\in G),
\]
so \(\tau\) lies in the centralizer
\[
C=C_{\operatorname{Sym}(X)}(G).
\]
Distinct valency-one pair-orbits give distinct involutions of \(C\).

Because \(G\) is transitive, \(C\) is semiregular: if \(h\in C\) fixes one point \(x\), then for every \(y=gx\),
\[
h(y)=hg(x)=gh(x)=gx=y,
\]
so \(h\) is the identity. Consequently every \(C\)-orbit has size \(|C|\), and therefore
\[
|C|\mid |X|=2m.
\]

Since \(m\) is odd, the 2-part of \(|C|\) has order at most \(2\). If \(|C|\) is odd, \(C\) has no involutions. If \(|C|\) is even, every involution generates a Sylow \(2\)-subgroup, and distinct involutions generate distinct Sylow \(2\)-subgroups. By Sylow's theorem, the number of Sylow \(2\)-subgroups divides \(|C|/2\), which is an odd divisor of \(m\). Thus \(C\) has at most \(m\) involutions. Hence
\[
s\le m. \tag{2}
\]

Combining (1) and (2),
\[
c\le \frac{3m-1}{2},
\]
and therefore
\[
\delta(X)\le 1+c\le \frac{3m+1}{2}. \tag{3}
\]

For the matching lower bound, Bargetz–Bartoš–Kubiś–Luggin's Example 6.8 constructs, for every \(m\), a 1-homogeneous space \(D_m\) on \(2m\) points with
\[
\delta(D_m)=\left\lfloor\frac m2\right\rfloor+1+m.
\]
When \(m\) is odd this equals \((3m+1)/2\). Together with (3), this proves
\[
\Delta_1(2m)=\frac{3m+1}{2}.
\]
\(\square\)

## Verification

The proof has two independent layers.

First, the group-theoretic upper bound uses only: pair-orbit regularity under a transitive action; the fact that a valency-one invariant graph is a perfect matching whose mate map centralizes the action; semiregularity of the centralizer of a transitive permutation group; and Sylow's theorem when the degree has 2-adic valuation one. Each implication is proved explicitly above except the elementary Sylow counting statement.

Second, the lower bound is the published construction \(D_m\). For odd \(m\),
\[
\left\lfloor m/2\right\rfloor+1+m=(3m+1)/2.
\]

As a finite sanity check separate from the proof, the degree-18 transitive-group catalog was scanned by generator orbits on the \(153\) unordered pairs. Among all \(983\) transitive groups of degree \(18\), the maximum number of pair-orbits is \(13\), attained by 18T4 and 18T5. Thus any vertex-transitive coloring on \(18\) vertices has at most \(13\) positive edge colors, agreeing with \(\Delta_1(18)=14\) after the diagonal color is included. This computation is not used for the general theorem.

## Relationship to prior work

Bargetz, Bartoš, Kubiś, and Luggin introduced \(\Delta_1(n)\), gave the construction \(D_m\), and proved in Proposition 6.11 that
\[
\Delta_1(2(2k+1))=3k+2
\]
when \(2k+1\) is prime. Their Question 1 explicitly leaves open the case with exactly one factor of \(2\) and composite odd part. The argument above removes the primality condition entirely and therefore closes that whole subfamily of their open question.

Their Remark 6.14 also reformulates the problem as maximizing colors in a vertex-transitive edge-coloring of a complete graph. The proof above operates directly in that equivalent permutation-group language: positive colors are unions of pair-orbits, and the only way many pair-orbits can have minimum valency is through invariant perfect matchings controlled by the centralizer.

The standard fact that the centralizer of a transitive permutation group is semiregular is also recorded in the Encyclopedia of Mathematics entry “Permutation group”; it is reproved in one line above so no external group-theoretic theorem beyond Sylow's theorem is needed.

Targeted exact-formula, vertex-transitive-coloring, and pair-orbit searches did not locate the prime-free statement. This supports, but cannot prove, originality.

## Limitations

The theorem settles only orders with exactly one factor of \(2\). It gives no new exact value for \(n=2^a q\) with \(a\ge2\) and odd \(q>1\), which remains the other family singled out by the source's Question 1.

The originality check cannot exclude an unpublished observation or an indexed result phrased in substantially different terminology.

The degree-18 catalog computation is only a sanity check; the theorem for all odd \(m\) rests on the general argument above.

## References

1. Christian Bargetz, Adam Bartoš, Wiesław Kubiś, Franz Luggin, “Homogeneous isosceles-free spaces,” arXiv:2305.03163, first posted 4 May 2023; *Revista de la Real Academia de Ciencias Exactas, Físicas y Naturales. Serie A. Matemáticas* 118 (2024), article 118. DOI: 10.1007/s13398-024-01587-y.
2. “Permutation group,” *Encyclopedia of Mathematics*, entry noting that the centralizer of a transitive permutation group is semiregular.
3. Alexander Hulpke and collaborators, GAP Transitive Groups library / TransGrp data, used only for the finite degree-18 sanity check.
