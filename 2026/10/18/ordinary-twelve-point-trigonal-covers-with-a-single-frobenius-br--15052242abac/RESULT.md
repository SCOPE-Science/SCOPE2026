# Ordinary twelve-point trigonal covers with a single Frobenius branch orbit

## Finding

For every integer \(n\ge5\) coprime to \(6\), consider all monic irreducible polynomials \(Q\in\mathbf F_3[x]\) of degree \(n\), and let \(C_Q\) be the smooth projective model of
\[
y^3-y=\frac{x^3-x}{Q(x)}.
\]
Each \(C_Q\) is a geometrically connected ordinary curve of genus \(2n-2\), has exactly twelve \(\mathbf F_3\)-points and \(\mathbf F_3\)-gonality three, and its degree-three cover has one closed branch point of degree \(n\). Its full automorphism group **over \(\mathbf F_3\)** is exactly the three deck translations. Among these curves, the exact number of distinct \(\mathbf F_3\)-isomorphism classes is
\[
\frac{1}{6n}\sum_{d\mid n}\mu(d)3^{n/d}.
\]
For \(n=5,7\), the numbers are respectively \(8\) and \(52\). This is an arithmetic isomorphism count for this explicitly defined subfamily; it is not a count of every ordinary trigonal curve of the corresponding genus.

## Assumptions and scope

Let \(k=\mathbf F_3\), let \(n\ge5\) satisfy \(\gcd(n,6)=1\), and let \(Q\) range over all monic irreducible members of \(k[x]\) of degree \(n\). Here \(\mu\) denotes the number-theoretic Möbius function, the \(3\)-rank means the rank of the geometric Jacobian's \(3\)-torsion, and *ordinary* means \(3\)-rank equal to genus. A rational automorphism or isomorphism is one defined over \(k\). No assertion is made about the full geometric automorphism group over \(\overline{k}\).

The numerator \(x^3-x\) is the distinguished monic polynomial vanishing at every finite rational base point. The irreducible denominator forces all geometric ramification poles into one Frobenius orbit, making the family a natural arithmetic test of simultaneously maximal gonality-relative rational points, ordinary reduction, and rigidity of the distinguished map.

## Proof

**Smooth connected cover and ramification.** The roots of \(Q\) are \(n\) distinct geometric points, because finite fields are perfect, and none is a root of \(x^3-x\), since \(n>1\). The rational function on the right has exactly \(n\) simple poles and is regular at infinity (with zero there of order \(n-3\)). Its pole orders are prime to three; therefore it is not an Artin–Schreier coboundary and defines a geometrically connected degree-three Galois extension. The smooth projective normalization is the stated curve. Each pole is totally ramified with lower jump one and different exponent four, and there is no other ramification. The wild Riemann–Hurwitz formula gives
\[
2g(C_Q)-2=-6+4n,\qquad g(C_Q)=2n-2.
\]
The branch support is the single closed point of degree \(n\) given by \(Q=0\), so geometric Frobenius cyclically permutes its \(n\) geometric points.

