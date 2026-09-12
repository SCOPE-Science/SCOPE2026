# Triple Milnor–Rédei vanishing over Q(ζ₈) at (p₂, p₃, q): μ₂(123) = 0

## Context

This record resolves the admitted TARGET claim on the mod-2 arithmetic triple
Milnor invariant over the 8th cyclotomic field. Arithmetic topology (Morishita
and successors) interprets the pairwise mod-2 linking numbers of primes as cup
products in étale cohomology and the triple invariant as a triple Massey
product evaluated against the Artin–Verdier trace, equivalently as the
decomposition (Rédei splitting) law of the third prime in an associated
Rédei-type dihedral extension of degree 8. The target fixes one explicit
triple satisfying the pairwise-vanishing hypothesis and asks for a proof or
disproof of the vanishing of the triple invariant.

## Definitions and objects

- K = Q(ζ₈) = Q(t)/(t⁴+1), ζ = t mod (t⁴+1), O_K = Z[ζ], class number 1.
- p₂ = unique prime above 2, uniformizer π₂ = 1+ζ, N(π₂) = 2.
- p₃ = prime above 3 with uniformizer π₃ = −1−ζ²−ζ³, N(π₃) = 9.
- q = prime above 17 with uniformizer π_q = 2−ζ³, N(π_q) = 17.
- S = {p₂, p₃, q}, U = Spec O_K ∖ S.
- c₁, c₂, c₃ ∈ H¹(U, Z/2): Kummer meridian classes of π₂, π₃, π_q.
- Pairwise linking numbers: cup products cᵢ ∪ cⱼ, detected by Hilbert symbols.
- Triple invariant μ₂(123) = ⟨c₁, c₂, c₃⟩ (triple Massey product in H²(U, Z/2))
  modulo indeterminacy c₁ ∪ H¹(U, Z/2) + H¹(U, Z/2) ∪ c₃, evaluated against
  the Artin–Verdier trace H²(U, Z/2) → Z/2.
- Rédei extension M/K: dihedral-type degree-8 extension built from a defining
  system (norm solution) for the Massey product; μ₂(123) = 0 iff q splits
  completely in M.

## Result (headline claim)

For the explicit triple above, all three pairwise mod-2 arithmetic linking
numbers vanish, the triple Massey product ⟨c₁, c₂, c₃⟩ is defined, and its
Artin–Verdier trace value μ₂(123) equals 0 modulo indeterminacy. Equivalently,
the Rédei-type dihedral degree-8 extension
M = K(√(1+ζ), √α) with α = a + b√(1+ζ),
a = −(1+ζ+ζ²), b = −(1+ζ−ζ³),
ramified only inside {p₂, p₃}, has q splitting completely: both K₁-primes
above q split into two unramified primes in M/K₁ ([2,2], all e = f = 1),
where K₁ = K(√π₂).

## Proof and evidence

1. Pairwise vanishing. K is totally complex, so only finite places matter.
The Hilbert symbols (πᵢ, πⱼ)_v were computed with PARI `nfhilbert` at all
relevant finite residue places (above 2, 3, 5, 17); all three grids are
identically +1, so cᵢ ∪ cⱼ = 0 and the Massey product is defined. A scan of
neighboring prime choices shows −1 entries, distinguishing this triple as the
one satisfying the hypothesis.

2. Explicit defining system. With s² = 1+ζ (K₁ = K(s)) and
z = ζ³+ζ²−1 (a unit, N_{K/Q}(z) = 1), the exact identity
a² − (1+ζ)b² = π₃·z² holds in Z[ζ]; in coordinates N/π₃ = −2ζ³−3ζ²−2ζ = z².
This was machine-checked and independently re-verified by exact integer
arithmetic in Z[t]/(t⁴+1). Hence α = a + bs satisfies N_{K₁/K}(α) = π₃z².
In absolute coordinates (t = y²−1), A(y) = y⁷−3y⁵−y⁴+2y³+y²−y−1 has
N_{K₁/Q}(A) = 9 and x²−A is irreducible over K₁, so [M:K₁] = 2, [M:K] = 8
with the standard Rédei dihedral closure configuration.

3. Ramification control. The discriminant of M is supported only above 2
(totally ramified tower, allowed) and one norm-9 prime above p₃; α has
valuation 0 at every prime above 17, so M/K is unramified at q and ramified
only inside {p₂, p₃} ⊂ {p₂, p₃, q}.

4. Splitting law. Both K₁-primes above q split into 2 unramified primes in
M ([2,2], e = f = 1), so the Frobenius of q in M/K is trivial and
μ₂(123) = 0 mod indeterminacy. A second independent defining system gives
the same [2,2] splitting, confirming independence of the defining-system
choice. An independent mod-17 residue-field check corroborates this: with
q at t = 8 mod 17 and K₁ lifts at y = 3, 14, A(y) = 8, 16 are both nonzero
quadratic residues mod 17.

## Limitations

Scope is the fixed explicit triple with F₂ coefficients only; no claim is
made about other prime choices (most fail the pairwise hypothesis) or other
coefficients. The dihedral Galois-closure identification uses the standard
Rédei norm-relation lemma rather than an explicit `polgalois` computation.
PARI `idealprimedec` ordering labels are version-dependent; mathematical
identity is pinned by the explicit uniformizers. Class-number,
irreducibility, Hilbert-symbol, and decomposition computations are
reproducible PARI calculations archived with the record.

## Reproducibility

Artifacts `verify_all.py` (consolidated PARI/cypari script) and `results.txt`
(log: class numbers 1, three all-+1 Hilbert rows, norm quotient square,
alpha nonsquare, [2,2] e = f = 1 splitting, second-system agreement)
reproduce the computational steps. The norm identity can be checked by hand
expansion in Z[ζ]. PARI version used: 2.15.4 via cypari.

## References

- M. Morishita, Milnor invariants and Massey products for prime numbers,
  Compositio Math. 140 (2003).
- F. Amano, Y. Mizusawa, M. Morishita, On mod 3 triple Milnor invariants and
  triple cubic residue symbols in the Eisenstein number field, Res. Number
  Theory 4 (2018), arXiv:1412.6894.
- J. Mináč, N. D. Tân, Triple Massey products over global fields (2015).
- M. J. Hopkins, K. Wickelgren, Splitting varieties for triple Massey
  products.
- The LMFDB (lmfdb.org) number-field databases: consulted; no overlapping
  record found.
