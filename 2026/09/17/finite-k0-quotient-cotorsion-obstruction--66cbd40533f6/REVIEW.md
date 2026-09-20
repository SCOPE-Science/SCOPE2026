# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The construction was checked at four separate mathematical levels.

First, the kernel of the finite \(K_0\)-quotient is extension closed because the
Euler class is additive on conflations. Complements of split monomorphisms and
kernels of split epimorphisms stay in the kernel, giving weak idempotent
completeness. Standard contractible cone conflations remain inside the
subcategory, proving the Frobenius property.

Second, semisimplicity gives a decomposition of every bounded complex into
cohomology stalks plus a contractible summand. Multiplication by the exponent
\(e\) of the finite image makes every truncated cohomology object admissible.
This proves exactly
\(\mathcal I=\langle\mathcal F\rangle\) and
\(\mathcal J=\langle\mathcal C\rangle\).

Third, the natural formula
\[
\operatorname{Ext}^1(X,Y)\cong
\bigoplus_n\operatorname{Hom}(H^nX,H^{n+1}Y)
\]
gives both ideal orthogonality and object orthogonality. Failure of either
morphism-vanishing condition is detected by an admissible stalk complex whose
cohomology object is repeated \(e\) times. The explicit cone constructions
produce a special \(\mathcal I\)-precover and special
\(\mathcal J\)-preenvelope for every object.

Fourth, the witnesses
\(S^0(R)\oplus S^1(R)\) and
\(S^1(R)\oplus S^2(R)\), for
\(\varphi([R])\ne0\), force any hypothetical special object approximation to
contain a truncation with Euler class \([R]\), contradicting membership in the
category. Every ambient complex is a summand of its \(e\)-fold direct sum, so
the stated idempotent-completion claim also follows.

The proof uses no empirical calculation.

## Originality

**PASS, to the best of our knowledge.**

Ren--Wang arXiv:2609.18681v1 supplies the modulus-two vector-space example and
identifies parity of truncated cohomology as the obstruction. The present
result replaces that one parity condition by an arbitrary nonzero finite
quotient of \(K_0(\mathcal S)\), shows that the same phenomenon works for every
Hom-finite semisimple finite-length base category, and identifies the signed
Euler class as the extension-stable invariant. In particular, it yields a
family for every modulus \(m\ge2\), with the \(m=2\) case recovering the source
example.

Targeted searches for finite-Grothendieck-quotient, congruence-mod-\(m\), Euler
class, and dense-subcategory formulations of the object-ideal cotorsion
counterexample found the Ren--Wang paper and general cotorsion/dense-subcategory
literature, but no matching finite-quotient theorem.

The use of Grothendieck-group kernels to define dense subcategories is classical:
Thomason's triangulated classification and Matsui's exact-category work are
relevant background. No novelty is claimed for that mechanism by itself.
Sun--Wang--Zhu and Zhang--Zhou provide positive comparison theorems under
additional assumptions; the construction here does not contradict those
results.

### Residual literature risk

The Ren--Wang paper is a very recent v1 preprint, so a concurrent revision or
independent generalization is a realistic risk. Dense-subcategory/K-theoretic
literature is broad, and an equivalent formulation not using cotorsion
terminology cannot be completely excluded. No specific inaccessible source was
found that appears likely to contain the full ideal-cotorsion construction.
The originality conclusion is not a claim of exhaustive literature coverage.

## Value

**PASS.**

The result changes the interpretation of the motivating example from a
modulus-two accident into a structural \(K_0\)-quotient mechanism. It explains
why parity can be expressed using unsigned total cohomology dimension, why that
formulation does not naively extend to higher moduli, and gives the correct
extension-stable replacement by the signed Euler class. The theorem also
produces simultaneous congruence obstructions whenever the semisimple base has
higher-rank \(K_0\), while retaining explicit complete ideal approximations.

## Scope of the claim

No novelty is claimed for ideal cotorsion theory, the Ren--Wang parity example,
the standard Frobenius structure on bounded complexes, the homotopy-category
Ext formula, or the classical classification/construction of dense
subcategories from Grothendieck groups. The claimed contribution is the finite
\(K_0\)-quotient theorem and its explicit cotorsion consequences.
