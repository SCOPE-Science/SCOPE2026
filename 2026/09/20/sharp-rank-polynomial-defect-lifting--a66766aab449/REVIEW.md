# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked at the three points where hidden hypotheses are most likely.

First, \(M=\operatorname{Ran}p(T)\) is \(T\)-invariant because \(T\) commutes
with \(p(T)\). In the finite-rank case \(M\) is finite-dimensional and therefore
closed and complemented. The restriction \(A=T|_M\) is a genuine
finite-dimensional operator. If \(q(A)=0\), then \(q(T)p(T)=0\), so the
degree bound \(\deg m_T\le d+r\) follows without any spectral or
complementability assumption beyond finite dimensionality of \(M\).

Second, for a bounded decomposition \(X=M\oplus Y\), \(T\) has upper-triangular
block form. Since \(p(T)\) maps all of \(X\) into \(M\), its lower-right block
vanishes; polynomial block calculus identifies that block with \(p(D)\).
Replacing the \(M\)-block by a scalar root of \(p\) and deleting the off-diagonal
block therefore produces a \(p\)-algebraic operator. The correction has range
inside \(M\), so no unjustified inheritance or complementability claim is used.

Third, for any competing correction \(F=T-S\) with \(p(S)=0\), the identity
\(T^n-S^n=\sum_{j=0}^{n-1}T^{n-1-j}FS^j\) is valid without commutativity.
Grouping the polynomial difference into exactly \(d\) rank-at-most-\(\operatorname{rank}F\)
terms gives \(\operatorname{rank}p(T)\le d\operatorname{rank}F\).
The two sharpness examples were checked directly: a nilpotent Jordan block of
size \(d+r\) attains the degree bound; scalar blocks attain the upper rank-distance
bound; cyclic completion of \(d\times d\) nilpotent shifts attains the lower
factor \(1/d\).

## Originality

Originality is asserted only **to the best of our knowledge**. Barnes (1985)
was inspected in full at the relevant theorem and Corollary 11. It proves that
finite-dimensional range of \(p(T)\) implies existence of a finite-rank
\(J\) with \(p(T-J)=0\), but the stated result does not give
\(\operatorname{Ran}J\subseteq\operatorname{Ran}p(T)\), the bound
\(\operatorname{rank}J\le\operatorname{rank}p(T)\), the sharp
minimal-polynomial degree bound, or the two-sided rank-distance estimate.

Álvarez (2014) was inspected through its definition and main theorem on
polynomially finite-rank linear relations. Its focus is Fredholm,
ascent/descent, and Riesz--Schauder structure; the inspected text does not state
the quantitative claims above. Searches using exact and synonymous formulations
for polynomially finite-rank operators, rank distance to \(p(S)=0\), complemented
defect range, and minimal-polynomial degree did not locate an exact prior
statement. Kramar (2012) is relevant because its abstract states that a
finite-rank perturbation of an algebraic operator is algebraic, but the full text
was not available in the inspected source. This is the principal unresolved
bibliographic risk.

## Value

The result converts a qualitative finite-rank lifting theorem into a sharp
quantitative structure statement. The defect itself supplies a canonical
finite-dimensional invariant space that simultaneously controls the degree of
algebraicity and the size and location of a correcting perturbation. The lower
rank-distance estimate shows that the upper correction bound is not merely an
artifact of the construction, while the extremal examples identify the exact
universal constants. The complemented-range version isolates a reusable block
mechanism beyond the finite-rank case.

## Limitations

The result concerns bounded operators on complex Banach spaces. The sharp
\(1/d\) lower constant is universal over degree-\(d\) polynomials; it is not
asserted to be optimal for every fixed polynomial. The full text of Kramar
(2012) was not inspected, and very old or poorly indexed equivalent statements
may have been missed.
