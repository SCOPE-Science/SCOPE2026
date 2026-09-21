# Threshold law for projection constants of block-diagonal graph subspaces

Let \(1\le p<q\le\infty\), put
\[
\delta=\frac1p-\frac1q>0,\qquad r=\delta^{-1},
\]
with \(1/\infty=0\). Let \((E_n)_{n\ge1}\) be nonzero Banach spaces. Write
\[
X_p=\Big(\bigoplus_{n\ge1}E_n\Big)_p,
\]
and let \(X_q=(\bigoplus E_n)_q\) when \(q<\infty\), while \(X_\infty=c_0(E_n)\).

For a scalar sequence \(\lambda=(\lambda_n)\), define the maximal diagonal operator
\[
D_\lambda:\operatorname{Dom}(D_\lambda)\subset X_p\to X_q,\qquad
D_\lambda(x_n)=(\lambda_nx_n),
\]
where
\[
\operatorname{Dom}(D_\lambda)=\{x\in X_p:(\lambda_nx_n)\in X_q\}.
\]
Its graph \(G_\lambda\) is a closed subspace of
\[
Z=X_p\oplus_\infty X_q.
\]

For \(t\ge0\), set
\[
L_\lambda(t)=
\left(\sum_{|\lambda_n|>t}|\lambda_n|^{-r}\right)^{1/r},
\]
with value \(+\infty\) when the series diverges, and define the scalar threshold functional
\[
\Theta(\lambda)=
\inf_{t\ge0}\max\{1,t,L_\lambda(t)\}.
\]
Let
\[
\pi_Z(G_\lambda)=\inf\{\|P\|:P:Z\to G_\lambda\text{ is a bounded projection}\},
\]
with value \(+\infty\) if \(G_\lambda\) is not complemented.

## Main theorem

For every choice of the Banach blocks \(E_n\),
\[
\boxed{\frac12\,\Theta(\lambda)
\le \pi_Z(G_\lambda)
\le 2^{1/p}\Theta(\lambda).}
\]

Consequently,
\[
\boxed{
G_\lambda\text{ is complemented in }X_p\oplus_\infty X_q
\iff
\exists t\ge0:\ 
\big(|\lambda_n|^{-1}\mathbf 1_{\{|\lambda_n|>t\}}\big)_n\in\ell_r.
}
\]

Thus complementability is governed, up to universal constants, by a one-dimensional threshold balance and is independent of the dimensions and internal geometry of the blocks.

## Proof

### 1. A block-multiplier lemma

If \(T_n\in\mathcal B(E_n)\) and
\[
T=\operatorname{diag}(T_n):X_q\to X_p,
\]
then
\[
\|T\|=\big\|(\|T_n\|)_n\big\|_{\ell_r},
\]
with the usual interpretation \(r=p\) when \(q=\infty\).

The upper estimate is Hölder's inequality applied to
\(\|T_nx_n\|\le\|T_n\|\|x_n\|\). For the reverse estimate, take finitely many
indices, choose unit vectors on which \(T_n\) nearly attains its norm, and optimize
the scalar amplitudes. Finite supports also give the \(c_0\) case.

### 2. Explicit threshold projections

Fix \(t\ge0\), let
\[
A=\{n:|\lambda_n|\le t\},\qquad B=\{n:|\lambda_n|>t\},
\]
and suppose \(L_\lambda(t)<\infty\). For \((x,y)\in Z\), define \(P_t(x,y)=(z,D_\lambda z)\) by
\[
z_n=
\begin{cases}
x_n,&n\in A,\\
\lambda_n^{-1}y_n,&n\in B.
\end{cases}
\]
The block-multiplier lemma shows that \(z\in X_p\), and the boundedness of
\(\lambda\) on \(A\) gives \(D_\lambda z\in X_q\). The map \(P_t\) fixes
\(G_\lambda\), hence is a projection onto it.

If \(q<\infty\),
\[
\|z\|_p
\le (1+L_\lambda(t)^p)^{1/p}\|(x,y)\|_Z,
\]
and
\[
\|D_\lambda z\|_q
\le (1+t^q)^{1/q}\|(x,y)\|_Z.
\]
For \(q=\infty\), the second factor is \(\max\{1,t\}\). Hence in every case
\[
\|P_t\|
\le 2^{1/p}\max\{1,t,L_\lambda(t)\}.
\]
Taking the infimum over \(t\) proves the upper bound.

### 3. Every projection yields a reciprocal tail estimate

Suppose \(Q:Z\to G_\lambda\) is a projection with \(\|Q\|=K\).
Simultaneous sign changes on the \(n\)-th copy of \(E_n\) in both \(X_p\) and
\(X_q\) are isometries of \(Z\) preserving \(G_\lambda\). Averaging conjugates
of \(Q\) over signs on the first \(N\) blocks does not increase its norm and
still gives a projection onto \(G_\lambda\). On finitely supported vectors these
averages stabilize as \(N\to\infty\), killing every off-diagonal block. By
density they extend to a block-diagonal projection \(P\) onto \(G_\lambda\)
with \(\|P\|\le K\).

