# Exact entry-depth spectrum for the quadratic congruential map \(x\mapsto x^2+1\) modulo \(2^k\)

## Finding
Let \(f_k:\mathbb Z/2^k\mathbb Z\to\mathbb Z/2^k\mathbb Z\) be \(f_k(x)=x^2+1\), for any integer \(k\ge3\). Every orbit reaches the unique two-cycle. Define \(d_k(x)\) as the smallest nonnegative number of iterations needed to reach either cycle vertex, and put \(B_k(t)=\#\{x\bmod 2^k:d_k(x)\le t\}\).

Write \(D_k=\lfloor(2k+1)/3\rfloor\). For any integer \(h\le k\) define
\[
O_k(h)=\begin{cases}2^{k-1},&h\le3,\\2^{k+2-h},&4\le h\le k,\end{cases}
\qquad
E_k(h)=\begin{cases}2^{k-2},&h\le5,\\2^{k+3-h},&6\le h\le k.\end{cases}
\]
Then \(B_k(0)=2\), and for every \(1\le t\le D_k\),
\[
\boxed{B_k(t)=O_k\!\left(k-\left\lfloor\frac{3t}{2}\right\rfloor+1\right)
+E_k\!\left(k-\left\lfloor\frac{3(t-1)}{2}\right\rfloor\right)
+2^{k-2}\mathbf1_{t=D_k}.}
\]
For \(t>D_k\), \(B_k(t)=2^k\). Consequently the number of residues of *exact* first-entry depth \(t\) is \(B_k(t)-B_k(t-1)\) (with \(B_k(-1)=0\)), giving the entire preperiod spectrum. Moreover, \(D_k\) is the sharp maximal entry depth and its maximizers are **exactly** the \(2^{k-2}\) residues divisible by four.

## Assumptions and scope
All powers, residue counts, and iteration times are over \(\mathbb Z/2^k\mathbb Z\). The two vertices of the cycle have opposite parities. The depth counts the first arrival at either cycle vertex; it does not count the subsequent cycling. The formulas hold without primality assumptions beyond the prime \(2\) and for *every* \(k\ge3\); the levels \(k=1,2\) are elementary exceptional levels (respectively, all two residues are periodic; and the depth histogram is \((2,2)\)).

## Proof
**1. Unique two-cycle.** Put \(f(x)=x^2+1\) over the two-adic integers, and \(g=f\circ f=x^4+2x^2+2\). Parity alternates under \(f\); \(g\) maps the even integers into \(2+8\mathbb Z_2\). For any even \(x,y\),
\[
g(x)-g(y)=(x-y)(x+y)(x^2+y^2+2).
\]
Here \(\nu_2(x+y)\ge1\) and \(\nu_2(x^2+y^2+2)=1\), so \(g\) is strictly contracting on \(2\mathbb Z_2\), with Lipschitz constant at most \(1/4\). Completeness yields exactly one fixed point \(e\in2\mathbb Z_2\), satisfying \(e\equiv2\pmod8\). Set \(o=f(e)\); then \(f(o)=e\), and \(o\equiv5\pmod{16}\). The two distinct elements \(e,o\) form a cycle. The contraction also holds modulo \(2^k\): every even orbit under \(g\) reaches \(e\bmod2^k\), and a cycle for \(g\) cannot have more than one point. Because \(f\) alternates parity, there are no other cycles for \(f_k\).

**2. Exact valuation gains.** In what follows, \(\nu_2(0)=+\infty\). If \(y\) is even with \(\nu_2(y-e)\ge3\), then \(\nu_2(y+e)=2\) (since \(\nu_2(2e)=2\)), giving
\[
\nu_2(f(y)-o)=\nu_2(y^2-e^2)=\nu_2(y-e)+2.
\]
If \(y\) is odd with \(\nu_2(y-o)\ge3\), then \(\nu_2(y+o)=1\), giving
\[
\nu_2(f(y)-e)=\nu_2(y^2-o^2)=\nu_2(y-o)+1.
\]
Thus sufficiently near the even cycle vertex, successive errors gain alternately two and one binary digits; the gains reverse in the other phase.

**3. Partition by input class.** For odd \(x\), let \(s=\nu_2(f(x)-e)=\nu_2(x^2-o^2)\ge3\). For all \(t\ge1\), the valuation of the error after \(t\) iterations, relative to the cycle vertex of matching parity, is exactly
\[
s+\left\lfloor\frac{3t}{2}\right\rfloor-1.
\]
For \(x\equiv2\pmod4\), put \(s=\nu_2(f(x)-o)=\nu_2(x^2-e^2)\ge5\). The corresponding valuation after \(t\ge1\) iterations is
\[
s+\left\lfloor\frac{3(t-1)}2\right\rfloor.
\]
These identities remain true when \(s=+\infty\) by the convention for valuations. Finally, if \(x\equiv0\pmod4\), then \(\nu_2(x-e)=\nu_2(x+e)=1\). After any \(t\ge1\) iterations, the matching-phase error has *exact* valuation
\[
\left\lfloor\frac{3t+1}{2}\right\rfloor.
\]
Thus all multiples of four have first-entry depth exactly \(\lceil(2k-1)/3\rceil=\lfloor(2k+1)/3\rfloor=D_k\). Every odd starting value has at least the accuracy of a multiple of four one iteration *later*, and every starting value congruent to two modulo four has at least the accuracy of a multiple of four two iterations later. Directly at \(k=3\), the latter class enters after at most one step. Hence all other classes enter strictly before \(D_k\), proving the maximum and its maximizers.

**4. Count each class exactly.** For \(1\le h\le k\), the number of odd residues \(x\bmod2^k\) with \(\nu_2(x^2-o^2)\ge h\) equals \(O_k(h)\). Indeed, for \(h\le3\) every odd square is \(1\pmod8\), and for \(h\ge3\), an odd square has exactly four square roots modulo \(2^h\), each lifting to \(2^{k-h}\) residues modulo \(2^k\). The formulas agree at \(h=3\).

Similarly, for \(x\equiv2\pmod4\), write \(x=2u\), \(e=2w\), with \(u,w\) odd. The condition \(\nu_2(x^2-e^2)\ge h\) is automatic for \(h\le5\). For \(h\ge5\), it is equivalent to \(u^2\equiv w^2\pmod{2^{h-2}}\). There are four roots modulo \(2^{h-2}\), each with \(2^{k-h+1}\) lifts of \(u\bmod2^{k-1}\), giving \(E_k(h)=2^{k+3-h}\). These expressions also agree at \(h=5\).

An input is in the basin after \(t\ge1\) steps exactly when its matching-phase error has valuation at least \(k\). Add the disjoint counts from the odd class, the \(2\pmod4\) class, and (only when \(t\ge D_k\)) the multiples of four. This proves the displayed cumulative formula for \(1\le t\le D_k\), with \(B_k(0)=2\) given by the unique periodic two-cycle. The exact-depth formula follows by differencing. \(\square\)

## Verification
The standalone script `verify.py` independently computes all residue orbits, without using the valuation proof, and checks every cumulative count and exact maximizing class for all \(3\le k\le14\). Run `python verify.py`. The output ends in `VERIFY_OK exact_all_residues_levels=3..14`. These experiments are finite checks, not a substitute for the proof valid for every \(k\).

## Relationship to prior work
Fan and Liao (2010), Theorem D / Theorem 6.1(4), already establish that for quadratic maps \(x^2-\lambda\) with \(\lambda\equiv3\pmod4\), all of \(\mathbb Z_2\) is attracted to a two-cycle. That *includes* \(x^2+1\), so the attraction assertion alone is not new. Their classification, however, does not supply the finite-level **first-entry-depth multiplicity distribution** or the sharp \(\lfloor(2k+1)/3\rfloor\) depth with its complete maximizing residue class, which are the present contribution. Fan and Liao (2014) treat \(x\mapsto x^2\), a distinct map with fixed-point rather than period-two attraction. Gilbert et al. (2001) discuss quadratic digraphs modulo a prime, not the entire dyadic tower. Somer and Křížek (2006) study the unshifted square-map digraph for composite moduli and do not establish this shifted quadratic claim. The minimum-depth classification should not be confused with the existing qualitative global-basin theorem.

## Limitations
Only \(x^2+1\) at powers of two is analyzed, not general quadratic coefficients or odd-prime moduli. Qualitative attraction to a two-cycle is prior art. The proof is self-contained and establishes exact finite-ring depths, but it does not provide an independent audit or universal literature-priority certification. Other equivalent formulations in specialized arithmetic-dynamics literature may exist.

## References
1. A.-H. Fan and L. Liao, *On minimal decomposition of p-adic polynomial dynamical systems*, arXiv:1010.5583v1, first public 2010-10-27, especially Theorem 6.1(4). https://arxiv.org/abs/1010.5583
2. S. Fan and L. Liao, *Dynamics of the square mapping on the ring of p-adic integers*, arXiv:1408.4574v1, first public 2014-08-20. https://arxiv.org/html/1408.4574v1
3. C. L. Gilbert, J. D. Kolesar, C. A. Reiter, and J. D. Storey, *Function digraphs of quadratic maps modulo p*, Fibonacci Quarterly 39(1) (2001), 32–49.
4. L. Somer and M. Křížek, *Structure of digraphs associated with quadratic congruences with composite moduli*, Discrete Math. 306 (2006), 2174–2185, doi:10.1016/j.disc.2005.12.026.
