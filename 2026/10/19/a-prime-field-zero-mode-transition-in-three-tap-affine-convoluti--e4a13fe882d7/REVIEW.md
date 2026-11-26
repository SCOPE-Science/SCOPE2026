# Independent mathematical audit

## correctness

PASS

PASS applies to /workspace/repairs/3/RESULT.md. The frozen determinant and nullity theorem is correct under q≥3; its literal ‘every prime’ mod-3 corollary includes p=2, where the group has only two elements and no such three distinct taps exist. The repair qualifies the corollary by oddness and keeps the full determinant scope. Independently, conjugation by a translation changes c to c+(1−a)t and eliminates it. In a regular-module basis f_{u,t}(s,v)=δ_{u,s}ψ(tv), the translation gives the entry ψ(−bt) and the multiplier sends (u,t) to (au,t/a), so ut is invariant. Its zero block is 2I plus a (q−1)-cycle; each nonzero block is a cycle plus a diagonal running over all nonzero frequencies. Only the identity and the full cycle contribute to a block determinant. The ordinary additive character takes each pth root p^{r−1} times on the field, with one identity occurrence removed in the nonzero block. The product of the nonidentity odd-p factors 1+ζ^j is 1, giving 2^{p^{r−1}−1}−1 after the cycle term. In characteristic two a diagonal factor is zero but the cycle contribution is +1. The zero block gives 2^{q−1}−(−1)^{q−1}. In the singular odd prime case the diagonal is nonzero and one starting component determines any kernel vector, so each of q−1 nonzero blocks contributes one dimension. The repaired mod-3 infinitude follows by the 3P−1 argument and removal of the single prime 2. An independent exact regular-matrix replay with b=c=1 found (det,nullity)=(0,2),(9,0),(0,4),(1673055,0) at q=3,4,5,9 respectively; script /workspace/branches/e083a720-c726-42f4-8c37-e58c7b131d5f/independent_affine_check.py. The uploaded modular/finite checks were read, not run; neither finite replay proves the field-uniform claim.

## originality

PASS

For the repaired finding the distinct content is the exact determinant throughout the prime-power family, including full-multiplier extension-field invertibility and the characteristic dependence. The prime-field singularity/nullity for p≥5 is explicitly credited as covered by a distinct indexed theorem, not claimed as novel by itself. The general block method is standard. No examined statement supplies the prime-power exact factor or the prime-versus-extension transition; the strongest narrower indexed result uses the analogous cyclotomic blocks, an acknowledged methodological overlap rather than coverage of extension fields.

## value

PASS

For this canonical, generating identity-translation-dilation support, determining exactly when a zero mode occurs, how many survive and the integer determinant in extension fields is a natural structural invariant. The dependence on the extension degree, and separately on characteristic two, resolves an actual boundary that the prime-field theorem does not address. The odd mod-3 corollary illustrates the prime regime without claiming a universal three-tap classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