Its \(n\)-th block has the form
\[
P_n(x,y)=
\big(A_nx+B_ny,\,
\lambda_n(A_nx+B_ny)\big),
\]
where \(A_n,B_n\in\mathcal B(E_n)\). Since \(P\) fixes the graph,
\[
A_n+\lambda_nB_n=I_{E_n}.
\]
Applying \(P\) to vectors supported in the first or second ambient summand gives
\[
|\lambda_n|\|A_n\|\le K
\]
for every \(n\), while
\[
\operatorname{diag}(B_n):X_q\to X_p
\quad\text{has norm at most }K.
\]
The block-multiplier lemma therefore yields
\[
\big\|(\|B_n\|)_n\big\|_{\ell_r}\le K.
\]

If \(|\lambda_n|>2K\), then \(\|A_n\|<1/2\), and
\[
|\lambda_n|\,\|B_n\|
=\|I-A_n\|
\ge1-\|A_n\|>\frac12.
\]
Consequently
\[
L_\lambda(2K)\le2K.
\]
Since every nonzero projection has norm at least one,
\[
\Theta(\lambda)\le2K.
\]
Taking the infimum over all \(Q\) proves
\[
\pi_Z(G_\lambda)\ge\frac12\Theta(\lambda).
\]

This also proves the complementability criterion.

## Power weights: a sharp finite-dimensional phase diagram

Take scalar blocks \(E_n=\mathbb K\), \(\lambda_n=n^\alpha\), and
\[
G_{\alpha,N}=
\operatorname{span}\{(e_n,n^\alpha e_n):1\le n\le N\}
\subset \ell_p^N\oplus_\infty\ell_q^N.
\]
Let \(\pi_{\alpha,N}\) be its relative projection constant and retain
\(\delta=1/p-1/q\).

Then, with constants depending only on \(p,q,\alpha\),
\[
\boxed{
\pi_{\alpha,N}\asymp
\begin{cases}
1,&\alpha\le0,\\[2mm]
N^{\min\{\alpha,\delta-\alpha\}},&0<\alpha<\delta,\\[2mm]
(\log(N+1))^\delta,&\alpha=\delta,\\[2mm]
1,&\alpha>\delta.
\end{cases}}
\]

Indeed, the main theorem reduces the problem to minimizing
\[
\max\left\{1,t,
\left(\sum_{\substack{1\le n\le N\\ n^\alpha>t}}
n^{-\alpha r}\right)^{1/r}\right\}.
\]
For \(0<\alpha<\delta\), integral comparison gives a competition between
\(N^\alpha\) and \(N^{\delta-\alpha}\), producing the smaller exponent.
At \(\alpha=\delta\), the reciprocal sum is harmonic, giving the logarithmic
boundary law. For \(\alpha>\delta\), \(\sum n^{-\alpha r}\) is uniformly
summable; for \(\alpha\le0\), the weights are uniformly bounded.

For the corresponding infinite graph,
\[
\boxed{
G_\alpha\text{ is complemented}
\iff
\alpha\le0\ \text{or}\ \alpha>\delta.
}
\]
Thus complementability is re-entrant: bounded weights give a complemented graph,
slow unbounded growth destroys complementability, and sufficiently fast growth
restores it because the inverse tail becomes an \(\ell_r\)-multiplier.

## Relation to classical work

Wojtaszczyk's 1973 paper on complemented subspaces and unconditional bases in
\(\ell_p\oplus\ell_q\), and the Edelstein--Wojtaszczyk direct-sum papers from
1976 and 1978, are classical antecedents for qualitative splitting of
unconditional structure. Albiac and Ansorena later gave a modern finite-direct-sum
classification and explicitly point to the Edelstein--Wojtaszczyk theorem for the
locally convex case.

The scalar qualitative consequences above are therefore adjacent to classical
unconditional-basis theory and are not isolated as the novelty claim. The
contribution claimed here is the quantitative two-sided threshold formula for the
relative projection constant of maximal block-diagonal graphs with arbitrary
Banach blocks, together with the sharp power-weight finite-section rates.

## Limitations

Originality is asserted only to the best of our knowledge. The full texts of the
1973, 1976, and 1978 Studia Mathematica papers were not all inspected in full.
They are the most plausible older sources for an equivalent scalar or qualitative
formulation. Classical monographs on sequence spaces and projection constants
were also not exhaustively checked. No located source stated the block-independent
threshold functional above or the power-weight projection-constant phase diagram.

## References

1. P. Wojtaszczyk, *On complemented subspaces and unconditional bases in
   \(l_p+l_q\)*, Studia Mathematica 47 (1973), 197--206.
   DOI: 10.4064/sm-47-3-197-206.
2. I. Edelstein and P. Wojtaszczyk, *On projections and unconditional bases in
   direct sums of Banach spaces*, Studia Mathematica 56 (1976), 263--276.
   DOI: 10.4064/sm-56-3-263-276.
3. P. Wojtaszczyk, *On projections and unconditional bases in direct sums of
   Banach spaces II*, Studia Mathematica 62 (1978), 193--201.
   DOI: 10.4064/sm-62-2-193-201.
4. F. Albiac and J. L. Ansorena, *Projections and unconditional bases in direct
   sums of \(\ell_p\) spaces, \(0<p\le\infty\)*, Mathematische Nachrichten
   294 (2021), 2052--2062. arXiv:1909.06829; DOI: 10.1002/mana.201900537.
