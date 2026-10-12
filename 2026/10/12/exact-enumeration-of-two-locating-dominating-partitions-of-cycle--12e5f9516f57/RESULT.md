# Exact enumeration of two locating-dominating partitions of cycles
## Finding
For every simple cycle \(C_n\) on the labeled vertex set \(\mathbb Z_n\), let \(a_n\) denote the number of **ordered** partitions \((L_0,L_1)\) of its vertices into two locating-dominating sets; exchanging the two parts counts as a different partition. Then \(a_3=0\), \(a_4=4\), and, for every \(n\ge5\), the admissible binary colorings are exactly the cyclic words avoiding the four factors \(000\), \(111\), \(00100\), and \(11011\).

Their complete enumerator is
\[
\boxed{\sum_{n\ge4}a_n x^n=\frac{4x^4+10x^5+10x^6+4x^7+12x^8+4x^9+4x^{10}+2x^{12}}{1-x^2-x^4-2x^5-x^6-x^8}.}
\]
In particular,
\[
(a_4,a_5,\ldots,a_{12})=(4,10,14,14,30,36,72,88,150),
\]
and, for \(n\ge13\),
\[
a_n=a_{n-2}+a_{n-4}+2a_{n-5}+a_{n-6}+a_{n-8}.
\]
Every cycle with \(n\ge4\) admits such a partition, and \(a_n\sim\rho^{-n}\), where \(\rho\approx0.660992531890120\) is the unique smallest-modulus zero of the denominator. Thus the number of ordered partitions grows asymptotically like \((1.51287639686409)^n\).

## Assumptions and scope
Graphs are finite and simple. The cycle \(C_n\), for \(n\ge3\), has vertices \(0,\ldots,n-1\), each adjacent to the two vertices with indices one less and one greater modulo \(n\). A locating-dominating set \(L\) is a dominating set for which the nonempty open-neighborhood signatures \(N(v)\cap L\) are different for distinct vertices \(v\notin L\). The ordered parts are exactly the vertices of color \(0\) and of color \(1\) in a binary word, with vertex indices fixed. Cyclic factors may wrap across the boundary. The theorem counts labeled assignments, **not** orbits under rotation or reflection and **not** partitions with the parts regarded as unordered. The indeterminate \(x\) in the generating series is formal.

## Proof
**Step 1: domination.** Suppose \(n\ge5\) and a binary word colors \(C_n\). The vertices of color \(0\) dominate the vertices of color \(1\) exactly when no color-\(1\) vertex has both neighbors of color \(1\); this is equivalent to avoiding \(111\). Interchanging the colors gives avoidance of \(000\). Thus simultaneous domination is equivalent to having every monochromatic run of length \(1\) or \(2\).

**Step 2: location.** Distinct vertices of \(C_n\) for \(n\ge5\) have at most one common neighbor. Consequently, two distinct vertices outside a dominating color class cannot have equal signatures both of size \(2\). Signatures of different sizes also cannot agree. Two outside vertices \(u,v\) with the same singleton signature \(\{s\}\) must be exactly the two neighbors of \(s\). For the outside color \(0\) and the locating color \(1\), both of those vertices must have their other neighbors colored \(0\). This forces the cyclic five-letter factor \(00100\), with \(s\) the central \(1\). Conversely, such a factor gives two outside vertices with the same singleton signature. For the other locating color the forbidden factor is \(11011\). The four-factor criterion follows, with no unexamined collision types.

**Step 3: run-length transfer.** Under the four-factor criterion, a cyclic word on at least five vertices has an even number \(r\ge4\) of alternating monochromatic runs. Each run length lies in \(\{1,2\}\). The additional two forbidden length-five factors say precisely that no three cyclically consecutive run lengths can equal \((2,1,2)\). Conversely, any even cyclic list of run lengths obeying these constraints determines alternating admissible words by specifying the first color and the position of its first vertex.

