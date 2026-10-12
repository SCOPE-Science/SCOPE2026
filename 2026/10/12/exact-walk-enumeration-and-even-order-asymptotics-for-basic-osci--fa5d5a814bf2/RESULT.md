# Exact walk enumeration and even-order asymptotics for basic oscillatory exponent profiles
## Finding
Let \(B_n\) denote the number of distinct nontrivial exponent profiles \((f_1,\ldots,f_{{n-1}})\) of basic \(n\)-by-\(n\) oscillatory matrices. Define \(W_L(h)\) to be the weighted number of length-\(L\) walks in \(\mathbb Z_{{\ge0}}\) that start at height \(h\), with step weights
\[
w(-2)=1,\quad w(-1)=2,\quad w(0)=3,\quad w(1)=2,\quad w(2)=1.
\]
Equivalently,
\[
W_0(h)=1,\qquad W_L(r)=0\text{{ for }}r<0,
\]
and
\[
W_{{L+1}}(h)=W_L(h-2)+2W_L(h-1)+3W_L(h)+2W_L(h+1)+W_L(h+2).
\]
Then for every integer \(m\ge1\),
\[
B_{{2m}}=W_{{m-1}}(0),\qquad
B_{{2m+1}}=2W_{{m-1}}(0)+W_{{m-1}}(1).
\]
The first values are
\[
(B_2,\ldots,B_{{15}})=(1,3,6,20,43,149,331,1169,2645,9447,21626,77816,179579,649589).
\]
For the even subsequence, put
\[
a_r=[u^0](u^{{-1}}+1+u)^{{2r}}.
\]
Its exact generating function is
\[
\sum_{{L\ge0}}W_L(0)t^L=(1-9t)^{{-1/2}}
\exp\!\left(\frac12\sum_{{r\ge1}}\frac{{a_r}}r t^r\right).
\]
In particular,
\[
B_{{2m}}\sim
\frac{{3\sqrt{{2-\sqrt3}}}}{{\sqrt{{\pi(m-1)}}}}\,9^{{m-1}}
\qquad(m\to\infty).
\]

## Assumptions and scope
Matrices are real and basic oscillatory in the standard sense used by Xie: their successive elementary bidiagonal factorization has exactly one positive factor at each adjacent index on each triangular side. The exponent profile records, for each nontrivial minor order \(k\), the least positive power for which all \(k\)-minors are positive. The statement counts distinct profiles, not factor orders or matrices realizing them.

The algebraic input is Xie's characterization of basic profiles. The probabilistic input is the classical Sparre--Andersen factorization for one-dimensional random walks. The finite values listed above are consequences of the exact recurrence; the asymptotic is not inferred from a finite census.

## Proof
Xie's Theorem 3.12 says that a positive integer vector \(f=(f_1,\ldots,f_{{n-1}})\) is a basic exponent profile exactly when
\[
f_k\le\max\{{k,n-k\}},\qquad |f_{{k+1}}-f_k|\le1,\qquad f_k+f_{{n-k}}\ge n.
\]
Its converse proof canonically constructs two symmetric basic profiles \(a,b\). On the left half, for \(k<n-k\),
\[
a_k=f_k,\qquad b_k=n-f_{{n-k}},
\]
and the complementary entries are fixed by \(a_k+a_{{n-k}}=b_k+b_{{n-k}}=n\). The inequality above is exactly \(a_k\ge b_k\) on the left half, and \(f=\max\{a,b\}\). Conversely, any such ordered pair of symmetric profiles determines \(f\) uniquely, because the left half recovers \(a\) and the reflected right half recovers \(b\).

For \(n=2m\), both symmetric profiles have central value \(m\). Read their left halves outward from the center and set the height to their difference. Each symmetric profile changes at each step by one of \(-1,0,1\); hence the height increment is a difference of two such steps. The five possible increments \(-2,-1,0,1,2\) occur with multiplicities \(1,2,3,2,1\), respectively. The order condition \(a_k\ge b_k\) is exactly nonnegativity of the height. This gives a weight-preserving bijection with the walks counted by \(W_{{m-1}}(0)\).

