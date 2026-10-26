# The complete amorphic-complexity spectrum of primitive ternary length-two substitutions

## Finding

Among all substitutions \(\varphi:\{0,1,2\}\to\{0,1,2\}^{2}\), exactly \(288\) are primitive. The associated two-sided minimal subshifts have **exactly eight possible amorphic-complexity values**, with the following exact numbers of *labeled substitutions* (not conjugacy classes):

| Amorphic complexity of the subshift | Number of primitive substitutions |
| :--- | ---: |
| \(0\) (finite periodic system) | 18 |
| \(1\) | 96 |
| \(2\) | 12 |
| \(\log 2/\log(2/\alpha)\), where \(\alpha\) is the positive root of \(x^3-x-2\) | 24 |
| \(\log 2/\log(2/\phi)\), where \(\phi=(1+\sqrt5)/2\) | 48 |
| \(\log 2/\log(2/\beta)\), where \(\beta\) is the positive root of \(x^3-x^2-2\) | 24 |
| \(\log 2/\log(2/\tau)\), where \(\tau\) is the positive root of \(x^3-x^2-x-1\) | 24 |
| \(+\infty\) | 42 |

In particular, **no such primitive system has amorphic complexity strictly between \(1\) and \(2\)**, and the gap is sharp since precisely \(12\) labeled substitutions have complexity \(2\). Among all \(288\), exactly \(114\) are tame and null (the \(18\) periodic plus the \(96\) of complexity one), and exactly \(174\) are neither tame nor null.

## Assumptions and scope

A substitution is a rule assigning to each of the three symbols a word of length two. It is primitive when some fixed positive substitution power of every symbol contains all three symbols. Labeled substitutions are distinguished as literal rules, even if relabeling the alphabet or topological conjugacy identifies their subshifts. The subshift includes every bi-infinite sequence all of whose finite factors occur in some substituted word. Amorphic complexity is the topological invariant defined through asymptotically separated orbit pairs in Gröger--Krawczyk. No conjugacy-class census is asserted.

## Proof

