# Sharp perimeter and concave gap-energy laws for antipodal lattice polygons
## Finding
Let \(n\ge3\) be an integer, let \(R>0\), and let
\[
S_{2n}(R)=\{R(\cos(\pi j/n),\sin(\pi j/n)):0\le j<2n\}.
\]
A complete antipodal selection takes exactly one member of each pair of indices \(\{j,j+n\}\), and its convex hull has exactly \(n\) vertices.

For a selection with increasing cyclic indices \(a_0,\ldots,a_{n-1}\), set
\[
g_j=a_{j+1}-a_j\quad(0\le j<n-1),\qquad
g_{n-1}=a_0+2n-a_{n-1}.
\]
Every gap is an integer in \(\{1,\ldots,n+1\}\) and \(\sum_jg_j=2n\). Let \(f\) be *strictly discretely concave* on that integer interval: for \(1\le k<n\),
\[
f(k+2)-f(k+1)<f(k+1)-f(k).
\]
Define the cyclic gap energy
\[
E_f=\sum_{j=0}^{n-1}f(g_j).
\]
Then the exact range endpoints, including all equality cases, are:

**Minimum (all \(n\)).**
\[
\boxed{\min E_f=f(n+1)+(n-1)f(1).}
\tag{1}
\]
Exactly the \(2n\) selections of \(n\) successive vertices minimize it; equivalently their gaps are one \(n+1\) and \(n-1\) ones.

**Maximum, odd \(n\).**
\[
\boxed{\max E_f=nf(2).}
\tag{2}
\]
Exactly the two alternating selections attain it; their gaps are all \(2\).

**Maximum, even \(n=2m\).**
\[
\boxed{\max E_f=f(1)+f(3)+(n-2)f(2).}
\tag{3}
\]
Exactly the \(2n\) rotations of the following *cyclic* gap pattern attain it:
\[
\boxed{(1,\underbrace{2,\ldots,2}_{m-1},3,
\underbrace{2,\ldots,2}_{m-1}).}
\tag{4}
\]
Consequently the maximum for even \(n\) is strictly smaller than the unconstrained uniform-gap value \(nf(2)\), because \(2f(2)>f(1)+f(3)\).

For the Euclidean polygonal perimeter, use the strictly concave chord-length function
\[
f(k)=2R\sin\frac{\pi k}{2n}.
\]
Then
\[
\boxed{\operatorname{Per}_{\min}
=2R\left[(n-1)\sin\frac\pi{2n}+\cos\frac\pi{2n}\right].}
\tag{5}
\]
The sharp maximum is
\[
\boxed{
\operatorname{Per}_{\max}=
\begin{cases}
2nR\sin(\pi/n),&n\text{ odd},\\
2R\left[(n-2)\sin(\pi/n)+\sin(\pi/(2n))
+\sin(3\pi/(2n))\right],&n\text{ even}.
\end{cases}}
\tag{6}
\]
For even \(n\), the obstruction to the regular \(n\)-gon perimeter is exactly
\[
\boxed{2nR\sin\frac\pi n-\operatorname{Per}_{\max}
=4R\sin\frac\pi n\left(1-\cos\frac\pi{2n}\right)
\sim\frac{\pi^3R}{2n^3}.}
\tag{7}
\]
The minimum approaches \((\pi+2)R\), and the maximum approaches \(2\pi R\), as \(n\) tends to infinity.

## Assumptions and scope
The points are *equally spaced* on the circle and all antipodal pairs must contribute exactly one endpoint. The theorem makes no assertion for irregularly placed antipodal pairs or for selections of fewer than \(n\) vertices. Strict discrete concavity is necessary for the stated exhaustive classification of all extremizers; weak concavity can create additional equality cases.

The condition \(g_j\le n+1\) follows simply because the remaining \(n-1\) positive integer gaps sum to at least \(n-1\), so \(g_j\le2n-(n-1)\). Chords subtending a cyclic gap \(k\) have length \(2R\sin(\pi k/(2n))\). No assumption about the center's membership in the polygon is needed.

## Proof
We use an elementary strict discrete majorization lemma: if integral vectors \(x,y\) have equal sums, and decreasingly sorted \(x\) majorizes decreasingly sorted \(y\), then for every strictly discretely concave \(f\),
\[
\sum_i f(x_i)\le\sum_i f(y_i),
\]
with equality only when the vectors have the same multiset of entries. To see this without appealing to an analytic convexity theorem, transfer one unit from any larger component to a component at least two smaller. The energy change is
\[
[f(a-1)-f(a)]+[f(b+1)-f(b)]>0
\qquad (a\ge b+2),
\]
because the forward differences decrease strictly. A finite chain of these balancing transfers realizes the majorization comparison and proves strictness.

**The minimum.** The decreasing vector
\[
u=(n+1,1,\ldots,1)
\]
majorizes every vector of \(n\) positive integer gaps summing to \(2n\): the sum of its largest \(r\) coordinates is \(n+r\), whereas every other such vector has at least \(n-r\) remaining positive entries, forcing the same upper bound \(n+r\). Thus strict concavity gives (1), with equality only for the gap multiset of \(u\). Every such cyclic gap sequence consists of \(n\) consecutive selected vertices, and each of the \(2n\) possible starts is a valid antipodal selection.

**The unrestricted maximum and the parity obstruction.** The uniform vector
\[
c=(2,\ldots,2)
\]
is majorized by every integral gap vector with average \(2\). For odd \(n\), the gaps all equal to \(2\) select precisely the even indices or precisely the odd indices; their antipodes differ in parity because \(n\) is odd. Hence both are valid and are the only maximizers, proving (2).

