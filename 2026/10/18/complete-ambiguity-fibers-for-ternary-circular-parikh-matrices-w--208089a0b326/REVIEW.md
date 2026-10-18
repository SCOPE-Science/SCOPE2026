# Mathematical review

## Correctness — PASS

The domain is fixed-composition ternary necklaces with two \(a\)'s and exactly one \(b\), not linear words. The unique \(b\) makes the cyclic anchor unique and ensures the full rotation-average is over \(n=h+3\) distinct conjugates. Each ordered-pair count is obtained by counting cuts; the triple \(abc\) occurs for an anchored positional triple only for \(c\) before \(a\), in exactly the positional-distance number of cuts. These arguments give a complete matrix in two integer parameters \(s=t+u\) and \(d=u-t\). Equality of matrices reduces to equality of \(s\) and \((d-2)^2\), whose only nontrivial positive-gap coincidence is \(d=1\) versus \(d=3\). The boundary constraints yield exactly \(h-1\) disjoint doubletons when \(h\geq2\), and no other collisions. The count, singleton number, one-\(a\) injectivity threshold, and limit all follow. Independent exhaustive direct-rotation checks agree for \(8436\) two-\(a\) necklaces across \(0\leq h\leq35\), but the proof, not those tests, establishes all lengths.

## Originality — PASS, with residual risk

The most relevant primary source is Poovanandran--Simpson--Teh, arXiv:2110.14858v1, especially its explicit open general ternary classification question and conditional \(CE_1\) rewriting theorem. That theorem already generates the particular \(caac\leftrightarrow acca\) coincidences; their existence is not claimed new. The new statement is the **only-if** classification and exact fiber enumerator for every parameter in a natural infinite fixed-composition family. Inspected later work on \(q\)-weighted circular Parikh matrices studies a stronger *different measurement*, and the work on Lyndon conjugates uses a different map. Indexed published-research comparisons and accessible related historical statements did not reveal exact coverage. Equivalent unindexed or overlooked published results remain possible; the relevant earlier rewriting construction limits the scope of originality.

## Mathematical value — PASS

This solves a complete and motivated first noninjective family inside the ternary circular Parikh reconstruction problem: when the uniquely anchored middle symbol occurs once, a single outer symbol is always reconstructible, whereas two outer symbols admit exactly classified collisions for every number of remaining letters. It determines the exact number and sizes of reconstruction classes (and therefore exact zero-error observation capacity), with a sharp threshold and asymptotic almost-sure uniqueness among the fixed-composition necklaces. It does not purport to solve the general ternary equivalence question.

## Remaining limitations

The described \(CE_1\) instances were previously known; no claim of a wholly new rewrite mechanism is made. The result is limited to the stated fixed composition, and the paper's published later version or unindexed work could contain an equivalent enumeration. Verification of finite cases is supportive, not a substitute for the combinatorial proof.

Self-review: passed. Independent audit: not yet performed.
