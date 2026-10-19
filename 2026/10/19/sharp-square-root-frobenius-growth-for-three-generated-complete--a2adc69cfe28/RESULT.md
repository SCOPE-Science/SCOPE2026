# Sharp square-root Frobenius growth for three-generated complete-intersection numerical semigroups

## Finding
For each integer \(m\ge4\), let \(\mathcal C_m\) be the class of numerical semigroups of multiplicity \(m\), embedding dimension exactly three, and complete-intersection presentation. Define
\[
 f_3^{\mathrm{CI}}(m)=\min_{S\in\mathcal C_m}F(S),
 \qquad g_3^{\mathrm{CI}}(m)=\min_{S\in\mathcal C_m}g(S),
\]
where \(F\) is the Frobenius number and \(g\) the genus. Then \(\mathcal C_m\ne\varnothing\) and
\[
 \boxed{\lim_{m\to\infty}\frac{f_3^{\mathrm{CI}}(m)}{m^{3/2}}=2,
 \qquad \lim_{m\to\infty}\frac{g_3^{\mathrm{CI}}(m)}{m^{3/2}}=1.}
\]
There is a uniform effective lower bound
\[
 \boxed{f_3^{\mathrm{CI}}(m)\ge2m\sqrt{m-1}-\frac52m.}
\]
An explicit coprimality-window construction supplies an effective upper bound. Put \(b=\lfloor\sqrt m\rfloor\), \(\omega(m)=\#\{p:p\text{ prime},\ p\mid m\}\), \(B=4^{\omega(m)}\), and \(a_0=\lfloor m/b\rfloor+1\). There is an integer \(a\in[a_0,a_0+B]\) coprime to \(m\), and each such choice yields a three-generated complete-intersection semigroup
\[
 S_{m,a}=\langle m,ab,a(b+1)\rangle
\]
with exact Frobenius number
\[
 F(S_{m,a})=a(b^2-b-1)+(a-1)m.
\]
In particular
\[
 f_3^{\mathrm{CI}}(m)\le
 (a_0+B)(b^2-b-1)+(a_0+B-1)m.
\]
The genus statement follows because every complete-intersection numerical semigroup is symmetric, so its genus is \((F+1)/2\).

## Assumptions and scope
A numerical semigroup is a cofinite additive submonoid of \(\mathbb N_0\). Its embedding dimension is the cardinality of its unique minimal positive generating set. Its multiplicity is the least positive element. A semigroup is a complete intersection when the size of a minimal presentation is one less than its embedding dimension. The minimum is over **complete-intersection** semigroups of embedding dimension **exactly three**, not over all three-generated semigroups. The claim concerns all integers \(m\ge4\), with no primality restriction. Both limiting variables range through all positive integers \(m\to\infty\). We use the established gluing characterization of complete intersections and the standard symmetry property of complete intersections.

## Proof
**1. Normal form and the Frobenius formula.** Every embedding-dimension-three complete-intersection numerical semigroup is a gluing of a two-generated numerical semigroup with \(\mathbb N_0\). Consequently its minimal generating set has the form
\[
 \{ab,ac,d\},\quad 2\le b<c,\quad \gcd(b,c)=1,\quad a\ge2,
 \quad d\in\langle b,c\rangle\setminus\{b,c\},\quad \gcd(a,d)=1.
\]
Here \(d\) is a nonminimal positive element of \(\langle b,c\rangle\), and the gluing condition guarantees precisely three minimal generators. Writing \(U=\langle b,c\rangle\), the semigroup is \(S=aU+d\mathbb N_0\), and
\[
 m(S)=\min(ab,d),\qquad
 F(S)=a(bc-b-c)+(a-1)d.\tag{1}
\]
To verify the second formula directly, note that for \(d\in U\) and \(\gcd(a,d)=1\), the Apéry set of \(S\) modulo \(d\) is \(a\operatorname{Ap}(U,d)\), with residue classes permuted by multiplication by \(a\). The largest Apéry element is \(a(F(U)+d)\), so \(F(S)=aF(U)+(a-1)d\). Sylvester's two-generator formula gives \(F(U)=bc-b-c\).

**2. Uniform lower bound.** Since \(c\ge b+1\),
\[
 bc-b-c\ge b^2-b-1>0.\tag{2}
\]
If \(m=d\le ab\), then \(ab\ge m\). Combining (1) and (2),
\[
 \begin{aligned}
 F(S)&\ge a(b^2-b-1)+(a-1)m\\
 &\ge \frac mb(b^2-b-1)+\left(\frac mb-1\right)m\\
 &=m\left(b+\frac{m-1}{b}-2\right)\\
 &\ge2m\sqrt{m-1}-2m,
 \end{aligned}\tag{3}
\]
where the last inequality is the arithmetic-geometric mean inequality. If instead \(m=ab\le d\), then (1)–(2) give
\[
 \begin{aligned}
 F(S)&\ge a(b^2-b-1)+(a-1)m\\
 &=m(a+b-2)-a\\
 &\ge 2m\sqrt m-\frac52m.
 \end{aligned}\tag{4}
\]
Indeed \(ab=m\), so \(a+b\ge2\sqrt m\) and \(a\le m/2\) because \(b\ge2\). Equations (3)–(4) imply \(F(S)\ge2m\sqrt{m-1}-5m/2\) for both cases, proving the universal bound. This derivation does not require a numerical search.

**3. Uniform construction with asymptotically optimal leading constant.** Fix \(m\ge4\), put \(b=\lfloor\sqrt m\rfloor\), and let \(U=\langle b,b+1\rangle\). Its Frobenius number is \(b^2-b-1<m\), so \(m\in U\) is not a minimal generator. Every integer \(a>m/b\) coprime to \(m\) gives a valid gluing
\[
 S=aU+m\mathbb N_0=\langle ab,a(b+1),m\rangle
\]
with multiplicity \(m\), embedding dimension three, and Frobenius number
\[
 F(S)=a(b^2-b-1)+(a-1)m.\tag{5}
\]
It remains to choose \(a\) close to \(\sqrt m\) even when \(m\) is composite. For an interval \(I\) of \(L\) consecutive integers, Möbius inversion gives
\[
 \begin{aligned}
 \#\{t\in I:\gcd(t,m)=1\}
 &=\sum_{d\mid m}\mu(d)\#\{t\in I:d\mid t\}\\
 &\ge L\frac{\varphi(m)}m-2^{\omega(m)}.
 \end{aligned}\tag{6}
\]
Since \(\varphi(m)/m=\prod_{p\mid m}(1-p^{-1})\ge2^{-\omega(m)}\), the right-hand side is strictly positive whenever \(L=4^{\omega(m)}+1\). Thus the interval \([a_0,a_0+B]\), with \(a_0=\lfloor m/b\rfloor+1\) and \(B=4^{\omega(m)}\), contains a coprime integer \(a\), and \(ab>m\). The upper bound follows from (5), which increases with \(a\).

Finally \(\omega(m)=o(\log m)\): if \(k=\omega(m)\), the product of the first \(k\) primes, and hence \(m\), is at least \((k+1)!\). Consequently \(B=4^{\omega(m)}=m^{o(1)}=o(\sqrt m)\). As \(b=\sqrt m+O(1)\) and \(a_0=\sqrt m+O(1)\), the selected integer satisfies \(a=\sqrt m+o(\sqrt m)\). Equation (5) now gives
\[
 F(S)=2m^{3/2}+o(m^{3/2}).\tag{7}
\]
Combining (7) with the lower bound from step 2 proves the claimed limit for \(f_3^{\mathrm{CI}}\). Every complete-intersection numerical semigroup is symmetric, yielding \(g(S)=(F(S)+1)/2\) and hence the genus limit.

## Verification
The included standalone script `verify_ci_asympt.py` constructs semigroups and checks (5) against independently computed Apéry/Frobenius numbers for multiplicities from \(4\) through \(130\). It checks successful bounded coprimality-window selection through multiplicity \(300\) and tests the lower bound on \(18{,}625\) small normalized gluings. All tests passed. The complete proof rests on gluing, the Apéry formula, an elementary AM–GM inequality and inclusion–exclusion; no finite test proves an infinite limit. Run `python3 verify_ci_asympt.py` with Python 3.9 or later; no external dependencies are required.

## Relationship to prior work
Li and Zhang [1] classify the pairs of embedding dimension and multiplicity that a complete-intersection numerical semigroup can realize. Their paper explicitly names minimization of Frobenius number or genus at a fixed pair among its natural follow-ups. The present statement instead fixes embedding dimension three, determines the **sharp leading constant** of the minimal Frobenius number and genus for *every* multiplicity tending to infinity, and gives an effective witness using a short coprimality window. Its proof uses their cited classical gluing characterization, not their existence theorem as a novelty claim.

García-García, Marín-Aragón, Moreno-Frías, Rosales and Vigneron-Tenorio [2] give algorithms for minimizing Frobenius number or genus among all numerical semigroups of fixed multiplicity and embedding dimension. That optimization ranges over a larger class, and the inspected text provides no corresponding complete-intersection asymptotic or the coefficient two. Their algorithm is a relevant comparison, not a proof of the present growth law. The classical three-generator Frobenius literature [3] provides formulas for special families; an exact equivalent asymptotic not identified in accessible material remains a bibliographic risk.

## Limitations
The theorem does **not** determine the exact minimizing semigroup or the exact minimum \(f_3^{\mathrm{CI}}(m)\) at any individual multiplicity. The displayed effective upper bound can be loose, particularly for small \(m\), and the \(o(m^{3/2})\) error is not asserted to have the best possible order. The argument is restricted to embedding dimension three and does not extend the sharp constant to higher embedding dimensions. The self-contained numerical checks are finite checks, not infinite certificates. The novelty assessment remains vulnerable to an equivalent unindexed result, including a reformulation in the classical literature on numerical-semigroup gluings.

## References
[1] Minglang Li and Yizhi Zhang, *A Complete Characterization of Realizable (Embedding Dimension, Multiplicity) Pairs for Complete Intersection Numerical Semigroups*, arXiv:2608.21556v1, first posted 2026-08-21, Sections 1–4. https://arxiv.org/abs/2608.21556

[2] J. I. García-García, D. Marín-Aragón, M. A. Moreno-Frías, J. C. Rosales and A. Vigneron-Tenorio, *Frobenius number and minimum genus of numerical semigroups with fixed multiplicity and embedding dimension*, arXiv:1712.05220v1, 2017, Sections 3–4. https://arxiv.org/abs/1712.05220

[3] A. M. Robles-Pérez and J. C. Rosales, *The Frobenius problem for numerical semigroups with embedding dimension equal to three*, Mathematics of Computation 81 (2012), 1609–1617. https://doi.org/10.1090/S0025-5718-2011-02561-5

[4] C. Delorme, *Sous-monoïdes d'intersection complète de ℕ*, Ann. Sci. École Norm. Sup. (4) 9 (1976), 145–154 (gluing characterization, as cited in [1]).
