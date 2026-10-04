# Positive Lebesgue measure for admissible non-central section areas

## Finding
Let \(\omega_3=4\pi/3\), let \(\gamma_* = \pi^{-1}\arctan 2\), and for \(\gamma\in(\gamma_*,1/2)\) set
\[
A(\gamma)=\omega_3\tan^3(\pi\gamma),\qquad R(\gamma)=\sec(\pi\gamma).
\]
Use the notation of Haddad--Ryabogin, arXiv:2605.00299v1: for \(A=A(\gamma)\),
\[
\delta_{A,k}=\pi\,\operatorname{dist}((2k-1)\gamma,\mathbb Z),
\]
and \(\alpha_{A,k}<\beta_{A,k}\) are the two smallest values among \(\delta_{A,1},\ldots,\delta_{A,k}\). Their condition \(C(A,k)\) is
\[
F_{A,+}(\alpha_{A,k},\beta_{A,k})<\delta_{A,k+1},\qquad
F_{A,-}(\alpha_{A,k})<\delta_{A,k+1}.
\]
Their admissible set \(\mathbb A\) consists of the values \(A>8\omega_3\) for which \(\gamma\) is irrational and all the conditions \(C(A,k)\) hold. Then \(\mathbb A\) has positive one-dimensional Lebesgue measure.

Therefore the rigidity conclusion of Haddad--Ryabogin holds for a positive-Lebesgue-measure set of section areas: if \(C\subset\mathbb R^4\) is a symmetric convex body of revolution containing the unit ball and every hyperplane tangent to the unit ball cuts \(C\) in the same three-dimensional area \(A\in\mathbb A\), then \(C\) is a Euclidean ball.

## Assumptions and scope
The argument uses the definitions and elementary estimates for \(F_{A,+}\) and \(F_{A,-}\), the continued-fraction estimates, and one explicit admissible example from arXiv:2605.00299v1. It does not alter the geometric part of that paper. The only new step is a measure-theoretic continued-fraction argument showing that a whole positive-measure family, rather than merely a positive-Hausdorff-dimension family, satisfies the paper's conditions.

Write an irrational \(\gamma=[a_0;a_1,a_2,\ldots]\) with convergents \(p_j/q_j\). We use the standard estimates, also stated in the source,
\[
\frac{1}{q_j(a_{j+1}+2)}<\lVert q_j\gamma\rVert<\frac1{q_{j+1}},
\qquad q_j\ge 2^{(j-1)/2},
\]
and the best-approximation property that if \(1\le m<q_{j+1}\), then \(\lVert m\gamma\rVert\ge\lVert q_j\gamma\rVert\).

The source also proves, in the range needed below,
\[
F_{A,-}(x)\le
\frac{x^2}{\cos x\sqrt{R^2\cos^2x-1}},
\]
and
\[
F_{A,+}(s,t)\le
\frac{st}{2\cos((s+t)/2)\sqrt{R^2-1}}.
\]

## Proof
First prove a uniform tail lemma. Fix a compact interval \(J\Subset(\gamma_*,1/2)\). Suppose \(\gamma\in J\) and, from some fixed index onward, its continued-fraction digits obey \(a_j\le j^2\). Then there is an integer \(K_J\), independent of \(\gamma\), such that \(C(A(\gamma),k)\) holds for every \(k\ge K_J\).

