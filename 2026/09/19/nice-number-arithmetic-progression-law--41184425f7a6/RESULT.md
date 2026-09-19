# Arithmetic-progression law for permutation-power nice numbers

## Statement

Call an integer \(n\ge 2\) **nice** if there is a permutation \(\sigma\) of \(\{1,\dots,n\}\) for which
\[
\{1^{\sigma(1)},2^{\sigma(2)},\dots,n^{\sigma(n)}\}
\]
is a complete residue system modulo \(n\).  Leonetti's 2026 classification gives, for even \(n\ge 6\),
\[
n\text{ is nice}\iff n=2p,\quad p\text{ prime},\quad p-1\text{ squarefree},
\]
while his 2018 theorem gives, for odd \(n\ge5\), that \(n\) is nice exactly when \(n\) is a safe prime.

For fixed \(m\ge1\) and \(a\pmod m\), write
\[
N_{m,a}(X)=\#\{n\le X:n\text{ is nice and }n\equiv a\pmod m\}.
\]
Let \(g=(2,m)\).  Define \(\kappa_m(a)=0\) if \(g\nmid a\).  Otherwise put
\[
M=\frac m g,
\]
and let \(b\pmod M\) be the unique class satisfying
\[
\frac2g\,b\equiv \frac ag\pmod M.
\]
If \((b,M)>1\), set \(\kappa_m(a)=0\).  If there is a prime \(q\) with \(q^2\mid M\) and
\(b\equiv1\pmod{q^2}\), again set \(\kappa_m(a)=0\).  In every remaining case define
\[
\boxed{
\kappa_m(a)=
\frac{\mathfrak A}{\varphi(M)}
\prod_{q\mid M}
\left(1-\frac1{q(q-1)}\right)^{-1}
\prod_{\substack{q\parallel M\\ b\equiv1\pmod q}}
\left(1-\frac1q\right),
}
\]
where
\[
\mathfrak A=\prod_q\left(1-\frac1{q(q-1)}\right)
=0.3739558136\ldots
\]
is Artin's constant.

