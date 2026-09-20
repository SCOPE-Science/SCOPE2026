# Review: exact maximum length-five non-overlapping codes

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof starts from the exact SQN(q,n) formulation established by Stanovnik, Moškon and Mraz and specializes it to n=5. After the symmetry x<->y, the remaining objective becomes affine in x4 and then affine in x3; both variables can therefore be optimized at endpoints. The two resulting branches reduce to explicit quadratics in x2. The concave branch has a closed-form vertex, and the normalized inequality against 81 q^5/1024 factors as (3-t) times a polynomial that is positive for t>=1. The other branch is monotone and has the stricter bound 216 q^5/3125.

The comparison with the Blackburn k=4 construction is exact. A residue-class check modulo 4 supplies a construction of size at least 81 q^5/1024 for every q>=4 except q=7; q=7 is treated directly. Equality conditions force x2=x3=x4=0 for q>=4, yielding precisely the I^4J pattern. The q=2 and q=3 cases are solved separately from the same integer program.

The enumeration formula uses Proposition 11 of the 2024 paper, which applies because n=5 is odd. For q>=4, equality leaves only the two orientations of the unique maximizing first-level alphabet split. For q=3 the single nontrivial choice at level 2 gives the factor 2, and q=2 has four optimal higher-level size patterns for each of the two first-level singleton partitions.

The compact verification artifact independently enumerates SQN(q,5) for q=2,...,12. It reproduces S(2,5),...,S(6,5)=(2,17,81,256,625), confirms the Blackburn size pattern for every normalized optimizer with q=4,...,12, and directly verifies all overlaps in an explicit ternary 17-word code. A full optimizer enumeration for q=2,...,7 combined with Proposition 11 reproduces N(2,5),...,N(6,5)=(8,12,8,10,12) and gives N(7,5)=14.

## Originality

**PASS, to the best of our knowledge.** Blackburn (2015) gives exact formulas through length three and a general large-alphabet conjecture. Stanovnik, Moškon and Mraz (2024) prove the exact length-four formula, formulate SQN, and explicitly state that they do not have a simple formula for larger codeword length; for n=5 they report computed values only for small q. Their Table 1 gives exactly the q=2,...,6 values recovered by this theorem.

Searches used the equivalent terminology non-overlapping code, cross-bifix-free code, mutually uncorrelated code, and strong comma-free code, together with S(q,5), length five, five-letter, and Blackburn Construction 4. Later checked literature includes work on variable-length non-overlapping codes, polarity/run-length constrained codes, and restricted overlap intervals. No checked source states the unrestricted all-q formulas proved here for S(q,5) and N(q,5).

The closest later sources are scientifically adjacent rather than covering: the 2025 constrained-code papers impose balance/run-length or restricted-overlap conditions, and the 2026 Q-Ary (t1,t2)-Overlap-Free Codes paper studies generalized restricted overlaps, construction sizes and non-expandability rather than the unrestricted maximum S(q,5). Its full text was inspected and does not state the all-q maximum or enumeration proved here.

A 2019 paper on ternary cross-bifix-free codes has an abstract sentence saying its constructions “achieved the maximum,” but the body and conclusion distinguish maximality from maximum cardinality: they prove non-expandability for arbitrary length and optimality only at length three, describing longer lengths as near-optimal and leaving maximum-cardinality questions for future work. In particular its odd-length construction has cardinality C(2m+1,m), so at length five it has 10 words, not the known optimum 17. It therefore does not cover the theorem here.

## Value

**PASS.** Length five is the first length for which the 2024 paper reports that Blackburn's k=n-1 construction can fail (at q=3), and it is the first length beyond their exact length-four theorem. The result replaces finite computational tables with a complete all-alphabet formula, identifies the sole small-alphabet obstruction, proves Blackburn's proposed pattern for every q>=4 at n=5, and also counts all maximum codes.

## Limitations

- Originality is a best-effort literature claim, not an exhaustive database guarantee.
- The proof relies on the exact SQN characterization of maximum non-overlapping codes from the 2024 paper.
- The theorem is specific to n=5; it does not establish a comparable formula for n>=6.
- The verification artifact checks finite parameter ranges and an explicit construction; the general theorem rests on the symbolic proof above, not on computation.
