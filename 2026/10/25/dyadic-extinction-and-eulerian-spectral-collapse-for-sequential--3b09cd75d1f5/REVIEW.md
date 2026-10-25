# Scientific review

## Correctness — PASS

The statement fixes the ring size, the exact repeated permutation sweep, field, and normalization of update positions. In the actual proof, the lower-triangular implicit matrix has determinant one; the characteristic determinant expansion partitions all permutations into independent adjacent transpositions and the two complete ring orientations. A separate characteristic-two transfer-matrix argument establishes the dyadic monomial criterion without extrapolation from finite tests. The low-degree support obstruction excludes every unbalanced orientation, and Cayley–Hamilton gives the uniform extinction bound. Circular Eulerian enumeration counts every schedule. The standalone verifier directly reconstructs sweep maps and determinant coefficients rather than calling the symbolic proof. The unrestricted proof is analytical; finite checks are supporting evidence.

## Originality — PASS (inspected evidence)

Macauley–Mortveit (arXiv:0802.4412) establish general update-order cycle-equivalence bounds, not the Rule-90 determinant or nilpotence census. Vielhaber (arXiv:1208.2762) studies asynchronous ECA expressivity and surveys Rule 90 as a reachability example, not a repeated fixed-order nilpotency threshold. Defant (arXiv:1511.06966) obtains orbit data for invertible Rules 150 and 105, which do not imply the noninvertible Rule-90 result. Balbi et al. (arXiv:2004.07128) study a named collection of non-maximally sensitive rules excluding 90. Donoso-Leiva et al. (arXiv:2509.07797v2, Sec. 3.1.2) make a contrasting universal nonconvergence assertion for Rule 90; the four-site trajectory in the proof is a direct counterexample to its literal formulation, not a consequence of it. Searches for equivalent matching-polynomial, Eulerian and nilpotent-schedule descriptions returned no dominating published theorem. No search exhausts unindexed literature; historical priority remains a residual risk.

## Mathematical value — PASS

Fixed-order update is an intrinsic parameter of asynchronous cellular automata. The theorem identifies an exact arithmetic extinction boundary (powers of two only), an exact balancing condition on schedules, and an Eulerian count of all successful schedules, while compressing factorially many update orders into a sharp set of spectral classes. The dyadic-vs-nondyadic dichotomy and concrete interaction with an existing contrary assertion make this more than a local computation or a relabeling of synchronous Rule 90. It intentionally does not claim a complete Jordan or cycle classification.

## Closest literature and limitations

See the five primary references and detailed statement-versus-implication comparisons in `RESULT.md` and `AUDIT.json`. The accessible 2012 full text was inspected for relevant Rule-90 remarks; its central results concern different update programmability. The 2025/2026 preprint's relevant theorem and argument were inspected in full. Additional unlocated equivalent results, and precise attribution of its disagreement with the recent preprint, remain scientific risks. The independent audit is outstanding.

Self-review: passed. Independent audit: not yet performed.
