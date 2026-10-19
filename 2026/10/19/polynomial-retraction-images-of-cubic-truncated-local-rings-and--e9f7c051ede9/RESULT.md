# Polynomial retraction images of cubic truncated local rings and the binary jet exception

## Finding

Let \(q\ge2\) be a prime power and let \(R=\mathbb F_q[t]/(t^3)\). A *polynomial function* is a set map \(F:R\to R\) induced by evaluating a polynomial in \(R[X]\), and a *polynomial retraction* is such a function satisfying \(F\circ F=F\). The number of **distinct functions**, not the number of representing polynomials, is counted throughout. Write \(C_a=a+tR\), a residue fiber of cardinality \(Q=q^2\), and put

\[
H_q=\begin{cases}q^4,&q=2,\\q^5,&q>2.\end{cases}
\]

**Image characterization.** A subset \(Y\subseteq R\) is the image of a polynomial retraction if and only if \(Y\ne\varnothing\) and, for every \(a\in\mathbb F_q\), the intersection \(Y\cap C_a\) is either empty, a singleton, or the entire fiber \(C_a\).

**Exact multiplicities.** Suppose an admissible image occupies \(k\) residue fibers, among which exactly \(s\) are full and \(k-s\) are singletons, where \(1\le k\le q\) and \(0\le s\le k\). There are exactly

\[
\bigl(k-s+sH_q\bigr)^{q-k}
\]

polynomial retractions with precisely that **specified** image. Thus the number of admissible image subsets is \((q^2+2)^q-1\), and the complete image-cardinality enumerator is

\[
I_q(z)=\sum_{k=1}^{q}\binom qk\sum_{s=0}^{k}\binom ks(q^2)^{k-s}\bigl(k-s+sH_q\bigr)^{q-k}z^{k+s(q^2-1)}.
\]

Its coefficient of \(z^r\) is the number of polynomial retractions of image cardinality \(r\). The identity is the unique full-rank retraction. Every proper retraction has image cardinality at most \(q^3-q^2+1\), and exactly \(q^3\) retractions attain this sharp bound; exactly \(q^3\) retractions have rank one (the constant maps).

## Assumptions and scope

All assertions hold for every prime power \(q\), including characteristic two and nonprime fields, and concern the equal-characteristic finite chain ring \(\mathbb F_q[t]/(t^3)\). Polynomial self-maps are not presumed additive or ring homomorphisms. Composition-idempotence \(F\circ F=F\) is distinct from the condition that an element of the ring is idempotent. The base field \(\mathbb F_q\) sits canonically inside \(R\); its residue fibers partition the \(q^3\) elements of \(R\).

## Proof

**1. Polynomial jets on a residue fiber.** For a polynomial \(P\in R[X]\), write each element of \(C_a\) uniquely as \(a+ts+t^2r\) with \(s,r\in\mathbb F_q\). Taylor expansion with the second Hasse derivative gives the exact congruence

\[
P(a+ts+t^2r)=P(a)+(ts+t^2r)P'(a)+t^2s^2P^{[2]}(a)\pmod{t^3}.
\]

When the output residue is prescribed to be \(b\), the resulting function has the form

\[
(s,r)\longmapsto \bigl(u+\alpha s,\;w+vs+\beta s^2+\alpha r\bigr),
\]

where \(u,\alpha,w,v,\beta\in\mathbb F_q\) are arbitrary. These parameters are attainable as jets of \(P\) at \(a\), by taking the corresponding zeroth, first and second Hasse derivatives. For \(q>2\), the three functions \(1,s,s^2\) on \(\mathbb F_q\) are linearly independent, so this is a unique description with \(q^5\) distinct functions for a fixed output residue. For \(q=2\), the polynomial functions \(s^2\) and \(s\) coincide; precisely \(v+\beta\) is detectable, leaving \(2^4\) distinct functions. The two coordinate functions in this display are unique for distinct \((u,\alpha,w,v+\beta)\) in the binary case.

For distinct \(a\in\mathbb F_q\), the ideals \((X-a)^3\subset R[X]\) are pairwise comaximal because differences between field elements are units of \(R\). The Chinese remainder theorem therefore lets us prescribe the second-order polynomial jets at every residue independently. Hence every independent selection of the displayed fiber maps (with arbitrary output residues) is realized by a *single* polynomial in \(R[X]\).

**2. Fixed residue fibers of an idempotent map.** Reduction modulo \(t\) of a polynomial function defines a set map \(\rho:\mathbb F_q\to\mathbb F_q\), and \(F^2=F\) forces \(\rho^2=\rho\). Thus the occupied residue fibers are exactly the fixed points of \(\rho\). For a fixed residue \(a\), the local map has \(b=a\) and satisfies idempotence. Its first coordinate \(s\mapsto u+\alpha s\) obeys \(\alpha^2=\alpha\) and \(\alpha u=0\), so \(\alpha\in\{0,1\}\).

