# Complete dyadic modular-hyperbola two-sum fibers and Kloosterman fourth moments

## Finding
For every integer \(k\ge 2\), put \(N=2^k\), \(U=(\mathbb Z/N\mathbb Z)^\times\), and
\[
H_k=\{(x,x^{-1}):x\in U\}\subseteq(\mathbb Z/N\mathbb Z)^2.
\]
Let \(R_k(s,z)\) count **ordered** pairs of points in \(H_k\) with vector sum \((s,z)\). The following rules determine **every** multiplicity, including all zeros.

If \(s=0\), then \(R_k(0,0)=2^{k-1}\) and \(R_k(0,z)=0\) for \(z\ne0\). If \(s\) is odd, or \(s\ne0\) is even but \(\nu_2(s)\ne\nu_2(z)\), then \(R_k(s,z)=0\). For nonzero even \(s\), put \(a=\nu_2(s)\in\{1,\ldots,k-1\}\) and \(m=k-a\). When \(\nu_2(z)=a\), write \(u=s/2^a\) and \(v=z/2^a\) as odd units modulo \(2^m\); let
\[
d=(s/2)^2-u v^{-1}\pmod{2^m}.
\]
Then the exact answer is
\[
\boxed{R_k(s,z)=2^a\rho_m(d)},\qquad
\rho_m(d)=\#\{w\in\mathbb Z/2^m\mathbb Z:w^2=d\}.
\]
This is explicit without any root-solving oracle: if \(d=0\) modulo \(2^m\), then \(\rho_m(d)=2^{\lfloor m/2\rfloor}\). Otherwise write \(d=2^{2j}e\) with \(e\) odd and \(2j<m\); if \(\nu_2(d)\) is odd, the count is zero. For even valuation, put \(\ell=m-2j\). Then
\[
\rho_m(d)=2^j\begin{cases}
1,&\ell=1,\\
2,&\ell=2\ \text{and}\ e\equiv1\pmod4,\\
4,&\ell\ge3\ \text{and}\ e\equiv1\pmod8,\\
0,&\text{otherwise}.
\end{cases}
\]

For \(a\ge2\), this specializes to a particularly simple **complete local fiber spectrum**: if \(m\ge3\), exactly \(2^{m-3}\) values of \(z\) have multiplicity \(2^{a+2}\), all others being zero; if \(m=1,2\), exactly one value of \(z\) has multiplicity \(2^{k-1}\). For \(a=1\), the displayed even-square root rule resolves the multiple dyadic fiber levels. In particular, the number of nonzero fibers for each \(s\) of valuation one is exactly
\[
L_m=1+\sum_{j=1}^{\lfloor(m-1)/2\rfloor}b_{m-2j},\qquad
b_1=b_2=1,\quad b_\ell=2^{\ell-3}\ (\ell\ge3),\qquad m=k-1.
\]
For \(k\ge4\), the two-point Minkowski sumset consequently has cardinality
\[
\boxed{|H_k+H_k|=\frac{4^{k-3}+8}{3}+2^{k-2}L_{k-1}}.
\]
For \(k=2,3\), the sumset sizes are \(2\) and \(4\), respectively.

The additive energy \(E(H_k)=\sum_{s,z}R_k(s,z)^2\) is exactly
\[
\boxed{E(H_k)=\begin{cases}8,&k=2,\\64,&k=3,\\6(k-3)2^{2k-2},&k\ge4.\end{cases}}
\]
If \(K_N(u,v)=\sum_{x\in U}\exp(2\pi i(ux+vx^{-1})/N)\), the **joint two-parameter** Kloosterman fourth moment is therefore
\[
\boxed{\sum_{u,v\bmod N}|K_N(u,v)|^4=N^2E(H_k).}
\]
With normalized Fourier synthesis \(\mathcal E\mathbf1=K_N/|U|\), counting measure on the two-dimensional frequency group yields \(\|\mathcal E\mathbf1\|_{\ell^4}^4=8,16,24(k-3)\) in the three cases \(k=2\), \(k=3\), and \(k\ge4\), respectively.

