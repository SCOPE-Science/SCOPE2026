# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof was checked at the following structural points.

1. On a right- or left-supported slice with support rank \(d<\infty\), every operator
has rank at most \(d\). The normalized ideal norm lies between operator norm and
trace norm, while trace, Hilbert-Schmidt and operator norms are uniformly equivalent
at fixed rank. Hence each such slice is isomorphic to a Hilbert space.

2. For a fixed right vector \(v\), the restriction of a strictly singular elementary
operator to \(\{u\otimes v:u\in H\}\) is strictly singular into a finite-support
slice, hence compact. After separating the left coefficient span into compact terms
and terms independent modulo \(K(H)\), bounded evaluations \(Y\mapsto Yz\) force
all right coefficients paired with the noncompact left quotient basis to vanish.

3. After the first reduction all left coefficients are compact. Repeating the argument
on fixed-range rank-one fibers, using the conjugate Hilbert-space identification and
\(Y\mapsto Y^*z\), forces the remaining right coefficients to be compact. Adjoint
preserves linear independence modulo \(K(H)\).

4. A two-sided multiplication \(X\mapsto KXC\) with \(K,C\) compact is compact on
the ideal: operator-norm finite-rank approximations of \(K,C\), together with the
ideal inequality, approximate it in superoperator norm by finite-rank maps.

5. The stronger witness is obtained without assuming strict singularity. If a fixed
rank-one fiber restriction is noncompact, Hilbert-space theory supplies an
infinite-dimensional subspace on which it is bounded below. If all column fibers
are compact, the first coefficient reduction applies; if all row fibers were also
compact, the second reduction would make the whole operator compact. Thus every
noncompact case has one of the two rank-one witnesses. The projections
\(X\mapsto P_EXP_v\) and \(X\mapsto P_uXP_F\) are contractive by the ideal property,
so the witnesses are 1-complemented.

No complementability claim about arbitrary block subspaces is used.

## Originality

**PASS, to the best of our knowledge.**

The closest checked literature separates into several neighboring themes:

- Fialkow--Loebl (1984) treats elementary mappings into ideals of operators.
- Apostol--Fialkow (1986) studies structural properties, range inclusion, and
  compactness phenomena for elementary operators. Its searchable full text was
  checked for “strictly singular,” with no occurrence located.
- Magajna (1987) gives a Calkin-independence theorem for systems of operator
  equations and an elementary-operator application.
- Lindström--Saksman--Tylli (2005) and Mathieu--Tradacete (2020) study strict
  singularity of a single two-sided multiplication \(S\mapsto ASB\) on full
  operator algebras \(L(X)\) for classes of Banach spaces.
- Brešar--Turovskii (2007) studies compact elementary operators on Banach algebras.
- Huang--Sukochev--Yu (2026) studies general bounded maps on operator ideals and
  relative \(\mathcal C_E\)-strict singularity; the located statement is not the
  ordinary Banach-space strict singularity assertion proved here.

Exact and synonymous searches involving “strictly singular elementary operator,”
“norm ideal,” “Schatten,” “finite elementary operator,” “finitely strictly
singular,” and rank-one witnesses did not locate the stated collapse theorem.

The principal residual risk is Fialkow--Loebl (1984): its bibliographic record and
its role in later papers were inspected, but its full text was not exhaustively
checked. Older survey and compact-elementary-operator literature was also not
exhaustively inspected for a differently phrased equivalent result. Accordingly,
the novelty claim is restricted to the ordinary strict-singularity/FSS/compactness
collapse and the complemented rank-one witness, rather than every compact-coefficient
characterization appearing in the theorem.

## Value

**PASS.**

General operator ideals can support noncompact strictly singular behavior. The theorem
shows that finite elementary superoperators form a substantially more rigid class:
noncompactness is always witnessed on a complemented copy of a Hilbert space made
entirely of rank-one operators. This simultaneously rules out both strictly singular
and finitely strictly singular noncompact finite elementary operators and supplies a
quantitative uniform lower bound for all Bernstein numbers.

## Scientific limitations

- The theorem assumes a normalized Banach norm ideal contained in \(K(H)\).
- Quasi-Banach ideals are not covered.
- Only finite elementary sums are covered; no assertion is made for infinite or
  integral elementary operators.
- No corresponding assertion is made for elementary operators on \(B(X)\) for a
  general Banach space.
- The originality assessment remains subject to the older-literature risk described
  above.
