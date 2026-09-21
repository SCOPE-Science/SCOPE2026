# Henselian residue criterion for generalized quasi t-fine rings

## Statement

Let \(R\) be a unital ring, let \(J(R)\) be its Jacobson radical, let
\(\mathcal T(R)\) be the set of torsion units, and let
\[
\mathcal Q(R)=\{q\in R:1-xq\in U(R)\text{ for every }x\in C_R(q)\}.
\]
Following Bien--Danchev--Ramezan-Nassab, \(R\) is **generalized quasi
\(t\)-fine** when
\[
R\setminus J(R)=\mathcal T(R)+\mathcal Q(R).
\]

The following gives an exact local criterion.

**Theorem 1 (torsion-lifting criterion).** Let \(R\) be a local ring and put
\(D=R/J(R)\). Then
\[
\mathcal Q(R)=J(R).
\]
Consequently,
\[
R\text{ is generalized quasi }t\text{-fine}
\quad\Longleftrightarrow\quad
\mathcal T(R)\longrightarrow D^\times
\text{ is surjective}.
\]
If these conditions hold, \(D\) is necessarily a locally finite field.

For commutative rings, the locality conclusion is already implicit in
Lemma 3.7 of arXiv:2609.19882v1. Thus a commutative ring \(R\) is generalized
quasi \(t\)-fine exactly when it is local and every nonzero residue class has
a torsion-unit lift.

This criterion becomes intrinsic for Henselian rings.

**Theorem 2 (Henselian residue criterion).** Let \((R,\mathfrak m,k)\) be a
commutative Henselian local ring. Then
\[
\boxed{
R\text{ is generalized quasi }t\text{-fine}
\quad\Longleftrightarrow\quad
k\text{ is a locally finite field}.
}
\]

In particular, every complete commutative local ring with locally finite
residue field is generalized quasi \(t\)-fine.

## Proof of Theorem 1

The inclusion \(J(R)\subseteq\mathcal Q(R)\) holds in every ring. Conversely,
if \(R\) is local and \(q\notin J(R)\), then \(q\) is a unit. Taking
\(x=q^{-1}\), which commutes with \(q\), gives
\[
1-xq=0,
\]
which is not a unit. Hence \(q\notin\mathcal Q(R)\), proving
\(\mathcal Q(R)=J(R)\).

Now let \(\pi:R\to D\) be reduction. If \(R\) is generalized quasi
\(t\)-fine and \(a\in R\setminus J(R)\), write
\(a=t+q\) with \(t\in\mathcal T(R)\) and \(q\in\mathcal Q(R)=J(R)\).
Then \(\pi(a)=\pi(t)\). Thus every element of \(D^\times\) is the reduction
of a torsion unit.

Conversely, assume \(\mathcal T(R)\to D^\times\) is surjective. Given
\(a\notin J(R)\), choose \(t\in\mathcal T(R)\) with
\(\pi(t)=\pi(a)\). Then
\[
a=t+(a-t),\qquad a-t\in J(R)=\mathcal Q(R),
\]
so \(R\) is generalized quasi \(t\)-fine.

Finally, surjectivity makes every element of \(D^\times\) torsion. A classical
periodic-division-ring theorem implies that a division ring with torsion
multiplicative group is commutative and algebraic over a finite prime field.
Hence \(D\) is a locally finite field.

## Proof of Theorem 2

Necessity follows from Theorem 1.

For sufficiency, suppose \(k\) is locally finite. Let
\(\bar a\in k^\times\). Then \(\bar a\) lies in a finite subfield of \(k\),
so it has finite order \(n\). If \(p=\operatorname{char}k\), then
\(p\nmid n\). Therefore \(\bar a\) is a simple root of
\[
f(X)=X^n-1,
\]
because
\[
f'(\bar a)=n\bar a^{\,n-1}\neq0.
\]
Hensel's lemma lifts \(\bar a\) to \(a\in R\) with \(a^n=1\). Thus every
element of \(k^\times\) has a torsion-unit lift. Theorem 1 completes the
proof.

## Sharp localization/completion contrast

The criterion exactly classifies the localizations of the integers:
\[
\boxed{
\mathbb Z_{(p)}\text{ is generalized quasi }t\text{-fine}
\quad\Longleftrightarrow\quad p\in\{2,3\}.
}
\]
Indeed, the only roots of unity in \(\mathbb Q\) are \(\pm1\), so the image
of \(\mathcal T(\mathbb Z_{(p)})\) in \(\mathbb F_p^\times\) is
\(\{\pm1\}\). This equals the full residue multiplicative group exactly for
\(p=2,3\).

