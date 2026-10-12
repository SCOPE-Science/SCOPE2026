# Self-review

## Correctness
PASS. On the affine chart \(z=1\), both generators are triangular translations fixing \(y\), so composition and inversion add their translation polynomials exactly. The resulting coefficient pair is \((a,b)=(m+n,n)\), which is zero only at \((m,n)=(0,0)\) in characteristic zero. The \(a=0\), \(b\ne0\) branch is genuinely quadratic. For \(a\ne0\), the displayed diagonal coordinate changes reduce the quartic to one of the two extremal normal forms. The source proves projective-equivalence invariance of quadratic length and quadratic length \(5\) for both normal forms. The checker replays all new coefficient identities and branch conditions.

## Originality
PASS. The initiating paper was inspected in full at the definitions, main theorem, normal forms, decomposition, and lower-bound proof; its text contains no relevant discussion of subgroups, iterates, or powers. Targeted searches for the exact normal forms together with powers/subgroups and for quadratic-length subgroup spectra returned the initiating paper, a 2020 thesis on low-degree quadratic length, and literature on the different Jonquières length, but no statement implying the exact \(\{0,1,5\}\) spectrum. A published-finding search likewise found no covering result; the closest finite-field quartic Cremona result concerns explicit maps over \(\mathbf F_4\), not quadratic length on this characteristic-zero subgroup.

## Value
PASS. The two generators are not arbitrary examples: they are exactly the two equivalence classes singled out by the new classification as extremizers of quadratic length among quartic de Jonquières maps. Computing the invariant on their entire generated subgroup shows a structural phenomenon invisible in the one-map classification: an infinite rank-two abelian subgroup has uniformly bounded quadratic length, with a complete sharp spectrum and a full cancellation diagonal of quadratic elements. This is a natural subgroup-level test of the new invariant rather than a parameter substitution.

## Closest literature and limitations
Blanc--Furter study iteration and dynamical behavior for the distinct Jonquières-factor length, which motivates but does not imply the present quadratic-length calculation. Nguyen's thesis gives low-degree classifications and de Jonquières bounds; only its public abstract was used for the originality comparison. A residual risk remains that an unindexed long-form source contains the same elementary subgroup observation. The claim is restricted to algebraically closed characteristic zero.

Self-review: passed. Independent audit: not yet performed.
