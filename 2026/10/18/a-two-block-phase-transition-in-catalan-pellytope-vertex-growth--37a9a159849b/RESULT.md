# A two-block phase transition in Catalan-pellytope vertex growth

## Finding

For each real \(0<\alpha<1\), let \(d_n=\lfloor\alpha n\rfloor\) and let \(V_n(\alpha)\) be the number of vertices of the Catalan pellytope \(\mathcal P_{d_n,n}\), defined below. For every fixed \(\alpha\in(0,1)\),

\[
\lim_{n\to\infty}\frac{n^2 V_n(\alpha)}{4^n}=
\begin{cases}
0,&0<\alpha\le\tfrac12,\\[3pt]
\displaystyle\frac{16(2\alpha-1)}{\pi\sqrt{\alpha(1-\alpha)}},&\tfrac12<\alpha<1.
\end{cases}
\]

In particular, the linear interpolation depth has a threshold at one half for the \(4^n/n^2\) vertex scale. This is a joint limit with both dimension and depth growing: it is not a statement about first fixing the depth.

## Assumptions and scope

For integers \(n\ge1\), \(1\le d\le n\), and coordinates \(y_1,\ldots,y_n\), define
\[
q_{k,j}(y)=1+y_j+y_jy_{j+1}+\cdots+y_jy_{j+1}\cdots y_{j+k-1},
\qquad1\le k\le d,\quad1\le j\le n-k+1,
\]
and the \(n\)-dimensional polytope
\[
\mathcal P_{d,n}=\operatorname{Newt}\!\left(\prod_{k=1}^{d}\prod_{j=1}^{n-k+1}q_{k,j}\right).
\]
The source proves that its vertex count \(S_n^{(d)}\) has generating function
\[
\sum_{r\ge0}S_r^{(d)}z^r=
\left(1-2z-\sum_{k=1}^{d-1}C_kz^{k+1}\right)^{-1},
\qquad C_k=\frac1{k+1}\binom{2k}{k}.
\]
The result here concerns \(d=d_n\) and the coefficient \(r=n\). The floor is part of the statement. For fixed \(\alpha>0\) the required condition \(1\le d_n<n\) holds for all sufficiently large \(n\).

## Proof

**1. Renewal-form expansion.** Set \(a_1=2\), \(a_j=C_{j-1}\) for every integer \(j\ge2\), and \(b_j=a_j4^{-j}\). The cited generating function, evaluated coefficientwise, gives
\[
4^{-n}S_n^{(d_n)}=
\sum_{m\ge1}\ \,\sum_{\substack{j_1+\cdots+j_m=n\\1\le j_i\le d_n}}
\prod_{i=1}^{m}b_{j_i}.
\tag{1}
\]
All summands are nonnegative. The Catalan generating function yields
\[
p:=\sum_{j\ge1}b_j=\frac34,
\qquad b_j\sim\frac{1}{4\sqrt\pi\,j^{3/2}},
\qquad b_j\le B j^{-3/2}\quad(j\ge1)
\tag{2}
\]
for some absolute finite \(B\). Because \(d_n<n\), the \(m=1\) term of (1) vanishes.

**2. Fixed number of blocks.** Denote the inner sum for a given \(m\) by \(T_{n,m}\) and fix \(m\ge2\). Write \(\kappa=1-\alpha>0\). In every admissible composition, at least two distinct parts are at least \(\kappa n/m\): the largest is at least \(n/m\), and the other \(m-1\) parts together have sum at least \(\kappa n\).

Fix a cutoff \(K\ge1\). In the contribution where exactly two parts exceed \(K\) and all others are at most \(K\), pick their two positions and fix the small parts, whose sum \(s\) is bounded independently of \(n\). Their remaining total is \(n-s\), so the contribution of the large pair is
\[
\sum_{\substack{j+(n-s-j)=n-s\\ K<j,n-s-j\le d_n}}
 b_j b_{n-s-j}.
\]
For \(\alpha>1/2\), the two lower cutoff inequalities are automatic for large \(n\), and the Catalan asymptotic in (2), uniformly on the closed macroscopic interval, gives the Riemann-sum limit
\[
n^2\sum_{j=n-s-d_n}^{d_n}b_jb_{n-s-j}
\longrightarrow \frac{I(\alpha)}{16\pi},
\quad I(\alpha):=\int_{1-\alpha}^{\alpha}
\frac{dt}{[t(1-t)]^{3/2}}.
\tag{3}
\]
For \(\alpha<1/2\), no such two-part configuration exists for all large \(n\). For \(\alpha=1/2\), at most \(s+1\) terms occur, each \(O(n^{-3})\), so the scaled limit is zero. Thus in every case (3) holds with the convention \(I(\alpha)=0\) for \(\alpha\le1/2\).

The configurations with at least three parts exceeding \(K\) do not contribute in the eventual cutoff limit. Indeed, choose the two distinct parts of size at least \(\kappa n/m\) and a third part greater than \(K\). By \(b_j\le B j^{-3/2}\), the sum over the first two positions, with a prescribed remaining total, is bounded by \(B^2\kappa^{-3}m^3n^{-2}\). The third contributes at most \(\sum_{j>K}b_j\), and each remaining position contributes at most \(p\). A finite union bound over choices of positions therefore gives
\[
\limsup_{n\to\infty}n^2\bigl(\text{weight of configurations with at least three parts greater than }K\bigr)
\le C_{m,\alpha}\sum_{j>K}b_j\xrightarrow[K\to\infty]{}0.
\tag{4}
\]
The small parts in the exactly-two contribution have combined limiting weight \((\sum_{j\le K}b_j)^{m-2}\). Letting \(K\to\infty\) proves
\[
\lim_{n\to\infty}n^2T_{n,m}=
\binom m2 p^{m-2}\frac{I(\alpha)}{16\pi}.
\tag{5}
\]

