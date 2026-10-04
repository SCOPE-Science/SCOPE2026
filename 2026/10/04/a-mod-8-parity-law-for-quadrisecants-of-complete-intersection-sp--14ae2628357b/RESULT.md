# A mod-8 parity law for quadrisecants of complete-intersection space curves
## Finding
Let \(4\le a\le b\), and let \(C\subset\mathbb P^3_{\mathbb C}\) be a general smooth complete-intersection curve of type \((a,b)\). Write
\[
p=ab,\qquad s=a+b,
\]
and let \(Q_{a,b}=\deg\operatorname{Sec}_4(C)\), where \(\operatorname{Sec}_4(C)\) is the Cayley zero-cycle of four-secant lines in the Grassmannian of lines. Then
\[
Q_{a,b}
=
\frac{p}{24}
\left(
2p^3-6p^2s+3ps^2+18ps-26p-66s+144
\right).
\]
The parity of \(Q_{a,b}\) depends only on \(a\bmod 8\) and \(b\bmod 8\). More precisely, \(Q_{a,b}\) is odd exactly when one of the following mutually exclusive conditions holds:

1. Exactly one of \(a,b\) is even, and that even degree is congruent to \(4\) or \(6\pmod 8\).
2. Both \(a,b\) are odd and
\[
a+b\equiv 0\ \text{or}\ 2\pmod 8.
\]

Thus exactly \(24\) of the \(64\) ordered residue pairs modulo \(8\) have odd quadrisecant degree. For example,
\[
Q_{4,5}=1275,\qquad Q_{5,5}=4775,\qquad Q_{6,7}=69825,
\]
whereas
\[
Q_{4,4}=320,\qquad Q_{4,6}=3468,\qquad Q_{5,7}=27230
\]
are even.

There is also a real consequence. Let \(C\subset\mathbb P^3_{\mathbb R}\) be a smooth real complete intersection of type \((a,b)\) belonging to the real open locus on which the four-secant scheme is zero-dimensional. If the residue criterion above makes \(Q_{a,b}\) odd, then \(C\) has at least one real quadrisecant line.

## Assumptions and scope
The complex statement concerns a general smooth complete intersection of two surfaces of degrees \(a,b\ge4\) in \(\mathbb P^3\). Generality is used only to remain in the finite four-secant regime: for general complete intersections with both defining degrees at least four, the maximum multisecant order is four, and the four-secant locus is zero-dimensional.

The real statement is deliberately phrased for the real open locus where that zero-dimensional regime holds. It asserts existence of a real point of the quadrisecant scheme, not transversality or a lower bound on the number of distinct real quadrisecants.

## Proof
A smooth complete intersection of type \((a,b)\) has degree
\[
d=ab=p
\]
and, by adjunction, genus
\[
g=1+\frac{ab(a+b-4)}2
=
1+\frac{p(s-4)}2.
\]
For a smooth space curve of degree \(d\) and genus \(g\), the classical Cayley number is
\[
\frac{(d-2)(d-3)^2(d-4)}{12}
-
\frac{g(d^2-7d+13-g)}2.
\]
Le Barz interprets this enumerative number as the degree of a zero-cycle \(\operatorname{Sec}_4(C)\) in the Grassmannian, while Hartshorne--Schlesinger use the same Cayley number in their four-secant existence argument.

Substituting the complete-intersection degree and genus and simplifying gives
\[
Q_{a,b}
=
\frac{p}{24}
\left(
2p^3-6p^2s+3ps^2+18ps-26p-66s+144
\right).
\]
Set
\[
N(a,b)=24Q_{a,b}.
\]
To determine \(Q_{a,b}\bmod 2\), it is enough to determine \(N(a,b)\bmod 48\).

