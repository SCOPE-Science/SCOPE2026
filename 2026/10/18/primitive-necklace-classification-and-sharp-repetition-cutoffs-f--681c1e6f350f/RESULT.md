# Primitive-necklace classification and sharp repetition cutoffs for two-variable logic on colored directed cycles

## Finding
Let \(\Sigma\) be a fixed nonempty finite alphabet. For each nonempty word \(w\in\Sigma^+\), construct the pointed-free relational structure \(C(w)\): its universe is the cyclically indexed positions of \(w\), the binary relation \(S(i,j)\) holds exactly when \(j=i+1\) modulo \(|w|\), and unary predicates \(P_a\) name the letter at each position. The logic \(\mathrm{FO}^2[S,(P_a)_{a\in\Sigma}]\) has equality, all Boolean connectives and quantifiers, but only the two reusable variable names \(x,y\); it has neither a linear order nor counting quantifiers.

Every nonempty cyclic word has a unique primitive root up to rotation: write \(w=u^k\) with \(u\) not a proper power, and put \(d=|u|\). Define
\[
  c(d)=\begin{cases}4,&d=1,\\3,&d=2,\\2,&d\ge3.\end{cases}
\]
**Theorem.** For all nonempty cyclic words \(u^k\) and \(v^\ell\) with primitive roots \(u,v\), the structures \(C(u^k)\) and \(C(v^\ell)\) satisfy the same two-variable first-order sentences **if and only if** \(u\) and \(v\) are cyclic rotations of each other and \(\min(k,c(|u|))=\min(\ell,c(|u|))\). Thus these repetition cutoffs are exact for every primitive-root length. Equality of entire two-variable theories on the indicated cycle class is decidable in linear time in the total input lengths when alphabet symbols admit constant-time comparison.

## Assumptions and scope
Both models are single nonempty finite **directed** cycles. For length one, \(S\) is a loop; for length two, \(S\) contains both ordered edges. All letter predicates are unary and partition the universe, and the alphabet is fixed and finite. Equivalence means agreement on *all* two-variable sentences, without a fixed quantifier-rank bound. Primitive necklace means a primitive word modulo cyclic rotation. A repetition \(u^k\) is read cyclically. The result does not assert anything about a general disjoint union of cycles, arbitrary additional relations, counting quantifiers, or visible linear order.

## Proof
**Step 1: arbitrarily long contiguous factors remain visible with two variables.** For each finite letter word \(a_0\cdots a_{t-1}\), a unary formula \(\theta_{a_0\cdots a_{t-1}}(x)\) asserts that the forward successor path of length \(t-1\) beginning at \(x\) has these labels. It uses only \(x\) and \(y\): begin with \(P_{a_0}(x)\), existentially quantify \(y\), assert \(S(x,y)\wedge P_{a_1}(y)\), then quantify a fresh occurrence of \(x\), assert \(S(y,x)\wedge P_{a_2}(x)\), and alternate until the end. The previous variable is no longer needed when overwritten. The sentence \(\exists x\,\theta_t(x)\) is true exactly when \(t\) occurs as a cyclic factor. All factors of every length are available in any nonempty repetition of the primitive root.

If the primitive periodic sequences \(u^\omega\) and \(v^\omega\) have the same finite-factor sets, then their primitive necklaces coincide. Indeed, every arbitrarily long prefix of \(u^\omega\) occurs in \(v^\omega\). There are only \(|v|\) possible start residues; some start residue works for unbounded prefix lengths. The two right-infinite periodic sequences then agree after that shift, so their least periods and primitive cyclic roots agree. Consequently different primitive necklaces have different two-variable theories.

**Step 2: repetition multiplicity below the cutoff is definably visible.** Since \(u\) is primitive of length \(d\), all of its \(d\) cyclic rotations are distinct. The unary two-variable formula \(T_u(x)=\theta_u(x)\) therefore singles out one residue modulo \(d\) inside \(C(u^k)\). The two-variable sentence
\[
  \exists x\,\exists y\,[x\ne y\wedge T_u(x)\wedge T_u(y)]
\]
holds precisely when \(k\ge2\). Shadowed variables within each conjunct in the definition of \(T_u\) do not change the two free occurrences \(x,y\) in the conjunction.

For \(d=2\), primitivity means \(u=ab\) with \(a\ne b\). In a twofold repetition, every differently colored pair is adjacent in at least one direction; in a threefold or higher repetition there is a differently colored nonadjacent pair. Thus
\[
 \exists x\,\exists y\,[P_a(x)\wedge P_b(y)\wedge\neg S(x,y)\wedge\neg S(y,x)]
\]
separates \(k=2\) from \(k\ge3\). For \(d=1\), the sentence \(\exists x\,S(x,x)\) distinguishes \(k=1\), the sentence \(\exists x\exists y[x\ne y\wedge S(x,y)\wedge S(y,x)]\) distinguishes \(k=2\) from \(k\ge3\), and the existence of distinct nonadjacent vertices distinguishes \(k=3\) from \(k\ge4\). Together these formulas distinguish every distinct capped multiplicity.

