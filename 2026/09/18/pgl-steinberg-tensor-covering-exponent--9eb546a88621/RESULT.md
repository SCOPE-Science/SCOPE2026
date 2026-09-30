# Alternate proof and refinements for the Steinberg tensor covering exponent of \(\operatorname{PGL}_n(q)\)

## Status and repository precedence

This record is **not a separate first discovery** of the exact Steinberg covering exponent. The earlier SCOPE record

`2026/09/17/steinberg-covering-number-for-pgln--e3667d632f22`

already proves that the Steinberg tensor covering exponent of \(\operatorname{PGL}_n(q)\) is \(2\) when \(\gcd(n,q-1)=1\) and \(3\) otherwise, and proves universal coverage by the third tensor power. The present record is retained as an alternate derivation and refinement: it makes the full square defect explicit, gives a short degree-obstruction proof of cube universality, and records a twisted central-character-fiber corollary for \(\operatorname{GL}_n(q)\).

## Statement

Let \(n\ge2\), let \(q\) be a prime power, and put
\[
\overline G=\operatorname{PGL}_n(q)=\operatorname{GL}_n(q)/Z,
\qquad d=\gcd(n,q-1).
\]
Write \(\mathrm{St}\) for the Steinberg character, descended to \(\overline G\).

If \((n,q)\ne(2,2)\), then
\[
\operatorname{Irr}(\mathrm{St}^2)
=
\operatorname{Irr}(\overline G)\setminus
\bigl(\operatorname{Lin}(\overline G)\setminus\{1\}\bigr).
\]
Thus the square misses exactly the \(d-1\) nontrivial linear characters. For \((n,q)=(2,2)\), \(\overline G\cong S_3\) and \(\mathrm{St}^2\) already has full support.

For every \(n\ge2\) and every prime power \(q\),
\[
\operatorname{Irr}(\mathrm{St}^3)=\operatorname{Irr}(\overline G).
\]
Consequently
\[
c_{\mathrm{St}}(\operatorname{PGL}_n(q))=
\begin{cases}
2,&\gcd(n,q-1)=1,\\
3,&\gcd(n,q-1)>1.
\end{cases}
\]
The exact \(2/3\) dichotomy and universal-cube conclusion duplicate the earlier SCOPE theorem cited above; the point retained here is the alternate proof and the refinements below.

## Input from Monteiro--Stasinski

Monteiro and Stasinski prove that every nonlinear irreducible character of \(\operatorname{GL}_n(q)\) that is trivial on the center occurs in \(\mathrm{St}^2\). Equivalently, every nonlinear irreducible character of \(\overline G\) occurs in \(\mathrm{St}^2\). They also construct a generally different irreducible character whose square has complete center-trivial support.

## Exact support of the square

The trivial character occurs because the Steinberg character is self-dual:
\[
\langle \mathrm{St}^2,1\rangle=\langle\mathrm{St},\mathrm{St}\rangle=1.
\]
Together with the Monteiro--Stasinski theorem, this accounts for the trivial character and every nonlinear irreducible.

Let \(\lambda\ne1\) be a linear character of \(\overline G\). Inflated to \(\operatorname{GL}_n(q)\), it is a determinant character \(\varepsilon\circ\det\) satisfying the center-triviality condition. Since \(\mathrm{St}\) is self-dual,
\[
\langle\lambda,\mathrm{St}^2\rangle
=\langle\lambda\mathrm{St},\mathrm{St}\rangle.
\]
The twist \(\lambda\mathrm{St}\) is irreducible and is not equal to \(\mathrm{St}\). Indeed, choose \(a\in\mathbb F_q^\times\) with \(\varepsilon(a)\ne1\) and set \(x=\operatorname{diag}(a,1,\ldots,1)\). The element \(x\) is semisimple, its Steinberg value is nonzero, and
\[
(\lambda\mathrm{St})(x)=\varepsilon(a)\mathrm{St}(x)\ne\mathrm{St}(x).
\]
Hence every nontrivial linear character is absent from the square. Outside \(\operatorname{PGL}_2(2)\), the linear character group has order \(d\), so the defect consists of exactly \(d-1\) constituents.

