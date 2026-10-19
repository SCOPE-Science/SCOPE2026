# Exact covariance geometry and variance inflation of reverse-complementary DNA stems

## Finding

Let a uniformly random length-\(n\) word be sampled from an even-sized alphabet of \(q\ge2\) letters with a fixed-point-free involutive complement. For stem length \(m\ge1\) and minimum separation \(g\ge0\), count all ordered pairs of **disjoint** length-\(m\) factors separated by at least \(g\) letters such that one factor is the reverse complement of the other. Denote this random count by \(H\).

Write \(B(r)=r(r-1)/2\) if \(r\ge2\), and \(B(r)=0\) otherwise. For all integers \(n\ge0\), \(m\ge1\), and \(g\ge0\),
\[
\mathbb E H=B(n-2m-g+2)q^{-m},
\]
\[
\operatorname{Var}(H)=B(n-2m-g+2)q^{-m}(1-q^{-m})
+2\sum_{d=1}^{m-1}B(n-2m-g-2d+2)(q^{-(m+d)}-q^{-2m}).
\]

More precisely, indicators for two distinct candidate stem pairs are **independent whenever their reflection centers differ**, irrespective of overlapping support positions. At the same center, the only dependent pairs are those shifted by a distance \(d\) satisfying \(1\le d<m\). Their covariance is exactly \(q^{-(m+d)}-q^{-2m}\). Thus the entire covariance matrix has a sparse, explicitly described support.

For fixed \(q,m,g\) as \(n\to\infty\), the ratio \(\operatorname{Var}(H)/\mathbb EH\) tends to
\[
1+2\sum_{d=1}^{m-1}q^{-d}-(2m-1)q^{-m}.
\]
For fixed \(q\), the successive \(m\to\infty\) limit of this constant is \((q+1)/(q-1)\), revealing persistent variance inflation above the independent-event prediction. For quaternary DNA, \(m=2,g=0\) gives the exact example
\[
\operatorname{Var}(H)=\frac{15B(n-2)+6B(n-4)}{256},
\]
with large-\(n\) variance-to-mean ratio \(21/16\).

## Assumptions and scope

Let \(\mathcal A\) be a finite alphabet with even cardinality \(q\ge2\). Let \(a\mapsto\overline a\) be an involution without fixed points. The random symbols \(W_1,\ldots,W_n\) are independent and uniform on \(\mathcal A\). For integers \(1\le i<j\le n-m+1\) with \(j-i\ge m+g\), set \(X_{i,j}=1\) precisely if
\[
W_{i+r}=\overline{W_{j+m-1-r}}\quad(0\le r<m).
\]
All indices are one-based in this display. Define \(H=\sum_{i,j}X_{i,j}\). Each candidate starting-position pair is counted once; different candidates matching the same letters are still separate possible stems. A loop means the intervening region of at least \(g\) unpaired symbols, with \(g=0\) permitted. The claim concerns perfect complementary stems as candidates, *not* a selected RNA/DNA fold.

## Proof

**1. One-stem probability and count.** The \(m\) disjoint position pairs of a stem are constraints \(W_u=\overline{W_v}\), each with probability \(1/q\). Thus \(\Pr(X_{i,j}=1)=q^{-m}\). The number of candidate pairs is \(B(n-2m-g+2)\), obtained by replacing \(j-i\ge m+g\) with the nonnegative difference of two ordered start positions. This proves the expectation.

