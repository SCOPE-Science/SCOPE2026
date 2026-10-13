# Independent Roman weight enumerator of cycles
## Finding
For every integer \(n\ge 5\), let \(C_n\) be the cycle on labeled vertices \(v_0,\ldots,v_{n-1}\), with indices read modulo \(n\). An independent Roman dominating function is a map \(f:V(C_n)\to\{0,1,2\}\) such that every vertex labeled \(0\) has a neighbor labeled \(2\), and the vertices with positive labels form an independent set. Write \(w(f)=\sum_v f(v)\) and
\[
I_n(x)=\sum_f x^{w(f)}.
\]

Every such function has at least one vertex labeled \(2\). Read the vertices labeled \(2\) cyclically and measure the edge distance from one to the next. Every gap has length exactly \(2\), \(3\), or \(4\), with the labels inside the gap forced to be
\[
2,0,2;\qquad 2,0,0,2;\qquad 2,0,1,0,2,
\]
respectively. Conversely, any cyclic concatenation of these three gap types gives an independent Roman dominating function.

If \(a,b,c\) are the numbers of gaps of lengths \(2,3,4\), then
\[
2a+3b+4c=n,
\qquad
w(f)=2a+2b+3c.
\]
For fixed \((a,b,c)\), put \(k=a+b+c\). The number of labeled functions with this gap inventory is
\[
\frac{n(k-1)!}{a!b!c!}.
\]
Therefore
\[
I_n(x)=\sum_{\substack{a,b,c\ge0\\a+b+c>0\\2a+3b+4c=n}}\frac{n(a+b+c-1)!}{a!b!c!}\,x^{2a+2b+3c}.
\]

The minimum weight is the previously known value
\[
i_R(C_n)=\left\lceil\frac{2n}{3}\right\rceil.
\]
The number of minimum-weight functions is
\[
\begin{cases}
3,&n\equiv0\pmod3,\\
n,&n\equiv1\pmod3,\\
\dfrac{n(n+1)}6,&n\equiv2\pmod3.
\end{cases}
\]

## Assumptions and scope
The cycle is simple and has \(n\ge5\) vertices. The standard independent Roman convention is used: positive labels induce an independent set, while every label \(0\) must have a neighboring label \(2\). The labeled-cycle count distinguishes vertex positions; rotations are not quotient-identified.

The restriction \(n\ge5\) isolates the stated contribution from the small complete-multipartite cycles \(C_3\) and \(C_4\), for which a broader complete-multipartite enumerator already applies. The displayed formula itself also evaluates correctly at those small orders, but they are not part of the originality claim.

## Proof
First, an independent Roman dominating function on a cycle must contain a label \(2\). If it contained no \(2\), then no vertex could be labeled \(0\); all vertices would be positive, contradicting independence.

Choose two consecutive label-\(2\) vertices in cyclic order, and let \(d\) be their edge distance. Independence implies \(d\ge2\). Every internal label \(0\) in this gap must be adjacent to one of the two endpoint labels \(2\), since by definition there is no other label \(2\) inside the gap.

If \(d=2\), the unique internal vertex is adjacent to both endpoints and cannot be positive, so the pattern is \(2,0,2\). If \(d=3\), both internal vertices must be \(0\), giving \(2,0,0,2\). If \(d=4\), the two vertices next to the endpoints must be \(0\); the middle vertex is adjacent to neither endpoint, so it cannot be \(0\), and independence then forces it to be the sole positive internal vertex, labeled \(1\). Thus the pattern is \(2,0,1,0,2\).

No gap can have \(d\ge5\). The vertex one step after the first endpoint and the vertex one step before the second endpoint must be \(0\). Every internal vertex not adjacent to an endpoint label \(2\) would then have to be positive. For \(d\ge5\), at least two consecutive internal vertices are not adjacent to either endpoint, so both would be positive, contradicting independence. Hence only the three displayed gap types occur.

Conversely, each of the three gap patterns has independent positive support and every zero in it is adjacent to an endpoint label \(2\). Cyclic concatenation preserves both properties, proving the structural classification.