For even \(n=2m\), a uniform gap-\(2\) sequence would select all vertices of a single parity. But antipodal indices differ by \(n\), an even number; therefore each antipodal pair consists of indices of the *same* parity. A uniform-gap selection would select both vertices from some such pairs, so it is inadmissible.

For any nonuniform integer gap vector with mean \(2\), the sum of its largest \(r\) entries is strictly greater than \(2r\) for each \(1\le r<n\). Since the sum is integral, it is at least \(2r+1\). Thus every nonuniform gap vector majorizes
\[
v=(3,\underbrace{2,\ldots,2}_{n-2},1),
\]
whose top-\(r\) partial sums are exactly \(2r+1\) for \(1\le r<n\). The strict discrete concavity lemma yields (3), with equality precisely if the gaps consist of a \(1\), a \(3\), and \(n-2\) copies of \(2\).

It remains essential to enforce the antipodal constraint rather than stopping at the unconstrained partition inequality. Rotate such a gap sequence so that the unique gap \(1\) comes first, and let \(k\) be the number of gaps \(2\) between the gap \(1\) and the gap \(3\). Starting at index \(0\), the selected indices up to the gap \(3\) have odd parity apart from the start; those after the gap \(3\) have even parity. Thus the selection contains exactly \(k+1\) odd vertices and \(n-k-1\) even vertices. For even \(n\), there are exactly \(n/2\) antipodal pairs of each parity; choosing exactly one endpoint from every pair forces exactly \(n/2\) selected vertices of each parity. Therefore \(k+1=m\), or \(k=m-1\), so precisely \(m-1\) gaps \(2\) lie between the unique \(1\) and \(3\). This yields precisely (4). Conversely, (4) selects the cyclic positions
\[
0,1,3,\ldots,n-1,n+2,n+4,\ldots,2n-2
\]
for \(n=2m\), which contain exactly one point from each opposite pair. Its \(2n\) rotations are all distinct since the gap pattern contains a unique \(1\). This proves the exhaustive even-order classification.

**Perimeters.** The chord function has strictly decreasing discrete forward differences on \(\{1,\ldots,n+1\}\), because \(\sin\) is strictly concave on \((0,\pi)\) and the sampled arguments lie in that interval. Substituting it into (1)--(3) gives (5) and (6). The sum-to-product identity
\[
\sin a+\sin(3a)=2\sin(2a)\cos a,
\quad a=\frac\pi{2n},
\]
gives (7), including its asymptotic expansion. Standard Taylor expansions yield the stated limits.

## Verification
Run the included standalone Python program with `python verify.py`. It independently enumerates every antipodal selection for \(3\le n\le14\), checks the complete predicted equality classes using the exact strictly concave energy \(f(k)=-k^2\), and checks the Euclidean perimeter formulas numerically for the same sizes. It also uses exact symbolic simplification to check the parity penalty and leading cubic expansion.

The exhaustive small-order enumeration is **not** an infinite proof. The quantified theorem is proved by the finite-transfer majorization argument and the even-order antipodal parity classification above.

## Relationship to prior work
Aichholzer, Caraballo, Díaz-Báñez, Fabila-Monroy, Ochoa, and Nigsch characterize *area*-minimizing and *area*-maximizing antipodal polygons for arbitrary antipodal points on a circle. Their source already identifies consecutive selections and thick alternating patterns for the **area** problem. Those geometric pattern names are therefore not claimed as novel. Importantly, the authors explicitly suggest replacing area by **perimeter** or by pairwise-distance sum as a separate direction at the end of their article.

Barba, Caraballo, Díaz-Báñez, Fabila-Monroy, and Pérez-Castillo study maximum **area** when fewer than all antipodal pairs are selected. In particular, their Theorem 2.7 writes an even-order area-optimizing gap pattern of the same \(1,2,\ldots,3,\ldots,2\) form when formally specialized to a complete transversal (the paper itself frames the principal problem with fewer selected points). That *configuration* is thus not claimed as new. Their sine-based discrete smoothing concerns area contributions, not a universal theorem about strictly concave *consecutive-gap energies* or the exact perimeter deficit under one-from-each-pair constraints.

General algorithms for maximum-perimeter polygons on planar point sets do not, by themselves, state these exact classifying formulas. Fejes Tóth's classical theorem on *sums over all point pairs* is a different functional from perimeter, which sums only adjacent edge lengths.

The novelty asserted here is limited to the perimeter values, strict equality classes in the evenly spaced antipodal case, and the common discrete-majorization law for all strictly concave gap costs. This law has not been deduced merely from the previously published area theorem.

## Limitations
The classification requires evenly spaced antipodal points and a strictly concave discrete gap cost; neither nonuniform antipodal positions nor arbitrary edge costs are covered. The minimum/maximum **area** patterns and the unconstrained regular-polygon perimeter comparison are prior mathematical knowledge. A historical derivation hidden in musical-scale or polygon-optimization literature remains a residual overlap risk. The exact strictness claim depends on finite-integer majorization, not on finite experimental enumeration.

## References
1. O. Aichholzer, L. E. Caraballo, J. M. Díaz-Báñez, R. Fabila-Monroy, C. Ochoa, and P. Nigsch, *Extremal antipodal polygons and polytopes*, arXiv:1301.6667v1 (2013).
2. O. Aichholzer et al., *Characterization of extremal antipodal polygons*, *Graphs and Combinatorics* 31 (2015), 321--333. DOI: 10.1007/s00373-015-1548-z.
3. L. Barba, L. E. Caraballo, J. M. Díaz-Báñez, R. Fabila-Monroy, and E. Pérez-Castillo, *Asymmetric polygons with maximum area*, arXiv:1501.07721v1 (2015).
