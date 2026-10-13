# Three-step overlap Bernoulli entropy is always strictly concave
## Finding
Let \(a_1=2<a_2<a_3\) be arbitrary integers and let \(P_3(p)\) be the third recursive overlap Bernoulli distribution of Neunhäuserer. Its Shannon entropy \(h_3(p)\) is strictly concave for \(0<p<1\). Consequently \(h_3\) is concave on \([0,1]\), symmetric about \(p=1/2\), and has the unique maximum \(p=1/2\).

Writing
\[
d_1=a_2-a_1,\qquad d_2=a_3-a_2,
\]
the source's moment-generating-function factorization shows, up to an irrelevant additive shift and the symmetry \(p\leftrightarrow1-p\), that the problem is exactly the entropy of
\[
S=B_1+d_1B_2+d_2B_3,
\]
where \(B_1,B_2,B_3\) are independent Bernoulli variables with common parameter \(p\).

This proves the source's entropy-concavity conjecture for every admissible sequence at \(n=3\). Levels \(n=1\) and \(n=2\) are already forced into the source's two proved extremal regimes, so \(n=3\) is the first level at which a genuinely overlapping unresolved configuration can occur.

## Assumptions and scope
All logarithms are natural; changing the logarithm base only multiplies entropy by a positive constant. The increments \(d_1,d_2\) are arbitrary positive integers. No regularity or growth assumption is imposed on the sequence beyond \(2=a_1<a_2<a_3\).

Define the binary entropy and Bernoulli variance factor by
\[
h(p)=-p\log p-(1-p)\log(1-p),
\qquad
s=p(1-p).
\]
Since an additive shift does not change entropy, and complementing all three Bernoulli bits reflects the weighted sum without changing entropy, it suffices to study the weighted sum displayed above.

## Proof
Permuting the three iid Bernoulli coordinates does not change the law of the weighted sum up to relabeling the weights. Sort the weight multiset as
\[
\{1,u,v\},\qquad 1\le u\le v.
\]
The eight subset sums can collide only when \(u=1\), \(v=u\), or \(v=u+1\). Indeed, apart from equal weights, the only possible equality between two distinct subset sums of three positive ordered weights is that the largest weight equals the sum of the other two.

Thus every weight triple belongs to exactly one of the following entropy types.

If all eight subset sums are distinct, no information is lost by the weighted-sum map, so
\[
H(S)=3h(p).
\]

If all three weights equal one, the law is binomial of order three. Merging the three one-success configurations and the three two-success configurations loses \(3s\log3\) units of entropy, hence
\[
H(S)=3h(p)-3s\log3.
\]

If exactly two weights coincide and there is no further subset-sum collision, namely \(\{1,1,v\}\) with \(v\ge3\) or \(\{1,u,u\}\) with \(u\ge2\), the only information loss comes from exchanging the equal-weight Bernoulli coordinates. The two merged pairs together lose \(2s\log2\), so
\[
H(S)=3h(p)-2s\log2.
\]

If all weights are distinct and \(v=u+1\), with \(u>1\), exactly two configurations collide: selecting the largest weight alone and selecting the two smaller weights. Their total mass is \(s\), and, conditional on that merged value, their relative probabilities are \(p\) and \(1-p\). The entropy loss is therefore \(s h(p)\), giving
\[
H(S)=(3-s)h(p).
\]

The remaining exceptional pattern is \(\{1,1,2\}\). It has both the equal-weight mergers and the single additive collision, so
\[
H(S)=(3-s)h(p)-2s\log2.
\]

These formulas exhaust all positive integer weight triples.

It remains to check strict concavity. On \(0<p<1\),
\[
h''(p)=-\frac1s,
\qquad
0<s\le\frac14,
\qquad
h(p)\le\log2.
\]
Hence
\[
\bigl(3h(p)\bigr)''=-\frac3s<0,
\]
\[
\bigl(3h(p)-2s\log2\bigr)''
=-\frac3s+4\log2
\le -12+4\log2<0,
\]
and
\[
\bigl(3h(p)-3s\log3\bigr)''
=-\frac3s+6\log3
\le -12+6\log3<0.
\]

