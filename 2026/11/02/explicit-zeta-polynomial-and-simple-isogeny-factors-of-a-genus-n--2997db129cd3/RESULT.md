# Explicit zeta polynomial and simple isogeny factors of a genus-nine Nakajima-extremal curve

## Finding
Let \(X/\mathbb F_2\) be the smooth projective normalization of
\[
 (x^7+x)(z^4+z)=x^8+x^6+x^4+x^2+1.
\]
This is the genus-\(9\) ordinary example in Proposition 7.2 of Tafazolian's 2026 construction. Its Hasse–Weil zeta function \(Z(X,T)=L_X(T)/((1-T)(1-2T))\) has the **exact numerator**
\[
\boxed{L_X(T)=(1-T+2T^2)(1+T+2T^2)^2
(1-T^2+4T^4)
(1-2T^2+T^4-8T^6+16T^8).}
\]
Consequently \(\#\operatorname{Jac}(X)(\mathbb F_2)=L_X(1)=1024\). Moreover its Jacobian has the \(\mathbb F_2\)-isogeny decomposition
\[
\operatorname{Jac}(X)\sim_{\mathbb F_2}
 E_{+}\times E_{-}^{2}\times A_2\times A_4,
\]
where \(E_{+}\) and \(E_{-}\) are elliptic curves with Frobenius traces \(+1\) and \(-1\), respectively, and \(A_2\), \(A_4\) are \(\mathbb F_2\)-simple abelian varieties of dimensions \(2\) and \(4\). Their Frobenius numerator factors are, respectively, \(1-T^2+4T^4\) and \(1-2T^2+T^4-8T^6+16T^8\). Explicit representatives of the elliptic factors are \(E_{-}:y^2+xy=x^3+1\) and \(E_{+}:y^2+xy=x^3+x^2+1\).

## Assumptions and scope
The base field is precisely \(\mathbb F_2\). The affine equation above is not assumed nonsingular: \(X\) always denotes its smooth projective normalization. The source proves that this curve is ordinary of genus \(9\) and belongs to a family with large geometric automorphism group. For completeness, the genus is also obtained from its degree-two Artin–Schreier cover of an elliptic curve, which has eight simple ramification poles. No assertion is made about analogous models with other parameters or base fields. The symbol \(T\) is a formal indeterminate and is unrelated to a geometric coordinate.

## Proof
**1. Smooth covering model and exceptional points.** Put \(E:y^2+xy=x^3+1\), \(H=x^3+1\), and \(N=x^4+x^3+1\). Over \(\mathbb F_2(E)\), set
\[
 z^2+z=\frac yx+\frac{N}{xH}.
\]
The identities, in \(\mathbb F_2[x]\),
\[
 H^3+N^2+xNH=x(x^8+x^6+x^4+x^2+1),
 \qquad xH^2=x^7+x,
\]
show, after eliminating \(y\), that the equation of \(X\) is the displayed plane model. Conversely, away from the denominators, \(y=x(z^2+z)+N/H\) recovers the elliptic coordinate; hence these models are birational. The Artin–Schreier right-hand side has eight distinct poles of order \(1\) at the geometric points above \(x=0\), \(x^3=1\), and the point at infinity. Over \(\mathbb F_{2^n}\), the places above these poles contribute exactly
\[
 B_n=2+2\gcd(3,2^n-1)
\]
points to \(X(\mathbb F_{2^n})\). The contribution is one point above each rational pole, because ramification is total. Since \(g(E)=1\), the Artin–Schreier Riemann–Hurwitz formula gives \(2g(X)-2=8\cdot2\), or \(g(X)=9\).

**2. Exact finite-field counts.** For \(K=\mathbb F_{2^n}\) and \(x\in K^\times\) with \(x^3\ne1\), let
\[
 b(x)=\frac{x^8+x^6+x^4+x^2+1}{x^7+x}.
\]
Thus, with the ramified fibers counted separately,
\[
 \#X(K)= B_n+\sum_{\substack{x\in K^\times\\x^3\ne1}}
 \#\{z\in K:z^4+z=b(x)\}.
\]
The attached `verify_zeta.py` enumerates **every** element of explicit binary-polynomial models of \(\mathbb F_{2^n}\), for each \(1\le n\le12\). In each field it verifies multiplicative inverses for every nonzero element, which in particular verifies that the chosen reduction polynomial defines a field. It independently calculates the same point counts through the elliptic Artin–Schreier model, using \(\operatorname{Tr}_{K/\mathbb F_2}(f)\). Both methods give
\[
 (N_1,\ldots,N_{12})=(4,8,4,24,44,8,116,312,508,808,2116,4056).
\]
This is a finite exhaustive calculation, not sampling.

**3. Unique Weil numerator.** Let \(s_n=2^n+1-N_n\), and write \(L_X(T)=\sum_{j=0}^{18}c_jT^j\), with \(c_0=1\). Newton's identities
\[
 kc_k=-\sum_{j=1}^k c_{k-j}s_j\qquad(1\le k\le9)
\]
produce \((c_0,\ldots,c_9)=(1,1,2,0,2,2,-4,-8,-11,5)\). The genus-nine Weil functional equation forces \(c_{18-k}=2^{9-k}c_k\) for \(0\le k\le8\). Therefore these nine exhaustive point counts uniquely determine the degree-\(18\) numerator, whose complete coefficient vector is
\[
 (1,1,2,0,2,2,-4,-8,-11,5,-22,-32,-32,32,64,0,256,256,512).
\]
Direct multiplication in \(\mathbb Z[T]\) gives the stated five factors (with one elliptic factor repeated). The counts for \(n=10,11,12\), not used to reconstruct the numerator, agree with the corresponding predicted Frobenius power sums.

**4. Simple isogeny factors.** A standard consequence of Tate's isogeny theorem over finite fields is that factorization of the rational Frobenius characteristic polynomial determines the isogeny factors, with multiplicities. The two degree-two factors have traces \(+1\) and \(-1\). The degree-four and degree-eight factors are irreducible over \(\mathbb Q\), as checked by exact integer-polynomial factorization in `verify_simple_factors.py`. Because they are irreducible factors of a Jacobian's Frobenius polynomial, their corresponding abelian isogeny factors are simple, of dimensions \(2\) and \(4\), and appear once. The repeated factor \((1+T+2T^2)^2\) gives two copies of \(E_-\). This establishes the asserted isogeny decomposition. Finally \(\#\operatorname{Jac}(X)(\mathbb F_2)=L_X(1)=1024\).

## Verification
Run `python3 verify_zeta.py` (Python standard library) and `python3 verify_simple_factors.py` (SymPy required). The first script verifies finite-field arithmetic and all \(12\) complete rational-point enumerations by two independent descriptions, the model-elimination identities, Newton's identities, the functional equation, the full numerator factorization, and the Jacobian order. Its final line is `VERIFY_OK`. The second verifies irreducibility of the degree-four and degree-eight factors and ends with `SIMPLE_FACTOR_VERIFY_OK`. Both scripts are standalone files embedded with this result. Exhaustive counts for degrees \(1\) through \(9\) are sufficient because the genus and functional equation are known independently.

## Relationship to prior work
S. Tafazolian, *Nakajima-extremal Artin–Schreier covers of ordinary elliptic curves in characteristic \(2\)*, arXiv:2609.14830v1, Proposition 7.2, supplies the genus-nine \(\mathbb F_2\) plane equation, the elliptic covering construction, ordinarity, and geometric automorphism group; these are **not** claimed as new. The present contribution is its explicit Hasse–Weil numerator, its full rational isogeny-factor pattern, and the resulting Jacobian order. Giulietti and Korchmáros, *Large \(2\)-groups of automorphisms of curves with positive \(2\)-rank* (arXiv:1104.5159), construct and analyze related but distinct genus-nine examples and large automorphism groups, not this enumerated \(\mathbb F_2\) zeta numerator. The Weil functional equation, Artin–Schreier ramification and Tate isogeny theorem are established general theory used in the proof rather than original contributions.

## Limitations
The calculation concerns this fixed \(\mathbb F_2\) model and its base extensions. The decomposition is up to \(\mathbb F_2\)-isogeny and does not determine integral endomorphism rings, polarizations, or explicit isogeny maps. The elliptic model and ramification data are adopted from and algebraically checked against the motivating paper. Novelty searches and accessible full-text comparisons do not constitute a proof of historical priority; a general statement or alternative model in less accessible literature might imply the same polynomial. No independent mathematical audit has been performed.

## References
1. S. Tafazolian, *Nakajima-extremal Artin–Schreier covers of ordinary elliptic curves in characteristic \(2\)*, arXiv:2609.14830v1 (first submitted 2026-09-13), especially Proposition 7.2. https://arxiv.org/abs/2609.14830
2. M. Giulietti and G. Korchmáros, *Large \(2\)-groups of automorphisms of curves with positive \(2\)-rank*, arXiv:1104.5159, Section 6.1. https://arxiv.org/abs/1104.5159
3. A. Weil, foundational zeta-function functional equation for smooth projective curves over finite fields; J. Tate, isogeny theorem for abelian varieties over finite fields (classical results).
