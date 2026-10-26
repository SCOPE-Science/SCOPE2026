# Quadratic-alphabet existence for systematic burst-deletion codes

## Finding

For every pair of integers \(n,t\ge1\), there exists a literal-systematic code \(E(x)=x\Vert p(x)\) from \(\mathcal A^n\) to \(\mathcal A^{n+t+1}\) that corrects every contiguous deletion burst of length at most \(t\), using \(t+1\) deletion-prone trailer symbols, whenever the alphabet size \(q\) is a power of two with \(q>2(n+t+1)^2+1\); the least such power of two satisfies \(q<4(n+t+1)^2+2\).

The construction is existential: it does not provide a pointwise efficient encoder for the trailer map.

## Assumptions and scope

Let \(n,t\ge1\) be integers, let \(\mathcal A\) be an alphabet of power-of-two size \(q\), and put \(M=n+t+1\). A literal-systematic encoder has the form \(E(x)=x\Vert p(x)\), where \(x\in\mathcal A^n\) is transmitted unchanged and \(p(x)\in\mathcal A^{t+1}\) is appended. A burst of length \(r\) deletes \(r\) consecutive coordinates, with \(0\le r\le t\). Correction means that distinct codewords have disjoint descendant sets for each permitted burst length. The claim concerns existence, not efficient evaluation, uniformity in \(n,t\), or optimality of the trailer count for every \(t\).

## Proof

Form a finite graph \(G\) whose vertices are all words in \(\mathcal A^M\). Join two distinct words when they share a descendant after deleting a consecutive block of some length \(r\in\{1,\ldots,t\}\). Partition the vertices into parts

\[
P_x=\{x\Vert s:s\in\mathcal A^{t+1}\},\qquad x\in\mathcal A^n.
\]

Every part has size \(q^{t+1}\). We bound the maximum degree. For a fixed \(r\), write \(B_r=M-r+1\) for the number of possible burst starting positions. A word has at most \(B_r\) distinct length-\(r\)-burst descendants. For a fixed descendant of length \(M-r\), at most \(B_rq^r\) words of length \(M\) can produce it by a length-\(r\) burst deletion: choose the insertion position and the inserted block. Therefore the number of neighbors contributed by length \(r\) is at most \(B_r(B_rq^r-1)\). Since \(B_r\le M\), the maximum degree \(d\) satisfies

\[
d\le\sum_{r=1}^{t}B_r(B_rq^r-1)\le M^2\sum_{r=1}^{t}q^r < \frac{M^2q^{t+1}}{q-1}.
\]

If \(q>2M^2+1\), then \(q-1>2M^2\), so \(d<q^{t+1}/2\). Thus each part has size strictly greater than \(2d\). Haxell's independent-transversal theorem gives an independent set meeting every part once. Its selected word for each prefix \(x\) defines \(p(x)\). Independence rules out a shared descendant after any burst of length \(1\) through \(t\); distinct prefixes handle length zero. Hence the resulting literal-systematic code corrects every burst of length at most \(t\).

Choose \(q\) to be the least power of two strictly greater than \(2M^2+1\). Because \(2M^2+1\) is odd and greater than one, it is not a power of two, so this choice also satisfies \(q<4M^2+2\), as claimed. The argument is a finite graph proof and uses no exhaustive experiment.

## Verification

The degree estimate counts all burst lengths separately and may overcount neighbors; overcounting is safe for the upper bound. The insertion count \(B_rq^r\) is an upper bound because different insertion descriptions can yield the same word. The strict inequality required by the independent-transversal theorem follows from \(q-1>2M^2\). No finite enumeration is used. The proof supplies existence only; it does not make the selected independent transversal efficiently computable from an individual prefix.

## Relationship to prior work

The recent study of literal-systematic deletion codes uses an independent-transversal argument for arbitrary deletion patterns. Its generic degree estimate counts all deletion-position sets, leading to an alphabet bound whose exponent grows with the deletion radius; it separately gives a uniform adjacent-burst construction for length at most two over an alphabet of quartic order. The present graph uses only contiguous bursts, whose length-\(r\) descendant count is at most \(M-r+1\), and includes all lengths \(1\) through \(t\) in one graph. This gives a nonuniform existence bound quadratic in \(M=n+t+1\), independent of \(t\) in the exponent. For \(t=2\) and \(n\ge3\), the three trailer symbols match the known lower bound for the literal-systematic at-most-two-burst model, but the present proof does not give a pointwise efficient encoder.

Earlier non-binary burst-deletion work also discusses systematic constructions, but the stated systematic construction has redundancy \(\log q\log n+O(\log q)\) and does not give a fixed \(t+1\)-symbol trailer over a quadratic-size alphabet. The Haxell theorem is a standard tool; the contribution here is the burst-specific conflict-degree estimate and its consequence for this resource regime.

## Limitations

The result is existential and nonuniform. It does not prove that the quadratic alphabet order is optimal, does not claim that \(t+1\) trailer symbols are necessary for every burst radius \(t>2\), and does not improve the best bit-redundancy bounds for unrestricted (not necessarily literal-systematic) codes. A bounded literature/database search cannot exclude every equivalent result; the principal residual risk is an unindexed prior construction with the same systematicity and alphabet metric.

## References

- Valery, Grishin, and Zabokritskiy, “Systematic Codes Correcting Two Deletions with Three Redundant Symbols over Large Alphabets,” arXiv:2609.38259 (first public version 2026-09-29), especially the generic independent-transversal benchmark and adjacent-burst sections.
- P. E. Haxell and R. Wdowinski, “Degree criteria and stability for independent transversals,” *Journal of Graph Theory* 106 (2024), 352–371, DOI 10.1002/jgt.23085; states the maximum-degree independent-transversal criterion used here.
- Shuche Wang, Yuanyuan Tang, Jin Sima, Ryan Gabrys, and Farzad Farnoud, “Non-binary Codes for Correcting a Burst of at Most \(t\) Deletions,” arXiv:2210.11818 (2022), for the different bit-redundancy regime.
