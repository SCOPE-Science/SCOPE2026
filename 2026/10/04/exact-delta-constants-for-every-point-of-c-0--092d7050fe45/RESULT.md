# Exact \(\Delta\)-constants for every point of \(c_0\)
## Finding
For every real \(x=(x_i)\in B_{c_0}\), set
\[
\Phi_x(r)=\sum_{\{i:\ |x_i|>r-1\}}\frac{1-|x_i|}{r+1-|x_i|},\qquad 1\le r\le2,
\]
where an infinite sum is interpreted in \([0,+\infty]\). Then
\[
\boxed{\ \delta c(x)=\inf\{r\in[1,2]:\Phi_x(r)\le1\}\ }.
\]
The feasible set is nonempty because \(r=1+\|x\|_\infty\) makes the active set empty. For every \(r>1\), the active set is finite because \(x\in c_0\).

A genuinely heterogeneous example is
\[
x=\left(\frac34,\frac14,\frac14,0,\ldots\right),\qquad
\delta c(x)=\frac{3+\sqrt{33}}8\approx1.093070330817.
\]
For the infinite-support vector \(x_i=1/i\), the same formula gives \(\delta c(x)=5/4\): immediately below \(5/4\) the fourth coordinate is active and the active sum exceeds \(1\), while at \(5/4\) that coordinate drops out.

## Assumptions and scope
The scalar field is real, matching the setup of Choi and Jung. The pointwise \(\Delta\)-constant is the quantitative invariant from their Definition 2.1. Equivalently,
\[
\delta c(x)=\inf_{S\ni x}\sup_{y\in S}\|x-y\|_\infty,
\]
where the infimum runs over slices \(S\) of \(B_{c_0}\) containing \(x\).

Coordinatewise sign changes are surjective linear isometries of \(c_0\), so it is enough to prove the formula for \(x_i\ge0\). Write \(d_i=1-x_i\).

## Proof
Fix a slice
\[
S(a,\delta)=\{y\in B_{c_0}:a(y)>1-\delta\},\qquad a\in S_{\ell_1},
\]
containing \(x\), and let
\[
R=\sup_{y\in S(a,\delta)}\|x-y\|_\infty.
\]
First, \(R\ge1\). Indeed, the inequality \(a(x)>1-\delta\) has positive slack. Since \(a_i\to0\), one may change a sufficiently remote zero coordinate of \(x\) to a sign of modulus \(1\) while keeping the point in the slice.

Let
\[
I_R=\{i:x_i>R-1\}.
\]
For every \(i\in I_R\), one must have \(a_i>0\). If \(a_i\le0\), a finitely supported sign vector can approximate the norm of \(a\) while having its \(i\)-th coordinate equal to \(-1\), producing a point of the slice at distance \(1+x_i>R\), a contradiction.

Set \(q=1-a(x)\). Then \(0\le q<\delta\), and
\[
q=\sum_j\bigl(|a_j|-a_jx_j\bigr)\ge\sum_{i\in I_R}a_i d_i.
\]
For \(i\in I_R\), we also have
\[
a_i(R+d_i)\ge\delta.
\]
Otherwise, for a sufficiently small \(\varepsilon>0\), fix the \(i\)-th coordinate at \(x_i-R-\varepsilon>-1\) and choose finitely many other coordinates with the maximizing signs of \(a\). This gives a point in the slice whose distance from \(x\) is larger than \(R\), contradicting the definition of \(R\).

If \(q>0\), every finite \(F\subset I_R\) therefore satisfies
\[
q\ge\sum_{i\in F}a_i d_i
>q\sum_{i\in F}\frac{d_i}{R+d_i}.
\]
Taking the supremum over finite \(F\) gives \(\Phi_x(R)\le1\). If \(q=0\), the displayed lower bound for \(q\) forces \(d_i=0\) on every active coordinate, so again \(\Phi_x(R)=0\). Thus every slice radius \(R\) is feasible, proving
\[
\delta c(x)\ge\inf\{r\in[1,2]:\Phi_x(r)\le1\}.
\]

For the reverse inequality, fix a feasible \(r\). Put
\[
I=\{i:x_i>r-1\},\qquad b_i=\frac1{r+d_i}\quad(i\in I),\qquad
\Phi=\sum_{i\in I}b_i d_i\le1.
\]
The set \(I\) is finite unless \(r=1\); if \(r=1\) and \(\Phi\le1\), it is finite as well because nonzero coordinates of a \(c_0\)-vector tend to zero and each additional small nonzero coordinate contributes asymptotically \(1/2\). If \(I\) is empty, the whole unit ball already lies within distance \(r\) of \(x\).

