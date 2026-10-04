# Exact odd-dimensional all-symbol PIR multiplicity of binary first-order Reed–Muller codes
## Finding
For every odd integer \(m\ge 3\), the binary first-order Reed–Muller code \(\mathrm{RM}_2(1,m)\) has maximum all-symbol PIR multiplicity
\[
t_{\max}=\frac{2^m-2}{3}.
\]
Equivalently, if the requested coordinate itself is reserved as the singleton recovery set, then the largest possible number of additional pairwise disjoint recovery sets is
\[
a_m=\frac{2^m-5}{3}.
\]

## Assumptions and scope
Use the standard evaluation generator matrix of \(\mathrm{RM}_2(1,m)\), whose coordinate indexed by \(x\in\mathbb F_2^m\) has column \(g_x=(1,x)^T\in\mathbb F_2^{m+1}\). A recovery set for coordinate \(p\) is a set of coordinate indices whose columns span \(g_p\). The all-symbol PIR multiplicity is the largest number of pairwise disjoint recovery sets available for every coordinate. Affine transitivity makes the optimum independent of \(p\).

The result concerns odd \(m\ge3\). The even-dimensional locality-three availability was already determined by Baumbaugh--Diaz--Friesenhahn--Manganiello--Vetter; the new statement closes the odd-dimensional exactness gap and translates it into the 2026 all-symbol PIR terminology.

## Proof
Fix a target \(p\in\mathbb F_2^m\). Any recovery set can be shrunk to a minimal subset whose columns sum to \(g_p\), because the field is binary. Since every generator column has first coordinate one, the cardinality of such a subset is odd. There is no one-element recovery set avoiding \(p\), because the columns \(g_x\) are distinct. Hence every nontrivial recovery set avoiding \(p\) has size at least three, and its size is odd.

A three-element set \(\{p+u,p+v,p+w\}\) recovers \(p\) precisely when
\[
g_{p+u}+g_{p+v}+g_{p+w}=g_p.
\]
Comparing the last \(m\) coordinates gives \(u+v+w=0\). Distinctness and avoidance of \(p\) mean that \(u,v,w\) are three distinct nonzero vectors, so \(w=u+v\) and
\[
\{u,v,w\}=U\setminus\{0\}
\]
for a unique two-dimensional subspace \(U\le\mathbb F_2^m\). Therefore disjoint recovery triples for \(p\) are exactly partial two-spreads: collections of two-dimensional subspaces meeting pairwise only in \(0\).

For odd \(m\), specialize the exact partial-spread theorem of Năstase and Sissokho to \(q=2\), \(t=2\), \(n=m\), and remainder \(r=1\). Its hypothesis \(2>(2^1-1)/(2-1)\) holds, and it gives a partial two-spread of cardinality
\[
\frac{2^m-2^{2+1}}{2^2-1}+1
=\frac{2^m-5}{3}.
\]
Translating the three nonzero vectors of each member \(U\) by \(p\) produces that many pairwise disjoint recovery triples for \(p\). Thus \(a_m\ge(2^m-5)/3\).

For the matching upper bound, suppose there were at least \((2^m-2)/3\) pairwise disjoint nontrivial recovery sets avoiding \(p\). The \(2^m-1\) available non-target coordinates and the size-at-least-three property force every one of the first \((2^m-2)/3\) sets to have size exactly three. They would therefore give a partial two-spread of size \((2^m-2)/3\), covering exactly \(2^m-2\) nonzero vectors of \(\mathbb F_2^m\) and leaving one nonzero vector \(z\).

But the XOR of the three nonzero vectors in every two-dimensional subspace is zero. Hence the XOR of all covered nonzero vectors would be zero. The XOR of all nonzero vectors of \(\mathbb F_2^m\) is also zero for \(m\ge2\), since each coordinate is one exactly \(2^{m-1}\) times. The single uncovered vector would therefore have to be zero, a contradiction. Consequently \(a_m\le(2^m-5)/3\), proving equality.

Finally, any family of recovery sets that contains the target coordinate can replace that member by the singleton \(\{p\}\) without harming disjointness; a family avoiding \(p\) has at most \(a_m\) members. Thus the maximum all-symbol PIR multiplicity is
\[
t_{\max}=1+a_m=\frac{2^m-2}{3}.
\]

## Verification
The standalone script `verify_rm_asp.py` checks the column-sum/recovery-triple correspondence, verifies explicit maximum-size partial two-spreads for \(m=3\) and \(m=5\), checks disjoint recovery families for every target coordinate in those cases, and independently verifies the arithmetic specialization of the partial-spread formula for several odd dimensions. These finite checks corroborate the proof but are not used as an infinite proof.

## Relationship to prior work
Baumbaugh, Diaz, Friesenhahn, Manganiello, and Vetter (2017/2018) proved that binary \(\mathrm{RM}(1,m)\) has locality three, determined availability \((2^m-1)/3\) for even \(m\), and for odd \(m\) gave only the lower bound \((2^m-4)/4\), explicitly noting that optimality had not been shown. Năstase and Sissokho (2016/2017) independently determined the exact maximum size of the relevant partial spreads in finite projective spaces. The proof above identifies the missing equivalence for recovery triples and also rules out larger arbitrary-size disjoint recovery families, not merely larger locality-three families.

Boruchovsky, Gruica, Niemann, and Yaakobi (2026) introduced the all-symbol PIR framework and listed the all-symbol PIR/batch properties of Reed–Muller codes among the remaining directions. Their definition counts the requested coordinate itself as a valid singleton recovery set, which explains the shift from availability \((2^m-5)/3\) to all-symbol PIR multiplicity \((2^m-2)/3\).

A separate 2025 line of work by Ly and Soljanin characterizes recovery sets of Reed–Muller *message symbols* for service-rate and one-step majority-logic questions. Those targets are polynomial coefficients rather than arbitrary stored codeword coordinates, so those results do not imply the present all-symbol coordinate theorem.

## Limitations
The theorem is for binary first-order Reed–Muller codes and odd \(m\ge3\). It does not determine all-symbol batch multiplicity, does not address higher-order or nonbinary Reed–Muller codes, and does not classify all maximum recovery families. Originality is supported by direct comparison with the cited primary sources and focused searches, but literature search cannot constitute an absolute proof that no equivalent statement exists under different terminology.

## References
1. A. Boruchovsky, A. Gruica, J. Niemann, E. Yaakobi, “Serving Every Symbol: All-Symbol PIR and Batch Codes,” arXiv:2601.04041, first posted 7 January 2026.
2. T. Baumbaugh, Y. Diaz, S. Friesenhahn, F. Manganiello, A. Vetter, “Batch Codes from Hamming and Reed–Muller Codes,” arXiv:1710.07386; J. Algebra Combin. Discrete Appl. 5(3), 153–165 (2018), DOI 10.13069/jacodesmath.466634.
3. E. Năstase, P. Sissokho, “The maximum size of a partial spread in a finite projective space,” arXiv:1605.04824; J. Combin. Theory Ser. A 152 (2017), 353–362.
4. H. Ly, E. Soljanin, “Optimum 1-Step Majority-Logic Decoding of Binary Reed-Muller Codes,” arXiv:2508.08736 (2025/2026 versions).
