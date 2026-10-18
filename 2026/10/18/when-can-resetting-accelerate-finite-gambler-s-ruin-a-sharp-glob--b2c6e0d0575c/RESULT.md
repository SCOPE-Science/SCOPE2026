# When can resetting accelerate finite gambler’s ruin? A sharp global criterion

## Finding

**Theorem (global resetting criterion).** For every pair of integers \(N\ge2\), \(1\le i\le N-1\), let \(T_\gamma\) be the first time a chain, initially at \(i\), hits \(\{0,N\}\). At every transient step independently, with probability \(\gamma\in[0,1)\) the chain resets to \(i\), using one full time step, and otherwise moves \(+1\) or \(-1\) with equal probabilities \((1-\gamma)/2\). Endpoints absorb immediately. Then

\[
\exists\,\gamma\in(0,1):\ \mathbb E T_\gamma<\mathbb E T_0=i(N-i)
\quad\Longleftrightarrow\quad
N^2-5(N-2i)^2+20<0.
\]

If the expression on the right is nonnegative, \(\mathbb E T_\gamma>i(N-i)\) for **every** \(\gamma\in(0,1)\); this is strict even at equality. If it is negative, all sufficiently small positive reset rates help, and a global minimum is attained in \((0,1)\). Thus the familiar infinitesimal-reset sufficient condition is also necessary in this entire finite family: a beneficial isolated intermediate reset rate cannot appear without a beneficial infinitesimal reset.

## Assumptions and scope

All integers \(N,i\) above are included, with no large-population approximation. The resetting decision occurs **instead of** a nearest-neighbor move and consumes one time step. This timing convention differs from a scheme which resets and immediately makes a new jump within the same time step; that distinct protocol is not covered. There is no reset after absorption. All means are finite for \(0\le\gamma<1\); at \(\gamma=1\) the chain never leaves \(i\).

## Proof

**1. Absorption generating function and restart formula.** Let \(T=T_0\), \(q=1-\gamma\) and \(F(q)=\mathbb E[q^T]\). The difference equation \(f_j=q(f_{j-1}+f_{j+1})/2\) for \(1\le j<N\), with \(f_0=f_N=1\), gives

\[
F(q)=\frac{\cosh(\mu\theta)}{\cosh(\nu\theta)},\quad
\nu=N/2,\quad \mu=|N-2i|/2,\quad
\cosh\theta=1/q.
\]

A restart trial succeeds without a reset with probability \(F(q)\). Its expected length, counting the resetting step, is \((1-F(q))/\gamma\). Renewal over independent failed trials therefore gives

\[
M(\gamma):=\mathbb E T_\gamma=
\frac{1-F(q)}{\gamma F(q)}.
\tag{1}
\]

Put \(y=1/q=1+z\), so \(z=\gamma/(1-\gamma)>0\). Let \(s=0\) when \(N\) is even and \(s=1/2\) when \(N\) is odd. Define the polynomials \(A(y),B(y)\) by \(A=T_\nu\), \(B=T_\mu\) for even \(N\), where \(T_j\) is the ordinary Chebyshev polynomial of the first kind. For odd \(N\), define \(P_j=U_j-U_{j-1}\) (Chebyshev second kind, \(U_{-1}=0\)) and take \(A=P_{\nu-1/2}\), \(B=P_{\mu-1/2}\). The half-angle identity for the odd case gives \(F(q)=B(y)/A(y)\). Consequently

\[
M(\gamma)=\frac{(1+z)(A(1+z)-B(1+z))}{z B(1+z)}.
\tag{2}
\]

Write \(\Delta=\nu^2-\mu^2=i(N-i)>0\), \(U=\nu^2-s^2\), \(V=\mu^2-s^2\). Since \(A(1)=B(1)=1\), and \(A'(1)-B'(1)=\Delta\), equation (2) tends to \(\Delta\) as \(z\downarrow0\).

