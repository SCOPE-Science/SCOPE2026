# Complete factor-complexity spectrum of a binary word with two phase defects

## Finding

For every triple of positive integers \(a,b,c\), consider the finite binary word
\[
W_{a,b,c}=(01)^a0(01)^b0(01)^c.
\]
For any integer length \(\ell\), write \(p_W(\ell)\) for the number of distinct contiguous factors of \(W\) of that length (not scattered subsequences). Set
\[
A=2a+1,\qquad B=2b+1,\qquad C=2c,\qquad T=\max\{A,B,C\},\qquad N=A+B+C.
\]
For positive \(X,Y\), and any integer \(k\), define the diagonal rectangle count
\[
H_{X,Y}(k)=\max\big\{0,\min(X-1,k)-\max(0,k-Y+1)+1\big\}.
\]
Define \(q_T(\ell)=2\) when \(1\le\ell<T\), \(q_T(\ell)=1\) when \(\ell=T\), and \(q_T(\ell)=0\) otherwise. Then, for every integer \(1\le\ell\le N\),
\[
\boxed{p_W(\ell)=q_T(\ell)+H_{A,B}(\ell-2)+H_{B,C}(\ell-2)-H_{\min(A,B),\min(B,C)}(\ell-2)+H_{A,C}(\ell-B-2).}
\]
Summing over all positive factor lengths gives the exact total
\[
\boxed{|\operatorname{Fact}^+(W)|=2T-1+AB+BC-\min(A,B)\min(B,C)+AC.}
\]
The subtraction term is a genuine interaction: factors straddling either phase defect can coincide even though they occur in disjoint positions.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); \(a,b,c\ge1\) are arbitrary integers. Factors are contiguous substrings, counted without multiplicity. The word has exactly two occurrences of the block `00`, and neither involves an endpoint convention. The three maximal alternating segments, all beginning with `0`, have respective lengths \(A,B,C\). This is a finite-word theorem; no periodic extension or asymptotic approximation is assumed.

## Proof

**Zero marked defects.** A factor avoiding `00` lies entirely in one of the three maximal alternating segments. Their maximum length is \(T\). For each \(1\le\ell<T\), the length-\(\ell\) alternating factor beginning in `0` and the one beginning in `1` both occur within any segment of length \(T\), since it provides at least two adjacent starting positions. At \(\ell=T\), exactly the factor beginning in `0` occurs (every segment begins with `0`), and for greater lengths no alternating factor occurs. These counts are \(q_T(\ell)\).

**Exactly one marked defect.** A factor with exactly one occurrence of `00` has a unique location of that block within itself. Its content is therefore uniquely specified by the two nonnegative integers \((u,v)\) giving the number of letters immediately to the left and right of the marked block: each side is forced to alternate. Such a factor has length \(\ell=u+v+2\). At the first occurrence, the permitted pairs are exactly the rectangle \(0\le u<A\), \(0\le v<B\). At the second, they are \(0\le u<B\), \(0\le v<C\). Both give the same alternating letter phases around `00`, so factors indexed by identical \((u,v)\) coincide across the two rectangles, and distinct index pairs give distinct factors. Their intersection has sides \(\min(A,B)\) and \(\min(B,C)\). Counting pairs on the diagonal \(u+v=\ell-2\) by inclusion–exclusion gives the three \(H\)-terms.

**Both marked defects.** A factor containing both `00` blocks must contain the unique inter-defect passage. Its length from the start of the first `00` through the end of the second is \(B+2\), since their starting positions are separated by \(B\) letters. It can be extended by \(u\) letters leftward with \(0\le u<A\), and \(v\) letters rightward with \(0\le v<C\). Its full content specifies \(u,v\) uniquely because the two `00` locations can be recovered from the factor. The resulting diagonal count is \(H_{A,C}(\ell-B-2)\). A factor with two blocks cannot equal one from the zero- or one-block categories.

The three disjoint cases partition all distinct factors, proving the spectrum. Finally \(\sum_k H_{X,Y}(k)=XY\) because it counts every pair of rectangle coordinates once, while \(\sum_{\ell\ge1}q_T(\ell)=2T-1\). Summing the spectrum yields the claimed total. All parts use exact finite bijections, not empirical extrapolation.

## Verification

The standalone `verify.py` constructs the word directly and, for every integer triple \(1\le a,b,c\le9\), compares the formula with a brute-force set of actual substrings at **every** length from \(1\) through \(N\). It checks the summed total independently. This covers \(729\) parameter triples; running `python3 verify.py` returns `VERIFY_OK 729 triples`. The full proof above, not the finite tests, establishes the unrestricted assertion.

## Relationship to prior work

Factor complexity is a standard linguistic-complexity invariant. Prezza's 2017 paper *String Attractors*, specifically its Definition 1, Lemma 1, and Theorem 3.1, gives general bounds relating distinct factor counts to string attractors; it does not furnish this two-phase-defect exact spectrum or the overlap term. The alternating word with two inserted letters is a controlled finite repetitive-text model where the entire factor-count profile is computable as four diagonal rectangle counts. A 2022 study of reconstruction of periodic words from fragment multisets treats a different inverse problem and does not imply this direct exact enumeration.

## Limitations

Only the displayed three-parameter family is classified. The result does not classify arbitrary substitutions, more than two defects, other alphabets, subsequences, or string-attractor minima. Exhaustive verification ends at \(a,b,c=9\) and is supplementary to the proof. Although no equivalent precise claim was identified in the inspected related sources and searches, the broader combinatorics-on-words literature is extensive and an unindexed equivalent could exist; independent scholarly verification remains to be carried out.

## References

1. Nicola Prezza, *String Attractors*, arXiv:1709.05314v1, first posted 2017-09-15; accessible full text: https://arxiv.org/html/1709.05314v2 ; relevant material: Section 3, Lemma 1, Theorem 3.1.
2. *On the Word Fragment Length for Unambiguous Reconstruction of a Periodic Word from a Complete Multiset of Fragments of Fixed Length*, 2022, https://doi.org/10.1134/S106456242202003X ; relevant material: setup and main reconstruction statement.