## Assumptions and scope
The coefficient ring is exactly \(\mathbb Z/2^k\mathbb Z\), \(k\ge2\), and the parameter on the hyperbola ranges over all odd units. A residue's valuation \(\nu_2\) is taken to be its integer representative's valuation truncated at \(k\), with \(\nu_2(0)=k\). Quotients by powers of two in the statement are uniquely interpreted in the indicated smaller residue ring. The result is an exact unweighted two-sum census and its constant-input Fourier consequence; it does not assert a sharp extension bound for arbitrary weights.

## Proof
**Step 1 (fiber reduction).** Writing \(y=s-x\), both \(x\) and \(y\) are units if and only if \(s\) is even and \(x\) is odd. The inverse-coordinate sum satisfies
\[
x^{-1}+y^{-1}=\frac{s}{xy}.
\]
For \(s=0\) every pair has inverse-coordinate sum zero. For nonzero even \(s\), the valuation of \(z\) must be \(a=\nu_2(s)\) because \(xy\) is a unit. Dividing \(z=s/(x(s-x))\) by \(2^a\) makes the equation equivalent to \(x(s-x)=uv^{-1}\) modulo \(2^{m}\), \(m=k-a\). Since \(s\) is even, completing the square in the integer ring gives
\[
x(s-x)=(s/2)^2-(x-s/2)^2.
\]
Each admissible \(x\bmod2^m\) has exactly \(2^a\) odd lifts modulo \(2^k\). If \(a=1\), then \(s/2\) is odd, the required square root is even, and the right-hand side is even; if \(a\ge2\), \(s/2\) is even, the required square root is odd, and the right-hand side is odd. Thus **every** square root counted by \(\rho_m\) has the required parity. This proves \(R_k(s,z)=2^a\rho_m(d)\), including \(m=1\).

**Step 2 (square-root census).** A residue divisible by an odd power of two cannot be a square. For \(d=0\), a square root must be divisible by \(2^{\lceil m/2\rceil}\), giving \(2^{\lfloor m/2\rfloor}\) roots. For \(d=2^{2j}e\) with \(e\) odd, dividing a root by \(2^j\) reduces to an odd square modulo \(2^{m-2j}\), with \(2^j\) lifts. An odd number has one square root modulo \(2\); modulo \(4\) the square residues are exactly \(1\) with two roots; modulo \(2^\ell\) for \(\ell\ge3\), the odd squares are exactly the residues \(1\pmod8\), each having four roots (the squaring map on the unit group has kernel of size four). This proves the stated complete formula. When \(a\ge2\), odd-square counts give the simplified local spectrum. When \(a=1\), even-square residues are precisely zero and those with valuation \(2j\ge2\), giving \(L_m\). Summing the resulting nonzero-fiber counts over the \(2^{m-1}\) choices of \(s\) in each valuation stratum gives the displayed Minkowski sum cardinality.

