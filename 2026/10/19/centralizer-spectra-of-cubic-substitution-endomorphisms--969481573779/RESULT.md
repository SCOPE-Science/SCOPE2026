# Centralizer spectra of cubic substitution endomorphisms

## Finding

Fix any prime power \(q=p^s\), \(s\geq1\), and set
\[
 A_q=\mathbb F_q[t]/(t^4),\qquad M_q=\operatorname{End}_{\mathbb F_q\text{-alg}}(A_q).
\]
Endomorphisms are unital and fix the coefficient field. Every member of \(M_q\) is represented uniquely by the substitution
\[
 f_{a,b,c}(t)=at+bt^2+ct^3\pmod {t^4},\qquad (a,b,c)\in\mathbb F_q^3.
\]
The multiplication in \(M_q\) is composition. For \(f\in M_q\), write \(C(f)=|\{g\in M_q:f\circ g=g\circ f\}|\); the centralizer here is a submonoid, not necessarily a group.

**Theorem (complete centralizer-size spectrum).** For even \(q\), the following disjoint strata partition the \(q^3\) endomorphisms:
\[
\begin{array}{c|c|c}
\text{condition}&\#\text{ endomorphisms}&C(f)\\\hline
 a\in\{0,1\},\ b=c=0&2&q^3\\
 a\in\{0,1\},\ (b,c)\ne(0,0)&2(q^2-1)&2q^2\\
 a\notin\{0,1\}&(q-2)q^2&q
\end{array}
\]
For odd \(q\), they are:
\[
\begin{array}{c|c|c}
\text{condition}&\#\text{ endomorphisms}&C(f)\\\hline
 a\in\{0,1\},\ b=c=0&2&q^3\\
 a\in\{0,1\},\ b=0,\ c\ne0&2(q-1)&3q^2\\
 a\in\{0,1\},\ b\ne0&2q(q-1)&q^2+q\\
 a=-1,\ c=-b^2&q&q^2\\
 a=-1,\ c\ne-b^2&q(q-1)&3q\\
 a\notin\{0,1,-1\}&(q-3)q^2&q
\end{array}
\]
All rows are stated *with their defining conditions*: if two centralizer sizes coincide at a small field order, their multiplicities must be added. In particular, the center \(Z(M_q)=\{f:C(f)=q^3\}\) has cardinality
\[
 |Z(M_q)|=\begin{cases}8,&q=2,\\6,&q=3,\\2,&q\ge4.\end{cases}
\]
The number of ordered commuting pairs is exactly
\[
 \sum_{f\in M_q}C(f)=\begin{cases}
 5q^4-4q^2,&\operatorname{char}\mathbb F_q=2,\\
 3q^4+9q^3-11q^2,&\operatorname{char}\mathbb F_q\ne2.
 \end{cases}
\]
Dividing by \(q^6\) gives the commuting probability for independent uniformly sampled members. For \(q=2\), the full eight-element monoid is commutative; the corresponding substitution monoid modulo \(t^5\) is already noncommutative.

## Assumptions and scope

All conclusions concern exactly the \(\mathbb F_q\)-**linear unital algebra endomorphisms**, not arbitrary ring endomorphisms (which can act on the coefficient field), and their commuting relation **under composition**, not pointwise polynomial multiplication. The algebra \(A_q\) has radical \((t)\) and radical length four. The substitution coordinates have no constant term since a nilpotent image of \(t\) must be in \((t)\); conversely, every triple gives a well-defined unital coefficient-field-fixing endomorphism. The formulas hold for every prime power, without a primality assumption on \(q\).

## Proof

Write \(f=f_{a,b,c}\) and \(g=f_{d,e,h}\). Expanding the substitutions modulo \(t^4\), including the characteristic-dependent coefficient \(2\), shows that \(f\circ g=g\circ f\) is equivalent to the *two* equations
\[
 b(d^2-d)+e(a-a^2)=0,\qquad
 h(a-a^3)+c(d^3-d)+2be(d-a)=0. \tag{1}
\]
The degree-one coefficients commute automatically. We count \((d,e,h)\) satisfying (1), for fixed \((a,b,c)\).

If the characteristic is two and \(a\notin\{0,1\}\), both \(a-a^2\) and \(a-a^3=a(1-a)^2\) are nonzero. Each \(d\) then uniquely determines \(e\) and \(h\), giving \(q\) solutions. For \(a\in\{0,1\}\), equations (1) reduce to \(b(d^2-d)=c(d^3-d)=0\). When \(b=c=0\) every triple commutes. Otherwise \(d\in\{0,1\}\) (the respective polynomials have exactly those roots in characteristic two), while \(e,h\) vary freely, giving \(2q^2\). This establishes the even-characteristic table and its multiplicities.

