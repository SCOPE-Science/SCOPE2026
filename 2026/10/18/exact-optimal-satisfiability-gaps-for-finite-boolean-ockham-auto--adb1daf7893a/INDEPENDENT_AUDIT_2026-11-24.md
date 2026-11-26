# Independent mathematical audit

## correctness

PASS

Independently checked the atom-coordinate argument in RESULT.md, lines 22–52. Composing the dual automorphism with complement gives a Boolean automorphism, hence an atom permutation. The membership vector at a position is uniform on q symbols, independently across atoms. Each unary application complements and advances one position, so depth d requires at most the first D=d+1 positions. For d>0 the initial symbols of successive states of a rooted closed walk reconstruct the unique indexed cyclic word (the overlap forces the rest of each state, including when the period is shorter than d); for d=0 the scalar gives |F_E|^ell. Independence across cycles gives the product. Any forbidden D-block occurs on the D-cycle with positive probability. One failing assignment can be forced by fixing at most D distinct atoms, giving the universal lower bound on a nonzero gap. For ell>=D the floor(ell/D) linear disjoint windows on a cycle are independent; avoiding even one forbidden block in all these windows gives the stated decay bound. An acyclic transfer graph gives degree zero on every nonempty atom set. Otherwise repeating a directed cycle produces a positive nonunit witness b at a length L>=D; the decay bound with (1-q^-D)^K<b forces L<DK and puts every length >=DK below b. The remaining rational maximum is exact, and no product with a nonunit factor can beat that single-cycle maximum. For even a, the fixed assignments are constant on gcd(ell,a) orbits. A prime with v_p(ell)>v_p(a) forces ell-gcd(ell,a)>=p^v_p(a)(p-1); ell=p^(v_p(a)+1) realizes equality for each prime. This gives the stated minimum and both examples. The finite checker was inspected, not run; the symbolic argument supplies all unbounded quantifiers. The introductory ‘nonunit exponents’ wording is imprecise: the exponents with finite support are the nonzero m_ell, as used throughout the proof.

## originality

PASS

Credit existing direct-product multiplicativity and the standard finite-memory symbolic-dynamics construction. The inspected statements do not cover the Ockham-specific equation test and attained optimal gap with the even-power valuation formula. The closest same-day atom-cycle result treats quantifier-free types up to necklace support, not counts of uniformly distributed assignments to a given equation. This is a bounded statement-level comparison, not a priority finding.

## value

PASS

The sharp gap across all finite atom permutations measures how close a genuinely nonvalid equation can come to validity. The elementary uniform bound alone does not decide that optimum, whereas the explicit terminating cutoff both computes it and exhibits a model attaining it. The even-power laws give an arithmetic optimizer and show that the crude uniform estimate can severely understate the gap. The result concerns a natural Boolean subclass and promises no efficient implementation or extension to general Ockham algebras.

The dated certificate retains the supplied scientific assessment, sources and limitations.
