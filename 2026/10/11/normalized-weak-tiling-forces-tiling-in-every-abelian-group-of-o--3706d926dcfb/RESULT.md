# Normalized weak tiling forces tiling in every abelian group of order \(16\)
## Finding
Let \(G\) be a finite abelian group of order \(16\). A nonempty set \(A\subseteq G\) has a normalized, nonnegative weak tiling function if and only if it is a genuine translational tile. Precisely,
\[
\exists h:G\to[0,\infty),\quad h(0)=1,\quad
\mathbf1_A*h=\mathbf1_G
\quad\Longleftrightarrow\quad
\exists B\subseteq G,\quad \mathbf1_A*\mathbf1_B=\mathbf1_G.
\]
This conclusion holds in all five abelian groups of order \(16\):
\[
\mathbb Z_{16},\quad \mathbb Z_8\times\mathbb Z_2,\quad
\mathbb Z_4^2,\quad \mathbb Z_4\times\mathbb Z_2^2,\quad \mathbb Z_2^4.
\]
The hypothesis **does not require** \(h\) to be positive definite. Hence each group is pd-flat in the sense of Kiss--Matolcsi--Matolcsi--Somlai. Their study of elementary prime-exponent groups motivates the stronger, complete order-\(16\) classification here, especially the four non-elementary cases.

The enumerated numbers of origin-containing translational tiles, listed at sizes \(1,2,4,8,16\), are:

| Group | \(1\) | \(2\) | \(4\) | \(8\) | \(16\) |
| --- | ---: | ---: | ---: | ---: | ---: |
| \(\mathbb Z_{16}\) | 1 | 15 | 95 | 139 | 1 |
| \(\mathbb Z_8\times\mathbb Z_2\) | 1 | 15 | 183 | 371 | 1 |
| \(\mathbb Z_4^2\) | 1 | 15 | 311 | 387 | 1 |
| \(\mathbb Z_4\times\mathbb Z_2^2\) | 1 | 15 | 359 | 787 | 1 |
| \(\mathbb Z_2^4\) | 1 | 15 | 455 | 1395 | 1 |

Every other nonempty set fails the normalized weak-tiling condition, as certified exactly by the attached program.

## Assumptions and scope
Write finite-group convolution as
\[
(f*g)(x)=\sum_{y\in G}f(x-y)g(y).
\]
All groups are additive. A genuine tile is a set \(A\) with a set \(B\) such that the translates \(A+b\), \(b\in B\), partition \(G\).

A normalized weak tile merely has a nonnegative function \(h\), not assumed integral, with \(h(0)=1\) and \(\mathbf1_A*h=\mathbf1_G\). This is weaker than the positive-definite weak-tiling condition of Reference 1, because no condition on the Fourier transform \(\widehat h\) is imposed. The theorem is restricted to abelian groups of exactly \(16\) elements. In particular it makes no claim for order \(32\), nonabelian groups, or infinite groups.

