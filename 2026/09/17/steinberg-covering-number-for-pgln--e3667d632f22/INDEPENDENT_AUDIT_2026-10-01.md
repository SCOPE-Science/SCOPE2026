# Independent audit — SCOPE-20260917-e3667d632f22

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

For the Steinberg character of PGL_n(q), the character covering number is exactly two when gcd(n,q-1)=1 and exactly three otherwise; more generally, a nonlinear self-dual irreducible of a finite group with cyclic abelianization whose square contains every nonlinear irreducible has a cube containing every irreducible.

## Correctness

**PASS** — The completion lemma was reconstructed from character inner products. Linear targets enter the cube because their twists of the self-dual nonlinear character occur in the square. For a nonlinear target, if its tensor product with the character had only linear constituents, the tensor representation would be trivial on the derived subgroup; the elementary identity A tensor B equals identity forces both factors scalar there, and cyclic abelianization would make the irreducible image abelian, contradicting nonlinear irreducibility. For GL_n(q), nontrivial center-trivial determinant twists exist exactly when gcd(n,q-1)>1 and are absent from the Steinberg square, while the cited recent theorem supplies every nonlinear center-trivial constituent. These facts give the sharp two-or-three formula.

## Originality

**PASS** — The exact two-or-three covering-number formula and the general cyclic-abelianization cube-completion lemma were not found in the older Steinberg-square literature or the recent GL_n(q) tensor-square paper. The recent paper supplies the nonlinear square coverage and notes the linear-character obstruction; the extra factor and its sharpness are the new implication checked here.

### Equivalent formulations

The searched aliases include tensor covering exponent, third tensor power, Steinberg cube, and projective general linear formulation. Evidence: Published-results search returned this record as the exact match; a later 2026-09-18 record explicitly describes itself as an alternate derivation of the 2026-09-17 theorem. No earlier exact two-or-three covering-number formulation was located.

### Broader coverage

Neither source dominates the final PGL_n(q) two-or-three classification. Evidence: The 2013 result covers simple groups of Lie type via Steinberg squares, which corresponds to the projective-special-linear/simple regime rather than the full PGL_n(q) linear-character defect. The 2026 paper supplies nonlinear center-trivial constituents in the Steinberg square and constructs another character with a universal square, but it does not state the exact Steinberg covering number found here.

### Exact database or table

The relevant exact-object check is theorem coverage rather than a database lookup; semantic searches were used to detect equivalent formulas. Evidence: No finite table is required because the claim is uniform in n and q.

### Claim versus prior implication

The final claim is a short but nontrivial consequence of the recent square theorem plus a separately proved completion lemma, not a mere parameter substitution. Evidence: The recent nonlinear-coverage theorem plus self-duality does imply the linear-target part of the cube argument, but it does not by itself state or prove that every nonlinear target lies in the cube; the cyclic-abelianization argument supplies that completion. The nontrivial determinant twist proves that the square genuinely fails when gcd(n,q-1)>1.

## Value

**PASS** — The claim determines the exact covering exponent of a canonical representation and isolates a reusable completion mechanism for cyclic abelianization. It turns the recently identified square defect into a sharp structural statement rather than merely another decomposition example.

## Sources inspected

- A tensor square theorem for characters of GL_n(q) — https://arxiv.org/abs/2609.17319. SUPPORTS the nonlinear-coverage input; very recent source remains a revision risk: The source extends Steinberg-square coverage in GL_n(q), separates the center-trivial linear issue, and constructs a universal-square character.
- Conjugacy action, induced representations and the Steinberg square for simple groups of Lie type — https://arxiv.org/abs/1209.1768. NOT_COVERING the non-simple PGL_n(q) defect classification: It establishes Steinberg-square universality for finite simple Lie-type groups subject to stated exceptions.

## Residual risks and limitations

- The key GL_n(q) paper is an extremely recent first-version preprint, so revisions or concurrent observations may affect priority.
- An older character-covering paper using different terminology could contain the cyclic-abelianization completion lemma.
- The theorem depends on the recent nonlinear center-trivial Steinberg-square input; the completion and sharpness arguments were independently reconstructed.
- Originality is best-of-knowledge because of the very recent source and possible concurrent work.

## Disposition

**PASSED**
