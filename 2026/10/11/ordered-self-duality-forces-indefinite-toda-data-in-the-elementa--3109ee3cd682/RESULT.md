# Ordered self-duality forces indefinite Toda data in the elementary Askey–Wilson family

## Finding

Fix
\\[
0<q<1.
\\]
For the canonical elementary Askey--Wilson parameters
\\[
a=q^{A+1},\\qquad
b=-q^{P+1},\\qquad
c=q^{B+1/2},\\qquad
d=-q^{Q+1/2},
\\]
with
\\[
A,P,B,Q\\in\\mathbb N_0,
\\]
consider the ordered duality transformation of the Askey--Wilson parameters used in the recent determinant formula.

The ordered parameter quadruple is fixed by duality exactly when
\\[
A=P+B+Q.
\\]
On this fixed locus, the reflectionless Toda spectral data occurring in the determinant representation have exactly
\\[
\\kappa_-
=
A+\\mathbf 1_{\\{P+Q\\text{ is odd}\\}}
\\]
negative norming parameters.

Consequently every nontrivial fixed point has indefinite norming data. In addition, its Toda tau function has a zero at
\\[
x=0
\\]
of exact multiplicity
\\[
A.
\\]
The unique ordered-duality fixed member with positive norming data and a zero-free tau function is therefore
\\[
(A,P,B,Q)=(0,0,0,0),
\\]
which is the free plane-wave case
\\[
(a,b,c,d)=(q,-q,q^{1/2},-q^{1/2}).
\\]

Thus, inside the complete discrete family treated by the source, nontrivial ordered bispectral self-duality is incompatible with the standard positive reflectionless-scattering chamber.

## Assumptions and scope

The parameter ordering is the canonical one used by the source:
\\[
(a,b,c,d)
=
(q^{A+1},-q^{P+1},q^{B+1/2},-q^{Q+1/2}).
\\]
The phrase "fixed by duality" means equality with the ordered dual parameter quadruple under the source transformation, not equality only after a permutation or a Weyl-group parameter reflection.

The norming parameters are the real Toda auxiliary parameters in the source's reflectionless Baker--Akhiezer representation. Their signs are exactly the signs \\(\\epsilon_j^\\pm\\) occurring in the source's specialized spectral data.

The conclusion about smoothness is deliberately limited: positivity of all norming parameters is the source's sufficient condition for a smooth real Baker--Akhiezer function. The result proves that every nontrivial ordered fixed point lies outside that positive chamber and that its tau denominator vanishes at the origin. It does not assert that every possible numerator fails to cancel every tau zero for every spectral value.

## Proof

The source gives the dual exponent transformation
\\[
\\widehat A
=
\\frac{A+P+B+Q}{2},
\\qquad
\\widehat P
=
\\frac{A+P-B-Q}{2},
\\]
\\[
\\widehat B
=
\\frac{A-P+B-Q}{2},
\\qquad
\\widehat Q
=
\\frac{A-P-B+Q}{2}.
\\]
Therefore
\\[
(\\widehat A,\\widehat P,\\widehat B,\\widehat Q)
=(A,P,B,Q)
\\]
if and only if any, hence all, of the four equations reduce to
\\[
A=P+B+Q.
\\]
This proves the fixed-locus classification.

It remains to count the negative Toda norming parameters. For either sign sector, write
\\[
r=n_+,
\\qquad
s=n_-.
\\]
The source index set is
\\[
I
=
\\{1,2,\\ldots,|r-s|,
|r-s|+2,\\ldots,r+s\\}.
\\]
Let
\\[
d=|r-s|.
\\]

If
\\[
r\\ge s,
\\]
then on the initial block
\\[
1\\le j\\le d
\\]
the source position variable satisfies \\(\\eta_j=j\\), and hence
\\[
\\epsilon_j=(-1)^{\\eta_j+j}=1.
\\]
The tail consists of
\\[
j=d+2k,
\\qquad
1\\le k\\le s.
\\]
There
\\[
\\eta_j=d+k,
\\]
so
\\[
\\epsilon_j
=(-1)^{2d+3k}
=(-1)^k.
\\]
Exactly
\\[
\\left\\lceil\\frac{s}{2}\\right\\rceil
\\]
of these signs are negative.

If
\\[
r<s,
\\]
then the source sign is
\\[
\\epsilon_j=(-1)^{\\eta_j}.
\\]
The initial block contributes
\\[
\\left\\lceil\\frac d2\\right\\rceil
\\]
negative signs. On the tail
\\[
j=d+2k,
\\qquad
1\\le k\\le r,
\\]
one has \\(\\eta_j=d+k\\). If \\(d\\) is even, the tail contributes \\(\\lceil r/2\\rceil\\) negative signs; if \\(d\\) is odd, it contributes \\(\\lfloor r/2\\rfloor\\). In either case the total is
\\[
\\left\\lceil\\frac{s}{2}\\right\\rceil.
\\]
Hence, for the two source sectors together,
\\[
\\kappa_-
=
\\left\\lceil\\frac{n^+_-}{2}\\right\\rceil
+
\\left\\lceil\\frac{n^-_-}{2}\\right\\rceil.
\\]

