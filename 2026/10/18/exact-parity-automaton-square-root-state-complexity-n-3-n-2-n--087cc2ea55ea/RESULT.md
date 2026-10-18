# Exact parity-automaton square-root state complexity \(n^3-n^2+n\)

## Finding

For every integer \(n\ge1\), every finite alphabet \(\Sigma\), and every \(n\)-state symmetric-difference finite automaton (XNFA) over \(\mathbb F_2\) recognizing a language \(L\), there is an XNFA with at most \(n^3-n^2+n\) states recognizing
\[
\sqrt L=\{w\in\Sigma^*:ww\in L\}.
\]
For every \(n\ge2\) the bound is attained by an XNFA with precisely \(n\) essential states on a **three-letter alphabet**. It is also attained for \(n=1\), and for \(n=2\) already on a two-letter alphabet. Hence the exact worst-case XNFA state complexity of language square root, over unrestricted finite alphabets or uniformly over alphabets of size three, is
\[
\boxed{\,n^3-n^2+n\,}.
\]
The initial and final sets of an XNFA may be arbitrary; the lower-bound sources use one initial and one final state.

## Assumptions and scope

All arithmetic is in \(\mathbb F_2\). An \(n\)-state XNFA has Boolean transition matrices \(M_a\in\mathbb F_2^{n\times n}\), initial row \(\lambda\in\mathbb F_2^{1\times n}\), and final column \(\gamma\in\mathbb F_2^{n\times1}\). For a word \(w=a_1\cdots a_t\), put \(M_w=M_{a_1}\cdots M_{a_t}\), with \(M_\varepsilon=I\). Membership is determined by \(\lambda M_w\gamma=1\), the parity of accepting paths. The square-root language has characteristic function \(s(w)=\lambda M_w^2\gamma\). There are no epsilon-transitions. State counts concern XNFA, not ordinary Boolean-semiring NFAs or DFAs.

A linear representation of a binary-valued series \(s\) over \(\mathbb F_2\) is exactly an XNFA in this sense: initial/final weights and transition weights all belong to \(\{0,1\}\). Its least state dimension equals the rank over \(\mathbb F_2\) of the word Hankel matrix \(H_s(u,v)=s(uv)\). Indeed, every \(d\)-state representation factors \(H_s\) through a \(d\)-dimensional space. Conversely, the span of the residual rows \(v\mapsto s(uv)\), with right shifts \(r_u\mapsto r_{ua}\), is a representation of dimension \(\operatorname{rank}H_s\).

## Proof

**1. Normalization.** If either endpoint vector is zero, the square-root series is identically zero and one state suffices. Otherwise a change of basis normalizes the two endpoint vectors to \(\lambda=e_0^\mathsf T\) and \(\gamma=e_m\), where \(m=0\) if \(\lambda\gamma=1\), and \(m=1\) if \(\lambda\gamma=0\) (for \(n\ge2\)). To see this, in the first case choose \(\gamma\) as the first basis vector and complete with vectors from \(\ker\lambda\); in the second case take \(\gamma\) as the second basis vector, choose the first vector on which \(\lambda\) equals one, and complete a basis. Similarity preserves the recognized series and all matrix products. The \(n=1\) case is immediate.

**2. Rank over the full binary matrix monoid.** Let \(\mathcal M_n=\mathbb F_2^{n\times n}\) under multiplication and define
\[
K_m(X,Y)=e_0^\mathsf T(XY)^2e_m\qquad(X,Y\in\mathcal M_n).
\]
Expanding the entry gives the exact identity
\[
K_m(X,Y)=\sum_{q,p,r=0}^{n-1}
X_{0p}X_{qr}\,Y_{pq}Y_{rm}.
\tag{1}
\]
For a triple \((p,q,r)\), regard the left factor \(X_{0p}X_{qr}\) and the right factor \(Y_{pq}Y_{rm}\) as functions of the entries of independently variable binary matrices. Products of distinct coordinate variables, together with the single-coordinate functions obtained from \(z^2=z\), are linearly independent as long as their square-free supports differ. This follows by evaluation on all zero-one support indicators (an inclusion-triangular evaluation matrix).

For each fixed \(q\), the left monomials of (1) are distinct unless \(q=0\) and \((p,r)\) and \((r,p)\) are swapped. The right monomials are distinct unless \(q=m\) and the same swap is made. Moreover, monomial supports from different \(q\)-blocks are disjoint on both sides: the left factors use row \(q\) in addition to row zero, and the right factors use column \(q\) in addition to column \(m\), with the special same-row or same-column blocks handled separately.

If \(m=0\), the off-diagonal swapped terms in block \(q=0\) occur twice with identical left and right monomials and cancel in characteristic two. Its \(n\) diagonal terms remain independent. Each of the \(n-1\) other blocks has rank \(n^2\). Therefore
\[
\operatorname{rank}_{\mathbb F_2}K_0=n+(n-1)n^2=n^3-n^2+n.
\]
If \(m\ne0\), block \(q=0\) has independent left monomials indexed by unordered pairs \(\{p,r\}\) and independent corresponding right coefficient sums; its rank is \(n(n+1)/2\). Block \(q=m\) has the same rank with left and right exchanged. The other \(n-2\) blocks have rank \(n^2\) each. The block row/column spaces are mutually disjoint, so
\[
\operatorname{rank}_{\mathbb F_2}K_m
=n(n+1)+(n-2)n^2=n^3-n^2+n.
\tag{2}
\]
These are exact ranks of the matrix indexed by **all** \(2^{n^2}\) binary matrices, not extrapolations from sampled inputs.

