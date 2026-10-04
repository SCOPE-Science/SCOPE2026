# The first post-1000 jump of \(M(H)\) occurs at \(H=1215\)
## Finding
Let \(M(H)\) denote the number of ordered triples \((a,b,c)\) of positive integers with \(a,b,c\le H\) for which both \((a,b,c)\) and \((a+1,b+1,c+1)\) are multiplicatively dependent of maximal rank. Then
\[
M(1214)=78,\qquad M(1215)=90.
\]
Up to permutation, the only new triples whose largest coordinate lies in \((1000,1215]\) are
\[
(3,75,1215)\quad\text{and}\quad(15,75,1215).
\]
Hence \(1215\) is the first height above the published \(H=1000\) census at which \(M(H)\) increases.

## Assumptions and scope
For a positive integer \(n>1\), let \(v(n)\) be its vector of prime exponents. A triple is multiplicatively dependent exactly when its three exponent vectors are linearly dependent over \(\mathbb Q\). It has maximal rank exactly when every pair is multiplicatively independent, so the three vectors span a two-dimensional rational plane. A maximal-rank triple cannot contain \(1\), so enumeration may start at \(2\).

The claim is finite and exact only through \(H=1215\). It does not assert that \(M(H)\) is unbounded or describe later jumps.

## Proof
For an independent pair of exponent vectors \(u,v\), form all Pluecker coordinates \(u_i v_j-u_j v_i\), divide them by their common gcd, and choose the sign so that the first nonzero coordinate is positive. This primitive coordinate vector is a canonical key for the rational plane \(\operatorname{span}_\mathbb Q(u,v)\): two independent pairs have the same key exactly when they span the same plane.

Construct the graph whose vertices are the integers \(2,\ldots,1215\), and whose edge \(\{a,b\}\) is labelled by the canonical plane key of \(v(a),v(b)\); multiplicatively dependent pairs have no key. An unordered triple \(a<b<c\) is multiplicatively dependent of maximal rank exactly when its three edges exist and carry one common key. Thus triangles in each key class enumerate every unordered maximal-rank dependent triple without imposing any arbitrary bound on relation exponents. Applying the same exact test to \((a+1,b+1,c+1)\) filters precisely the consecutive triples.

The resulting census contains 15 unordered consecutive maximal-rank triples through \(1215\). Exactly 13 have largest coordinate at most \(1000\), agreeing with the published census, and the only remaining two are \((3,75,1215)\) and \((15,75,1215)\). There is therefore no new unordered triple with largest coordinate from \(1001\) through \(1214\), and exactly two appear at \(1215\). Maximal rank forces three distinct coordinates, so every unordered triple has exactly six orderings. Hence \(M(1214)=6\cdot13=78\) and \(M(1215)=6\cdot15=90\).

For direct witness checks,
\[
1215^2=3^9\cdot75,\qquad 1216=4^2\cdot76,
\]
so both \((3,75,1215)\) and its translate \((4,76,1216)\) are dependent. Likewise,
\[
15^9=75^4\cdot1215,\qquad 1216=16\cdot76,
\]
so the second pair of triples is dependent. Their displayed prime-exponent vectors are pairwise non-proportional, proving maximal rank.

## Verification
Run `python3 verify.py`. The verifier factors every integer through \(1216\), constructs primitive Pluecker keys using exact integer arithmetic, enumerates all key-class triangles through \(H=1215\), applies the same test after translation by \(1\), and checks the four explicit multiplicative identities. Its expected terminal line is:

`VERIFY_OK H=1215 total_unordered=15 le1000=13 new_at_1215=2 M1214=78 M1215=90`

The accompanying `census.json` records the full list of 15 unordered triples. No floating-point arithmetic, probabilistic primality test, or bounded search over multiplicative-relation exponents is used.

## Relationship to prior work
Vukusic and Ziegler reported that there are 13 maximal-rank consecutive triples with \(2\le a<b<c\le1000\). Shparlinski and Sleiman adopted the ordered counting function \(M(H)\), recorded the consequent value \(M(1000)=78\), proved the asymptotic upper bound \(M(H)\le H^{1/2}(\log H)^c\), and explicitly noted that even \(M(H)\to\infty\) is unknown.

The pair \((75,1215)\) itself is not new. It is the known exceptional Benelux pair: \(75\) and \(1215\) have the same prime support, and so do \(76\) and \(1216\). Hercher's 2025 search and OEIS A343101 both record it. What is established here is the exact next boundary for the different triple-counting function: no maximal-rank consecutive triple occurs between the published cutoff and \(1214\), while exactly two unordered triples appear at \(1215\).

## Limitations
This is a finite exact cutoff, not an asymptotic theorem and not evidence by itself that infinitely many such triples exist. The exceptional Benelux pair was previously known, so novelty is limited to its role in the first post-1000 jump and the exhaustive exclusion of all competing triples through \(1214\). Literature searches can miss unindexed computations, and that remains the principal originality risk.

## References
1. I. E. Shparlinski and N. Sleiman, *Counting consecutive multiplicatively dependent triples*, arXiv:2609.29408v1 (2026), first public 24 September 2026; primary MSC 11G30.
2. I. Vukusic and V. Ziegler, *Consecutive tuples of multiplicatively dependent integers*, arXiv:2103.08542 (2021), especially the finite census in Section 3/5.
3. C. Hercher, *On one of Erdős' Problems -- An Efficient Search for Benelux Pairs*, arXiv:2506.01099v1 (2025).
4. OEIS A343101, Benelux pairs; entry containing \((75,1215)\).
