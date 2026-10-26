# Review of a Galois-twist rank law for random generation of square-zero local algebras

## Correctness — PASS

The algebra admits a coefficient-field section because its field residue is separable. The radical is a module for a product of Galois-indexed fields. The proof calculates the radical part of the generated algebra by a two-sided inclusion: crossed derivations yield the necessary linear spans, and a graph subalgebra realizes the converse. Conditional on field-generating residues, a change of variables produces independent uniform matrices with \(r\) rows for the identity twist and \(r-1\) for each nonidentity twist. Finite-field rank enumeration and divisor-lattice inversion give the stated joint law and full-generation probability. The code exhaustively checks small examples but is not an infinite proof.

## Originality — PASS against inspected sources

Sercombe--Shalev (arXiv:2009.01115, publicly posted 2020-09-02) study random generation and classify maximal-subalgebra types, without stating this complete isotypic rank distribution. Iovanov--Sistko (arXiv:1705.00762) supply the general maximal-subalgebra background. Kravchenko--Mazur--Petrenko (J. Algebra 426 (2015)) give a general counting/lifting framework, but no identical specialized product law was identified in the accessible text. The latter article could not be examined fully, and earlier equivalent formulations in crossed-derivation or bimodule terminology remain possible. No exhaustive priority claim is made.

## Value — PASS

The result settles a complete natural conditional random-subalgebra profile for all square-zero local finite-field associative algebras with a field residue. The difference between \(r\) and \(r-1\) effective random rows is a structural feature of noncommutative Galois twists, and its multiplicative independence yields both explicit random-generation probabilities and exact minimal positive generator thresholds. This is more informative than a single finite table, while not claiming a theorem about nonsquare-zero or semisimple-product quotients.

## Scientific limitations

The dimension/profile law is conditional on full generation of the residue field. The formula does not classify subalgebras generated with residues in proper subfields. The proof requires \(J^2=0\) and a single separable field residue. Computational checks use small characteristic-two instances. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
