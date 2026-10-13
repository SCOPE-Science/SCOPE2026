# Paired-domination polynomial of book graphs
## Finding
For every integer \(n\ge2\), let
\[
B_n=K_{1,n}\mathbin{\square}P_2
\]
be the square book graph. Write its spine vertices as \(a,b\), and write the page vertices as \(x_i,y_i\) for \(1\le i\le n\), so page \(i\) has edges \(ab,ax_i,x_iy_i,y_ib\). A paired-dominating set is a dominating set \(S\) such that the induced graph \(B_n[S]\) has a perfect matching. Define
\[
D_{\mathrm{pr}}(B_n;x)=\sum_{S}x^{|S|},
\]
where the sum is over all paired-dominating sets.

Then
\[
D_{\mathrm{pr}}(B_n;x)
=x^2(1+x^2)^n+n(n-1)x^4(1+x^2)^{n-2}+(2n+1)x^{2n}.
\]
Equivalently, every paired-dominating set is in exactly one of the following four types.

1. Both spine vertices are selected, and each page is either in state \(00\) or \(11\), where the two bits record membership of \(x_i,y_i\).
2. Both spine vertices are selected, exactly one page is in state \(10\), exactly one distinct page is in state \(01\), and every other page is in state \(00\) or \(11\).
3. Exactly one spine vertex is selected. If it is \(a\), exactly one page is in state \(10\) and all other pages are in state \(11\); if it is \(b\), exactly one page is in state \(01\) and all other pages are in state \(11\).
4. Neither spine vertex is selected, and every page is in state \(11\).

