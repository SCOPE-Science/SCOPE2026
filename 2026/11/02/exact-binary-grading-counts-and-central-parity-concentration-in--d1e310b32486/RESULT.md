# Exact binary-grading counts and central-parity concentration in finite Heisenberg extensions

## Finding

Let \(q\) be any prime power and \(n,r\) integers with \(n\geq 1\) and \(r\geq 1\). Define the finite-field Lie algebra
\[
 L_{n,r}=\mathfrak h_{2n+1}(\mathbb F_q)\oplus\mathbb F_q^r,
\]
where the second summand is central. Write \(Z=Z(L_{n,r})\), \(c=\dim Z=r+1\), and \(K=[L_{n,r},L_{n,r}]\), a distinguished one-dimensional subspace of \(Z\). A **binary grading** is an ordered pair of subspaces \((L_0,L_1)\) with \(L_{n,r}=L_0\oplus L_1\) and \([L_i,L_j]\subseteq L_{i+j\pmod 2}\). Neither component is required to be nonzero; we count distinct ordered decompositions on this fixed algebra, **not** equivalence classes under automorphisms.

Set \(S_0(q)=1\) and, for \(a\geq 1\),
\[
 S_a(q)=q^{a^2}\prod_{i=1}^{a}(q^{2i}-1)=|\operatorname{Sp}_{2a}(q)|.
\]
Write \(\binom ab_q\) for the Gaussian binomial coefficient, taken to be zero when \(b\notin\{0,\dots,a\}\). The number \(E_{n,r}(q)\) of binary gradings with \(K\subseteq L_0\), and the number \(O_{n,r}(q)\) with \(K\subseteq L_1\), are exactly
\[
 E_{n,r}(q)=\sum_{t=0}^{r}\binom rt_q q^{t(c-t)}
 \sum_{b=0}^{n}\frac{S_n(q)}{S_b(q)S_{n-b}(q)}
 q^{2(n-b)t+2b(c-t)},
\]
\[
 O_{n,r}(q)=q^{nc+n(n+1)/2}\prod_{i=1}^{n}(q^i+1)
 \sum_{t=1}^{c}\binom r{t-1}_q q^{t(c-t)}.
\]
In particular, \(E_{n,r}+O_{n,r}\) counts all binary gradings, over every characteristic, including characteristic two. The same formulas also hold at the boundary \(r=0\) (ordinary Heisenberg algebras), although the new central-stabilization assertion concerns \(r\geq1\).

For fixed \(q,r\), as \(n\to\infty\), put
\[
 C_q=\prod_{i=1}^{\infty}(1-q^{-2i}),\qquad
 D_q=\prod_{i=1}^{\infty}(1+q^{-i}),
\]
\[
 B_{r,q}=\sum_{t=1}^{c}\binom r{t-1}_q q^{t(c-t)},\qquad
 A_{r,q}=\frac12\sum_{t=0}^{r}\binom rt_q q^{t(c-t)}
 \sum_{k\in\mathbb Z}q^{-k^2+(c-2t)k}.
\]
All constants are finite and positive. For a uniformly chosen binary grading,
\[
 \boxed{\Pr(K\subseteq L_1)
 =1-\frac{A_{r,q}}{C_qD_qB_{r,q}}q^{-n}+o(q^{-n}).}
\]
Thus the derived line lies in the odd component with probability tending to one, at an explicitly determined rate \(q^{-n}\), despite the two possible parities both being realized.

## Assumptions and scope

Choose a vector-space splitting \(L_{n,r}=V\oplus Z\), with \(\dim V=2n\). The Lie bracket is \([u+z_1,v+z_2]=\omega(u,v)z_*\), for a chosen \(0\neq z_*\in K\) and a nondegenerate alternating bilinear form \(\omega\) on \(V\). In characteristic two, alternating means \(\omega(v,v)=0\) for all \(v\), and no division by two is used. The isomorphism class is independent of the splitting and symplectic basis. The results concern gradings indexed by the group \(\mathbb Z/2\mathbb Z\) with fixed labels \(0,1\); they are not gradings of Lie superalgebras or classifications up to conjugation.

The center is characteristic as a subspace and is itself graded for every group grading: if \(z=z_0+z_1\in Z\) is the decomposition into homogeneous parts, then \([z_i,L_j]=0\) separately because the outputs have different degrees. The derived subspace is graded by the same degree argument. Since \(K\) is one-dimensional, precisely one of \(K\subseteq L_0\) and \(K\subseteq L_1\) holds.

## Proof

