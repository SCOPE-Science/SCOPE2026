# Exact image-rank profile and mean of endomorphism monoids of finite cycles

## Finding

For the simple undirected cycle \(C_n\) with \(n\ge3\), write \(R_n(z)=\sum_{f\in\operatorname{End}(C_n)}z^{|\operatorname{im}f|}\). If \(n\) is odd then \(R_n(z)=2nz^n\). If \(n=2m\ge4\), let \(A_s\) be the adjacency matrix of the simple path on \(s\) vertices, set \(T_s=\operatorname{tr}(A_s^{2m})\) for \(s\ge1\), and \(T_0=0\). Then
\[
R_{2m}(z)=4mz^{2m}+2m\sum_{r=2}^{m+1}(T_r-2T_{r-1}+T_{r-2})z^r.
\]
For a uniformly chosen endomorphism of \(C_{2m}\), its exact expected image size is
\[
\mathbb E|\operatorname{im}f|=\frac{4^m+4m}{\binom{2m}{m}+2}\sim\sqrt{\pi m}.
\]
Conditional on non-invertibility, the mean image size is exactly \(4^m/\binom{2m}{m}\). In particular, the noninvertible image ranks occur precisely at sizes \(2,\ldots,m+1\). The total number of endomorphisms is \(2m(\binom{2m}{m}+2)\), consistent with the known total-count formula.

## Assumptions and scope

A simple cycle \(C_n\) has vertex set \(\mathbb Z/n\mathbb Z\), with undirected edges connecting residues differing by \(1\). No loops are present. An endomorphism means an adjacency-preserving transformation from this cycle to itself. Its **image rank** is the number of distinct vertices in its image; this is different from the rank of a monoid, meaning the minimum size of a generating set. The theorem concerns ordinary (not weak) endomorphisms and holds for every integer \(n\ge3\). A path on one vertex has zero adjacency matrix, hence \(T_1=0\).

## Proof

Every graph endomorphism \(f\) is uniquely specified by its initial image \(a\in\mathbb Z/n\mathbb Z\) and a sequence \((\varepsilon_1,\ldots,\varepsilon_n)\in\{-1,1\}^n\) of edge increments such that \(\sum_{i=1}^n\varepsilon_i\equiv0\pmod n\). Indeed, set \(f(j)=a+\sum_{i=1}^j\varepsilon_i\pmod n\) for successive cycle vertices, and use the closing condition for the final edge. For \(n\ge3\), the two neighbors are distinct, so each map determines one increment sequence. Since its sum has absolute value at most \(n\), the sum is either \(-n\), \(0\), or \(n\). The first and last cases are precisely the two constant increment sequences, which produce \(2n\) dihedral automorphisms. A zero sum is possible only for even \(n=2m\), when there are \(\binom{2m}{m}\) increment sequences, each admitting \(2m\) initial images.

Take a zero-sum increment sequence of length \(2m\). Its partial sums \(S_0=0, S_j=\sum_{i=1}^j\varepsilon_i\) form a nearest-neighbor bridge with \(S_{2m}=0\). Write \(h=\max_{0\le j\le2m}S_j-\min_{0\le j\le2m}S_j\). There are exactly \(m\) positive and \(m\) negative steps, so \(1\le h\le m\). The visited partial sums form every integer in this interval, and reduction modulo \(2m\) is injective there; hence the image cardinality is \(h+1\). Every \(1\le h\le m\) actually occurs: use \(h\) consecutive positive steps, \(h\) consecutive negative steps, followed by \(m-h\) alternating positive/negative pairs. This is a closed bridge of span \(h\).

Let \(b_h\) be the number of zero-sum increment sequences with span exactly \(h\). For every \(s\ge1\), the trace \(T_s=\operatorname{tr}(A_s^{2m})\) counts closed nearest-neighbor walks of length \(2m\) confined to a path with \(s\) vertices, keeping track of their starting vertex. A bridge with span \(h\) admits exactly \(s-h\) vertical translations into such a path if \(h\le s-1\), and none otherwise. Consequently
\[
T_s=\sum_{h=1}^{s-1}(s-h)b_h,\qquad b_h=T_{h+1}-2T_h+T_{h-1}.
\]
Each admissible bridge gives \(2m\) distinct endomorphisms according to its initial image. With the \(4m\) automorphisms, this proves the full rank polynomial. Optionally, the trace is a closed spectral expression
\[
T_s=\sum_{j=1}^{s}\left(2\cos\frac{\pi j}{s+1}\right)^{2m},
\]
with the sum equal to an integer; no approximate numerical evaluation is required.

