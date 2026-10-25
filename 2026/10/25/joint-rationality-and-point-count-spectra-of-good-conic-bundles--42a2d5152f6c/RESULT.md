# Joint rationality and point-count spectra of good conic bundles over finite fields

## Finding
For every fixed integer \(n\ge4\), there is a closed joint limiting distribution for rationality and the normalized number of rational points on good, balanced conic bundles over odd finite fields, in the finite-type parameter family of Hernandez [1].

Write \(S(X)=(\#X(\mathbb F_q)-(q+1)^2)/q\), and put \(I(X)=1\) if \(X\) is \(\mathbb F_q\)-rational, otherwise \(I(X)=0\). Set
\[
\begin{aligned}
F_n(z)&=2^{-n}[u^n]\left(\frac{\exp((z+z^{-1}-2)u)}{1-2u}+\exp((z-z^{-1})u)\right),\
R_n(z)&=2^{1-n}[u^n]\left(1+\frac{u^2z^{-2}}2+u^3z^{-1}\right)\frac{\exp((z-1)u)}{\sqrt{1-2u}}.
\end{aligned}
\]
Here \([u^n]\) extracts the coefficient of \(u^n\) in a formal power series, and \(z\) is an invertible formal variable. Then
\[
\lim_{q\to\infty}\mathbb E\big[z^{S(X)}v^{I(X)}\big]
=F_n(z)+(v-1)R_n(z).
\]
Thus \([z^s]F_n(z)\) is the limiting probability of excess \(s\), while \([z^s]R_n(z)\) is the limiting joint probability of excess \(s\) and rationality. The rationality marginal \(R_n(1)\) agrees with [1].

Moreover, every rational good conic bundle with these hypotheses has
\[
\#X(\mathbb F_q)\ge q^2+1.
\]
The bound is attained in the family over arbitrarily large odd finite fields: for every \(n\ge4\), its limiting joint mass is
\[
\lim_{q\to\infty}\Pr\big(I(X)=1,\ S(X)=-2\big)
=2^{-n}[u^{n-2}]\frac{\exp(-u)}{\sqrt{1-2u}}>0.
\]

## Assumptions and scope
Fix \(n\ge4\). A *good conic bundle* is a smooth projective surface \(X\) over \(\mathbb F_q\) with a morphism to \(\mathbb P^1\) whose geometric generic fiber is \(\mathbb P^1\) and whose \(n\) distinct geometric singular fibers each consist of two transverse projective lines. The *balanced* condition and sampling measure are exactly those of [1], Section 2.1 and its finite-type moduli space: sample rational points of the specified parameter space, not arbitrary equations or uniformly weighted abstract isomorphism classes. Only odd \(q\) are considered; limits hold for the fixed-characteristic and varying-odd-characteristic regimes justified in [1]. The event \(I(X)=1\) refers to rationality over \(\mathbb F_q\), not geometric rationality.

The geometric monodromy group is \(W(D_n)\), the even signed permutations of \(n\) letters, of order \(2^{n-1}n!\) [1,2]. For an element \(g\), each permutation cycle has a sign, namely the product of sign changes around the cycle; an odd number of negative cycles is excluded. A positive (resp. negative) fixed cycle is a permutation fixed point with positive (resp. negative) sign.

## Proof
**1. Exact point-count interpretation.** Every nonsingular fiber over a rational base point is a smooth conic over \(\mathbb F_q\), hence has \(q+1\) rational points. A geometrically nodal fiber over a rational base point has either two rational lines meeting transversely, with \(2q+1\) points, or two Galois-conjugate lines meeting at a unique rational point, with one point. Hence its deviation from a smooth fiber is \(+q\) or \(-q\), respectively. Geometric singular fibers above nonrational base points do not contribute. Therefore, for the signed Frobenius permutation \(g\),
\[
S(X)=\#\{\text{positive fixed cycles of }g\}
-\#\{\text{negative fixed cycles of }g\}.
\]
This equality holds over each finite field, without taking a limit.

**2. Passage to Weyl-group averages.** The monodromy theorem [2, Corollary 29] and the two forms of Chebotarev equidistribution used in [1, Sections 2.4--2.5 and 4] make the limiting law of every conjugacy-invariant statistic equal to the uniform average on \(W(D_n)\), with \(n\) fixed. The fixed-cycle statistic and the rationality indicator are conjugacy invariant. According to the classification in [1, Proposition 10], based on [3, Corollary 9], rationality occurs exactly when the signed-cycle type has (a) no negative cycles, (b) two negative singleton cycles and all others positive, or (c) one negative singleton and one negative two-cycle and all others positive.

**3. Every signed type.** Work temporarily in the full signed group \(W(B_n)\). For every permutation cycle of length \(\ell\), there are \(2^{\ell-1}\) sign assignments of each cycle sign. Mark a positive singleton by \(z\) and a negative singleton by \(z^{-1}\). The exponential formula for labeled cycles gives the unrestricted generating function
\[
\exp\left((z+z^{-1}-2)u\right)(1-2u)^{-1}.
\]
To project to an even number of negative cycles, average with the sign character. In the signed-character generating function all cycles of length at least two cancel, while a singleton has weight \(z-z^{-1}\); the resulting correction is \(\exp((z-z^{-1})u)\). Taking half the sum, extracting the coefficient of \(u^n\), multiplying by \(n!\), and dividing by \(2^{n-1}n!\) proves the displayed formula for \(F_n\).

**4. Rational types.** The exponential generating series for positive signed cycles alone is
\[
A(u,z)=\exp((z-1)u)(1-2u)^{-1/2},
\]
because each positive cycle of length \(\ell\) has \(2^{\ell-1}\) sign assignments, and singleton cycles are weighted by \(z\). Adding two negative singletons contributes the factor \(u^2z^{-2}/2\); adding a negative singleton and a negative two-cycle contributes \(u^3z^{-1}\), the latter coefficient including both odd sign assignments on the transposition. The rational classes have generating series
\[
\left(1+u^2z^{-2}/2+u^3z^{-1}\right)A(u,z).
\]
Coefficient extraction and division by the even signed group order prove \(R_n\). The joint generating polynomial is \(F_n+(v-1)R_n\): nonrational types have coefficient \(1\) in \(v\), rational types coefficient \(v\).

**5. Sharp boundary.** In the three rational signed-cycle types, negative singleton cycles number at most two; all remaining singleton cycles are positive. Thus \(S\ge-2\) for every rational bundle, which is exactly \(\#X(\mathbb F_q)\ge q^2+1\). Equality requires the type with two negative singletons and no positive singletons. Removing the two negative singletons yields the positive-signed derangement series
\[
\exp(-u)(1-2u)^{-1/2}
=\exp\left(\sum_{\ell\ge2}\frac{2^{\ell-1}u^{\ell}}{\ell}\right).
\]
The coefficient of \(u^{n-2}\) is strictly positive for \(n-2\ge2\), since the single positive \((n-2)\)-cycle contributes. Multiplying by the normalization \(2^{-n}\) gives the stated limiting joint mass. Chebotarev supplies examples for arbitrarily large eligible \(q\).

## Verification
A standalone pure-Python checker in `verify.py` enumerates every even signed permutation for \(4\le n\le7\) and compares both Laurent-polynomial distributions coefficient-by-coefficient to independently computed exponential-formula coefficients using exact rational arithmetic. It also checks the three rational-type total counts from [1] and the sharp-boundary mass. It returns `VERIFY_OK`. For instance, at \(n=4\), \(147\) of \(192\) even signed permutations have rational types, and \(12\) of \(192\) have rational type with excess \(-2\). These finite checks support the symbolic derivation but are not an infinite proof.

## Relationship to prior work
Hernandez [1] gives the signed-cycle rationality classification, Chebotarev framework, and *marginal* limiting rationality probability \(R_n(1)\), but not the rational-point-excess statistic or either Laurent generating polynomial. Hassett and Hernandez [2] establish the moduli construction and full Weyl-group monodromy; Yang [3] supplies the foundational Galois-cohomological signed-cycle restrictions. The formulas above are a joint arithmetic--birational refinement of those ingredients, not a new proof of their foundational theorems. The equality case turns the presence of two negative rational fibers into a sharp point-count boundary with an explicit positive limiting mass.

## Limitations
This is a limit theorem for fixed \(n\ge4\) in the particular balanced sampling space of [1], not a uniform counting result over isomorphism classes, not a statement for characteristic two, and not an explicit finite-field error bound. The lower bound is a *necessary* condition for rationality, not a sufficient condition. The monodromy, rationality classification and equidistribution theorems are cited inputs. No claim is made that a literature search proves uniqueness or settles all priority questions. Independent mathematical validation has not been performed.

## References
[1] Amanda Hernandez, *What are the odds that a conic bundle over a finite field is rational?*, arXiv:2607.15997v1 (public 17 July 2026), https://arxiv.org/abs/2607.15997.

[2] Brendan Hassett and Amanda Hernandez, *Moduli of conic surfaces over the line*, arXiv:2607.16006v1 (public 17 July 2026), https://arxiv.org/abs/2607.16006.

[3] Kaiqi Yang, *Potentially stably rational conic bundles over nonclosed fields*, arXiv:2410.21436 (first public October 2024), https://arxiv.org/abs/2410.21436.
