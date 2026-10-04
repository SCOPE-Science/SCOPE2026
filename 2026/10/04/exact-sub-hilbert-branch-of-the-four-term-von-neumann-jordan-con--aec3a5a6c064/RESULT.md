# Exact sub-Hilbert branch of the four-term von Neumann–Jordan constant on \(\ell_q\)
## Finding
For every index set \(I\) with at least two elements, every \(1\le q<2\), and every \(0\le\lambda\le1\), the real sequence space \(\ell_q(I)\) satisfies
\[
C'''_{\mathrm{NJ}}(\lambda,\ell_q(I))=
\bigl(\lambda^q+(1-\lambda)^q\bigr)^{2/q}+2^{2/q}\lambda(1-\lambda).
\]
Here \(C'''_{\mathrm{NJ}}\) is the four-term von Neumann–Jordan-type constant defined below. For every allowed \(q\) and \(\lambda\), equality is attained by any two distinct coordinate unit vectors.

## Assumptions and scope
All spaces are real. Let \(X\) be a Banach space and \(S_X\) its unit sphere. For \(0\le\lambda\le1\), define
\[
C'''_{\mathrm{NJ}}(\lambda,X)=\sup_{x,y\in S_X}\frac12\Bigl(
\|\lambda x+(1-\lambda)y\|^2+\|\lambda x-(1-\lambda)y\|^2
+\lambda(1-\lambda)\|x-y\|^2+\lambda(1-\lambda)\|x+y\|^2
\Bigr).
\]
The finding concerns \(X=\ell_q(I)\), where \(I\) has at least two elements and \(1\le q<2\). No finite-dimensionality assumption is used.

## Proof
First assume \(1<q<2\), and put \(r=q/(q-1)>2\). Clarkson's sharp inequality gives, for arbitrary \(u,v\in\ell_q(I)\),
\[
\|u+v\|_q^r+\|u-v\|_q^r
\le 2\bigl(\|u\|_q^q+\|v\|_q^q\bigr)^{r-1}.
\]
For nonnegative \(A,B\) and \(r\ge2\), the two-dimensional norm comparison
\[
A^2+B^2\le 2^{1-2/r}(A^r+B^r)^{2/r}
\]
therefore yields
\[
\|u+v\|_q^2+\|u-v\|_q^2
\le2\bigl(\|u\|_q^q+\|v\|_q^q\bigr)^{2/q}.
\]
Indeed, the powers agree because \((r-1)/r=1/q\).

Take \(x,y\in S_{\ell_q(I)}\), set \(u=\lambda x\) and \(v=(1-\lambda)y\), and apply the preceding inequality. This gives
\[
\|\lambda x+(1-\lambda)y\|_q^2+\|\lambda x-(1-\lambda)y\|_q^2
\le2\bigl(\lambda^q+(1-\lambda)^q\bigr)^{2/q}.
\]
A second application with \(u=x\) and \(v=y\) gives
\[
\|x+y\|_q^2+\|x-y\|_q^2\le2\,2^{2/q}.
\]
Substitution in the definition proves the desired upper bound.

Choose distinct indices \(i,j\in I\) and set \(x=e_i\), \(y=e_j\). Their supports are disjoint, so
\[
\|\lambda e_i\pm(1-\lambda)e_j\|_q=
\bigl(\lambda^q+(1-\lambda)^q\bigr)^{1/q},
\qquad
\|e_i\pm e_j\|_q=2^{1/q}.
\]
Both upper bounds are then equalities, proving the formula for \(1<q<2\).

For \(q=1\), the triangle inequality gives
\[
\|\lambda x\pm(1-\lambda)y\|_1\le1,
\qquad
\|x\pm y\|_1\le2,
\]
for unit vectors \(x,y\). Hence
\[
C'''_{\mathrm{NJ}}(\lambda,\ell_1(I))\le1+4\lambda(1-\lambda).
\]
Distinct coordinate unit vectors attain equality. This is exactly the displayed formula at \(q=1\).

## Verification
The proof is analytic and does not depend on numerical experiments. The exponent conversion was checked directly from \(r=q/(q-1)\): one has \((r-1)/r=1/q\), so the Clarkson bound followed by the two-coordinate norm comparison gives precisely the power \(2/q\). The disjoint-support witness was substituted into all four norm terms, giving equality term by term. The endpoint \(q=1\) was checked separately, rather than inferred by a limiting argument.

At the nonclaimed boundary \(q=2\), the formula simplifies to \(1\), agreeing with the Hilbert-space parallelogram identity and with the published \(q\ge2\) calculation. This boundary agreement is a consistency check, not part of the novelty claim.

## Relationship to prior work
Wang, Liu, Li, Ni, Yang, Sarfraz and Li define \(C'''_{\mathrm{NJ}}(\lambda,X)\) in arXiv:2110.15741. In the current version, their Example 3.1 computes the \(\ell_q\) value for \(q\ge2\) (stated on the normalized range \(0<\lambda\le1/2\)); the surrounding text explicitly introduces that calculation for \(q\ge2\). The inspected source does not give the complementary \(1\le q<2\) formula proved here. The present result supplies that missing exponent branch and identifies disjoint-support extremizers throughout it.

Searches for the notation, its verbal aliases, the sub-Hilbert exponent range, and the resulting formula did not locate a stronger or equivalent published formula. Those searches reduce but cannot eliminate the risk of differently notated or unindexed prior work.

## Limitations
The claim is restricted to real \(\ell_q(I)\) and to \(1\le q<2\). No assertion is made here about other Banach lattices, equality classification beyond the exhibited disjoint-support extremizers, or novelty of the already published \(q\ge2\) branch. Bibliographic search cannot prove absolute novelty, so differently indexed literature remains a residual risk.

## References
1. Y. Wang, Q. Liu, Q. Li, Q. Ni, Z. Yang, M. Sarfraz, and Y. Li, *Novel constants based on the generalization of Von Neumann-Jordan constant*, arXiv:2110.15741. Earliest public preprint: 2021-10-29. See the definition of \(C'''_{\mathrm{NJ}}\) and Example 3.1 in the current version.
2. J. A. Clarkson, *Uniformly convex spaces*, Transactions of the American Mathematical Society 40 (1936), 396–414.