If \(\alpha=1\), then \(u=0\); the second coordinate is \(r\mapsto r+g(s)\), where \(g(s)=w+vs+\beta s^2\). Idempotence yields \(g(s)=0\) as a function for all \(s\), and the whole fiber map is the identity. If \(\alpha=0\), the first coordinate becomes the constant \(u\) and the second coordinate is \(g(s)\); idempotence implies \(g(s)=g(u)\) for every \(s\). The whole fiber map is therefore a constant. Both possibilities are polynomial maps, with exactly \(1\) identity function and exactly \(q^2\) distinct constant functions per fixed residue. The argument uses functions rather than formal coefficient equality and remains valid when \(q=2\).

**3. Images and multiplicities.** Every occupied residue fiber is fixed under \(\rho\), and by Step 2 its image is either the entire fiber or one point. Conversely, prescribe an arbitrary nonempty set of occupied residues, declaring each either full or represented by one chosen point. On occupied residues choose identity or the required constant. On each of the remaining \(q-k\) residue fibers, choose independently a target occupied residue: there are \(k-s\) singleton targets with one compatible constant map each and \(s\) full targets with \(H_q\) possible polynomial maps each, by Step 1. CRT gluing gives a retraction, and different function choices give distinct retractions. Therefore the number onto a particular image is \((k-s+sH_q)^{q-k}\).

For each residue there are \(1\) empty choice, \(q^2\) choices of singleton, or \(1\) full choice. Independence gives \((q^2+2)^q-1\) nonempty images. Choosing their occupied residues, full residues and singleton values gives the displayed rank polynomial.

**4. Extremal ranks.** An image has cardinality \(k+s(q^2-1)\). The unique possibility attaining \(q^3\) is every fiber full, yielding the identity. The maximum below full cardinality is obtained by taking all \(q\) fibers occupied and exactly one singleton, giving \(q^3-q^2+1\). There are \(q\cdot q^2=q^3\) choices of that singleton image, and each has exactly one retraction because no residue is unoccupied. At cardinality one, only constant maps occur, one per element of \(R\), again \(q^3\) maps.

## Verification

The standalone script `verify_cubic_retracts.py` evaluates local jets over \(\mathbb F_2\), \(\mathbb F_3\) and \(\mathbb F_4\), checking that the distinct local polynomial functions number respectively \(16,243,1024\). It independently enumerates all \(1024\) polynomial self-maps of \(\mathbb F_2[t]/(t^3)\), checks composition idempotence pointwise on all eight ring elements, and compares each image-class coefficient with the formula. The resulting rank polynomial is

\[
I_2(z)=8z+16z^2+32z^4+8z^5+z^8,
\]

whose coefficients sum to \(65\). For \(q=3\), the formula predicts total \(193294\) polynomial retractions; this larger count is an algebraic consequence of the formula, not an exhaustive computational census. Reproduce the finite checks with `python3 verify_cubic_retracts.py` using Python 3 and no external packages. The proof, not finite enumeration, establishes the assertions for all prime powers.

## Relationship to prior work

Al-Maktry's 2020 public preprint studies polynomial functions and polynomial permutations on finite split square-zero dual-number algebras, providing important interpolation and derivative context. Al-Ezeh, Al-Maktry and Frisch (2019) similarly develop polynomial-function descriptions for dual numbers over residue-class rings. Those objects have a square-zero radical and are not the present chain ring with \(t^2\ne0\). Aichinger's 2001 near-ring theorem characterizes ideal ranges of certain near-ring idempotents; it does not provide the present arbitrary-subset image classification, per-image multiplicities, or finite-field binary jet exception. The exact rank/image classification above concerns **composition-idempotent polynomial functions**, not idempotent algebra endomorphisms or mere counts of polynomial functions. Standard CRT and Hasse–Taylor identities are used as known tools, not claimed as new.

## Limitations

The result is restricted to the ring \(\mathbb F_q[t]/(t^3)\) and makes no claim for mixed-characteristic length-three chain rings or for higher nilpotency indices. All polynomial maps are unary and evaluated with coefficients in the same commutative ring. Equivalence with an overlooked rank/image enumeration in older finite-ring, near-ring or polynomial-function literature is a remaining originality risk; relevant broader bibliography was not exhaustively available. Finite computations do not certify the infinite-family statement.

## References

- A. A. A. Al-Maktry, *Polynomial functions over dual numbers of several variables*, arXiv:2002.01304v1, publicly posted 2020-02-03; https://arxiv.org/abs/2002.01304 .
- H. Al-Ezeh, A. A. Al-Maktry, S. Frisch, *Polynomial functions on rings of dual numbers over residue class rings of the integers*, arXiv:1910.00238v1, publicly posted 2019-10-01; https://arxiv.org/abs/1910.00238 .
- E. Aichinger, *On near-ring idempotents and polynomials on direct products of Omega-groups*, Proceedings of the Edinburgh Mathematical Society 44 (2001); DOI:10.1017/S0013091599001418.
- S. Frisch, *Polynomial functions on finite commutative rings*, 1999, bibliographic/abstract evidence only.
