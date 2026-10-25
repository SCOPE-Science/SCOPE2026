# Self-review

## Correctness — PASS
The definition of the binary tortoise map agrees with the original recursive map for ordered binary words. Rational mechanical rotation produces exactly \(\min\{n+1,q\}\) distinct factor cells. Crossing their boundaries creates lexicographically increasing adjacent transpositions, with a repeated transposition every \(q\) indices. Before the second transposition is exposed, removing the first \(1\) merges exactly the boundaries indexed by \(1\le j\le h\); after it is exposed those merges disappear one by one. This establishes both formula branches and the exact threshold for all coprime parameters. The integer factor checker passes 773 coprime parameter pairs and 52,813 enumerations; a separate exact-midpoint checker passes 48,807 boundary comparisons. The computation is a test, not the infinite proof.

## Originality — PASS within examined evidence
Defant–Kravitz introduce the operators and study global preimage enumerations, not the Christoffel periodic factor-language count. Campbell–Rampersad introduce tortoise factor complexity and study automatic-word examples; their conclusion explicitly raises Sturmian-style extensions, not a rational-slope enumeration. A separately known irrational-Sturmian formula is not applicable by substituting rational slopes: at \(n\ge q\) the factor language is capped at \(q\), repeated rotation discontinuities appear, and the \(p=1\) family even drops from two images to one at the period boundary. Targeted mathematical-record searches did not identify an exact rational formula. Residual risk: an unindexed Christoffel-factor or stack-sorting classification may imply the same count.

## Mathematical value — PASS
The exact all-length result closes the rational mechanical-word case of a new stack-sorting factor invariant. It identifies the sharp recovery time \(q+\lfloor(q-1)/p\rfloor\) after phase-collisions and a non-monotone boundary effect when the period has one \(1\). This is an intrinsic, parameter-uniform classification for a canonical family, rather than a small-table computation or a replacement of an irrational parameter by a rational one.

## Limits and closest literature
The conclusion covers one-step tortoise images of periodic reduced rational mechanical binary words, not hare images, further tortoise iterations, or irrational mechanical words. The source operator is Defant–Kravitz (2018 preprint; journal 2020), and the motivating factor-complexity framework is Campbell–Rampersad (2026). Neither examined source contains the claimed rational formula. The accessible prior irrational formula supplies related but not covering coverage; independent historical-priority review remains appropriate.

Self-review: passed. Independent audit: not yet performed.
