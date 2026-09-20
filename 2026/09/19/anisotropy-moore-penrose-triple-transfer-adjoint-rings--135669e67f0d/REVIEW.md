# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The central implication was checked in both directions. If the underlying
Hermitian or skew-Hermitian form is anisotropic, every subspace is nondegenerate.
For an arbitrary endomorphism \(T\), orthogonal decompositions of
\(\ker T\) and \(\operatorname{im}T\) therefore give an explicit Moore–Penrose
inverse by inverting \(T\) on \((\ker T)^\perp\) and setting the inverse to zero
on \((\operatorname{im}T)^\perp\). Hence every element is Moore–Penrose
invertible.

If the form is isotropic, the rank-one construction in `RESULT.md` gives
endomorphisms \(A,B,C\) with \(ABC=0\) but \(ACB=\theta_{u,y}\), whose image is
an isotropic line. Were \(\theta_{u,y}\) Moore–Penrose invertible, the
self-adjoint idempotent \(TT^\dagger\) would have that isotropic line as its
image. Images of self-adjoint idempotents are nondegenerate, a contradiction.
This establishes failure of Condition (3). Since Condition (4) always implies
Condition (3), the two conditions are equivalent in the stated class.

The finite-field specialization was checked independently from the standard
isotropy criterion for \(x_1^2+\cdots+x_n^2\). In particular, the displayed
\(M_2(\mathbb F_5)\) witness satisfies \(ABC=0\), \(ACB=A\), and \(A\) has
isotropic image.

## Originality

PASS, to the best of our knowledge.

Chen--Wang--Zou, arXiv:2609.20084v1, was inspected in full through its HTML
version. Section 4 defines Condition (3),
\[
abc=0\Rightarrow acb\in R^\dagger,
\]
and Condition (4),
\[
abc\in R^\dagger\Rightarrow acb\in R^\dagger,
\]
proves \((1)\Rightarrow(4)\Rightarrow(3)\), and explicitly asks in Question 4.3
whether (3) implies (4). The paper gives \(M_2(\mathbb C)\) with conjugate
transpose as a \(*\)-regular example where both conditions hold, but it does not
state an anisotropy criterion for adjoint matrix rings.

Classical \(*\)-regular-ring theory already identifies proper involutions on
regular rings with the setting in which every element has a Moore–Penrose
inverse; that fact is prior art and is not claimed. Pearl (1968) is prior art on
generalized inverses over arbitrary fields. Huylebrouck--Puystjens--Van Geel
(1988) specifically treats Moore–Penrose inverses of matrices over semisimple
Artinian rings with involution. Targeted searches did not locate the present
transposed-triple equivalence, the isotropic rank-one obstruction, or the stated
finite-field classification.

The full texts of Pearl (1968) and Huylebrouck--Puystjens--Van Geel (1988) were
not independently inspected. The latter is the strongest residual originality
risk because its title and abstract directly concern arbitrary involutions on
finite matrix rings. No concrete evidence of the transposed-triple result was
found, but this access limitation remains material.

The originality claim is restricted to the bridge from Chen--Wang--Zou's
Conditions (3) and (4) to anisotropy in adjoint endomorphism rings, not to
\(*\)-regularity, adjoint involutions, Hermitian-form theory, or general
Moore–Penrose criteria.

## Value

PASS.

The result gives a substantial partial answer to an explicit open question in a
new preprint for a canonical and broad family of simple Artinian \(*\)-rings.
It also identifies a sharp structural boundary rather than merely producing
examples: anisotropy is exactly the condition under which both transposed-triple
properties hold.

For ordinary transpose over finite fields, the criterion becomes an elementary
complete classification. The explicit rank-one witness on the isotropic side
makes failure transparent and reusable.

## Limitations

The result does not settle Question 4.3 for arbitrary \(*\)-rings. It addresses
adjoint involutions on finite-dimensional endomorphism rings.

The two older generalized-inverse papers identified above were not both
available for full-text inspection and remain the principal prior-art
uncertainty. No independent validation is asserted.
