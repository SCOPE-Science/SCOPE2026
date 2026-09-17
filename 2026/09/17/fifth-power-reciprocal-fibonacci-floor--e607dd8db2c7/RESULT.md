# Exact floor formula for reciprocal fifth-power Fibonacci tails

## Statement

Let \(F_0=0,F_1=1,F_{n+1}=F_n+F_{n-1}\) be the Fibonacci sequence and let
\(L_n=F_{n-1}+F_{n+1}\) be the Lucas sequence. Define
\[
S_n=\sum_{k=n}^{\infty}\frac1{F_k^5},\qquad M=31958,
\]
and
\[
A_n=M(F_n^5-F_{n-1}^5)
+1102(-1)^n(7F_{3n}-2L_{3n})
+1763F_n-106L_n.
\]
Let \(r_n\) be the least nonnegative residue of \(A_n\) modulo \(M\).

**Theorem.** For every integer \(n\ge 4\),
\[
\boxed{\left\lfloor S_n^{-1}\right\rfloor=\frac{A_n-r_n}{31958}.}
\]
Equivalently, if
\[
G_n=F_n^5-F_{n-1}^5
+\frac{(-1)^n(7F_{3n}-2L_{3n})}{29}
+\frac{1763F_n-106L_n}{31958},
\]
then
\[
\boxed{\left\lfloor S_n^{-1}\right\rfloor=\lfloor G_n\rfloor\qquad(n\ge4).}
\]
The residue correction \(r_n=A_n\bmod 31958\) is periodic with period \(3654\); the finite certificate in `artifacts/verify.py` checks one complete period.

## Context

Exact integer parts of inverse reciprocal Fibonacci tails are known for several low powers. Hwang, Park and Song treated the fourth power in 2022, and their September 2026 preprint gives a continuous approximation and exact floor formula for the cubic case. Their concluding remarks explicitly identify construction of an explicit \(g_{s,n}\) for higher powers \(s\ge5\) as a substantially more complicated direction. Wan, Liang and Liao meanwhile give a general asymptotic theory for arbitrary positive exponent \(d\) in generalized Fibonacci subsequences, with explicit corollaries developed for \(d=1,2,3,4\).

The asymptotic expansion used below is therefore **not** claimed as a standalone novelty: it is compatible with the general arbitrary-\(d\) framework of Wan--Liang--Liao. The contribution here is the exact floor formula at \(d=5\), obtained by combining a compact explicit Fibonacci--Lucas approximant with a modular nonintegrality obstruction, an effective error bound, and exact finite certificates.

## Proof

Put
\[
\alpha=\frac{1+\sqrt5}{2},\qquad \beta=\frac{1-\sqrt5}{2}=-\alpha^{-1},
\qquad z_n=(-1)^n\alpha^{-2n}.
\]
Binet's formula gives
\[
\frac1{F_k^5}=5^{5/2}\alpha^{-5k}
\left(1-(-1)^k\alpha^{-2k}\right)^{-5}.
\]
Using
\((1-u)^{-5}=\sum_{j\ge0}\binom{j+4}{4}u^j\)
and summing geometrically in \(k\), one obtains the exact representation
\[
S_n=\frac{5^{5/2}\alpha^{-5n}}{1-\alpha^{-5}}H(z_n),
\]
where
\[
H(z)=\sum_{j\ge0}b_jz^j,
\qquad
b_j=\binom{j+4}{4}\frac{1-\alpha^{-5}}
{1-(-1)^j\alpha^{-(5+2j)}}.
\]
Thus
\[
S_n^{-1}=C_0\alpha^{5n}H(z_n)^{-1},
\qquad
C_0=\frac{1-\alpha^{-5}}{25\sqrt5}
=-\frac1{10}+\frac{13\sqrt5}{250}.
\]
Expanding \(H(z)^{-1}\) through degree two yields
\[
S_n^{-1}=C_0\alpha^{5n}+C_1(-1)^n\alpha^{3n}+C_2\alpha^n+E_n,
\]
with
\[
C_1=-\frac{39}{145}+\frac{64\sqrt5}{725},
\qquad
C_2=-\frac{16244}{79895}+\frac{104689\sqrt5}{798950}.
\]

Let \(\overline{\phantom{x}}\) denote conjugation in \(\mathbb Q(\sqrt5)\). Taking traces of the first three terms gives a rational sequence
\[
\operatorname{Tr}(C_0\alpha^{5n})
+(-1)^n\operatorname{Tr}(C_1\alpha^{3n})
+\operatorname{Tr}(C_2\alpha^n).
\]
Since, for rational \(a,b\),
\[
\operatorname{Tr}((a+b\sqrt5)\alpha^m)=aL_m+5bF_m,
\]
direct simplification gives exactly
\[
G_n=F_n^5-F_{n-1}^5
+\frac{(-1)^n(7F_{3n}-2L_{3n})}{29}
+\frac{1763F_n-106L_n}{31958}.
\]
Consequently \(G_n=A_n/M\).

### The approximant never hits an integer