## Proof
First, a translation of \(A\) preserves the weak-tiling relation and its normalization: if \(a_0\in A\), put \(A'=A-a_0\); then
\[
\mathbf1_{A'}*h(x)=(\mathbf1_A*h)(x+a_0)=1.
\]
Thus it suffices to treat the \(2^{15}\) subsets containing \(0\) in a fixed labeling of each group.

Let \(A\ni0\) be a normalized weak tile. For every \(a\in A\),
\[
1=(\mathbf1_A*h)(a)=\sum_{a'\in A}h(a-a')
\ge h(0)=1.
\]
Nonnegativity shows that every other summand vanishes. Hence
\[
h(t)=0\quad (t\in(A-A)\setminus\{0\}).
\]
Put \(T_A=G\setminus(A-A)\). Any remaining nonzero weight \(h(t)\), apart from \(t=0\), must lie in \(T_A\). For \(x\in G\setminus A\) the convolution identity therefore becomes
\[
\sum_{t\in T_A}\mathbf1_A(x-t)h(t)=1.
\tag{1}
\]

For each of the five groups, form the addition table exactly from its invariant factors. For each \(A\ni0\), compute the forbidden difference set \(A-A\), the allowed shift set \(T_A\), and the translate blocks \(A+t\) for \(t\in T_A\).

There are three exhaustive possibilities. If \(A\) plus all its allowed translates fails to cover \(G\), equation (1) is impossible at an uncovered point. Otherwise check, by enumerating subsets \(B\subseteq T_A\cup\{0\}\) of the necessary size \(|B|=16/|A|\), whether the \(|B|\) translates \(A+b\) partition \(G\); if so \(A\) tiles. In the remaining cases define the \(0\)-\(1\) matrix
\[
M_A(x,t)=\mathbf1_A(x-t),\quad x\in G\setminus A,\ t\in T_A.
\]
The standalone verifier `verify_order16.py` proves
\[
\operatorname{rank}_{\mathbb Q}[M_A\mid\mathbf1]
>
\operatorname{rank}_{\mathbb Q}M_A
\]
for **every** remaining case. The rank test uses fraction-free integer Gaussian elimination, with integer gcd normalization of rows, not floating-point tolerances. Thus (1) has no rational solution. Since both matrix and right-hand side have rational entries, solvability over \(\mathbb R\) would imply solvability over \(\mathbb Q\), a contradiction.

The complete certificate covers exactly
\[
5\cdot2^{15}=163840
\]
subsets containing \(0\). The program's assertions check every case and the terminal record states its precise conclusion; the same run gives the cardinality counts in the table above.

Conversely, if \(A+B=G\) is a genuine tiling, translate \(B\) so that \(0\in B\). Then \(h=\mathbf1_B\) is nonnegative, has \(h(0)=1\), and satisfies \(\mathbf1_A*h=\mathbf1_G\). This proves both directions.

## Verification
Run `python3 verify_order16.py` using a standard Python \(3.9\) or later interpreter. The program is standalone, contains no downloads, external data, third-party package or floating-point operations, and checks all five group operations, all rooted subsets, all legal translates, every tiling witness, and every remaining exact linear obstruction.

As a nontrivial local rank certificate, take \(G=\mathbb Z_{16}\) and
\[
A=\{0,1,2,9\},\quad
T_A=\{3,4,5,6,10,11,12,13\}.
\]
The allowed translates *do* cover \(G\setminus A\), but no genuine tiling exists. On the ordered complement
\[
X=(3,4,5,6,7,8,10,11,12,13,14,15),
\]
consider the integer vector
\[
w=(0,1,-1,-1,2,-1,2,-2,0,1,0,0).
\]
It satisfies \(\sum_{x\in X}w(x)=1\) while for every \(t\in T_A\),
\[
\sum_{a\in A}w(a+t)=0.
\]
Multiplying (1) by \(w\) and summing yields \(1=0\), an exact obstruction. The full checker supplies the analogous exact rank contradictions systematically, including all configurations where simple uncovered-point tests do not suffice.

## Relationship to prior work
Kiss--Matolcsi--Matolcsi--Somlai (Reference 1) introduced normalized positive-definite weak tiling and pd-flatness in finite abelian groups. Their detailed structural results concern elementary \(p\)-groups, with complete classifications in dimensions one and two and partial treatment in dimension three. The present theorem drops Fourier positivity and treats every abelian group of order \(16\), including four non-elementary groups not covered by that elementary-group classification.

The elementary-abelian group \(\mathbb Z_2^4\) had already been addressed by a separate exact weak-tiling census. Its case is **included here as known coverage**, not presented as an independent novelty. The new content is the complete all-isomorphism-type order-\(16\) theorem, notably its four remaining group types and their exact subset counts.

The later work *A lonely weak tile* (Reference 2) constructs a weak pd-tile that fails ordinary tiling in a much larger finite abelian group, illustrating why an exact low-order rigidity result is not tautological. That construction does not imply a claim for groups of order \(16\). Related work on weak tiling in cyclic groups with two distinct prime factors uses a different family of ambient groups and does not establish the present result.

## Limitations
The certificate is exhaustive for abelian groups of order \(16\), not for all finite abelian groups. It uses exact integer rank, but is a computational proof whose exhaustiveness depends on the transparent loop and group-table construction in the supplied standalone checker. It does not claim that the order-\(16\) cutoff is maximal, or that every weak-tiling weight is itself an indicator of a tiling complement. Rather, it proves existence of an indicator complement whenever *some* normalized nonnegative weak tiling exists.

## References
1. G. Kiss, D. Matolcsi, M. Matolcsi and G. Somlai, *Tiling and weak tiling in \((\mathbb Z_p)^d\)*, arXiv:2212.05513v1 (11 December 2022); *Sampling Theory, Signal Processing, and Data Analysis* 22 (2024), article 1, DOI 10.1007/s43670-023-00073-7.
2. G. Kiss, I. Londner, M. Matolcsi and G. Somlai, *A lonely weak tile*, arXiv:2410.04948v1 (7 October 2024); *Expositiones Mathematicae* 44 (2026), article 125636.
3. M. N. Kolountzakis, N. Lev and M. Matolcsi, *Spectral sets and weak tiling*, arXiv:2209.04540v1 (9 September 2022).
