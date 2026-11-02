# Exact collision-free triple moments of the parabola over every residue ring

## Finding

Define the parabolic graph \(P_m=\{(t,t^2):t\in\mathbb Z/m\mathbb Z}\). We count *ordered* sums of three of its points whose parameter differences are all invertible modulo \(m\), a local form of distinct-point (collision-free) addition. The result gives the complete fiber distribution and exact support of this restricted triple convolution, for every modulus, including prime powers and non-squarefree composites.

For \(m\ge2\) and \((s,w)\in(\mathbb Z/m\mathbb Z)^2\), put
\[
N_m(s,w)=\#\left\{(x,y,z)\pmod m:\ \begin{array}{l}x+y+z=s,\\x^2+y^2+z^2=w,\\ \gcd(x-y,m)=\gcd(y-z,m)=\gcd(z-x,m)=1\end{array}\right\}.
\]
For an odd prime \(p\), let \(\chi_p\) be the quadratic character with \(\chi_p(0)=0\). Define the local coefficient \(c_p\) by
\[
\begin{aligned}
c_2(s,w)&=0,\\
c_3(s,w)&=\begin{cases}6,&(s,w)\equiv(0,2)\pmod3,\\0,&\text{otherwise},\end{cases}\\
c_p(s,w)&=\begin{cases}
(p-1)(1+\chi_p(-3)),&d=0,\\
p-\chi_p(-3)-3\left(1+\chi_p(d/2)\right),&d\ne0,
\end{cases}\qquad p\ge5,\quad d=3w-s^2\pmod p.
\end{aligned}
\]
Division by \(2\) takes place in \(\mathbb F_p\). The exact answer is
\[
\boxed{N_m(s,w)=\prod_{p^k\parallel m}p^{k-1}c_p(s\bmod p,w\bmod p).}
\]
In particular, the support size is
\[
\boxed{\#\{(s,w)\pmod m:N_m(s,w)>0\}=m^2\prod_{p\mid m}\rho_p,}
\]
where
\[
\rho_p=\begin{cases}
0,&p=2,\\1/9,&p=3,\\2/5,&p=5,\\4/7,&p=7,\\
(p-1)/p,&p\ge11,\ p\equiv2\pmod3,\\
1,&p\ge13,\ p\equiv1\pmod3.
\end{cases}
\]
Thus the collision-free threefold sumset is the entire ambient plane **if and only if** all prime divisors of \(m\) are congruent to \(1\) modulo \(3\) and are at least \(13\). For instance, this holds modulo all powers of \(13\), while the support fractions modulo \(5\), \(7\), and \(11\) are respectively \(2/5\), \(4/7\), and \(10/11\).

## Assumptions and scope

The domain is the commutative ring \(\mathbb Z/m\mathbb Z\) for every integer \(m\ge2\). Pairwise *unit-distinct* means the differences of any two parameters are units. This is stronger than the parameters being merely unequal modulo a composite \(m\). Each triple is ordered; every permutation is counted separately. The theorem classifies exact fibers and image support, not the unrestricted threefold sumset, in which coinciding parameters are permitted.

## Proof

**Prime fields and the two small characteristics.** If \(p=2\), three parameters cannot be pairwise distinct in \(\mathbb F_2\); hence the local count is zero. If \(p=3\), every admissible triple is a permutation of \((0,1,2)\), and all six have first moment \(0\) and second moment \(2\).

Fix an odd prime \(p\ge5\) and a target \((s,w)\). Set \(a=3x-s\), \(b=3y-s\), and \(z=(s-a-b)/3\). This is a bijective change of variables for fixed \(s\). Direct expansion gives
\[
Q(a,b):=a^2+ab+b^2=\frac32(3w-s^2)=:t.
\]
The quadratic form is nonsingular with discriminant \(-3\). Write \(\epsilon=\chi_p(-3)\). Diagonalization yields \(4Q=(2a+b)^2+3b^2\). Hence, by the standard quadratic-character count (or split/nonsplit norm count),
\[
\#\{(a,b)\in\mathbb F_p^2:Q(a,b)=t\}=
\begin{cases}p+(p-1)\epsilon,&t=0,\\p-\epsilon,&t\ne0.\end{cases}
\]
Here is a direct justification of the count: if \(\epsilon=1\), the two linear factors of \(Q\) give \(2p-1\) zeros and \(p-1\) solutions for each nonzero target; if \(\epsilon=-1\), \(Q\) is the norm map from \(\mathbb F_{p^2}\) and has one zero and \(p+1\) solutions for each nonzero target.

The three forbidden coincidences \(x=y\), \(x=z\), \(y=z\) are three distinct lines through the origin of the \((a,b)\)-plane, each of which restricts \(Q\) to three times a square. For \(t=0\), the union of these collision lines meets the level set only at \((0,0)\), so exactly one point is removed. For \(t\ne0\), their intersections with the level set are disjoint, and each contains \(1+\chi_p(t/3)\) points. Since \(t/3=(3w-s^2)/2\), subtracting these three collision contributions gives the displayed \(c_p\) formula. This also proves nonnegativity at the small primes without relying on an asymptotic bound.

**Prime powers.** Let \((x,y,z)\) be a solution modulo \(p^j\) with pairwise unit differences. To lift to prescribed \((s,w)\) modulo \(p^{j+1}\), write the increment to each coordinate as \(p^j\) times a digit \((u,v,t)\) modulo \(p\). The resulting two linear conditions have coefficient matrix
\[
\begin{pmatrix}1&1&1\\2x&2y&2z\end{pmatrix}\pmod p.
\]
Its rank is exactly \(2\): \(p\) is odd and at least two among the reduced parameters differ. Thus each admissible solution has exactly \(p\) lifts to every prescribed next-level target; the unit conditions persist under lifting. Induction gives the factor \(p^{k-1}\) for every prime-power modulus.

**Products of coprime prime powers.** The Chinese remainder theorem identifies triples, targets, and unit-difference constraints componentwise, so all local counts multiply exactly.

**Exact support.** For every fixed \(s\) and \(p\ge5\), the map \(w\mapsto d=3w-s^2\) permutes \(\mathbb F_p\). If \(p\equiv2\pmod3\), then \(\epsilon=-1\), so the zero target is missing; for \(p=5\), in addition, precisely the two nonzero values of \(d\) for which \(\chi_p(d/2)=1\) are missing; for \(p\ge11\), the nonzero counts are positive. If \(p\equiv1\pmod3\), then \(\epsilon=1\), so \(d=0\) is represented; for \(p=7\), precisely the three nonzero values with \(\chi_p(d/2)=1\) are missing; for \(p\ge13\), all nonzero values are represented. At \(p=3\), only one of nine target pairs occurs, and at \(p=2\) none occurs. These counts give \(\rho_p\). The prime-power lifting and Chinese remainder theorem yield the global support formula and its exact covering criterion.

## Verification

The standalone file `verify.py` enumerates complete ordered triples and target fibers independently of the proof and compares every target with the character formula. It successfully checked all \(86504\) target fibers across \(23\) moduli \(2,3,4,5,7,8,9,11,13,17,19,25,27,35,45,49,55,63,77,81,121,125,169\), including nonsquarefree and mixed-prime moduli. Run `python verify.py` with a standard Python installation. Finite enumeration corroborates but does not establish the universal lifting/CRT assertions.

## Relationship to prior work

Restricted additive sums with distinct parameters are studied by Hou and Sun (2002). Their primary theorem concerns single-coordinate restricted field sums; it does not give the joint two-moment fiber distribution or prime-power lifting here. Mockenhaupt and Tao (first circulated 18 April 2002) study finite-field parabolas through restriction and convolution estimates; those statements do not count collision-free three-point fibers in residue rings. Shparlinski (2013) studies additive decompositions of multiplicative subgroups, not the present two-dimensional graph fibers. Modern work on parabola Fourier norms and exponential spectra is also related geometrically but yields different invariants. General quadratic-form solution counts underpin a step of the proof and are not asserted as new. The claim of historical novelty is limited to the exact collision-free threefold moment distribution together with its sharp all-modulus support criterion.

## Limitations

The unit-difference condition is essential: the formula is not for merely unequal parameters modulo a composite integer. This result says nothing about the unrestricted threefold parabolic sumset or arbitrary polynomial graphs. The local conic count is classical; the contribution is its combination with the collision restriction, exact Hensel multiplicity, and the global support classification. Specialized older work might contain an equivalent formulation; historical priority is not independently certified. Independent mathematical audit has not been performed.

## References

1. Q.-H. Hou and Z.-W. Sun, *Restricted sums in a field*, Acta Arithmetica 102 (2002), 239–249. DOI: 10.4064/aa102-3-3.
2. G. Mockenhaupt and T. Tao, *Restriction and Kakeya phenomena for finite fields*, arXiv:math/0204234, version 1 posted 18 April 2002; Duke Math. J. 121 (2004), 35–74.
3. I. E. Shparlinski, *Additive Decompositions of Subgroups of Finite Fields*, arXiv:1301.2872v1 (14 January 2013).
