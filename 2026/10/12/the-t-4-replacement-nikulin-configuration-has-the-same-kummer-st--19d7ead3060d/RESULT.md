# The \(t=4\) replacement Nikulin configuration has the same Kummer structure
## Finding
For the generic \(t=4\) Kummer surface considered by Roulleau and Sarti, put
\[
F=\frac12(L-A_1-A_2-A_3-A_4).
\]
Their four replacement curves are
\[
B_i=\frac12\!\left(L-3A_i-\sum_{1\le j\le4,\ j\ne i}A_j\right),\qquad 1\le i\le4,
\]
and therefore
\[
F=A_i+B_i\qquad(1\le i\le4).
\]
The complete replacement configuration
\[
\mathcal C'=\{B_1,B_2,B_3,B_4,A_5,\ldots,A_{16}\}
\]
is in the same automorphism orbit as the original configuration
\(\mathcal C=\{A_1,\ldots,A_{16}\}\). Thus the two configurations define the same Kummer structure.

## Assumptions and scope
The surface is the generic Picard-rank-\(17\) Kummer K3 surface of arXiv:1907.12215 in the case \(t=4\), so \(L^2=16\), \(L\cdot A_i=0\), the \(A_i\) are disjoint \((-2)\)-curves, and the Néron--Severi coefficient restriction of the source's Lemma 8 applies: in an expression \(aL-\sum b_iA_i\), all coefficients lie in \(\frac12\mathbb Z\), and when \(a\in\mathbb Z\), a half-integral coefficient forces at least eight of the \(b_i\) to be half-integral. The source proves that the \(B_i\) above are irreducible disjoint \((-2)\)-curves and that \(\mathcal C'\) is a Nikulin configuration.

## Proof
First, direct intersection calculation gives \(F^2=2\), \(F\cdot A_i=1\) for \(i\le4\), and \(F\cdot A_j=0\) for \(j\ge5\). Also \(F=A_i+B_i\), hence \(F\cdot B_i=1\).

We prove that \(F\) is nef and determine its contracted roots. Let \(\Gamma=aL-\sum b_iA_i\) be an irreducible \((-2)\)-curve distinct from the \(A_i\). Since \(L\) is nef, \(a>0\); since \(\Gamma\ne A_i\), one has \(b_i=\frac12\Gamma\cdot A_i\ge0\). From \(\Gamma^2=-2\),
\[
\sum_{i=1}^{16} b_i^2=8a^2+1.
\]
If \(F\cdot\Gamma<0\), then with \(S=b_1+b_2+b_3+b_4\) one has \(S>8a\). Cauchy--Schwarz gives
\[
S^2\le4\sum_{i=1}^4 b_i^2\le32a^2+4,
\]
whereas \(S^2>64a^2\). Hence \(a^2<1/8\), impossible because \(a\in\frac12\mathbb Z\) and \(a>0\). Thus \(F\) is nef.

If \(F\cdot\Gamma=0\), the same estimate gives \(64a^2\le32a^2+4\), so \(a=0\). For a root with \(a=0\), Lemma 8 rules out half-integral coefficients: eight half-integral \(b_i\)'s would already contribute at least \(2\) to \(\sum b_i^2\), while here \(\sum b_i^2=1\). Therefore all \(b_i\) are integral, and exactly one is \(\pm1\). Effectivity leaves precisely the curves \(A_i\). Consequently the \((-2)\)-curves orthogonal to \(F\) are exactly \(A_5,\ldots,A_{16}\).

The standard base-point criterion for a nef divisor on a K3 surface says that if a nef divisor \(D\) with \(D^2=2\) has fixed part, then \(D=2E+R\), where \(E^2=0\), \(R^2=-2\), \(E\cdot R=1\), and hence \(D\cdot R=0\). Applied to \(F\), this would force \(R=A_j\) for some \(j\ge5\), so
\[
E=\frac12(F-A_j)
\]
would have coefficient \(1/4\) on \(L\), contradicting Lemma 8. Hence \(|F|\) is base-point free.

Because \(F\) is primitive, nef and big with \(F^2=2\), \(|F|\) gives the standard genus-two degree-two model \(\varphi_F:X\to\mathbb P^2\), after contracting exactly \(A_5,\ldots,A_{16}\). Let \(\iota\) be its covering involution, lifted to \(X\). For \(i\le4\), the divisor \(A_i+B_i=F\) is the pullback of a line. Both components have \(F\)-degree one, so the involution cannot preserve either component individually; it exchanges them. Thus \(\iota(A_i)=B_i\). The involution preserves the set of curves contracted by \(F\), namely \(\{A_5,\ldots,A_{16}\}\). Therefore
\[
\iota(\mathcal C)=\mathcal C'.
\]
Nikulin configurations in the same automorphism orbit define the same Kummer structure, proving the claim.

## Verification
The accompanying `verify.py` checks all lattice identities used in the construction exactly over \(\mathbb Q\): the squares and pairings of \(F\) and the \(B_i\), the identities \(F=A_i+B_i\), and the numerical inequalities driving the nefness argument. The infinite step is the symbolic Cauchy--Schwarz argument written above, not a finite enumeration. Base-point freeness additionally uses the standard K3 base-point criterion together with the source's Néron--Severi coefficient restriction.

## Relationship to prior work
Roulleau--Sarti construct the four curves \(B_i\), prove that they form a new Nikulin configuration together with \(A_5,\ldots,A_{16}\), and explicitly state in Remark 22(ii) that they do not know whether this configuration gives another Kummer structure. The argument above supplies an automorphism identifying the two configurations. The mechanism is a genus-two polarization that is simultaneously \(A_i+B_i\) for all four replacements.

Targeted searches were made for the source title together with “same Kummer structure”, for the \(t=4\) replacement formulas, for a degree-two polarization or double-plane involution in this case, and for later work by the same authors. No source located in those searches states this \(t=4\) identification.

## Limitations
The statement is for the generic \(t=4\) surface and the specific four-curve replacement configuration of the cited paper. It does not classify all automorphisms or all Nikulin configurations on that K3 surface, and it does not assert an analogous involution for other odd-\(\beta_0\) cases. The originality search cannot exclude an equivalent argument hidden in literature that is poorly indexed or uses substantially different terminology.

## References
1. Xavier Roulleau and Alessandra Sarti, *Explicit Nikulin configurations on Kummer surfaces*, arXiv:1907.12215; first public version 29 July 2019; published in *Advances in Geometry* 22 (2022), 329--340. See Lemma 8, Corollary 21, and Remark 22(ii).
2. B. Saint-Donat, *Projective models of K3 surfaces*, *American Journal of Mathematics* 96 (1974), 602--639, for the standard linear-system criterion used for nef divisors on K3 surfaces.
