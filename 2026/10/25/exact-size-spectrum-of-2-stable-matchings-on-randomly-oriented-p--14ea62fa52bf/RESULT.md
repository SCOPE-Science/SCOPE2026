# Exact size spectrum of \(2\)-stable matchings on randomly oriented preference cycles

## Finding
For every integer \(n\ge3\), let \(S_{n,j}\) be the number of \(2\)-stable matchings with exactly \(j\) edges on the labeled cycle \(C_n\), where each vertex independently chooses one of the two strict orders on its neighbors with probability \(1/2\), and ranks itself last. For every integer \(0\le j\le\lfloor n/2\rfloor\),
\[
\mathbb E[S_{n,j}]=2^{1-n}4^j\binom{n}{2j}.
\]
Hence the **entire annealed size polynomial** is
\[
\mathbb E\!\left[\sum_{j\ge0}S_{n,j}z^j\right]
=2^{1-n}\sum_{j=0}^{\lfloor n/2\rfloor}\binom{n}{2j}(4z)^j
=2^{-n}\big((1+2\sqrt z)^n+(1-2\sqrt z)^n\big).
\]
This last expression is a polynomial: its odd powers of \(\sqrt z\) cancel. In particular,
\[
\mathbb E\!\left[\sum_jS_{n,j}\right]
=(3/2)^n+(-1/2)^n.
\]

## Assumptions and scope
The graph is the simple, undirected, labeled cycle with vertices \(0,\ldots,n-1\), and edge \(i\) joining \(i\) and \(i+1\) modulo \(n\). The two incident neighbors are distinct because \(n\ge3\). Each agent has a strict rank function with its favorite neighbor ranked \(1\), its other neighbor ranked \(2\), and remaining unmatched ranked \(3\). All \(2^n\) preference profiles have probability \(2^{-n}\). A matching is any set of disjoint cycle edges, not necessarily perfect. A \(2\)-blocking pair is an unchosen cycle edge whose two endpoints each improve their partner rank by at least \(2\) after forming this pair. The claims apply simultaneously to every valid integer size \(j\).

## Proof
**Blocking-pair reduction.** A matched vertex has partner rank \(1\) or \(2\), so the maximum possible rank improvement from switching to another neighbor is at most \(1\). An unmatched vertex has rank \(3\), and gains at least \(2\) precisely when the proposed neighbor is ranked \(1\). Therefore an edge is \(2\)-blocking if and only if both endpoints are unmatched and each ranks the other first.

**Transfer encoding.** Encode a matching by edge indicators \(e_i\in\{0,1\}\), where \(e_i=1\) selects edge \(i\), and each vertex's order by \(o_i\in\{0,1\}\), with \(o_i=1\) favoring its clockwise neighbor and \(o_i=0\) favoring its counterclockwise neighbor. Matching feasibility requires \(e_{i-1}e_i=0\). By the preceding reduction, the edge joining \(i\) to \(i+1\) is blocking exactly when
\[
e_{i-1}=e_i=e_{i+1}=0,\qquad(o_i,o_{i+1})=(1,0).
\]
These are the only forbidden local patterns.

Use the six states \((a,b,o)\) with \(a,b,o\in\{0,1\}\) and \(ab=0\), in the order
\[
(0,0,0),(0,0,1),(0,1,0),(0,1,1),(1,0,0),(1,0,1).
\]
A transition \((a,b,o)\to(b,c,o')\) is permitted exactly when \(bc=0\) and \((a,b,c,o,o')\ne(0,0,0,1,0)\); assign transition weight \(z^c\). In the displayed state order its transfer matrix is
\[
T(z)=\begin{pmatrix}
1&1&z&z&0&0\\
0&1&z&z&0&0\\
0&0&0&0&1&1\\
0&0&0&0&1&1\\
1&1&z&z&0&0\\
1&1&z&z&0&0
\end{pmatrix}.
\]
For a labeled cyclic sequence, assigning state \((e_{i-1},e_i,o_i)\) at position \(i\) is a bijection between admissible pairs (a preference profile, a \(2\)-stable matching) and length-\(n\) closed walks through these states. The product of edge weights is \(z^{\sum_i e_i}\). Thus **without rotational division**,
\[
\sum_{\omega\in\{0,1\}^n}\sum_{M:\,\text{2-stable under }\omega}z^{|M|}
=\operatorname{tr}(T(z)^n).
\]

