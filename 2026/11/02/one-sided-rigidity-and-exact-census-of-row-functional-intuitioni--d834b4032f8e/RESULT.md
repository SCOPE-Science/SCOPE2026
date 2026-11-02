# One-sided rigidity and exact census of row-functional intuitionistic binary-modal chain frames

## Finding

For every integer \(n\geq1\), consider the labelled chain \(C_n=\{0,1,\ldots,n-1\}\) and a ternary accessibility relation \(R\subseteq C_n^3\) with at most one output pair \((v,w)\) for each input world \(u\). Impose both of the intuitionistic binary-modal frame monotonicity clauses of Kaminski (2026), stated precisely below. Then every nonempty such relation is **one-sided**: its active input worlds form a final interval, and either every output's first coordinate or every output's second coordinate equals the top world.

More precisely, all relations are uniquely classified by an active-suffix length \(m\in\{1,\ldots,n\}\), an orientation (left-variable or right-variable), and an \((m-1)\)-bit increment word. The free output coordinate ends at \(n-1\) and increases by either zero or one at each successive active world. The two orientations coincide only for the all-zero increment word, which gives the constant output \((n-1,n-1)\). There is also the empty relation.

Consequently the **exact number of labelled row-partial-functional frames** is
\[
F_n=1+\sum_{m=1}^n(2^m-1)=2^{n+1}-n-1.
\]
If every world is required to have an output (total functionality), the number is exactly \(2^n-1\). If target-coordinate commutativity is additionally imposed, there are exactly \(n+1\) partial-functional frames (including the empty one) and exactly one total-functional frame.

This is an obstruction to a genuinely two-variable *deterministic* interpretation of the binary existential modality on finite intuitionistic chains: wherever its output is defined, one argument is necessarily evaluated at the top world. The result concerns frame structure, not an axiomatization or decision procedure for the full logic.

## Assumptions and scope

Write \(N=n-1\). The ternary relation \(R(u,v,w)\) has its first coordinate as the input/evaluation world; \((v,w)\) are the two output worlds. **Row-partial-functionality** means that for each \(u\) there exists at most one ordered pair \((v,w)\) satisfying \(R(u,v,w)\). An input is *active* if it has such a pair. No seriality, reflexivity, commutativity or associativity of \(R\) is assumed.

The two frame axioms are:

(M1) For all \(u\leq u'\) and all \(v,w\), if \(R(u,v,w)\), then there exist \(v'\geq v\), \(w'\geq w\) with \(R(u',v',w')\).

(M2) For all \(u,v,w,v',w'\), if \(R(u,v,w)\), \(v'\geq v\), and \(w'\geq w\), then there is some \(u'\geq u\) with \(R(u',v',w')\).

The inequalities and quantifiers range over \(C_n\). For an active \(u\), denote its unique output by \(f(u)=(a_u,b_u)\). The classified normal forms are precisely:

* All inactive inputs precede the final interval \(u=n-m,\ldots,N\).
* Either \(f(u)=(a_u,N)\) for all active \(u\), or \(f(u)=(N,a_u)\) for all active \(u\).
* \(a_N=N\), and \(a_{u+1}-a_u\in\{0,1\}\) for every pair of successive active inputs.

For \(m=1\), the increment word is empty, and the only output is \((N,N)\). Each normal form stays within the chain because starting from \(N\) and subtracting at most \(m-1\leq n-1\) binary increments produces a nonnegative initial value.

## Proof

**1. Active suffix and monotone output path.** If input \(u\) is active and \(u'\geq u\), condition (M1) forces input \(u'\) to be active. Thus the active inputs form a suffix. At two successive active inputs, the witness pair in (M1) is unique, so both components of \(f(u)\) are nondecreasing as \(u\) increases. Therefore the outputs form a chain in the coordinatewise product order on \(C_n^2\).

**2. The top output and one-sided rigidity.** Apply (M2) to the output of the last active input \(N\), enlarging both coordinates to \(N\). As the only input at least \(N\) is \(N\) itself, the unique output there must be \(f(N)=(N,N)\). Now let \(k\) be the first active input, and write \(f(k)=(a,b)\). Suppose both \(a<N\) and \(b<N\). Clause (M2) applied at \(k\) requires the two incomparable target pairs \((a+1,b)\) and \((a,b+1)\) to occur among outputs at inputs at least \(k\). But by Step 1 all such outputs are coordinatewise comparable. Contradiction. Hence \(a=N\) or \(b=N\). Coordinatewise monotonicity then forces that same coordinate to remain \(N\) at every active input.

