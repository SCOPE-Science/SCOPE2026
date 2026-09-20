# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof is a direct specialization of Bao's explicit rank formula. For
\[
(A,B,C)=\bigl(16,\ 8u(9-u^2),\ -27(u^2-1)^2\bigr)
\]
one has
\[
B^2-4AC=64(u^2+3)^3,
\]
and, with \(D=\sqrt{-3}\),
\[
2\sqrt A\sqrt C-B=[2(u+D)]^3,
\qquad
-2\sqrt A\sqrt C-B=[2(u-D)]^3.
\]
These identities force the first two summand ranks to be \(1\) and \(2\). The remaining cube condition is equivalent to \(u^2-1=4r^3\), hence to a rational point on \(Y^2=X^3+16\). LMFDB 27.a4 records rank \(0\) and torsion \(\mathbb Z/3\mathbb Z\), leaving only \(u=\pm1\), exactly the excluded degenerate parameters. Exact symbolic checks reproduce all algebraic identities and the displayed sections. No numerical experiment is used as a substitute for the proof.

Potential failure modes were checked explicitly: \(A,C,B^2-4AC\) are nonzero for every rational \(u\ne\pm1\); the choice \(\sqrt C=3(u^2-1)\sqrt{-3}\) is valid for either sign of \(u^2-1\); and the cube-in-\(\mathbb Q(\omega)\) condition for a rational number is legitimately reduced to a rational cube, as proved in Bao's Proposition 3.6.

## Originality

Bao's current v1 states the full rank formula and proves rank at most three. In Section 6 it gives parametric maximal-rank examples with summand pattern \((1,1,1)\), whereas Example 6.4 gives a single numerical example for the pattern \((1,2,0)\), \((A,B,C)=(16,280,-972)\). No parametric \((1,2,0)\) family is stated there.

The surrounding literature identified in Bao and checked for scope includes Desjardins--Naskręcki (2024) and Kloosterman (2026), both treating the smaller two-coefficient family \(y^2=x^3+At^6+B\). Searches for the displayed coefficient family, its equivalent cubic identities, and a parametric rank-three \((1,2,0)\) construction did not identify prior coverage. The exact coefficient formulas do not appear in the current SCOPE archive either.

Originality is therefore assessed as PASS to the best of our knowledge, with an important residual risk: Bao's motivating preprint was submitted only on 14 September 2026, so unindexed contemporaneous follow-up work may exist. No inaccessible paper was identified whose title, abstract, or metadata specifically indicates this family or an equivalent \((1,2,0)\) parametrization.

## Value

The result converts a numerically isolated maximal-rank mechanism in the new complete rank classification into an explicit rational one-parameter family. The construction is also structurally transparent: two conjugate cube identities force the rank-two middle contribution, while the unwanted third contribution is ruled out globally by a rank-zero Mordell curve. This gives a reusable template for constructing or classifying other maximal-rank subfamilies inside Bao's parameter space.

## Scope and limitations

The result does not classify all maximal-rank triples, does not assert pairwise non-isomorphism for distinct parameters, and does not independently reprove Bao's rank formula or the LMFDB rank computation for 27.a4. The symbolic artifact checks the specialized algebra only.
