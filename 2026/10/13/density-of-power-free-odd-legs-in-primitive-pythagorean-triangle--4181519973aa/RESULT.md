# Density of power-free odd legs in primitive Pythagorean triangles

## Finding
Fix an integer \(k\ge2\). Let \(T_k(X)\) count primitive positive integer right triangles with hypotenuse at most \(X\), up to interchange of legs, whose unique odd leg is \(k\)-free (not divisible by the \(k\)-th power of a prime). Then
\[
T_k(X)=\frac{X}{2\pi}P_k+o_k(X),\qquad
P_k=\prod_{\substack{p\ \mathrm{prime}\\p>2}}\left(1-\frac{2}{p^{k-1}(p+1)}\right).
\]
The limit of the proportion of all primitive right triangles with \(k\)-free odd leg is exactly \(P_k\). In particular, the squarefree-odd-leg proportion \(P_2\) is a positive constant (approximately \(0.70752\)). The distinction between odd and even legs matters: the even leg in any primitive Pythagorean triple is divisible by \(4\), so it is never squarefree.

## Assumptions and scope
An integer \(n\ge1\) is \(k\)-free if no prime \(p\) satisfies \(p^k\mid n\). An integer right triangle is primitive when its three side lengths have greatest common divisor \(1\); in that case exactly one leg is odd. We count each triangle once, independently of interchanging the legs. The exponent \(k\ge2\) is fixed as \(X\to\infty\). No uniformity in a growing exponent is asserted. The Euler product converges absolutely because its factors differ from \(1\) by \(O(p^{-k})\).

## Proof
**1. An exact bijection.** Euclid's primitive parametrization has \(m>n\ge1\), \(\gcd(m,n)=1\), opposite parity, hypotenuse \(m^2+n^2\), odd leg \(m^2-n^2\), and even leg \(2mn\). Put \(u=m-n\), \(v=m+n\). Then \(u,v\) are positive odd coprime integers with \(u<v\),
\[
m=(u+v)/2,\quad n=(v-u)/2,\quad m^2-n^2=uv,\quad m^2+n^2=(u^2+v^2)/2.
\]
Conversely every such \((u,v)\) gives coprime opposite-parity \((m,n)\) and exactly one primitive triangle. Since \(\gcd(u,v)=1\), the odd leg \(uv\) is \(k\)-free precisely when both \(u\) and \(v\) are \(k\)-free. Consequently \(T_k(X)\) counts pairs
\[
0<u<v,\quad u,v\ \mathrm{odd},\quad \gcd(u,v)=1,\quad u,v\ \mathrm{are}\ k\text{-free},\quad u^2+v^2\le2X.
\]
The planar sector \(\Omega_X\) defined by \(0<u<v\) and \(u^2+v^2\le2X\) has area \(\pi X/4\).

**2. Exact local factors.** The parity restriction gives density \(1/4\) at \(p=2\). At any odd prime \(p\), failure means either \(p\) divides both coordinates (probability \(p^{-2}\)), or \(p^k\) divides exactly one coordinate and \(p\) does not divide the other (combined probability \(2p^{-k}(1-p^{-1})\)). These are disjoint. The admissible fraction of residue classes modulo \(p^k\) is therefore
\[
\lambda_{p,k}=1-p^{-2}-2p^{-k}(1-p^{-1})
=(1-p^{-2})\left(1-\frac{2}{p^{k-1}(p+1)}\right).
\]
All \(\lambda_{p,k}\) are positive; the factors tend to \(1\) sufficiently fast for their product to converge to a strictly positive number.

**3. Passing from local to global density.** Fix a real cutoff \(z\ge3\), and impose the local conditions only for odd primes \(p\le z\), together with both coordinates being odd. The Chinese remainder theorem gives a periodic union of residue classes modulo \(Q_z=2\prod_{3\le p\le z}p^k\) with density
\[
\delta_z=\frac14\prod_{3\le p\le z}\lambda_{p,k}.
\]
For each fixed \(z\), counting lattice points in the dilated bounded sector yields
\[
\#(\Omega_X\cap\mathrm{admissible\ residues})
=\frac{\pi X}{4}\,\delta_z+O_{k,z}(\sqrt X).
\]
Here a fixed-residue lattice-point estimate follows by covering the piecewise-smooth sector boundary with \(O_{Q_z}(\sqrt X)\) unit cells.

