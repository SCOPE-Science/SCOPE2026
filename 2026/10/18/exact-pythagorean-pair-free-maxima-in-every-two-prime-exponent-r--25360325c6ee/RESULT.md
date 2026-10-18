# Exact Pythagorean-pair-free maxima in every two-prime exponent rectangle

## Finding
For positive integers \(A,B\), put
\[
T_{A,B}=\{2^a3^b:0\le a<A,\ 0\le b<B\}.
\]
Call a subset admissible if there do not exist distinct \(x,y\) in that subset and a positive integer \(z\) with \(x^2+y^2=z^2\). Define, for integers \(0\le w\le A+2B-3\),
\[
L_w=\max\!\left(0,\min\!\left(B-1,\left\lfloor\frac w2\right\rfloor\right)-\max\!\left(0,\left\lceil\frac{w-A+1}{2}\right\rceil\right)+1\right).
\]
The exact maximum admissible cardinality and exact number of maximizing subsets are
\[
\alpha(A,B)=\sum_{w=0}^{A+2B-3}\left\lceil\frac{L_w}{2}\right\rceil,
\qquad
\mathcal M(A,B)=\prod_{\substack{w:L_w>0\\2\mid L_w}}\left(\frac{L_w}{2}+1\right).
\]
In particular, every positive integer \(N\) satisfies
\[
\alpha(N,N)=
\begin{cases}
N(N+1)/2,&N\equiv0\pmod4,\\
N(N+2)/2,&N\equiv2\pmod4,\\
(2N^2+3N-1)/4,&N\equiv1\pmod4,\\
(2N^2+3N+1)/4,&N\equiv3\pmod4.
\end{cases}
\]

## Assumptions and scope
The prime support is fixed at \(\{2,3\}\); exponent bounds \(A,B\) vary independently through all positive integers. The hypotenuse \(z\) is any positive integer, not required to lie in the box. Every factor in the count \(\mathcal M\) corresponds to a component with an even number of vertices; an empty product equals one. No assumption is made about primality of the hypotenuse.

## Proof
**The only primitive Pythagorean pair with both positive legs supported on the primes \(2,3\) is \(\{3,4\}\).** For a hypothetical pair, divide both legs and the hypotenuse by the gcd of the legs. Since the normalized coprime legs cannot both be odd, one is odd and one even. If the odd leg equals one, then \(z^2-y^2=1\), so \((z-y)(z+y)=1\), impossible for a positive even leg \(y\). Thus the odd leg equals \(3^\beta\) for some \(\beta\ge1\). Coprimality forces the even leg to equal \(2^\alpha\), \(\alpha\ge1\). When \(\alpha=1\), the square equation reduces to \(5\pmod8\), impossible. Thus \(\alpha\ge2\). The hypotenuse is odd and coprime to three; therefore
\[
(z-3^\beta)(z+3^\beta)=2^{2\alpha},\qquad\gcd(z-3^\beta,z+3^\beta)=2.
\]
Both factors are positive even powers of two. Since their gcd is two, they must be \(2\) and \(2^{2\alpha-1}\), respectively. Subtracting gives
\[
3^\beta=2^{2\alpha-2}-1.
\]
If \(\alpha\ge3\), the right side is seven modulo eight, whereas powers of three are one or three modulo eight; contradiction. Hence \(\alpha=2\) and \(\beta=1\), giving \(3,4,5\). Conversely, \(3^2+4^2=5^2\).

It follows that **every forbidden pair**, and no other pair, has the form \(\{3d,4d\}\) for a positive integer \(d\) supported on \(\{2,3\}\). Put \(d=2^i3^j\). The two exponent vectors are \((i,j+1)\) and \((i+2,j)\). In the exponent rectangle, connect any two vectors related by \((a,b)\mapsto(a+2,b-1)\). This graph has no other edges.

The weight \(w=a+2b\) is preserved along each edge. For a fixed \(w\), the admissible points \((a,b)\) satisfy \(b\in[0,B-1]\), \(a=w-2b\in[0,A-1]\). They form a consecutive integer interval in \(b\) with exactly \(L_w\) points; consecutive points are connected. Thus the forbidden-pair graph is the disjoint union of **paths of order \(L_w\)**, including singleton paths. On a path of \(L\) vertices, the maximum independent-set cardinality is \(\lceil L/2\rceil\). If \(L=2k+1\), its maximizing independent set is uniquely the odd-position vertices. If \(L=2k\), its maximizing independent sets are exactly the \(k+1\) choices determined by the position of the one doubled gap among its selected vertices (equivalently, the standard count of \(k\)-subsets of a path of order \(2k\) with no adjacencies). Independent choices across paths prove both formulas.

For the square case \(A=B=N\), write \(O_N\) for the number of weights with odd \(L_w\). Since the total of all path orders is \(N^2\), \(\alpha(N,N)=(N^2+O_N)/2\). Directly from the interval count, the left flank weights \(w=0,\ldots,N-2\) have lengths \(\lfloor w/2\rfloor+1\), and the right flank is symmetric. When \(N=2m\), the central \(N\) weights all have length \(m\); the flanks contribute \(2m=N\) odd-order components. Hence \(O_N=N\) for even \(m\), and \(O_N=2N\) for odd \(m\). When \(N=2m+1\), the central \(N\) weights have alternating lengths \(m+1\) (\(m+1\) times) and \(m\) (\(m\) times); the flanks contribute \(4\lceil m/2\rceil\) odd-order components. Consequently \(O_N=(3N-1)/2\) when \(N\equiv1\pmod4\), and \(O_N=(3N+1)/2\) when \(N\equiv3\pmod4\). Substitution proves all four cases.

## Verification
Run `python3 verify.py` using Python 3 standard library only. The verifier checks the actual integer-square test for every distinct pair in all \(100\) rectangles \(1\le A,B\le10\); compares every resulting edge to the predicted \(3:4\) path graph; independently brute-forces all candidate subsets for rectangles with \(AB\le16\), checking both the maximum and number of maximizers; and verifies the square formulas for \(1\le N\le200\). These are finite cross-checks, not substitutes for the unrestricted proof above.

## Relationship to prior work
Rongzhong Xiao, *Pythagorean pairs in boxes of prime powers* (arXiv:2610.11965, first submitted 2026-10-08), considers a box with both growing prime support and common exponent bound, and proves decay of the admissible density as the number of prime coordinates increases. The present theorem instead treats **all rectangles on the fixed prime support \(\{2,3\}\)**, giving exact cardinalities and counts of all maximum sets. The fixed-support square case at \(N=2\) agrees with the direct small-box enumeration, but it neither implies the general formulas nor is implied by the large-support asymptotics. The classical parametrization of Pythagorean triples explains the underlying \(3,4,5\) relation, but alone does not give the extremal counting formulas without the path decomposition.

## Limitations
Only the fixed support \(\{2,3\}\) is classified; for larger prime supports, additional primitive triples produce more complicated graphs. The exact formula is a structural consequence of the particular smooth prime support and should not be read as a large-support asymptotic. This claim has not received independent validation. Related exact results on prime-support boxes might be unindexed.

## References
1. Rongzhong Xiao, *Pythagorean pairs in boxes of prime powers*, arXiv:2610.11965v1 (2026-10-08); introduction and Theorem 1.1 inspected in publicly accessible v2.
2. N. Frantzikinakis, O. Klurman, J. Moreira, *Partition regularity of Pythagorean pairs*, as referenced in Xiao's Section 1.1 (density formulation; background).