Consequently,
\[
\gamma_{\mathrm{pr}}(B_n)=2,
\]
the unique minimum paired-dominating set is \(\{a,b\}\), and
\[
D_{\mathrm{pr}}(B_n;1)=2^n+n(n-1)2^{n-2}+2n+1.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The theorem is stated for \(n\ge2\). The boundary \(n=1\) is \(B_1\cong C_4\) and is deliberately excluded from the claimed family formula because the second displayed term is written with exponent \(n-2\); directly, its paired-domination polynomial is \(4x^2+x^4\).

The proof uses only the definition of paired domination and the explicit adjacency in the book graph. The polynomial counts all paired-dominating sets, not only minimum sets.

## Proof
For each page, record its state as \(00,10,01,11\) according to whether \(x_i,y_i\) belong to \(S\).

**Case 1: neither \(a\) nor \(b\) lies in \(S\).** If a page were in state \(00\), then its vertex \(x_i\) would have no selected neighbor, because its only neighbors are \(a\) and \(y_i\); hence domination fails. Thus each page contains at least one selected vertex. In the induced graph on \(S\), vertices from different pages have no edges, and a singleton page vertex has no selected neighbor. Therefore a perfect matching exists exactly when every page is in state \(11\). This gives one set of size \(2n\).

**Case 2: exactly one spine vertex lies in \(S\).** By symmetry assume \(a\in S\) and \(b\notin S\). A page cannot be in state \(00\), because then \(y_i\) is undominated, and it cannot be in state \(01\), because a selected singleton \(y_i\) would be isolated in \(B_n[S]\). Hence every page is in state \(10\) or \(11\). Every state-\(10\) singleton can be matched only to \(a\), so at most one such page is possible. Since a perfect matching has even order, the selected order
\[
1+k+2(n-k)=2n+1-k
\]
is even, where \(k\) is the number of state-\(10\) pages. Thus \(k\) is odd, and therefore \(k=1\). Conversely, with exactly one state-\(10\) page, match its \(x_i\) to \(a\), and match \(x_j\) to \(y_j\) in every other page. There are \(n\) such sets. The reflected case with \(b\) gives another \(n\), all of size \(2n\).

**Case 3: both \(a,b\in S\).** Domination is automatic. Let \(p\) be the number of state-\(10\) pages and \(q\) the number of state-\(01\) pages. A state-\(10\) singleton can be matched only to \(a\), so \(p\le1\); similarly \(q\le1\). If \((p,q)=(0,0)\), match \(a\) to \(b\) and match every selected state-\(11\) page internally. If \((p,q)=(1,1)\), match \(a\) to the unique state-\(10\) singleton and \(b\) to the unique state-\(01\) singleton, then match each selected state-\(11\) page internally.

It remains to exclude \((p,q)=(1,0)\) and \((0,1)\). In the first case, the state-\(10\) singleton forces \(a\) to be its matching partner. Vertex \(b\) cannot then be matched to \(a\). If \(b\) is matched to a selected \(y_j\) from a state-\(11\) page, the corresponding \(x_j\) is left with no available matching partner: its possible partners inside the selected graph are only \(a\) and \(y_j\), both already used. Hence no perfect matching exists. The other case is symmetric.

Therefore, with both spine vertices selected, either all pages are in states \(00\) or \(11\), or there is exactly one state \(10\) page and one distinct state \(01\) page, with all others in states \(00\) or \(11\).

The first subcase contributes
\[
x^2(1+x^2)^n.
\]
For the second, choose the state-\(10\) page and then the distinct state-\(01\) page in \(n(n-1)\) ordered ways. The remaining pages independently contribute either zero or two selected vertices, giving
\[
n(n-1)x^4(1+x^2)^{n-2}.
\]
The one-spine cases contribute \(2n x^{2n}\), and the no-spine case contributes \(x^{2n}\). Summing proves the stated formula.

The coefficient of \(x^2\) is \(1\) for every \(n\ge2\), so the paired-domination number is \(2\) and \(\{a,b\}\) is the unique minimum set. Substitution \(x=1\) gives the stated total count.

## Verification
The accompanying `verify.py` constructs \(B_n\) directly, enumerates every subset for \(1\le n\le8\), tests domination from adjacency, tests existence of a perfect matching by recursive search, compares the resulting coefficient vector with the closed formula for \(n\ge2\), and checks the four structural types independently. The computation is a finite regression check only; the proof above establishes the theorem for all \(n\ge2\).

## Relationship to prior work
Haynes and Slater introduced paired domination as domination together with a perfect matching in the selected induced subgraph. Choudhary, Margulies, and Hicks later studied total and paired domination for Cartesian products, proving general product inequalities. The square book \(B_n\) is precisely the Cartesian product \(K_{1,n}\mathbin{\square}P_2\), so that literature gives a direct motivation for asking for exact paired-domination structure on this family, but the inspected product paper does not give this coefficientwise enumeration.

A 2016 paper introduced the paired-domination polynomial and states in its public abstract that it computes the polynomial for some standard graph families. The accessible public material did not expose the full family list, so that source is retained as an explicit residual originality risk rather than treated as evidence of noncoverage. Searches under book-graph, square-book, star-prism, Cartesian-product, and paired-domination-polynomial formulations did not locate a statement implying the four-type classification or the displayed polynomial. Published exact paired-domination polynomials for chain graphs and complete multipartite graphs do not subsume the book family.

## Limitations
The theorem claims only \(n\ge2\); the cycle boundary \(n=1\) is not part of the originality claim. Search-based originality cannot exclude an unindexed or inaccessible family-specific formula. In particular, the full text of the 2016 polynomial paper was not available through the inspected public route beyond its abstract, so its unstated standard-family computations remain a residual risk. The finite verifier reaches \(n=8\) and is not an infinite proof.

## References
1. T. W. Haynes and P. J. Slater, “Paired-domination in graphs,” *Networks* 32 (1998), 199–206. DOI: 10.1002/(SICI)1097-0037(199810)32:3<199::AID-NET4>3.0.CO;2-F.
2. K. Choudhary, S. Margulies, and I. V. Hicks, “A Note on Total and Paired Domination of Cartesian Product Graphs,” *The Electronic Journal of Combinatorics* 20(3) (2013), P25. DOI: 10.37236/2535.
3. W. Ulatowski, “The paired-domination and the upper paired-domination numbers of graphs,” *Opuscula Mathematica* 35 (2015), 127–135. DOI: 10.7494/OpMath.2015.35.1.127.
4. Puttaswamy, A. Alwardi, and S. R. Nayaka, “Introduction to Paired Domination Polynomial of a Graph,” *International Journal of Physical and Mathematical Sciences* 10(9) (2016).
