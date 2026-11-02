# Sharp three-state memory creation by Gibbs averaging of exact two-step Markov mixers

## Finding

Let \(P\) range over all nonnegative \(3\times3\) doubly stochastic matrices that are **exactly mixed after two transitions**, \(P^2=\Pi\), where \(\Pi=\frac13\mathbf 1\mathbf 1^{\mathsf T}\). Average the first two states by the Gibbs kernel \(G\) for the partition \(\{\{1,2\},\{3\}\}\), and set \(Q=GPG\). Then there is a real \(\tau\) in the **sharp, fully attainable interval**

\[
\sqrt3-2\ \le\ \tau\ \le\ \frac{\sqrt3-1}{2}
\]

such that for every integer \(m\ge1\),

\[
Q^m=\Pi+\tau^m(G-\Pi),\qquad
\|Q^m-\Pi\|_{F,\pi}^2=|\tau|^{2m},\qquad
\max_i\|Q^m(i,\cdot)-\pi\|_{\mathrm{TV}}=\frac23|\tau|^m,
\]

with uniform stationary distribution \(\pi=(1/3,1/3,1/3)\). The free scalar is exactly \(\tau=(3P_{33}-1)/2\). Every interior value of the interval is attainable by a **strictly positive** transition matrix, and both endpoints are attained by nonnegative transition matrices whose squares are strictly positive. For each integer \(m\ge2\), the exact worst-case squared weighted-Frobenius error is

\[
\sup_{P^2=\Pi}\|(GPG)^m-\Pi\|_{F,\pi}^{2}
=\left(\frac{\sqrt3-1}{2}\right)^{2m},
\]

and the corresponding maximum total-variation error is \(\frac23((\sqrt3-1)/2)^m\). In contrast, \(P^m=\Pi\) for all \(m\ge2\). Thus Gibbs averaging can turn a two-step exact mixer into a chain with a nonzero geometric memory mode. No such nontrivial obstruction exists for doubly stochastic chains on two states.

## Assumptions and scope

All matrices are finite row-stochastic kernels with common uniform invariant law \(\pi\). The equation \(P^2=\Pi\) is required exactly, not approximately; it already implies that the chain is irreducible and aperiodic, because its second transition matrix has strictly positive entries. The Gibbs kernel, its projection, and the weighted quadratic error are

\[
G=\begin{pmatrix}\frac12&\frac12&0\\\frac12&\frac12&0\\0&0&1\end{pmatrix},\quad
\Pi=\begin{pmatrix}\frac13&\frac13&\frac13\\\frac13&\frac13&\frac13\\\frac13&\frac13&\frac13\end{pmatrix},\quad
\|A\|_{F,\pi}^2=\sum_{i,j}\frac{\pi_i}{\pi_j}A_{ij}^2=\sum_{i,j}A_{ij}^2.
\]

For any probability vectors \(\mu,\nu\), \(\|\mu-\nu\|_{\mathrm{TV}}=\frac12\sum_j|\mu_j-\nu_j|\). Both extremal errors maximize over this one nontrivial two-block partition and all eligible three-state \(P\). Permuting state labels gives the same result for any partition of block sizes two and one. No claim is made for nonuniform invariant laws, higher dimensions, or arbitrary partitions.

## Proof

**1. Centered nilpotence and a complete parameterization.** A doubly stochastic \(P\) commutes with \(\Pi\) and preserves the two-dimensional zero-sum subspace. The condition \(P^2=\Pi\) says its restriction to that subspace is nilpotent of index at most two. Consequently \(\operatorname{tr}P=1\) and \(\det P=0\). Conversely, for a doubly stochastic three-state matrix, these two scalar conditions make the restriction have characteristic polynomial \(z^2\); Cayley--Hamilton then gives \((P-\Pi)^2=0\) and \(P^2=\Pi\). Hence the two conditions are equivalent.

Write \(s=P_{33}\), \(r=1-s\), and let \(t=P_{31}+P_{13}\) and \(d=P_{31}-P_{13}\). The row- and column-sum conditions together with \(\operatorname{tr}P=1\) force the exact representation

\[
P=\begin{pmatrix}
r-\frac t2&s+\frac d2&\frac{t-d}{2}\\
s-\frac d2&\frac t2&r-\frac{t-d}{2}\\
\frac{t+d}{2}&r-\frac{t+d}{2}&s
\end{pmatrix}.
\]

Here \(0\le s\le1\). Reading all nine inequalities shows entrywise nonnegativity is precisely

\[
|d|\le2s,\qquad |d|\le\min(t,2r-t)=r-|t-r|.
\]

A direct determinant calculation, independent of stochastic inequalities, gives

\[
\det P=\frac34\left[d^2-(t-r)^2-3\left(s-\frac13\right)^2\right].
\]

Therefore \(\det P=0\) implies

\[
|d|=\sqrt{(t-r)^2+3(s-1/3)^2}\ge\sqrt3\,|s-1/3|.
\]

Together with nonnegativity, this implies the **necessary** inequality

\[
\sqrt3\,\left|s-\frac13\right|\le\min(1-s,2s).
\]

Conversely, for every \(s\in[0,1]\) satisfying that inequality, put \(t=1-s\) and \(d=\sqrt3(s-1/3)\). Then the displayed entry inequalities hold, the determinant vanishes, and the matrix squares to \(\Pi\). Thus the inequality is **sufficient**, not merely necessary. Solving its two linear-piece constraints yields the exact closed interval

