# The finite-one cardinality spectrum inside many-one degrees is one, three, or countably infinite
## Finding

For a many-one degree \(\mathbf d\), write
\[
F(\mathbf d)=\{[X]_{\mathrm{fo}}:X\in\mathbf d\}.
\]

Then the possible cardinalities of \(F(\mathbf d)\) are exactly
\[
\boxed{\{1,3,\aleph_0\}}.
\]

More precisely:

\[
|F([\varnothing]_m)|=1,
\qquad
|F([\mathbb N]_m)|=1.
\]

The unique nontrivial recursive many-one degree has
\[
|F(\mathbf d_{\mathrm{rec}})|=3.
\]

Every nonrecursive many-one degree \(\mathbf d\) satisfies exactly one of
\[
|F(\mathbf d)|=1
\]
or
\[
|F(\mathbf d)|=\aleph_0.
\]

Consequently no many-one degree contains exactly two finite-one degrees, and no many-one degree contains exactly
\[
n
\]
finite-one degrees for any finite
\[
n\ge4.
\]

The cardinality \(3\) occurs only for the nontrivial recursive many-one degree.

## Assumptions and scope

A many-one reduction is a total computable function \(f\) satisfying
\[
x\in A\Longleftrightarrow f(x)\in B.
\]

A finite-one reduction is a many-one reduction whose fibres are finite.

The notation
\[
[A]_m
\]
and
\[
[A]_{\mathrm{fo}}
\]
denotes the induced many-one and finite-one degrees.

There are three recursive many-one degrees: the degree of \(\varnothing\), the degree of \(\mathbb N\), and the common degree of all recursive sets that are nonempty and have nonempty complement.

The statement concerns the **number** of finite-one degrees inside a many-one degree. It does not classify the full internal order structure in the countably infinite case.

## Proof

We separate recursive and nonrecursive many-one degrees.

### Recursive degrees

The many-one degree of \(\varnothing\) contains only \(\varnothing\), because
\[
A\le_m\varnothing
\]
implies \(A=\varnothing\). Hence it contains exactly one finite-one degree.

Similarly, the many-one degree of \(\mathbb N\) contains only \(\mathbb N\), and therefore exactly one finite-one degree.

Every recursive set \(A\) with
\[
A\ne\varnothing
\quad\text{and}\quad
A\ne\mathbb N
\]
belongs to one common many-one degree. Indeed, if \(A\) and \(B\) are both nontrivial recursive sets, choose fixed witnesses
\[
b_1\in B,
\qquad
b_0\notin B,
\]
and define
\[
f(x)=
\begin{cases}
b_1,&x\in A,\\
b_0,&x\notin A.
\end{cases}
\]
Since \(A\) is recursive, \(f\) is total computable and reduces \(A\) to \(B\). Symmetry gives many-one equivalence.

Richter, Stephan, and Zhang prove that this greatest nontrivial recursive many-one degree contains exactly three finite-one degrees: the degree of the finite nonempty sets, the degree of the cofinite sets with nonempty complement, and the degree containing all other recursive sets.

Thus the finite cardinalities realized by recursive many-one degrees are exactly
\[
1
\quad\text{and}\quad
3.
\]

### Nonrecursive degrees

Cintioli proves that every nonrecursive many-one degree contains either exactly one or infinitely many finite-one degrees.

Richter, Stephan, and Zhang prove that every many-one degree contains at most countably many finite-one degrees.

Therefore the infinite alternative in Cintioli's dichotomy is necessarily
\[
\aleph_0.
\]

So every nonrecursive many-one degree satisfies
\[
|F(\mathbf d)|\in\{1,\aleph_0\}.
\]

Combining the recursive and nonrecursive cases gives
\[
|F(\mathbf d)|\in\{1,3,\aleph_0\}
\]
for every many-one degree \(\mathbf d\).

All three values occur. The value \(1\) occurs already in the two trivial recursive degrees. The value \(3\) occurs in the nontrivial recursive degree. Countably infinite examples occur among nonrecursive nonirreducible degrees covered by Cintioli's theorem and the earlier constructions cited there.

Finally, Cintioli excludes every finite cardinality greater than one in the nonrecursive case, while the recursive case realizes only \(1\) and \(3\). Hence \(3\) is the unique finite cardinality greater than one, and it occurs only in the nontrivial recursive degree.

## Verification

The two source ingredients were checked in their primary full texts.

Cintioli's Corollary 7 states:
every nonrecursive many-one degree contains either exactly one or infinitely many finite-one degrees. Its proof explicitly rules out
\[
1<|F(\mathbf d)|<\aleph_0
\]
for every nonrecursive many-one degree.

Richter, Stephan, and Zhang state in their conclusion that every many-one degree contains at least one and at most countably many finite-one degrees. The same conclusion states that the greatest recursive many-one degree contains exactly three finite-one degrees, namely the finite nonempty, cofinite nonuniversal, and remaining recursive classes.

The two trivial recursive many-one degrees are checked directly: each contains only its unique representative set.

The classification therefore follows by an exhaustive partition into recursive and nonrecursive many-one degrees.

## Relationship to prior work

Richter, Stephan, and Zhang explicitly left open whether a nonrecursive many-one degree could contain finitely many, but more than one, finite-one degrees. Their conclusion records the recursive exception with exactly three finite-one degrees and asks whether other finite cardinalities occur.

Cintioli answered that open question negatively for every nonrecursive many-one degree: only one or infinitely many finite-one degrees are possible there.

Putting the two 2026 results together closes the cardinality-spectrum question globally:
\[
1,\quad 3,\quad \aleph_0
\]
are the only possibilities.

Targeted searches for the global spectrum, for a many-one degree with exactly two finite-one degrees, and for finite cardinalities other than three did not locate a separate published formulation of this complete spectrum.

## Limitations

This theorem determines only cardinalities. It does not classify the possible partial orders \(F(\mathbf d)\) when they are countably infinite.

It does not answer whether every nonrecursive many-one degree has a least finite-one degree, nor the finer interpolation questions raised by Cintioli.

The proof is a synthesis of two recent structural theorems plus the elementary classification of recursive many-one degrees; no new priority construction is claimed.

## References

[1] Patrizio Cintioli, “Every Nonrecursive Many-One Degree Contains Either One or Infinitely Many Finite-One Degrees,” arXiv:2609.00419, first posted 31 August 2026.

[2] Linus Richter, Frank Stephan, and Xiaoyan Zhang, “Chains and Antichains inside Many-One Degrees and Variants,” arXiv:2607.06218, first posted 7 July 2026.
