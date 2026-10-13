# A cyclic cubic symmetry of the quadratic four-square polynomial triple
## Finding
Let \(G(T)=16T^3+55T^2-64T+16\), the parameter cubic occurring in the quadratic classification of four-square polynomial triples. For any root \(k\), put \(K=\mathbb Q(k)\). Then \(K/\mathbb Q\) is a cyclic cubic extension with field discriminant
\[
\operatorname{Disc}(K)=91^2=8281.
\]
An explicit generator of \(\operatorname{Gal}(K/\mathbb Q)\) is induced by
\[
\tau(T)=\frac{4(7T-4)}{67T-36},\qquad
\tau^2(T)=\frac{4(9T-4)}{67T-28},\qquad \tau^3(T)=T.
\]
For the normalized triple
\[
a=X^2-\frac1{k^2},\qquad b=p^2a+2p,\qquad c=q^2a+2q,
\]
with
\[
\sigma=\frac{k(8k-3)}{4(2k-1)},\qquad p=\frac{\sigma+1}2,\qquad q=\frac{\sigma-1}2,
\]
the generator has a direct entry-level interpretation:
\[
\frac1{\tau(k)^2}=\frac{q^2}{k^2}-2q,
\qquad
\frac1{\tau^2(k)^2}=\frac{p^2}{k^2}-2p.
\]
Consequently, after the source's monic re-normalization of the distinguished entry, the Galois cycle is \(a\to c\to b\to a\).

## Assumptions and scope
The result concerns the parameter cubic and normalized quadratic real four-square polynomial triple of arXiv:2610.05565v1. The source proves that \(G\) is irreducible over \(\mathbb Q\), has three distinct real roots, and that those three roots correspond to the three choices of distinguished monic entry. No assertion is made here about higher-degree four-square polynomial triples or about coefficient fields of other constructions.

## Proof
Write
\[
\tau(T)=\frac{28T-16}{67T-36}.
\]
A direct polynomial identity is
\[
G(\tau(T))=\frac{512G(T)}{(67T-36)^3}.
\]
The projective matrix \(M=\begin{pmatrix}28&-16\\67&-36\end{pmatrix}\) satisfies
\[
M^2=\begin{pmatrix}-288&128\\-536&224\end{pmatrix},
\qquad M^3=512I,
\]
so the induced fractional-linear map has order dividing \(3\), with the displayed formula for \(\tau^2\). A root \(k\) of \(G\) cannot make any denominator vanish because \(G\) is irreducible over \(\mathbb Q\). Moreover the fixed-point equation \(\tau(T)=T\) is \(67T^2-64T+16=0\), whose discriminant is \(-192\). Since the three roots of \(G\) are real, \(\tau(k)\neq k\). Hence \(k,\tau(k),\tau^2(k)\) are the three roots of \(G\), all lying in \(K\). Thus \(K\) is the splitting field and \(\tau\) induces a generator of a cyclic Galois group of order \(3\).

For the entry action, substituting the source formulas for \(p\) and \(q\) and reducing with \(G(k)=0\) gives the exact identities
\[
\frac1{\tau(k)^2}-\left(\frac{q^2}{k^2}-2q\right)
=\frac{G(k)(784k^4-768k^3+93k^2+80k-16)}{64k^2(2k-1)^2(7k-4)^2}=0,
\]
and
\[
\frac1{\tau^2(k)^2}-\left(\frac{p^2}{k^2}-2p\right)
=\frac{G(k)(1296k^4-1280k^3+285k^2+48k-16)}{64k^2(2k-1)^2(9k-4)^2}=0.
\]
The source proves \(p,q\neq0\). Therefore
\[
c(X/q)=X^2-\frac1{\tau(k)^2},\qquad
b(X/p)=X^2-\frac1{\tau^2(k)^2},
\]
which identifies the Galois orbit with the three possible distinguished monic entries.

It remains to determine the field discriminant. Put \(y=16k\). Then \(y\) is an algebraic integer with minimal polynomial
\[
F(Y)=Y^3+55Y^2-1024Y+4096,
\]
whose polynomial discriminant is \((128\cdot91)^2\). The element
\[
z=\frac{y^2+119y+64}{128}
\]
is integral because it satisfies
\[
z^3+10z^2-361z+1702=0.
\]
The lattice with basis \(1,y,z\) therefore lies in \(\mathcal O_K\); its basis-change determinant from \(1,y,y^2\) is \(1/128\), so its discriminant is \(91^2\). Hence \(\operatorname{Disc}(K)\) divides \(91^2\).

Finally,
\[
F(Y-2)=Y^3+49Y^2-1232Y+6356
\]
is Eisenstein at \(7\), and
\[
F(Y-1)=Y^3+52Y^2-1131Y+5174
\]
is Eisenstein at \(13\). Thus both primes are totally ramified of degree \(3\) in \(K\). Because \(7\) and \(13\) are prime to \(3\), this ramification is tame and each contributes discriminant exponent \(2\). Hence \(7^2 13^2\) divides \(\operatorname{Disc}(K)\), forcing \(\operatorname{Disc}(K)=91^2\).

## Verification
The accompanying `verify.py` uses exact rational polynomial arithmetic only. It verifies the Möbius identity, the projective order-three relation, both entry-renormalization congruences modulo \(G\), the integral relation for \(z\), the discriminant calculation, and the two Eisenstein shifts. Its expected terminal line is `VERIFY_OK mobius_order=3 root_cycle=exact entry_cycle=a->c->b field_discriminant=8281 eisenstein=7,13`.

## Relationship to prior work
arXiv:2610.05565v1 gives \(G\), proves its irreducibility and positive square polynomial discriminant, and proves that its three roots correspond to the three choices of distinguished entry in the unique real quadratic equivalence class. Its Remark 3.7 identifies the other two roots indirectly through constant terms, but does not give a Galois-theoretic interpretation, an explicit order-three fractional-linear generator, or the field discriminant. arXiv:2607.06586v1 supplies the original root-based construction using the cubic \(Y^3-2Y^2+Y-4/91\) and notes its square discriminant. General cyclic-cubic theory explains why a square discriminant is compatible with a cyclic cubic field, but does not supply the source-specific generator or its exact action on the three normalized entries.

## Limitations
The cyclicity itself is not claimed as a new general theorem: for irreducible cubics, square-discriminant criteria are classical. The new content is the explicit source-specific Galois generator, its exact identification with the distinguished-entry cycle, and the exact maximal field discriminant. The discriminant proof uses the standard facts that an Eisenstein cubic is totally ramified locally and that a tame totally ramified cubic has local discriminant exponent \(2\).

## References
1. M. Jukić Bokun and A. Jurasić, *Four-square polynomial triples: quadratic classification and equal-degree obstructions*, arXiv:2610.05565v1, 2026.
2. A. Jurasić, *Four squares from three real polynomials*, arXiv:2607.06586v1, 2026.