**1. Graded central decompositions.** Let \(Z_i=Z\cap L_i\) and \(t=\dim Z_1\). The center has an ordered decomposition \(Z=Z_0\oplus Z_1\). If \(K\subseteq Z_0\), then \(0\leq t\leq r\). Choosing \(Z_0\), a \((c-t)\)-subspace through \(K\), gives \(\binom rt_q\) choices; every such \(Z_0\) has exactly \(q^{t(c-t)}\) complementary subspaces \(Z_1\). Hence the central factor is \(\binom rt_q q^{t(c-t)}\). If instead \(K\subseteq Z_1\), then \(1\leq t\leq c\). The analogous factor is \(\binom r{t-1}_q q^{t(c-t)}\).

**2. The quotient and its lifts.** Since \(Z\) is graded, its symplectic quotient \(V=L_{n,r}/Z\) receives an ordered direct-sum grading \(V=V_0\oplus V_1\). Fix this quotient grading and the central grading. Relative to a fixed linear splitting \(V\hookrightarrow L_{n,r}\), each lifted grading is uniquely described by a linear graph map \(f_0:V_0\to Z/Z_0\simeq Z_1\) and \(f_1:V_1\to Z/Z_1\simeq Z_0\). The number of lifts is therefore
\[
 q^{(\dim V_0)t+(\dim V_1)(c-t)}.
\]
The bracket of lifted elements is unchanged by these central graph maps, so none of these choices creates further constraints. Different graph maps give different ordered graded decompositions.

**3. The even-derived case.** If \(K\subseteq Z_0\), the only bracket constraint not automatic by degree is \([V_0,V_1]=0\). Since \(V_0\oplus V_1=V\) and \(\omega\) is nondegenerate, this is equivalent to an orthogonal decomposition into two symplectic summands. Therefore \(\dim V_1=2b\) for some \(0\leq b\leq n\). The symplectic group acts transitively on ordered orthogonal decompositions of these dimensions, with stabilizer \(\operatorname{Sp}_{2b}(q)\times\operatorname{Sp}_{2(n-b)}(q)\). Their number is
\[
 \frac{S_n(q)}{S_b(q)S_{n-b}(q)}.
\]
Applying the lift exponent from step 2 with \(\dim V_0=2(n-b)\) and \(\dim V_1=2b\), then summing the center and quotient possibilities, proves the asserted formula for \(E_{n,r}(q)\).

**4. The odd-derived case.** If \(K\subseteq Z_1\), the required conditions are \(\omega(V_0,V_0)=\omega(V_1,V_1)=0\): both quotient components must be totally isotropic. Because they complement one another in a nondegenerate \(2n\)-dimensional symplectic space, each is an \(n\)-dimensional Lagrangian. The number of Lagrangian subspaces is \(\prod_{i=1}^{n}(q^i+1)\): count pairs consisting of an isotropic line and a Lagrangian through it, then induct on the symplectic quotient of that line. For each Lagrangian \(V_0\), its transverse Lagrangian complements are graphs of symmetric bilinear forms, of which there are exactly \(q^{n(n+1)/2}\). This characterization and count remain valid in characteristic two. For all such pairs the lift factor is \(q^{nc}\), independent of \(t\). Multiplication by the central count in step 1 and summation over \(1\leq t\leq c\) proves the asserted formula for \(O_{n,r}(q)\).

For completeness, the symplectic-group order \(S_n(q)\) follows by recursively counting symplectic bases: choose the first nonzero basis vector in \(q^{2n}-1\) ways and its symplectic partner in \(q^{2n-1}\) ways, then apply induction on the orthogonal complement. Consequently \(S_n(q)=q^{n^2}\prod_{i=1}^n(q^{2i}-1)\), with no restriction on field characteristic.

**5. Asymptotics and the parity cancellation.** Write \(C_{q,j}=\prod_{i=1}^{j}(1-q^{-2i})\), with \(C_{q,0}=1\). Since
\[
 \frac{S_n(q)}{S_b(q)S_{n-b}(q)}
 =q^{4b(n-b)}\frac{C_{q,n}}{C_{q,b}C_{q,n-b}},
\]
we substitute \(k=2b-n\). The full exponent of \(q\) in the even formula, apart from the center coefficient, becomes \(n^2+nc-k^2+(c-2t)k\). For each fixed integer \(k\) of parity \(n\), the ratio of the \(C\)-factors tends to \(1/C_q\). These ratios are bounded above by \(C_q^{-2}\), while the tails are bounded by a convergent Gaussian series. Dominated convergence yields
\[
 \frac{E_{n,r}(q)}{q^{n^2+nc}}\longrightarrow
 \frac{1}{C_q}\sum_{t=0}^r\binom rt_q q^{t(c-t)}
 \sum_{\substack{k\in\mathbb Z\\k\equiv n\pmod2}}
 q^{-k^2+(c-2t)k}.
\]
The apparent dependence on parity disappears *after summation over \(t\)*. The involution \((t,k)\mapsto(r-t,1-k)\) interchanges the two parities and preserves both \(\binom rt_q\) and the entire exponent
\[
 t(c-t)-k^2+(c-2t)k.
\]
Hence the parity-restricted sum equals one half of the unrestricted sum, namely \(A_{r,q}\). This establishes \(E_{n,r}(q)\sim (A_{r,q}/C_q)q^{n^2+nc}\).

