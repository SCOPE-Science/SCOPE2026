# Variance-controlled Jordan growth for random-walk momentum polynomials

## Finding

Let \(m\ge3\), and let \(p_0,\ldots,p_m\) satisfy \(p_j\ge0\), \(p_0>0\), \(p_1=0\), \(\sum_{j=0}^m p_j=1\), \(\sum_{j=0}^m jp_j=1\), and \(\sum_{j=3}^m p_j>0\). Define \(P_r(z)=z^r\) for \(0\le r<m\), and for \(n\ge m-1\) define

\[
\sum_{j=0}^m p_j P_{n+1-j}(z)=zP_n(z).
\]

Write \(\sigma^2=\sum_{j=0}^m p_j(1-j)^2\). For every fixed integer \(k\ge1\),

\[
P_n^{(k)}(1)=\frac{n^{2k}}{\sigma^{2k}(2k-1)!!}+O(n^{2k-1}),\qquad n\to\infty.
\]

For the standard Jordan block \(J_q=I+N_q\) of fixed size \(q\ge2\), with ones on the superdiagonal and \(N_q^q=0\), this implies

\[
\|P_n(J_q)\|_2=\frac{n^{2q-2}}{(q-1)!\,\sigma^{2q-2}(2q-3)!!}+O(n^{2q-3}).
\]

Moreover, \(\sigma^2\le m-1\), with equality only for \(p_0=(m-1)/m\), \(p_m=1/m\), and \(p_j=0\) for \(0<j<m\). This endpoint law uniquely minimizes the leading coefficient in the Jordan-block growth formula for every fixed \(q\ge2\).

## Assumptions and scope

The probability constraints are equivalent to a mean-zero integer-valued random variable \(Y\) with \(\mathbb P(Y=1-j)=p_j\). The positive mass on some \(j\ge3\) selects a genuine higher-order recurrence rather than the Chebyshev two-step case. The order \(m\), derivative order \(k\), and Jordan size \(q\) are fixed as \(n\to\infty\). The norm statement uses the Euclidean operator norm and the standard Jordan block.

## Proof

Let \(D_{n,k}=P_n^{(k)}(1)\), with \(D_{n,0}=1\). Differentiating the defining recurrence gives

\[
\sum_{j=0}^m p_jD_{n+1-j,k}=D_{n,k}+kD_{n,k-1}.
\]

Define \((\mathcal L f)_n=\sum_jp_jf_{n+1-j}-f_n=\mathbb E[f(n+Y)-f(n)]\). Since \(\mathbb EY=0\) and \(\mathbb EY^2=\sigma^2>0\), for a polynomial with leading term \(a n^{2k}\),

\[
(\mathcal L f)_n=a\binom{2k}{2}\sigma^2 n^{2k-2}+O(n^{2k-3})
\]

for \(k\ge2\); for \(k=1\), the leading term is the constant \(a\sigma^2\). The recurrence has characteristic equation at \(z=1\) equivalent, after setting \(s=1/r\), to \(G(s)-s=0\), where \(G(s)=\sum_jp_js^j\). The constraints give

\[
G(s)-s=(s-1)^2H(s),\quad H(s)=\sum_{j=2}^mp_j\sum_{\ell=0}^{j-2}(j-1-\ell)s^\ell.
\]

The coefficients of \(H\) are nonnegative and nonincreasing. If \(H(s)=0\) and \(|s|<1\), writing \((1-s)H(s)\) in terms of consecutive coefficient differences and taking absolute values gives \(a_0<a_0\), a contradiction. On \(|s|=1\), \(G(s)=s\) and \(p_0>0\) force \(s=1\), whereas \(H(1)=G''(1)/2=\sigma^2/2>0\). Thus all roots of \(H\) lie strictly outside the unit disk. Equivalently, the recurrence has a double characteristic root at \(r=1\) and all other roots strictly inside the unit disk (zero roots, if present, are also inside).