Put \(R=\sqrt{2X}\). Among pairs in the sector, a forbidden odd prime \(p>z\) dividing both coordinates occurs in at most
\[
\sum_{z<p\le R}(R/p+1)^2
=O(R^2/z+R\log(2R)+R)
\]
pairs, using the elementary bound on the harmonic series; primes can even be replaced by all integers in this estimate. Separately, a forbidden odd prime \(p>z\) with \(p^k\mid u\) or \(p^k\mid v\) occurs in at most
\[
2R\sum_{z<p\le R^{1/k}}\left\lfloor\frac{R}{p^k}\right\rfloor
=O_k(R^2/z^{k-1})
\]
pairs. Thus the large-prime tail is \(O_k(X/z+\sqrt X\log(2X))\), valid for fixed \(k\ge2\). Take \(X\to\infty\) first with \(z\) fixed, then \(z\to\infty\). It follows that
\[
T_k(X)=\frac{\pi X}{16}\prod_{p>2}\lambda_{p,k}+o_k(X).
\]

**4. Simplification and relative density.** The classical Euler product gives
\[
\prod_{p>2}(1-p^{-2})
=\frac{\zeta(2)^{-1}}{1-2^{-2}}=\frac8{\pi^2}.
\]
Substitution proves
\[
\frac{\pi}{16}\prod_{p>2}\lambda_{p,k}
=\frac1{2\pi}\prod_{p>2}\left(1-\frac{2}{p^{k-1}(p+1)}\right).
\]
Applying the same periodicity and tail argument without the \(k\)-free restrictions yields \(T_{\mathrm{all}}(X)\sim X/(2\pi)\), and division proves that the limiting proportion is \(P_k\). Every Euler factor is strictly between zero and one; the product is strictly positive, while the factor at \(p=3\) makes it strictly less than one.

## Verification
The accompanying `verify.py` implements two independent exact finite enumerations: primitive Euclidean parameter pairs and coprime odd-factor pairs. It compares ordered triples and their counts for \(k\in\{2,3,4\}\) and \(X\in\{50,500,10000,100000,1000000\}\). The observed counts at \(X=1000000\) are \(112912\), \(147134\), and \(155649\) respectively. These are regression checks only; the proof of the infinite statement is given above. A separate bounded prime product is an illustration, not a proof of the exact Euler-product value.

## Relationship to prior work
Euclid's parametrization and the factorization of the odd leg as two coprime odd factors are classical. Zelator's 2008 paper studies obstructions involving squarefree factors of primitive Pythagorean legs; Overmars and Ntogramatzidis (2015) develop an alternative parametrization. Burson (2020) discusses squarefree odd-leg factors, without the present counting density. Ochieng (2019) counts primitive Pythagorean triples with a fixed odd leg via divisor factorizations, not the proportion of those with power-free odd leg as hypotenuse grows. The contribution claimed here is solely the explicit all-hypotenuse counting density and its \(k\)-free Euler factors, not the classical parametrization or fixed-leg divisor formulas.

## Limitations
The leading asymptotic is for each fixed exponent and includes only an \(o_k(X)\) remainder; no effective power-saving error or distribution for varying \(k\) is proved. It is not asserted that earlier unindexed sources cannot contain an equivalent density calculation. Finite enumerations do not establish the infinite limit. This study concerns the odd leg of primitive right triangles; it is not a squarefreeness theorem for arbitrary integer right triangles.

## References
1. K. Zelator, *Two Theorems on the Structure of Pythagorean Triples and Some Diophantine Consequences* (first version 2008-05-07), arXiv:0805.1052, https://arxiv.org/abs/0805.1052.
2. A. Overmars and L. Ntogramatzidis, *A New Parameterisation of Pythagorean Triples in Terms of Odd and Even Series* (first version 2015-04-01), arXiv:1504.03163, https://arxiv.org/abs/1504.03163.
3. S. Ochieng, *Pythagorean Triples with Common Sides* (2019), DOI:10.1155/2019/4286517, https://doi.org/10.1155/2019/4286517.
4. S. Burson, *The Mobius Function and Congruent Numbers* (first version 2020-06-24), arXiv:2006.16760, https://arxiv.org/abs/2006.16760.
5. Classical Euler product \(\zeta(2)=\pi^2/6\) and the Chinese remainder theorem.
