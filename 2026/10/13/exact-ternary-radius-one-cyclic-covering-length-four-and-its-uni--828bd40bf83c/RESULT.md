# Exact ternary radius-one cyclic covering length four and its unique symmetry class

## Finding

Let \(\Sigma=\{0,1,2\}\), and let \(\mathcal{L}_3(4,1)\) denote the minimum length of a **single cyclic sequence** whose consecutive windows of length four cover all \(81\) words in \(\Sigma^4\) within Hamming distance one. Then

\[
\mathcal{L}_3(4,1)=12.
\]

Exactly \(48\) **indexed** sequences of length \(12\) attain this minimum. They form one orbit under cyclic rotation, reversal, and uniform permutation of the three alphabet symbols. Without allowing reversal, there are exactly two orbits, each of cardinality \(24\), represented by `001022021121` and its reversal. Thus the value and the full equality-case classification are exact.

## Assumptions and scope

A cyclic sequence \(s=(s_0,\ldots,s_{m-1})\in\Sigma^m\), for \(m\ge1\), has a window \(w_i(s)=(s_i,s_{i+1},s_{i+2},s_{i+3})\), with indices taken modulo \(m\), at every position \(0\le i<m\). For words \(x,y\in\Sigma^4\), the Hamming distance \(d_H(x,y)\) is the number of differing coordinates. The covering condition is

\[
(\forall y\in\Sigma^4)(\exists i\in\{0,\ldots,m-1\})\quad d_H(y,w_i(s))\le1.
\]

An indexed sequence records each position as a distinguished starting index; rotated tuples count separately unless they literally agree. A uniform alphabet relabeling is a single permutation applied to all coordinates, not an independent relabeling at each position. Reversal and rotation preserve the covering property. The theorem is only about the ternary alphabet, four-coordinate windows, and radius one; it is **not** a statement about all covering codes or arbitrary numbers of cyclic components.

## Proof

**(1) Sphere-volume lower bound.** Each radius-one ball in \(\Sigma^4\) contains exactly \(1+4(3-1)=9\) words. A cyclic sequence of length \(m\) supplies at most \(m\) such balls. Since \(|\Sigma^4|=3^4=81\), covering is impossible for \(m\le8\).

**(2) Exhaustive elimination of lengths nine through eleven.** For every integer \(m\in\{9,10,11,12\}\), enumerate every element of \(\Sigma^m\) exactly once, using lexicographic Cartesian products of the three symbols. For each candidate, form its \(m\) modular length-four windows and bitwise-union their closed Hamming balls. Index the \(81\) target words by their lexicographic positions; represent a set by the corresponding \(81\)-bit nonnegative integer. The full target set has mask \(2^{81}-1\). A candidate satisfies the covering property if and only if the union mask equals that full mask. The exact counts of successful sequences are

\[
\begin{array}{c|rrrr}
m & 9 & 10 & 11 & 12\\ \hline
|\Sigma^m| & 19683 & 59049 & 177147 & 531441\\
\text{successful} & 0 & 0 & 0 & 48.
\end{array}
\]

For additional reproducible diagnostics, the maximum numbers of targets covered by any candidate at these four lengths are respectively \(69,76,76,81\). All those values follow from the finite loops specified above and implemented without any external search or optimization library in `verify.py`. Thus lengths below \(12\) are impossible; at least one length-\(12\) solution exists.

**(3) Optimal witness.** The cyclic twelve-symbol word `001022021121` has all \(81\) target words within Hamming distance one of its twelve length-four windows; this is checked by direct calculation of the same mask, not by inferring from the aggregate census. Hence \(\mathcal{L}_3(4,1)\le12\), which meets the lower bound from steps (1)--(2).

**(4) Equality cases and symmetries.** Let \(a\) be the preceding witness and \(a^{\mathrm{rev}}\) its reversal. Enumerate all six permutations \(\pi\in S_3\) of the alphabet and all twelve rotations of \(\pi(a)\), forming \(G(a)\). Compute \(G(a^{\mathrm{rev}})\) likewise. The exact set operations give \(|G(a)|=|G(a^{\mathrm{rev}})|=24\), \(G(a)\cap G(a^{\mathrm{rev}})=\varnothing\), and their union equals the set of all \(48\) successful length-\(12\) tuples from step (2). Thus there are two rotation-and-relabeling classes, exchanged by reversal, and one class once reversal is allowed. These claims concern all length-\(12\) indexed sequences; they are not estimates from random sampling.

## Verification

Run `python3 verify.py` using Python \(3.10\) or later and no third-party dependencies. It recomputes every length-\(9\), \(10\), \(11\), and \(12\) target mask from scratch, verifies the exact counts and maximal partial-coverage sizes, checks the witness, constructs the two symmetry orbits, and confirms that they partition the complete set of all optimizers. Successful execution ends in `VERIFY_OK`. An independently written C++ enumeration is also included as `verify_independent.cpp`; compiling it with a C++17 compiler provides a secondary cross-language check of the complete census and symmetry count.

## Relationship to prior work

Chung and Cooper introduced cyclic de Bruijn covering codes and published general bounds and a table of *binary* small parameters. Chee, Etzion, Ta and Vu developed covering sequences and covering-sequence codes, with their finite table focused on binary parameters. Etzion's 2026 nonbinary constacyclic Hamming-code approach constructs covering-*sequence codes* (multiple cyclic components); this does not give a sharp lower bound or a classification of single-cycle ternary length-four optima. Ta and Vu's 2026 constant-factor covering-sequence constructions apply in the asymptotic large-span regime, without supplying the claimed finite value or symmetry classification. Our result determines one exact finite nonbinary parameter, plus all equality cases; it neither strengthens nor contradicts those general construction theorems.

## Limitations

The minimum and orbit classification are established by a complete, transparently specified finite exhaustive computation, not by a closed-form analytic enumeration of optimizers. The result says nothing about other ternary window lengths or radii, and nothing about arbitrary families of multiple cycles. An unindexed earlier calculation of this finite parameter cannot be excluded by the literature searches conducted. Independent scientific validation has not been performed.

## References

1. F. Chung and J. N. Cooper, *De Bruijn Cycles for Covering Codes*, arXiv:math/0310385 (2003), https://arxiv.org/abs/math/0310385.
2. Y. M. Chee, T. Etzion, H. Ta and V. K. Vu, *Constructions of covering sequences and 2D-sequences*, Designs, Codes and Cryptography 93 (2025), https://doi.org/10.1007/s10623-025-01726-5.
3. H. Ta and V. K. Vu, *Near-Optimal Covering Sequences*, arXiv:2606.29236 (2026), https://arxiv.org/abs/2606.29236.
4. T. Etzion, *Covering Sequences and Covering-Sequences Codes*, arXiv:2607.14840v1 (first posted 16 July 2026), https://arxiv.org/abs/2607.14840.
