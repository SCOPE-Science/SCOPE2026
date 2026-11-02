# Link-homology rigidity for two-curve Wahl singularities from branched involutions

## Finding

**Theorem.** Let \(B\) be a smooth connected projective complex curve of genus \(h\ge2\), and \(C\to B\) a connected double cover simply branched at \(r=2k\) distinct points, where \(k\ge1\). Write \(\iota\) for its deck involution. Contract the diagonal \(\Delta_C\) and graph \(\Gamma_\iota\) of \(\iota\) in \(C\times C\) using the negative-definite contraction of Du [1], and denote the resulting normal surface germ by \((X_{h,k},o)\) and its oriented link by \(M_{h,k}\). Put \(a=h-1\) and \(e=\gcd(2a,k)\). Then

\[
H_1(M_{h,k},\mathbb Z)\cong
\mathbb Z^{8a+6k+3}\oplus
\mathbb Z/(2e)\mathbb Z\oplus
\mathbb Z/(8a(a+k)/e)\mathbb Z.
\]

The **abstract first homology group alone** recovers both \(h\) and \(k\), hence the full weighted minimal-good-resolution graph and the Wahl local second Chern number. If \(b=\operatorname{rank}H_1(M_{h,k},\mathbb Z)\), \(T=|\operatorname{Tor}H_1(M_{h,k},\mathbb Z)|\), and \(u=(b-3)/2\), the inverse formula is

\[
a=\frac{u-\sqrt{u^2-3T/4}}2,
\qquad k=\frac{u-4a}{3},\qquad h=a+1.
\]

Moreover, **the integer values** of \(c_2^{\mathrm W}(X_{h,k})\) attained by this construction are exactly \(-3,-4,-5,\ldots\). The displayed formulas are uniform in \((h,k)\); neither the linking form nor a presentation of the full link group is needed.

## Assumptions and scope

The base curve and double cover are smooth, connected, and complex; the branch divisor is reduced and consists of \(2k\) points. Both parameters \(h\ge2\) and \(k\ge1\) are arbitrary. Du's contraction theorem [1] guarantees that the two-component exceptional divisor is analytically contractible. The first-homology computation concerns the oriented boundary of a small regular neighborhood of the exceptional divisor. No assertion is made about the first homology of unrelated normal surface singularities.

## Proof

**1. Existence and intersection matrix.** Riemann–Hurwitz gives
\[
2g(C)-2=2(2h-2)+2k=4a+2k=:d.
\]
The involution fixes exactly \(r=2k\) ramification points. At each fixed point its derivative on the curve is \(-1\), so \(\Delta_C\) and \(\Gamma_\iota\) meet transversely at exactly \(r\) points. Adjunction on \(C\times C\) gives self-intersection \(-d\) for each. Their intersection matrix is
\[
Q=\begin{pmatrix}-d&r\\r&-d\end{pmatrix}.
\]
Since \(d-r=4a>0\), this matrix is negative definite. The curves have genus \(g(C)=2a+k+1>1\), so the resulting good resolution has no exceptional rational \((-1)\)-curves and is minimal. For any integers \(a,k\ge1\), choose an arbitrary genus-\(a+1\) curve \(B\) and a reduced divisor \(D\) of \(2k\) points. The multiplication-by-two map on \(\operatorname{Pic}^0(B)\) is surjective, so \(\mathcal O_B(D)\) has a square root. The associated double cover exists and is connected because its branch locus is nonempty.

**2. Boundary homology.** Let \(N\) be a small regular neighborhood of the exceptional union \(E=\Delta_C\cup\Gamma_\iota\), with \(M=\partial N\). The space \(N\) retracts onto \(E\). Mayer–Vietoris for two genus-\(g\) surfaces meeting at \(r\) points gives
\[
H_2(N,\mathbb Z)=\mathbb Z^2,\quad
H_1(N,\mathbb Z)=\mathbb Z^{4g+r-1},\quad H^3(N,\mathbb Z)=0.
\]
Poincaré–Lefschetz duality identifies \(H_2(N,M;\mathbb Z)\) with \(H^2(N;\mathbb Z)\cong\mathbb Z^2\). The natural map \(H_2(N)\to H_2(N,M)\) is represented by \(Q\). Since \(H_1(N,M)\cong H^3(N)=0\), the pair long exact sequence yields
\[
0\to\operatorname{coker}(Q)\to H_1(M,\mathbb Z)\to
\mathbb Z^{4g+r-1}\to0.
\]
The final quotient is free, so this sequence splits as abelian groups. Smith normal form of the full-rank \(2\times2\) matrix \(Q\) has invariants \(\gcd(d,r)\) and \((d^2-r^2)/\gcd(d,r)\). Now
\[
4g+r-1=8a+6k+3,\quad
\gcd(d,r)=2\gcd(2a,k)=2e,\quad
d^2-r^2=16a(a+k),
\]
proving the homology formula. This derivation works even though the dual graph has \(r-1\) independent cycles, and does not assume a rational-homology-sphere link.

