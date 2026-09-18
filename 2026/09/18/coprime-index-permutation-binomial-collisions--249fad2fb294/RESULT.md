# Collision rigidity and exact enumeration for coprime-index permutation binomials

Let \(q\) be a prime power, \(e\ge 2\),
\[
L=\ell_e(q)=\frac{q^e-1}{q-1},\qquad N=q^e-1=(q-1)L,
\]
and consider
\[
f_{r,d,a}(X)=X^r\bigl(X^{d(q-1)}+a\bigr)\qquad(a\in\mathbb F_{q^e}^{\times}).
\]
Fan's Corollary 6.1 classifies this family when \(\gcd(d,L)=1\): it is a permutation of \(\mathbb F_{q^e}\) exactly when
\[
\gcd(r,q-1)=1,\qquad (-a)^L\ne1,
\]
and
\[
r\ell_h(q)\equiv d\pmod L
\]
for some \(1\le h<e\) with \(\gcd(h,e)=1\). The result below determines the collisions between different coprime indices \(d\), and consequently gives the exact number of distinct permutation functions in the whole coprime-index family.

## Theorem

Assume \(q>2\), and let
\[
U=(\mathbb Z/L\mathbb Z)^\times.
\]
For \(D\subseteq U\), let \(\mathcal P_D\) be the set of distinct functions \(\mathbb F_{q^e}\to\mathbb F_{q^e}\) represented by admissible \(f_{r,d,a}\) with \(d\bmod L\in D\). Put
\[
E=\frac{\varphi(e)\varphi(N)}{\varphi(L)},\qquad
A=(q-2)L,
\]
and let
\[
P(D)=\frac12\#\{d\in D:-d\in D\},
\]
the number of unordered antipodal pairs contained in \(D\).

Then
\[
|\mathcal P_D|=
\begin{cases}
|D|AE-P(D)E,& q\text{ odd and }e\text{ odd},\\[1mm]
|D|AE,&\text{otherwise}.
\end{cases}
\]

More precisely, if two admissible representatives with coprime indices define the same function and their indices are different modulo \(L\), then necessarily
\[
d'\equiv-d\pmod L,\qquad a=a'=1,
\]
and
\[
r'\equiv r+d(q-1)\pmod N.
\]
Conversely, whenever \(q\) and \(e\) are both odd, every admissible \((d,r,1)\) has exactly this antipodal second representation, with the corresponding parameter \(h\) replaced by \(e-h\). Thus these are all cross-index collisions.

For the full coprime-index family \(D=U\), this gives
\[
\boxed{
|\mathcal P_U|=
\begin{cases}
\displaystyle \frac{\varphi(e)\varphi(q^e-1)}{2}
\bigl(2(q-2)\ell_e(q)-1\bigr),&q,e\text{ odd},\\[3mm]
\displaystyle \varphi(e)\varphi(q^e-1)(q-2)\ell_e(q),&\text{otherwise}.
\end{cases}}
\]
For \(q=2\), the coefficient condition has no solutions and the count is \(0\).

## Proof

### 1. The number of admissible exponent classes for one index

Fix \(d\in U\). For every \(h\) with \(1\le h<e\) and \(\gcd(h,e)=1\), the number \(\ell_h(q)\) is a unit modulo \(L\). Hence Fan's congruence fixes one residue class
\[
r\equiv d\ell_h(q)^{-1}\pmod L.
\]
The \(\varphi(e)\) classes arising from the admissible values of \(h\) are distinct. The reduction map
\[
(\mathbb Z/N\mathbb Z)^\times\longrightarrow(\mathbb Z/L\mathbb Z)^\times
\]
is surjective, so each unit class modulo \(L\) has exactly \(\varphi(N)/\varphi(L)\) unit lifts modulo \(N\). Therefore a fixed coprime index \(d\) has exactly
\[
E=\frac{\varphi(e)\varphi(N)}{\varphi(L)}
\]
admissible exponent classes modulo \(N\).

The coefficient condition excludes exactly the \(L\) elements for which \((-a)^L=1\). Thus the number of admissible coefficients is
\[
(q^e-1)-L=(q-2)L=A.
\]
Before comparing different \(d\)'s, each fixed index therefore contributes \(AE\) distinct functions.

### 2. Rigidity of equality as functions

For an admissible triple, both exponents
\[
r,\qquad r+d(q-1)
\]
are nonzero modulo \(N\), and they are distinct modulo \(N\). Choose their representatives in \(\{1,\ldots,N-1\}\). If two such binomials agree as functions on \(\mathbb F_{q^e}\), their difference, after reducing exponents modulo \(N\), has degree at most \(N-1=q^e-2\) and vanishes at all \(N\) nonzero field elements. Hence that reduced polynomial is zero. The two two-point supports, with coefficients, must therefore coincide.

