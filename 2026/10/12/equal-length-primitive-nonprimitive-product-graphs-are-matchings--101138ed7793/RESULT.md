# Equal-length primitive nonprimitive-product graphs are matchings
## Finding
Let \(A\) be a finite alphabet with at least two letters, and fix \(\ell\ge1\). Form \(G_\ell(A)\) with the primitive words in \(A^\ell\) as vertices, joining distinct primitive words \(p,q\) exactly when \(pq\) is non-primitive.

Then \(G_\ell(A)\) is a matching. Equivalently, every primitive word has at most one distinct equal-length primitive word whose concatenation with it is non-primitive.

If \(n=|A|\) and \(\pi_n(m)\) is the number of primitive words of length \(m\), then
\[
|E(G_\ell(A))|
=\frac12\sum_{\substack{d\mid\ell\\d\ge3,\ d\ {\rm odd}}}
\pi_n\!\left(\frac{2\ell}{d}\right).
\]
The same sum without the factor \(1/2\) is exactly the number of vertices incident to an edge.

## Assumptions and scope
A nonempty word is primitive if it is not a proper integer power. Concatenation is ordinary word product.

The edge relation is symmetric: if \(pq=r^k\), then \(qp\) is a cyclic conjugate of \(r^k\) and is again a \(k\)-th power.

The primary source already classifies all ordered pairs of distinct equal-length primitive words with non-primitive product and counts them. The new statement is the global degree rigidity: those pairs form disjoint partner pairs rather than a relation that can branch at one primitive word.

## Proof
Take an edge \(p\!-\!q\). Proposition 4.1 of Echi, Khalfallah, and Kroumi implies that there is an odd integer
\[
d\ge3,\qquad d\mid\ell,
\]
such that \(pq\) is a \(d\)-th power of a primitive root of length
\[
a=\frac{2\ell}{d}.
\]

Suppose one primitive word \(p\) had two partners \(q_1,q_2\). Write
\[
pq_1=r_1^{d_1},\qquad pq_2=r_2^{d_2},
\]
with primitive \(r_1,r_2\) and odd divisors \(d_1,d_2\ge3\) of \(\ell\). Put
\[
a=\frac{2\ell}{d_1},\qquad b=\frac{2\ell}{d_2}.
\]
Since \(p\) is a common prefix of \(r_1^\omega\) and \(r_2^\omega\), it has periods \(a\) and \(b\).

If \(d_1\ne d_2\), the Fine--Wilf threshold holds:
\[
\ell\ge a+b-\gcd(a,b).
\]
After division by \(\ell\), this is
\[
1\ge\frac2{d_1}+\frac2{d_2}-\frac2{\operatorname{lcm}(d_1,d_2)}.
\]
For distinct odd integers at least \(3\), this is elementary. If both are at least \(5\), their two positive terms total at most \(4/5\). If one is \(3\), say \(d_1=3\), then either \(3\mid d_2\), giving \(2/3\), or \(d_2\ge5\) is coprime to \(3\), giving
\[
\frac23+\frac4{3d_2}\le\frac{14}{15}.
\]

Fine--Wilf therefore gives \(p\) period \(g=\gcd(a,b)\). Since \(a,b\) are multiples of \(g\) and \(\ell\ge a,b\), the prefixes \(r_1,r_2\) themselves have period \(g\). Their primitivity forces \(a=g=b\), contradicting \(d_1\ne d_2\).

Thus \(d_1=d_2\), hence \(a=b<\ell\). Both primitive roots are the same length-\(a\) prefix of \(p\), so \(r_1=r_2\). Therefore
\[
pq_1=r_1^{d_1}=r_2^{d_2}=pq_2,
\]
and cancellation gives \(q_1=q_2\). Every vertex has degree at most one.

The source's Theorem 4.2 counts ordered pairs by
\[
\epsilon(n,\ell)=
\sum_{\substack{d\mid\ell\\d\ge3,\ d\ {\rm odd}}}
\pi_n\!\left(\frac{2\ell}{d}\right).
\]
Each graph edge contributes exactly the two ordered pairs \((p,q)\) and \((q,p)\), yielding the edge and incident-vertex formulas.

## Verification
Run `python3 verify.py` beside `certificate.json`.

The checker independently enumerates primitive words and the non-primitive-product relation for binary lengths through \(9\) and ternary lengths through \(6\). In every case the maximum graph degree is at most \(1\), and the ordered-pair count agrees with the source formula computed using Möbius inversion.

A second finite window checks symmetry of the relation. The numerical Fine--Wilf inequality is checked for every distinct odd exponent pair through \(999\). These are consistency checks; the infinite theorem is proved symbolically above.

## Relationship to prior work
Echi, Khalfallah, and Kroumi give a complete structural description of pairs of primitive words whose product is non-primitive. In the equal-length case, Proposition 4.1 forces an odd product exponent at least \(3\), and Theorem 4.2 counts all ordered pairs.

Their paper does not state that the corresponding equal-length relation has maximum degree \(1\). The ordered-pair count alone also does not imply that different parametrized pairs cannot share an endpoint. The matching theorem follows by comparing two hypothetical decompositions sharing the same first word and applying Fine--Wilf across their two induced periods.

Searches under “unique partner”, “matching”, “same-length primitive product”, and direct degree formulations located the source and related primitive-product work but no published statement of this global degree rigidity.

## Limitations
The theorem is restricted to equal-length factors. When \(|p|\ne|q|\), the source's general parametrization has additional cases, and no analogous matching assertion is made.

An unindexed note could contain the same matching reformulation.

## References
1. O. Echi, A. Khalfallah, and D. Kroumi, “On Primitive Words With Non-Primitive Product,” RAIRO - Theoretical Informatics and Applications 56 (2022), article 4, DOI 10.1051/ita/2022004.
2. N. J. Fine and H. S. Wilf, “Uniqueness theorems for periodic functions,” Proceedings of the American Mathematical Society 16 (1965), 109--114.
