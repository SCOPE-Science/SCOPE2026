# Exact maximal-pattern complexity of periodic-marker extensions of pattern Sturmian words

## Finding

Let \(m\geq2\), let \(x=x_0x_1\ldots\) be a uniformly recurrent binary word with maximal pattern complexity \(p_x^*(k)=2k\) for every integer \(k\geq1\), and let \(w_1,\ldots,w_{m-1}\) be an arbitrary fixed marker template whose letters belong to a finite alphabet disjoint from \(\{0,1\}\). Form the one-sided interleaved word \(y\) by
\[
y_{mj}=x_j,\qquad y_{mj+r}=w_r\quad(1\leq r<m,\ j\geq0).
\]
For a nonempty residue set \(S\subseteq\mathbb Z/m\mathbb Z\), define the **silent-phase signature count**
\[
D_w(S)=\#\Big\{\big(w_{(s+r)\bmod m}\big)_{r\in S}:s\in\mathbb Z/m\mathbb Z,\ 0\notin s+S\Big\}.
\]
Every subscript of \(w\) in this definition is nonzero, because only phases not sampling residue zero are included. Coordinates are ordered by the canonical representatives \(0,\ldots,m-1\) of \(S\). In particular the empty collection of silent phases has count zero.

**Exact all-length theorem.** For every integer \(k\geq1\),
\[
\boxed{\ p_y^*(k)=2k+\max_{\substack{\varnothing\ne S\subseteq\mathbb Z/m\mathbb Z\\ |S|\leq k}}D_w(S).\ }
\]
Thus the entire complexity function, including its finite-length onset, is determined by finite cyclic projections of the marker template; it is independent of which uniformly recurrent binary pattern Sturmian base word is used.

**Sharp four-letter family.** For every \(m\geq3\), use two distinct markers \(A,B\notin\{0,1\}\), choose \(w_1=\cdots=w_{m-2}=A\) and \(w_{m-1}=B\), and retain any base \(x\) satisfying the hypotheses. Then, for *every* integer \(k\geq1\),
\[
\boxed{\ p_y^*(k)=2k+\min\!\left\{k+1,\left\lceil\frac m2\right\rceil\right\}.\ }
\]
Consequently the eventual additive excess \(\lceil m/2\rceil\) is unbounded as \(m\) increases, although every word in the family uses exactly the same four-letter alphabet. It attains this excess for all \(k\geq\lceil m/2\rceil-1\). The case of a single anomalous periodic marker is motivated by measuring how the periodic skeleton, rather than the alphabet size, changes complexity.

## Assumptions and scope

For a word \(z\) over a finite alphabet and any finite nonempty set of nonnegative positions \(T=\{t_1<\dots<t_k\}\), define
\[
F_z(T)=\{(z_{n+t_1},\ldots,z_{n+t_k}):n\geq0\},\qquad p_z(T)=|F_z(T)|,
\]
and \(p_z^*(k)=\sup_{|T|=k}p_z(T)\). Since each \(p_z(T)\) is an integer bounded by the number of \(k\)-letter words over the alphabet, the supremum is attained. Requiring the smallest element of \(T\) to be zero gives the same supremum for the uniformly recurrent words considered here.

The binary alphabet and marker alphabet must be disjoint. The marker positions repeat with the same template at every block of length \(m\). Both symbols of the binary base occur, and the base is uniformly recurrent and pattern Sturmian in the sense \(p_x^*(k)=2k\). Every irrational mechanical Sturmian sequence is an admissible base. The result does not require bounded continued-fraction coefficients, substitutional structure, or a special phase of the Sturmian word. The first formula applies to all templates and all lengths, while the second specifies one natural two-color template family.

## Proof

**Step 1: an exact phase decomposition for every window.** Let \(T\subseteq\mathbb N_0\) be finite and nonempty, and let \(S\subseteq\mathbb Z/m\mathbb Z\) be its set of residues. For every \(r\in S\), set
\[
U_r=\{(t-r)/m:t\in T,\ t\equiv r\pmod m\},\qquad n_r=|U_r|.
\]
Then \(n_r\geq1\) and \(\sum_{r\in S}n_r=|T|\). Group starting indices for \(F_y(T)\) by their residues \(s\pmod m\).

