# Harder–Narasimhan filtration of complete hyperelliptic curves in projective four-space

## Finding
Let \(C\) be any smooth complex hyperelliptic curve of genus \(g\geq3\), let \(\pi:C\to\mathbb P^1\) be its hyperelliptic morphism and \(A=\pi^*\mathcal O_{\mathbb P^1}(1)\). For a general line bundle \(L\in\operatorname{Pic}^{g+4}(C)\), the complete linear series embeds \(C\) in \(\mathbb P^4\). Its normal bundle \(N=N_{C/\mathbb P^4}\) has the complete Harder–Narasimhan filtration
\[
0\subset E_1\subset E_2\subset N,
\qquad
E_1\cong L^2A^{g-2},\quad
E_2/E_1\cong L^2A^{-1},\quad
N/E_2\cong LA^2.
\]
Every successive quotient is a line bundle and its degree is, in descending order,
\[
\boxed{\left(4g+4,\;2g+6,\;g+8\right)}.
\]
In particular, \(E_1\) is the **unique maximal destabilizing subbundle**, and the middle HN step is a canonical rank-two subbundle defined using the cubic-scroll normal sequence.

## Assumptions and scope
The ground field is \(\mathbb C\); \(g\) ranges over all integers at least three. The curve \(C\) is arbitrary smooth hyperelliptic and \(L\) lies in the nonempty Zariski-open subset of \(\operatorname{Pic}^{g+4}(C)\) for which \(\pi_*L\cong\mathcal O(1)\oplus\mathcal O(2)\). On that locus the map defined by the complete series is an embedding and \(h^0(C,L)=5\). Tensor products of line bundles are abbreviated by juxtaposition, so \(L^2A^{-1}\) means \(L^{\otimes2}\otimes A^{\otimes(-1)}\). A Harder–Narasimhan filtration is the unique filtration by saturated subbundles with semistable quotients of strictly decreasing slopes.

## Proof
**The cubic scroll and the first step.** The balanced direct image \(\pi_*L\cong\mathcal O(1)\oplus\mathcal O(2)\) gives the smooth cubic rational normal scroll \(S=\mathbb P(\pi_*L)\subset\mathbb P^4\). Write \(H\) for its hyperplane divisor and \(f\) for a ruling fiber. Then \(H^2=3\), \(Hf=1\), \(f^2=0\), and, by the two points in each hyperelliptic fiber and by \(\deg L=g+4\),
\[
C\sim2H+(g-2)f.
\]
The regular embeddings \(C\subset S\subset\mathbb P^4\) give an exact normal sequence
\[
0\longrightarrow N_{C/S}\longrightarrow N\longrightarrow N_{S/\mathbb P^4}|_C\longrightarrow0.
\]
Here \(N_{C/S}=\mathcal O_C(C)\cong L^2A^{g-2}\), of degree \(4g+4\). Define \(E_1=N_{C/S}\).

**A low-dimensional scroll quotient, including the range outside the existing large-rank lemma.** For the cubic scroll the normal bundle itself has the standard locally free resolution
\[
0\longrightarrow\mathcal O_S(2f)\longrightarrow
\mathcal O_S(H+f)^{\oplus3}\longrightarrow N_{S/\mathbb P^4}\longrightarrow0.
\]
For completeness, this follows by comparing the relative Euler sequence of \(S=\mathbb P(\mathcal O(1)\oplus\mathcal O(2))\) with the ambient Euler sequence and quotienting by the pullback of \(T_{\mathbb P^1}\cong\mathcal O(2)\). Restrict the sequence to \(C\) and tensor by \((LA)^{-1}\). Since all terms are vector bundles the restriction stays exact, giving
\[
0\longrightarrow D^{-1}\longrightarrow\mathcal O_C^{\oplus3}
\longrightarrow Q\longrightarrow0,
\qquad D=LA^{-1},\quad Q=N_{S/\mathbb P^4}|_C\otimes(LA)^{-1}.
\]
The injection is the dual of the complete evaluation map for \(D\): indeed \(\pi_*D=\mathcal O\oplus\mathcal O(1)\), so the three displayed scroll sections form a basis of \(H^0(C,D)\) and generate \(D\). Thus \(Q=M_D^*\), where \(M_D\) is the kernel of \(H^0(D)\otimes\mathcal O_C\to D\).

