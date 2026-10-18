# A simple prime-order Jacobian in the smallest rigid characteristic-five Artin–Schreier stratum

## Finding

Let \(X/\mathbb F_5\) be the smooth projective model of
\[
y^5-y=x^4+x^2+x.
\]
The curve has genus \(6\) and \(5\)-rank \(0\). Its complete Hasse–Weil numerator is
\[
\begin{aligned}
L_X(T)={}&1-10T^2+10T^3+55T^4-25T^5-175T^6\\
&-125T^7+1375T^8+1250T^9-6250T^{10}+15625T^{12}.
\end{aligned}
\]
This polynomial is irreducible over \(\mathbb Q\); consequently \(\operatorname{Jac}(X)\) is **simple over \(\mathbb F_5\)**. Furthermore,
\[
\#\operatorname{Jac}(X)(\mathbb F_5)=L_X(1)=11731,
\]
which is prime. Hence \(\operatorname{Jac}(X)(\mathbb F_5)\) is cyclic of prime order \(11731\). Also \(\#X(\mathbb F_5)=\#X(\mathbb F_{25})=6\), so the curve has no closed points of degree two over \(\mathbb F_5\).

## Assumptions and scope

All assertions concern exactly the displayed model over the prime field \(\mathbb F_5\), and the geometric smooth projective completion, not the singular projective closure of its affine equation. Tafazolian and Kazemifard's Lemma 3.3 chooses this model in the first permitted \(5\)-rank-zero, no-extra-automorphism genus stratum in characteristic \(5\): their theorem proves that its full geometric automorphism group is \(C_5\). The geometric automorphism and genus conclusions are used as published background, not asserted as new results.

## Proof

**Genus and point at infinity.** The Artin–Schreier cover of \(\mathbb P^1\) has degree \(5\). Its rational function \(f(x)=x^4+x^2+x\) has exactly one pole, of order \(4\), at infinity, prime to the characteristic. Therefore the cover is geometrically irreducible, totally ramified over infinity, and has precisely one rational point above infinity over every extension \(\mathbb F_{5^n}\). The Artin–Schreier genus formula gives
\[
2g-2=-10+(5-1)(4+1)=10,
\qquad g=6.
\]
The Deuring–Shafarevich formula yields \(5\)-rank zero.

**Exhaustive extension counts.** For every integer \(n\ge1\), the additive map \(y\mapsto y^5-y\) on \(\mathbb F_{5^n}\) has kernel \(\mathbb F_5\) and image equal to the trace-zero subspace. Thus the *exact* formula
\[
\#X(\mathbb F_{5^n})=1+5\#\{x\in\mathbb F_{5^n}:\operatorname{Tr}_{\mathbb F_{5^n}/\mathbb F_5}(x^4+x^2+x)=0\}
\]
holds, not merely an estimate. The six finite exhaustive counts are:

| \(n\) | \(5^n\) | trace-zero inputs | \(\#X(\mathbb F_{5^n})\) |
|---:|---:|---:|---:|
| 1 | 5 | 1 | 6 |
| 2 | 25 | 1 | 6 |
| 3 | 125 | 31 | 156 |
| 4 | 625 | 129 | 646 |
| 5 | 3125 | 700 | 3501 |
| 6 | 15625 | 3115 | 15576 |

The executable `verify.py` constructs each entire finite field in a polynomial basis, tests each defining polynomial for irreducibility using exhaustive monic divisor trials, enumerates every field element, and obtains each count in **two** ways: direct enumeration of the image and fibres of \(y^5-y\), and independently by the trace of \(x^4+x^2+x\). Both give the displayed integers and agree with `certificate.txt`. The degree-\(2\) through degree-\(6\) monic moduli over \(\mathbb F_5\) used are, respectively,
\[
 t^2+2,\quad t^3+t+1,\quad t^4+2,\quad
 t^5+4t+1,\quad t^6+t+2.
\]

**Reconstruction of the numerator.** Define \(S_n=5^n+1-\#X(\mathbb F_{5^n})\). The six values just established are
\[
(S_1,S_2,S_3,S_4,S_5,S_6)=(0,20,-30,-20,-375,50).
\]
Writing \(L_X(T)=\sum_{j=0}^{12}c_jT^j\), Newton's identities give \(c_0=1\) and
\[
k c_k=-\sum_{j=1}^{k}S_jc_{k-j}\qquad (1\le k\le6).
\]
This yields
\[
(c_0,c_1,c_2,c_3,c_4,c_5,c_6)=(1,0,-10,10,55,-25,-175).
\]
The genus-six Weil functional equation imposes \(c_{12-k}=5^{6-k}c_k\) for \(0\le k\le6\), giving the complete stated numerator. Because only degrees at most the genus were needed, the finite enumerations plus the functional equation establish all extension-field counts, via the resulting rational zeta function.

**Irreducibility and prime cardinality.** Reduction modulo \(2\) gives
\[
\overline{L_X}(T)=T^{12}+T^8+T^7+T^6+T^5+T^4+1\in\mathbb F_2[T].
\]
The exact binary-polynomial calculation verifies
\[
T^{2^{12}}\equiv T\pmod{\overline{L_X}},\quad
\gcd(\overline{L_X},T^{2^6}-T)=1,\quad
\gcd(\overline{L_X},T^{2^4}-T)=1.
\]
The degree-\(12\) Rabin criterion, for prime divisors \(2,3\) of \(12\), proves irreducibility modulo \(2\). Since the integral numerator has odd leading coefficient, it is irreducible over \(\mathbb Q\). Its reciprocal characteristic polynomial is therefore also irreducible. If the Jacobian had a proper nontrivial \(\mathbb F_5\)-abelian subvariety, the Frobenius characteristic polynomial would factor; hence the Jacobian is \(\mathbb F_5\)-simple. Exact summation gives \(L_X(1)=11731\), and trial division through \(\lfloor\sqrt{11731}\rfloor=108\) proves primality. The rational group must be cyclic because its order is prime.

## Verification

Run `python3 verify.py` with Python 3 (standard library only). The program checks field irreducibility and full enumerations, both point-count methods for all \(1\le n\le6\), the Newton and functional-equation coefficients, modular irreducibility and primality. Its final output is `VERIFY_OK`. The accompanying `certificate.txt` records the actual counts, complete trace histograms, coefficients and final assertions. The source of truth for these computations is the supplied executable, not an unaudited summary of its output.

## Relationship to prior work

Tafazolian–Kazemifard [1, Lemma 3.3 and Theorem 1.1] identify the polynomial and prove genus, \(p\)-rank and rigidity. They do not state its Weil numerator, its irreducibility, or the prime cardinality of the rational Jacobian. The full accessible manuscript was searched for the zeta numerator and the relevant sections were read.

Bouw–Ho–Malmskog–Scheidler–Srinivasan–Vincent [2] compute zeta functions of curves \(y^p-y=xR(x)\) with additive \(R\). Their allowed one-pole degrees are \(p^h+1\), hence \(2,6,26,\ldots\) when \(p=5\), not \(4\); their supersingular, large-automorphism setting does not imply this numerator. McGuire–Yılmaz [3] study \(y^p-y=x^{p^k+1}+ax\), with the same degree restriction, and do not treat this quartic. Both provide important adjacent techniques but no dominating theorem for the displayed curve. Finite-field point enumeration and the Weil functional equation are standard; the contribution is the exact previously unspecified arithmetic of this naturally distinguished example.

## Limitations

Simplicity is proved **over \(\mathbb F_5\)** only; geometric simplicity, the full endomorphism ring and polarization classification are not determined. No uniform formula for other primes or other defining polynomials is claimed. The calculation is finite and exhaustive for the degrees required by genus six; it is not a claim that finitely many examples alone prove a general family theorem. An equivalent unpublished or unindexed zeta calculation may exist, and an inaccessible detailed isogeny-class database query leaves a residual comparison risk.

## References

1. S. Tafazolian and A. Kazemifard, *Artin–Schreier curves of prescribed p-rank without extra automorphisms*, arXiv:2610.13279 (first posted 2026-10-09), especially Lemma 3.3 and Theorem 1.1.
2. I. Bouw, W. Ho, B. Malmskog, R. Scheidler, P. Srinivasan and C. Vincent, *Zeta functions of a class of Artin–Schreier curves with many automorphisms*, arXiv:1410.7031 (2014).
3. G. McGuire and E. S. Yılmaz, *Divisibility of L-polynomials for a family of Artin–Schreier curves*, J. Pure Appl. Algebra 223 (2019), 3341–3358, DOI:10.1016/j.jpaa.2018.11.005.
4. H. Stichtenoth, *Algebraic Function Fields and Codes*, 2nd ed., Springer (2009), Artin–Schreier ramification/genus formula.
