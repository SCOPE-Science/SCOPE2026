# The complete two-sum fiber spectrum of a quartic graph over prime-square rings

## Finding

Let \(p\ge5\) be prime, \(R=\mathbb Z/p^2\mathbb Z\), and \(C=\{(t,t^4):t\in R\}\). For \(s,y\in R\), let \(r(s,y)=\#\{(a,b)\in R^2:a+b=s,\ a^4+b^4=y\}\). Write \(\chi\) for the Legendre character modulo \(p\), with \(\chi(0)=0\), and set
\[
b=\chi(-1),\quad c=\chi(-3),\quad e=\chi(-6),\quad h=\gcd(4,p-1),
\qquad L=\frac{p-2+b}{4},\quad H=\frac{p-4-b-2c-2e}{8},\quad u=1+c,\quad v=1+e.
\]
The integers \(L,H\) are nonnegative. For each of the \(p^2-p\) unit sums \(s\), the multiset of values of \(r(s,y)\) for \(y\in R\) consists of:

- \(pL\) copies of \(2\) and \(pH\) copies of \(4\), from the nonexceptional classes of \(\lambda=8ys^{-4}\bmod p\);
- one value \(p+v\) at \(\lambda=1\) in \(R\), and \(p-1\) copies of \(v\) at the other lifts of \(\lambda=1\bmod p\);
- one value \(pu\) at \(\lambda=-8\) in \(R\);
- \(p^2-[pL+pH+p+1]\) additional zeros, including the other \(p-1\) lifts of \(\lambda=-8\bmod p\).

Equal multiplicities from distinct entries of the list are combined, including when \(u\) or \(v\) is zero. For each of the other \(p\) choices of \(s\), the multiset consists of one \(p\), exactly \(p(p-1)/h\) copies of \(h\), and \(p^2-1-p(p-1)/h\) zeros.

Consequently
\[
|C+C|=(p^2-p)\left[p(L+H)+1+\frac{(p-1)v}{2}+\frac u2\right]+p\left[1+\frac{p(p-1)}h\right],
\qquad E(C):=\sum_{s,y}r(s,y)^2=p^2\bigl(6p^2-8p+3+2(p-1)(p-2)c\bigr).
\]
For a **primitive** additive character \(\psi:R\to\mathbb C^\times\), meaning one of order \(p^2\), the normalized function
\[
\mathcal E_\psi1(X,Y)=p^{-2}\sum_{t\in R}\psi(Xt+Yt^4)
\]
satisfies \(\sum_{X,Y\in R}|\mathcal E_\psi1(X,Y)|^4=E(C)/p^4\). For a nontrivial **imprimitive** character, the same sum instead equals the field quartic energy \(3p^2-3p+1-2(p-1)c\).

## Assumptions and scope

Pairs are ordered and include diagonal pairs. Ring equations are modulo \(p^2\) unless a reduction is specified. Fourier sums in the statement use counting measure on \(R^2\). The Fourier identity is for constant input, not a sharp norm assertion for arbitrary weights.

## Proof

**Reduction and lifting.** Parametrize each pair of sum \(s\) uniquely by \(d=a-b\), so that \(a=(s+d)/2\), \(b=(s-d)/2\). Then \(8(a^4+b^4)=s^4+6s^2d^2+d^4\). For unit \(s\), put \(z=d/s\) and \(g(z)=z^4+6z^2+1\). The equation is \(g(z)=\lambda\). Its derivative is \(4z(z^2+3)\). For each fixed target lift, a regular residue root has one lift by the congruence \(g(z_0+pt)\equiv g(z_0)+ptg'(z_0)\pmod{p^2}\). The exceptional target reductions \(1,-8\) are distinct. Over \(1\), the residue root \(0\) gives all \(p\) lifts at the single target \(1\) and nowhere else, and the \(v\) regular roots of \(z^2=-6\) give one lift each for every lift of the target. For the residue value \(-8\), use \(g(z)+8=(z^2+3)^2\); precisely the \(u\) roots of \(z^2=-3\bmod p\) contribute, each with all \(p\) lifts at \(-8\) and nowhere else. All other residue fibers have \(0,2\) or \(4\) regular roots in opposite pairs.

**Counting the regular residue fibers.** Over \(\mathbb F_p\),
\[
g(z)-g(w)=(z^2-w^2)(z^2+w^2+6).
\]
The first factor vanishes at \(2p-1\) pairs, the second at \(p-b\), and both at \(2u\). For the second count, \(\sum_z\chi(z^2+6)=-1\), since \(w^2-z^2=6\) has \(p-1\) solutions by factoring and using \(p\ne2,3\); multiply the sum by \(b\) to count \(z^2+w^2=-6\). Thus the second moment of the \(g\)-fibers modulo \(p\) is \(3p-3-b-2c\), and their first moment is \(p\). Removing the two exceptional residue fibers, of sizes \(1+v\) and \(u\), gives
\[
2L+4H=p-(1+v)-u,\qquad 4L+16H=3p-3-b-2c-(1+v)^2-u^2.
\]
Solving yields the stated \(L,H\); lifting gives the unit-sum multiset.

**Nonunit sums and sumset.** If \(p\mid s\), the equation becomes \(8y=d^4\). Each of \((p-1)/h\) nonzero fourth powers in the field has \(h\) regular roots, each of which lifts uniquely to each of the \(p\) target lifts. The \(p\) multiples of \(p\) all map to zero, and no other argument does. This proves the second multiset, and counting its positive entries and those for unit sums yields the sumset formula.

**Energy.** Equivalently, the energy counts triples \((s,d,f)\) for which
\[
P(s,d,f)=(d^2-f^2)(d^2+f^2+6s^2)=0.
\]
Over \(\mathbb F_p\), each nonzero \(s\) has \(3p-3-b-2c\) solutions by the count for \(g\). At \(s=0\), there are \(1+h(p-1)\) solutions of \(d^4=f^4\). Since \(h=3+b\), the field energy is \(E_p=3p^2-3p+1-2(p-1)c\). On \(P=0\) the gradient of the product vanishes exactly on \(d=f=0\) and at the further intersections \(d^2=f^2=-3s^2\) with \(s\ne0\): away from common zeros, the only singular points of a single vanishing factor come from the line \(d=f=0\) for the first factor, or the origin for the second. The number of singular triples is \(S=p+2(p-1)u\). A regular triple has \(p^2\) lifts solving \(P=0\) in \(R\); a singular triple has all \(p^3\) lifts, as either both factors vanish modulo \(p\) or \(p\mid d,f\) makes the first factor zero modulo \(p^2\). Thus \(E(C)=p^2E_p+(p^3-p^2)S\), giving the claimed expression.

**Fourier normalization.** Write \(\psi(x)=\exp(2\pi i jx/p^2)\) with \(j\in R\). Expanding the fourth power and summing the two frequencies gives \(p^4\) precisely for quadruples with both coordinate differences annihilated by \(j\), and zero otherwise. If \(p\nmid j\), this means the differences vanish in \(R\), giving \(p^{-8}p^4E(C)\). If \(j\ne0\) and \(p\mid j\), the differences need only vanish modulo \(p\). Each field quadruple then has \(p^4\) lifts, so the answer is \(p^{-8}p^4p^4E_p=E_p\).

## Reproducibility

For a bounded direct check, for each \(p\in\{5,7,11,13,17\}\), loop over \(s,a\in\{0,\ldots,p^2-1\}\), set \(b=(s-a)\bmod p^2\) with its least nonnegative representative, and increment a counter at \((s,(a^4+b^4)\bmod p^2)\). Include zero counters when comparing each row's multiset. Summing the squared counters gives respectively \(2225,14749,55781,198913,323969\). The corresponding loop at modulus \(p\) gives \(69,115,351,445,849\). For instance the order-five character on \(\mathbb Z/25\mathbb Z\) yields fourth moment \(69\), not \(2225/5^4=89/25\). The comparison of these finite examples is not the universal proof.

## Relationship to prior work and limitations

Finite-field quartic-energy calculations determine \(E_p\), not the prime-square fibers. The exceptional lifts and nonunit-sum stratum above are specific to the prime-square ring. Finite-field extension moment methods are background, not a novelty claim for character orthogonality. This classification does not cover higher prime powers, general composite moduli, or the weighted extension norm. Exact historical priority is not asserted.

## References

1. C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647.
2. *Exact additive energy of the finite-field quartic graph* (finite-field energy).
3. *An arithmetic phase transition in the invariant quartic-graph Fourier norm* (weighted finite-field extension quotient).
