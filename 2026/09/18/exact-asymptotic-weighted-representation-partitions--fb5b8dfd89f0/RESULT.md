# Exact asymptotics for eventual weighted-representation balance

## Statement

Let \(k>1\) be fixed.  For \(A\subseteq\mathbb N\), where \(\mathbb N=\{0,1,2,\ldots\}\), write
\[
R_{1,k}(A,n)=\#\{(a_1,a_2)\in A^2:n=a_1+ka_2\}
\]
and
\[
D_A(n)=R_{1,k}(A,n)-R_{1,k}(\mathbb N\setminus A,n).
\]
For an integer \(c\), define
\[
N_{k,c}(T)=\#\{A\subseteq\mathbb N:D_A(n)=c\text{ for every }n\ge T\}.
\]

Li, Xu and Yan proved in arXiv:2609.20385v1 that, for fixed \(k>1\) and fixed \(c\),
\[
N_{k,c}(T)\asymp_{k,c}\frac{2^T}{T^{k/2}}.
\]
The following gives the exact first-order asymptotic and a diffusive extension in which the eventual difference may vary with \(T\).

**Theorem.**  Let \((c_T)\) be any integer sequence satisfying
\[
\frac{c_T}{\sqrt T}\longrightarrow \gamma\in\mathbb R.
\]
Then
\[
\boxed{
N_{k,c_T}(T)
\sim
\frac{2^k}{\sqrt{k+3}}
\left(\frac{2k}{\pi}\right)^{k/2}
\exp\!\left(-\frac{2k^2\gamma^2}{k+3}\right)
\frac{2^T}{T^{k/2}}.}
\]

In particular, for every fixed integer \(c\),
\[
\boxed{
N_{k,c}(T)
\sim C_k\frac{2^T}{T^{k/2}},\qquad
C_k=\frac{2^k}{\sqrt{k+3}}
\left(\frac{2k}{\pi}\right)^{k/2}.}
\]
The leading constant is independent of the fixed offset \(c\).

For the function \(f_k(t)=N_{k,0}(t)\) of Yang and Chen this yields
\[
\boxed{f_k(t)\sim C_k\frac{2^t}{t^{k/2}}.}
\]
Consequently, if \(1<k<\ell\), then the comparison sharpened from eventual inequality to
\[
\boxed{
\frac{f_k(t)}{f_\ell(t)}
\sim \frac{C_k}{C_\ell}t^{(\ell-k)/2}.}
\]

Yan and Shan's quantity \(g_{k,m}(t)\), for fixed \(m\ge0\), is the same count with \(c=m+1\) and \(T=mk+t\).  Hence
\[
\boxed{
g_{k,m}(t)
\sim 2^{mk}C_k\frac{2^t}{t^{k/2}}.}
\]

## Proof

The proof starts from the finite sign reduction in Li--Xu--Yan and then evaluates its asymptotic probability sharply.

For \(j\ge0\), set
\[
\varepsilon_j=
\begin{cases}
1,&j\in A,\\
-1,&j\notin A.
\end{cases}
\]
Li--Xu--Yan prove
\[
2D_A(n)=\sum_{j=0}^{q}\varepsilon_j+
\sum_{j=0}^{q}\varepsilon_{kj+s}
\qquad(n=kq+s,\ 0\le s<k),
\]
and also that \(D_A(n)=c\) for all \(n\ge T\) is equivalent to the \(k\) boundary equations at the unique integers \(n_s\in[T,T+k-1]\) with \(n_s\equiv s\pmod k\), together with
\[
\varepsilon_n=-\varepsilon_{\lfloor n/k\rfloor}\qquad(n\ge T+k).
\]
Thus every admissible finite sign vector up to \(T+k-1\) has a unique infinite continuation.

Write
\[
T=kq+r,\qquad 0\le r<k,
\]
and put \(q_s=(n_s-s)/k\), \(Q=\max_s q_s\).  Then
\[
q_s=\begin{cases}q+1,&s<r,\\q,&s\ge r,\end{cases}
\]
when \(r>0\), while all \(q_s=q\) when \(r=0\).  In particular \(Q=\lceil T/k\rceil\).