Index a four-state weighted matrix \(T\) by the ordered pairs \((1,1),(1,2),(2,1),(2,2)\). Give a transition from \((a,b)\) to \((b,c)\) weight \(x^c\) when \(c\in\{1,2\}\) and \((a,b,c)\ne(2,1,2)\); otherwise give it weight zero. Thus
\[
T=\begin{pmatrix}
x&x^2&0&0\\
0&0&x&x^2\\
x&0&0&0\\
0&0&x&x^2
\end{pmatrix}.
\]
For each even run count \(r\), the polynomial \(\operatorname{tr}(T^r)\) counts cyclic run-length lists with their first run distinguished. To reconstruct a labeled color word, choose its first-run color (two choices) and first-run start (\(n\) choices); every word with \(r\) runs is then represented exactly \(r\) times, once per possible distinguished run. Therefore, for every \(n\ge5\),
\[
a_n=2n\,[x^n]\sum_{\substack{r\ge2\\r\,\mathrm{even}}}\frac{\operatorname{tr}(T^r)}{r}
=n[x^n]\sum_{k\ge1}\frac{\operatorname{tr}((T^2)^k)}{k}.
\]
As an identity of formal power series, the logarithmic determinant identity yields
\[
\sum_{n\ge1}b_nx^n=-x\frac{d}{dx}\log\det(I-T^2),\quad
\det(I-T^2)=Q(x)=1-x^2-x^4-2x^5-x^6-x^8,
\]
where \(b_n=a_n\) for \(n\ge5\). Direct differentiation gives
\[
\sum_{n\ge1}b_nx^n=\frac{2x^2+4x^4+10x^5+6x^6+8x^8}{Q(x)}.
\]
The formal trace series has extraneous low-order terms \(2x^2\) and \(6x^4\). There is no ordinary simple cycle with two vertices; at four vertices, exactly the four cyclic rotations of \(0011\) are valid. The two alternating words \(0101\) and \(1010\), counted in the formal trace term, fail because the opposite vertices of a four-cycle have identical two-neighbor signatures. Thus, using \(a_4=4\), the required series is \(-xQ'(x)/Q(x)-2x^2-2x^4\). Multiplication by \(Q(x)\) gives exactly the boxed numerator. At three vertices no such partition exists: if one color occurs once, its two outside vertices have the same singleton signature; a monochromatic coloring plainly fails domination.

**Step 4: recurrence and asymptotics.** Comparing coefficients in \(Q(x)\sum a_nx^n\) gives the displayed recurrence for all \(n\ge13\). Its nonnegative coefficients together with the positive initial values imply \(a_n>0\) for every \(n\ge4\). Finally
\[
Q(x)=-(x^4-x^3+x^2+x-1)(x^4+x^3+x^2+x+1).
\]
Let \(h(t)=t^2+t^4+2t^5+t^6+t^8\) for \(t\ge0\). This is strictly increasing from \(h(0)=0\) to a value greater than \(1\) at \(t=1\); consequently exactly one \(\rho\in(0,1)\) satisfies \(h(\rho)=1\), and numerically \(\rho\approx0.660992531890120\). If \(Q(z)=0\), then \(1=|z^2+z^4+2z^5+z^6+z^8|\le h(|z|)\). Therefore no root has modulus less than \(\rho\). If equality holds with \(|z|=\rho\), equality in the triangle inequality forces the powers \(z^2\) and \(z^5\) to have positive real phase because their weighted sum equals \(1\); since \(\gcd(2,5)=1\), this forces \(z=\rho\). Hence \(\rho\) is the unique smallest-modulus root. Also \(Q'(\rho)=-h'(\rho)<0\), so it is simple. In \(-xQ'(x)/Q(x)\), the pole there has principal part \((1-x/\rho)^{-1}\) and contributes \(\rho^{-n}\) to the coefficient of \(x^n\), while all other poles give strictly smaller exponential contributions. Removing the two low-degree terms does not affect the asymptotic. Hence \(a_n\sim\rho^{-n}\).

## Verification
The standalone Python 3 standard-library file `verify.py` recomputes the two locating-dominating conditions directly for all \(2^n\) ordered colorings of each simple cycle with \(4\le n\le16\), checks the forbidden-factor criterion independently for \(5\le n\le16\), and independently counts cyclic run-length sequences with a transfer computation for \(5\le n\le40\). Those results agree with the rational-series coefficients. The exact run output is stored in `verification_output.txt`. Run `python3 verify.py`. Finite verification supports but does not replace Steps 1–4.

## Relationship to prior work
Foucaud, Maniya, Paul and Pradhan (2025) investigate the existence of partitions into two locating-dominating sets and prove such partitions exist in several graph classes. Their Question 1 concerns existence in general twin-free isolate-free graphs; their examined paper gives no all-orders cycle partition count. The previously known bipartite-graph existence result includes even cycles but does not enumerate labeled partitions, and does not directly address odd cycles. Chakraborty, Foucaud, Henning and Laihonen (2026) establish the weaker universal partition into a dominating set and a locating-dominating set, not two locating-dominating classes. Zelinka (1998) introduced the location-domatic number, which optimizes the number of classes rather than counting labeled optimal two-class partitions. The inaccessible full text of that historical paper leaves a residual equivalence risk, explicitly noted in `REVIEW.md`.

## Limitations
This is an exact theorem for the cycle family; there is no assertion for arbitrary twin-free graphs, for partitions into three or more locating-dominating classes, or for dihedral/orbit counts. The structural criterion for \(n\ge5\) is not valid without the separately treated four-vertex exception. No independent external audit or external certification is claimed.

## References
1. F. Foucaud, P. V. Maniya, K. Paul, D. Pradhan, *Locating-dominating partitions for some classes of graphs*, arXiv:2506.12933v1 (first public posting June 15, 2025), https://arxiv.org/html/2506.12933v1 .
2. D. Chakraborty, F. Foucaud, M. A. Henning, T. Laihonen, *A note on partitioning the vertex set of a graph into a dominating set and a locating dominating set*, Electronic Journal of Combinatorics **33** (2026), P1.51, doi:10.37236/14049, https://doi.org/10.37236/14049 .
3. B. Zelinka, *Location-domatic number of a graph*, Mathematica Bohemica **123** (1998), 67–71, doi:10.21136/MB.1998.126298, https://doi.org/10.21136/MB.1998.126298 .
