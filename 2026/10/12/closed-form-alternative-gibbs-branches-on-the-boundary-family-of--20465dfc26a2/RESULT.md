# Closed-form alternative Gibbs branches on the boundary family of the wand hard-core model

## Finding

Consider the fertile three-state hard-core model in the wand case on a Cayley tree of even order \(k\ge4\). On the invariant set \(I_3\) for alternative boundary laws, take the natural boundary value
\[
m=\frac{k}{2}+1,
\]
so that \(2m-k=2\). The source proves general existence conditions for alternative Gibbs measures and then analyzes the special instance \(k=4,m=3\). For the whole even-order boundary family, the positive solutions admit a complete closed form.

For \(0<\lambda\le1\), the \(I_3\) equations have only the translation-invariant positive solution. For \(\lambda>1\), there are exactly two additional positive solutions. Define
\[
s=\lambda^{{2/k}},\qquad
u=\frac{{s+\sqrt{{s^2+8s}}}}2,
\]
and
\[
z_\pm=\frac{{u\pm\sqrt{{u^2-4}}}}2.
\]
Then \(z_+>1>z_->0\), \(z_+z_-=1\), and the two non-translation-invariant solutions are precisely
\[
(z_+,z_-),\qquad (z_-,z_+).
\]
In particular, the critical activity is
\[
\lambda_c=1
\]
for every even \(k\ge4\) in this family.

## Assumptions and scope

The activity is \(\lambda>0\). The tree order \(k\) is even and at least four, and \(m=k/2+1\). The statement concerns the source's invariant set \(I_3\) for alternative boundary laws in the fertile three-state wand model. It does not classify solutions on other invariant sets, arbitrary boundary laws, periodic measures, extremality, or thermodynamic stability.

The source's boundary-law correspondence is used to interpret positive solutions as Gibbs measures. Its symmetric solution is the unique translation-invariant solution in this sector.

## Proof

On \(I_3\), the source equations are
\[
z_1=\lambda\left(\frac{{1+z_1}}{{z_1+z_2}}\right)^m
\left(\frac{{1+z_2}}{{z_1+z_2}}\right)^{{k-m}},
\]
\[
z_2=\lambda\left(\frac{{1+z_2}}{{z_1+z_2}}\right)^m
\left(\frac{{1+z_1}}{{z_1+z_2}}\right)^{{k-m}}.
\]
Dividing them gives
\[
z_1(1+z_1)^{{k-2m}}=z_2(1+z_2)^{{k-2m}}.
\]
For \(2m-k=2\), this is
\[
\frac{{z_1}}{{(1+z_1)^2}}=\frac{{z_2}}{{(1+z_2)^2}},
\]
which factors exactly as
\[
(z_1-z_2)(1-z_1z_2)=0.
\]
Thus every non-translation-invariant positive solution satisfies \(z_1z_2=1\).

Write \(z_1=z>0\) and \(z_2=z^{-1}\). Substitution into the first boundary-law equation gives
\[
\lambda=\frac{{(z^2+1)^k}}{{z^{{k/2}}(z+1)^k}}.
\]
Set
\[
u=z+z^{-1}\ge2.
\]
Because \(z^2+1=zu\) and \((z+1)^2=z(u+2)\), the branch equation becomes
\[
\lambda=\frac{{u^k}}{{(u+2)^{{k/2}}}}.
\]
Taking the positive \(2/k\)-th power yields
\[
s:=\lambda^{{2/k}}=\frac{{u^2}}{{u+2}}.
\]
The function \(u\mapsto u^2/(u+2)\) is strictly increasing for \(u\ge2\), since
\[
\frac{{d}}{{du}}\frac{{u^2}}{{u+2}}=\frac{{u(u+4)}}{{(u+2)^2}}>0,
\]
and its value at \(u=2\) is \(1\). Hence there is no non-symmetric positive solution for \(0<\lambda<1\), the branches coalesce at \(\lambda=1\), and for every \(\lambda>1\) there is exactly one \(u>2\).

Solving \(u^2=s(u+2)\) gives
\[
u=\frac{{s+\sqrt{{s^2+8s}}}}2,
\]
the other quadratic root being negative. Finally, solving \(z+z^{-1}=u\) gives exactly
\[
z_\pm=\frac{{u\pm\sqrt{{u^2-4}}}}2.
\]
These are positive, reciprocal, and distinct for \(u>2\). Therefore the two ordered non-translation-invariant solutions are exactly the two stated permutations. Together with the unique symmetric solution, this proves the complete \(I_3\) count.

## Verification

The bundled verifier substitutes rational reciprocal pairs into the source equations exactly for multiple even orders, checks the reduced activity identity without floating-point arithmetic, and separately checks the explicit radical reconstruction numerically for representative activities. These finite checks corroborate the algebra; the all-order conclusion follows from the proof above.

## Relationship to prior work

Khakimov, Makhammadaliev and Umirzakova introduce the alternative Gibbs construction and derive the \(I_3\) system. Their Theorem 3.2 identifies the general parameter region in which non-translation-invariant alternative measures can occur; for \(2m-k=2\) they note the reciprocal condition \(z_1z_2=1\). They then specialize to \(k=4,m=3\), derive the one-versus-three classification with critical activity \(1\), and write its scalar activity function. The result here closes the entire natural boundary family \(2m=k+2\) for all even \(k\ge4\), proving that the same threshold persists and giving explicit branches in radicals.

A 2025 paper with the closely related title “Alternative Gibbs measures for hard-core model in the case wand: existence, criticality, and iteration dynamics” is bibliographically visible and concerns new arbitrary-order existence conditions, but its full text was not accessible in the checked sources. Exact-form searches did not reveal the displayed all-even-order classification or radical formula there. This remains the principal literature risk.

## Limitations

The claim is restricted to \(I_3\) and to the boundary family \(m=k/2+1\). It does not assert that these exhaust all alternative Gibbs measures of the model. The later 2025 same-object article could contain an equivalent result under different notation; only its bibliographic summary and searchable metadata were available for comparison.

## References

1. R. Khakimov, M. Makhammadaliev, K. Umirzakova, “Alternative Gibbs measure for fertile three-state Hard-Core models on a Cayley tree,” arXiv:2401.08706v1, first public 2024-01-15; *Phase Transitions* 97 (2024), 536–556, DOI:10.1080/01411594.2024.2373783.
2. “Alternative Gibbs measures for hard-core model in the case wand: existence, criticality, and iteration dynamics,” *Bulletin of the Institute of Mathematics* 8(6) (2025), 13–23; bibliographic summary inspected, full text unavailable in the checked sources.
