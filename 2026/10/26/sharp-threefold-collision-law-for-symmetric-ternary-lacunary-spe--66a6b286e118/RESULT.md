# Sharp threefold collision law for symmetric ternary lacunary spectra

## Finding

Let \(\Lambda=\{0\}\cup\{\pm3^j:j\in\mathbb Z_{\ge0}\}\). For each integer \(D\), let \(r(D)\) count unordered multisets \(\{a,b,c\}\) of three members of \(\Lambda\), with \(a+b+c=D\), subject to \(a+b\ne0\), \(a+c\ne0\), and \(b+c\ne0\). Thus a pair that cancels is forbidden, but repeated nonzero entries are allowed. Then

\[r(0)=0,\qquad 0\le r(D)\le3\quad(D\in\mathbb Z),\]

and the exact saturation set is

\[\boxed{r(D)=3\iff D\in\{\pm5\cdot3^v,\pm7\cdot3^v:v\in\mathbb Z_{\ge0}\}.}\]

For \(D=5\) the three multisets are \(\{1,1,3\}\), \(\{-1,3,3\}\), \(\{-3,-1,9\}\). For \(D=7\), they are \(\{1,3,3\}\), \(\{1,-3,9\}\), and \(\{-1,-1,9\}\). Negation and scaling by \(3^v\) supply all other saturation examples.

## Assumptions and scope

The assertion is for all integer targets and the full infinite signed-power-of-three set, including zero. It counts unordered noncancelling three-element multisets, not ordered triples, not permutation-weighted coefficient sums and not arbitrary cubic representations with cancelling pairs. For a finitely supported trigonometric polynomial \(P(t)=\sum_{\lambda\in\Lambda}a_\lambda e^{i\lambda t}\), the primitive part of each Fourier coefficient of \(P^3\), after excluding all products with a cancelling frequency pair, has at most three distinct unordered monomial types. This interpretation is not a bound on the unrestricted Fourier coefficient or the Fourier extension norm.

## Proof

**Two-summand lemma.** Let \(B=\{0\}\cup\{\pm3^j:j\ge1\}\). For \(R\ne0\), there are at most two unordered pairs \(\{u,w\}\subset B\) satisfying \(u+w=R\), and exactly two if and only if \(R=\pm2\cdot3^j\) for some \(j\ge1\). Every integer has a unique finite balanced ternary expansion with digits in \(\{-1,0,1\}\). A sum of two different signed powers, or of a signed power and zero, is already such an expansion; any such pair is unique. An equal-power pair \(\{\varepsilon3^j,\varepsilon3^j\}\), where \(\varepsilon=\pm1\), has exactly the extra representation \(\{-\varepsilon3^j,\varepsilon3^{j+1}\}\), by the ternary carry identity \(2\varepsilon3^j=-\varepsilon3^j+\varepsilon3^{j+1}\). There are no other pairs. The case \(R=0\) consists only of forbidden cancelling pairs.

**Three-adic reduction.** No primitive triple sums to zero. Indeed, let \(e\) be its least exponent among nonzero entries. If exactly one term has exponent \(e\), the sum is \(\pm3^e\) modulo \(3^{e+1}\); if two do, their signs cannot be opposite, and the sum is \(\pm2\cdot3^e\) modulo \(3^{e+1}\). If all three do, the signs must all agree and the sum is \(\pm3^{e+1}\). In every case the sum is nonzero. The same argument shows, for \(D\ne0\) and \(v=\nu_3(D)\), that every primitive triple for \(D\) has entries all divisible by \(3^v\), apart from the single possible exceptional triple \(\{\operatorname{sgn}(D)3^{v-1},\operatorname{sgn}(D)3^{v-1},\operatorname{sgn}(D)3^{v-1}\}\), which exists only if \(v\ge1\) and \(D=\pm3^v\). Thus outside the latter special targets division by \(3^v\) bijects representations with those of the coprime-to-three integer \(d=D/3^v\).