Consequently, solving the inhomogeneous derivative recurrence produces a polynomial leading term plus bounded decaying modes. Induction on \(k\) now yields \(D_{n,k}=c_kn^{2k}+O(n^{2k-1})\). The case \(k=1\) gives \(c_1=1/\sigma^2\); for \(k\ge2\), comparison of the leading terms gives

\[
c_k\,k(2k-1)\sigma^2=k c_{k-1},\qquad c_k=\frac{1}{\sigma^{2k}(2k-1)!!}.
\]

For \(J_q=I+N_q\), polynomial functional calculus gives \(P_n(J_q)=\sum_{k=0}^{q-1}D_{n,k}N_q^k/k!\). The highest term is \(c_{q-1}n^{2q-2}N_q^{q-1}/(q-1)!\), and \(\|N_q^{q-1}\|_2=1\), proving the stated norm asymptotic.

Finally, \(Y\in[-(m-1),1]\) and \(\mathbb EY=0\). Therefore \((1-Y)(Y+m-1)\ge0\), so taking expectations gives \(\sigma^2\le m-1\). Equality forces \(Y\) to be supported only at the two endpoints. The mean-zero and total-mass constraints then give \(p_0=(m-1)/m\) and \(p_m=1/m\), uniquely. Since the leading Jordan coefficient decreases strictly with \(\sigma^2\), this law is the unique minimizer.

## Verification

The included `verify.py` checks the exact derivative recurrence using rational arithmetic for three admissible distributions, checks the mean/variance constraints, and compares finite first-derivative values with the proved leading coefficient. These finite checks are sanity checks only; the asymptotic result follows from the recurrence and proof above, not from finite experiments.

## Relationship to prior work

Cowal, Marshall, and Pollock introduce this mean-zero random-walk polynomial family, prove boundedness on its stability region and rapid growth past \(1\), and use it in momentum-accelerated power iteration (arXiv:2510.24608, especially the recurrence and Theorem 1.2). Their matrix application assumes a diagonalizable matrix with a simple dominant eigenvalue. The present claim instead differentiates the recurrence at the boundary point and gives the exact fixed-order derivative coefficient and the resulting Jordan-block growth law; neither coefficient is stated in that paper. Miña-Díaz, Rubin, and Wennman study supremum norms and boundary values of Chebyshev/Faber polynomials on curves with corners and cusps (arXiv:2509.22588, Theorems 1–2), not the derivative asymptotic for this recurrence or its Jordan-block consequence. The classical Chebyshev case is excluded by the higher-order assumption here.

## Limitations

The estimates hold for each fixed derivative order and fixed Jordan size; no uniform estimate as \(k\), \(q\), or \(m\) grows is claimed. The Jordan-block result quantifies polynomial amplification and does not assert convergence of a normalized eigenvector iteration for a defective dominant eigenvalue. Related preprints on the deltoid recurrence and on momentum power iteration may contain additional special-case discussion; their full texts were not available in the bounded retrieval attempt, so that remains a stated literature risk rather than a claim of exhaustive novelty.

## References

1. P. Cowal, N. F. Marshall, and S. Pollock, *Random Walks, Faber Polynomials and Accelerated Power Methods*, arXiv:2510.24608 (first public version 2025-10-28).
2. E. Miña-Díaz, O. Rubin, and A. Wennman, *Norms of Chebyshev and Faber Polynomials on Curves with Corners and Cusps*, arXiv:2509.22588 (2025).
3. P. Cowal, N. F. Marshall, and S. Pollock, *Faber Polynomials in a Deltoid Region and Power Iteration Momentum Methods*, arXiv:2507.01885 (related special-case literature; full text not inspected).
4. A. Barletta, N. F. Marshall, and S. Pollock, *Momentum Accelerated Power Iterations and the Restarted Lanczos Method*, arXiv:2511.05364 (related literature; full text not inspected).