**3. Reconstruction from the abelian group.** Let \(b=8a+6k+3\) and \(T=16a(a+k)\). Set \(u=(b-3)/2=4a+3k\). Eliminating \(k\) gives
\[
3T/16=a(u-a).
\]
Hence \(a\) solves \(a^2-ua+3T/16=0\). Its discriminant is
\[
u^2-3T/4=(2a+3k)^2.
\]
Of the two roots, the smaller root is \(a\), because \(0<a<u/4\); the larger is \(u-a>3u/4\). Thus \(a\) is recovered uniquely, then \(k=(u-4a)/3\). The genus, vertex weights, number of edges and Wahl invariant follow. By Du's formula [1],
\[
c_2^{\mathrm W}(X_{h,k})=-\frac{r(d+r)}{d-r}
=-2k-\frac{2k^2}{a}.
\]
This proves that any two members of the construction with isomorphic integral first link homology have the same Wahl number and weighted resolution graph. Neumann's topological graph-reconstruction theorem [2] concerns the full link, not this stronger first-homology statement within a specific family.

**4. Exact integer spectrum.** Since \(a,k\ge1\), one always has \(c_2^{\mathrm W}<-2\), hence no integer greater than \(-3\) occurs. Conversely, for every integer \(N\ge3\), if \(N=2s\), set \(k=s-1\) and \(a=(s-1)^2\); if \(N=2s+1\), set \(k=s\) and \(a=2s^2\). In either case both parameters are positive and the last displayed formula equals \(-N\). The double-cover existence in step 1 realizes every such pair.

## Verification

Run `python3 verify.py` with the Python standard library. It checks exact Smith divisors, the reconstruction formula, and Wahl values for all \(1\le a,k\le100\), plus explicit realizations of the \(998\) integers \(3\le N\le1000\). It returns `VERIFY_OK`. These are arithmetic checks; the general theorem is proved above using topology, Riemann–Hurwitz, and a discriminant argument. Examples: \((a,k)=(2,1)\) gives \(H_1=\mathbb Z^{25}\oplus\mathbb Z/2\oplus\mathbb Z/48\) and \(c_2^{\mathrm W}=-3\); \((1,1)\) gives \(\mathbb Z^{17}\oplus\mathbb Z/2\oplus\mathbb Z/16\) and \(-4\); \((8,2)\) gives \(\mathbb Z^{79}\oplus\mathbb Z/4\oplus\mathbb Z/320\) and \(-5\).

## Relationship to prior work

Du [1] supplies the singularity construction and the formula for \(c_2^{\mathrm W}\), including negative examples and an unbounded sequence; neither is claimed here as new. Mumford and Neumann [2,3] establish foundational plumbing and link-topology relations. The additional statement concerns reconstruction of all exceptional numerical data **from the abelian group** \(H_1(M,\mathbb Z)\), rather than from the oriented link or its fundamental group, and its exact integer realization spectrum. The proof makes explicit the extra Mayer–Vietoris/Smith-form calculation and injectivity argument not given by the cited statements alone.

## Limitations

This theorem is restricted to two-curve diagonal/involution-graph contractions with positive branching and quotient genus at least two. It does not say first homology classifies arbitrary normal surface singularities or their analytic isomorphism classes. Indeed the same parameters permit complex moduli of the branch curve. The motivating preprint's abstract and independently available introductory synopsis, rather than its complete proof, were available for textual comparison; its full text could contain an implicit equivalent topological analysis. Definitive historical priority and independent mathematical assessment are outstanding.

## References

[1] Rong Du, *Negative Values of Wahl's Second Chern Number for Normal Surface Singularities*, arXiv:2610.25606v1 (first public preprint 2026-10-19), https://arxiv.org/abs/2610.25606.

[2] Walter D. Neumann, *A calculus for plumbing applied to the topology of complex surface singularities and degenerating complex curves*, Trans. Amer. Math. Soc. **268** (1981), 299–344. DOI:10.1090/S0002-9947-1981-0632532-8.

[3] David Mumford, *The topology of normal singularities of an algebraic surface and a criterion for simplicity*, Publ. Math. IHÉS **9** (1961), 5–22. DOI:10.1007/BF02698717.