Then, for every fixed \(m\) and residue class \(a\pmod m\),
\[
\boxed{
N_{m,a}(X)=\kappa_m(a)\operatorname{Li}(X/2)
+o_m\!\left(\frac{X}{\log X}\right).
}
\]
Consequently the limiting residue distribution of nice numbers exists for every fixed modulus:
\[
\boxed{
\lim_{X\to\infty}
\frac{N_{m,a}(X)}{\#\{n\le X:n\text{ is nice}\}}
=\frac{\kappa_m(a)}{\mathfrak A}.
}
\]
In particular,
\[
\boxed{
\#\{n\le X:n\text{ is nice}\}
\sim \mathfrak A\operatorname{Li}(X/2)
\sim \frac{\mathfrak A}{2}\frac{X}{\log X}.
}
\]
Thus the total counting law is unconditional even though infinitude of the odd nice numbers (equivalently, safe primes) remains open.

A concrete local bias already appears modulo \(6\):
\[
\boxed{
\frac{N_{6,2}(X)}{N(X)}\to\frac25,
\qquad
\frac{N_{6,4}(X)}{N(X)}\to\frac35,
}
\]
and every other residue class modulo \(6\) has limiting proportion zero.  Hence the asymptotically dominant nice numbers are not equidistributed even among the two allowable nonzero even classes modulo \(6\).

## Proof

By Leonetti's even classification, apart from finitely many small values, the even nice numbers are exactly
\[
2p\qquad(p\text{ prime},\ p-1\text{ squarefree}).
\]
By the odd classification, odd nice numbers are safe primes.  A standard Selberg upper sieve applied to the two linear forms \(t\) and \(2t+1\) gives
\[
\#\{p\le Y:p,2p+1\text{ prime}\}\ll \frac{Y}{(\log Y)^2}.
\]
Therefore the odd nice numbers contribute only \(O(X/(\log X)^2)\), which is negligible on the \(X/\log X\) scale.

It remains to count, for fixed \(M\) and a reduced class \(b\pmod M\),
\[
S_{M,b}(Y)=\#\{p\le Y:p\equiv b\pmod M,\ p-1\text{ squarefree}\}.
\]
The squarefree indicator gives
\[
\mu^2(p-1)=\sum_{d^2\mid p-1}\mu(d),
\]
so
\[
S_{M,b}(Y)=
\sum_d\mu(d)\,
\#\{p\le Y:p\equiv b\pmod M,\ p\equiv1\pmod{d^2}\}.
\]
For squarefree \(d\), the two congruences are compatible exactly when
\[
b\equiv1\pmod{(M,d^2)}.
\]
When compatible they specify one reduced class modulo \(\operatorname{lcm}(M,d^2)\).  Truncate at
\(d\le (\log Y)^B\).  The Siegel--Walfisz theorem applies uniformly to the resulting polylogarithmic moduli; after summing the errors and then letting the cutoff grow, while bounding the discarded part by
\[
\sum_{d>D}\left(\frac{Y}{d^2}+1\right)
=O\!\left(\frac YD+\sqrt Y\right),
\]
one obtains
\[
S_{M,b}(Y)
= C(M,b)\operatorname{Li}(Y)+o_M(Y/\log Y),
\]
where
\[
C(M,b)=
\sum_{\substack{d\ge1\\ b\equiv1\ ({\rm mod}\ (M,d^2))}}
\frac{\mu(d)}{\varphi(\operatorname{lcm}(M,d^2))}.
\]
The series is absolutely convergent.

Its Euler factors are explicit.  After factoring out \(1/\varphi(M)\):

- if \(q\nmid M\), including \(q\) in \(d\) contributes the ratio \(1/[q(q-1)]\), hence the local factor \(1-1/[q(q-1)]\);
- if \(q\parallel M\) and \(b\equiv1\pmod q\), the local factor is \(1-1/q\); if \(b\not\equiv1\pmod q\), it is \(1\);
- if \(q^2\mid M\) and \(b\equiv1\pmod{q^2}\), every prime in the progression has \(q^2\mid p-1\), so the constant is \(0\); otherwise the local factor at \(q\) is \(1\).

This is exactly the displayed formula for \(\kappa_m(a)\) after translating the congruence \(2p\equiv a\pmod m\) to \(p\equiv b\pmod M\).  If the translation is impossible or \((b,M)>1\), only finitely many even prime candidates remain, so the same formula with zero main constant holds.  Adding the lower-order odd nice branch proves the theorem.

For \(m=1\), one has \(M=1\) and \(\kappa_1(0)=\mathfrak A\), giving the global asymptotic.  For \(m=6\), the two dominant classes correspond to \(p\equiv1,2\pmod3\).  The local factor at \(3\) gives constants \(2\mathfrak A/5\) and \(3\mathfrak A/5\), respectively, yielding the \(2/5\)--\(3/5\) split.

## Context and originality

Leonetti's 2026 paper completes the structural classification of even nice numbers but does not state an asymptotic counting law or a residue-class distribution theorem.  The analytic ingredient that primes \(p\) with \(p-1\) squarefree have Artin-constant relative density is classical (Mirsky), and later work treats much stronger linear patterns inside the shifted-squarefree primes.  The claim here is therefore not novelty of the squarefree-prime sieve itself; it is the explicit transfer of the completed nice-number classification into a full fixed-modulus distribution law, including the local obstruction factors and the unconditional domination of the unresolved safe-prime branch.

Searches for the defining permutation-power formulation together with counting, arithmetic progressions, Artin's constant, shifted-squarefree primes, and equivalent nice-number terminology did not identify a prior statement of this distribution law.  Originality is claimed only to the best of our knowledge.

## Limitations

The modulus \(m\) is fixed; no uniformity for growing moduli is asserted.  No asymptotic for Sophie Germain or safe primes is proved, and no claim is made that infinitely many odd nice numbers exist.  The result uses standard Siegel--Walfisz and Selberg-sieve inputs rather than an optimized error term.  The 2025 Kowitz paper was available only through bibliographic/abstract-level material in the sources inspected; its abstract concerns the counterexample \(62\) to the earlier safe-prime conjecture and does not indicate a counting theorem.  Mirsky's 1949 article was identified through its bibliographic record and later literature; the present proof does not depend on uninspected details of that paper.

## Reproducibility

`artifacts/verify.py` independently enumerates primes up to \(10^6\), tests squarefreeness of \(p-1\), computes a finite Euler product for Artin's constant, and checks the predicted modulo-6 split numerically.  `artifacts/verification.txt` records its deterministic output.  The computation is illustrative; the theorem is proved analytically above.

## References

1. Paolo Leonetti, *A characterization of Sophie Germain primes - II*, arXiv:2609.20208 (2026), especially Theorem 1.3. https://arxiv.org/abs/2609.20208
2. Paolo Leonetti, *A characterization of Sophie Germain primes*, International Journal of Number Theory 14 (2018), 653--660; the odd classification is restated as Theorem 1.1 of the 2026 paper. https://doi.org/10.1142/S1793042118500409
3. Leon Mirsky, *The Number of Representations of an Integer as the Sum of a Prime and a k-Free Integer*, American Mathematical Monthly 56 (1949), 17--19. https://doi.org/10.1080/00029890.1949.11990233
4. Pierre-Yves Bienvenu, *A higher-dimensional Siegel-Walfisz theorem*, arXiv:1607.06625; the paper explicitly treats linear patterns in primes \(p\) for which \(p-1\) is squarefree. https://arxiv.org/abs/1607.06625
5. Matteo Bordignon and Ethan Simpson Lee, *Explicit upper bounds for the number of primes simultaneously representable by any set of irreducible polynomials*, arXiv:2211.11012; see the Selberg-sieve discussion and Sophie Germain application. https://arxiv.org/abs/2211.11012
6. Krzysztof Kowitz, *Generalized “Riesel” numbers and nice numbers*, Discrete Mathematics, Algorithms and Applications 17 (2025), 2450104. https://doi.org/10.1142/S1793830924501040
