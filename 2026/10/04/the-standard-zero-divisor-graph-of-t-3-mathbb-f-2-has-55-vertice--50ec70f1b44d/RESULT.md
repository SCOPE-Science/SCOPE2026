# The standard zero-divisor graph of \(T_3(\mathbb F_2)\) has 55 vertices, not 27

## Finding

For \(R=T_3(\mathbb F_2)\), using the standard noncommutative zero-divisor digraph convention (all nonzero one-sided zero-divisors as vertices) and its underlying simple graph (distinct \(A,B\) adjacent when \(AB=0\) or \(BA=0\)), the graph has exactly \(55\) vertices, \(420\) edges, and diameter \(2\). Therefore the 27-vertex graph used in Hanna--Alkandari--Bhat (2025) is not the standard zero-divisor graph of \(T_3(\mathbb F_2)\); metric invariants computed on that 27-vertex host cannot be transferred to the standard graph without recomputation.

The discrepancy is structural rather than a naming issue. The 2025 article states that the upper-triangular binary ring has \(2^6=64\) elements, then works with a 27-vertex graph after excluding the remaining nonzero matrices. Under the standard noncommutative zero-divisor definition used in the earlier matrix-ring literature, the vertex set must instead contain all nonzero one-sided zero-divisors.

## Assumptions and scope

Let \(T_3(\mathbb F_2)\) be the ring of matrices
\[
A=\begin{pmatrix}
a&b&c\\
0&d&e\\
0&0&f
\end{pmatrix},
\qquad a,b,c,d,e,f\in\mathbb F_2.
\]
The directed zero-divisor graph has every nonzero left or right zero-divisor as a vertex and an arc \(A\to B\) when \(AB=0\). Its underlying simple graph joins distinct vertices when at least one of \(AB\) and \(BA\) vanishes.

This is the convention explicitly stated for noncommutative rings by Abdioğlu (2016) and used by Tucci--McDermott--El-Khatib--Harvey (2019).

## Proof

There are \(2^6=64\) upper-triangular binary \(3\times3\) matrices. An upper-triangular matrix is a unit exactly when every diagonal entry is a unit. Over \(\mathbb F_2\), the only nonzero field element is \(1\), so a unit has diagonal \((1,1,1)\), while its three strictly upper-triangular entries are arbitrary. Hence there are
\[
2^3=8
\]
units.

A finite ring element is either a unit or a zero-divisor. Therefore \(T_3(\mathbb F_2)\) has \(64-8=56\) zero-divisors including the zero matrix, and exactly
\[
56-1=55
\]
nonzero zero-divisors. Thus the standard zero-divisor graph cannot have 27 vertices.

For the two additional graph invariants, `verify.py` enumerates all 64 matrices from the six binary coordinates, identifies units independently by brute-force two-sided inversion, checks one-sided annihilators for every nonunit, constructs the underlying simple graph by testing \(AB=0\) or \(BA=0\) on every unordered pair, and performs breadth-first search from every vertex. The exact output is:

```text
VERIFY_OK
ring_elements=64
units=8
nonzero_zero_divisors=55
underlying_simple_edges=420
diameter=2
```

Thus the standard underlying graph has \(420\) edges and diameter \(2\).

## Verification

Two independent criteria are checked in `verify.py`: (i) brute-force existence of a two-sided inverse and (ii) the triangular diagonal criterion. They agree on exactly eight units. Every one of the other 55 nonzero matrices is explicitly checked to have a nonzero one-sided annihilator, while no unit does.

The edge count is exhaustive over all \(\binom{55}{2}=1485\) unordered vertex pairs. Diameter is obtained by exact breadth-first search from each of the 55 vertices, with connectivity asserted at every start vertex.

## Relationship to prior work

Li and Tucci (2013) developed zero-divisor graphs for upper-triangular matrix rings and fully described the \(2\times2\) finite-domain case, but did not give this \(3\times3\), \(\mathbb F_2\) host census. Abdioğlu (2016) states the standard noncommutative directed-graph convention: the vertex set is the union of nonzero left and right zero-divisors and \(r\to s\) exactly when \(rs=0\). Tucci et al. (2019) explicitly record that, in a finite ring, every element is a unit or a zero-divisor and that an upper-triangular matrix is a unit exactly when all diagonal entries are units.

Hanna, Alkandari, and Bhat (2025) instead describe the same six-coordinate binary upper-triangular ring as having 64 matrices, then construct a 27-vertex graph and discard the rest. That host therefore differs from the standard zero-divisor graph before any metric-dimension computation begins. The present finding does not assert that their calculations on their selected 27-vertex graph are arithmetically wrong; it establishes that those values are not invariants of the standard \(T_3(\mathbb F_2)\) zero-divisor graph without a fresh computation on the 55-vertex host.

## Limitations

This finding is specific to \(T_3(\mathbb F_2)\) and to the standard noncommutative zero-divisor convention stated above. It does not compute the fault-tolerant metric dimension or fault-tolerant edge metric dimension of the corrected 55-vertex graph. It also does not classify alternative graph conventions that intentionally impose extra symmetry or commutativity conditions.

The 2013 Li--Tucci full PDF was not retrievable during this run, although its publisher record and abstract were inspected; the proof here does not depend on unavailable material from that paper. The 2016 and 2019 full-text renderings and the 2025 article text were sufficient for the definitional and counting comparison.

## References

1. A. Li and R. P. Tucci, “Zero Divisor Graphs of Upper Triangular Matrix Rings,” *Communications in Algebra* 41 (2013), 4622–4636. DOI: 10.1080/00927872.2012.706841. Published online 2013-09-20.
2. C. Abdioğlu, “Zero-divisor graph of matrix rings and Hurwitz rings,” *Turkish Journal of Mathematics* 40 (2016), 201–209. DOI: 10.3906/mat-1505-51. Published online 2015-08-19; final version 2016-01-01.
3. R. P. Tucci, S. McDermott, O. El-Khatib, and R. B. Harvey, “Zero-Divisor Graphs of Upper Triangular Matrices over Finite Fields,” *International Journal of Recent Engineering Research and Development* 4(1) (2019), 87–91.
4. L. A. Hanna, M. M. Alkandari, and V. K. Bhat, “Fault-Tolerant Metric Dimension and Applications: Zero-Divisor Graph of Upper Triangular Matrices,” *Mathematics* 13 (2025), 3678. DOI: 10.3390/math13223678.
