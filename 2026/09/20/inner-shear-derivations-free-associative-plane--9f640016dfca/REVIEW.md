# Scientific review

## Correctness: PASS

The main statements admit direct checks once two classical facts about the free associative plane are used.

For the kernel, grade by the number of occurrences of x. The term delta_f lowers x-degree and the commutator with g(y) preserves it. Hence the top x-degree component of a D_{f,g}-constant centralizes g(y). For nonconstant g, Bergman's centralizer theorem gives a polynomial centralizer; because y itself centralizes g(y), that centralizer must be k[y]. A nonzero component of positive x-degree is therefore impossible, proving ker D_{f,g}=k[y].

For local nilpotence, delta_f commutes with -ad_{g(y)}. For n>=2 the f-term disappears from the iterates of x and
D^n(x)=sum_i (-1)^i binom(n,i) g(y)^i x g(y)^(n-i).
When g is nonconstant, the highest-degree terms are distinct free words, so no iterate vanishes; their degrees also grow strictly, excluding local finiteness. When g is scalar, the commutator term vanishes and repeated application of delta_f lowers x-degree, so the derivation is locally nilpotent.

For isotropy, a commuting automorphism preserves ker D=k[y], so y must map to ay+b. The Czerniakiewicz--Makar-Limanov identification of the automorphism groups of k<x,y> and k[x,y], together with the polynomial Jacobian, forces x to map to cx+h(y). Substitution into rho D=D rho yields independently
f(ay+b)=c f(y)
and
[x,g(ay+b)-g(y)]=0.
The latter is equivalent to g(ay+b)-g(y) being scalar. Conversely these identities directly imply commutation. No extra hypothesis on f is used.

The residual affine-symmetry formula was also checked coefficientwise after translating g so that its degree-(d-1) coefficient vanishes. For d>=2, the leading coefficient first forces a^d=1, the next coefficient forces the affine symmetry to fix the translated center, and the remaining positive-degree coefficients give a^j=1 on the support of the centered polynomial. The gcd formula follows. The f-condition is then exactly equality of the characters a^j on the support of the centered f.

The source examples are recovered at (f,g)=(0,y) and (1,y), and abelianization gives f(y) partial_x as stated.

## Originality: PASS, qualified to the best of our knowledge

Baltazar--Lopes--Morales, arXiv:2609.19470v1, was inspected in the relevant full-text section. Its Proposition 27 treats D(x)=[x,y], D(y)=0 and its Proposition 29 treats D(x)=1+[x,y], D(y)=0. The paper proves the unbounded shear isotropy for those examples and discusses abelianization, but it does not state the family D(x)=f(y)+[x,g(y)], its exact kernel, the sharp condition g in k for local nilpotence, or the full isotropy formula.

Targeted searches were made for the same family and equivalent descriptions using free-associative derivations, inner perturbations, triangular derivations, centralizers, commuting automorphisms, and isotropy groups. No matching theorem was located. Bergman's centralizer theorem is prior art and is used only to identify C_F(g(y))=k[y]. The classical free-plane automorphism theorem and the triangulability of locally nilpotent derivations are also prior art and are not claimed as new.

Crode--Shestakov, DOI 10.1080/00927872.2020.1729363, is close background because it classifies locally nilpotent derivations of the free associative plane and gives another proof of the automorphism-group correspondence. Its published abstract and bibliographic description were inspected, but the full article was not exhaustively checked here. Since the new family is non-locally-nilpotent for nonconstant g, that paper is not strong evidence of coverage, but it remains a plausible source of adjacent lemmas. Drensky--Makar-Limanov, DOI 10.3842/SIGMA.2019.091, concerns locally nilpotent derivations and their kernels; it is likewise adjacent rather than a located source for the non-locally-nilpotent isotropy classification.

The principal residual originality risk is older free-associative derivation or automorphism literature using different notation for a triangular derivation plus a commuting inner derivation. The proof becomes short after this mechanism is identified, so concurrent or unindexed equivalent coverage cannot be excluded. Originality is therefore claimed only for the exact family classification and residual affine-symmetry description, to the best of our knowledge.

## Value: PASS

The result turns two isolated counterexamples from the 2026 source into a complete and explicit mechanism. It shows that a commuting inner perturbation by a nonconstant polynomial in the kernel variable simultaneously forces ker D=k[y], destroys both local nilpotence and local finiteness, and leaves an infinite-dimensional shear subgroup untouched. The full isotropy group is computed rather than merely shown to have unbounded degree, and the finite residual affine symmetry is reduced to support gcds of centered polynomials. This sharply separates the source of unbounded isotropy from local nilpotence in the free associative plane.

Same-model review: passed. Independent audit: not yet performed.
