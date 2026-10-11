# Scientific review

## Correctness — PASS
The two-phase conjugacy is explicit, and the three-block lift is determined by its two initial symbols. The return-word induction computes both long return increments; the counts of ones and the determinant are checked by direct recurrences. Smith normal form gives the exact return-subgroup index. Crucially, the proof does not equate an arbitrary return subgroup with a minimal component without argument: almost periodicity supplies finitely many clopen components, whose fibre-translation stabilizer is shown to coincide with the stabilized return subgroup. This closes the finite-to-infinite step. The attached finite checker corroborates the return words and modular indices but is not treated as a proof of the theorem.

## Originality — PASS, with residual risk
The closest direct comparison is Kang–Jäger, arXiv:2609.01140v1, Theorem 1.7 and Proposition 4.10 (minimal if and only if the three-block modulus is odd), and Lemma 4.11 (each minimal component has a well-defined fibre rank). Their results do not specify the exact number of components or their common rank when the modulus is even. Hedlund's decomposition and the known return-word combinatorics do not separately imply the stated arithmetic index without the stabilizer identification and integral Smith computation. Older literature on finite odometer extensions or period-doubling cocycles could contain equivalent terminology; the record does not claim absolute priority. The relevant primary preprint was read through its statements and proofs, including the decomposition section.

## Value — PASS
Nonminimality alone leaves open the exact decomposition of a natural parametrized family of finite-to-one dynamical extensions. The result computes two intrinsic discrete invariants for every modulus, showing that the odd factor has no effect on the number of components while the two-primary factor controls all splitting. It makes the general rank concept concrete across an unbounded family and supplies an exact arithmetic mechanism, rather than an isolated numerical example.

## Scope and limitations
The formula applies to the period-doubling substitution and the length-three difference code only. The theorem does not classify measure spectra or other block lengths. The checker is finite; the analytic induction and stabilizer proof carry the infinite conclusion. Independent audit has not been conducted.

Same-model review: passed. Independent audit: not yet performed.
