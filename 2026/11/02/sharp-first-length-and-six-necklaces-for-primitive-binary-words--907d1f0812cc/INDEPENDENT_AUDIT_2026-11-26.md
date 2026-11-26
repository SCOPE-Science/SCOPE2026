# Independent mathematical audit

## correctness

PASS

Independent exhaustive replay visits all 131,070 strings at lengths 1–16, tests primitivity and every cyclic conjugate using exact binary prefix/suffix counts, and finds no qualifiers through 15 and 96 at 16. Each qualifying word has eight ones; the six least rotations and the full shortest-border vectors match RESULT.md. The six canonical-root lengths in the stated order are 8,8,8,6,8,4. Primitivity gives orbit size 16; explicit dihedral/complement comparison gives three pairs of necklaces. The two bundled implementations corroborate the count, but do not explicitly check the reversal/complement classification. The independent replay does. Taking complements of the compared factors inside the whole word proves that border lengths k and n-k are equivalent; in particular the frozen half-length cutoff is exhaustive. Nothing about larger lengths follows from this run.

## originality

PASS

Credit prior existence at length 16. The supported distinct claim is the exact lower cutoff for primitive binary words together with the census and symmetry classification of all first examples. Best-of-knowledge conclusion from the checked primary and indexed claims, not a guarantee of priority.

## value

PASS

The natural question is where the primitive-word obstruction for ordinary borders first fails when equality is replaced by Abelian equivalence. A prior witness alone does not identify that boundary. A complete list of the first counterexamples supplies all minimal tests for structural conjectures about the circular property, not merely further examples or an arbitrary finite count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