Assume \(I\ne\varnothing\). Define
\[
q=\frac1{1+\sum_{i\in I}b_i x_i},\qquad
a_i=qb_i\quad(i\in I).
\]
Put \(a_k=q(1-\Phi)\) on one coordinate \(k\notin I\), and set all remaining coefficients to zero. If \(1-\Phi>0\), choose \(k\) so far in the tail that \(x_k<1\); this is always possible because \(x_k\to0\). The normalization identity
\[
\sum_{i\in I}a_i+a_k
=q\left(1+\sum_{i\in I}b_i x_i\right)=1
\]
shows \(a\in S_{\ell_1}\). Writing \(\tau=a_kx_k\), we have \(0\le\tau<q\) and
\[
a(x)=1-q+\tau.
\]
(The case \(a_k=0\) simply has \(\tau=0\).)

For \(\eta>0\), the slice \(S(a,q-\tau+\eta)\) contains \(x\). If \(y\) lies in this slice, then for every active \(i\),
\[
a(y)\le1-a_i(1-y_i)
\]
implies
\[
y_i>x_i-r+\frac{\tau-\eta}{a_i}.
\]
Hence \(x_i-y_i<r+(\eta-\tau)/a_i\le r+\eta/a_i\). Positive deviations on active coordinates are at most \(d_i\le1\le r\). On inactive coordinates, \(x_j\le r-1\), so even \(y_j=-1\) gives \(|x_j-y_j|\le r\); tail deviations are at most \(1\). Therefore the slice radius is at most \(r+C\eta\), with \(C<\infty\) because \(I\) is finite. Letting \(\eta\downarrow0\) gives \(\delta c(x)\le r\). Taking the infimum over feasible \(r\) proves the formula for arbitrary \(x\in B_{c_0}\), with no finite-support hypothesis.

## Verification
For the known equal-coordinate family \(x=t\sum_{k=1}^n e_k\), the active sum below the jump \(r=1+|t|\) is
\[
\Phi_x(r)=\frac{n(1-|t|)}{r+1-|t|}.
\]
Consequently the formula reduces to
\[
\delta c\left(t\sum_{k=1}^n e_k\right)
=\min\{1+|t|,\max\{1,(n-1)(1-|t|)\}\},
\]
which is exactly the family computed in Choi--Jung, Remark 3.4(3).

For \(x=(3/4,1/4,1/4,0,\ldots)\), all three nonzero coordinates are active at the interior root and
\[
\frac{1/4}{r+1/4}+2\frac{3/4}{r+3/4}=1,
\]
so \(r=(3+\sqrt{33})/8\), verifying the stated heterogeneous example algebraically.

The accompanying `verify_delta_c0_formula.py` uses only the Python standard library. It checks \(77\) equal-coordinate cases, the exact heterogeneous value, the threshold \(5/4\) on long harmonic prefixes, the constructive slice-functional radius on heterogeneous vectors, and ten deterministic numerical searches over competing positive slice functionals. These computations are consistency checks; the infinite-dimensional statement rests on the proof above.

## Relationship to prior work
Choi and Jung introduced the quantitative pointwise \(\Delta\)-constant and studied \(c_0\) in Section 3.1 of arXiv:2307.10647. Their Proposition 3.2 computes the Daugavet constant on \(c_0\), Theorem 3.3 supplies lower bounds for the \(\Delta\)-constant, and Remark 3.4(3) gives the exact equal-coordinate finite-support family. Their text also emphasizes that exact \(\Delta\)-constant calculations are substantially harder than the Daugavet-constant calculation. The formula here supplies an exact value for every point of \(B_{c_0}\) and contains their equal-coordinate formula as a special case.

Abrahamsen, Lima, Martiny, and Perreau studied almost \(\Delta\)-points and asymptotic geometry in arXiv:2203.14528; in particular their Section 6 provides the background that \(c_0\) admits almost \(\Delta\)-points although it has no \(\Delta\)-points. The present result is quantitative and pointwise rather than an existence statement.

Targeted semantic searches for exact \(c_0\) \(\Delta\)-constant formulas, active-coordinate descriptions, and variants of the displayed sum found no statement implying the formula above. This is evidence of noncoverage, not a proof of bibliographic novelty.

## Limitations
The argument is for real \(c_0\), as in the cited definition. It does not assert the corresponding formula for finite-dimensional \(\ell_\infty^N\); the fresh tail coordinates of \(c_0\) are essential to the upper construction and to the universal lower floor \(R\ge1\). It also does not address complex scalars or other Banach sequence spaces.

Bibliographic searches cannot exclude every unindexed or newly posted source. The novelty conclusion therefore remains subject to ordinary literature verification.

## References
1. G. Choi and M. Jung, *The Daugavet and Delta-constants of points in Banach spaces*, arXiv:2307.10647, first posted 2023-07-20, revised 2024-06-24; related DOI 10.1017/prm.2024.83.
2. T. A. Abrahamsen, V. Lima, A. Martiny, and Y. Perreau, *Asymptotic geometry and Delta-points*, arXiv:2203.14528, first posted 2022-03-28.
