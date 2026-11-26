# Independent mathematical audit

## correctness

PASS

An appended absent symbol cannot give a square, so every crucial word uses all five letters. First-appearance relabeling gives exactly one canonical representative and each complete-alphabet orbit has size 5!. A new forbidden factor can only end at the appended position, so a breadth-first canonical prefix census pruned by the suffix test is exhaustive. In /tmp/opencode/crucial_review.py I encoded Parikh vectors by base-8 positional weights; every tested half-length is ≤7, so a difference with signed digits in [−7,7] can vanish only when all digits vanish, by taking the lowest nonzero digit modulo 8. Before appending any letter, each candidate suffix length computes a deficit; a square is forced by a letter exactly when that deficit is its unit vector. The replay checked every depth 1–13, found no shorter full-alphabet crucial word, and gave 297588 canonical prefixes overall, 209190 at depth 13, of which 205424 use all five letters. It found precisely 14 crucial words and compared all 70 singleton witnesses against the frozen CSV. Sorted spectra match the four claimed frequencies 8,3,2,1 and 14·120=1680. Evdokimov–Kitaev Theorem 5 independently supplies the minimum length 13. The frozen C++ program already filters out multiple-witness candidates by design; the witness uniqueness here instead follows after independently retaining every word with all five nonempty witness sets. No frozen script was executed.

## originality

PASS

The length formula and existence of a minimizer are old. The comparison supports a distinct full census of five-letter minimizers and the classification by unique right-extension obstructions; none of the inspected constructions or adjacent exact tables gives these data.

## value

PASS

Classifying all minimizers at the sharp length of a classical obstruction problem is a motivated extremal census. Beyond giving the number of orbits, it isolates an exact structural fact: each of the five possible continuations of every minimizer is blocked at a unique length, and the permitted joint spectra fall into four explicitly counted families. This information is useful for comparing extremal constructions and is not implied by knowing the minimum length. No generalization to larger alphabets or to bicrucial words is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
