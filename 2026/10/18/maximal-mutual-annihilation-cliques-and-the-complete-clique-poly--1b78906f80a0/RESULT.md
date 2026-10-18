# Maximal mutual-annihilation cliques and the complete clique polynomial of rank-one square-zero matrices

## Finding
Let \(q\) be any prime power, \(n\ge2\), and \(V=\mathbb F_q^n\). Let \(G_{n,q}\) be the simple graph whose vertices are the nonzero rank-one square-zero endomorphisms of \(V\), with distinct vertices adjacent if and only if they commute. Every edge in fact satisfies **both products zero**.

For each proper nonzero vector subspace \(U<V\), define
\[
\mathcal C(U)=\{u\otimes\varphi:\;0\ne u\in U,\;0\ne\varphi\in U^\perp\},
\qquad U^\perp=\{\varphi\in V^*:\varphi(U)=0\}.
\]
The set is understood as a set of **distinct matrices**, not a list of choices of factors. **The maximal cliques of \(G_{n,q}\) are exactly the distinct sets \(\mathcal C(U)\), for all \(0<U<V\).** Consequently the graph has exactly \(\sum_{r=1}^{n-1}{n\brack r}_q\) maximal cliques. A maximal clique indexed by an \(r\)-dimensional subspace has size
\[
D_{n,q}(r)=\frac{(q^r-1)(q^{n-r}-1)}{q-1}.
\]
Its clique number is \(D_{n,q}(\lfloor n/2\rfloor)\), and the number of maximum cliques is \({n\brack n/2}_q\) for even \(n\), and \(2{n\brack (n-1)/2}_q\) for odd \(n\).

More strongly, let \(c_k(n,q)\) be the number of unordered \(k\)-element pairwise-commuting vertex subsets, with \(c_0=1\). Their **entire clique polynomial** \(C_{n,q}(z)=\sum_{k\ge0}c_k(n,q)z^k\) is
\[
\boxed{C_{n,q}(z)=1+\sum_{r=1}^{n-1}\sum_{s=1}^{n-r}{n\brack r}_q{n-r\brack s}_q
\sum_{i=0}^{r}\sum_{j=0}^{s}{r\brack i}_q{s\brack j}_q
(-1)^{r+s-i-j}q^{\binom{r-i}{2}+\binom{s-j}{2}}
(1+z)^{(q^i-1)(q^j-1)/(q-1)}.}
\]
In particular, \(C_{4,2}(z)=1+105z+1260z^2+3780z^3+5460z^4+5040z^5+3150z^6+1290z^7+315z^8+35z^9\). These formulas hold in all finite characteristics, including characteristic two.

## Assumptions and scope
A rank-one operator is written \(u\otimes\varphi\), acting by \(v\mapsto\varphi(v)u\). It has square zero exactly when \(\varphi(u)=0\). The graph has no zero vertex and no loops; different nonzero scalar multiples are distinct vertices. The Gaussian coefficient \({a\brack b}_q\) counts \(b\)-subspaces in \(\mathbb F_q^a\), and is zero outside \(0\le b\le a\). The coefficient \(c_k\) counts **subsets without repetition**. The empty clique is counted once. No assumption that \(q\) is prime rather than a prime power is made.

## Proof
**Commutation is mutual annihilation.** Write \(A=u\otimes\varphi\) and \(B=v\otimes\psi\), with each vector and covector nonzero and \(\varphi(u)=\psi(v)=0\). Then
\[
AB=\varphi(v)\,u\otimes\psi,\qquad BA=\psi(u)\,v\otimes\varphi.
\]
If \(AB=BA\ne0\), equality of their rank-one images and row spaces forces \(v\in ku\) and \(\psi\in k\varphi\). Thus \(B\) is a nonzero scalar multiple of \(A\), so \(AB=0\), a contradiction. Hence commuting implies \(AB=BA=0\), equivalent to \(\varphi(v)=\psi(u)=0\). This includes the scalar-multiple case, whose products are zero.

**Maximal-clique classification.** Let \(S\) be a nonempty clique and set \(U=\sum_{A\in S}\operatorname{im}(A)\). For every \(A=u\otimes\varphi\in S\), mutual annihilation says \(\varphi\) annihilates every image, hence \(\varphi\in U^\perp\). In particular \(U\) is proper (the covectors are nonzero), and \(S\subseteq\mathcal C(U)\). Conversely every pair of elements of \(\mathcal C(U)\) annihilates one another. Therefore maximality forces \(S=\mathcal C(U)\). To see that \(\mathcal C(U)\) is maximal, note that its images span \(U\), while its covectors span \(U^\perp\). A rank-one square-zero operator commuting with every element must have image in \((U^\perp)^\perp=U\) and covector in \(U^\perp\); it already belongs to \(\mathcal C(U)\). The image span of \(\mathcal C(U)\) is exactly \(U\), so different subspaces give different maximal cliques. There are \({n\brack r}_q\) of dimension \(r\). The dyad representation \(u\otimes\varphi\) is unique up to simultaneous inverse nonzero scaling; thus its size is \(D_{n,q}(r)\). Maximizing this size is equivalent to minimizing \(q^r+q^{n-r}\), which occurs only at the middle rank or the two adjacent middle ranks as stated.

