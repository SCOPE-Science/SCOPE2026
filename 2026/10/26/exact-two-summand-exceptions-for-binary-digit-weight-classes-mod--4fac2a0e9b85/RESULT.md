# Exact two-summand exceptions for binary digit-weight classes modulo three

## Finding
For \(c\in\{0,1,2\}\), put \(A_c=\{n\in\mathbb N_0:s_2(n)\equiv c\pmod3\}\), where \(s_2(n)\) counts the ones in the binary representation of \(n\). Define \(E_c=\mathbb N_0\setminus(A_c\cup(A_c+A_c))\). Then the following are **exact equalities of infinite sets**:

\[
E_0=\{2,4,5,6,8,9,10,12,16,17\}\cup\{2^j-1:j\ge1,\ j\equiv1,2\pmod3\}\cup\{3\cdot2^{3j}-1:j\ge1\},
\]
\[
E_1=\{0,13,14,21,22,26\}\cup\{2^{3j}-1:j\ge1\}\cup\{3\cdot2^{3j-1}-1:j\ge1\},
\]
\[
E_2=\{0,1,2,4\}\cup\{2^{3j}-1:j\ge1\}.
\]

These are the only exceptions to representation with **one or two** same-class summands. For \(X\ge2\), their counting functions satisfy
\[
\#(E_0\cap[0,X])=\log_2 X+O(1),\qquad
\#(E_1\cap[0,X])=\frac23\log_2 X+O(1),\qquad
\#(E_2\cap[0,X])=\frac13\log_2 X+O(1).
\]
Thus all three exceptional sets are infinite but have natural density zero.

## Assumptions and scope
All integers and both summands are nonnegative. A one-summand representation is permitted independently of the two-summand condition. When \(c=0\), zero is in \(A_0\); when \(c=1,2\), zero is not. Two summands may be equal. Binary representations use no leading zeros, with the representation of zero treated separately. Exponents \(j\) in all infinite families are positive.

## Proof
**1. Exact automaton for two summands.** Read digits of a proposed target \(n\) from least significant to most significant. A state is a triple \((\kappa,r,s)\in\{0,1\}\times(\mathbb Z/3\mathbb Z)^2\). Start in \((0,0,0)\). For each target digit \(d\in\{0,1\}\), make every transition obtained by choosing summand digits \(a,b\in\{0,1\}\) satisfying
\[
a+b+\kappa\equiv d\pmod2,
\]
and set \(\kappa'=\lfloor(a+b+\kappa)/2\rfloor\), \(r'=r+a\pmod3\), \(s'=s+b\pmod3\). The target has a representation in \(A_c+A_c\) exactly when the reachable state set contains \((0,c,c)\) after all digits. Indeed, each path is precisely ordinary binary addition, while final carry zero precludes nonzero higher summand digits. A separate running residue of target digits tests membership in \(A_c\). Hence membership in \(E_c\) is recognized by a finite automaton.

**2. Exact automata for the three asserted sets.** Over reverse binary words (least significant digit first), the positive repunit \(2^j-1\) is the word of \(j\) ones; a three-state cycle tracks \(j\pmod3\). The number \(3\cdot2^j-1\) has ordinary binary expansion `10` followed by \(j\) ones, so its reverse word is \(j\) ones followed by `01`. A finite nondeterministic automaton recognizes the indicated residues of \(j\), and a finite trie recognizes each explicitly listed exceptional integer. These automata are built directly by `reference_nfa` in the accompanying certificate.

**3. Exhaustive finite automaton equivalence.** A state of the comparison process consists of (i) the subset of the 18 possible carry-and-residue states, (ii) the residue modulo three of the target's own digit sum, and (iii) the subset of states reachable in the asserted-exception NFA. Applying each of the two possible next input digits determines the next comparison state exactly. Breadth-first search enumerates every reachable state, so this comparison is exhaustive over **all finite binary words**, not a truncation by integer size. The assertion `missing(dest)==expected(dest)` is tested whenever the last digit is 1, which is precisely when an LSD-first word is a canonical positive binary representation. Zero is separately checked on the canonical one-digit word `0`. The supplied verifier implements these elementary transitions explicitly and reaches **108, 108, and 107** paired states for \(c=0,1,2\), respectively, without a mismatch. Finite reachability proves all three asserted identities simultaneously for every nonnegative integer.

**4. Counting exceptions.** The finite lists contribute only bounded corrections. The repunits with exponents in two nonzero residue classes modulo three contribute \(\frac23\log_2 X+O(1)\), whereas exponents in one class contribute \(\frac13\log_2 X+O(1)\). Each shifted family \(3\cdot2^{3j+\delta}-1\) likewise contributes \(\frac13\log_2 X+O(1)\). The families overlap in at most finitely many numbers: shifted-family binary expansions begin `10` and thus cannot be positive repunits, and all remaining overlaps with fixed finite lists are bounded. Summing proves the stated asymptotic counts.

## Verification
Run `python3 certify_mod3_sums.py` from the directory containing the supplied certificate. It uses only Python's standard library. The finite-state equivalence output is:

```
residue 0: PASS; 108 reachable paired states; reference NFA 43 states
residue 1: PASS; 108 reachable paired states; reference NFA 30 states
residue 2: PASS; 107 reachable paired states; reference NFA 11 states
PASS: all three infinite classifications; direct check n <= 10000
```

The separate direct comparison for all \(0\le n\le10000\) tests the same exceptional formulas against literal bounded two-summand enumeration. This numerical cross-check cannot itself prove an infinite statement; the finite-state equivalence in step 3 does so, contingent on the clearly specified transition semantics and the executable exhaustive-state check.

## Relationship to prior work
Allouche and Shallit (arXiv:2112.13627, first made public 27 December 2021) study two-summand representation functions for evil and odious numbers (binary digit sum **modulo two**), and higher-summand results for those same classes. Their general automata and logic framework permits formulating the present question but the inspected paper does not contain the explicit three-class modulo-three exception classification. Shallit (arXiv:2103.10904) studies Frobenius numbers of tails of automatic sequences, including evil and odious numbers, a different question from the one-or-two-summand zero-set classification. The present contribution is the explicit full set identities above, not the known general decidability of automatic predicates.

## Limitations
The result is restricted to base two, binary weight classes modulo three, and one or two summands. No assertion about the minimal number of summands beyond two, other moduli, or other bases is made. The proof is computer-assisted in the precise sense that the finite automaton reachability census is executed by the included readable certificate; an independent formal proof checker was not employed. Earlier unindexed or differently formulated results might cover the classification; no publication-priority claim is made.

## References
1. Jean-Paul Allouche and Jeffrey Shallit, *Additive Properties of the Evil and Odious Numbers and Similar Sequences*, arXiv:2112.13627, version 1 submitted 27 December 2021; sections 1–5 and automata constructions.
2. Jeffrey Shallit, *Frobenius Numbers and Automatic Sequences*, arXiv:2103.10904, version 1 submitted 19 March 2021; sections 2–4.