If \(-s\pmod m\) belongs to \(S\), then the sampled vector has binary symbols exactly in the positions of \(T\) with residue \(r=-s\pmod m\); all other coordinates are fixed marker symbols. Writing the starting index as \(ma+s\), its varying binary coordinates are
\[
\bigl(x_{a+u+\varepsilon_{s,r}}\bigr)_{u\in U_r},
\]
where \(\varepsilon_{s,r}\in\{0,1\}\) is the same carry for every \(u\in U_r\). Uniform recurrence guarantees that every finite sampled pattern of \(x\) occurs arbitrarily late; hence shifting all sample indices by \(\varepsilon_{s,r}\) leaves the sampled language unchanged. This active phase contributes exactly \(p_x(U_r)\) words.

Active phases belonging to distinct \(r\)'s cannot produce the same sampled word: the locations containing binary letters differ, and no marker is binary. Active words cannot agree with any word from a silent phase, either. If \(-s\notin S\), all sampled coordinates are constant markers and the phase contributes the single signature \((w_{(s+r)\bmod m})_{r\in S}\). Silent phases may repeat one another; their union has precisely \(D_w(S)\) elements. Therefore there is an *exact identity*, not merely an upper bound:
\[
\boxed{\ p_y(T)=\sum_{r\in S}p_x(U_r)+D_w(S).\ }
\tag{1}
\]
This equation also holds for a uniformly recurrent base with any other known maximal pattern complexity; the value \(2k\) is used only in the next step.

**Step 2: optimize the arbitrary marker template.** From (1) and the base hypothesis,
\[
p_y(T)\leq\sum_{r\in S}2n_r+D_w(S)=2|T|+D_w(S).
\]
Conversely, fix any nonempty \(S\) with \(|S|\leq k\). Choose positive integers \(n_r\) summing to \(k\), and for each \(r\in S\) choose a finite window \(U_r\) of cardinality \(n_r\) satisfying \(p_x(U_r)=2n_r\). Such windows exist by the definition of \(p_x^*\). Define
\[
T=\bigcup_{r\in S}\{mu+r:u\in U_r\}.
\]
It contains exactly \(k\) positions with residue support \(S\), and (1) gives \(p_y(T)=2k+D_w(S)\). Maximizing over \(S\) proves the first boxed formula. If normalization of windows to minimum zero is desired, note that \(y\) is uniformly recurrent: occurrences of a finite block of \(y\) correspond to occurrences of an appropriate finite block of \(x\) at one prescribed phase modulo \(m\), which have bounded gaps. Hence translating a finite window changes no sampled language after the harmless corresponding shift of origin.

**Step 3: count the single-defect marker signatures.** Fix \(m\geq3\), let \(w_{m-1}=B\) and every other marker equal \(A\), and take nonempty \(S\subseteq\mathbb Z/m\mathbb Z\) of size \(t\). Set
\[
b(S)=\#\{r\in S:r+1\notin S\}\quad\text{(cyclic addition modulo }m\text{)}.
\]
In a silent phase, at most one selected residue sees \(B\). For a given \(r\in S\), the pattern with a single \(B\) in coordinate \(r\) occurs in a silent phase precisely when \(r+1\notin S\). These are \(b(S)\) distinct signatures. The all-\(A\) signature occurs exactly when there exists a residue \(u\notin S\) with \(u-1\notin S\), that is, when the complement of \(S\) contains an adjacent cyclic pair. The complement has \(m-t\) sites and exactly \(b(S)\) runs, so such a pair exists if and only if \(m-t>b(S)\). Thus
\[
\boxed{\ D_w(S)=b(S)+\mathbf1_{\{m-t>b(S)\}}.\ }
\tag{2}
\]
The identity includes \(S=\mathbb Z/m\mathbb Z\), for which both sides are zero.

