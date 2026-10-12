# The four irreducible singular Barth–Bauer sections normalize to the same \(S_4\) genus-two curve
## Finding
Let \(X\subset\mathbb P^3_{\mathbb C}\) be the smooth quartic
\[
\sum_{i=0}^3 z_i^4-6\sum_{i<j}z_i^2z_j^2=0
\]
and let
\[
C_\alpha=X\cap\{z_2+\alpha z_3=0\}.
\]
Naskręcki isolates four geometrically irreducible singular members by
\[
(\alpha^2-2\alpha-1)(\alpha^2+2\alpha-1)=0.
\]
For every one of these four parameters, the normalization is the same genus-two curve:
\[
\widetilde C_\alpha\cong B:\quad y^2=(x^2+1)(x^4-6x^2+1)=x^6-5x^4-5x^2+1.
\]
The reduced geometric automorphism group of \(B\) is \(S_4\). Hence its full geometric automorphism group has order \(48\), including the hyperelliptic involution.

## Assumptions and scope
Everything is over \(\mathbb C\). The claim concerns only Naskręcki's one-parameter family \(C_\alpha\) and the four roots of the factor \(g_1\) in Proposition 2.3. The source proves that these four members are geometrically irreducible quartics with a unique node and geometric genus \(2\). The other eight singular parameters, the roots of \(g_2\), give reducible unions of two conics and are outside the claim. The statement does not assert that the four plane quartic models are identical as embedded curves, only that their normalizations are isomorphic.

## Proof
After eliminating \(z_2=-\alpha z_3\), the source's plane quartic equation is
\[
F=z_0^4+z_1^4+(\alpha^4-6\alpha^2+1)z_3^4-6(\alpha^2+1)(z_0^2+z_1^2)z_3^2-6z_0^2z_1^2.
\]
The singular-irreducible factor is exactly
\[
(\alpha^2-2\alpha-1)(\alpha^2+2\alpha-1)=\alpha^4-6\alpha^2+1.
\]
Hence on every root the \(z_3^4\)-term vanishes. The source identifies the unique node as \([0:0:1]\). Projection from it to \([z_0:z_1]\in\mathbb P^1\) gives the degree-two map from the normalization. On \(z_1=1\), with \(x=z_0/z_1\),
\[
6(\alpha^2+1)(x^2+1)z_3^2=x^4-6x^2+1.
\]
No root of \(\alpha^4-6\alpha^2+1\) has \(\alpha^2+1=0\). Defining
\[
y=\sqrt{6(\alpha^2+1)}(x^2+1)z_3
\]
gives
\[
y^2=(x^2+1)(x^4-6x^2+1)=x^6-5x^4-5x^2+1.
\]
This identifies the normalization function field independently of \(\alpha\). The sextic is square-free, so its smooth projective model has genus \(2\).

Goldstein, Guralnick, Howe and Zieve record, citing Igusa's classification, that in characteristic different from \(2\) and \(5\) the curve
\[
y^2=x^6-5x^4-5x^2+1
\]
has reduced geometric automorphism group \(S_4\), and that this \(S_4\) case occurs uniquely. Over \(\mathbb C\), the full automorphism group therefore has order \(2\cdot24=48\).

## Verification
The accompanying `artifacts/verify.py` checks the polynomial identity defining \(g_1\), nonvanishing of \(\alpha^2+1\), the common sextic, square-freeness, four distinct parameters, and the nondegenerate Hessian at the source's node. It returns `VERIFY_OK`. The automorphism-group classification is a literature theorem rather than a finite computation in the verifier.

## Relationship to prior work
Naskręcki's Propositions 2.3–2.4 determine all singular parameters and prove that the four roots of \(g_1\) give geometrically irreducible quartics with one node and geometric genus \(2\), but do not identify the normalization or automorphism group. Goldstein–Guralnick–Howe–Zieve give the exact sextic model above as the unique reduced-\(S_4\) genus-two case, but do not concern the Barth–Bauer quartic. The new step is the exact projection-from-the-node calculation connecting these two statements.

Targeted semantic database searches for the exact source, exact sextic, normalization, Barth–Bauer aliases, and \(S_4\)-automorphism formulations found no covering statement. The current and prior own ledgers were searched for the same object and aliases and contain no overlapping claim.

## Limitations
The result is over \(\mathbb C\). It does not determine fields of definition for the individual normalization isomorphisms, stable reduction, monodromy, or embedded projective equivalence classes of the four nodal quartics. An obscure differently indexed source could still contain the same cross-identification.

## References
1. B. Naskręcki, *Explicit equations of 800 conics on a Barth-Bauer quartic*, arXiv:2108.13402, first version 30 August 2021, especially Propositions 2.3 and 2.4.
2. D. Goldstein, R. M. Guralnick, E. W. Howe, and M. E. Zieve, *Nonisomorphic curves that become isomorphic over extensions of coprime degrees*, Journal of Algebra 320 (2008), 2526–2558, arXiv:0801.4614, DOI:10.1016/j.jalgebra.2008.06.003.
