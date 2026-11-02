# Scientific review: sharp degree-two McKinsey census

## Correctness (PASS)

The argument translates falsification of \(\Box\Diamond p\to\Diamond\Box p\) into simultaneous splitting of the successor sets at a world. With maximum outdegree two, at most two two-element sets form a bipartite graph. A dead end itself invalidates the axiom globally, while one-successor rows force the implication. The resulting unique partition into \(k\) singleton rows and \(n-k\) doubleton rows gives the explicit sum. The binomial upper and lower bounds at \(k\approx n/W_0(n)\) establish the stated logarithmic asymptotic. The six-world triangle example violates the degree-two criterion at maximum outdegree three. An independent exhaustive frame-and-valuation computation for \(n\le4\) matches \(1,6,75,1612\). Risk: finite tests do not prove general theorems; the full argument above supplies the arbitrary-size proof.

## Originality (PASS subject to historical-priority limits)

Theorem 26 of van Benthem, ten Cate and Yang, arXiv:2603.12171 (12 March 2026), establishes general McKinsey frame-validity coNP-completeness through Set Splitting. Its proof supplies the relevant general semantic interpretation but not the bounded-degree enumeration. Chen and Ma, *The McKinsey Axiom on Weakly Transitive Frames* (doi:10.1007/s11225-024-10145-x), prove a closely related singleton/terminal-successor characterisation on weakly transitive frames only: that overlapping scope is prior art, not claimed as new. This result removes the weak-transitivity hypothesis in a different restriction (maximum outdegree two) and adds all-order labelled counts and rarity asymptotics. OEIS A185289 agrees on the first four positive terms but differs already at the fifth (52805 versus 52795). Scientific record, query and implication comparisons did not identify a dominating earlier statement, but old uncatalogued modal-logic enumerations remain a risk. Novelty is not independently certified.

## Value (PASS)

This is a complete all-parameter enumeration of a natural tractable family inside a general coNP-complete finite-frame validity problem. It gives a combinatorial explanation of the sharp degree-two/degree-three transition and an asymptotic rarity law. The theorem does not assert broader modal-logic complexity reductions, an unlabelled count, or any publication priority certificate.

## Reproducibility and evidence limits

Read `RESULT.md` for definitions, all quantifiers, the proof, and direct references. Run `python checker.py` (Python standard library only) to exhaustively check sizes one through four and the six-world example. These computations test finite samples and are not substituted for the all-integers argument. Other variants and general maximum-degree-three validity are not classified. Historical priority may change with additional external literature review.

Self-review: passed. Independent audit: not yet performed.