For \(n=2m+1\), the central pair \((f_m,f_{{m+1}})\) can only be
\[
(m,m+1),\quad(m+1,m),\quad(m+1,m+1).
\]
The corresponding initial differences \(a_m-b_m\) are \(0,0,1\). The same outward construction therefore gives two copies of walks starting at height \(0\) and one copy starting at height \(1\), proving the odd formula.

For the generating function, normalize the five step weights by \(9\). Let \(S_j\) be the resulting symmetric random walk starting at \(0\). Then
\[
W_L(0)=9^L\Pr(S_1\ge0,\ldots,S_L\ge0).
\]
The Sparre--Andersen factorization gives
\[
\sum_{{L\ge0}}\Pr(S_1\ge0,\ldots,S_L\ge0)s^L
=\exp\left(\sum_{{r\ge1}}\frac{{\Pr(S_r\ge0)}}r s^r\right).
\]
Symmetry yields
\[
\Pr(S_r\ge0)=\frac12\left(1+\Pr(S_r=0)\right),
\qquad
\Pr(S_r=0)=\frac{{a_r}}{{9^r}},
\]
which gives the displayed generating function after setting \(s=9t\).

To evaluate its dominant constant, the characteristic function of one normalized step is
\[
\phi(\theta)=\left(\frac{{1+2\cos\theta}}3\right)^2.
\]
Thus
\[
\sum_{{r\ge1}}\frac{{\Pr(S_r=0)}}r
=-\frac1{{2\pi}}\int_{{-\pi}}^\pi\log(1-\phi(\theta))\,d\theta.
\]
Because
\[
1-\phi(\theta)=\frac49(1-\cos\theta)(2+\cos\theta),
\]
the standard logarithmic cosine integrals give
\[
\frac1{{2\pi}}\int_{{-\pi}}^\pi\log(1-\phi(\theta))\,d\theta
=\log\left(\frac{{2+\sqrt3}}9\right).
\]
Hence the analytic factor at the dominant singularity contributes
\[
\exp\left(\frac12\sum_{{r\ge1}}\frac{{\Pr(S_r=0)}}r\right)
=3\sqrt{{2-\sqrt3}}.
\]
The usual coefficient transfer for a \((1-s)^{{-1/2}}\) singularity gives the stated even-order asymptotic.

## Verification
The symbolic proof above establishes the infinite statement. The accompanying `verify.py` is only a finite regression check: it independently enumerates all vectors satisfying Xie's three conditions through order \(9\), compares them with the weighted-walk recurrence, checks the listed recurrence values through order \(15\), and verifies the algebraic value of the dominant constant numerically. It terminates with `CHECK_OK`.

## Relationship to prior work
Xie's 2026 paper proves the complete if-and-only-if characterization of basic exponent profiles and, separately, counts the symmetric basic profiles: for order \(2m\) the symmetric count is \(3^{{m-1}}\), and for order \(2m+1\) it is \(2\cdot3^{{m-1}}\). The paper does not give an enumeration of all nonsymmetric basic profiles, a walk model for that count, or the asymptotic constant above. Its proof of Theorem 3.12 supplies the canonical pair of symmetric profiles used here.

Xie's earlier 2026 paper develops minor-order exponent profiles and characterizes them through triangular factor orders, but the inspected abstract does not provide this all-basic-profile enumeration or asymptotic. Older work on basic oscillatory matrices concerns factorization, exponents, and structural containment rather than the enumerative invariant isolated here. The random-walk step uses the classical Sparre--Andersen factorization, not a new probability theorem.

## Limitations
The result counts profile vectors only; it does not count matrices or factor orders realizing each vector. The odd-order exact recurrence is proved, but no odd-order asymptotic constant is claimed here. The originality claim is confined to the walk enumeration, generating function, and even-order asymptotic extracted from the recent profile classification; the classification itself is due to Xie.

## References
1. Wei Xie, *Exponent Profiles of Oscillatory Matrices under Matrix and Inverse Sparsity*, arXiv:2609.35846v1, 2026. In particular Corollary 3.10 and Theorem 3.12.
2. Wei Xie, *Minor-Order Exponent Profiles of Oscillatory Matrices*, arXiv:2609.05787v1, 2026.
3. Achi Brandt, *A Generalization of a Combinatorial Theorem of Sparre Andersen About Sums of Random Variables*, Mathematica Scandinavica 9 (1961), 352--358, DOI:10.7146/math.scand.a-10640.
