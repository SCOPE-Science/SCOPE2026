# Review of the length-four cyclic palindrome cover theorem

## Correctness — PASS

The target factor \(abba\) with \(a\ne b\) has a uniquely dedicated length-two \(b\)-run flanked by \(a\)-runs. Constant targets need runs of length at least four. Their costs yield \(N\ge R+q(q-1)+3q\). Each unordered pair requires both run patterns \(aba\) and \(bab\), forcing three skeleton traversals when \(q\ge3\); even-degree parity adds a matching-sized cost for even alphabets. The \(q=2\) run bound is handled separately. An explicit Eulerian zigzag and run-length assignment attains all bounds. Equality determines all stated run and transition multiplicities. The included verifier gives constructive checks for \(2\le q\le50\) and independent exact state-space minima at \(q=2,3\); finite checks supplement the proof.

## Originality — PASS, with limitations

Full-text comparison with Gardner–Godbole (2017, arXiv:1711.07029) and Chen–Kitaev–Sun (2019, arXiv:1908.01116) finds their universal-cycle settings and restrictions different from minimum at-least-once all-palindrome cyclic covers. OEIS A330022 contains the known binary length-four superstring value 12, expressly excluded from novelty claims. A pre-existing length-three palindrome-cover classification has the same unordered-edge parity mechanism, but does not state the forced length-two internal runs, length-four long runs, and length-four \(q\)-ary optimum. This is a closely related weighted-run refinement, rather than an independent new method. Residual risk: an earlier shortest-superstring or graph-postman specialization may contain the same statement under different terminology; search absence is not proof of priority.

## Mathematical value — PASS

The shortest at-least-once cover of every ordinary four-letter palindrome is a natural optimal-overlap problem with \(q^2\) prescribed factors. This theorem gives an exact all-alphabet optimum, a parity jump, and mandatory run lengths/adjacency profiles, rather than a constructed upper bound or a single binary table value. The explicit witnesses and proof facilitate comparison with longer even-palindrome coverings and palindromic superstring questions. It does not claim enumeration of optimum words or a general theorem at every factor length.

Self-review: passed. Independent audit: not yet performed.
