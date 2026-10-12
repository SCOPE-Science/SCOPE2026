# Base-point-free and very-ample spectra on Festi's Picard-\(U\) K3 surface
## Finding
Let \(X\) be the Picard-rank-two K3 surface used by Festi to realize the order-three automorphism bound for every degree \(2d\) with \(d>1\). Choose the source's basis \(e,f\) of
\[
\operatorname{Pic}(X)\cong U,\qquad e^2=f^2=0,\qquad e\!\cdot\! f=1,
\]
so that \(F=f\) is the elliptic fiber, \(O=e-f\) is the unique effective \((-2)\)-curve, and the ample cone is
\[
\{xe+yf:y>x>0\}.
\]
For every integer \(d>1\), the primitive ample classes \(D\) with \(D^2=2d\) are exactly
\[
D_{x,y}=xe+yf
\]
where
\[
xy=d,\qquad 1\le x<y,\qquad \gcd(x,y)=1.
\]
Consequently their number is \(2^{\omega(d)-1}\), where \(\omega(d)\) is the number of distinct prime divisors of \(d\).

Among these classes,
\[
D_{x,y}\text{ is base-point free}\iff x\ge2,
\]
and
\[
D_{x,y}\text{ is very ample}\iff x\ge3.
\]
If \(x=1\), the base locus is exactly the section \(O\). If \(x=2\), the system is base-point free but its restriction to the smooth elliptic fiber has degree \(2\), so the induced morphism is not an embedding.

Thus Festi's uniform choice \(e+df\) is ample for every \(d>1\) but is never base-point free: its fixed curve is \(O\). The first primitive base-point-free ample class in this family is
\[
2e+3f,\qquad (2e+3f)^2=12,
\]
and the first primitive very ample class is
\[
3e+4f,\qquad (3e+4f)^2=24.
\]
More precisely, if \(N_{\mathrm{amp}}(d)\), \(N_{\mathrm{bpf}}(d)\), and \(N_{\mathrm{va}}(d)\) denote the three counts, then
\[
N_{\mathrm{amp}}(d)=2^{\omega(d)-1},\qquad
N_{\mathrm{bpf}}(d)=2^{\omega(d)-1}-1,
\]
and
\[
N_{\mathrm{va}}(d)=2^{\omega(d)-1}-1-\varepsilon(d),
\]
where \(\varepsilon(d)=1\) exactly when \(v_2(d)=1\) and \(d>2\), and is \(0\) otherwise.

## Assumptions and scope
The statement is over \(\mathbb C\) and concerns the specific Picard-\(U\) K3 surface and ample chamber used in Festi's degree-\(2d\) construction. The order-three automorphism acts trivially on the Picard lattice in this example, so every class in the classification is invariant as a divisor class. The result classifies primitive ample classes on this fixed surface by their complete linear systems; it does not claim a classification for all K3 surfaces with an order-three automorphism.

## Proof
Write \(D=xe+yf\). Since \(D^2=2xy\), the condition \(D^2=2d\) is \(xy=d\). Festi's ample-cone calculation gives \(y>x>0\). Primitivity in the lattice basis is exactly \(\gcd(x,y)=1\). Conversely, every such pair gives a primitive ample class. Because coprimality forces every prime-power divisor of \(d\) to lie wholly in one of \(x\) or \(y\), the ordered coprime factorizations are obtained by assigning each of the \(\omega(d)\) prime-power blocks to one factor. Swapping the factors identifies complementary assignments, and \(d>1\) prevents a coprime diagonal pair. Hence the number of ample classes is \(2^{\omega(d)-1}\).

