# Exact endpoint norms of nonlinear isotype projections on generalized dihedral groups
## Finding
Let \(A\) be a finite abelian group and
\[
G=\operatorname{Dih}(A)=A\rtimes\langle\tau\rangle,
\qquad \tau^2=e,\qquad \tau a\tau=a^{-1}\quad(a\in A).
\]
Choose a character \(\lambda\in\widehat A\) with \(\lambda\ne\lambda^{-1}\). Its order
\[
L=\operatorname{ord}(\lambda)
\]
is at least \(3\), and the induced representation \(\pi_\lambda=\operatorname{Ind}_A^G\lambda\) is an irreducible two-dimensional representation; \(\pi_\lambda\) and \(\pi_{\lambda^{-1}}\) are equivalent. Let \(P_\lambda\) be the central Fourier multiplier that retains exactly this irreducible block and annihilates every other block. With normalized counting measure on \(G\),
\[
\|P_\lambda\|_{\ell^1(G)\to\ell^1(G)}
=\|P_\lambda\|_{\ell^\infty(G)\to\ell^\infty(G)}
=C_L,
\]
where
\[
C_L=\frac{2}{L}\sum_{j=0}^{L-1}\left|\cos\frac{2\pi j}{L}\right|
=\begin{cases}
\dfrac{2}{L}\csc\dfrac{\pi}{2L},&L\text{ odd},\\[1mm]
\dfrac{4}{L}\cot\dfrac{\pi}{L},&4\mid L,\\[1mm]
\dfrac{4}{L}\csc\dfrac{\pi}{L},&L\equiv2\pmod4.
\end{cases}
\]
Consequently
\[
\|P_\lambda\|=1\quad\Longleftrightarrow\quad \operatorname{ord}(\lambda)=4.
\]
Since a finite abelian group and its dual have the same exponent, \(\operatorname{Dih}(A)\) admits a contractive nonlinear single-isotype Fourier projection if and only if
\[
4\mid\exp(A).
\]
The constants have the residue-class expansions
\[
C_L=\frac4\pi+
\begin{cases}
\dfrac{\pi}{6L^2}+O(L^{-4}),&L\text{ odd},\\[1mm]
-\dfrac{4\pi}{3L^2}+O(L^{-4}),&4\mid L,\\[1mm]
\dfrac{2\pi}{3L^2}+O(L^{-4}),&L\equiv2\pmod4.
\end{cases}
\]
Thus the odd and twice-odd orders approach \(4/\pi\) from above, whereas orders divisible by \(4\), apart from the exceptional contractive order \(4\), approach it from below.

## Assumptions and scope
All spaces use normalized counting measure. The result concerns a single nonlinear central isotype projection. It does not determine intermediate \(\ell^p\)-norms, noncentral matrix-entry multipliers, or projections onto unions of irreducible blocks.

The condition \(\lambda\ne\lambda^{-1}\) is exactly what makes the inversion orbit \(\{\lambda,\lambda^{-1}\}\) have size two. Standard induction from the normal index-two subgroup \(A\) then gives the two-dimensional irreducible representation \(\pi_\lambda\).

## Proof
The induced character is
\[
\chi_\lambda(a)=\lambda(a)+\lambda(a)^{-1}=2\operatorname{Re}\lambda(a)
\quad(a\in A),
\qquad
\chi_\lambda(\tau a)=0.
\]
For normalized counting measure, finite-group Fourier inversion shows that the multiplier selecting a degree-two irreducible block is convolution by
\[
K_\lambda(g)=2\chi_\lambda(g^{-1}).
\]
Hence
\[
K_\lambda(a)=4\operatorname{Re}\lambda(a),
\qquad K_\lambda(\tau a)=0.
\]
For convolution by a kernel \(K\) on a finite group, both endpoint operator norms equal the normalized \(\ell^1\)-mass of \(K\). For \(\ell^1\), a point mass attains the bound. For \(\ell^\infty\), choose an input of modulus one whose phase agrees with the translated kernel at one output point. Therefore
\[
\|P_\lambda\|_{1\to1}=\|P_\lambda\|_{\infty\to\infty}
=\frac{2}{|A|}\sum_{a\in A}|\operatorname{Re}\lambda(a)|.
\]
Because \(\lambda\) has order \(L\), its image is all of the \(L\)-th roots of unity and every image value has exactly \(|A|/L\) preimages. Thus
\[
\|P_\lambda\|_{1\to1}=\|P_\lambda\|_{\infty\to\infty}
=\frac2L\sum_{j=0}^{L-1}\left|\cos\frac{2\pi j}{L}\right|=C_L.
\]
This also proves an exact quotient principle: the norm depends on \(A\) only through the cyclic image of \(\lambda\), and equals the endpoint norm of the two-frequency projection onto \(\{-1,1\}\) on \(\mathbb Z_L\).

