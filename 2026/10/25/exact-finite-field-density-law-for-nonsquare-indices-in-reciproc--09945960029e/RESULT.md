# Exact finite-field density law for nonsquare indices in reciprocal-sum sequences

## Finding

Fix an arbitrary positive integer \(h\). For each starting integer \(x_0\geq1\), set
\[
x_{n+1}=\frac{h^2}{x_0+\cdots+x_n}=\frac{a_{n+1}}{b_{n+1}}
\]
with positive coprime numerator and denominator. Call \(n\geq2\) a *failure index* when \(Q_n=(2/h)a_n+b_n\) is **not** the square of an integer, and denote the finite set of failure indices by \(F_h(x_0)\).

For each prime power \(p^\alpha\parallel h\), define the finite-field map
\[
T_p(r)=r+r^{-1}\quad(r\in\mathbb F_p^\times).
\]
For every integer \(j\geq1\), let \(b_{p,j}\) count the elements \(r\in\mathbb F_p^\times\) whose forward orbit first reaches zero on iteration \(j\). Stop at zero; an orbit that repeats a nonzero state without reaching zero does not count. Put \(B_p=\sum_{j=1}^{p-1}b_{p,j}\), with \(b_{p,j}=0\) for \(j\geq p\), and \(L=h\operatorname{rad}(h)=\prod_{p^\alpha\parallel h}p^{\alpha+1}\).

Let \(I\) be the union, over the primes dividing \(h\), of the indices \(j+1\) with \(b_{p,j}>0\). In the **idempotent polynomial ring**
\[
\mathcal R=\mathbb Q[z_n:n\in I]/(z_n^2-z_n:n\in I),
\]
define
\[
G_h(\mathbf z)=\prod_{p^\alpha\parallel h}
\left(1-\frac{B_p}{p^{\alpha+1}}
+\sum_{j=1}^{p-1}\frac{b_{p,j}}{p^{\alpha+1}}z_{j+1}\right).
\]
Reduce powers via \(z_n^2=z_n\); for each subset \(J\subseteq I\), write \([z_J]G_h\) for the coefficient of \(z_J=\prod_{n\in J}z_n\) in the resulting squarefree-monomial basis (including \(z_\varnothing=1\)). **Then**
\[
\#\{1\leq x_0\leq X:F_h(x_0)=J\}
= X\,[z_J]G_h+O(L),\qquad X\to\infty.
\]
Thus every exact failure-index pattern has a computable rational density, and the density of exactly \(k\) failures is \(\sum_{|J|=k}[z_J]G_h\). The set \(F_h(x_0)\) depends only on \(x_0\bmod L\), so this assertion includes an exact finite residue-class algorithm, not merely an asymptotic existence statement. For \(h=1\), take the empty product, \(L=1\), and \(F_h(x_0)=\varnothing\) always.

For the concrete case \(h=145=5\cdot29\), the nonzero basin counts are
\[
(b_{5,1},b_{5,2})=(2,2),\qquad
(b_{29,1},b_{29,2},b_{29,3})=(2,4,2).
\]
Among the \(L=21025\) residue classes, exactly \(17493\), \(3512\), and \(20\) have respectively zero, one, and two **distinct** failure indices. The distinction matters: among the \(32\) residue classes where both primes cause a failure, \(12\) have the two prime obstructions at the same index, so only \(20\) have two distinct failure indices.

## Assumptions and scope

The integer \(h\) is fixed, positive, and unrestricted; \(x_0\) ranges through all positive integers. A perfect square means the square of an integer (not merely a rational square). The notation \(p^\alpha\parallel h\) means \(\alpha\geq1\) is the exact exponent of \(p\) in \(h\). The local map \(T_p\) is used only while its argument is nonzero; zero is recorded as a first hit, not iterated further. The finite ring above has a unique squarefree monomial normal form. All error estimates are for fixed \(h\); the coefficient \([z_J]G_h\) is nonnegative and the finite residue-class error has absolute size at most \(L\).