Both \(M=31958\) and \(1102\) are divisible by \(19\). Hence
\[
A_n\equiv1763F_n-106L_n
\equiv15F_n+8L_n
\equiv4F_n-3F_{n-1}\pmod{19},
\]
using \(L_n=F_n+2F_{n-1}\). The residues of
\(4F_n-3F_{n-1}\) for \(n=1,\ldots,9\) are
\[
4,1,5,6,11,17,9,7,16.
\]
The same quantity satisfies the Fibonacci recurrence modulo \(19\), and its first two values recur at \(n=10,11\); hence this nonzero nine-term block repeats forever. Thus
\[
19\nmid A_n\quad\text{for every }n\ge1.
\]
In particular \(G_n\notin\mathbb Z\), and because its denominator divides \(M\), its distance from the nearest integer is at least \(1/M\).

### A uniform error bound

For \(|z|=t\le0.01\),
\[
|b_j|\le\binom{j+4}{4}.
\]
Writing
\[
H(z)=1+b_1z+b_2z^2+T(z),
\]
Taylor's theorem applied to \((1-t)^{-5}\) gives
\[
|T(z)|\le38t^3,
\qquad
|H(z)-1|\le6t.
\]
Using
\[
\frac1{1+u}=1-u+u^2-\frac{u^3}{1+u},
\qquad u=H(z)-1,
\]
and \(|b_1|\le5, |b_2|\le15\), termwise estimation gives
\[
\left|H(z)^{-1}-\bigl(1-b_1z+(b_1^2-b_2)z^2\bigr)\right|<424t^3.
\]
For \(n\ge5\), \(|z_n|<0.01\). Also
\[
|C_0|<\frac1{50},\quad
|\overline{C_0}|<\frac14,\quad
|\overline{C_1}|<\frac12,\quad
|\overline{C_2}|<\frac12.
\]
The first inequality follows from the positive expression for \(C_0\), and the remaining elementary bounds follow, for example, from \(\sqrt5<9/4\). Therefore
\[
|S_n^{-1}-G_n|
<\left(\frac{424}{50}+\frac14+\frac12+\frac12\right)\alpha^{-n}
<10\alpha^{-n}
\qquad(n\ge5).
\]
Now
\[
\alpha^{27}=F_{27}\alpha+F_{26}
>\frac32F_{27}+F_{26}=416020>319580=10M,
\]
so for every \(n\ge27\),
\[
|S_n^{-1}-G_n|<\frac1M.
\]
Since \(G_n\) stays at least \(1/M\) away from every integer, \(S_n^{-1}\) and \(G_n\) lie in the same open unit interval. Hence
\[
\lfloor S_n^{-1}\rfloor=\lfloor G_n\rfloor\qquad(n\ge27).
\]

### Exact certification of the remaining cases

For \(4\le n\le26\), let
\[
T_{n,K}=\sum_{k=n}^{K}\frac1{F_k^5},\qquad K=n+40.
\]
Because \(F_{j+2}\ge2F_j\), splitting the omitted terms into the two parity classes gives the rigorous rational majorant
\[
0<S_n-T_{n,K}\le
\frac{32}{31}\left(\frac1{F_{K+1}^5}+\frac1{F_{K+2}^5}\right)=R_{n,K}.
\]
Thus
\[
\frac1{T_{n,K}+R_{n,K}}<S_n^{-1}<\frac1{T_{n,K}}.
\]
The standalone exact-rational verifier checks that, for every \(n=4,\ldots,26\), both endpoints lie in the unit interval predicted by \((A_n-r_n)/M\). This proves the theorem for all remaining \(n\).

## Reproducibility

Run

```text
python3 artifacts/verify.py
```

with Python 3. The verifier uses only the standard library and exact integer/rational arithmetic. It checks the finite cases \(4\le n\le26\), the mod-19 obstruction, and one complete period of the residue correction modulo \(31958\). `artifacts/verify-output.txt` records the expected output.

## Limitations and originality scope

The theorem concerns the ordinary Fibonacci sequence and exponent \(5\); it does not establish corresponding formulas for all higher exponents or for general second-order recurrences. Originality is asserted only to the best of our knowledge. Exact-phrase, synonymous, and nearby-literature searches found no prior exact floor formula for the fifth-power tail. The closest general result, Wan--Liang--Liao, supplies arbitrary-exponent asymptotic estimates but not this floor determination; the closest exact low-power papers treat exponents \(3\) and \(4\). Because one of those papers was posted extremely recently, unindexed contemporaneous follow-up work remains a residual risk.

Same-model review: passed. Cross-model review: not yet performed.

## References

1. W. Hwang, J.-D. Park, K. Song, *Continuous approximation to the reciprocal sum of the cubes of Fibonacci numbers*, arXiv:2609.18179 (2026). https://arxiv.org/abs/2609.18179
2. Y. Wan, Z. Liang, Q. Liao, *The asymptotic estimation for two classes of generalized Fibonacci sub-sequences*, Mathematica Bohemica, first online 10 April 2026; arXiv:2510.13472. https://arxiv.org/abs/2510.13472
3. W. Hwang, J.-D. Park, K. Song, *On the reciprocal sum of the fourth power of Fibonacci numbers*, Open Mathematics 20 (2022), 1642--1655. https://doi.org/10.1515/math-2022-0525
4. H. Li, K. Yang, P. Yuan, *The asymptotic behavior of the reciprocal sum of generalized Fibonacci numbers*, Electronic Research Archive 33 (2025), 409--432. https://doi.org/10.3934/era.2025020
5. H. Ohtsuka, S. Nakamura, *On the sum of reciprocal Fibonacci numbers*, Fibonacci Quarterly 46/47 (2008/2009), 153--159. https://doi.org/10.1080/00150517.2008.12428174
