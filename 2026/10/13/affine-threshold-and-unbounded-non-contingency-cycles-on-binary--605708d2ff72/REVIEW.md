# Scientific review: affine threshold and unbounded non-contingency cycles

## Correctness — PASS

The local coordinate is the indicator that all successor bits agree. Its algebraic normal form has degree \(r-1\) for \(r\ge2\) and is constant for \(r\le1\). Thus the affine threshold is exact, even with empty successors and self-loops. Every row of the associated binary matrix has even weight, so \(B\boldsymbol1=0\), giving the exact formula \(\Delta^k(x)=\boldsymbol1+B^k x\) for every \(k\ge1\). The finite-dimensional image-kernel decomposition proves that the first stable rank index is the least uniform preperiod and that the order on the stable image is the least eventual period. A cyclic-permutation minimal-polynomial calculation gives periods at least \(n-1\) for each odd \(n\). The n=3 matrix and all boundary cases were checked independently. The supplied verifier replays 15,002 frame cases and 237,068 initial event valuations. No finite exploration is used as a proof of the universal statements.

## Originality — PASS, subject to residual risk

The 2026 motivating paper establishes the semantics and labelled sequent calculi for path-defined frame classes, not this linear classification; its accessible full text was inspected at the semantics, calculus and completeness arguments. Humberstone's agreement semantics and the earlier knowing-whether literature are credited, as are classical linear algebra facts. Searches for binary-successor non-contingency over \(\mathbb F_2\), iterated knowing-whether cycles, affine thresholds and matrix periodicity produced no direct equivalent. The closest relevant already-established result gives finite-transitive-frame stabilization, whose transitivity hypothesis excludes the nontransitive periodic witnesses. A historical full text on agreement was not completely retrievable; hidden equivalences remain possible. Search noncoverage does not establish absolute novelty.

## Value — PASS

The object is the natural iterated non-contingency truth-set operator. The exact two-successor threshold separates genuinely affine from nonlinear behavior, allowing a complete least-preperiod/least-period classification instead of a mere finite simulation. The unbounded odd-cycle family proves that small local uncertainty does not impose a universal global convergence or period bound; three worlds already suffice for nontrivial periodicity. The phenomenon is structural and mathematically motivated rather than an arbitrary parameter slice.

## Scientific limits

The conclusions apply to finite frames and equality of operators on all event valuations. They do not claim an axiomatization, an infinite-state theorem, or novelty of the ordinary Fitting decomposition itself. Equivalent prior treatments using Boolean networks, cellular dynamics or agreement semantics remain a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
