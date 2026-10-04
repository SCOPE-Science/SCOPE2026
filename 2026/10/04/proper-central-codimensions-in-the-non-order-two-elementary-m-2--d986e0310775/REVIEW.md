# Review: Proper central codimensions in the non-order-two elementary \(M_2\) branch

## Correctness
**PASS.** The proof reconstructs the relevant quotient dimensions from the linearly independent normal forms in arXiv:2609.20488v1, Remark 4.7, and then applies the complete central-polynomial classification in Theorems 4.11 and 4.12. The proper-central count separates the no-off-degree even-parity classes from balanced positive off-degree classes. The coefficient identity
\[
[x^0](2+x+x^{-1})^n=\binom{2n}{n}
\]
is exact, and the total-codimension simplification similarly uses
\[
[x^1](2+x+x^{-1})^n=\binom{2n}{n-1}.
\]
No finite computation is used as an infinite proof. The assumptions \(\operatorname{char}F=0\), finite abelian \(G\), \(g^2\ne1\), and \(*\in\{\gamma_2,\gamma_3\}\) are maintained throughout.

## Originality
**PASS, with residual literature risk.** The 2026 source explicitly says that exact central and proper central codimensions are computed for the Klein-group grading; in the non-order-two elementary branch it gives total asymptotics, normal forms, and a central-polynomial theorem but does not state the formula \(\binom{2n}{n}-2^{n-1}\) or the shift \(c_n^{(G,*),\delta}=c_{n-1}^{(G,*)}\). The companion transpose-superinvolution paper gives an exact total codimension formula and central generators, but the inspected text does not state this proper-central sequence. Targeted searches for the formula, the shift, and equivalent formulations found no covering result. The closest related record treats the order-two elementary grading and square classes, not this branch. A residual risk remains that older central-polynomial literature encodes the same count implicitly without presenting it as a codimension theorem.

## Value
**PASS.** Proper central codimensions are a standard quantitative invariant, and recent work specifically studies their exponential growth. The result gives the exact finite-rank sequence in a branch where the motivating paper stops at total asymptotics and central generators. The exact one-step shift is structurally stronger than merely recovering the exponent \(4\): it immediately yields the asymptotic \(1/4\) proper-central proportion and a closed formula at every degree.

## Closest literature and limitations
The closest primary sources are arXiv:2609.20488v1 and arXiv:2609.20458v1. The general exponent context is D. La Mattina, R. B. dos Santos and A. C. Vieira, DOI 10.1007/s00209-025-03689-8. The theorem is limited to the non-order-two elementary grading branch in characteristic zero, and originality remains subject to the possibility of an older implicit equivalent count.

Same-model review: passed. Independent audit: not yet performed.