**2. An exact coefficient formula.** Expand \(A(1+z)=\sum_{j\ge0} a_jz^j\) and \(B(1+z)=\sum_{j\ge0}b_jz^j\). Both polynomials have nonnegative coefficients, and \(a_0=b_0=1\). For either parity, their coefficients \(c_j(\lambda)\), evaluated at \(\lambda=\nu\) or \(\mu\), obey

\[
c_0(\lambda)=1,\quad c_1(\lambda)=\lambda^2-s^2,\quad
\frac{c_j(\lambda)}{c_{j-1}(\lambda)}=
\frac{\lambda^2-(j-1+s)^2}{j(2j-1)}\quad(j\ge2),
\tag{3}
\]

for \(j\) through its polynomial degree (thereafter coefficients are zero). This is verified directly from the Chebyshev differential equation, or by induction using \(T_{m+1}=2yT_m-T_{m-1}\) and \(P_{m+1}=2yP_m-P_{m-1}\). In particular \(a_1=U\), \(b_1=V\), \(a_1-b_1=\Delta\).

The sign of \(M(\gamma)-\Delta\) equals the sign of

\[
W(z)=(1+z)(A(1+z)-B(1+z))-\Delta z B(1+z).
\tag{4}
\]

The coefficients of degrees zero and one vanish. Direct substitution of (3) shows that the coefficient of \(z^2\) is

\[
w_2=\frac{\Delta}{6}(\nu^2-5\mu^2+5)=
\frac{\Delta}{24}\bigl(N^2-5(N-2i)^2+20\bigr).
\tag{5}
\]

If \(w_2<0\), equation (4) is negative for all small \(z>0\), proving benefit at small \(\gamma>0\).

**3. The global converse via coefficient positivity.** Suppose \(w_2\ge0\). We prove every coefficient \(w_k\), \(k\ge2\), is nonnegative. If \(B\equiv1\) this follows at once from the nonnegative \(a_j\), since \(w_k=a_k+a_{k-1}\) for \(k\ge2\). Otherwise \(V>0\).

For \(k\ge2\) while \(b_{k-1}>0\), put

\[
R_{k-1}=\frac{a_{k-1}}{b_{k-1}},\qquad
r_\lambda(k)=\frac{\lambda^2-(k-1+s)^2}{k(2k-1)},\qquad
Q_k=\frac{1+\Delta+r_\mu(k)}{1+r_\nu(k)}.
\]

Using (3), \(w_k\ge0\) if and only if \(R_{k-1}\ge Q_k\), because

\[
w_k=(1+r_\nu(k))a_{k-1}-(1+\Delta+r_\mu(k))b_{k-1}.
\tag{6}
\]

Writing \(m_k=2k^2-k-1\) and \(d_k=k^2+k-1\) when \(s=0\), or \(d_k=k^2\) when \(s=1/2\), algebra yields

\[
Q_k=1+\frac{\Delta m_k}{U+d_k}>1.
\tag{7}
\]

Here \(d_k\) is increasing and, for every integer \(k\ge2\), \(m_{k+1}/m_k\le14/5\). Thus

\[
\frac{Q_{k+1}}{Q_k}\le\frac{m_{k+1}}{m_k}\le\frac{14}{5}<3.
\tag{8}
\]

On the other hand, when \(b_k>0\), coefficient formula (3) gives

\[
\frac{R_k}{R_{k-1}}
=\frac{\nu^2-(k-1+s)^2}{\mu^2-(k-1+s)^2}
\ge\frac UV.
\tag{9}
\]

The assumption \(w_2\ge0\) forces \(U/V\ge3\): when \(s=0\), we have \(U\ge5V-5\), and either \((\nu,\mu)=(2,1)\), giving \(U/V=4\), or \(\nu\ge3\), giving \(U/V\ge5U/(U+5)\ge45/14\). When \(s=1/2\), \(U\ge5V-4\), \(V>0\) forces \(U\ge6\), and \(U/V\ge5U/(U+4)\ge3\). The remaining \(N=2\) case has \(B\equiv1\).