Now fix a gap inventory \((a,b,c)\), let \(k=a+b+c\), and assume \(2a+3b+4c=n\). The weight is \(2k+c=2a+2b+3c\). To count labeled functions, count pairs consisting of a function and a distinguished label-\(2\) vertex. There are \(n\) choices for the distinguished vertex and
\[
\frac{k!}{a!b!c!}
\]
ordered cyclic gap words starting there. Each function has exactly \(k\) choices of distinguished label-\(2\) vertex. Dividing by \(k\) gives \(n(k-1)!/(a!b!c!)\), proving the enumerator.

For the minimum, observe that
\[
3w(f)-2n=2a+c.
\]
Thus \(w(f)\ge\lceil2n/3\rceil\). Equality forces the smallest possible value of \(2a+c\) compatible with the residue of \(n\). If \(n\equiv0\pmod3\), equality has \(a=c=0\), so all gaps have length \(3\), giving exactly \(3\) labeled functions. If \(n\equiv1\pmod3\), equality has \(a=0,c=1\), giving exactly \(n\) functions. If \(n=3q+2\), equality has either \((a,c)=(1,0)\) or \((a,c)=(0,2)\); the two multinomial contributions sum to
\[
n+\frac{n(q-1)}2=\frac{n(n+1)}6.
\]
This proves the minimum-function census.

## Verification
The standalone checker `verify.py` constructs every labeling of \(C_n\) for \(5\le n\le12\). It tests the independent Roman definition directly from neighborhoods, independently tests the cyclic-gap characterization, compares the complete weight distribution with the closed coefficient formula, and verifies both the known minimum weight and the new minimum-function count.

Replay result:

`VERIFY_OK n_range=5..12 labelings=797040 irdf_functions=294 criterion_checks=797040 coefficient_checks=144 minimum_checks=8 max_order=12`

This finite computation is a boundary and implementation check. The all-orders theorem follows from the proof above, not from extrapolation.

## Relationship to prior work
Ebrahimi Targhi', Jafari Rad, Mynhardt, and Wu give the standard independent Roman definition, bounds, and structural results; their public article page records publication on 2012-02-29 and the paper is classified under 05C69. Adabi, Ebrahimi Targhi, Jafari Rad, and Moradi explicitly state the scalar equality \(i_R(C_n)=\gamma_R(C_n)\), so the minimum value is treated here as prior work rather than as the new contribution.

The closest previously checked all-function result concerns connected complete multipartite graphs. It covers the exceptional identities \(C_3\cong K_3\) and \(C_4\cong K_{2,2}\), but it does not imply the cycle result for \(n\ge5\), because those cycles are not complete multipartite and their independent Roman functions have the cyclic gap structure proved above. Searches under the standard parameter name together with “cycle,” “polynomial,” “weight enumerator,” “all functions,” and “minimum functions” did not locate a published all-weight cycle enumerator or the displayed gap census.

## Limitations
The result is for ordinary independent Roman domination on cycles, not for weak, total, restrained, strong, or Roman \(\{2\}\)-variants. It counts labeled functions rather than equivalence classes under dihedral symmetry. The literature comparison cannot exclude poorly indexed theses, non-English sources, or results stated under unusual terminology; that residual bibliographic risk is recorded in the review. The scalar minimum \(i_R(C_n)=\lceil2n/3\rceil\) is not claimed as new.

## References
1. E. Ebrahimi Targhi', N. Jafari Rad, C. M. Mynhardt, and Y. Wu, “Bounds for Independent Roman Domination in Graphs,” *Journal of Combinatorial Mathematics and Combinatorial Computing* 80 (2012), 351–365. Public article page: https://combinatorialpress.com/jcmcc-articles/volume-080/bounds-for-independent-roman-domination-in-graphs/.
2. S. Adabi, A. R. Ebrahimi Targhi, N. Jafari Rad, and M. Moradi, “Properties of independent Roman domination in graphs,” *Australasian Journal of Combinatorics* 52 (2012), 11–18. Public PDF: https://ajc.maths.uq.edu.au/pdf/52/ajc_v52_p011.pdf.
3. E. Ebrahimi Targhi', N. Jafari Rad, and C. M. Mynhardt, “A note on independent Roman domination in unicyclic graphs,” *Opuscula Mathematica* 32 (2012), 715–718. DOI: 10.7494/OpMath.2012.32.4.715.