**Residue classification.** By changing all signs, suppose \(d\equiv1\pmod3\). At least one entry is \(\pm1\). Three such entries either contain an opposite pair (forbidden) or sum to \(\pm3\) (wrong residue). With exactly one \(\pm1\) entry it must be \(1\); with exactly two they must both be \(-1\). Therefore all primitive triples lie in exactly one of the following families:

\[\{1,u,w\},\quad u,w\in B,\quad u+w=d-1\ne0;\qquad \{-1,-1,w\},\quad w=d+2\in B.\]

The first family has at most two members by the two-summand lemma; the second has at most one, since \(w\) is fixed. The side conditions are exactly those for noncancelling triples, because \(B\) contains no \(\pm1\) and the sum-zero pair in \(B\) is explicitly excluded. Hence \(r(d)\le3\).

For equality the first family must have two members, forcing \(d=1+2\varepsilon3^j\), where \(j\ge1\) and \(\varepsilon\in\{-1,1\}\); additionally the second family requires \(d+2=3+2\varepsilon3^j\) to be a signed power of three in \(B\). If \(\varepsilon=1\), this is \(3(1+2\cdot3^{j-1})\), a power of three only at \(j=1\), giving \(d=7\). If \(\varepsilon=-1\), the expression is \(-3(2\cdot3^{j-1}-1)\), a signed power of three only at \(j=1\), giving \(d=-5\). For \(j\ge2\), both positive factors in parentheses exceed one and are not divisible by three, so cannot be powers of three. Sign reversal yields \(d\in\{\pm5,\pm7\}\). The displayed examples establish that these cases indeed attain three.

Finally, for a special target \(D=\pm3^v\) with \(v\ge1\), the normalized coprime-to-three target is \(\pm1\). Its only primitive representation is the sign of \(\{-1,-1,3\}\), as the residue classification shows: the first family's pair would have zero sum. The exceptional equal-entry triple adds exactly one, for a total of two. These targets do not saturate. All integers are covered.

## Verification

Run `python verify.py`. It exhaustively enumerates primitive unordered triples for the finite truncations with exponents \(0\le j<J\), at \(J=3,4,5,7,11\), and checks the complete depth-specific set of targets with three representations. At depth \(11\) there are \(36\) such targets. Finite enumeration corroborates but cannot replace the proof for infinitely many frequencies.

## Relationship to prior work

Gonçalves and Ferreira (arXiv:2510.20934v1, publicly posted 2025-10-23) prove a sharp circle Fourier extension inequality for spectra with successive ratios strictly greater than three. Their Section 1.2 singles out the exact ratio-three spectrum as an unresolved endpoint involving additional two-term and mixed cubic collisions; their Lemma 4 uses the stricter lacunarity assumptions and does not establish the present bound and exact saturation set. Ciccone and Gonçalves (arXiv:2208.09441) establish a sharp result for spectra having the \(\mathrm{P}(3)\) property, which fails here, and discuss exceptions for ratios three, four and five. The available prior statements do not imply the complete primitive fiber theorem above. A known aggregate equal-coefficient sixth-moment formula for this spectrum does not determine the maximum of each separate primitive fiber or its locations.

## Limitations

The theorem neither gives a sharp Fourier extension constant nor supplies Bessel-integral bounds needed in the motivating Fourier extension problem. It does not cover other radices or arbitrary lacunary sequences. The no-cancelling-pair restriction and the distinction between unordered monomial types and multiplicity-weighted ordered convolution coefficients are essential. Unindexed historical work could contain an equivalent arithmetic classification; independent scientific verification has not been performed.

## References

1. F. Gonçalves and J. P. Ferreira, *On a Sharp Fourier Extension Inequality on the Circle with Lacunary Spectrum*, arXiv:2510.20934v1, first public 2025-10-23; https://arxiv.org/html/2510.20934v1 .
2. V. Ciccone and F. Gonçalves, *Sharp Fourier Extension on the Circle Under Arithmetic Constraints*, arXiv:2208.09441 (2022); https://arxiv.org/abs/2208.09441 .