It remains to evaluate the absolute-cosine sum. Put
\[
S_L=\sum_{j=0}^{L-1}\left|\cos\frac{2\pi j}{L}\right|.
\]
If \(L\) is odd, set \(q=\lfloor(L-1)/4\rfloor\). There are no zero cosine samples. The positive samples are the central sample and the two symmetric blocks of length \(q\), so the fact that the full cosine sum is zero gives
\[
S_L=2\left(1+2\sum_{j=1}^{q}\cos\frac{2\pi j}{L}\right).
\]
The Dirichlet-kernel identity
\[
1+2\sum_{j=1}^{q}\cos(j\theta)
=\frac{\sin((q+1/2)\theta)}{\sin(\theta/2)}
\]
with \(\theta=2\pi/L\) has numerator \(\cos(\pi/(2L))\), whether \(L\equiv1\) or \(3\pmod4\). Hence
\[
S_L=\csc\frac{\pi}{2L}.
\]
If \(L=4m\), the only zero samples occur at quarter turns. The positive sum is
\[
1+2\sum_{j=1}^{m-1}\cos\frac{2\pi j}{L}=\cot\frac\pi L,
\]
so \(S_L=2\cot(\pi/L)\). If \(L=4m+2\), the positive sum is
\[
1+2\sum_{j=1}^{m}\cos\frac{2\pi j}{L}=\csc\frac\pi L,
\]
so \(S_L=2\csc(\pi/L)\). These are the three displayed closed forms.

For contractivity, in the odd case put \(x=\pi/(2L)\), and in the \(L\equiv2\pmod4\) case put \(x=\pi/L\). In both cases
\[
C_L=\frac4\pi\frac{x}{\sin x}>\frac4\pi>1.
\]
When \(4\mid L\), put \(x=\pi/L\). Then
\[
C_L=\frac4\pi x\cot x.
\]
At \(L=4\) this equals one. For \(L\ge8\), \(0<x\le\pi/8\), and \(x\cot x\) is strictly decreasing on \((0,\pi/2)\); hence
\[
C_L\ge\frac12\cot\frac\pi8=\frac{1+\sqrt2}{2}>1.
\]
This proves the unique contractive order. The three asymptotic expansions follow by substituting the Taylor expansions of \(\csc x\) and \(\cot x\) into the exact formulas.

Finally, a finite abelian group has a character of order \(4\) if and only if its exponent is divisible by \(4\), because the dual group has the same invariant factors. This proves the existence criterion.

## Verification
The standalone script `artifacts/verify.py` checks the closed forms directly and also checks the quotient reduction on many noncyclic abelian groups \(\mathbb Z_m\times\mathbb Z_n\). For every tested character of order at least \(3\), it computes the average of \(|\operatorname{Re}\lambda|\) over the whole product group and compares it with the closed form determined solely by the character order. It additionally tests the contractivity classification through order \(400\).

The replay line from the packaged path is recorded in `VERIFICATION.md`. These are finite regression checks only; the universal statement is proved analytically above.

## Relationship to prior work
Atto, Mensah, and Assiamoua develop Fourier multipliers on compact groups and provide the general multiplier framework used here, but do not give the generalized-dihedral sharp endpoint constant or its contractivity classification. Lambert studies minimum-norm Fourier projections onto finite character spans on compact abelian groups; the present result is a nonabelian single-isotype projection, although its norm collapses to an abelian quotient constant.

Brochero Martínez studies central irreducible idempotents in finite dihedral group algebras over finite fields, and Dai--Li study primitive decompositions in complex dihedral group algebras and derive trigonometric identities from character orthogonality. Those algebraic works are highly relevant to the projector kernel, but the inspected material does not state the endpoint \(\ell^1\) or \(\ell^\infty\) norm, the generalized-dihedral quotient-by-character-order principle, or the exact norm-one classification.

Greenleaf's general theorem on norm-one idempotent measures says that a norm-one idempotent measure on a locally compact group is a character-weighted Haar measure on a compact subgroup. After the present projector kernel is identified, that theorem provides a broader route to the qualitative contractivity restriction. The quantitative formula for every character order, the cyclic quotient reduction, and the residue-class behavior are not supplied by that classification.

## Limitations
The 2024 Dai--Li paper is a particularly plausible terminology-adjacent source because it treats complex dihedral idempotents and trigonometric identities. The accessible article page and abstract were inspected, but the article body was not exposed through the accessed full-text interface. It is therefore retained as a concrete residual originality risk rather than used as evidence of noncoverage.

An older equivalent formula might also occur under “primitive central idempotent,” “projection constant,” or “Lebesgue constant” terminology. No such implication was located in the targeted searches. The theorem itself is restricted to one nonlinear isotype and the endpoint spaces.

## References
1. E. J. Atto, Y. Mensah, V. S. K. Assiamoua, “The Fourier Multipliers of p-Fourier Spaces on Compact Groups,” *Journal of Advances in Mathematics and Computer Science* 4(5), 667–673 (2014), published 2013-12-02, DOI: 10.9734/BJMCS/2014/5086.
2. P. V. Lambert, “On the Minimum Norm Property of the Fourier Projection in L1-Spaces,” in *Functional Analysis and Approximation*, 139–152 (1981), DOI: 10.1007/978-3-0348-9369-5_15.
3. F. E. Brochero Martínez, “Structure of Finite dihedral group algebra,” arXiv:1405.3716, first public 2014-05-14; journal DOI: 10.1016/j.ffa.2015.05.002.
4. F. P. Greenleaf, “Norm decreasing homomorphisms of group algebras,” *Pacific Journal of Mathematics* 15(4), 1187–1219 (1965), DOI: 10.2140/PJM.1965.15.1187.
5. L. Dai, Y. Li, “Primitive decompositions of idempotents of the group algebras of dihedral groups and generalized quaternion groups,” *AIMS Mathematics* 9(10), 28150–28169 (2024), DOI: 10.3934/math.20241365.