\[
\frac{2\sqrt3-3}{3}\ \le\ s\ \le\ \frac1{\sqrt3}.
\]

An explicit extremizing family for every point of this interval is

\[
P(s)=\begin{pmatrix}
\frac{1-s}{2}&s+\frac{d}{2}&\frac{1-s-d}{2}\\
s-\frac d2&\frac{1-s}{2}&\frac{1-s+d}{2}\\
\frac{1-s+d}{2}&\frac{1-s-d}{2}&s
\end{pmatrix},\qquad d=\sqrt3\left(s-\frac13\right).
\]

It has positive entries for all strict interior \(s\), except no exception is necessary at \(s=1/3\), where \(P(s)=\Pi\). At either endpoint some entries equal zero. For every permitted \(s\), the determinant, trace, and stochastic identities established above prove \(P(s)^2=\Pi\).

**2. The compressed eigenmode.** Let \(H=G-\Pi\). The two-block Gibbs projection has exactly one centered direction, hence \(H^2=H\), \(H\Pi=\Pi H=0\), and \(\operatorname{tr}H=1\). Direct block averaging of any doubly stochastic \(P\) yields

\[
GPG=\Pi+\frac{3P_{33}-1}{2}H=\Pi+\tau H.
\]

One way to check the coefficient is to observe that the \((3,3)\) entry of the left side is \(s\), while the same entry on the right is \(1/3+(2/3)\tau\). Projection orthogonality now implies \((\Pi+\tau H)^m=\Pi+\tau^mH\) for every \(m\ge1\).

Because \(H\) is a rank-one orthogonal projection, \(\|H\|_{F,\pi}^2=\operatorname{tr}H=1\). Its third row is \((-1/3,-1/3,2/3)\), with total variation \(2/3\) from zero, while each of the first two rows has variation \(1/3\). Hence the two exact distance formulas follow. Transferring the sharp interval for \(s\) through \(\tau=(3s-1)/2\) gives \([\sqrt3-2,(\sqrt3-1)/2]\). Since \((\sqrt3-1)/2>2-\sqrt3\), its upper endpoint maximizes \(|\tau|\), proving the sharp worst-case formulas at every positive time, and in particular for \(m\ge2\).

**3. Minimality.** Every doubly stochastic two-state matrix has form \(\begin{psmallmatrix}a&1-a\\1-a&a\end{psmallmatrix}\). Its centered eigenvalue is \(2a-1\), so \(P^2=\Pi\) forces \((2a-1)^2=0\), thus \(P=\Pi\). Any Gibbs sandwich of \(\Pi\) remains \(\Pi\). Dimension three is therefore minimal for the stated memory creation.

## Verification

The accompanying standalone `verify.py` uses symbolic exact arithmetic, not floating-point sampling, to check the determinant and Gibbs compression identities, all-parameter extremizing family, both endpoint matrices, projected powers through six steps, two-state rigidity, and 48 additional strictly positive rational two-step mixing examples. Its saved output reports **3,714 passing assertions**. These checks independently catch normalization or algebraic mistakes; the universal interval and all-time conclusions are justified by the preceding elementary inequalities and matrix identities, not by finite testing. Reproduce in an environment with Python 3 and SymPy by executing `python verify.py`.

## Relationship to prior work

Choi and Wang (2026), arXiv:2610.39239v1, introduce the relevant Gibbs partition construction, prove one-step Bregman projection properties without reversibility, and establish their every-time Frobenius improvement theorem **under a reversible ergodic baseline** (Theorem 4.1). Their proof uses self-adjointness when converting singular-value compression into bounds for powers. The current example is intrinsically nonreversible whenever \(\tau\ne0\): a self-adjoint centered matrix whose square is zero must itself be zero. Thus their power inequality does not apply, and in fact is reversed strictly for every \(m\ge2\) in the nontrivial examples.

Choi, Lim and Wang (2025/2026), arXiv:2512.13067v2, develop group averaging and projected chains; their Proposition 3.2 likewise explicitly assumes self-adjointness for a spectral-gap comparison. Their general partition-reduction formalism is compatible with the exact two-block calculation here but does not itself specify the sharp attainable memory spectrum among three-state two-step mixers.

The contribution assessed here is the **complete sharp three-state attainable interval and its exact multi-time error law**, including explicit positive witnesses and the dimension-two obstruction. General one-step compression is a known fact and is not claimed as new.

## Limitations

The result treats only three states with uniform invariant distribution and the one nontrivial Gibbs partition type. It does not assert an increase in every possible mixing metric or under all nonreversible baselines. Although the displayed theorem has a complete elementary proof, earlier stochastic-matrix or lumping literature may contain an equivalent extremal characterization under different terminology; no assertion of definitive historical uniqueness is made. The included symbolic checks are not external or independent mathematical certification.

## References

- Michael C. H. Choi and Youjia Wang, *Bregman projections and partition design for accelerating finite Markov chains*, arXiv:2610.39239v1, first public 2026-10-29. https://arxiv.org/abs/2610.39239 ; relevant Sections 2--4 and Theorem 4.1.
- Michael C. H. Choi, Ryan J. Y. Lim, and Youjia Wang, *Group-averaged Markov chains II: tuning of group action in finite state space*, arXiv:2512.13067v2, first public 2025-12-15. https://arxiv.org/abs/2512.13067 ; relevant Section 3, Proposition 3.2, and partition-reduction discussion.