The source parameter identification gives
\\[
n^+_-=A+B.
\\]
On the fixed locus,
\\[
A-B=P+Q\\ge0,
\\]
so the second minus parameter is
\\[
n^-_-=A-B=P+Q.
\\]
Thus
\\[
\\kappa_-
=
\\left\\lceil\\frac{A+B}{2}\\right\\rceil
+
\\left\\lceil\\frac{A-B}{2}\\right\\rceil.
\\]
Because
\\[
A-B=P+Q,
\\]
the two numerators have the same parity. If \\(P+Q\\) is even, the sum is \\(A\\); if \\(P+Q\\) is odd, both ceilings contribute an extra half and the sum is \\(A+1\\). Hence
\\[
\\kappa_-
=
A+\\mathbf 1_{\\{P+Q\\text{ is odd}\\}}.
\\]

For a nontrivial fixed point,
\\[
A=P+B+Q>0.
\\]
The tau product from the source contains the factor
\\[
\\prod_{\\ell=1}^{A}
(1-q^{x+\\ell})^{A+1-\\ell}
(1-q^{x+1-\\ell})^{A+1-\\ell}.
\\]
At
\\[
x=0,
\\]
the unique vanishing factor in the entire product is the second factor with \\(\\ell=1\\):
\\[
(1-q^x)^A.
\\]
Every plus-sign factor is strictly positive for real \\(x\\), and the half-integer minus factors are nonzero at \\(x=0\\). Therefore
\\[
\\operatorname{ord}_{x=0}\\tau(x)=A.
\\]

Finally, if
\\[
A=P=B=Q=0,
\\]
both index sets are empty, there are no negative norming parameters, the tau function is identically one, and the source reduces the Askey--Wilson function to the free plane wave. This proves all assertions.

## Verification

The recent primary source was inspected at the ordered duality map, the discrete exponent transformation, the sign configurations, the identification of the sign data with Toda norming parameters, the positivity criterion for smooth real Baker--Akhiezer data, and the fully factored tau function.

The sign-count lemma was also checked independently over a finite grid of integer pairs as a sanity check, but the proof above is symbolic and covers all nonnegative integers. No finite enumeration is used to establish the theorem.

The fixed-locus algebra has no hidden divisibility assumption: equality with the ordered dual quadruple forces
\\[
A=P+B+Q,
\\]
and conversely that one equation makes all four transformed exponents equal to their originals.

The tau-zero multiplicity is exact, because at \\(x=0\\) only the factor \\((1-q^x)^A\\) vanishes in the source's complete product formula.

## Relationship to prior work

Van Diejen and Kirillov's recent paper gives the complete determinant/evaluation formula for this discrete four-parameter family, its duality transformation, the sign configurations of the reflectionless spectral data, and the tau-factorization. It does not state the ordered fixed locus, count the negative norming parameters there, or identify the resulting incompatibility between nontrivial fixed duality and the positive-norming chamber.

Earlier work of van Diejen and Kirillov develops inverse-scattering formulas for reflectionless Jacobi operators and special \\(q\\)-spherical-function subfamilies. That work supplies the spectral framework but predates the complete four-integer family used here.

General Askey--Wilson duality literature describes the dual parameter transformation and self-dual degenerations in the \\(q\\)-Askey scheme. The checked sources do not combine the fixed-locus algebra of this 2026 elementary family with its specialized Toda norming-sign data.

Targeted searches for ordered self-duality, fixed dual parameters, negative norming indices, and positive reflectionless Toda data did not locate an implication-equivalent statement.

## Limitations

The theorem classifies fixed points of the ordered duality map in the canonical parameter chamber. Because the Askey--Wilson function also has parameter permutations and Weyl-group reflection symmetries, a broader classification of parameters that are dual only up to those symmetries is not claimed.

The theorem identifies negative norming parameters and a real zero of the tau denominator. It does not claim that the Baker--Akhiezer numerator fails to cancel that zero for every spectral parameter.

No statement is made for generic continuous Askey--Wilson parameters outside the discrete elementary family.

## References

1. J. F. van Diejen and A. N. Kirillov, *Elementary Askey--Wilson Functions*, arXiv:2609.37390v1, 2026.
2. J. F. van Diejen and A. N. Kirillov, *Formulas for \\(q\\)-spherical functions using inverse scattering theory of reflectionless Jacobi operators*, Communications in Mathematical Physics 210 (2000), 335--369; Hokkaido University Preprint Series in Mathematics 430 (1998), DOI: 10.14943/83576.
3. T. H. Koornwinder, *Charting the \\(q\\)-Askey scheme. II. The \\(q\\)-Zhedanov scheme*, Indagationes Mathematicae 34 (2023), DOI: 10.1016/j.indag.2022.12.003.