**2. Distinct-center independence.** Each stem at starts \((i,j)\) imposes \(m\) edges between positions, with reflection center (sum of endpoint indices) \(c=i+j+m-1\). Its edges all satisfy \(u+v=c\) and form a matching, because its two blocks are disjoint. For any two stems of distinct centers \(c\ne c'\), their joint constraint graph is the union of two matchings; if it had a cycle, the two edge colors would alternate. Two consecutive reflections on the integer line, \(u\mapsto c-u\) then \(u\mapsto c'-u\), translate by the nonzero integer \(c'-c\). A nonzero translation has no finite orbit, so such a cycle cannot exist. The graph is therefore a forest with exactly \(2m\) distinct edges. For a forest with \(e\) complement-edges, uniform independent labels satisfy all constraints with probability \(q^{-e}\), since choosing one root label per component fixes the rest uniquely. Therefore \(\Pr(X_{i,j}=X_{k,l}=1)=q^{-2m}\), proving independence at distinct centers.

**3. Same-center covariance.** If the centers agree and the start pairs differ, write their left starts as \(i\) and \(i+d\), \(d>0\), and their right starts as \(j\) and \(j-d\). The associated sets of reflected edges are equal up to a shift of their left intervals. For \(d<m\), they share exactly \(m-d\) edges, so the union has \(m+d\) edges, all belonging to a single matching and hence simultaneously satisfiable with probability \(q^{-(m+d)}\). If \(d\ge m\), the sets have no common edges, giving probability \(q^{-2m}\). Subtracting the product of marginal probabilities proves the covariance classification.

**4. Count dependent pairs and sum.** At fixed shift \(d\ge1\), the two candidates \((i,j)\) and \((i+d,j-d)\) are both admissible exactly when \(j-i\ge m+g+2d\). Their number is \(B(n-2m-g-2d+2)\), and the chosen orientation \(d>0\) counts each unordered pair of distinct candidates exactly once. The identity \(\operatorname{Var}(\sum X)=\sum\operatorname{Var}(X)+2\sum_{e<f}\operatorname{Cov}(X_e,X_f)\) now yields the displayed exact variance.

**5. Asymptotics.** For fixed \(m,g,d\), \(B(n-a)/B(n-b)\to1\) as \(n\to\infty\). Divide the variance identity by the expectation and simplify; finally use \(\sum_{d=1}^{m-1}q^{-d}\to1/(q-1)\), while \(mq^{-m}\to0\), to obtain the successive limit. The quaternary example is direct substitution into the exact formula.

## Verification

Run `python3 verify.py` from the same extracted package directory. It enumerates small uniform alphabets and checks rational first and second moments independently; a parity-union-find computation checks the joint constraint rank and center-based covariance law. The finite verification complements but is not substituted for the proof above. Its source and all dependencies (Python standard library only) are included.

## Relationship to prior work

Nguyen et al., *On the Design of Codes for DNA Computing: Secondary Structure Avoidance Codes* (2023), and Chu, Wang and Zhang, *Improved constructions of secondary structure avoidance codes for DNA sequences* (2023), use forbidden reverse-complementary stems to construct and bound codes. Their inspected treatments concern avoidance, redundancy and rate, rather than a second-moment null law for the number of candidate stems. Fitch (1983) investigates expected frequencies of potential secondary structures (with base composition and other parameters), which is closer to the mean than to the present full pairwise covariance classification; its complete full text could not be obtained here. A published random-word matching-variance study by Burden et al. concerns approximate matches between two independent sequences, not the one-word anti-diagonal dependence classified here. The originality comparison is conditioned on the inspected sources and is not a claim of exhaustive literature coverage.

## Limitations

The symbols are iid and uniform, the alphabet complement has no fixed points, and the stems are exact matches; nonuniform base composition, stacking energies, mismatch/wobble pairing and structural folding constraints are outside this claim. The proof gives exact first two moments and pairwise independence for many candidate pairs, not mutual independence or a distributional limit. The displayed limiting ratio takes \(n\to\infty\) before \(m\to\infty\). Older primary literature on expected stem counts could not all be examined in full, and independent review has not been performed.

## References

- T. H. Nguyen, K. Cai, H. M. Kiah, T. T. Dao and K. A. S. Immink, *On the Design of Codes for DNA Computing: Secondary Structure Avoidance Codes*, arXiv:2302.13714v1, first posted 2023-02-27.
- H. Chu, T. Wang and Z. Zhang, *Improved constructions of secondary structure avoidance codes for DNA sequences*, arXiv:2304.11403v1, first posted 2023-04-22.
- W. M. Fitch, *Calculating the expected frequencies of potential secondary structure in nucleic acids as a function of stem length, loop size, base composition and nearest-neighbor frequencies*, Nucleic Acids Research 11 (1983), DOI:10.1093/nar/11.13.4655.
- C. J. Burden, S. S. Kantorovitz and S. R. Wilson, *Approximate word matches between two random sequences*, 2008, DOI:10.1214/07-AAP452. This concerns a different random-matching model.