Indeed, fix large \(k\), put \(m=2k-1\), and choose \(n\) with \(q_n\le m<q_{n+1}\). Consecutive convergent denominators are coprime, hence two consecutive denominators cannot both be even. Therefore among
\[
q_{n-3},q_{n-2},q_{n-1},q_n
\]
there are at least two odd denominators. For each such odd denominator \(q_r=2j_r-1\), one has \(j_r\le k\) and
\[
\delta_{A,j_r}=\pi\lVert q_r\gamma\rVert<\frac{\pi}{q_{r+1}}\le\frac{\pi}{q_{n-2}}.
\]
Thus both of the two smallest previous angular distances satisfy
\[
\alpha_{A,k},\beta_{A,k}\le \frac{\pi}{q_{n-2}}.
\]
The recurrence \(q_{j+1}=a_{j+1}q_j+q_{j-1}\), together with \(m<q_{n+1}\), gives
\[
q_{n-2}>
\frac{m}{(a_{n-1}+1)(a_n+1)(a_{n+1}+1)}.
\]
For large \(n\), the digit bound therefore yields
\[
\alpha_{A,k},\beta_{A,k}
\le
\frac{\pi((n+1)^2+1)^3}{2k-1}.
\]
Since \(q_n\le2k-1\) and \(q_n\ge2^{(n-1)/2}\), one has \(n=O(\log k)\), uniformly. Hence
\[
\alpha_{A,k},\beta_{A,k}=O\!\left(\frac{(\log k)^6}{k}\right).
\]

For the next angular distance, put \(M=2k+1\) and choose \(t\) with \(q_t\le M<q_{t+1}\). Best approximation and the lower continued-fraction estimate give
\[
\delta_{A,k+1}
=\pi\lVert M\gamma\rVert
\ge \pi\lVert q_t\gamma\rVert
>
\frac{\pi}{q_t(a_{t+1}+2)}
\ge
\frac{\pi}{M(a_{t+1}+2)}.
\]
Again \(t=O(\log k)\), so the digit bound implies
\[
\delta_{A,k+1}=\Omega\!\left(\frac{1}{k(\log k)^2}\right)
\]
uniformly on \(J\).

Because \(J\) is compact, \(R(\gamma)\) stays uniformly away from the singular values in the displayed bounds for \(F_{A,+}\) and \(F_{A,-}\). For large \(k\), \(\alpha_{A,k}\) and \(\beta_{A,k}\) are uniformly small, and those bounds give
\[
F_{A,-}(\alpha_{A,k}),\quad
F_{A,+}(\alpha_{A,k},\beta_{A,k})
=O\!\left(\frac{(\log k)^{12}}{k^2}\right).
\]
This is \(o(1/(k(\log k)^2))\), so both inequalities in \(C(A,k)\) hold for every sufficiently large \(k\), uniformly in the stated family. This proves the tail lemma. Notice that no parity restriction on all large convergent denominators is needed; four consecutive denominators always contain two odd ones.

Now use the explicit admissible number from the source,
\[
\gamma_1=\frac{\sqrt2+40}{94}=[0;2,3,1,2,2,2,\ldots],
\]
for which the paper verifies every condition \(C(A(\gamma_1),k)\). Choose a compact interval \(J\Subset(\gamma_*,1/2)\) containing \(\gamma_1\) in its interior. Apply the uniform tail lemma to the bound \(a_j\le j^2\), obtaining \(K_J\). The finitely many inequalities \(C(A,k)\) for \(k<K_J\) are strict at \(\gamma_1\), and their ingredients are continuous in \(\gamma\) away from rational collision points. Hence there is an open interval \(U\subset J\) around \(\gamma_1\) on which all these finitely many conditions remain true.

Take a sufficiently deep continued-fraction cylinder \(I_L\) determined by the first \(L\) digits of \(\gamma_1\), with \(L\ge4\), so that \(I_L\subset U\). Inside it define
\[
S_L=\{\gamma\in I_L:a_j(\gamma)\le j^2\text{ for every }j>L\}.
\]
This set has positive Lebesgue measure. To see this directly, recall that a cylinder ending at denominator \(q_n\) has length
\[
|I_n|=\frac1{q_n(q_n+q_{n-1})}.
\]
If \(r=q_{n-1}/q_n\in(0,1)\), the relative length of the child cylinder with next digit \(m\) is
\[
\frac{1+r}{(m+r)(m+1+r)}.
\]
Consequently the relative proportion discarded by requiring the next digit to be at most \(M\) is
\[
\sum_{m>M}\frac{1+r}{(m+r)(m+1+r)}
=\frac{1+r}{M+1+r}
\le\frac2{M+1}.
\]
Applying this successively with \(M=j^2\) and summing the first-violation proportions gives
\[
|S_L|\ge |I_L|\left(1-\sum_{j>L}\frac2{j^2+1}\right)>0,
\]
where the final inequality holds already for \(L\ge4\).

