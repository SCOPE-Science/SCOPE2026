# Totient census of isolated singular loci in two-heavy weighted projective spaces
## Finding
For every integer \(r\ge2\), consider
\[
X_{r,a,b}=\mathbb P(\underbrace{1,\ldots,1}_{r},a,b),\qquad 1\le a\le b.
\]
Write \(\varphi\) for Euler's totient function and
\[
\Phi(r)=\sum_{m=1}^r\varphi(m).
\]
Among the members with at worst canonical singularities, exactly
\[
3\Phi(r)
\]
have zero-dimensional singular locus (where the empty singular locus is allowed). Among the members with at worst terminal singularities, exactly
\[
3\Phi(r-1)
\]
have zero-dimensional singular locus. Therefore exactly
\[
3\varphi(r)
\]
of the canonical-but-not-terminal boundary spaces have zero-dimensional singular locus.

More explicitly, put \(d=b-a\). On the canonical non-terminal boundary the zero-dimensional-singular-locus pairs are precisely
\[
d=r,\quad 1\le a\le2r,\quad \gcd(a,r)=1,
\]
or
\[
a=r+d,\quad 1\le d<r,\quad \gcd(d,r)=1.
\]
In particular, since \(\Phi(r)\sim 3r^2/\pi^2\), the proportion of zero-dimensional-singular-locus spaces tends to \(6/\pi^2\) in both the canonical and terminal families.

## Assumptions and scope
The base field is \(\mathbb C\), \(r\ge2\), and the weights are ordered \(1\le a\le b\). "Zero-dimensional singular locus" includes the smooth case. The result concerns ordinary weighted projective spaces, not fake weighted projective spaces.

## Proof
Weighted projective space is the quotient of \(\mathbb C^{r+2}\setminus\{0\}\) by the weighted \(\mathbb C^\times\)-action. Any point with at least one nonzero unit-weight coordinate lies in a smooth affine chart. Hence every singular point lies on the coordinate line where all unit-weight coordinates vanish, namely the weighted line with weights \(a,b\).

At a point of that line with both heavy coordinates nonzero, the stabilizer is the group of roots of unity whose order divides both \(a\) and \(b\), so the generic stabilizer has order \(\gcd(a,b)\). Thus the singular locus contains a curve exactly when \(\gcd(a,b)>1\). If \(\gcd(a,b)=1\), the generic point of the heavy line has trivial stabilizer; only its two coordinate endpoints can have nontrivial stabilizer, so the singular locus is zero-dimensional. Therefore
\[
\dim \operatorname{Sing}X_{r,a,b}\le0
\quad\Longleftrightarrow\quad
\gcd(a,b)=1.
\]

It remains to count coprime pairs inside the canonical and terminal regions. The local Reid--Tai age test on the two heavy charts gives the following closed form. With \(d=b-a\), canonicity is equivalent to
\[
0\le d\le r,\qquad 1\le a\le r+d,
\]
and terminality is equivalent to
\[
0\le d<r,\qquad 1\le a<r+d.
\]
For completeness, the first inequality comes from the chart \(\frac1b(1^r,a)\): at the first group element its age forces \(d\le r\) (strictly \(d<r\) for terminality), and once this holds all higher ages satisfy the same bound. The chart \(\frac1a(1^r,b)\) similarly gives \(a\le r+d\) (strictly \(a<r+d\)).

Now
\[
\gcd(a,b)=\gcd(a,a+d)=\gcd(a,d).
\]
For \(d=0\), coprimality occurs only at \(a=1\), contributing one canonical and one terminal pair. For fixed \(1\le d\le r\), the canonical range is \(1\le a\le r+d\). Splitting it into \(1\le a\le d\) and \(a=d+c\) with \(1\le c\le r\), the number of coprime choices is
\[
\varphi(d)+\#\{1\le c\le r:\gcd(c,d)=1\}.
\]
Summing over \(d=1,\ldots,r\), and denoting by \(K(r)\) the number of ordered coprime pairs \((c,d)\in[1,r]^2\), gives
\[
1+\Phi(r)+K(r).
\]
By symmetry about the diagonal, every coprime ordered pair off the diagonal occurs in a transposed pair, while the only coprime diagonal pair is \((1,1)\). The lower triangle \(1\le c\le d\le r\) contains exactly \(\Phi(r)\) coprime pairs, so
\[
K(r)=2\Phi(r)-1.
\]
Hence the canonical count is \(3\Phi(r)\).

The terminal region is the same triangular range with \(r\) replaced by \(r-1\): for \(d=0\) only \(a=1\) is coprime, and for \(1\le d\le r-1\) one has \(1\le a\le (r-1)+d\). The identical argument gives \(3\Phi(r-1)\).

Subtracting yields
\[
3\Phi(r)-3\Phi(r-1)=3\varphi(r).
\]
The explicit boundary description follows directly. On \(d=r\), coprimality is \(\gcd(a,r)=1\), giving \(2\varphi(r)\) choices in \(1\le a\le2r\). On the other boundary \(a=r+d\) with \(0\le d<r\), one has
\[
\gcd(a,b)=\gcd(r+d,r+2d)=\gcd(r,d),
\]
so exactly the \(\varphi(r)\) values \(1\le d<r\) coprime to \(r\) contribute. Finally, the classical summatory-totient asymptotic \(\Phi(r)\sim3r^2/\pi^2\), together with the total canonical and terminal counts \(3r(r+1)/2\) and \(3r(r-1)/2\), gives the limiting proportion \(6/\pi^2\).

## Verification
The proof is symbolic. The standalone script `verify_isolated_totient.py` independently enumerates every canonical and terminal pair for \(2\le r\le150\), tests \(\gcd(a,b)=1\), checks both totient formulas, and compares the explicit boundary description with direct enumeration. It returns `VERIFY_OK`. This finite regression is not used to justify the infinite statement.

## Relationship to prior work
Kasprzyk gives general canonical and terminal criteria for weighted projective spaces, including the quotient and toric descriptions underlying the local age test. The present theorem adds a closed all-dimensional arithmetic census for the natural two-heavy family after imposing the geometrically meaningful condition that the singular locus be zero-dimensional. Targeted searches for the same family together with isolated singularities, coprimality, summatory totients, or the formula \(3\Phi(r)\) did not locate an equivalent statement. The closest indexed weighted-projective result found concerns reflexive weighted-projective four-simplices and \(h^*\)-vectors, not the singular-locus census here.

## Limitations
The theorem is special to the family with exactly two possibly non-unit weights. It does not classify singular strata for three or more non-unit weights or for fake weighted projective spaces. The originality assessment is search-based: an equivalent result under substantially different notation could have been missed. The asymptotic uses the classical summatory-totient estimate and is not an effective error bound here.

## References
1. A. M. Kasprzyk, *Classifying terminal weighted projective space*, arXiv:1304.3029, first posted 2013-04-10. https://arxiv.org/abs/1304.3029
2. M. Reid, *Young person's guide to canonical singularities*, Proc. Sympos. Pure Math. 46 (1987), 345--414.