**3. No skipped values.** In the remaining coordinate, let \(a_k\) be the value at first active input. For every \(c\in\{a_k,\ldots,N\}\), (M2) at \(k\) requires an output at some later input whose variable coordinate is exactly \(c\) (while the other coordinate stays \(N\)). Thus the weakly increasing integer sequence \(a_k,a_{k+1},\ldots,a_N=N\) attains every intermediate integer. Equivalently, its adjacent increments all lie in \(\{0,1\}\). Conversely, any weakly increasing sequence ending at \(N\) with such increments attains every integer between its value at \(u\) and \(N\), for each active \(u\).

**4. Sufficiency.** Every proposed normal form satisfies (M1): for any active input \(u\), every later input is active, and its output dominates \(f(u)\) coordinatewise. To check (M2), take an active \(u\), and any \((v',w')\) coordinatewise above its output. The fixed coordinate is already \(N\), so its enlargement still equals \(N\). The other coordinate is some integer \(c\) between \(a_u\) and \(N\). By Step 3, \(c\) appears at an active input \(u'\geq u\), yielding exactly the requested pair. The empty relation satisfies both implications vacuously.

**5. Enumeration and the commutative case.** For a fixed suffix length \(m\), there are \(2^{m-1}\) possible increment words in each orientation. Precisely one word, the all-zero word, belongs to both orientations: any other word produces an output with one coordinate strictly below \(N\), distinguishing the orientations. Thus the number for that suffix length is \(2\cdot2^{m-1}-1=2^m-1\). Sum over \(m\) and add the empty relation to obtain \(F_n\). Total functionality fixes \(m=n\), yielding \(2^n-1\). Commutativity under \((v,w)\leftrightarrow(w,v)\), combined with row-partial-functionality, requires each active output to be diagonal. One-sided rigidity forces each to equal \((N,N)\), giving exactly one such relation per suffix length plus the empty relation, hence \(n+1\).

## Verification

The standalone `checker.py` directly evaluates both quantified frame conditions for every partial row function over chains of sizes \(n=1,2,3,4\), independently constructs the proposed normal form predicate, compares them on **every** assignment of rows, and checks the counts \(2,5,12,27\). It also verifies the serial and commutative refinements. Running `python checker.py` returns `ALL_CHECKS_OK`. This is an exhaustive finite consistency check only through four worlds; the unbounded theorem follows from the five proof steps above, not from finite enumeration.

## Relationship to prior work

Kaminski (2026, Definition 2) formulates the two ternary persistence conditions (M1) and (M2) and proves soundness and strong completeness of the resulting intuitionistic binary-modal semantics. Those clauses are the *premises* used here, not an original contribution. Kaminski (2024) addresses the distinct, additional associativity assumption and undecidability of associative binary-modal logics; neither result classifies deterministic finite chain frames.

A related observational-equivalence classification for unrestricted finite-chain ternary relations uses coordinatewise row down-closures and suffix unions. Its statements concern semantic equivalence classes and fiber sizes of arbitrary relational presentations. Such information does not itself give the structural one-sidedness theorem, the unit-step normal form or the count of row-partial-function frames established here. Earlier analyses of unary modal finite-chain frames concern binary, rather than ternary, accessibility relations and their different confluence conditions.

## Limitations

The rigidity depends simultaneously on **both** frame axioms, a finite **linear chain**, and **at most one output pair per input**. It does not apply to unrestricted ternary relations, to general partial orders, or necessarily to branching nondeterministic interpretations. The existence of the exact formula does not establish completeness of this restricted frame class for the ambient logic, any complexity bound for logic validity, or a result under added associativity. A historically equivalent specialized enumeration could exist in earlier algebraic or ternary-frame literature; comparison with the accessed sources does not establish absolute priority.

## References

1. M. Kaminski, *Intuitionistic logic of a binary modality*, Archive for Mathematical Logic, first publicly available 2026-09-09, DOI 10.1007/s00153-026-01025-3. https://link.springer.com/article/10.1007/s00153-026-01025-3.
2. M. Kaminski, *On undecidability of the propositional logic of an associative binary modality*, Archive for Mathematical Logic 63 (2024), 837–857, DOI 10.1007/s00153-024-00921-w. https://link.springer.com/article/10.1007/s00153-024-00921-w.