## Proof

**1. Reduced recurrence and criterion for failure.** Put \(S_n=x_0+\cdots+x_n\) and \(t_n=S_n/h=u_n/v_n\) in lowest positive terms. Then
\[
t_{n+1}=t_n+t_n^{-1},\qquad
u_{n+1}=u_n^2+v_n^2,\quad v_{n+1}=u_nv_n.
\]
The consecutive numerators and denominators remain coprime since \(\gcd(u_n,v_n)=1\). For \(d_j=\gcd(h,u_j)\), reduction of \(x_{j+1}=hv_j/u_j\) gives \(a_{j+1}=hv_j/d_j\) and \(b_{j+1}=u_j/d_j\); for \(j\geq1\),
\[
Q_{j+1}=\frac{2v_j+u_j}{d_j}
=\frac{(u_{j-1}+v_{j-1})^2}{d_j}.
\]
If \(d_j=1\) this is an integer square. If an odd prime \(p\mid d_j\), then \(p\nmid u_{j-1}+v_{j-1}\): otherwise \(u_{j-1}^2+v_{j-1}^2\equiv0\) and \(u_{j-1}+v_{j-1}\equiv0\) imply \(2u_{j-1}v_{j-1}\equiv0\pmod p\), contradicting coprimality. Thus \(Q_{j+1}\) has negative \(p\)-adic valuation. If \(2\mid d_j\), then \(u_{j-1},v_{j-1}\) are both odd, \(\nu_2(u_j)=1\), and \(\nu_2(d_j)=1\). Consequently \(\nu_2(Q_{j+1})\) is odd, preventing an integer square. Hence
\[
j+1\in F_h(x_0)\iff\gcd(h,u_j)>1\quad(j\geq1).
\]

**2. Local \(p\)-adic trichotomy.** Fix \(p^\alpha\parallel h\) and work with \(t_0=x_0/h\in\mathbb Q_p\). If \(\nu_p(x_0)<\alpha\), then \(\nu_p(t_0)<0\); the identity \(T(t)=t+t^{-1}\) preserves negative valuation, so \(p\nmid u_j\) for every \(j\geq1\). If \(\nu_p(x_0)>\alpha\), then \(\nu_p(t_0)>0\), its next valuation is negative, and all subsequent valuations stay negative; again there is no failure caused by \(p\) at any \(j\geq1\).

In the remaining case \(\nu_p(x_0)=\alpha\), let \(m=h/p^\alpha\), which is invertible modulo \(p\). The initial reduction is the nonzero element
\[
r\equiv (x_0/p^\alpha)m^{-1}\pmod p.
\]
While the reduced orbit under \(T_p\) avoids zero, the rational orbit remains a \(p\)-adic unit and reduction commutes with iteration. At its first zero on iteration \(j\geq1\), the reduced numerator \(u_j\) is divisible by \(p\) and its denominator is not. One further iteration has negative valuation, thereafter preserved; no later index can be spoiled by \(p\). If the finite orbit instead repeats before hitting zero, no \(j\) is spoiled. Thus precisely the first-zero depth identifies this prime's unique possible failure index \(j+1\). Any first-zero orbit visits \(j\) distinct nonzero residues before zero, so \(j\leq p-1\).

**3. Residue weights and Chinese remainder.** For each \(r\in\mathbb F_p^\times\), precisely one residue class \(x_0\bmod p^{\alpha+1}\) has \(\nu_p(x_0)=\alpha\) and initial reduction \(r\): namely \(x_0=p^\alpha s\), where \(s\equiv rm\pmod p\). All other classes cause no \(p\)-failure. Therefore the local probabilities are exactly \(b_{p,j}/p^{\alpha+1}\) for an index \(j+1\), and \(1-B_p/p^{\alpha+1}\) for no index. The moduli \(p^{\alpha+1}\) are pairwise coprime across primes dividing \(h\). The Chinese remainder theorem makes the local outcomes independent when \(x_0\) ranges uniformly over \(\mathbb Z/L\mathbb Z\). The *global set of bad indices is the union* of local singleton sets: if two primes strike at the same index, that index is counted only once. Multiplication in the idempotent polynomial ring encodes exactly this set-union rule. Its reduced coefficient \([z_J]G_h\) therefore equals the proportion of residue classes with global bad-index set \(J\), proving periodicity and the density formula. Each class occurs \(X/L+O(1)\) times in \([1,X]\), so the total discrepancy is at most \(L\).

