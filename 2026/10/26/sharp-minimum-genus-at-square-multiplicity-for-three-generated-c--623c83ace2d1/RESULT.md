# Sharp minimum genus at square multiplicity for three-generated complete-intersection numerical semigroups

## Finding
For every integer \(s\ge2\), among all complete-intersection numerical semigroups \(S\subseteq\mathbb N_0\) with embedding dimension \(3\) and multiplicity \(s^2\), the minimum genus is exactly
\[
\boxed{\min g(S)=s^2(s-1).}
\]
The unique semigroup attaining it is
\[
\boxed{S_s=\langle s^2,s(s+1),s^2+1\rangle.}
\]
Equivalently, the minimum Frobenius number is \(2s^2(s-1)-1\), uniquely attained by \(S_s\).

## Assumptions and scope
A numerical semigroup is a cofinite additive submonoid of \(\mathbb N_0\). Its embedding dimension is its number of indispensable additive generators, its multiplicity its least positive element, its genus its number of positive gaps, and its Frobenius number the largest gap. A complete intersection means a numerical semigroup whose minimal presentation has embedding dimension minus one relations. The theorem concerns all such semigroups, for every integer \(s\ge2\), under the *exact* constraints embedding dimension three and multiplicity \(s^2\). It does not assert a minimum for arbitrary multiplicities or embedding dimensions.

## Proof
**Gluing normal form.** Delorme's classical characterization says every complete-intersection numerical semigroup other than \(\mathbb N_0\) is a gluing of two complete-intersection semigroups. If its embedding dimension is three, the factors necessarily have embedding dimensions one and two. Consequently, each object in the theorem has a presentation
\[
S=\langle qa,qb,p\rangle=q\langle a,b\rangle+p\mathbb N_0,
\]
where \(2\le a<b\), \(\gcd(a,b)=1\), \(q\ge2\), \(p\in\langle a,b\rangle\setminus\{0,a,b\}\) is not a minimal generator, and \(\gcd(p,q)=1\). The three displayed generators are indispensable. The Frobenius number of the two-generator factor is \(ab-a-b\). The gluing Frobenius formula here is
\[
F(S)=q(ab-a-b)+(q-1)p. \tag{1}
\]
For completeness, if \(0\le j<q\), each integer in residue class \(jp\pmod q\) has the unique expression \(jp+qx\), and it belongs to \(S\) exactly when \(x\in\langle a,b\rangle\). Indeed other nonnegative multiples of \(p\) differ by \(qp\), and \(p\in\langle a,b\rangle\) makes those differences harmless. The largest missing number in that residue class is \(jp+q(ab-a-b)\), giving (1).

Set \(m=s^2\). Because \(a\ge2\) and \(b\ge a+1\),
\[
ab-a-b\ge a^2-a-1. \tag{2}
\]
The multiplicity is \(m=\min(qa,p)\). We split into two exhaustive cases.

**Case I: \(qa=m\).** Necessarily \(p>m\), since \(p=m=qa\) would contradict \(\gcd(q,p)=1\). By (1)–(2),
\[
\begin{aligned}
F(S)&\ge q(a^2-a-1)+(q-1)(m+1)\\
&=m(a+q-2)-1\\
&\ge 2s^2(s-1)-1.
\end{aligned}
\]
The final inequality is arithmetic–geometric mean applied to the positive integers \(a,q\) with \(aq=s^2\). Equality forces \(a=q=s\), \(b=a+1\), and \(p=m+1\).

**Case II: \(p=m<qa\).** Using (1)–(2) and \(q>s^2/a\),
\[
\begin{aligned}
F(S)&\ge q(a^2-a-1+s^2)-s^2\\
&>s^2\left(a+\frac{s^2}{a}-2-\frac1a\right).
\end{aligned}
\]
Subtract \(F_0=2s^2(s-1)-1\). The resulting strict lower bound for \(F(S)-F_0\) is
\[
\frac{s^2((a-s)^2-1)}a+1.
\]
If \(a\ne s\), the square \((a-s)^2\) is at least one, so \(F(S)>F_0\). If \(a=s\), integrality and \(qa>s^2\) imply \(q\ge s+1\), giving the stronger bound
\[
F(S)\ge(s+1)(2s^2-s-1)-s^2
=2s^3-2s-1>F_0.
\]
Thus Case II is never extremal.

**Attainment and uniqueness.** Choose \(a=q=s\), \(b=s+1\), and \(p=s^2+1\). The identity \(s^2+1=(s-1)s+(s+1)\) shows that \(p\) is a non-generator of \(\langle s,s+1\rangle\), and \(\gcd(s,s^2+1)=1\). Classical gluing therefore makes \(S_s\) a complete intersection with precisely three minimal generators and multiplicity \(s^2\). Equation (1) yields
\[
F(S_s)=s(s(s+1)-s-(s+1))+(s-1)(s^2+1)
=2s^2(s-1)-1.
\]
Every complete-intersection numerical semigroup is symmetric, so \(g(S)=(F(S)+1)/2\). The genus bound and its attainment follow. The equality conditions in Case I and strictness in Case II force the same three generators, hence uniqueness.

## Verification
Run `python verify.py` from the directory containing the included verifier. It independently enumerates all gluing parameters whose Frobenius number does not exceed the constructed bound for \(2\le s\le6\), checks uniqueness of the optimum, and computes the Frobenius number directly from the generating set. Expected final line: `VERIFY_OK`. The script tests finite cases only; the above inequalities prove the claim for all \(s\ge2\).

## Relationship to prior work
Li and Zhang (2026) classify which pairs (embedding dimension, multiplicity) occur for complete-intersection numerical semigroups, and explicitly raise the **minimum genus at fixed pair** as a further problem. Their paper supplies neither this extremal square-multiplicity formula nor the uniqueness statement. Delorme's 1976 gluing characterization and the two-generator Frobenius formula are essential prior ingredients, not new claims. García-García and collaborators (2017) provide algorithms for minimum genus among *all* numerical semigroups at fixed embedding dimension and multiplicity; that does not directly determine the minimum restricted to complete intersections. The result here treats the full infinite square-multiplicity slice, rather than one isolated numerical example.

## Limitations
The theorem is restricted to embedding dimension three and perfect-square multiplicities. It gives no general minimum for nonsquare multiplicities or for higher embedding dimension. The proof depends on standard published gluing and symmetry theorems. Literature coverage cannot exclude an older equivalent extremal formula in unindexed sources; independent mathematical and priority review remains outstanding.

## References
- M. Li and Y. Zhang, *A Complete Characterization of Realizable (Embedding Dimension, Multiplicity) Pairs for Complete Intersection Numerical Semigroups*, arXiv:2608.21556v1, first public August 21, 2026, Sections 1–4, especially Section 4(ii). https://arxiv.org/abs/2608.21556
- C. Delorme, *Sous-monoïdes d'intersection complète de* \(\mathbb N\), Annales scientifiques de l'École normale supérieure 9 (1976), 145–154.
- J. C. Rosales and P. A. García-Sánchez, *Numerical Semigroups*, Springer, 2009, Section 8.3.
- J. I. García-García, D. Marín-Aragón, M. A. Moreno-Frías, J. C. Rosales, A. Vigneron-Tenorio, *Frobenius number and minimum genus of numerical semigroups with fixed multiplicity and embedding dimension*, arXiv:1712.05220 (2017).