**Step 3: a uniform two-pebble back-and-forth relation above the cutoff.** Suppose the primitive roots are the same word \(u\) of period \(d\) and that both multiplicities are at least \(c(d)\). Relate assignments to the two reusable variables whenever their pebbled positions have matching residues modulo \(d\) and the same complete atomic two-variable type. Here the atomic type comprises equality and the truth values of \(S(x,y)\), \(S(y,x)\), and all unary colors. Such a relation includes the empty assignment, because both cycles contain all residues.

To answer an existential move replacing one pebble while the other stays at a residue \(r\), choose a new position of the required residue \(s\) having the same atomic relation to the stationary pebble. This is always possible, for the following exhaustive reason. If \(d\ge3\), a cycle containing two full copies of \(u\) realizes, relative to each position: equality at residue \(r\), a distinct non-neighbor at residue \(r\), a forward neighbor at residue \(r+1\), a backward neighbor at residue \(r-1\), and a non-neighbor of each of the latter two residues. All other residues occur as non-neighbors. The same list occurs in every higher repetition. For \(d=2\), the forward and backward neighbors have the same residue and are distinct as soon as the cycle has at least three copies; a further non-neighbor of this opposite residue then also exists. For \(d=1\), four positions supply equality, separate forward and backward neighbors, and a distinct non-neighbor. Exactly the same atomic options persist at all higher multiplicities. Thus the matching-residue, matching-atomic-type assignments form a two-pebble back-and-forth system. Structural induction over formulas (including arbitrarily many alternating quantifiers) proves agreement on every \(\mathrm{FO}^2\) sentence.

If both multiplicities are below \(c(d)\) and their capped values agree, they are equal and the cycles are isomorphic. This completes both directions of the theorem.

**Algorithm.** Compute the least period of each word by a prefix-function computation in linear time. Compute the lexicographically least cyclic rotation of the primitive root using a linear-time minimum-rotation algorithm. Compare these canonical roots and the capped repetition exponents. Every step costs linear time in the input length for a fixed finite alphabet.

## Verification
The accompanying standalone Python program `verify.py` independently constructs all cyclic binary necklaces of lengths at most nine (153 models) and ternary necklaces of lengths at most six (225 models). It iterates the exact full two-pebble semantic-type refinement for ordered pairs, using atomic colors, equality and both directed successor atoms, then both possible pebble rebindings. It compares the resulting complete sentence-theory partition with the predicted primitive-necklace/capped-repetition signatures. Results: 140 equal theory classes on 153 binary models and 219 classes on 225 ternary models, with no mismatches in either direction. Run `python3 verify.py` with the Python standard library. Finite comparisons do not substitute for the unrestricted proof in Steps 1--3.

## Relationship to prior work
Michaliszyn and Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations* (first public 2026-10-07), study satisfiability with arbitrary numbers of successor graphs induced by (possibly infinite) linear orders and unrestricted further predicates. Their Section 2 and introductory distinctions explicitly require each successor to come from a linear order; no finite directed cycle of size exceeding one is such a successor graph. Their star-type and bounded-multiplicity certificates are conceptually related, but do not give the exact primitive-necklace classification or the sharp \(4,3,2\) cycle-power cutoffs established here.

Weis and Immerman, *Structure Theorem and Strict Alternation Hierarchy for \(\mathrm{FO}^2\) on Words* (2009), classify finite linearly ordered words, with and without successor in a signature that retains the linear order. The present logic has *no* order and its models are circular words; the ordered-word structure theorems do not directly imply the sharp uniform cutoffs in this theorem. Fournier and Turán, *A Game for Counting Logic Formula Size and an Application to Linear Orders* (2025), address formula-size games and linear-order settings, rather than this cyclic two-variable theory equivalence.

## Limitations
The theorem is specific to a single directed successor cycle with unary colors, equality, and exactly two variables, without counting quantifiers or an order predicate. Adding a third variable can count more representatives of a residue class, so the sharp thresholds must not be exported to richer logics. The result is a self-review mathematical argument with bounded experimental corroboration, not an independently certified theorem. Although targeted searches found no equivalent statement, an older unindexed two-pebble treatment of circular successor structures could subsume the classification.

## References
1. J. Michaliszyn and P. Witkowski, *Two-Variable Logic with Arbitrarily Many Successor Relations*, arXiv:2610.09758, first publicly posted 2026-10-07. https://arxiv.org/abs/2610.09758 (Sections 1--2 and the related-work discussion inspected).
2. P. Weis and N. Immerman, *Structure Theorem and Strict Alternation Hierarchy for FO² on Words*, *Logical Methods in Computer Science* 5(3), 2009, arXiv:0907.0616. https://arxiv.org/pdf/0907.0616 (Introduction and main structure-theorem setting inspected).
3. G. Fournier and G. Turán, *A Game for Counting Logic Formula Size and an Application to Linear Orders*, arXiv:2505.16185, first publicly posted 2025-05-22. https://arxiv.org/pdf/2505.16185 (Introduction and principal problem setting inspected).
