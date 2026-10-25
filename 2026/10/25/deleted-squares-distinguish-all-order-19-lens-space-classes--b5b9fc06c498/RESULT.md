# Deleted squares distinguish all order-19 lens-space classes

## Finding

For the three-dimensional lens spaces \(L(19,q)\), with normalized parameters \(1\le q\le9\), the ordered deleted squares distinguish all five homeomorphism classes. Precisely, if \(q'\not\equiv \pm q^{\pm1}\pmod{19}\), then

\[
F_2(L(19,q))\not\simeq F_2(L(19,q')).
\]

Here \(F_2(L)=\{(x,y)\in L\times L:x\ne y\}\). There are \(32\) nonhomeomorphic normalized pairs; an exact finite-field Massey-product obstruction rejects every one.

## Assumptions and scope

The lens-space convention is \(L(p,q)=S^3/\langle(z,w)\mapsto(\zeta z,\zeta^q w)\rangle\), where \(\zeta=e^{2\pi i/p}\), \(p\) is an odd prime, and \(q\) is coprime to \(p\). For \(p=19\), parameters may be normalized to \(1\le q\le9\). The standard homeomorphism criterion is \(q'\equiv\pm q^{\pm1}\pmod{19}\). The claim concerns only this prime-order family and ordered two-point configuration spaces; it does not settle the analogous question for arbitrary primes or manifolds.

## Proof

Evans-Lee and Saveliev prove that a homotopy equivalence between deleted squares of \(L(p,q)\) and \(L(p,q')\), for odd prime \(p\), induces a scalar diagonal map on fundamental groups. Its scalar \(\alpha\) must satisfy \(q\alpha^2\equiv q'\) or \(-q'\pmod p\). On the second cohomology of the universal covers, the induced map is determined by \(c=f^*(1)\) and \(\beta=\alpha^{-1}\):

\[
f^*(t^k)=t^{\beta k}c.
\]

With coefficients in \(\mathbb F_2\), the relevant groups are identified with \(R=\mathbb F_2[t]/(1+t+\cdots+t^{p-1})\). For \(p=19\), the order of \(2\) modulo \(19\) is \(18\), so the cyclotomic polynomial \(1+t+\cdots+t^{18}\) is irreducible over \(\mathbb F_2\); hence \(R\cong\mathbb F_{2^{18}}\), and every nonzero \(c\) is a unit.

The published formula for the triple Massey operation is encoded by \(M_q(a,b)=\langle t^a,1,t^b\rangle\). For \(b\ne0\), if \((-bq\bmod p)\in\{1,\ldots,q-1\}\), then \(M_q(0,b)=\sum_{i=1}^{b}t^i\); if \((bq\bmod p)\in\{1,\ldots,q-1\}\), then \(M_q(0,b)=\sum_{i=b}^{p-1}t^i\); otherwise it is zero. For nonzero \(a,b\), define \(a\prec_q b\) when either \((bq\bmod p)\in\{1,\ldots,q-1\}\) and \(a\ge b\), or \((-bq\bmod p)\in\{1,\ldots,q-1\}\) and \(a\le b\). The formula is \(t^a+t^b\) if both \(a\prec_q b\) and \(b\prec_q a\), \(t^a\) if only the first holds, \(t^b\) if only the second holds, and zero otherwise. Indices are represented by \(0,\ldots,p-1\); the \(a=0\) or \(b=0\) cases use the displayed formula and symmetry. A general monomial triple follows from the shift rule \(\langle t^i,t^j,t^k\rangle=t^jM_q(i-j,k-j)\). The defining indeterminacy is retained throughout the test.

Naturality of Massey products requires, for every \(k,\ell\in\mathbb Z/19\mathbb Z\),

\[
\mu_{q'}(t^{\beta k}c,c,t^{\beta\ell}c)-f^*\!\left(\mu_q(t^k,1,t^\ell)\right)
\in\operatorname{span}_{\mathbb F_2}\{t^{\beta k}c,t^{\beta\ell}c\}.
\]

The included C++17 program enumerates all normalized nonhomeomorphic pairs \((q,q')\), all allowed \(\beta\), and every nonzero vector \(c\in R\). For each candidate it checks all \(19^2\) ordered pairs \((k,\ell)\) using exact bit-mask arithmetic over \(\mathbb F_2\). It finds \(32\) nonhomeomorphic homotopy-equivalent pairs and zero candidates satisfying all Massey constraints. Thus no deleted-square homotopy equivalence exists for any such pair. The computation also checks the published \(p=5,q=2\) formula examples, a known homeomorphic pair at \(p=19\), and known distinguishing examples at \(p=7\) and \(p=11\).

## Verification

The executable `verify` was built from the included `verify.cpp` and run from the package directory. It exits successfully only if the formula controls pass, the homeomorphic \((19,2),(19,9)\) pair has the expected \(19\) survivors for each allowed scalar, and the known nonhomeomorphic controls \((7,1),(7,2)\) and \((11,2),(11,3)\) have no survivors. The full output is in `verification-output.txt`. For the target family, all \(32\) pairs have zero survivors for both scalar choices. This is a finite exact obstruction computation, not a numerical approximation.

## Relationship to prior work

Longoni and Salvatore used a nontrivial Massey product to distinguish deleted squares for a homotopy-equivalent pair of lens spaces at order \(7\). Miller computed the Massey-product structure for universal covers of two-point configuration spaces of three-dimensional lens spaces. Evans-Lee and Saveliev derived a scalar-map restriction and reproduced the full Massey formulas; their explicit examples include primes \(11\), \(13\), and \(17\), and they left open whether deleted-square homotopy type distinguishes lens spaces up to homeomorphism. The present result is the complete order-\(19\) case: it checks all \(32\) nonhomeomorphic normalized pairs, rather than adding only one example. published-finding corpus searches for the exact \(p=19\) deleted-square claim returned no matching record; the closest records concerned unrelated topology.

## Limitations

The conclusion is restricted to three-dimensional lens spaces with fundamental group \(\mathbb Z/19\mathbb Z\). It does not prove that deleted squares distinguish lens spaces for arbitrary prime order, nor does it classify configuration spaces of more than two points. The proof uses the published Massey formulas and the published necessary condition on induced maps; the exhaustive finite calculation is reproducible, but no independent audit has been performed. The literature search is bounded and cannot exclude an unindexed prior computation of the same finite case.

## References

1. K. Evans-Lee and N. Saveliev, *On the deleted squares of lens spaces*, arXiv:1502.03408v1, first public version 2015-02-11. Theorem on induced maps and Sections 7.1–7.3.
2. R. Longoni and P. Salvatore, *Configuration spaces are not homotopy invariant*, arXiv:math/0401075v1, first public version 2004-01-08.
3. M. S. Miller, *Rational homotopy models for two-point configuration spaces of lens spaces*, *Homology, Homotopy and Applications* 13 (2011), 43–62, DOI 10.4310/HHA.2011.v13.n2.a4.
