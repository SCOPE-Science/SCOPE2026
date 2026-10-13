# Review of Sharp Kesten–Stigum gap on the large \(k=3\) hardcore-SOS branch

## Correctness — PASS
The domain is explicit: \(0<\theta<1\), \(k=3\), hinge admissibility, \(x=1\), and the large root \(y_1>2^{1/4}\). The source boundary-law identity gives \(\theta=(y^3-y)/(y^4-2)\). Setting \(r=y^2\) yields the exact factorization
\[
\theta y^3-2=\frac{(r-2)^2(r+1)}{r^2-2}\ge0.
\]
The transition-eigenvalue ordering is rederived rather than assumed: after clearing positive denominators, both inequalities \(\lambda_2-\lambda_1\ge0\) and \(\lambda_2+\lambda_1\ge0\) reduce to manifestly positive expressions for \(0<\theta<1\). Therefore \(\lambda=\lambda_2\le1/3\), and the sharp Kesten–Stigum margin follows. Equality is checked exactly at \(y=\sqrt2\), \(\theta=1/\sqrt2\). Risk: none to the stated algebraic conclusion; the result must not be read as an extremality theorem.

## Originality — PASS
The motivating full text states only the sufficient subregion \(\theta>(\sqrt3-1)/8^{1/4}\approx0.435\) where the large branch fails Kesten–Stigum, and then says stronger extremality analysis is challenging. Exact-phrase, identifier, branch, and formula searches found no published statement of the all-\(\theta\) sharp bound. A later hard-core-SOS extremality paper was inspected because of its close title; it treats the wand admissibility graph and explicitly contrasts its boundary-law equation with the hinge graph. The closest earlier three-state SOS extremality paper treats a different SOS interaction on a binary tree. Risk: an equivalent short calculation could exist in weakly indexed notes or under different branch notation, but no implication-equivalent source was found.

## Value — PASS
The source devotes a section to Kesten–Stigum regions and leaves the \(k=3\) large branch controlled only for \(\theta\gtrsim0.435\). The sharp bound closes that entire unresolved parameter interval for the source's own non-extremality test and identifies its exact best-case margin and maximizer. This is a natural branch-level reconstruction invariant, not an arbitrary parameter slice. Its value is limited but substantive: it narrows future extremality work by proving that Kesten–Stigum cannot decide this branch anywhere in \(0<\theta<1\).

## Closest literature and limitations
The closest source is Jahnel–Rozikov, arXiv:2404.03297, whose equations and partial large-branch estimate are the starting point. Khakimov–Makhammadaliev–Rozikov, arXiv:2412.05963, concerns the wand graph rather than the hinge graph. Külske–Rozikov (2015) concerns a different three-state SOS model on the binary tree. The present result does not establish extremality, reconstruction, or any statement outside its stated branch.

Self-review: passed. Independent audit: not yet performed.
