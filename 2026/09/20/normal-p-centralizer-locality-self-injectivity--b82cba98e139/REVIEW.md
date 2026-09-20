# Review: locality and self-injectivity of normal p-subgroup centralizer algebras

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The proof separates into two standard structural inputs and one socle
argument.

For \(1\ne P\unlhd G\), the Brauer map
\[
\operatorname{Br}_P:(kG)^P\to kC_G(P)
\]
is a surjective algebra map. Its kernel is spanned by non-singleton \(P\)-orbit
sums. Normality of the \(p\)-subgroup forces \(P\) to act trivially on every simple
\(kG\)-module, so each such orbit sum acts as its orbit size times one operator.
That size is divisible by \(p\), hence every kernel basis element lies in
\(J(kG)\). The kernel is therefore nilpotent and lies in the Jacobson radical of
\((kG)^P\). It follows that the semisimple quotient of \((kG)^P\) is the same as
that of \(kC_G(P)\).

The locality criterion then reduces to the standard fact that a finite group
algebra in characteristic \(p\) is local exactly for a \(p\)-group.

In the local case, augmentation is the unique simple quotient. The full group sum
\(\omega_G\) is killed by the radical. If \(P\) is noncentral, the Brauer kernel is
nonzero and has nonzero socle. This socle is independent of \(k\omega_G\), because
the Brauer image of \(\omega_G\) is the nonzero sum of the elements of \(C_G(P)\),
whereas the kernel has zero Brauer image. Thus the regular module has socle
dimension at least two. A finite-dimensional local self-injective algebra with
residue field \(k\) has one-dimensional socle, so self-injectivity fails. If \(P\)
is central, the fixed algebra is \(kG\); locality then forces \(G\) to be a
\(p\)-group, and \(kG\) is symmetric.

The implications among symmetric, Frobenius and self-injective are used only in
directions valid for finite-dimensional algebras, with the converse supplied by
the explicit central case. If \(P\) is central then the Brauer kernel is zero,
as required.

Under the stronger hypothesis \(C_P(g)=1\) for every \(g\notin P\), each outside
\(P\)-orbit is exactly one coset \(Pg\). Direct multiplication of coset sums gives
\(X_qX_r=|P|X_{qr}=0\) and multiplication by \(kP\) through augmentation. This
verifies the explicit algebra isomorphism
\(A\cong Z(kP)\ltimes k^{[G:P]-1}\) and the stated radical/socle formulas.

## Originality

**PASS, to the best of our knowledge.** Danz--Ellers--Murray (2013) explicitly
raise the symmetry question for modular centralizer algebras and, for a normal
\(p\)-subgroup, record the surjective Brauer map with nilpotent kernel. Their paper
does not state the locality/self-injectivity classification above.

Allan (2011), Proposition 2.2, proves that \(kR^Q\) is not self-injective when
\(R\) is a \(p\)-group and \(Q\) is a noncentral subgroup. The present statement
uses normality of \(P\) to pass through the Brauer quotient for an arbitrary finite
ambient group \(G\), obtains the exact criterion
\(C_G(P)\) a \(p\)-group for locality, and then classifies self-injectivity,
Frobenius and symmetry throughout that local regime.

Searches through current indexed literature using combinations of “centralizer
algebra”, “normal p-subgroup”, “Brauer map/kernel”, “local”, “self-injective”,
“symmetric”, “self-centralizing”, and “characteristic p” did not locate an exact
or stronger statement. The closest directly relevant sources remain the two papers
above.

The residual originality risk is non-negligible because the proof combines
standard tools in a short way. An equivalent result could be buried as an
unstated corollary in modular Hecke-algebra or Brauer-construction literature under
different terminology.

## Value

**PASS.** The theorem converts a qualitative symmetry question into an exact
group-theoretic classification for a natural and broad family. It gives the
semisimple quotient of \((kG)^P\) for normal \(P\), an if-and-only-if locality
criterion \(C_G(P)\) is a \(p\)-group, and an if-and-only-if
self-injective/Frobenius/symmetric criterion inside that local family, with
immediate consequences for groups of characteristic \(p\) and for Frobenius groups
with \(p\)-group kernel. In the latter case it additionally gives an explicit
square-zero extension model rather than only a negative symmetry statement.

The argument also explains the obstruction: a nonzero Brauer kernel contributes
socle independently of the universal group-sum socle vector.

## Scientific limitations

The theorem requires \(P\) to be normal for the nilpotence argument. It does not
classify symmetry when \(C_G(P)\) is not a \(p\)-group, so the nonlocal case remains
outside the result. The originality assessment is qualified by the possibility of
an equivalent unstated consequence in older modular-representation or Hecke-algebra
literature.

## Sources checked

- S. Danz, H. Ellers and J. Murray, *The Centralizer of a Subgroup in a Group
  Algebra*, Proc. Edinburgh Math. Soc. 56 (2013), 49--56,
  DOI 10.1017/S0013091512000077. The full author manuscript was inspected,
  including the orbit-sum basis, the symmetry question, and the Brauer-map
  argument for normal \(p\)-subgroups.
- A. Allan, *Modular Centralizer Algebras Corresponding to p-Groups*,
  J. Algebra 339 (2011), 156--171, DOI 10.1016/j.jalgebra.2011.04.026,
  arXiv:1011.3559. The full arXiv text was inspected, especially Proposition 2.2
  and the split-extension discussion.