Every \(\gamma\in S_L\) is irrational. Its finite conditions \(C(A,k)\) with \(k<K_J\) hold because \(I_L\subset U\), while all later conditions hold by the uniform tail lemma. Thus \(A(\gamma)\in\mathbb A\) for every \(\gamma\in S_L\).

Finally, \(A(\gamma)=\omega_3\tan^3(\pi\gamma)\) is smooth and strictly increasing on \((\gamma_*,1/2)\), with
\[
A'(\gamma)=4\pi^2\tan^2(\pi\gamma)\sec^2(\pi\gamma)>0.
\]
On the compact cylinder \(I_L\), its derivative is bounded below by a positive constant. Hence \(A(S_L)\subset\mathbb A\) has positive Lebesgue measure. Therefore \(\mathbb A\) itself has positive Lebesgue measure.

## Verification
The proof was checked in five independent logical pieces: the parity argument for four consecutive convergent denominators; the upper estimate for the two smallest odd-multiple distances; the best-approximation lower estimate for the next odd-multiple distance; the exact continued-fraction cylinder child-length ratio and its telescoping tail; and preservation of positive measure under the monotone map \(\gamma\mapsto A(\gamma)\).

For the cylinder step, the discarded relative mass after imposing \(a_j\le j^2\) is bounded by \(2/(j^2+1)\); the numerical tail from \(j=5\) is approximately \(0.435699\), strictly below \(1\). This numerical value is only a sanity check: convergence of the displayed series and the inequality below \(1\) for sufficiently large \(L\) are elementary and the proof does not depend on floating-point computation.

No finite experiment is used as evidence for the infinite conclusion. The tail lemma is uniform and analytic.

## Relationship to prior work
Haddad--Ryabogin prove that their admissible set \(\mathbb A\) has positive Hausdorff dimension and explicitly say that positive Lebesgue measure appears likely but was not pursued. Their Question 15 asks whether \(\mathbb A\) has positive Lebesgue measure. The argument above answers that question affirmatively by removing the global parity restriction from the tail estimate and combining a uniform polynomial-digit tail criterion with an elementary positive-measure cylinder construction.

Targeted searches for the paper title, its arXiv identifier, the phrase "positive Lebesgue measure," the Barker--Larman context, and the continued-fraction formulation did not locate a later paper or published result giving this conclusion. Searches of the published published-finding corpus corpus under the same claim and aliases also returned no statement implying it.

## Limitations
The conclusion concerns the particular admissible set \(\mathbb A\) and four-dimensional symmetric bodies of revolution treated by arXiv:2605.00299v1. It does not solve the Barker--Larman problem in general, does not remove the body-of-revolution or symmetry hypotheses of the cited theorem, and does not estimate the exact measure or density of \(\mathbb A\).

The novelty assessment is based on targeted searches through the current public literature and published published-finding corpus records; it cannot exclude an unindexed, unpublished, or differently phrased prior proof. The argument also relies on the source paper's stated inequalities for \(F_{A,+}\) and \(F_{A,-}\) and its verified admissible base point \(\gamma_1\).

## References
1. J. Haddad and D. Ryabogin, *On convex bodies with constant non-central sections*, arXiv:2605.00299v1, first submitted 2026-05-01, https://arxiv.org/abs/2605.00299.
2. Standard continued-fraction facts used above are also recorded in Propositions 10--12 of the cited preprint.
