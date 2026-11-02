# Scientific review: all-window optimal cyclic Reed–Muller read order

## Correctness — PASS

The claimed domain is precisely the binary affine-evaluation code of length \(2^m\), for every integer \(m\ge2\), and cyclic read widths \(1\le b\le2^m\). The universal bound is established by counting all-zero-window incidences over all \(2^{m+1}-1\) nonzero affine functions, with no independence assumption on an arbitrary coordinate window. The achieving order is derived from a primitive-field trace sequence: the exact counts of zero and one width-\(b\) patterns before insertion follow from independent trace functionals for \(b\le m\). The one-symbol insertion changes an all-zero-window count by at most one. A separate primitive-polynomial recurrence prohibits all-zero runs of length \(m+1\) for both affine constants. The proof explicitly excludes the zero codeword and handles \(b=1\), \(b=m\), \(b=m+1\), and \(b=2^m\). The independently written direct enumerator in `verify.py` checks dimensions \(2\) through \(8\), all widths through \(m+1\), and all rooted coordinate orders at dimension three. This is corroboration, not the basis of the infinite theorem.

## Originality — PASS, qualified

The closest directly relevant published statement is Pan–Ling–Liu, arXiv:2309.08920, Section 4, Theorem 4.6. Its evaluation coordinates are explicitly ordered lexicographically; its sharp \(b\)-symbol distance within that fixed presentation does not optimize over coordinate permutations. For example, at \(m=4,b=3\), it gives \(10\), whereas the proved coordinate permutation realizes \(14\). Zhu–Shi, arXiv:2203.11567, considers irreducible cyclic codes on nonzero field elements and their \(b\)-symbol spectra, not the permutation optimum of the full affine evaluation code. Ding–Zhang–Ge, arXiv:1609.09236, provides general \(b\)-symbol bounds and other constructions, not this specialized sharp family. Indexed results concerning simplex cyclic or one-coordinate-punctured pair distance and a finite extended-Hamming pair-spectrum classification cover related \(b=2\) information; the claimed contribution is the simultaneous **all-width, all-dimensional** theorem, in particular widths \(b\ge3\). Relevant research-record searches did not reveal equivalent or stronger coverage. This does not prove historical uniqueness; unindexed permutation-optimized read-distance literature remains a priority risk.

## Value — PASS

Overlapping \(b\)-symbol reading is sensitive to a code's coordinate ordering. The result solves a natural optimization problem for an important classical binary code, giving one implementable layout that attains all read-window optima simultaneously. It replaces the conventional lexicographic profile \(\min(2^{m-1}+b-1,2^m)\) with a sharp permutation-optimized profile \(2^m-2^{m-b}\) for \(b\le m\), and reaches the full-length bound already at \(b=m+1\). The gap grows with code length at fixed \(b\ge2\). The main contribution is a universal bound paired with a construction, not the restatement of prior pair-distance instances. No claim of uniqueness of optimal layouts or improved physical channel performance is made.

## Closest literature and limitations

- Ding, Zhang, Ge, *Maximum Distance Separable Codes for b-Symbol Read Channels*, arXiv:1609.09236v1 (2016-09-29), general read metric and bounds.
- Zhu, Shi, *The b-symbol weight distribution of irreducible cyclic codes and related consequences*, arXiv:2203.11567v1 (2022-03-22), related nonzero-field cyclic simplex hierarchy.
- Pan, Ling, Liu, *New bounds for b-Symbol Distances of Matrix Product Codes*, arXiv:2309.08920v1 (2023-09-16), Section 4 and Theorem 4.6, fixed lexicographic Reed–Muller order.

The theorem is binary, first-order, and cyclic-window-specific. The finite program is not a proof for unbounded dimension. Historical-priority checking beyond the inspected texts remains independent work.

Self-review: passed. Independent audit: not yet performed.