Following the source notation, let
\[
P_s=\{x:Q<x\le n_s,\ x\equiv s\pmod k\},\qquad M_s=|P_s|.
\]
The union of these sets is exactly
\[
\bigcup_{s=0}^{k-1}P_s=\{Q+1,Q+2,\ldots,T+k-1\}.
\]
Hence the complementary set in the finite boundary system is not merely of size \(T/k+O(1)\), but exactly
\[
C=\{0,1,\ldots,Q\}.
\]
Moreover
\[
M_s=m_0T+O_k(1),\qquad m_0=\frac{k-1}{k^2}.
\]

For \(x\in C\), let
\[
a_{s,x}=\mathbf1_{x\le q_s}+\mathbf1_{x\equiv s\pmod k},
\qquad
S_s=\sum_{x\in C}a_{s,x}\varepsilon_x.
\]
For all but possibly the endpoint \(x=Q\),
\[
a_{s,x}=1+\mathbf1_{x\equiv s\pmod k}.
\]
The boundary equations become
\[
\sum_{x\in P_s}\varepsilon_x=2c_T-S_s,
\qquad 0\le s<k.
\]
The parity condition needed for each Rademacher sum is automatic: Li--Xu--Yan's equation (3.2) gives
\[
2c_T-S_s\equiv M_s\pmod2.
\]

Let
\[
p_M(h)=\Pr(\delta_1+\cdots+\delta_M=h),
\]
where the \(\delta_i\) are independent uniform signs.  Since \(C,P_0,\ldots,P_{k-1}\) partition \(\{0,\ldots,T+k-1\}\), conditioning on the signs in \(C\) gives the exact identity
\[
\boxed{
N_{k,c_T}(T)=2^{T+k}\,
\mathbb E\prod_{s=0}^{k-1}p_{M_s}(2c_T-S_s).}
\tag{1}
\]

Now give the signs \((\varepsilon_x)_{x\in C}\) their uniform product distribution.  The vector
\[
\frac{S}{\sqrt T}=\frac{(S_0,\ldots,S_{k-1})}{\sqrt T}
\]
is a bounded triangular array sum.  Its covariance converges to the matrix
\[
B=\frac1{k^2}\bigl(I+(k+2)J\bigr),
\]
where \(J\) is the all-ones matrix.  Indeed, over each complete block of \(k\) consecutive residues, the diagonal quadratic sum is \(k+3\), while every off-diagonal quadratic sum is \(k+2\); the endpoint contributes only \(O_k(1)\).  The Lindeberg condition is immediate because each summand is bounded.  Therefore
\[
\frac{S}{\sqrt T}\Longrightarrow Z\sim N(0,B).
\tag{2}
\]

On the correct parity class, the local central limit estimate for a Rademacher sum is
\[
p_M(h)=\sqrt{\frac{2}{\pi M}}
\exp\!\left(-\frac{h^2}{2M}\right)(1+o(1))
\tag{3}
\]
uniformly, for example, for \(|h|\le M^{5/8}\).  This follows directly from Stirling's formula applied to
\(2^{-M}\binom{M}{(M+h)/2}\).  A standard binomial bound gives
\[
p_M(h)\ll M^{-1/2}\exp\!\left(-\frac{h^2}{2M}\right)
\]
on the parity class.  Since every \(S_s\) is a sum of bounded independent variables with variance \(O_k(T)\), Hoeffding's inequality shows that the complement of
\(\max_s|S_s|\le T^{5/8}\) has exponentially small probability.  Thus (3) may be inserted into (1) with an \(o(T^{-k/2})\) error in the expectation.

Using \(M_s/T\to m_0\), \(c_T/\sqrt T\to\gamma\), (2), and bounded convergence after the preceding tail estimate, we obtain
\[
T^{k/2}\mathbb E\prod_{s=0}^{k-1}p_{M_s}(2c_T-S_s)
\longrightarrow
\left(\frac{2}{\pi m_0}\right)^{k/2}
\mathbb E\exp\!\left(
-\frac{\|Z-2\gamma\mathbf1\|^2}{2m_0}
\right).
\tag{4}
\]