**Points, gonality, and ordinarity.** All four points of \(\mathbf P^1(k)\), namely \(0,1,-1,\infty\), are unramified. The right-hand function vanishes at all four, and over \(k\) every element satisfies \(y^3-y=0\). Thus each rational base point has three rational preimages and \(\#C_Q(k)=12\). The displayed map has degree three. Every degree-\(d\) morphism to \(\mathbf P^1\) over \(k\) gives at most \(4d\) rational points, so the gonality is exactly three and the point count attains this gonality-relative upper bound. The Deuring–Shafarevich formula for \(n\) totally ramified poles gives \(3\)-rank \(2(n-1)=g(C_Q)\), proving ordinarity.

**Uniqueness of the trigonal map.** By the Castelnuovo–Severi inequality, two non-equivalent degree-three maps from a smooth curve to \(\mathbf P^1\) would force genus at most \((3-1)(3-1)=4\). Indeed, if their combined map has degree three, then the maps are equivalent by a projectivity; otherwise the combined map is birational to its image and the inequality applies. Here \(g(C_Q)\ge8\). Consequently, every \(k\)-isomorphism \(C_Q\to C_{Q'}\) descends to a projectivity \(M\in\operatorname{PGL}_2(k)\) of the base; the uniqueness applies in particular to automorphisms.

**Arithmetic rigidity.** For an isomorphism, the Artin–Schreier generators satisfy \(y'\mapsto u y+h(x)\), where \(u\in k^\times\) and \(h\in k(x)\), so
\[
\frac{M(x)^3-M(x)}{Q'(M(x))}
-u\frac{x^3-x}{Q(x)}=h(x)^3-h(x).
\]
The two terms on the left have no poles of order larger than one, even after projectivity. Every pole of \(h^3-h\), if it has one, has order divisible by three. Therefore \(h\) has no poles, hence is constant in \(k\), and \(h^3-h=0\). Accordingly the two rational functions are equal up to \(u\). Their zero divisors have simple zeros at \(0,1,-1\), and a zero of order \(n-3\ge2\) at infinity. The unique multiple zero forces \(M(\infty)=\infty\), so \(M(x)=ax+b\) for \(a\in k^\times\) and \(b\in k\). Equality of their pole divisors yields
\[
Q'(ax+b)=a^nQ(x).
\]
Conversely, this polynomial equality implies the two covers are isomorphic, because \((ax+b)^3-(ax+b)=a(x^3-x)\) and \(a^{1-n}=1\) for odd \(n\) in \(k^\times=\{1,-1\}\). Thus \(u=1\), and **two members are \(k\)-isomorphic if and only if their monic denominators lie in the same orbit of the six-element affine group \(\operatorname{AGL}_1(k)\)**.

**Free action and exact count.** Suppose a nonidentity affine base transformation fixes one monic irreducible \(Q\). On the \(n\) distinct roots of \(Q\), it commutes with the transitive Frobenius \(n\)-cycle. The centralizer of an \(n\)-cycle in the symmetric group is cyclic of order \(n\). Since the affine transformation has order dividing \(6\), its action on those roots is trivial when \(\gcd(n,6)=1\). It then fixes at least three geometric base points and must be the identity, a contradiction. Hence all affine orbits have size six. The classical Möbius-inversion count of monic degree-\(n\) irreducibles is \(n^{-1}\sum_{d\mid n}\mu(d)3^{n/d}\); division by six gives the formula. For a fixed \(Q\), the only affine base automorphism is the identity, and the only automorphisms above it are the three translations \(y\mapsto y+c\) with \(c\in k\). This gives \(\operatorname{Aut}_k(C_Q)\cong C_3\).

## Verification

The included `verify_classification.py` checks irreducibility with the polynomial Rabin criterion, enumerates all monic irreducibles in degrees five and seven over \(\mathbf F_3\), and checks every six-element affine orbit independently at coefficient level. On execution with ordinary Python 3 it reports, respectively, \(48\) polynomials in \(8\) free orbits and \(312\) polynomials in \(52\) free orbits. A first representative in degree five is \(Q=x^5+2x^4+1\). These finite checks corroborate the formula for two small parameters; the proof for every qualifying \(n\) is the algebraic argument above, not an extrapolation from the checks.

## Relationship to prior work

The sharp \(d(q+1)\) bound and the existence of large-genus curves attaining it are prior results (Faber–Vermeulen and Vermeulen). The genus and \(p\)-rank formulas and moduli interpretation for Artin–Schreier covers are classical and treated by Ho–Pries. A later result of Tafazolian–Kazemifard establishes a broad numerical existence theorem for Artin–Schreier curves without extra geometric automorphisms. None of these is claimed as new here. The new claim is the *joint*, explicitly enumerated arithmetic family with full rational splitting, ordinary Jacobians, a Frobenius-transitive degree-\(n\) branch divisor, and exactly computed \(\mathbf F_3\)-isomorphism classes. The two-sided isomorphism rigidity and free affine orbit calculation are the critical additional deductions.

## Limitations

The result concerns \(n\ge5\) with \(\gcd(n,6)=1\) only, and is an arithmetic, not geometric, isomorphism classification of the displayed subfamily. It neither classifies all trigonal curves nor asserts that their geometric automorphism groups are always \(C_3\). Publication priority of this exact subfamily count has not been independently certified; a previously unindexed specialized construction could imply it. The executable checks cover degrees five and seven, not all degrees.

## References

- H. Charalambous, K. Karagiannis, A. Kontogeorgis, *The Relative Canonical Ideal of the Kummer–Artin Schreier–Witt Family of Curves*, arXiv:1905.05545 (first posted 2019-05-14); Ann. Inst. Fourier 73 (2023), 1085–1113, doi:10.5802/aif.3543. Primary MSC 14H10; the canonical-ideal criterion excludes trigonal curves.
- X. Faber, F. Vermeulen, *On abelian covers of the projective line with fixed gonality and many rational points*, arXiv:2202.12969 (2022), especially Theorem 1.2 and Lemma 2.1.
- F. Vermeulen, *Curves of fixed gonality with many rational points*, arXiv:2102.00900 (2021), Theorem 1.1.
- A. M. Ho, R. Pries, *A Mass Formula for Artin–Schreier Curves Over Finite Fields*, arXiv:2203.10187 (2022), Sections 2 and 5–7.
- S. Tafazolian, A. Kazemifard, *Artin–Schreier curves of prescribed \(p\)-rank without extra automorphisms*, arXiv:2610.13279 (2026), Theorem 1.1 and Section 5; later contextual work, not the chronological source for this direction.
