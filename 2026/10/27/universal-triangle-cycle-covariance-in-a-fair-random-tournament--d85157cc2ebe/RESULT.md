# Universal triangle–cycle covariance in a fair random tournament

## Finding
Fix integers \(n\ge3\) and \(3\le k\le n\). Give every pair of distinct vertices in \([n]\) one of its two directions, independently with probability \(1/2\) each. Let \(T\) be the number of directed cyclic triangles, and let \(C_k\) be the number of directed simple cycles of length \(k\), identifying cycles only under rotation of the starting vertex. In particular, opposite cyclic directions are separate possible cycles, though they cannot both occur on one undirected cycle.

The exact mixed-moment identity is

\[
\boxed{\operatorname{Cov}(T,C_k)=\frac{k}{4}\mathbb E C_k=\frac{(n)_k}{4\,2^k}>0,\qquad 3\le k\le n.}
\]

Here \((n)_k=n(n-1)\cdots(n-k+1)\). For any *specified* oriented simple cycle of length \(k\), the conditional expectation of \(T\) exceeds its unconditional expectation by exactly \(k/4\), with no dependence on the number of vertices outside the cycle.

Consequently every directed-cycle count satisfies the finite-sample relative variance bound

\[
\boxed{\frac{\operatorname{Var}(C_k)}{(\mathbb E C_k)^2}\ge\frac{k^2}{3\binom n3}.}
\]

Equality holds for \(k=3\). In the Hamiltonian case \(k=n\), the right-hand side equals \(2n/((n-1)(n-2))\), asymptotic to \(2/n\).

## Assumptions and scope
The underlying graph is the complete simple graph with exactly \(n\) labeled vertices. Every unordered pair is oriented independently and uniformly. The cycles counted by \(C_k\) have distinct vertices and consistently directed edges; arbitrary closed walks and undirected cycles are not counted. A cyclic triangle is counted once, not three times by starting position. The claim holds for every finite pair \((n,k)\) satisfying \(n\ge3\) and \(3\le k\le n\), without a sparsity or asymptotic assumption.

## Proof
**1. The local triangle law.** A random orientation of the three edges of a fixed triangle is cyclic in exactly two of the eight equiprobable states. Therefore \(\mathbb E T=\binom n3/4\). Conditional on the orientation of any *one* of its edges, its probability of being cyclic remains \(1/4\): one of the four completions is cyclic. Conditional instead on a specified oriented directed path of two edges, the remaining edge closes a cyclic triangle with probability \(1/2\).

**2. Conditioning on one prescribed directed cycle.** Select pairwise distinct vertices \(v_1,\ldots,v_k\) and let \(A\) be the event that \(v_1\to v_2\to\cdots\to v_k\to v_1\). It has probability \(2^{-k}\). For \(k\ge4\), exactly \(k\) vertex triples contain two edges of this specified cycle: the triples \(\{v_i,v_{i+1},v_{i+2}\}\), indexed cyclically. Their prescribed edges form a directed two-edge path; the missing chord remains fair, giving conditional cyclic probability \(1/2\), rather than \(1/4\). All other triples contain at most one prescribed cycle edge, so the local triangle law says their conditional cyclic probability remains \(1/4\). Hence \(\mathbb E[T\mid A]-\mathbb ET=k(1/2-1/4)=k/4\).

For \(k=3\), the only fully prescribed vertex triple is itself the directed triangle; its conditional cyclic probability is \(1\) rather than \(1/4\). Every other triple has at most one prescribed edge. Therefore \(\mathbb E[T\mid A]-\mathbb ET=3/4=k/4\), proving the same response at the boundary.

**3. Summing over all candidate cycles.** There are \((n)_k/k\) distinct ordered, cyclically oriented candidate \(k\)-cycles, after quotienting the starting-point rotation but not identifying reversal. Their indicator events each have probability \(2^{-k}\). Let \(I_A\) denote a candidate's event indicator. Linearity gives

\[
\mathbb E C_k=\frac{(n)_k}{k\,2^k},\qquad
\operatorname{Cov}(T,C_k)
=\sum_A \mathbb P(A)\bigl(\mathbb E[T\mid A]-\mathbb ET\bigr)
=\frac{(n)_k}{k\,2^k}\frac{k}{4}.
\]

No independence between different candidate-cycle events is assumed or needed.

**4. Variance bound.** Taking \(k=3\) in the mixed-moment identity yields \(\operatorname{Var}(T)=3\mathbb ET/4=3\binom n3/16\). Cauchy–Schwarz now gives

\[
\operatorname{Var}(C_k)\ge
\frac{\operatorname{Cov}(T,C_k)^2}{\operatorname{Var}(T)}
=\frac{k^2(\mathbb EC_k)^2}{3\binom n3}.
\]

For \(k=3\) the two random variables in this inequality are identical, so equality holds.

## Verification
Run the included `verify.py` with Python 3 (standard library only). It exhaustively enumerates every tournament on three through six vertices and computes independent integer sums for the means and all mixed moments for each available cycle length. It also enumerates the remaining fair arc orientations on seven vertices after prescribing a directed cycle of length five, six, or seven; it independently checks the claimed \(k/4\) conditional response. The program prints `PASS 37 exact equalities` and raises an assertion error on failure. These finite checks supplement, but do not replace, the proof for all \(n\) and \(k\).

## Relationship to prior work
Linial and Morgenstern (2014) study extremal feasible relations between counts of cyclic triples and four-cycles in *deterministic* tournaments; their exact four-vertex counting identities do not give mixed moments of a fair random tournament for all lengths. Chan, Grzesik, Král', and Noel (2019) extend the extremal problem, and Grzesik, Král', Lovász, and Volec (2020) derive cycle expectations and extremal cycle densities for arbitrary lengths; the relevant statements do not assert the uniform finite covariance identity or the resulting lower bound on relative variance. Janson (1995) proves asymptotic normality for Hamiltonian-cycle counts in a random tournament; this is a pertinent fluctuation predecessor, but the complete text was not available for comparison and may contain special-case moment identities. The all-length finite identity is not a consequence of the cited marginal means or extremal bounds alone.

## Limitations
This theorem is about first mixed moments only: it does not imply stochastic dominance, positive association, or a joint central limit theorem. The variance inequality is a lower bound, not an exact formula for \(\operatorname{Var}(C_k)\) when \(k>3\). Historical priority remains subject to comparison with inaccessible earlier full texts, especially Hamiltonian-cycle work and pre-1995 tournament cycle enumeration. Mathematical correctness has not been independently audited.

## References
1. N. Linial and A. Morgenstern, *On the number of 4-cycles in a tournament*, arXiv:1405.1576, first posted 2014-05-07. https://arxiv.org/abs/1405.1576
2. T. F. N. Chan, A. Grzesik, D. Král', and J. A. Noel, *Cycles of length three and four in tournaments*, arXiv:1902.00572, first posted 2019-02-01. https://arxiv.org/abs/1902.00572
3. A. Grzesik, D. Král', L. M. Lovász, and J. Volec, *Cycles of a given length in tournaments*, arXiv:2008.06577, first posted 2020-08-14. https://arxiv.org/abs/2008.06577
4. S. Janson, *Hamilton cycles in a random tournament*, Random Structures & Algorithms 6 (1995), 213–220. https://doi.org/10.1002/rsa.3240060209