**Whole clique polynomial.** Every nonempty clique \(S\) has the intrinsic image span \(U=\sum_{A\in S}\operatorname{im}A\) and covector span \(W=\sum_{u\otimes\varphi\in S}k\varphi\subseteq V^*\). These satisfy \(0<U<V\), \(0<W\subseteq U^\perp\). Write \(r=\dim U\), \(s=\dim W\). There are exactly \({n\brack r}_q{n-r\brack s}_q\) such ordered pairs of subspaces. For a fixed pair, all allowed vertices lie in the rank-one Segre set \(\{u\otimes\varphi:0\ne u\in U,0\ne\varphi\in W\}\), which has \(D(i,j)=(q^i-1)(q^j-1)/(q-1)\) members when the image and covector spaces have dimensions \(i,j\). Hence its arbitrary-subset polynomial is \((1+z)^{D(i,j)}\). Möbius inversion in the independent subspace lattices of \(U\) and \(W\), whose codimension-\(d\) Möbius coefficient is \((-1)^dq^{\binom d2}\), extracts exactly those subsets spanning **both** spaces. Summing over every \(U,W\) produces the boxed double Gaussian–Möbius formula. Each nonempty clique has a unique pair of spans, so is counted exactly once. The empty clique makes no contribution to the \(r,s>0\) terms (their constant Möbius sums vanish) and supplies the initial \(1\). This completes the proof.

## Verification
The complete, standalone Python 3 script `verify_cliques.py` uses only the standard library. It independently constructs literal matrices, evaluates both matrix products (rather than relying on the flag criterion), enumerates all maximal cliques by Bron–Kerbosch, enumerates all their subsets without repetition, computes the full Gaussian–Möbius polynomial, compares every coefficient, and checks the maximal-clique rank-size distribution. Tested cases: \((q,n)=(2,2),(2,3),(2,4),(3,2),(3,3),(5,2)\). All pass; for \((q,n)=(2,4)\), the enumeration finds \(105\) vertices, \(65\) maximal cliques, and \(20{,}436\) cliques including the empty clique. These computations independently corroborate—but do not establish—the all-prime-power theorem.

## Relationship to prior work
Prior commuting-graph work describes full matrix-algebra commuting graphs and rank-one matrix behavior, notably Dolinar–Kuzma–Oblak (2010 preprint/2012 journal) and Mohammadian (2010). The orthogonality graph of an associative ring (Bakhadly–Guterman–Markova, 2014 original/2015 translation) studies mutual annihilation and in particular graph diameters. The graph's projective point–hyperplane incidence description and local neighbor counts are known antecedents, **not** claimed as original. The present result identifies **every maximal clique** and computes the **entire labeled finite-field clique polynomial**, rather than distances, degrees, or local neighbor statistics. No absolute literature-priority claim is made; a relevant older orthogonality-graph full text could not be completely assessed.

## Limitations
Only nonzero rank-one square-zero matrices are vertices; results do not describe the full commuting graph of all matrices or higher-rank nilpotent elements. The graph is not the general directed zero-product graph. Maximal cliques are graph-theoretic (inclusion-maximal), while maximum cliques have greatest cardinality. The theorem holds for finite fields; for arbitrary infinite fields the maximal-clique set classification still makes sense, but the enumerative formulas are not asserted. The status here is a complete self-contained proof and computational corroboration, not independent validation or a guarantee of publication priority.

## References
1. G. Dolinar, B. Kuzma, P. Oblak, *On maximal distances in a commuting graph*, arXiv:1009.5543v1, public 28 September 2010; Electronic Journal of Linear Algebra 23 (2012), 243–256. https://arxiv.org/abs/1009.5543
2. A. Mohammadian, *On commuting graphs of finite matrix rings*, Communications in Algebra 38 (2010), 988–994, published online 11 March 2010. https://doi.org/10.1080/00927870902911771
3. B. R. Bakhadly, A. E. Guterman, O. V. Markova, *Graphs Defined by Orthogonality*, Zapiski Nauchnykh Seminarov POMI 428 (2014), 49–80; Journal of Mathematical Sciences 207 (2015), 698–717. https://www.mathnet.ru/rus/znsl6052 and https://doi.org/10.1007/s10958-015-2393-6