For \(\operatorname{PGL}_2(2)\cong S_3\), the degree-two Steinberg character satisfies
\[
\mathrm{St}^2=1+\operatorname{sgn}+\mathrm{St}.
\]

## A short degree obstruction for the cube

Assume first \((n,q)\ne(2,2)\). Suppose \(\chi\in\operatorname{Irr}(\overline G)\) were absent from \(\mathrm{St}^3\). Then
\[
0=\langle\chi,\mathrm{St}^3\rangle
 =\langle\chi\mathrm{St},\mathrm{St}^2\rangle.
\]
All multiplicities are nonnegative, and the square contains every irreducible except the \(d-1\) nontrivial linears. Therefore every constituent of \(\chi\mathrm{St}\) would have to be one of those linears.

For such a linear \(\lambda\),
\[
[\chi\mathrm{St}:\lambda]
=\langle\chi,\lambda\mathrm{St}\rangle.
\]
Because \(\lambda\mathrm{St}\) is irreducible, this multiplicity is either zero or one. Therefore
\[
\chi(1)\mathrm{St}(1)\le d-1.
\]
But
\[
\mathrm{St}(1)=q^{n(n-1)/2}\ge q,
\qquad d=\gcd(n,q-1)\le q-1,
\]
which is impossible. Hence the cube has full support. The exceptional \(S_3\) case is immediate from its already-full square.

This is an alternate proof of the universal-cube conclusion already present in the 2026/09/17 SCOPE record, whose proof instead uses a cyclic-abelianization completion lemma.

## Twisted central-character fibers in \(\operatorname{GL}_n(q)\)

Let \(G=\operatorname{GL}_n(q)\) and let \(\eta\) be a linear character of \(G\). For every \(r\ge3\),
\[
(\eta\mathrm{St})^r=\eta^r\mathrm{St}^r.
\]
Since \(\mathrm{St}^r\) contains every irreducible character trivial on \(Z(G)\), twisting gives
\[
\operatorname{Irr}((\eta\mathrm{St})^r)
=
\{\rho\in\operatorname{Irr}(G):
\rho|_{Z(G)}=\rho(1)\,\eta^r|_{Z(G)}\}.
\]
This is a convenient central-character-fiber formulation of the cube-and-higher support statement.

## Relation to prior work and scope

The earlier SCOPE record `2026/09/17/steinberg-covering-number-for-pgln--e3667d632f22` has precedence inside this repository for the universal Steinberg cube and exact \(2/3\) covering exponent. Those conclusions are therefore not claimed as original here.

Externally, Monteiro--Stasinski (arXiv:2609.17319) supply the decisive nonlinear square-support theorem. Heide--Saxl--Tiep--Zalesski prove Steinberg-square universality for the relevant finite simple groups of Lie type. Classical character-covering-number literature concerns related but generally different group-wide invariants.

The scientific contribution retained in this record is narrower: an explicit all-linear description of the square defect, a compact degree-obstruction proof of the cube, and the twisted \(\operatorname{GL}_n(q)\) central-character-fiber corollary. No new decomposition multiplicities are claimed.

## References

1. SCOPE, *The Steinberg covering number of PGL_n(q) is 2 or 3*, `2026/09/17/steinberg-covering-number-for-pgln--e3667d632f22`.
2. N. Monteiro and A. Stasinski, *A tensor square theorem for characters of \(\operatorname{GL}_n(q)\)*, arXiv:2609.17319 (2026).
3. G. Heide, J. Saxl, P. H. Tiep and A. E. Zalesski, *Conjugacy action, induced representations and the Steinberg square for simple groups of Lie type*, Proc. London Math. Soc. 106 (2013), 908--930; arXiv:1209.1768.
