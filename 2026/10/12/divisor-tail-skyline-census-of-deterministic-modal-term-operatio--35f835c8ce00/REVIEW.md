# Scientific assessment: divisor–tail skyline census

## Correctness — PASS (self-review)

The key normalization uses inverse image as a Boolean endomorphism, so all nested modalities reduce to shifted input variables. Every rooted forward trace is realizable by definition, and a finite common distinguishing horizon separates the finite set of possible traces. Thus one freely chooses one output bit per trace, leading to exactly \(2^{|T_f(q)|}\) operations, with no hidden assumption that each valuation independently realizes all traces. The precise realizability criterion is \(d\mid\ell(w)\) and \(b\le h(w)\); disjoint classes of exact eventual period and preperiod have the counted sizes. Degree and nullary boundaries are checked in the proof. Exhaustive trace construction and independent partition refinements corroborate the formula for all 288 endofunctions on at most four vertices at three alphabet sizes; direct Boolean modal-term closure is also checked in 15 small cases. There is no infinite computational extrapolation.

## Originality — PASS (self-review, with uncertainty)

The closest established theory computes **modal distinguishing certificates** (Wißmann–Milius–Schröder, arXiv:2105.00669 and arXiv:2203.11175) and characterizability/local tabularity (ten Cate–Koudijs, arXiv:2304.06646), not the exact arity-wise term clone of a fixed arbitrary finite deterministic frame. The group-shift setting and Boolean endomorphism condition of Castillo-Ramirez et al. (arXiv:1908.09675) count different objects. A related exact criterion for *whether a fixed coloring generates the whole powerset* does not directly determine the term-clone count across all input valuations: it asks when a single valuation distinguishes worlds, not how many distinct uniform term operations exist. Explicit overlapping basic ingredients are not claimed as new. Residual risk: the polynomial may be implicit in pre-existing modal algebra, universal algebra, or symbolic dynamics treatments not located under these aliases. Search failure is not a novelty certificate.

## Mathematical value — PASS (self-review)

An exact and natural invariant is obtained for **every** finite functional graph, including arbitrary mixtures of branching trees and directed cycles. The formula separates combinatorial data that affect term expressiveness from inessential branch multiplicity, quantifies the interaction of cycle-period divisibility, handles all arities including zero, and supplies an exact leading-degree structural parameter. The entire term-clone arity spectrum is not a restatement of single-coloring generation and is not a small ad-hoc finite enumeration. It provides usable formulas without enumerating all \(q^{|W|}\) valuations or closure-saturating the enormous operation set.

## Sources and limitations

Primary full-text comparisons: Wißmann et al., 2021/2022, sections on generic distinguishing witnesses and refinement; ten Cate and Koudijs, 2023 preprint, sections on finite characterizations and local tabularity; Castillo-Ramirez et al., 2019 preprint, statements and arguments on group-shift cellular automata and finite Boolean alphabets. All three were inspected in lawful open-access PDFs. Distinctness of the precise polynomial is a qualified assessment, not an independently certified historical priority claim.

Self-review: passed. Independent audit: not yet performed.
