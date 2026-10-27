# Exact count of integer Lucas sequences with bounded roots

## Finding

For an integer radius \\(T\\ge2\\), let \(N(T)\) be the number of distinct nondegenerate Lucas sequences
\[
U_0=0,\qquad U_1=1,\qquad U_{n+2}=A U_{n+1}-B U_n,
\]
with \(A,B\in\mathbb Z\) and both characteristic roots of \(x^2-Ax+B\) in the closed disk \(|z|\le T\). Here nondegenerate means \(AB\ne0\) and the ratio of the two roots is not a root of unity. Then
\[
\boxed{N(T)=4T^3-2T^2-2T-2\left\lfloor\frac{T}{\sqrt2}\right\rfloor-2\left\lfloor\frac{T}{\sqrt3}\right\rfloor.}
\]

Distinct parameter pairs give distinct sequences because \(U_2=A\) and \(U_3=A^2-B\).

## Assumptions and scope

The radius \(T\) is an integer with \\(T\\ge2\\). Parameters \(A,B\) are integers. The characteristic roots \(\alpha,\beta\) are the roots of \(z^2-Az+B\). The nondegeneracy convention is \(AB\ne0\) and \(\alpha/\beta\) not a root of unity. No formula for nonintegral radii is asserted.

## Proof

First, for real integer coefficients and integer \(T>0\), the two roots lie in \(|z|\le T\) exactly when
\[
|B|\le T^2,\qquad |A|T\le T^2+B. \tag{1}
\]
Necessity follows from \(B=\alpha\beta\) and, for real roots, the endpoint products \((T-\alpha)(T-\beta)\) or \((T+\alpha)(T+\beta)\); for nonreal roots, \(B=|\alpha|^2\) and \(|A|\le2\sqrt B\le T+B/T\). Conversely, nonreal roots have modulus \(\sqrt B\), so (1) suffices. For real roots, if one root has modulus greater than \(T\), the other has modulus less than \(T\) by \\(|B|\\le T^2\\); according to whether the roots have the same or opposite signs, \(T^2+B-|A|T\) is respectively \((T-|\alpha|)(T-|\beta|)<0\) or \((T-|\alpha|)(T+|\beta|)<0\), contradicting (1).

For each integer \(B\in[-T^2,T^2]\), (1) permits exactly
\[
2\left(T+\left\lfloor\frac BT\right\rfloor\right)+1
\]
integer values of \(A\). Pairing \(B\) with \(-B\) gives
\[
\sum_{B=-T^2}^{T^2}\left\lfloor\frac BT\right\rfloor=-(T^2-T),
\]
since each positive nonmultiple of \(T\) contributes \(-1\) to the paired sum and multiples contribute zero. Thus the total number of integer pairs satisfying the root bound, before exclusions, is \(4T^3+4T+1\).

The pairs with \(A=0\) or \(B=0\), counted once at their intersection, number \(2T^2+2T+1\). Among the remaining pairs, \(\varepsilon=\alpha/\beta\) can be a root of unity only of order \(1,3,4,6\): a root of unity in a field of degree at most two has order \(1,2,3,4\), or \(6\), and order \(2\) forces \(A=0\), already excluded. The identity
\[
\frac{A^2}{B}=\varepsilon+2+\varepsilon^{-1}
\]
gives \(A^2/B=4,1,2,3\) for orders \(1,3,4,6\), respectively. Since \(A,B\) are integers, these relations force exactly the remaining degenerate families
\[
(A,B)=(2r,r^2),\ (r,r^2),\ (2r,2r^2),\ (3r,3r^2),\qquad r\in\mathbb Z\setminus\{0\}.
\]
Their root moduli are respectively \(|r|,|r|,\sqrt2|r|,\sqrt3|r|\). They are disjoint and contribute
\[
4T+2\left\lfloor\frac{T}{\sqrt2}\right\rfloor+2\left\lfloor\frac{T}{\sqrt3}\right\rfloor
\]
pairs. Subtracting both exclusion counts from \(4T^3+4T+1\) yields the stated formula.

## Verification

The argument is symbolic and applies to every integer \\(T\\ge2\\). The supplementary script `verify.py` checks the exact counting formula against direct enumeration of the integer parameter region for each \(T=2,\ldots,40\). That finite check is only a sanity check; it is not used as a proof for all radii.

## Relationship to prior work

Hajdu and Tijdeman study the same parameter-counting problem in *Integers represented by Lucas sequences*, especially Theorem 2.2 and Section 4. Their Theorem 2.2 gives upper and lower bounds for the number of nondegenerate Lucas sequences with bounded characteristic roots; the published version improves the integer-radius lower bound to \\(4T^3-9T^2\\) in Remark 2. Their Lemma 4.1 lists the nonreal root-of-unity families under a nonzero-discriminant hypothesis. Neither the arXiv version nor the inspected published version states the exact integer-radius formula; it follows by counting the integer points in the exact root-bound region and also removing the repeated-root family. This is an exact refinement of that counting problem, not a claim about the values of individual sequence terms.

Akiyama and Pethő study distributions and volumes for real-coefficient polynomials with bounded roots. That is related geometric context, but the accessible abstract does not establish an exact count for integer Lucas parameters.

## Limitations

The formula concerns integer radii and the standard nondegeneracy convention only. The finite script checks finitely many radii; universality rests on the proof above. No claim is made that all literature has been exhaustively searched, and independent audit has not been performed.

## References

1. L. Hajdu and R. Tijdeman, “Integers represented by Lucas sequences,” arXiv:2408.04982, first submitted 2024-08-09; see Theorem 2.2, Lemma 4.1, and Section 4. https://arxiv.org/abs/2408.04982
2. S. Akiyama and A. Pethő, “On the distribution of polynomials with bounded roots, I. Polynomials with real coefficients,” *Journal of the Mathematical Society of Japan* 66 (2014), 927–949. https://doi.org/10.2969/jmsj/06630927