Suppose the characteristic is odd. For \(a\notin\{0,1,-1\}\) the coefficients of \(e\) and \(h\) in (1) are nonzero, giving one solution \((e,h)\) per \(d\). For \(a\in\{0,1\}\), the first equation reduces to \(bd(d-1)=0\). If \(b\ne0\), \(d=0\) or \(1\), and the second equation reduces to \(2be(d-a)=0\), with \(h\) unrestricted. For \(d=a\) there are \(q^2\) choices for \((e,h)\); for the other \(d\) there are \(q\), totaling \(q^2+q\). If \(b=0,c\ne0\), the only restriction is \(d^3=d\), with the three distinct roots \(0,1,-1\); this gives \(3q^2\). If \(b=c=0\), both equations vanish and every \(g\) commutes.

Finally let \(a=-1\) in odd characteristic. The first equation uniquely forces
\[
 e=\frac b2d(d-1),
\]
and the second equation then factors as
\[
 (c+b^2)d(d-1)(d+1)=0.
\]
If \(c=-b^2\), any \(d\) is allowed, and the free \(h\) gives \(q^2\) commuting elements; otherwise exactly the three distinct choices \(d\in\{0,1,-1\}\) are possible, giving \(3q\). Counting the indicated \((a,b,c)\)-strata gives the odd-characteristic table.

Summing row multiplicities times centralizer sizes yields the two displayed commuting-pair polynomials; summing just the multiplicities yields \(q^3\). The center formula selects exactly rows with \(C(f)=q^3\), retaining coincidences at \(q=2,3\). To see the length-five boundary at \(q=2\), take \(f(t)=t+t^2\) and \(g(t)=t+t^3\). Modulo \(t^5\), their compositions differ by \(t^4\), whereas the length-four theorem proves commutativity of all eight substitutions.

## Verification

Run `python3 checker.py`. The checker independently constructs finite-field arithmetic and performs truncated polynomial substitution, without invoking equations (1), to exhaustively compute each element-centralizer. It compares the complete multiplicity map (merging coincident sizes) and the commuting-pair total to the theorem. Executed finite fields: \(q=2,3,4,5,7\), including the genuine extension field \(\mathbb F_4\). Expected total commuting-pair counts in that order: \(64,387,1216,2725,9751\). Exhaustive finite checks do not prove the all-fields assertion; the proof above establishes that assertion.

## Relationship to prior work

Enochs--Jenda--Ozbek (2015) studies composition submonoids of formal power series, classifying which coefficient support sets produce monoids; it does not supply the present finite jet centralizer-size fibers. Tarizadeh (2017) develops algebraic foundations and the universal property of formal power series; its statements do not imply the finite-field composition-centralizer enumeration without the calculations here. Cohen (2018), Lemma 2.1, explicitly writes the quadratic and cubic coefficients of series composition. We use that **known** coefficient law and contribute the complete solution count of its commutativity conditions over finite fields, including noninvertible elements; the source instead classifies finite-order *invertible* characteristic-zero series. Byszewski--Cornelissen--Tijsma (2020) studies torsion and automata in the *invertible tangent-to-identity* Nottingham group; that subgroup and invariant differ from the full monoid, which includes zero linear coefficients. The exact counting claim is limited to this natural radical-length-four algebra and is not an assertion about untruncated formal series. No equivalently complete profile was located in the inspected sources or targeted mathematical-record searches.

## Limitations

No classification for higher nilpotency length or arbitrary ring endomorphisms is claimed. The proof is an explicit low-length finite-field analysis, and the result may be encoded under different notation in existing substitution-semigroup literature. The 2015 composition-monoid study supplies older background; the 2017 formal-series treatment and 2018 composition-coefficient study also inform the present finite-field investigation. The earlier coefficient identity is not claimed as new.

## References

- E. Enochs, O. Jenda, F. Ozbek, *Submonoids of the formal power series*, arXiv:1510.05984v1 (2015), https://arxiv.org/abs/1510.05984 .
- A. Tarizadeh, *A fresh look into monoid rings and formal power series rings*, arXiv:1709.01426v1 (2017), https://arxiv.org/abs/1709.01426 .
- M. M. Cohen, *Elements of Finite Order in the Group of Formal Power Series Under Composition*, arXiv:1804.00059v1 (2018), https://arxiv.org/abs/1804.00059 .
- J. Byszewski, G. Cornelissen, D. Tijsma, *Automata and finite order elements in the Nottingham group*, arXiv:2008.04971v1 (2020), https://arxiv.org/abs/2008.04971 .
