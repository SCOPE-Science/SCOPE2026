# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

The proof was checked at three levels.

First, the character-theoretic input from Monteiro--Stasinski is used only in the form they
state directly: the Steinberg square of \(\operatorname{GL}_n(q)\) contains every nonlinear
irreducible character trivial on the center. The proof here does not strengthen that input or
assume coverage of the missing linear characters.

Second, the cube-completion step is purely formal once one controls the abelianization.
For a center-trivial linear \(\lambda\), the twist
\(\lambda\operatorname{St}_n\) is a nonlinear center-trivial irreducible and hence occurs in
\(\operatorname{St}_n^2\); self-duality then puts \(\lambda\) in the cube. For a nonlinear
\(\chi\), if \(\chi\operatorname{St}_n\) had only linear constituents, its restriction to the
derived subgroup would be trivial. The identity
\(A\otimes B=I\) for invertible matrices forces both factors to be scalar. Since the relevant
abelian quotient is cyclic, scalar action on the derived subgroup would make the whole
Steinberg image abelian, impossible for a nonlinear irreducible representation.

Third, sharpness of exponent \(3\) when \(d=\gcd(n,q-1)>1\) was checked independently of the
cube argument. A nontrivial center-trivial determinant character \(\lambda\) exists.
Self-duality gives
\[
\langle\operatorname{St}_n^2,\lambda\rangle
=
\langle\operatorname{St}_n,\lambda\operatorname{St}_n\rangle.
\]
The twist is distinct from Steinberg because a suitable semisimple diagonal element has
nonzero Steinberg value but is changed by \(\lambda\). Hence the square misses \(\lambda\).
When \(d=1\), Monteiro--Stasinski identify their universal-square character with Steinberg;
the exceptional \(\operatorname{GL}_2(2)\cong S_3\) case also has the explicit square
\(1+\operatorname{sgn}+\operatorname{St}\).

No empirical computation is needed for the theorem.

## Originality

**PASS, to the best of our knowledge.**

Heide--Saxl--Tiep--Zalesski (2013) prove Steinberg-square universality for finite simple groups
of Lie type, with their stated unitary exceptions. Monteiro--Stasinski (arXiv:2609.17319v1)
extend the tensor-square problem to \(\operatorname{GL}_n(q)\): they show that the Steinberg
square contains all nonlinear center-trivial irreducibles, explicitly note that it is not
enough in general because linear characters can be missing, and construct a different
irreducible character whose square covers all center-trivial irreducibles.

The present result keeps the Steinberg character fixed and determines the exact tensor power
needed on \(\operatorname{PGL}_n(q)\): two when \(\gcd(n,q-1)=1\), three otherwise. Targeted
searches for Steinberg cube/third tensor power, Steinberg character covering number,
\(\operatorname{PGL}_n(q)\) Steinberg tensor powers, and cyclic-abelianization formulations
found the 2013 square theorem, recent tensor-product literature, and the 2026 source paper,
but no matching \(2/3\) formula or the stated completion lemma.

### Residual literature risk

The source preprint was submitted on 15 September 2026 and is still a very recent v1, so a
concurrent author revision or independent observation is a realistic risk. Character
covering numbers have older literature, and an equivalent short lemma could exist under
different terminology. No specific inaccessible paper was identified that appears likely to
contain this exact \(\operatorname{PGL}_n(q)\) covering-number formula. The originality claim
is therefore qualified to the best of our knowledge rather than exhaustive.

## Value

**PASS.**

The result gives a sharp answer for a canonical representation rather than replacing
Steinberg by a specially constructed character. It shows that the failure of the Steinberg
square in the non-simple adjoint case costs exactly one tensor factor and identifies the
precise arithmetic boundary \(\gcd(n,q-1)=1\). The abstract cyclic-abelianization lemma also
isolates a reusable mechanism: universal nonlinear coverage in a self-dual square upgrades
to full coverage in the cube.

The proof is short, but the conclusion is not a routine numerical parameter variation: it
turns the recent “all nonlinear constituents” theorem into an exact character-covering
number and explains why the missing linear sector is repaired uniformly in one step.

## Scope of the claim

No novelty is claimed for the 2013 Steinberg-square theorem, the
Monteiro--Stasinski nonlinear-coverage theorem, Steinberg self-duality, the standard
description of linear characters of \(\operatorname{GL}_n(q)\), or the semisimple-value
formula for the Steinberg character. The claimed contribution is the exact \(2/3\)
covering-number theorem and the cube-completion lemma used to obtain it.