For the expectation, let \(M\) be the largest partial sum of a uniformly chosen zero-sum bridge of length \(2m\). For \(1\le a\le m\), reflecting a bridge at its first visit to height \(a\) bijects bridges with \(M\ge a\) and unrestricted nearest-neighbor walks from \(0\) to \(2a\) in \(2m\) steps. Thus
\[
\mathbb P(M\ge a)=\frac{\binom{2m}{m+a}}{\binom{2m}{m}}.
\]
By sign reversal, the expected negative minimum equals the expected maximum, hence
\[
\mathbb E(h)=\frac{2}{\binom{2m}{m}}\sum_{a=1}^{m}\binom{2m}{m+a}
=\frac{4^m}{\binom{2m}{m}}-1,
\]
using symmetry of the binomial row. Therefore the mean rank of a nonautomorphism is \(1+\mathbb E(h)=4^m/\binom{2m}{m}\). Averaging this over the \(2m\binom{2m}{m}\) nonautomorphisms together with the \(4m\) automorphisms of rank \(2m\), then dividing by \(2m(\binom{2m}{m}+2)\), yields
\[
\mathbb E|\operatorname{im}f|=\frac{4^m+4m}{\binom{2m}{m}+2}.
\]
Finally \(\binom{2m}{m}\sim4^m/\sqrt{\pi m}\), and \(4m/4^m\to0\), proving the stated asymptotic.

## Verification

The included `verify.py` independently enumerates all endomorphisms from their initial vertices and edge increments for \(n=4,6,8,10,12\), compares the exact histogram to the path-adjacency trace formula, and checks the total count and first moment by integer arithmetic. For \(n=4\), the histogram is \(\{2:8,3:16,4:8\}\); for \(n=6\) it is \(\{2:12,3:72,4:36,6:12\}\). Execution prints `VERIFY_OK`. The finite checks illustrate the formulas but do not replace the general argument above.

## Relationship to prior work

Dimitrova, Fernandes, Koppitz, and Quinteiro give descriptions of the endomorphism monoids of cycles, their Green relations, regularity, minimal generating-set rank, and total cardinality. In particular, their Proposition 1.9 proves the same aggregate total \(2m(\binom{2m}{m}+2)\). Here we refine the aggregate by the image cardinalities **of all individual endomorphisms**, obtaining an explicit finite-difference path-trace distribution and its first moment. The trace-weighted-bridge argument goes beyond their reported total count; their result on generating rank concerns a different statistic. Michels and Knauer previously established the endomorphism total and kernel congruence-class counts for cycles. Existing exact work on **idempotent** cycle retractions counts a strict subset of these maps and does not give the distribution of all endomorphisms. The combinatorial reflection principle itself is classical and not claimed as novel.

## Limitations

The theorem treats ordinary endomorphisms of simple cycles, not weak endomorphisms, arbitrary graph homomorphisms, or other graph families. The 2009 primary paper on congruence classes of paths and cycles was available only via its abstract, citation and publicly indexed total-count data, not full text; it might contain a related rank refinement that could not be excluded completely. No claim of absolute historical priority is made.

## References

1. I. Dimitrova, V. H. Fernandes, J. Koppitz, and T. M. Quinteiro, *On monoids of endomorphisms of a cycle graph*, arXiv:2310.04149, first posted 6 October 2023. Journal version: *Mathematica Slovaca* 74 (2024), 1071–1088, DOI:10.1515/ms-2024-0078. https://arxiv.org/abs/2310.04149
2. M. A. Michels and U. Knauer, *The congruence classes of paths and cycles*, *Discrete Mathematics* 309 (2009), 5352–5359, DOI:10.1016/j.disc.2008.11.022. https://doi.org/10.1016/j.disc.2008.11.022
3. OEIS A112850, total number of endomorphisms of undirected even cycles, https://oeis.org/A112850; OEIS A112849, induced congruence classes, https://oeis.org/A112849.