For a centered Gaussian vector with covariance \(B\),
\[
\mathbb E\exp\!\left(-\frac12(Z-\mu)^T(m_0I)^{-1}(Z-\mu)\right)
=
\det(I+B/m_0)^{-1/2}
\exp\!\left(-\frac12\mu^T(m_0I+B)^{-1}\mu\right).
\]
Here
\[
I+B/m_0=\frac{kI+(k+2)J}{k-1},
\]
so
\[
\det(I+B/m_0)=\left(\frac{k}{k-1}\right)^k(k+3).
\]
Also \(m_0I+B\) has eigenvalue \((k+3)/k\) on the span of \(\mathbf1\).  With \(\mu=2\gamma\mathbf1\), the Gaussian factor in (4) therefore equals
\[
\left(\frac{k-1}{k}\right)^{k/2}\frac1{\sqrt{k+3}}
\exp\!\left(-\frac{2k^2\gamma^2}{k+3}\right).
\]
Because \(m_0=(k-1)/k^2\), (4) simplifies to
\[
\frac1{\sqrt{k+3}}
\left(\frac{2k}{\pi}\right)^{k/2}
\exp\!\left(-\frac{2k^2\gamma^2}{k+3}\right).
\]
Multiplying by the exact factor \(2^{T+k}\) in (1) proves the theorem.

## Verification

`artifacts/verify_exact_counts.py` uses only exact integer arithmetic for the finite sign count.  It first compares the reduced count against direct enumeration of the original \(k\) boundary equations for small instances.  It then computes larger exact counts and compares
\[
N_{k,c}(T)T^{k/2}/2^T
\]
with the predicted constant.  The recorded output shows convergence for \(k=2,3,4\), and also checks the diffusive case \(c_T\approx\frac12\sqrt T\) for \(k=2,3\).  The computation is supporting evidence; the theorem is proved analytically above.

## Relation to prior work and limitations

Li--Xu--Yan, arXiv:2609.20385v1 (submitted 17 September 2026), prove the order of magnitude \(N_{k,c}(T)\asymp_{k,c}2^T/T^{k/2}\) for fixed \(c\).  Their proof reduces the question to the same finite sign system and uses central-binomial upper and lower estimates; it does not state an asymptotic formula or leading constant.  The theorem above evaluates that finite system by a multivariate central limit theorem and a lattice local limit estimate, and it also allows \(c_T\) to move on the natural \(\sqrt T\) scale.

The older weighted-representation literature checked includes Yang--Chen (2012), Qu (2016), Li--Shan--Yan (2024), Chen--Ding--Lü--Zhang (2024), and Yan--Shan (2025).  Those works address existence, structure, growth of representation functions, or exact formulas in bounded parameter ranges rather than the large-\(T\) leading constant here.

Originality is asserted only to the best of our knowledge.  The motivating preprint is extremely recent, so contemporaneous work not yet indexed remains a residual risk.  No inaccessible source was identified whose available metadata specifically suggests the exact constant or the diffusive \(c_T\) extension.

The theorem keeps \(k\) fixed.  It does not provide uniformity as \(k\) grows with \(T\), nor does it treat offsets larger than the diffusive scale covered by \(c_T/\sqrt T\to\gamma\).

## References

1. S.-S. Li, Y.-T. Xu, X.-H. Yan, *A problem of Yang and Chen on weighted representation functions*, arXiv:2609.20385v1 (2026), https://arxiv.org/abs/2609.20385.
2. Q.-H. Yang, Y.-G. Chen, *Partitions of natural numbers with the same weighted representation functions*, J. Number Theory 132 (2012), 3047--3055.
3. Z. Qu, *A note on representation functions with different weights*, Colloq. Math. 143 (2016), 105--112, https://doi.org/10.4064/cm6512-12-2015.
4. S.-S. Li, Y.-Q. Shan, X.-H. Yan, *Partitions of natural numbers and their weighted representation functions*, Bull. Aust. Math. Soc. 110 (2024), 12--18, https://doi.org/10.1017/S0004972723001053.
5. S.-Q. Chen, Y. Ding, X. Lü, Y. Zhang, *Correct order on some certain weighted representation functions*, C. R. Math. 362 (2024), 547--552, https://doi.org/10.5802/crmath.573.
6. X.-H. Yan, Y.-Q. Shan, *Partitions of the set of natural numbers and their weighted representation functions*, Ramanujan J. 67 (2025), Article 53, https://doi.org/10.1007/s11139-025-01113-7.