**3. Universal upper bound.** For any particular input automaton, the word Hankel matrix for the square-root language is obtained by restricting \(K_m\) to pairs \((M_u,M_v)\) attained by words. Thus its rank is at most the rank in (2). By the residual-space construction, a parity automaton with at most \(n^3-n^2+n\) states recognizes the square root.

**4. Sharpness with three letters.** For \(n\ge2\), use a three-letter source automaton with \(\lambda=e_0^\mathsf T\), \(\gamma=e_1\), and transition matrices: the cyclic permutation \(C:e_i\mapsto e_{i+1\bmod n}\); the transvection \(T=I+E_{0,1}\); and the projection \(D=\operatorname{diag}(1,\ldots,1,0)\). The matrices \(C,T\) generate \(\mathrm{GL}_n(\mathbb F_2)\). Indeed, cyclic conjugation supplies elementary transvections around the directed coordinate cycle; commutators of adjacent transvections supply all other elementary transvections; elementary row additions generate the full invertible group over \(\mathbb F_2\). For \(n=2\), the two opposite transvections already generate the group. Conjugates of \(D\) delete arbitrary one-dimensional coordinates, and their products yield diagonal projections of every rank. Left and right multiplication by invertibles give every binary matrix of each rank. Hence \(C,T,D\) generate all of \(\mathcal M_n\).

Every row and column index of \(K_1\) is consequently attained by some words. Therefore the square-root word Hankel matrix has the full rank in (2) and no smaller XNFA can recognize the result. The input language itself has XNFA dimension exactly \(n\): all matrices are accessible, and the ordinary coefficient Hankel matrix \(e_0^\mathsf T XYe_1\) has rank \(n\), since both the reachable rows \(e_0^\mathsf T X\) and observable columns \(Ye_1\) span \(\mathbb F_2^n\). Thus the source is not artificially padded.

For \(n=1\), a one-state source with its unique state initial and accepting and identity transition realizes rank one.

**5. Binary sharpness at dimension two.** With \(n=2\), initial row \((1,0)\), final column \((0,1)^\mathsf T\), and binary transitions
\[
M_a=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad
M_b=\begin{pmatrix}1&1\\1&0\end{pmatrix},
\]
consider Hankel rows indexed by \(\varepsilon,a,b,ab,bb,abb\) and columns indexed by \(\varepsilon,b,ab,bb,abb,babb\). Their \(6\times6\) binary acceptance matrix is
\[
\begin{pmatrix}
0&1&1&1&0&1\\
0&1&1&0&0&0\\
1&1&0&0&1&0\\
1&0&1&0&0&0\\
1&0&0&1&0&0\\
0&0&0&1&0&0
\end{pmatrix},
\]
which has rank six over \(\mathbb F_2\). The universal upper bound is six, proving binary sharpness in this dimension.

## Verification

The attached standalone `verify.py` recomputes the monomial-collision rank independently for \(1\le n\le8\), obtains the full \(2^{n^2}\)-by-\(2^{n^2}\) matrix-Hankel ranks for \(n=2,3\) (both normalized endpoint types), enumerates the three-generator closures for \(n=2,3\), and checks the stated binary \(6\times6\) witness minor. All calculations use exact XOR arithmetic; recorded output is provided in `verification_output.txt`. The proof for all \(n\) is symbolic and does not rely on those finite tests.

## Relationship to prior work

Onishchenko (arXiv:2605.02957, first posted 2026-05-02) proves a sharp \(n^3\) state complexity of language square root for ordinary NFAs, using existential acceptance of runs. Chistikov, Piórkowski, Rino and van der Merwe (arXiv:2607.00742, first posted 2026-07-01) study parity-acceptance automata, weighted by \(\mathbb F_2\), and their algorithmic complexity. The current theorem determines a **different output representation cost**: it uses the parity of paths, establishes a smaller sharp polynomial for every \(n\ge2\), and exhibits ternary sharpness. The general Hankel-rank representation method is standard (Berstel and Reutenauer, *Noncommutative Rational Series with Applications*, Ch. 2); the explicit matrix-monoid rank calculation is the additional ingredient.

## Limitations

The claim is about parity automata over \(\mathbb F_2\), not Boolean-semiring NFAs, deterministic automata, or other coefficient fields. Sharpness is established with three letters for every \(n\ge2\); the optimal worst-case alphabet size for higher \(n\) is not classified. The work does not address higher word roots or arbitrary endomorphisms. The finite checker is independent arithmetic evidence, not an external mathematical audit; unindexed earlier equivalent formulations remain a possible priority risk.

## References

1. S. Onishchenko, *Nondeterministic state complexity of square root*, arXiv:2605.02957v1, posted 2026-05-02. https://arxiv.org/abs/2605.02957
2. D. Chistikov, R. Piórkowski, N. Rino, B. van der Merwe, *Algorithms and fine-grained complexity for nondeterministic and symmetric difference automata*, arXiv:2607.00742v1, posted 2026-07-01. https://arxiv.org/abs/2607.00742
3. J. Berstel, C. Reutenauer, *Noncommutative Rational Series with Applications*, Cambridge University Press, Ch. 2, 2010. https://doi.org/10.1017/CBO9780511760860.003
