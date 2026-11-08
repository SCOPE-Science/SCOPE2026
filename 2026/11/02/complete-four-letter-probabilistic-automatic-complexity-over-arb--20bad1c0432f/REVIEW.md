# Independent mathematical audit

## correctness

PASS

For q>=2 unique strict length-four maximum under two-state row-stochastic probabilistic automata exists for each of 13 nonconstant nonexceptional restricted-growth patterns. Independently evaluated all exact rational two-state certificates in CERTIFICATES.json using BigInt denominator-cleared recurrence and all s^4 active-letter competitors for each s<=4; all 13 claimed exact gaps matched, including 0123 margin 35/4096. Constant word has a trivial two-state accepting witness, and one state cannot distinguish words. Gill's binary lower bound for 0100=abaa survives restriction to the two used letters; Kjos-Hanssen's general three-state bound supplies the upper bound. For unused letters take an average of active matrices: any word containing one expands as a strictly suboptimal convex combination, since every active replacement differs from the original target at that position. Exactly q(q-1) exceptional words follow.

## originality

PASS

Gill already classifies binary length-four A_P, including the exceptional 0100 pattern, and gives a mixture extension of binary witnesses to larger alphabets; those binary cases are explicitly credited. For genuinely three- and four-symbol equality patterns, no two-state witnesses are supplied by the inspected binary theorem. Kjos-Hanssen proves the universal three-state upper bound, not this exact arbitrary-alphabet four-letter two-state classification. New explicit rational witnesses and count are not directly implied by those published statements.

## value

PASS

The complete length-four classification is the first short-word threshold beyond the known binary-only cases for a natural probabilistic automaton complexity. The nonbinary 0123 witness and convex closure show precisely which equality patterns need a third state, rather than just exhibiting isolated examples; q(q-1) provides the exact alphabet-size dependence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