**3. Uniformity in the number of blocks.** For every \(m\ge2\) and every \(n\), the two-large-parts argument above holds with threshold \(\kappa n/m\). Choose those two positions, sum their product over at most \(n\) possible splits, and sum all other part lengths without restriction. This bounds
\[
n^2T_{n,m}\le \binom m2 B^2\kappa^{-3}m^3 p^{m-2}
\le C_\alpha m^5p^{m-2}.
\tag{6}
\]
The bound is summable over \(m\) because \(p=3/4<1\), even though \(m\) is not fixed in (1). Dominated convergence for the nonnegative series gives
\[
\begin{aligned}
\lim_{n\to\infty}\frac{n^2S_n^{(d_n)}}{4^n}
&=\frac{I(\alpha)}{16\pi}\sum_{m\ge2}\binom m2p^{m-2}\\
&=\frac{I(\alpha)}{16\pi(1-p)^3}
=\frac{4I(\alpha)}\pi.
\end{aligned}
\]
For \(\alpha>1/2\), elementary integration yields
\[
I(\alpha)=\frac{4(2\alpha-1)}{\sqrt{\alpha(1-\alpha)}}.
\]
The displayed piecewise limit follows. No Tauberian assertion or interchange of two unproved limiting processes is needed. \(\square\)

## Verification

`CHECKER.py` requires only the Python standard library. Running `python3 CHECKER.py` checks 55 exact published-table entries through dimension ten, 66 independently enumerated finite ordered-composition coefficients, and representative finite-dimensional values on both sides of the phase threshold. It also checks the two-macroscopic-block Riemann-sum constant numerically for three parameter choices. The mathematical conclusion for all dimensions and every fixed real parameter follows from the proof above, not the finite checker.

## Relationship to prior work

Bossinger and Gürdoğan [1] define these polytopes and establish the vertex generating function (their §3.4, Proposition 3.25 and Corollary 3.26). That finite-depth identity is an essential premise, not a new discovery here. Their discussion treats fixed depth and the Catalan endpoint, whereas the present result evaluates the diagonal scale \(d_n=\lfloor\alpha n\rfloor\) and resolves its one-half threshold with an explicit constant. The Pell number case of Bossinger, Telek and Tillmann-Morris [2] corresponds to fixed depth two and is not a linear-depth limit. Calvo Cortes and Frost [3] develop a broader Dyck-path polytope framework; its accessible abstract does not resolve the present quantitative comparison, and its full manuscript was not inspected. Seki [4] proves algebraic irreducibility of finite Catalan generating-function truncations; those polynomials and that property differ from the diagonal coefficient problem. The fewest-big-jumps principle of Kerriou and Mörters [5] concerns sums of a growing number of heavy-tailed random variables under a moving cutoff. It supplies an illuminating analogy for the two-block mechanism; its stated large-deviation model does not supply the geometric-number-of-blocks coefficient identity or the particular polytope constant here. General truncated-renewal estimates may give alternative proofs, but no inspected result was identified that gives the exact diagonal polytope limit without the additional coefficient analysis.

## Limitations

The limit is pointwise in each fixed \(\alpha\in(0,1)\); no uniform estimate as \(\alpha\to0\), \(\alpha\to1/2\), or \(\alpha\to1\) is asserted. The vanishing limit for \(\alpha\le1/2\) does not determine the next nonzero order there. The theorem concerns vertex counts only, not the full face vector, polytope volume, or asymptotic combinatorial equivalence. Bibliographic priority remains subject to unindexed or inaccessible literature, including potential consequences of general renewal estimates. The relationship to general fewest-big-jumps theorems has not been exhaustively resolved, and no independent scientific validation has been performed.

## References

[1] Lara Bossinger and Ömer Gürdoğan, *A combinatorial interpolation between the hypercube and the associahedron*, arXiv:2609.38456v1 (first posted 2026-09-29), §3.4, Proposition 3.25 and Corollary 3.26. https://arxiv.org/html/2609.38456v1

[2] Lara Bossinger, Máté L. Telek and Hannah Tillmann-Morris, *Binary geometries from pellytopes*, Le Matematiche 80 (2025), 189–209. https://lematematiche.dmi.unict.it/index.php/lematematiche/article/view/2739

[3] Veronica Calvo Cortes and Hadleigh Frost, *Dyck Paths, Configuration Spaces and Polytopes For Linear Nakayama algebras*, arXiv:2602.04571 (2026). https://arxiv.org/abs/2602.04571

[4] Shin-ichiro Seki, *Irreducibility of truncations of the Catalan generating function*, arXiv:2609.10526v1 (2026). https://arxiv.org/html/2609.10526v1

[5] Céline Kerriou and Peter Mörters, *The fewest-big-jumps principle and an application to random graphs*, Bernoulli 31 (2025), 2525–2543; arXiv:2206.14627. https://arxiv.org/abs/2206.14627