**Exact spectral calculation.** Direct determinant expansion, or elementary elimination, gives the polynomial identity
\[
\det(\lambda I-T(z))=\lambda^4\big((\lambda-1)^2-4z\big).
\]
The trace of the positive integer power of a square matrix equals the sum of the same powers of its eigenvalues counted with algebraic multiplicity, even if the matrix is not diagonalizable. Since \(n\ge3\), the four zero eigenvalues contribute nothing, and therefore
\[
\operatorname{tr}(T(z)^n)=(1+2\sqrt z)^n+(1-2\sqrt z)^n
=2\sum_{j=0}^{\lfloor n/2\rfloor}\binom{n}{2j}4^jz^j.
\]
Comparing coefficients of \(z^j\) yields exactly \(2\cdot4^j\binom{n}{2j}\) successful (preference-profile, matching) pairs of size \(j\). Dividing by \(2^n\) establishes all assertions. \(\square\)

## Verification
The standalone `verify_cycle_k2.py` directly enumerates all matchings and all preference profiles for each \(n=3,\ldots,11\), computing blocking moves from the original rank-difference definition independently of the transfer construction. For each feasible size \(j\), the resulting integer count agrees with \(2\cdot4^j\binom{n}{2j}\). The same program independently constructs the six-state matrix and compares traces with the proposed polynomial identity at \(z\in\{0,1,2,3,7\}\) for powers \(1\) through \(16\). The accompanying `checks.txt` contains the actual output. These finite checks corroborate the proof but are not its source of universal validity; the displayed bijection and characteristic polynomial prove the all-\(n\) theorem.

## Relationship to prior work
Fanelli and Moscardelli, *Approximately Stable Matching*, introduce the exact rank-improvement \(k\)-blocking definition and analyze existence, dynamics, and graph-topology effects. For cycle degree \(2\), their general sufficient \(k=2\) existence bound does not supply the number of \(2\)-stable solutions or their size spectrum under independently random local preferences. Pittel and Rudov, *Stable matchings under relaxed random preferences*, study counts in a different full bipartite model and a different relaxation governed by \(\varepsilon\); their first-moment results do not imply the cycle formulas. A separate literature comparison of finite classical stable-roommates censuses and matching-complex cycle enumerations found no direct coverage. This is a best-knowledge literature comparison, not a claim of exhaustive publication priority.

## Limitations
The expectation averages over profiles, and does not determine the variance, concentration, or typical (quenched) number of stable matchings. The identity uses independent uniformly random binary orders, cycle acceptability, degree exactly \(2\), and the rank-distance threshold exactly \(2\); it does not by itself extend to other thresholds, topologies, or correlated preferences. No claim is made about strategic mechanisms or adjustment dynamics. Priority uncertainty remains for unindexed or previously circulated exact enumerations. The primary conference volume is labeled 2025, whereas its accessible publisher page expressly dates first publication online to 2026-08-25; earlier public versions could exist.

## References
1. Angelo Fanelli and Luca Moscardelli, *Approximately Stable Matching*, ECAI 2025 proceedings, first published online 2026-08-25, DOI: https://doi.org/10.3233/FAIA251234 . Full text: https://journals.sagepub.com/doi/10.3233/FAIA251234 .
2. Boris Pittel and Kirill Rudov, *Stable matchings under relaxed random preferences*, International Journal of Game Theory 55, article 43 (2026), published 2026-10-09. DOI: https://doi.org/10.1007/s00182-026-01016-x .