If the supports have the same orientation, then
\[
d'\equiv d\pmod L,\qquad r'\equiv r\pmod N,\qquad a'=a.
\]
If the supports are reversed, comparison of the two monic terms and the two coefficient-\(a\) terms forces
\[
a=a'=1,
\]
while the support equations give
\[
d'\equiv-d\pmod L,
\qquad
r'\equiv r+d(q-1)\pmod N.
\]
This proves that no other cross-index collision is possible.

### 3. The antipodal representation is admissible

Suppose
\[
r\ell_h(q)\equiv d\pmod L.
\]
Set
\[
d'\equiv-d\pmod L,
\qquad
r'\equiv r+d(q-1)\pmod N.
\]
Modulo \(L\),
\[
r'\equiv r\bigl(1+(q-1)\ell_h(q)\bigr)=rq^h.
\]
Using
\[
q^h\ell_{e-h}(q)=\ell_e(q)-\ell_h(q),
\]
we obtain
\[
r'\ell_{e-h}(q)
\equiv-r\ell_h(q)
\equiv-d
\pmod L.
\]
Also \(\gcd(e-h,e)=1\), and \(r'\equiv r\pmod{q-1}\), so \(\gcd(r',q-1)=1\). Thus the reversed support satisfies the exponent conditions for the antipodal index.

It remains only to decide whether the forced coefficient \(a=1\) is admissible. This requires
\[
(-1)^L\ne1.
\]
In characteristic \(2\) it never holds. If \(q\) is odd, then
\[
L=1+q+\cdots+q^{e-1}\equiv e\pmod2,
\]
so it holds exactly when \(e\) is odd. Hence cross-index collisions occur exactly for odd \(q\) and odd \(e\).

Finally, a unit \(d\bmod L\) cannot satisfy \(d\equiv-d\pmod L\): that would imply \(L\mid2d\), and hence \(L\mid2\), whereas \(L\ge q+1\ge4\). Thus the collision relation consists of disjoint antipodal pairs. Each unordered pair \(\{d,-d\}\subseteq D\) identifies exactly \(E\) pairs of representations (one for each admissible exponent class at \(a=1\)). Subtracting these duplicate representations gives the stated formula.

For \(D=U\), the units split into \(\varphi(L)/2\) antipodal pairs, yielding the boxed count.

## Example

Take \(q=3\) and \(e=3\). Then
\[
L=13,\qquad N=26,\qquad E=2,\qquad A=13.
\]
There are \(\varphi(13)=12\) coprime index classes. Naively multiplying the fixed-index count gives \(12\cdot13\cdot2=312\) representations. Since \(q\) and \(e\) are odd, the six antipodal index pairs each contribute \(E=2\) duplicated functions. Hence
\[
|\mathcal P_U|=312-12=300.
\]

By contrast, for \(q=4,e=3\), one has \(L=21\), \(E=6\), and \(A=42\). Characteristic \(2\) rules out the antipodal coefficient \(a=1\), so the full count is
\[
\varphi(21)\cdot42\cdot6=3024.
\]

## Verification

`artifacts/verify_counts.py` checks the exponent-index classification and the antipodal support involution with exact integer arithmetic for a selection of parameters, including both parity regimes. It also evaluates the closed count formulas. The corresponding output is in `artifacts/verify-output.txt`. These finite checks support the algebraic proof but do not replace it.

## Relation to the literature and limitations

Fan's arXiv:2609.20354v1 (17 September 2026) gives an exact distinct-function count for the \(d=1\) family in Corollary 1.3 and then classifies every fixed coprime index in Corollary 6.1. In the inspected version, no exact count across all coprime \(d\) is stated. The theorem above fills that enumeration gap and shows why simply multiplying the fixed-index count by \(\varphi(L)\) is wrong precisely when \(q\) and \(e\) are both odd.

Hou and Pallozzi Lavorante introduced an equivalence relation on permutation binomials generated by output scaling, Frobenius, and monomial substitutions. That equivalence is different from equality as functions, which is the relation counted here. Their work therefore provides relevant structural background but does not subsume the collision count above.

Originality is asserted only to the best of our knowledge. Exact and synonymous searches for coprime-index permutation binomial counts, equality/collisions of the functions, antipodal indices, and the family \(X^r(X^{d(q-1)}+a)\) found no prior statement matching the theorem. The main residual risk is unindexed contemporaneous work because the motivating classification is extremely recent. No inaccessible paper was identified whose available title, abstract, or citation context specifically indicates the same all-coprime-index enumeration.

## References

1. Xiang Fan, *A complete classification of permutation binomials of the form \(X^r(X^{q-1}+a)\) over finite fields*, arXiv:2609.20354v1 (2026). https://arxiv.org/abs/2609.20354
2. Xiang-dong Hou and Vincenzo Pallozzi Lavorante, *New Results on Permutation Binomials of Finite Fields*, arXiv:2111.06533; Finite Fields and Their Applications 88 (2023), 102179. https://arxiv.org/abs/2111.06533