**1. Exact finite search domain and primitivity.** There are \(3^6=729\) rules. For each, form the \(3\)-by-\(3\) incidence matrix \(M\), whose entry \(M_{ij}\) counts occurrences of \(i\) in \(\varphi(j)\). Primitivity is equivalent to \(M^5\) being strictly positive: a primitive nonnegative \(3\)-by-\(3\) matrix has exponent at most \((3-1)^2+1=5\) (Wielandt's exponent bound), and positivity of a power is the definition. The included independent-integer enumeration tests all \(729\) possibilities and finds precisely \(288\) primitive rules.

**2. Pair-discrepancy matrices.** Index unordered distinct-symbol pairs in the order \((01,02,12)\). Associate to a primitive rule its \(3\)-by-\(3\) integer matrix \(D\) whose column corresponding to pair \(\{a,b\}\) counts, for each site of the two images, the resulting unequal output pair \(\{\varphi(a)_i,\varphi(b)_i\}\). Matched output symbols contribute nothing. For a height-one substitution, Theorem B of Gröger--Krawczyk identifies the discrepancy spectral radius \(\lambda=\rho(D)\) and gives

\[\operatorname{ac}(X_\varphi)=\frac{\log 2}{\log 2-\log\lambda},\]

with the standard endpoint conventions \(\lambda=0\mapsto0\) and \(\lambda=2\mapsto+\infty\). Their Theorem A identifies tame and null primitive systems as precisely those of amorphic complexity \(0\) or \(1\).

**3. The complete exact characteristic-polynomial census.** The following list is the entirety of the computed distribution among the \(288\) primitive rules. Each row is the monic polynomial \(\det(xI-D)\) and its number of rules. The last column gives its Perron root, not necessarily the true discrepancy rate if the substitution has height greater than one.

| \(\det(xI-D)\) | Count | Perron root |
| :--- | ---: | :--- |
| \(x^3\) | 12 | \(0\) |
| \(x^3-1\) | 12 | \(1\) |
| \(x^3-x^2\) | 36 | \(1\) |
| \(x^3-x\) | 18 | \(1\) |
| \(x^3-2x^2+x\) | 30 | \(1\) |
| \(x^3-x^2-2x+2\) | 12 | \(\sqrt2\) |
| \(x^3-x-2\) | 24 | \(\alpha\) |
| \(x^3-x^2-x\) | 36 | \(\phi\) |
| \(x^3-2x^2+1\) | 12 | \(\phi\) |
| \(x^3-x^2-2\) | 24 | \(\beta\) |
| \(x^3-x^2-x-1\) | 24 | \(\tau\) |
| \(x^3-2x^2\) | 12 | \(2\) |
| \(x^3-2x^2-x+2\) | 18 | \(2\) |
| \(x^3-3x^2+3x-2\) | 4 | \(2\) |
| \(x^3-x^2-2x\) | 12 | \(2\) |
| \(x^3-3x-2\) | 2 | \(2\) |

The enumeration is a *finite proof*, with transparent integer operations only, not empirical extrapolation: `verify.py` enumerates the entire stated search domain; computes primitivity from exact incidence matrices; forms every discrepancy matrix by the defining two-site rule; evaluates every characteristic polynomial by two independent integer formulas; and asserts each displayed category count. In particular, its checked operations constitute an exhaustive certificate for all \(729\) possible rules. The root assignments follow by elementary factoring or monotonicity of the named cubics. In the \(x^3\) case, \(D^3=0\) is independently checked for each of the twelve rules.

**4. The exceptional periodic three-cycles.** For a primitive substitution on a three-letter alphabet, its height is at most three and is coprime to its constant length two (the standard height decomposition recalled by Gröger--Krawczyk). Thus the only possible heights are one and three. A height-three system with only three symbols has a distinct symbol occupying each position class modulo three and is therefore a periodic three-cycle. For any permutation \((a,b,c)\) of the alphabet, the rule fixing the bi-infinite periodic word \(\ldots abcabc\ldots\) is forced by the correspondence

\[\varphi(a)=ab,\quad\varphi(b)=ca,\quad\varphi(c)=bc.\]

There are exactly six such labeled rules; all appear in the characteristic-polynomial row \(x^3-2x^2-x+2\). Their raw pair-matrix Perron root is two, but their subshift is finite and has amorphic complexity zero. This is why one cannot apply the height-one spectral formula to that row without separating them.

For all other primitive rules, height is one. Gröger--Krawczyk Proposition 3.10 states that height-one discrepancy rate zero is equivalent to finiteness. It follows that the only other finite rules are exactly the twelve with \(D^3=0\). The remaining \(12\) rules in the exceptional characteristic-polynomial row have height one and amorphic complexity \(+\infty\). This proves the displayed eight-way classification and both dynamical-property counts.

**5. The sharp gap.** Every positive finite discrepancy rate in the height-one census is either one, \(\sqrt2\), or one of the strictly larger positive algebraic numbers \(\alpha,\phi,\beta,\tau\). Since \(\lambda\mapsto\log2/\log(2/\lambda)\) is strictly increasing for \(1\le\lambda<2\), complexity one is followed immediately by complexity two. Its count of twelve proves attainment.

## Verification

From this document's folder, run `python3 verify.py`. It uses only the Python standard library, enumerates all \(729\) rules, and checks the \(288\) primitive rules, the \(16\) characteristic-polynomial classes, the six exceptional three-cycles, and all eight spectral-class totals. There are no numerical eigenvalue approximations in the verifier; characteristic polynomials are computed by two different exact-integer methods. The mathematical link from those finite checks to infinite-time amorphic complexity is the published Theorems A and B, not a finite-orbit experiment.

## Relationship to prior work

Gröger and Krawczyk (arXiv:2602.23267v1, public February 26, 2026) prove the general discrepancy spectral formula and tame/null equivalence. The finite complete ternary length-two spectrum, exact labeled family counts, periodic-height separation, and sharp internal gap above one are the present specialized enumeration; the general theorems and the discrepancy construction are *not* new here. Fuhrmann and Gröger (2019) previously obtain exact binary formulas and bounds for higher alphabets, but do not give this ternary all-rule census. Arithmetic and spectral calculations depend on the cited prior general theorems.

## Limitations

The counts classify labeled primitive rules, not mutually nonconjugate subshifts. They do not address nonprimitive rules, larger alphabets or longer substitution images. The proof's exhaustive finite part can be independently inspected and rerun; the underlying infinite-time spectral formula is imported from a published general theorem, not reproved. Older equivalent tabulations under terminology other than amorphic complexity cannot be categorically ruled out; bibliographic priority remains subject to independent review. No independent external audit has been performed.

## References

1. Maik Gröger and Elżbieta Krawczyk, *Tameness, nullness, and amorphic complexity of automatic systems*, arXiv:2602.23267v1, publicly posted 2026-02-26. https://arxiv.org/html/2602.23267v1 (Theorems A and B; Definitions 2.15 and 3.4; Proposition 3.10).
2. Gabriel Fuhrmann and Maik Gröger, *Constant length substitutions, iterated function systems and amorphic complexity*, *Mathematische Zeitschrift* **295** (2020), 1385–1404; first published 2019-11-22. https://doi.org/10.1007/s00209-019-02426-2.
3. H. Wielandt, *Unzerlegbare, nicht negative Matrizen*, *Mathematische Zeitschrift* **52** (1950), 642–648 (primitive-matrix exponent bound).
