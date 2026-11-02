# An unbounded dyadic residue frequency in the first exceptional Lucas recurrence

## Finding
Let \(U_0=0\), \(U_1=1\), and \(U_{n+2}=U_{n+1}+9U_n\) for every integer \(n\ge0\). For a modulus \(m\), let \(\pi(m)\) be the least positive period of the sequence modulo \(m\), and let \(v_m(r)\) count indices \(0\le n<\pi(m)\) for which \(U_n\equiv r\pmod m\). Put \(\Omega(m)=\{v_m(r):0\le r<m\}\).

**Theorem.** For every \(k\ge2\), \(\pi(2^k)=3\cdot2^{k-1}\). There is a uniquely specified \(\tau\in\mathbb Z_2\) and a convergent \(2\)-adic interpolation \(f(t)=U_{6t+3}\) on nonnegative integers satisfying \(f'(\tau)=0\) and
\[
\nu_2(f(t)-f(\tau))=4+2\nu_2(t-\tau)\quad(t\in\mathbb Z_2,\ t\ne\tau).
\]
For every \(k\ge5\), put \(r_k=f(\tau)\bmod2^k\). Then \(r_k\equiv2\pmod4\) and
\[
\boxed{v_{2^k}(r_k)=2^{\lfloor k/2\rfloor}.}
\]
Consequently the set \(\bigcup_{k\ge1}\Omega(2^k)\) is unbounded, and the recurrence is **not stable modulo \(2\)** in the standard sense of eventual constancy of \(\Omega(2^k)\). The assertion is an exact count for a distinguished residue, not a claim that this residue necessarily has maximum frequency.

## Assumptions and scope
The coefficient pair is the fixed natural Lucas pair \((a,b)=(1,9)\), with recurrence \(U_{n+2}=aU_{n+1}+bU_n\). We use \(\mathbb Z_2\) for the ring of \(2\)-adic integers; \(\nu_2(0)=+\infty\). An ordinary nonnegative index is embedded into \(\mathbb Z_2\). The analytic interpolation is constructed explicitly from a matrix logarithm; no analytic interpolation of arbitrary real indices is intended. The theorem applies to all integers \(k\ge5\) for the frequency count and \(k\ge2\) for the shortest period.

## Proof
**1. The companion period.** Let
\[
A=\begin{pmatrix}1&9\\1&0\end{pmatrix},\quad
v_0=\begin{pmatrix}1\\0\end{pmatrix},\quad
v_3=A^3v_0=\begin{pmatrix}19\\10\end{pmatrix}.
\]
Then \(A^nv_0=(U_{n+1},U_n)^T\). Direct exact multiplication gives
\[
A^3=\begin{pmatrix}19&90\\10&9\end{pmatrix},\qquad
A^6=\begin{pmatrix}1261&2520\\280&981\end{pmatrix}
=I+4B,
\quad B=\begin{pmatrix}315&630\\70&245\end{pmatrix}\equiv I\pmod2.
\]
Modulo \(2\), \(A\) has order \(3\); modulo \(4\) it has order \(6\), since \(A^3\not\equiv I\pmod4\), while \(A^6\equiv I\pmod4\). For every \(j\ge0\), binomial induction gives
\[
(A^6)^{2^j}\equiv I+2^{j+2}B\pmod{2^{j+3}}.
\]
Hence \(A^6\) has order \(2^{k-2}\) modulo \(2^k\), so \(A\) has order \(6\cdot2^{k-2}=3\cdot2^{k-1}\) for \(k\ge2\). The scalar sequence has the same least period: if \(A^nv_0=v_0\), then commutation with \(A\) fixes \(Av_0\) as well, and the two vectors \(v_0\) and \(Av_0\) form a basis modulo \(2^k\). Thus \(A^n=I\).

**2. Analytic interpolation and the critical index.** Write \(X=A^6-I=4B\) and use the convergent matrix logarithm and exponential
\[
L=\log(I+X)=\sum_{j\ge1}\frac{(-1)^{j+1}X^j}{j}\in4M_2(\mathbb Z_2),
\qquad E(t)=\exp(tL),\quad t\in\mathbb Z_2.
\]
The \(2\)-adic exponential converges on \(4M_2(\mathbb Z_2)\); the logarithm is its inverse there. Consequently \(E(t)=A^{6t}\) for all nonnegative integers \(t\). Set \(f(t)=(E(t)v_3)_2\), the lower matrix-vector coordinate. It is a \(\mathbb Z_2\)-valued analytic function interpolating exactly \(U_{6t+3}\).

Put \(J=L/4\). Since \(X/4=B\equiv I\pmod2\), the first logarithm term and the valuations of the others give \(J\equiv I\pmod2\). Moreover \(v_3=(19,10)^T\), whose lower coordinate is \(2\pmod4\). Thus for any \(t\in\mathbb Z_2\) and any integer \(j\ge1\),
\[
\nu_2\big((L^jE(t)v_3)_2\big)\ge2j+1.
\]
For \(j=2\), equality always holds: \(J^2\equiv I\pmod4\), \(E(t)\equiv I\pmod4\), so the lower coordinate of \(J^2E(t)v_3\) is \(2\pmod4\). Hence \(\nu_2(f''(t))=5\), for every \(t\).

A needed finite cancellation is verified without a numerical approximation. Since \(X\) is divisible by \(4\), \(L\equiv X-X^2/2\pmod{64}\). For the lower coordinates of these two matrix-vector products one obtains
\[
(Xv_3)_2=15120,\qquad (X^2v_3)_2/2=14288400,
\]
whose difference is divisible by \(64\). Therefore \(f'(0)=(Lv_3)_2\in64\mathbb Z_2\).

Now write the convergent Taylor expansion of \(g(t)=f'(t)/32\) at zero. Its constant term is even, its linear coefficient \(f''(0)/32\) is odd, and every coefficient of \(t^j\) for \(j\ge2\) is even: using the derivative bound above, its valuation is at least
\[
2(j+1)+1-5-\nu_2(j!)=2j-2-\nu_2(j!)\ge1.
\]
These higher coefficients tend to zero in \(\mathbb Z_2\); their sum is a \(2\)-adically \(1\)-Lipschitz function. Thus \(g(t)=c+ut+2H(t)\), with \(c\in2\mathbb Z_2\), \(u\in\mathbb Z_2^\times\), and \(H\) a \(1\)-Lipschitz function. For all \(s,t\in\mathbb Z_2\),
\[
\nu_2(g(t)-g(s))=\nu_2(t-s).
\]
The contraction \(t\mapsto u^{-1}(y-c-2H(t))\) has a unique fixed point for every \(y\in\mathbb Z_2\). In particular there is a **unique** \(\tau\in\mathbb Z_2\) with \(g(\tau)=0\), equivalently \(f'(\tau)=0\).

**3. Exact quadratic contact.** Taylor expansion at \(\tau\) is valid on all of \(\mathbb Z_2\):
\[
f(\tau+h)-f(\tau)
=\frac{f''(\tau)}2h^2+\sum_{j\ge3}\frac{f^{(j)}(\tau)}{j!}h^j.
\]
The quadratic coefficient has valuation precisely \(4\). For every \(j\ge3\), the \(j\)-th coefficient has valuation at least \(2j+1-\nu_2(j!)\ge6\). Indeed these lower bounds exceed the valuation \(4+2\nu_2(h)\) of the quadratic term after multiplication by \(h^j\), for every nonzero \(h\in\mathbb Z_2\). Hence ultrametric noncancellation proves
\[
\nu_2(f(\tau+h)-f(\tau))=4+2\nu_2(h).
\]
Also \(f(\tau)\equiv10\equiv2\pmod4\), because \(E(\tau)\equiv I\pmod4\).

**4. Exact frequency.** For \(k\ge5\), the fundamental period has length \(6\cdot2^{k-2}\). Index positions \(n=6t+3\) in that period are in one-to-one correspondence with \(0\le t<2^{k-2}\). Set \(h_k=\lceil(k-4)/2\rceil\). The contact law says
\[
f(t)\equiv f(\tau)\pmod{2^k}
\quad\Longleftrightarrow\quad t\equiv\tau\pmod{2^{h_k}}.
\]
There are exactly \(2^{k-2-h_k}=2^{\lfloor k/2\rfloor}\) such indices \(t\). No other index class can contribute: modulo \(2\), \(U_n\) is even precisely when \(3\mid n\); when \(n\equiv0\pmod6\), \(U_n\equiv0\pmod4\), since \(A^{6t}\equiv I\pmod4\) and \(U_0=0\). The target \(f(\tau)\) is \(2\pmod4\), so only \(n\equiv3\pmod6\) can attain it. This proves the exact frequency. Since \(2^{\lfloor k/2\rfloor}\to\infty\), eventual constancy of the set \(\Omega(2^k)\) is impossible. \(\square\)

## Verification
The accompanying `VERIFY.py` independently enumerates every residue in complete periods for \(5\le k\le15\), computes the critical index modulo a sufficient power of \(2\) by a discrete approximation to \(f'/32\), and confirms exact frequencies \(2^{\lfloor k/2\rfloor}\). It also verifies the integer matrix identities and their divisibility certificates. The finite checks are supporting evidence; the unrestricted assertions use the valuation and contraction argument above.

## Relationship to prior work
Carlip and Jacobson's 1996 *Fibonacci Quarterly* theorem computes every frequency when the two recurrence coefficients satisfy \(a\) odd and \(b\equiv1\pmod{16}\). Their table marks \(b\equiv9\pmod{16}\) as unresolved and explicitly identifies conjectured nonstability for omitted cases; the coefficient \(b=9\) in the present theorem lies outside their covered family. Their 1996 *Acta Arithmetica* paper concerns arbitrarily late onsets of stability in other parameter families and does not furnish the critical contact law proved here in the accessible descriptive record. Lang and Lang (2013) examine residue completeness of Fibonacci cycles with fixed recurrence and varying initial values, which does not imply the present statement. Bragman and Rowland (2025) determine the density of values of the ordinary Fibonacci sequence; neither this different recurrence nor the unbounded occurrence multiplicities follow from that density.

## Limitations
This theorem proves nonstability for the single natural coefficient pair \((1,9)\), not for every odd pair with \(b\equiv9\pmod{16}\). It identifies one residue with growing exact multiplicity but does not classify all frequencies or the entire image. The research literature may contain an independently obtained equivalent result; independent review has not yet been performed. The historic 1996 paper has publication month verified, but no day-precision public posting date was established; the date-specific archival source anchor used in accompanying metadata is the 2013-04-10 original public preprint by Lang and Lang.

## References
1. W. Carlip and E. Jacobson, *On the Stability of Certain Lucas Sequences Modulo \(2^k\)*, Fibonacci Quarterly **34** (1996), 298–305. https://www.fq.math.ca/Scanned/34-4/carlip.pdf
2. W. Carlip and E. Jacobson, *Unbounded stability of two-term recurrence sequences modulo \(2^k\)*, Acta Arithmetica **74** (1996), 329–346. https://doi.org/10.4064/aa-74-4-329-346
3. C. L. Lang and M. L. Lang, *Fibonacci system and residue completeness*, arXiv:1304.2892v1, first posted 2013-04-10. https://arxiv.org/abs/1304.2892
4. N. Bragman and E. Rowland, *Limiting density of the Fibonacci sequence modulo powers of a prime*, Research in Number Theory **11** (2025), 88, arXiv:2202.00704. https://doi.org/10.1007/s40993-025-00667-1
5. E. Jacobson, *The Distribution of Residues of Two-Term Recurrence Sequences* (1990). https://ijmp.org/wp-content/uploads/2018/05/Distribution_TwoTerm_Recurrence.pdf