The parity is periodic with period \(8\) in each argument. Indeed, a direct expansion gives
\[
N(a+8,b)-N(a,b)=16bR(a,b)
\]
for an integral polynomial \(R\), and modulo \(3\) one has
\[
bR(a,b)
\equiv
b^2\left((a^3+a)b^2+a+2b^2+1\right)
\pmod3.
\]
If \(3\mid b\), this is zero. Otherwise \(b^2\equiv1\pmod3\), and Fermat's congruence \(a^3\equiv a\pmod3\) reduces the bracket to \(3a+3\), again zero. Hence
\[
48\mid N(a+8,b)-N(a,b).
\]
By symmetry the same holds after replacing \(b\) by \(b+8\). Therefore \(Q_{a,b}\bmod2\) is determined by the \(64\) residue pairs modulo \(8\).

Exact evaluation on those \(64\) classes gives the following equivalent description. If both degrees are even, \(Q_{a,b}\) is even. If exactly one is even, odd parity occurs precisely when the even residue is \(4\) or \(6\). If both are odd, odd parity occurs precisely when their sum is \(0\) or \(2\) modulo \(8\). This yields \(24\) odd ordered residue pairs.

For the real consequence, the zero-dimensional four-secant scheme is defined over \(\mathbb R\). Every non-real closed point occurs with its complex conjugate and contributes even total degree. An odd total degree therefore forces a real closed point of degree one, which is a real point of the Grassmannian and hence a real projective line meeting \(C\) in a subscheme of length at least four.

## Verification
The bundled exact-integer checker performs three independent finite verifications after the uniform symbolic reduction.

First, it recomputes the complete-intersection specialization of the Cayley formula for all \(4\le a,b\le80\). Second, it verifies the period-\(8\) parity law directly throughout that box. Third, it checks all \(64\) residue classes and verifies that the stated logical criterion agrees exactly with oddness in \(24\) classes.

The checker is regression evidence for the arithmetic manipulations. The infinite theorem does not rest on bounded sampling: period \(8\) is proved symbolically above, so the \(64\)-class evaluation is exhaustive.

## Relationship to prior work
Patrick Le Barz develops the secant-cycle formalism for smooth algebraic curves and defines the zero-cycle \(\operatorname{Sec}_4(C)\) whose degree is the Cayley four-secant number. He also discusses excess-multiplicity phenomena for special complete intersections. Robin Hartshorne and Enrico Schlesinger state the Cayley number with the sign convention used here and record that the maximum multisecant order of a general complete intersection of type \((a,b)\) with both degrees at least four is four.

The inspected sources supply the enumerative input and the finite-multisecant regime. They do not state the mod-\(8\) parity classification, the \(24/64\) residue count, or its real-existence consequence. Claim-specific searches for parity, odd quadrisecant counts, and real quadrisecants of complete-intersection curves did not locate a source giving these conclusions.

## Limitations
The parity theorem concerns the degree of the quadrisecant zero-cycle. On special curves where the four-secant locus acquires excess dimension, that degree need not equal the cardinality of the set of quadrisecant lines. The real conclusion is therefore restricted to the zero-dimensional real open locus.

The result does not determine how many real quadrisecants occur when the degree is even, nor does it assert that the zero-cycle is reduced. It also does not treat complete intersections involving a quadric or cubic surface, where higher-order multisecants and excess phenomena are structurally different.

A residual literature risk remains because nineteenth- and twentieth-century multisecant formulas are dispersed across sources; no inspected or retrieved source stated the residue classification itself.

## References
Patrick Le Barz, *Formules pour les espaces multisécants aux courbes algébriques*, Comptes Rendus Mathématique 340 (2005), 743--746. DOI: 10.1016/j.crma.2005.04.002. Published online 10 May 2005.

Robin Hartshorne and Enrico Schlesinger, *Gonality of a general ACM curve in projective 3-space*, arXiv:0812.1634, first submitted 9 December 2008; later published in Pacific Journal of Mathematics 251 (2011), 269--313. The preprint lists MSC 14H50 and 14H51.