**Step 3 (energy by independent collision counting).** Write \(n=|U|=2^{k-1}\). Two pairs with the same first sum \(s\) and inverse sum are equivalent to \(x(s-x)\equiv x'(s-x')\pmod{2^m}\). Put \(s=2t\) and \(x'=x+2h\). Their product difference is
\[
x(s-x)-x'(s-x')=-4h(t-x-h).
\]
For \(a\ge2\), \(t-x\) is odd. If \(m\ge3\), the condition \(2^{m-2}\mid h(t-x-h)\) holds exactly when \(h\equiv0\) or \(h\equiv t-x\pmod{2^{m-2}}\), two disjoint residue classes. The collision probability for uniformly chosen \(x,x'\in U\) is \(2^{3-m}\). For \(m=1,2\), it is one. There are \(2^{m-1}\) first-coordinate sums of valuation \(a\). Thus each \(a\) from \(2\) through \(k-3\) contributes \(4n^2\) to energy, and the last two strata together contribute \(3n^2\).

For \(a=1\), \(t-x\) is even. When \(k\ge4\), the collision condition first forces \(h\) even, say \(h=2\ell\), \(t-x=2c\). For \(k=4\) the remaining condition is automatic, hence probability \(1/2\). For \(k\ge5\), the condition becomes \(2^r\mid\ell(c-\ell)\) with \(r=k-5\). Uniform independent \(c\) and \(\ell\) give
\[
\Pr(2^r\mid\ell(c-\ell))
=\sum_{j=0}^{r-1}2^{-j-1}2^{-(r-j)}+2^{-r}
=\frac{r+2}{2^{r+1}}.
\]
The preliminary evenness condition contributes a factor \(1/2\), so for all \(k\ge4\) the collision probability is \((k-3)/2^{k-3}\). Since there are \(2^{k-2}\) values of \(s\) with valuation one, their total energy contribution is \(2(k-3)n^2\). The zero-sum row contributes \(n^2\). For \(k\ge4\), adding contributions yields
\[
E(H_k)=\bigl(2(k-3)+4(k-4)+3+1\bigr)n^2
=6(k-3)n^2.
\]
For \(k=2,3\), all nonzero fibers have the single multiplicity \(n\); their counts give the two stated boundary energies.

**Step 4 (Fourier normalization).** Expanding the fourth power of \(K_N\) and using
\(\sum_{u\bmod N}\exp(2\pi i u j/N)=N\) for \(j=0\) and zero otherwise, separately in both coordinates, gives \(\sum|K_N|^4=N^2\sum R_k(s,z)^2\). Division by \(n^4\) proves the normalized constant-input moment. No limit passage or extrapolation from numerical data is used.

## Verification
Run `python3 check_fibers.py` from the folder containing this document. The checker reconstructs every ordered two-sum fiber and compares every entry with the independent square-root formula for \(2\le k\le10\); it also checks the exact energy and compares direct complex Fourier fourth moments for \(k=2,3,4,5\). Expected completion marker: `VERIFY_OK exact_fiber_positions=1398096 exponents=2..10 direct_complex_fourth_moments=4`. These are finite diagnostic checks, not the proof for all \(k\).

## Relationship to prior work
Shparlinski's 2011 survey introduces modular hyperbolas and their exponential-sum setting. Bower–Evans–Luo–Miller (2012) analyze the **coordinate** sum \(x+x^{-1}\) of an individual hyperbola point and its associated set size; that is not the ambient two-point convolution \((x,x^{-1})+(y,y^{-1})\) classified here. Zhang (2011) gives one-parameter fourth power means of classical Kloosterman sums for a fixed coprime second parameter, while Guo–Geng–Pan (2014) give character-averaged moments for odd prime powers; neither accessible stated theorem specifies this complete two-parameter dyadic fiber census. The standard \(2\)-adic square-root facts are credited as classical arithmetic and are not claimed as new.

## Limitations
The result gives a full dyadic **unweighted** representation profile, its sumset cardinality, and the joint fourth moment, but no general sharp weighted extension inequality or individual Kloosterman bound. It does not extend by a simple substitution to odd prime powers. An equivalent formulation could be present in older local-ring convolution literature; Zhang (2011) was not available in full text for an exhaustive comparison. No independent mathematical validation or priority certification is claimed.

## References
1. I. E. Shparlinski, *Modular Hyperbolas*, arXiv:1103.2879 (first posted 2011-03-15), https://arxiv.org/abs/1103.2879.
2. A. Bower, R. Evans, V. Luo, S. J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930 (first posted 2012-12-12), https://arxiv.org/abs/1212.2930.
3. W. Zhang, *The fourth and sixth power mean of the classical Kloosterman sums*, J. Number Theory 131 (2011), 228–238, DOI 10.1016/j.jnt.2010.08.008.
4. X. Guo, G. Geng, X. Pan, *On the fourth power mean of the general k-th Kloosterman sums*, Adv. Difference Equations 2014, article 103, DOI 10.1186/1687-1847-2014-103.
