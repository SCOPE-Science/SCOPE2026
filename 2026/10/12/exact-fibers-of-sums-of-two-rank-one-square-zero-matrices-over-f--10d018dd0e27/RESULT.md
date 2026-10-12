# Exact fibers of sums of two rank-one square-zero matrices over finite fields

## Finding
Let \(V=\mathbb F_q^n\), for a prime power \(q\) and integer \(n\ge2\), and define the nonzero minimal nilpotent similarity orbit
\[\mathcal C=\{X\in\operatorname{End}(V):\operatorname{rank}X=1,\ X^2=0\}.\]
For a prescribed matrix \(B\in\operatorname{End}(V)\), the **ordered additive convolution fiber** is
\[F(B)=\#\{(X,Y)\in\mathcal C\times\mathcal C:X+Y=B\}.\]
Then the following exhaustive formula holds over **every finite field**, including characteristic two:
\[
F(B)=\begin{cases}
0,&\operatorname{tr}B\ne0\ \text{or}\ \operatorname{rank}B\ge3,\\
\dfrac{(q^n-1)(q^{n-1}-1)}{q-1},&B=0,\\
2q^{n-1}-q-2,&\operatorname{rank}B=1,\ \operatorname{tr}B=0,\\
q e_0(T)+q+1-e(T),&\operatorname{rank}B=2,\ \operatorname{tr}B=0.
\end{cases}
\]
In the last line, \(U=\operatorname{im}B\) is a two-dimensional \(B\)-stable space, \(T=B|_U\), \(e(T)\) is the number of one-dimensional \(\mathbb F_q\)-subspaces \(L\subset U\) with \(T(L)\subseteq L\), and \(e_0(T)\) is the number of such \(L\) with \(T(L)=0\).

The formula distinguishes geometric boundary strata that the existence-only square-zero decomposition criteria do not count. For example, when \(\operatorname{char}\mathbb F_q=2\), a rank-two trace-zero target with \(T=\lambda I_U\) and \(\lambda\ne0\) has \(F(B)=0\); a rank-two target with \(T=0\) has \(F(B)=q(q+1)\). When \(n=2\) and \(q=2\), a nonzero rank-one nilpotent target also has no representation.

## Assumptions and scope
The ground field is \(\mathbb F_q\) with \(q\) an arbitrary prime power, including nonprime fields. The dimension \(n\) is any integer at least two. Both summands are **nonzero** rank-one square-zero operators, not general square-zero operators; ordered pairs are counted. All dimensions, traces, eigenlines, and counts are over \(\mathbb F_q\). A rank-one operator \(u\otimes\varphi\) is square-zero exactly when \(\varphi(u)=0\); its square is \(\varphi(u)(u\otimes\varphi)\), and its trace equals \(\varphi(u)\). Thus every summand is traceless.

## Proof
**Step 1: support and zero fiber.** Since each summand has rank one and trace zero, the target has rank at most two and trace zero. Every ordered decomposition of the zero target is uniquely \((X,-X)\), where \(X\in\mathcal C\), so \(F(0)=|\mathcal C|\). Every nonzero \(u\in V\) admits exactly \(q^{n-1}-1\) nonzero functionals \(\varphi\in V^*\) with \(\varphi(u)=0\). Each operator \(u\otimes\varphi\) is produced by exactly \(q-1\) scalar rescalings of its factors. Hence
\[|\mathcal C|=\frac{(q^n-1)(q^{n-1}-1)}{q-1}.\]

**Step 2: rank-one fiber.** Let \(B=u\otimes\varphi\ne0\), with \(\varphi(u)=0\). Whenever two nonzero rank-one operators sum to a rank-one operator, either their image lines agree or their row-functional lines agree: if both pairs were independent, their sum would have rank two. In the common-image case write \(X=u\otimes\psi\), \(Y=u\otimes(\varphi-\psi)\). Square-zero and nonzero summands require \(\psi(u)=0\) and \(\psi\notin\{0,\varphi\}\), giving \(q^{n-1}-2\) choices. Dually, the common-row case also gives \(q^{n-1}-2\) choices. Both cases hold simultaneously exactly when \(X=cB\), \(Y=(1-c)B\) with \(c\in\mathbb F_q\setminus\{0,1\}\), giving \(q-2\) overlaps. Inclusion-exclusion yields
\[F(B)=2(q^{n-1}-2)-(q-2)=2q^{n-1}-q-2.\]

**Step 3: rank-two fiber and quotient identification.** Suppose \(\operatorname{rank}B=2\) and \(\operatorname{tr}B=0\). Put \(K=\ker B\), \(E=V/K\), and \(U=\operatorname{im}B\). Factor \(B=L\pi\) through the quotient \(\pi:V\to E\) and the isomorphism \(L:E\to U\subset V\). If \(B=X+Y\) with both summands of rank one, their image lines must be independent and span \(U\), and their row-functional lines must be independent and span the row space of \(B\). Consequently each summand maps \(V\) into \(U\) and vanishes on \(K\). There are unique rank-one endomorphisms \(P,Q:E\to E\) with
\[X=LP\pi,\qquad Y=LQ\pi,\qquad P+Q=I_E.\]
Because \(P\) and \(I_E-P\) both have rank one, \(P\) is an idempotent of rank one. Conversely, every rank-one idempotent \(P\) yields two rank-one summands by these formulas. This establishes a bijection before imposing the square-zero constraint.

**Step 4: the trace condition becomes an eigenline problem.** Write \(P=v\otimes\lambda\) on the two-space \(E\), with \(v\ne0\) and \(\lambda(v)=1\). Let \(S=\pi L:E\to E\), which is conjugate via \(L\) to \(T=B|_U\), since \(B L=L S\). By cyclicity of rectangular traces,
\[\operatorname{tr}(LP\pi)=\operatorname{tr}(PS)=\lambda(Sv).\]
The target has trace zero, so the second summand is traceless if and only if the first is. Thus admissibility is exactly
\[\lambda(v)=1,\qquad\lambda(Sv)=0.\]
Fix an image line \(\ell=\langle v\rangle\) in \(E\). When \(Sv=0\), the first equation has \(q\) solutions for \(\lambda\). When \(Sv\in\langle v\rangle\setminus\{0\}\), the equations contradict each other and yield none. When \(Sv\notin\langle v\rangle\), the vectors \(v,Sv\) form a basis of \(E\), so the two equations uniquely determine \(\lambda\). There are \(q+1\) lines in \(E\), of which \(e(S)=e(T)\) are invariant and \(e_0(S)=e_0(T)\) are zero eigenlines. Summing the three cases yields
\[F(B)=q e_0(T)+q+1-e(T).\]
Every projection counted once corresponds to one **ordered** pair, and conversely all ordered pairs arise. This completes the proof in every characteristic.

## Verification
The standalone `verify.py` uses only the Python standard library. Execute `python verify.py`. It enumerates all distinct nonzero rank-one square-zero matrices, forms all ordered sums, and independently evaluates the displayed formula by finite-field Gaussian elimination and restricted eigenline enumeration. For \((q,n)=(2,2),(3,2),(4,2),(5,2),(2,3),(3,3),(2,4)\), it checks **every** target; for \((q,n)=(4,3)\), it checks every attained target plus selected unattained targets. The \(q=4\) implementation uses \(\mathbb F_2[t]/(t^2+t+1)\). All tests terminate with `VERIFY_OK`. Finite checks are corroboration, not proof of the all-fields theorem.

## Relationship to prior work
The square-zero decomposition problem and broader quadratic-summand existence criteria were studied by Botha and by de Seguins Pazzis; Song–Zheng–Cao also give an alternative existence equivalence. De Seguins Pazzis explicitly distinguishes the previously solved **two square-zero summands** existence problem from his **idempotent plus square-zero** main theorem. The present result fixes the strict rank-one nonzero orbit and gives the full prescribed-target **ordered multiplicity**, including all zero fibers, for every field size and dimension. An existence characterization does not determine these multiplicities, and neither the inspected full text nor the available abstracts establish this orbit-convolution formula. The elementary two-dimensional eigenspace/projection counting used here is distinct from classifying the possible invariant-factor types of target matrices. Previously available structural ingredients and known existence work are not presented as new.

## Limitations
This theorem does not count decompositions with arbitrary-rank square-zero summands or more than two summands. It does not assert that the formula is the first appearance of this fact anywhere in the broader literature; an equivalent finite-group orbit-convolution calculation under different terminology remains a residual bibliographic risk. Full text of Botha's paper was not accessible through the routes used, and Song–Zheng–Cao's full text was obstructed; their published abstracts and the explicit discussion in de Seguins Pazzis were used only for statement-level comparison. No independent mathematical audit has been performed.

## References
1. C. de Seguins Pazzis, *Sums of two triangularizable quadratic matrices over an arbitrary field*, arXiv:1109.2255v1 (first posted 2011-09-10), full text https://arxiv.org/html/1109.2255v4 .
2. J. D. Botha, *Sums of two square-zero matrices over an arbitrary field*, Linear Algebra and its Applications 436 (2012), 516–524, DOI:10.1016/j.laa.2011.07.011 .
3. X. Song, B. Zheng, C. Cao, *A Note on Decomposing a Square Matrix as Sum of Two Square Nilpotent Matrices over an Arbitrary Field*, The Scientific World Journal (2013), article 640350, DOI:10.1155/2013/640350 .
