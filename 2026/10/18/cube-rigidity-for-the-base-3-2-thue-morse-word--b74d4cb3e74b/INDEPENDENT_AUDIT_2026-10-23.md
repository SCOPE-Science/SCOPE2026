# Independent mathematical audit

## correctness

PASS

The recurrence groups aligned triples as (a_m,1-a_m,a_m), a_m=x_{2m}; adjacent equalities in x can start only at indices 2 mod 3. Every four successive a_m include adjacent equal a-values because one of their even-index pairs equals x_(3j),x_(3j+2). An alternating x factor of length ten would cross three consecutive aligned triple boundaries, forcing four alternating a-values, a contradiction; maximum alternation length at most nine. In a period-p length-3p cube with 3 not dividing p, any equal neighboring letters recur at two or three pair starts with distinct residues mod3, impossible. The cube must therefore be alternating, requiring even p and 3p<=9, hence p=2, words 010101 or 101010. If L>=3p and p coprime to3, the alternating period-2 prefix propagates and L<=9; otherwise exponent below 3. Recurrence directly gives x12..20=101010101, attaining sharp 9/2. No assumption on periods divisible by three.

## originality

PASS

The aligned length-three recurrence is due to Dekking and not novel; Dekking documents the conjecture that unrestricted critical exponent is five. The current proof adds a local equality-residue obstruction and exact 9/2 restricted exponent not found in the inspected original sequence papers or the later frequency-analysis work. Resultary semantic search did not identify a same-word repetition classification. A semantically equivalent earlier specialized word-combinatorics result remains possible.

## value

PASS

Determines an exact sharp restricted critical exponent and a universal factor classification for a well-studied nonuniform-base digit-parity word. This gives a natural separable obstruction within the unresolved unrestricted power problem, not a trivial finite sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