**4. Worked collision example.** Direct iteration of \(T_p\) over the \(4\) nonzero residues modulo \(5\) gives two first hits at depth \(1\) and two at depth \(2\). Over the \(28\) nonzero residues modulo \(29\), there are respectively \(2,4,2\) first hits at depths \(1,2,3\). The two local denominators are \(25\) and \(841\). The number of residue classes with neither obstruction is \((25-4)(841-8)=17493\). Exactly \(4\cdot8=32\) have both obstructions; their failure indices coincide in \(2\cdot2+2\cdot4=12\) classes, so precisely \(20\) have two distinct failures. The remaining \(21025-17493-20=3512\) have one.

## Verification

The accompanying standalone `CHECK.py` uses only Python's standard library. It computes every local first-zero basin, builds the exact idempotent product via sets, and exhaustively enumerates all residues modulo \(L\) for \(h\in\{1,2,4,5,10,13,17,25,29,65,145\}\). It independently compares the local reductions with the first seven reduced integer numerator recurrences on representative initial values. All assertions passed, with output `VERIFY_OK`. This finite verification supports the explicit example and catches index/normalization errors; the theorem for arbitrary \(h\) follows from the proof, not extrapolation from test cases.

## Relationship to prior work

Matijasevick, Rodríguez, and Salazar (2026), Theorem B and Proposition 4.1, prove that each prime dividing \(h\) spoils at most one square and identify the finite-field first-hit obstruction (Remark 4.2). Their Section 7, Question 1 explicitly asks for proportions of initial values with exactly a given number of failures. The present formula supplies all those proportions, and moreover the exact failure-index-set distribution for every \(h\), with collision correction when different primes spoil the same term. The prime-factor restriction and one-possible-failure regime are a simpler contained subcase, not the source of the full distribution.

Jones and Manes (2014) study Galois representations on preimage trees of quadratic rational maps, a broader background topic but not an expression for these reciprocal-sum square-failure densities. A related Matijasevick companion preprint on \(z+k/z\) and zeros of iterates is cited by the motivating paper but its full text was not located; it is a residual literature risk.

## Limitations

The theorem is an exact finite algorithm for fixed \(h\), not a closed elementary function of its prime factors alone: computing basin sizes may require examining all nonzero residues modulo each dividing prime. Its \(O(L)\) error is not uniform when \(h\) varies with \(X\). The full text of the cited companion arithmetic-dynamics preprint could not be inspected, so no claim of exhaustive worldwide novelty is made. No assertion about arbitrary nonsquare \(k\), perturbed recursions, or higher perfect powers is included.

## References

1. M. Matijasevick, S. Rodríguez, G. Salazar, *Perfect squares in reciprocal-sum sequences and primes that are inert in quadratic fields*, arXiv:2610.00765v1 (first posted September 30, 2026), Sections 2, 4, and 7. https://arxiv.org/html/2610.00765v1
2. R. Jones, M. Manes, *Galois theory of quadratic rational functions*, Commentarii Mathematici Helvetici **89** (2014), 173–213, arXiv:1101.4339. https://arxiv.org/abs/1101.4339
3. M. Matijasevick, *Arithmetic dynamics of \(z+k/z\): Galois groups, prime divisors of orbits, and zeros of iterates*, cited as a 2026 preprint in reference [2] of arXiv:2610.00765v1; full text not located.