Since \(b(S)\leq\min\{t,m-t\}\), (2) gives the sharp maximum over sets of exactly \(t\) residues:
\[
\max_{|S|=t}D_w(S)=
\begin{cases}
t+1,&1\leq t<m/2,\\
m-t,&m/2\leq t\leq m.
\end{cases}
\tag{3}
\]
For \(t<m/2\), equality is attained by choosing \(t\) pairwise nonadjacent occupied residues. For \(m/2\leq t<m\), choose \(m-t\) pairwise nonadjacent omitted residues; then \(b(S)=m-t\), giving equality. At \(t=m\), (3) is immediate. Maximizing (3) over \(1\leq t\leq\min(k,m)\) yields \(\min\{k+1,\lceil m/2\rceil\}\). Substitution into the first formula proves the second boxed formula and its sharp onset and unbounded-excess assertions.

## Verification

The standalone program `verify_pattern.py` uses Python 3 standard-library integer arithmetic and finite sets. Run `python3 verify_pattern.py`; its expected successful output is:

`VERIFY_OK: 17861 independent finite exact assertions`

Its independently implemented checks enumerate two-color marker templates of block lengths \(2\) through \(6\), all nonempty residue supports, and relevant finite window sizes. They compare direct sampled words over the entire period of a rational mechanical test word with the independently computed phase-signature prediction, including samples that do not maximize the binary base complexity. For the single-defect templates of lengths \(3\) through \(11\), they exhaust all residue subsets, verify (2), check the sharp maximum, and construct attaining windows directly. The mechanical test word has rational slope \(98/257\), so it is **not** an admissible irrational Sturmian base for the universal theorem; it is used only to test finite local identities. Proof of the universal claim is the analytical argument above, not the program's finite calculations.

## Relationship to prior work

Kamae and Zamboni introduced maximal pattern complexity and the binary minimal-growth value \(2k\). Schlortt's *On the structure of sequences with minimal maximal pattern complexity* (arXiv:2505.05627v1, initially public 8 May 2025), Theorem 1.3, proves eventual linearity \(p_y^*(k)=2k+C\) for one pattern Sturmian residue threaded with constant residues, without calculating \(C\) for general templates or the entire function at finite \(k\). Its Sections 5 and 6 and examples already establish some special exact values and the possibility that \(C\) exceeds the elementary alphabet lower bound; those facts are not claimed here as new. The present theorem computes the exact all-length correction from a finite cyclic signature optimization and exhibits its unbounded growth at fixed four-letter alphabet size.

Le, Pavlov and Schlortt, *On subshifts with low maximal pattern complexity* (arXiv:2508.13420v1), Theorem C and Proposition 4.7, give structural descriptions allowing periodic interleavings; these do not specify the marker-template complexity correction. The one-hole Toeplitz complexity framework of Gjini, Kamae, Tan and Xue is related for Toeplitz bases but does not directly subsume the arbitrary irrational Sturmian-base subfamily. An equivalent formula in an earlier specialized word-combinatorics source has not been excluded conclusively.

## Limitations

Disjointness of the binary and marker alphabets, uniform recurrence of the base, and a template constant on every nonbinary residue are essential stated hypotheses. The result does not cover interleavings of several nonconstant residues, markers that share the binary alphabet, or arbitrary nonrecurrent binary bases. The formula identifies exact symbolic pattern counts and does not assert entropy, spectral, or measure-rigidity conclusions beyond those counts. Finite checks neither prove the irrational case nor establish research priority. No independent scientific audit or validation has been performed.

## References

1. Casey Schlortt, *On the structure of sequences with minimal maximal pattern complexity*, arXiv:2505.05627v1 (first posted 8 May 2025), especially Theorem 1.3 and Sections 5–6. https://arxiv.org/html/2505.05627v1
2. Anh N. Le, Ronnie Pavlov and Casey Schlortt, *On subshifts with low maximal pattern complexity*, arXiv:2508.13420v1 (first posted 19 August 2025), especially Theorem C and Proposition 4.7. https://arxiv.org/html/2508.13420v1
3. Teturo Kamae and Luca Q. Zamboni, *Sequence entropy and the maximal pattern complexity of infinite words*, Ergodic Theory and Dynamical Systems 22 (2002), 1191–1199.
4. Nertila Gjini, Teturo Kamae, Bo Tan and Yu-Mei Xue, *Maximal pattern complexity for Toeplitz words*, Ergodic Theory and Dynamical Systems 26 (2006), 1073–1086. https://doi.org/10.1017/S0143385706000150