For base points, use the K3 base-divisor criterion of Mayer--Saint-Donat: a big and nef line bundle has base points exactly when it can be written
\[
mE+C,
\]
with \(m\ge2\), \(E\) a smooth elliptic curve, \(C\) a smooth rational curve, and \(E\!\cdot\!C=1\); then the base locus is exactly \(C\). In \(U\), an isotropic class \(ae+bf\) satisfies \(ab=0\). A smooth elliptic curve is nef, while \(e\!\cdot\!O=-1\), so the only primitive nef isotropic class is \(F=f\). Likewise a \((-2)\)-class satisfies \(ab=-1\), so the only effective one is \(O=e-f\). Since
\[
D=xO+(x+y)F,
\]
the Mayer--Saint-Donat form occurs exactly when \(x=1\); in that case
\[
D=O+(y+1)F
\]
and the base locus is exactly \(O\). Therefore \(D\) is base-point free exactly for \(x\ge2\).

Now assume \(x\ge2\). The class is primitive and ample. Saint-Donat's projective-model criterion says that, for such a polarization of square at least \(4\), failure of very ampleness can occur through an elliptic curve \(E\) with \(D\!\cdot\!E=2\) (the divisible exceptional case cannot occur because \(D\) is primitive). The only smooth elliptic class is \(F\), and
\[
D\!\cdot\!F=x.
\]
Thus \(x=2\) is exactly the non-very-ample base-point-free case, while every \(x\ge3\) class is very ample. The failure at \(x=2\) is also visible directly: \(D|_F\) has degree \(2\), and a degree-two line bundle on an elliptic curve cannot embed \(F\).

The first base-point-free class requires a coprime factorization \(d=xy\) with \(2\le x<y\), whose minimum is \((x,y)=(2,3)\), giving \(d=6\) and square \(12\). The first very ample class requires \(3\le x<y\), whose minimum coprime pair is \((3,4)\), giving \(d=12\) and square \(24\).

For the counting refinements, the unique factor pair with \(x=1\) accounts for the subtraction in \(N_{\mathrm{bpf}}(d)\). A coprime pair with \(x=2\) exists exactly when \(d=2m\) with odd \(m>1\), equivalently \(v_2(d)=1\) and \(d>2\), giving the additional subtraction in \(N_{\mathrm{va}}(d)\).

## Verification
The accompanying script checks the lattice identities, enumerates coprime factor pairs, and verifies the three counting formulas for \(2\le d\le5000\), including the first base-point-free and very ample thresholds. This finite replay is only a consistency check: the proof above establishes the formulas for every \(d>1\) by prime-power factorization and the K3 linear-system criteria.

## Relationship to prior work
Festi proves that the Picard-\(U\) example has ample cone \(y>x>0\) and uses the single class \(e+df\) to produce a primitive polarization of every square \(2d\), \(d>1\). The source does not classify all primitive classes of a fixed degree by global generation or very ampleness, nor point out that its uniform class \(e+df\) has the section \(O\) as fixed base curve. The Mayer--Saint-Donat and Saint-Donat theorems supply general K3 linear-system criteria; the new step is their exact specialization to this order-three Picard-\(U\) surface together with the resulting arithmetic count and sharp degree thresholds.

## Limitations
The result concerns complete linear systems of primitive ample classes on one fixed Picard-\(U\) K3 surface. It does not determine equations of the embeddings for \(x\ge3\), the precise rational-scroll model in every \(x=2\) case, or moduli-level counts up to isomorphism of polarized surfaces. The originality comparison cannot exclude an older equivalent observation phrased purely in the classical theory of elliptic K3 surfaces.

## References
1. D. Festi, *Polarized K3 surfaces with an automorphism of order 3 and low Picard number*, arXiv:2306.17539v1; Journal of the Mathematical Society of Japan 77 (2025), 619--628, DOI 10.2969/jmsj/91759175.
2. U. Rieß, *Base divisors of big and nef line bundles on irreducible symplectic varieties*, Annales de l'Institut Fourier 73 (2023), 609--633, DOI 10.5802/aif.3530. The opening K3 proposition records the Mayer criterion used above.
3. B. Saint-Donat, *Projective models of K-3 surfaces*, American Journal of Mathematics 96 (1974), 602--639, DOI 10.2307/2373709.