At \(k=2\), the base inequality \(R_1\ge Q_2\) is exactly \(w_2\ge0\). By (8)–(9), \(R_k/Q_{k+1}>R_{k-1}/Q_k\) for all subsequent indices at which \(b_k>0\). Hence the coefficient inequality persists inductively. Once \(b_{k-1}=0\), the coefficients of \(B\) at every higher degree also vanish, so \(w_k=a_k+a_{k-1}\ge0\). Thus \(W(z)\ge0\) for all \(z\ge0\). Indeed \(W(z)>0\) for every \(z>0\), because the leading coefficient of \(W\) is positive: \(A\) has strictly greater degree than \(B\). This proves strict worsening at all positive restart probabilities under \(w_2\ge0\), including the equality boundary.

**4. Existence of an interior optimum in the beneficial regime.** When \(w_2<0\), small positive rates improve the mean. As \(\gamma\uparrow1\), \(q\downarrow0\) and \(F(q)\to0\) because \(T\ge1\); equation (1) implies \(M(\gamma)\to\infty\). By continuity and compactness away from the divergent endpoint, a global minimizing rate is attained strictly inside \((0,1)\). This completes the theorem.

## Verification

The included `verify.py` uses exact integer Chebyshev polynomials and rational arithmetic to confirm the sign of the complete polynomial \(W\) for every integer \(2\le N\le60\) and all interior starting positions. Separately, for \(2\le N\le10\), it computes the absorbing-chain fundamental matrix at three rational reset parameters and compares the resulting mean with equation (2). The verification completed 1,905 assertions and reported `PASS`. These finite checks support but do not replace the preceding proof.

## Relationship to prior work

Bonomo–Pal (2021) provide a discrete first-passage renewal framework, but use a restart/jump clock convention different from the consuming-one-step reset considered here. Chen–Li–Huang (2021) study exactly the absorbing-chain reset convention used here and explicitly derive the finite lattice's **sufficient** infinitesimal-reset criterion in their equations (38)–(40). The quadratic threshold in (5) is therefore **not** presented as independently new. The contribution is an exact global converse, showing that neither intermediate reset rates nor the zero-derivative boundary can beat the reset-free mean, via the coefficient comparison (6)–(9). Méndez–Masó-Puigdellosas–Campos (2022) discuss continuum bounded-domain restart criteria; their continuum model does not imply the finite correction or the all-rate discrete theorem. Radice–Cristadoro–Thapa (2024) consider one-sided jump barriers and a different reset/jump-in-one-step convention, not the present finite two-boundary chain. These comparisons are based on inspected primary text and do not constitute a comprehensive historical-priority guarantee.

## Limitations

This theorem addresses expected absorption time only. It does not establish uniqueness of an optimal positive rate, describe conditional splitting times, or treat drifted, lazy, heterogeneous or continuous-time walks. Every reset must cost a complete time step. The result is supported by an analytical proof and finite checking, but has not undergone independent mathematical validation. An equivalent coefficient-positivity theorem under another terminology remains a historical-priority risk.

## References

1. O. L. Bonomo and A. Pal, “First passage under restart for discrete space and time: application to one dimensional confined lattice random walks,” arXiv:2102.00895 (first public version 2021-02-01).
2. H. Chen, G. Li and F. Huang, “First passage in discrete-time absorbing Markov chains under stochastic resetting,” arXiv:2111.01330 (first public version 2021-11-02), particularly equations (31) and (38)–(40).
3. V. Méndez, A. Masó-Puigdellosas and D. Campos, “Non-standard diffusion under Markovian resetting in bounded domains,” arXiv:2201.12043 (first public version 2022-01-28).
4. M. Radice, G. Cristadoro and S. Thapa, “Optimal conditions for first passage of jump processes with resetting,” arXiv:2410.05835 (first public version 2024-10-08).
