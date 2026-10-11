# Review

## Correctness
PASS. The source supplies the two possible finite-return symbolic left endpoints and the negative-doubling address map. Iterating the address recursion through a length-\(k\) prefix gives slope \((-1/2)^k\). In the even case \(\beta=w\beta\) and \(L=w\alpha\), so subtraction gives \(b-b_*=2^{-k}(b-a)\). In the odd case \(\beta=w\alpha\) and \(L=w^\infty\); solving the fixed-point equation for \(\pi_{-2}(w^\infty)\) gives \(b-b_*=(b-a)/(2^k+1)\). The source singleton case handles \(k=\infty\). The proof does not extrapolate from experiments.

## Originality
PASS. The closest primary source, arXiv:2610.03327v1, states the parity-sensitive symbolic plateau endpoints and the address map but does not state the resulting Euclidean boundary-gap formulas or their normalized parity law. Searches using negative-doubling, decreasing-Lorenz, survivor-plateau, return-time, endpoint-width, and negative-beta aliases found no implication-equivalent published-finding corpus record or published statement. Earlier increasing-Lorenz hole work is qualitatively related but does not dominate this negative-doubling parity formula. Residual risk remains that the affine calculation may have appeared as an unstated or differently worded folklore observation.

## Value
PASS. The source proves a devil's-staircase phenomenon but its plateau theorem is symbolic. The new formula assigns an exact Euclidean scale to every nontrivial finite-return plateau in the class, solely from the dynamical return depth and its parity. This provides a natural quantitative invariant for comparing plateaux and makes the parity distinction geometrically visible rather than only combinatorial.

## Closest literature and limitations
Ding--Steiner--Sun is the direct source for the symbolic classification and address map. Sun--Li--Ding (arXiv:2311.02465) treats hole plateaux for increasing expansive Lorenz maps and is background rather than a covering result. The claim is restricted to the source's weak-admissible finite-return class; it does not classify arbitrary plateau measures or frequencies, and precritical dual coding can affect endpoint names but not coordinate width.

Same-model review: passed. Independent audit: not yet performed.
