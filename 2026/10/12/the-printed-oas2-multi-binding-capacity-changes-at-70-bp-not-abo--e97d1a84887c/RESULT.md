# The printed OAS2 multi-binding capacity changes at 70 bp, not above 70 bp

## Finding

The OAS2 Model-M defines the maximum number of enzymes that can bind simultaneously to one dsRNA molecule by
\[
n(L)=\left\lfloor\frac{L}{2R_O}\right\rfloor,
\]
while Table 1 fixes
\[
2R_O=35\ {\rm bp}.
\]
For the seven measured lengths,
\[
L\in\{40,50,60,70,80,90,120\}\ {\rm bp},
\]
the formula therefore gives
\[
n(L)=(1,1,1,2,2,2,3).
\]
In particular,
\[
n(70)=2.
\]

The article nevertheless states that Model-M is taken with \(n=1\) for every length smaller than or equal to \(70\) bp and is therefore equivalent to Model-E there. Its model-selection table implements that override.

For Model-M with capacity \(n\), the kinetic parameters are
\[
(k_1,k_{1m}),\ldots,(k_n,k_{nm}),k_p,
\]
so there are \(2n+1\) free kinetic parameters. The article defines its AICc parameter count as the number of free model parameters plus one, hence
\[
K=2n+2.
\]
The printed floor rule requires the sequence
\[
K=(4,4,4,6,6,6,8).
\]
Table 2 instead reports
\[
K=(4,4,4,4,6,6,8).
\]
Thus the only measured length at which the implementation disagrees with the printed capacity law is \(70\) bp.

Under the printed law, the \(70\)-bp Model-M contains the state \(D_2\), parameters \(k_2\) and \(k_{2m}\), and the byproduct contribution \(2k_pD_2\). It is therefore not equivalent to Model-E. The published \(70\)-bp Model-M model-selection entry is an \(n=1\) calculation, not the \(n=2\) model specified by the displayed capacity formula.

## Assumptions and scope

The result concerns the mathematical model exactly as printed in the article. It uses the stated capacity law, the fixed OAS2 diameter, the seven measured dsRNA lengths, the Model-M reaction chain, the paper's definition of \(K\), and Table 2.

The calculation does not assert that two OAS2 enzymes biologically must fit on every \(70\)-bp dsRNA. The floor rule is itself a modelling assumption. The point is that the article simultaneously gives that assumption and a different boundary convention.

The experimental study underlying the data establishes a minimum dsRNA length of about \(35\) bp for OAS2 activation, but it does not by itself establish the Model-M occupancy rule. Thus the inconsistency is mathematical and source-specific rather than a claim of experimentally proven two-enzyme occupancy at \(70\) bp.

## Proof

The article fixes
\[
2R_O=35\ {\rm bp}
\]
and defines
\[
n(L)=\left\lfloor\frac{L}{2R_O}\right\rfloor.
\]
Substitution gives
\[
\left\lfloor\frac{40}{35}\right\rfloor
=
\left\lfloor\frac{50}{35}\right\rfloor
=
\left\lfloor\frac{60}{35}\right\rfloor
=1,
\]
\[
\left\lfloor\frac{70}{35}\right\rfloor
=
\left\lfloor\frac{80}{35}\right\rfloor
=
\left\lfloor\frac{90}{35}\right\rfloor
=2,
\]
and
\[
\left\lfloor\frac{120}{35}\right\rfloor=3.
\]

For capacity \(n\), equation (3.3) uses one association/dissociation pair
\[
(k_i,k_{im})
\]
for every
\[
i\in\{1,\ldots,n\},
\]
together with \(k_p\). Hence it contains \(2n+1\) free kinetic parameters. Equation (4.3) defines the AICc count \(K\) as the number of free model parameters plus one, so
\[
K=2n+2.
\]
Applying this to the formula-defined capacities gives
\[
(4,4,4,6,6,6,8).
\]

Table 2 reports Model-M counts
\[
(4,4,4,4,6,6,8).
\]
The sequences agree at \(40,50,60,80,90,\) and \(120\) bp and disagree only at \(70\) bp.

The discrepancy is also visible directly in the differential equations. When \(n=1\), equation (3.3) reduces to Model-E after relabelling \(D_1\) as \(D\). When \(n=2\), equation (3.3) includes the additional reversible transition
\[
D_1+E\rightleftharpoons D_2
\]
and the output equation contains
\[
k_p(D_1+2D_2).
\]
Thus the formula-defined \(70\)-bp Model-M cannot be equivalent to Model-E.

## Verification

The bundled `verify.py` evaluates the floor rule on all seven measured lengths and derives the AICc parameter counts from the Model-M parameter structure. It checks that the source table differs from the formula-derived sequence only at \(70\) bp.

It also checks that the source's displayed \(70\)-bp RSS, together with \(M=25\) and \(K=4\), gives an AICc within \(0.01\) of the published value \(61.98\). The residual difference is consistent with Table 2 displaying RSS only to one decimal place. This arithmetic replay is only a consistency check on which model was tabulated; it is not a refit of the missing \(n=2\) model.

## Relationship to prior work

Lee et al. define and calibrate the three OAS2 activation models considered here. Their full article gives the capacity formula, the \(35\)-bp diameter, the explicit \(n\leq3\) Model-M equations, the special statement that lengths at most \(70\) bp use \(n=1\), and Table 2.

Koul et al. provide the experimental OAS2 data and report that OAS2 activation has a minimum dsRNA-length requirement of about \(35\) bp. That experimental result motivates the length scale but does not state the multi-binding capacity law or resolve the \(70\)-bp boundary.

A same-titled 2020 master's thesis is cited by the article as a precursor. Its repository record was located, but direct full-text access was unavailable during this check, so no whole-document non-coverage claim is made about it. The accepted statement is restricted to the internally incompatible rules and table in the published article.

Targeted searches by DOI, title, \(70\)-bp boundary, floor-capacity rule, parameter count, correction, and erratum terminology did not locate a published correction of this boundary inconsistency.

## Limitations

The result does not determine which of the two boundary conventions is biologically preferable.

It does not reconstruct the unreported \(n=2\) fit at \(70\) bp and therefore does not claim what its RSS, AICc, Akaike weight, or model-selection ranking would be.

The global all-length Model-M fit uses a shared maximum parameter set and cannot be repaired merely by changing a single displayed \(K\) entry; a corrected global fit would require re-running the model with an unambiguous length-to-capacity rule.

## References

1. D. Lee, A. Koul, N. Lubna, S. A. McKenna, S. Portet, “Mathematical modelling of OAS2 activation by dsRNA and effects of dsRNA lengths,” AIMS Mathematics 6 (2021), 5924–5941. DOI: 10.3934/math.2021351.
2. A. Koul, S. Deo, E. P. Booy, G. L. Orriss, M. Genung, S. A. McKenna, “Impact of double-stranded RNA characteristics on the activation of human 2'-5'-oligoadenylate synthetase 2 (OAS2),” Biochemistry and Cell Biology 98 (2020), 70–82. DOI: 10.1139/bcb-2019-0060.