**The second step.** The evaluation map of \(\pi_*D=\mathcal O\oplus\mathcal O(1)\), pulled back to \(C\), has source \(\mathcal O_C\oplus A\), target \(D\), and kernel \(AD^{-1}\) (by determinants). The complete evaluation of \(\mathcal O\oplus\mathcal O(1)\) on \(\mathbb P^1\) has kernel \(\mathcal O(-1)\). Comparing these two evaluations by the snake lemma yields
\[
0\longrightarrow A^{-1}\longrightarrow M_D\longrightarrow AD^{-1}\longrightarrow0.
\]
Dualize to obtain
\[
0\longrightarrow DA^{-1}=LA^{-2}\longrightarrow Q\longrightarrow A\longrightarrow0.
\]
Undoing the twist produces
\[
0\longrightarrow L^2A^{-1}\longrightarrow N_{S/\mathbb P^4}|_C
\longrightarrow LA^2\longrightarrow0.
\]
Let \(E_2\subset N\) be the inverse image of the displayed saturated line subbundle in the normal quotient. This proves all three line-quotient identifications.

**Harder–Narasimhan verification.** The degree of \(L\) is \(g+4\) and that of \(A\) is two, so the quotient degrees are respectively \(4g+4\), \(2g+6\), and \(g+8\). For every \(g\ge3\),
\[
4g+4>2g+6>g+8,
\]
with differences \(2g-2\) and \(g-2\). Every line bundle is stable and all inclusions have locally free quotients. Therefore this three-step filtration satisfies the defining Harder–Narasimhan property. Its uniqueness proves that \(E_1\) is the canonical first HN subbundle. The determinant also agrees with adjunction:
\[
(L^2A^{g-2})(L^2A^{-1})(LA^2)=L^5A^{g-1}=\det N.
\]
This finishes the proof.

## Verification
The attached standard-library program \(`verify_hn.py`\) checks the three degree formulas, strict inequalities, determinant exponents, and the adjunction-derived total degree for integer genera in a representative finite range, outputting \(`VERIFY_OK`\). These finite arithmetic checks are not a proof of the infinite family; the proof is the two exact normal/evaluation diagrams above, which work symbolically for every integer \(g\ge3\). No external computational certificate is needed.

## Relationship to prior work
Liu (2026, Theorem 2.1 and Lemma 2.2) gives the complete-series semistability threshold and the scroll destabilizing line \(N_{C/S}\); its Lemma 4.1 studies a scroll-core sequence in the **different rank range** \(r\ge g+2\), with \(r=n-1\). Here \(r=3<g+2\) for \(g\ge3\). We use the cubic-scroll geometry to determine the entire three-graded Harder–Narasimhan filtration in this low-rank range. In particular, knowing only that the scroll line destabilizes does not determine the degree or saturation of the second HN step.

Coskun, Jovinelly and Larson (2026, Section 1.1.3) already identify the two-step HN filtration for the **genus-two** sextic in \(\mathbb P^4\), including the semistable rank-two quotient. That known case is expressly excluded: our theorem begins with \(g=3\) and has three *strictly* decreasing line-quotient slopes. General Brill–Noether results for curves outside the hyperelliptic locus do not imply the special-locus HN polygon. The scroll resolution is classical, and no novelty is claimed for that ingredient by itself.

## Limitations
No statement is made for special polarizations with unbalanced direct image, for non-hyperelliptic curves, or for characteristic other than zero. The filtration is one of vector bundles; it does **not** assert that the extensions split. The result determines HN degrees and factors, not individual extension classes, Hilbert-scheme geometry, or the HN polygon in ambient dimensions other than four. It has not undergone independent mathematical audit. Because the computation uses standard scroll and evaluation sequences, an equivalent derivation may exist in older or unindexed literature; the exact all-genus \(g\ge3\) statement was not identified in the inspected sources.

## References
- Xuyan Liu, *Normal bundles of hyperelliptic curves and uniform propagation of semistability*, arXiv:2610.12854v1, submitted October 9, 2026, especially Section 2 and Section 4.1; https://arxiv.org/html/2610.12854v1 .
- Izzet Coskun, Eric Jovinelly and Eric Larson, *Stability of normal bundles of Brill–Noether curves in \(\mathbb P^4\)*, arXiv:2608.01511v1, submitted August 2, 2026, especially Section 1.1.3; https://arxiv.org/abs/2608.01511 .
- Izzet Coskun and Geoffrey Smith, *Stability of normal bundles of Brill–Noether curves*, arXiv:2306.12653, 2023; https://arxiv.org/abs/2306.12653 .