On the other hand,
\[
 O_{n,r}(q)=B_{r,q}\,q^{n^2+(c+1)n}\prod_{i=1}^{n}(1+q^{-i}),
\]
so \(O_{n,r}(q)\sim B_{r,q}D_q q^{n^2+(c+1)n}\). Thus \(E_{n,r}/O_{n,r}\sim (A_{r,q}/(C_qD_qB_{r,q}))q^{-n}\). Since \(E_{n,r}/O_{n,r}\to0\), the fraction \(O_{n,r}/(E_{n,r}+O_{n,r})\) has the claimed expansion.

## Verification

The accompanying standalone `verify.py` counts all ordered subspace decompositions \(L=L_0\oplus L_1\) by independent reduced-row-echelon enumeration and directly tests the homogeneous Lie-bracket rules. It checks six full cases:
\[
 (q,n,r;E,O)=(2,1,0;5,12),\ (2,1,1;33,72),\ (2,1,2;385,816),
\]
\[
 (2,2,0;97,480),\ (3,1,0;10,36),\ (3,1,1;136,432).
\]
It also exhaustively enumerates every \(3\times3\) idempotent linear projector over \(\mathbb F_2\) and \(\mathbb F_3\) and tests its induced homogeneous bracket conditions, independently recovering the two \(n=1,r=0\) counts. The command `python3 verify.py` returned `VERIFY_OK: six exhaustive decomposition cases, two exhaustive projector cases`. These finite checks corroborate, but cannot replace, the unrestricted proof.

As an asymptotic numerical check only, at \(q=2,r=1\), the normalized ratio \(q^nE_{n,r}/O_{n,r}\) is approximately \(0.8649262644\) at \(n=8\) and \(0.8645836534\) at \(n=12\), approaching the derived constant approximately \(0.8645608354\). Numerical convergence does not establish the infinite statement.

## Relationship to prior work

Calderón, Draper, Martín and Sánchez, *Gradings and Symmetries on Heisenberg type algebras* (arXiv:1405.4093, 2014), Section 3 and Theorem 1, provide the symplectic homogeneous-basis/gradation structure for the **ordinary** Heisenberg algebra with one-dimensional **center**, studying gradings up to equivalence, fine gradings and Weyl groups. The \(r=0\) qualitative symplectic splitting structure is prior art and is not claimed as new. Their defining Heisenberg object has \(\dim Z=1\); the centrally stabilized family here has \(\dim Z=r+1>1\), and the present result enumerates *each labeled decomposition* over arbitrary finite fields rather than classifying gradings up to equivalence.

Eick and Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields* (arXiv:2205.03155, first posted 2022-05-06), develop algorithms and data for finite-field **simple** Lie algebras, not counts for this nilpotent family. Hakavuori, Kivioja, Moisala and Tripaldi, *Gradings for nilpotent Lie algebras* (arXiv:2011.06871, 2020), study characteristic-zero/torsion-free gradings and do not assert this positive-characteristic binary-grading census. Existing related records on Heisenberg subalgebra commutativity and fixed-point-free automorphisms concern different invariants; they do not imply this count without further arguments.

## Limitations

The theorem counts literal ordered \(\mathbb Z/2\mathbb Z\)-homogeneous decompositions, not grading-orbit isomorphism classes or grading-preserving automorphism groups. It does not classify every group grading, nor does the asymptotic concern a regime where \(q\) or \(r\) varies with \(n\). The case \(r=0\) has already been treated qualitatively in prior literature. An earlier formula implicit in broader finite classical-group involution or symplectic orbit counting remains a publication-priority possibility; no global uniqueness claim is made. The finite verification cases are not a substitute for the analytic asymptotic or a proof of global novelty.

## References

1. A. Calderón, C. Draper, C. Martín and T. Sánchez, *Gradings and Symmetries on Heisenberg type algebras*, 2014 preprint, arXiv:1405.4093. https://arxiv.org/abs/1405.4093
2. B. Eick and T. Moede, *Computing subalgebras and \(\mathbb Z_2\)-gradings of simple Lie algebras over finite fields*, 2022 preprint, arXiv:2205.03155. https://arxiv.org/abs/2205.03155
3. E. Hakavuori, K. Kivioja, T. Moisala and F. Tripaldi, *Gradings for nilpotent Lie algebras*, 2020 preprint, arXiv:2011.06871. https://arxiv.org/abs/2011.06871
