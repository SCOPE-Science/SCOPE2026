# Scientific review

## Correctness — PASS

The claim has two parts, each with a separate finite or symbolic proof. The infinite-family law relies on a bijection between left-maximal primitive squares and starts of circular runs. The crucial primitive-square lemma is justified using the Fine–Wilf theorem, and the factor-frequency identity holds because every de Bruijn length-\(n\) block occurs exactly once. The exact-length counts require two nonmatching boundary letters and a length-\((L+2)\) factor inside the de Bruijn uniform range. The complementary long-run count follows by a checked geometric sum. The argument explicitly excludes all purported periods at least \(n\), because such a repeated factor would duplicate a length-\(n\) window at distinct circular starts.

The binary order-five census is exhaustive for mathematical reasons, not because many examples were sampled. Every de Bruijn cycle corresponds uniquely to a Boolean 16-entry nonsingular feedback function with one 32-state orbit, and all 65,536 functions are tested. A separate Euler-tour construction independently returns precisely the same 2,048 cycles. Two different positioned-run detectors—maximal shift-equality blocks versus direct minimal-period and boundary tests—agree on every cycle. The actual embedded `checker.py` was executed and returned `VERIFY_OK`. Its asserted six profiles and total frequencies match the stated claim.

This proof does not rely on an experiment to establish the unrestricted \(q,n,p\) formula. Conversely, the finite table is claimed only for order five.

## Originality — PASS, with historical-priority risk

The precise new contribution sought is the all-cycle period-profile table at binary order five together with a uniform low-period run baseline and explicit length refinement. The uniform baseline is a relatively short consequence of ordinary de Bruijn factor balance plus the primitive-square bijection; its elementary nature is acknowledged rather than presented as a deep new upper bound. The nonrigid order-five table, particularly the six supported period profiles, is not implied by uniform factor counts at lengths at most five: periods three and four require information about longer, cycle-dependent factors.

Bannai et al.'s original preprint, arXiv:1406.0263 (2014), develops general run theory, proves global upper bounds for arbitrary linear strings and gives run algorithms; it does not provide this family-specific circular table. Ilie–Yu–Zhang (2004), inspected in the author's full-text PDF at its de Bruijn section, study the distinctly defined minimum repetition-encoding cost and derive an asymptotic lower bound; they do not count maximal periodic intervals. Fredricksen's 1982 survey covers generation algorithms, with only its abstract available for inspection here. An existing cycle generator can be used to reproduce the new computation, but the construction algorithm itself neither specifies this invariant nor entails the six numerical frequencies without further analysis. Relevant accessible historical claims on Cantor-word maximal repetitions, the order-five Burrows–Wheeler run spectrum and the order-five Lyndon spectrum concern distinct objects or transforms, not the positioned circular runs of the original de Bruijn cycles.

The completed published-finding corpus, bibliographic and own-record searches did not reveal an equivalent or dominating result. The absence of an indexed match is not a proof of priority. The unavailable full text of some older shift-register and sequence-complexity literature remains a named residual risk. There is no directly identified stronger covering result or unresolved decisive same-invariant comparison.

## Value — PASS

Runs are a central repetition invariant in string algorithms, while de Bruijn cycles form a canonical maximally factor-diverse class. The result separates rigid behavior fixed by universal short-factor coverage from the first genuinely cycle-dependent period profiles. It gives a reproducible, complete benchmark for all 2,048 order-five cycles and two exact closed-form identities valid at arbitrary alphabet size and order. The order-five family is naturally selected as the first binary order with more than a few dozen rotation classes; the six-profile classification is not a cherry-picked subclass or a routine increment of an existing numerical threshold. Its exact table and structural rigidity boundary provide a baseline for higher-order repetitions research and for testing circular-run enumeration methods.

## Scope and residual risks

The higher-period distribution at general order, and any explicit higher-order total-run spectrum, are not claimed. Historical novelty is best-knowledge rather than certified priority. No independent audit has been performed; the review and verification reported here are non-independent scientific checks.

Self-review: passed. Independent audit: not yet performed.