For
\[
G(p)=(3-s)h(p),
\]
direct differentiation gives
\[
G''(p)
=
2h(p)
+
2(2p-1)\log\frac{1-p}{p}
+
1-\frac3s.
\]
The middle term is nonpositive because \(2p-1\) and \(\log((1-p)/p)\) have opposite signs. Therefore
\[
G''(p)
\le
1+2\log2-12
=
-11+2\log2<0.
\]
Finally,
\[
\bigl(G(p)-2s\log2\bigr)''
=
G''(p)+4\log2
\le
-11+6\log2<0.
\]
Every possible entropy formula is therefore strictly concave on \((0,1)\).

Continuity at \(p=0,1\) extends concavity to the closed interval. The source already proves the symmetry \(h_3(p)=h_3(1-p)\); strict concavity then makes \(p=1/2\) the unique maximizer.

## Verification
The subset-sum classification was checked directly from
\[
0,1,u,v,1+u,1+v,u+v,1+u+v.
\]
For \(1\le u\le v\), any nontrivial collision is forced by \(u=1\), \(u=v\), or \(v=u+1\), yielding exactly the five entropy types in the proof.

The entropy-loss formulas were replayed from the eight Bernoulli configurations. Equal-probability two-state mergers lose the merged mass times \(\log2\); equal-probability three-state mergers lose the merged mass times \(\log3\). In the additive collision, the merged mass is \(s\) and the conditional split is Bernoulli with parameter \(p\), so the loss is exactly \(s h(p)\).

The curvature bounds use only \(s\le1/4\), \(h(p)\le\log2\), and
\[
(2p-1)\log\frac{1-p}{p}\le0.
\]
No finite enumeration or numerical grid is used as proof.

## Relationship to prior work
Neunhäuserer introduced the recursive overlap Bernoulli family and conjectured that \(h_n(p)\) is concave for every strictly increasing sequence. The source proves the conjecture only in the binomial regime \(a_n=n+1\) and in the non-overlapping regime \(a_{n+1}\ge2a_n\), and reports computational evidence for other sequences. Its full text explicitly says that no proof is known there for the remaining overlapping cases. The first public version is arXiv:2609.05546v1, dated 2 September 2026, with primary MSC 60C05.

The present result handles every admissible sequence at \(n=3\), including the first partial-overlap patterns not covered by those two extremal proofs. For example, weights \(\{1,2,3\}\) have the additive collision \(3=1+2\), while \(\{1,1,2\}\) has both a repeated weight and an additive collision; both are covered by the exact formulas above.

Li's recent work on weighted Bernoulli sums studies multiplicative comparisons between Rényi entropies for uniform Bernoulli vectors. Its inspected full text fixes the Bernoulli parameter at \(1/2\) and explicitly notes that its main coupling does not directly extend to biased Bernoulli variables. It does not establish common-parameter Shannon-entropy concavity. The classical Shepp–Olkin theorem covers ordinary unweighted Bernoulli sums, not these weighted subset-sum collisions.

Focused searches for weighted-Bernoulli, subset-sum, three-weight, and recursive-overlap entropy concavity found no theorem dominating the \(n=3\) result.

## Limitations
The proof is complete only for the third recursive level. It does not prove the conjecture for \(n\ge4\), where several independent subset-sum collisions can interact and the five-type classification no longer applies.

The result concerns Shannon entropy as the common Bernoulli parameter varies. It does not establish analogous concavity for other Rényi orders, independently varying Bernoulli parameters, arbitrary real weights at higher dimension, or infinite Bernoulli convolutions. An equivalent older three-weight entropy result under different subset-sum terminology remains a residual literature risk.

## References
1. J. Neunhäuserer, *Recursive overlap Bernoulli distributions and an entropy concavity conjecture*, arXiv:2609.05546v1, 2 September 2026.
2. J. Li, *Multiplicative comparisons of Rényi entropies for weighted Bernoulli sums*, arXiv:2609.01529v1, 1 September 2026.
3. L. Shepp and I. Olkin, *Entropy of the sum of independent Bernoulli random variables and of the multinomial distribution*, Proceedings of the Sixth Berkeley Symposium, 1972.