By contrast, the \(p\)-adic completion \(\mathbb Z_p\) is Henselian with
residue field \(\mathbb F_p\), hence
\[
\boxed{\mathbb Z_p\text{ is generalized quasi }t\text{-fine for every prime }p.}
\]
Thus for every \(p\ge5\), completion changes the answer from false to true.
More generally, the Henselization of any commutative local ring with locally
finite residue field is generalized quasi \(t\)-fine.

## A matrix obstruction in mixed characteristic

The positive-characteristic matrix permanence result in Proposition 3.8 of
arXiv:2609.19882v1 cannot simply be extended to arbitrary characteristic.

**Proposition 3.** If \(p\ge5\), then for every \(n\ge1\),
\[
\boxed{
M_n(\mathbb Z_{(p)})\text{ is not generalized quasi }t\text{-fine}.
}
\]

Choose \(a\in\mathbb Z\) whose residue
\(\bar a\in\mathbb F_p^\times\) is not \(\pm1\), and suppose
\[
aI_n=U+Q
\]
were a generalized quasi \(t\)-fine decomposition. By Lemma 3.5 of
arXiv:2609.19882v1, reduction \(\bar Q\) is nilpotent. Hence
\[
\chi_{\bar U}(X)=(X-\bar a)^n.
\]
Since \(U\) has finite multiplicative order and has rational entries,
\(\chi_U(X)\) is a product of cyclotomic polynomials.

Write the index of any cyclotomic factor as \(m=p^s d\) with
\((d,p)=1\). Modulo \(p\), the distinct roots of \(\Phi_m\) are precisely
the primitive \(d\)-th roots of unity; for \(s\ge1\),
\[
\Phi_{dp^s}(X)\equiv
\Phi_d(X)^{\varphi(p^s)}\pmod p.
\]
Because the full reduced characteristic polynomial has only the single
distinct root \(\bar a\), every cyclotomic factor must have only one distinct
root modulo \(p\). Since \(p\nmid d\), \(\Phi_d\) is separable modulo \(p\);
therefore \(\varphi(d)=1\), so \(d=1\) or \(2\), forcing that root to be
\(1\) or \(-1\). This contradicts the choice of \(\bar a\).

Thus the mixed-characteristic obstruction persists in every matrix size.

## Context and prior literature

Bien, Danchev and Ramezan-Nassab introduced generalized quasi \(t\)-fine rings
in arXiv:2609.19882v1. Their Section 3 proves, among other things, that
\(\mathcal Q(R)=J(R)\) for commutative \(R\), gives \(F[[x]]\) for finite
\(F\) and \(\mathbb Z_{(2)}\) as examples, proves that the center of a
generalized quasi \(t\)-fine ring is local, and establishes matrix and group
ring results under additional hypotheses. The full v1 text does not state a
Henselian residue-field classification, the classification of
\(\mathbb Z_{(p)}\), or the mixed-characteristic matrix obstruction above.

The simple-root lifting used here is standard Hensel theory. Complete local
rings are Henselian (Stacks Project, Tag 04GM). The periodic-division-ring
input is classical; for example, Khazal records that a periodic division ring
is a field algebraic over a finite prime field.

## Limitations

Originality is claimed only to the best of our knowledge. The definition of
generalized quasi \(t\)-fineness, the equality
\(\mathcal Q(R)=J(R)\) in the commutative case, the locality result for the
center, and the positive-characteristic matrix theorem are prior work.
Hensel's lemma and the periodic-division-ring theorem are also standard.

The new claims are the exact local torsion-lifting criterion, the Henselian
residue-field equivalence, the sharp
\(\mathbb Z_{(p)}\) versus \(\mathbb Z_p\) contrast, and the all-size
\(M_n(\mathbb Z_{(p)})\) obstruction for \(p\ge5\). Because the terminology
was introduced in a very recent preprint, a later revision or independent
contemporary observation remains a material originality risk. No claim is
made here about a full matrix-ring classification over general Henselian
local rings.

## References

1. M. H. Bien, P. V. Danchev, M. Ramezan-Nassab, *Generalized \(t\)-Fine and
   Quasi \(t\)-Fine Rings*, arXiv:2609.19882v1 (2026).
   https://arxiv.org/abs/2609.19882v1
2. The Stacks Project, Section 10.153, Henselian local rings; in particular
   Lemma 10.153.9 (Tag 04GM).
   https://stacks.math.columbia.edu/tag/04GM
3. R. R. Khazal, *Multiplicative periodicity in rings*, Acta Sci. Math.
   (Szeged) 41 (1979), Proposition 3.
   https://acta.bibl.u-szeged.hu/38618/1/math_041_fasc_001_002.pdf
4. M. H. Bien, P. V. Danchev, M. Ramezan-Nassab, *On Semi-Nil Clean Rings
   with Applications*, arXiv:2408.13164.
   https://arxiv.org/abs/2408.13164
