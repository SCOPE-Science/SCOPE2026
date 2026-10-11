# Sharp finite-boundary versus full-shift reversibility for nonlinear first-degree cellular automata

## Finding

**Theorem (exact boundary transition and sharp inverse radius).** Let \(d\geq2\), write \(\rho=\operatorname{rad}(d)=\prod_{p\mid d}p\), and choose coefficients \(c_0,\ldots,c_7\in\mathbb Z/d\mathbb Z\). Define
\[
R(a,b,z)=c_0abz+c_1ab+c_2az+c_3bz+c_4a+c_5b+c_6z+c_7\pmod d.
\]
Suppose \(\gcd(c_5,d)=1\), \(\rho\mid c_0,c_1,c_2,c_3\), and \(\rho\mid c_4c_6\). These are the finite-null-boundary, all-length invertibility conditions of Baby and Bhattacharjee [1]. Denote by \(F\) the corresponding cellular automaton on \((\mathbb Z/d\mathbb Z)^{\mathbb Z}\), with \((Fx)_i=R(x_{i-1},x_i,x_{i+1})\). Then:

1. \(F\) is bijective if and only if **both** \(\rho\mid c_4\) and \(\rho\mid c_6\). Whenever it is bijective, its inverse is a sliding-block code with centered radius at most \(E-1\), where \(E=\max_{p\mid d}v_p(d)\).
2. If either divisibility fails, there exist two distinct spatially periodic configurations with identical images, and one may choose their common spatial period \(L\) to divide \(p-1\) for a prime \(p\mid d\). In fact, one configuration is the zero configuration.
3. The uniform inverse-radius bound \(E-1\) cannot be decreased in this family. For every \(d\), the globally reversible linear rule \((Fx)_i=x_i+\rho x_{i-1}\pmod d\) has least possible centered inverse radius exactly \(E-1\).

Thus invertibility for **every finite length under zero boundary conditions** does not imply reversibility on the bi-infinite full shift. The two notions are distinguished by separate, rather than product, radical divisibility of the neighbor coefficients.

## Assumptions and scope

The state ring is \(\mathbb Z/d\mathbb Z\) for an arbitrary integer \(d\ge2\). The source hypothesis concerns finite words of every positive length with exterior entries equal to zero; the new conclusion concerns the two-sided infinite product space with no imposed boundary values. A centered radius bound \(r\) means the inverse coordinate at \(i\) depends only on output coordinates in \([i-r,i+r]\). We use \(v_p(d)\) for the exponent of the prime \(p\) in \(d\). The coefficients and rule are fixed; no limit in lattice length or assumptions on initial configurations are needed.

## Proof

**I. Finite-null-boundary context.** Reducing modulo any prime \(p\mid d\), all terms involving \(c_0,\ldots,c_3\) disappear. The finite-null-boundary map is affine, with diagonal coefficient \(c_5\) a unit and with at most one of \(c_4,c_6\) nonzero modulo \(p\). Its matrix is therefore triangular with invertible diagonal. It is a permutation modulo \(p\) for every length. To lift from modulo \(p^k\) to modulo \(p^{k+1}\), write a candidate correction as \(x+p^k t\); its image changes by \(p^k J_p t\) modulo \(p^{k+1}\), where \(J_p\) is that same invertible triangular matrix modulo \(p\). Hence every target has a unique lift of its preimage at every digit. The Chinese remainder theorem combines the prime-power inverses. This reconstructs the finite all-length assertion [1] without relying on finite enumeration.

**II. Full-shift sufficiency and radius.** Now assume the stronger conditions \(\rho\mid c_4,c_6\) separately. For each \(p^e\parallel d\), the map is coordinatewise \(c_5x_i+c_7\) modulo \(p\). Thus any target \(y\) uniquely determines \(x_i\pmod p\) from \(y_i\). Suppose \(x^{(k)}\) is already determined modulo \(p^k\) and \(F(x^{(k)})=y\pmod{p^k}\). Correct by \(x_i^{(k+1)}=x_i^{(k)}+p^k t_i\). Because the four mixed coefficients and both neighbor coefficients vanish modulo \(p\), the only nonzero partial derivative modulo \(p\) is the central derivative \(c_5\). Thus
\[
F(x^{(k)}+p^kt)_i\equiv F(x^{(k)})_i+p^kc_5t_i\pmod{p^{k+1}}.
\]
There is exactly one \(t_i\pmod p\), computed by multiplying the normalized residual by \(c_5^{-1}\pmod p\), at each coordinate. The update increases the radius needed from the output by at most one. Starting at radius zero modulo \(p\), the unique inverse modulo \(p^e\) has centered radius at most \(e-1\). Combining the finitely many components by the Chinese remainder theorem yields a two-sided inverse of radius at most \(E-1\). Uniqueness and existence follow coordinatewise without compactness or a passage through finite boundary systems.

**III. Necessity: explicit short periodic collision.** Suppose \(p\mid d\) and not both \(c_4,c_6\) vanish modulo \(p\). Under the product hypothesis \(p\mid c_4c_6\), exactly one is nonzero. Put \(a=c_4\pmod p\), \(b=c_5\pmod p\neq0\), and \(z=c_6\pmod p\). Choose
\[
\lambda=\begin{cases}-a/b,&a\neq0,\\-b/z,&z\neq0,\end{cases}
\qquad\lambda\in\mathbb F_p^\times.
\]
Then \(a+b\lambda+z\lambda^2=0\). Let \(L\) be the multiplicative order of \(\lambda\), hence \(L\mid(p-1)\). Define the nonzero \(L\)-periodic configuration
\[
\delta_i=(d/p)\lambda^i\pmod d,
\]
where any integer representative of the field value \(\lambda^i\) can be used. At primes other than \(p\), every \(\delta_i\) is zero modulo the complete prime power dividing \(d\); at \(p^e\parallel d\), each \(\delta_i\) is a multiple of \(p^{e-1}\). Every mixed term in \(R(\delta_{i-1},\delta_i,\delta_{i+1})-R(0,0,0)\) contains at least two such factors and one coefficient divisible by \(p\), so vanishes modulo \(p^e\). The surviving linear contribution equals
\[
(d/p)\lambda^{i-1}(a+b\lambda+z\lambda^2)\equiv0\pmod d,
\]
with the congruence understood modulo \(p\) for the parenthesized expression. Consequently \(F(\delta)=F(0)\), although \(\delta\ne0\). Thus \(F\) is noninjective and cannot be reversible. This construction also covers \(p=2\), when \(L=1\).

**IV. Radius sharpness.** Take \(F=I+\rho S^{-1}\), where \((S^{-1}x)_i=x_{i-1}\). Since \(\rho^E\equiv0\pmod d\), its inverse is the finite local polynomial
\[
F^{-1}=\sum_{j=0}^{E-1}(-\rho)^jS^{-j}.
\]
For any prime \(p\) attaining \(v_p(d)=E\), the coefficient \((-\rho)^{E-1}\) has valuation exactly \(E-1\) and is nonzero modulo \(p^E\). Thus output coordinates at distance \(E-1\) genuinely affect the inverse; no shorter centered window determines it. The case \(E=1\) gives radius zero.

## Verification

Run `python3 verify.py` from this package (Python 3.9 or newer; standard library only). It reports `VERIFIED 19733 exact finite assertions`. Tests include all admissible coefficient tuples over moduli 2 and 4 against null-boundary bijectivity at lengths 1, 2, 3; 70 seeded examples per modulus over 6, 8, 9, 12, 16 and 18; exact finite-ring digit-wise inversions; concrete periodic collisions; and inverse-radius sharpness witnesses through modulus 36. These are finite diagnostics. The all-moduli, all-length, full-shift theorem is proved in Sections II–IV and is not inferred from the test results.

## Relationship to prior work

Baby and Bhattacharjee [1] prove the finite-null-boundary, all-length coefficient characterization. That theorem is a **hypothesis** for the new result; their proof does not classify invertibility on the unrestricted bi-infinite lattice or construct inverse radii and periodic noninjectivity witnesses. Bhattacharjee and Das [2] distinguish periodic-boundary finite systems from infinite configurations and offer general reachability-tree techniques, but do not give the explicit criterion for this eight-coefficient nonlinear family. Classical results on **additive** cellular automata [3,4] cover the linear specializations and their Laurent-polynomial reversibility theory. Those specializations are not claimed independently new: the new mathematical statement is a complete boundary comparison valid simultaneously for the nonlinear coefficient class, with sharp quantitative inverse locality and short witnesses. General reversible-CA theory also ensures that a bijective full-shift CA has a local inverse; the constructive \(E-1\) bound here is specific to this family.

## Limitations

The theorem assumes the precise coefficient conditions in [1]. It does not classify all polynomial rules outside that class, multidimensional lattices, or higher-neighborhood interactions. The inverse radius is a uniform maximum across admissible rules; individual inverse rules may use smaller windows. Earlier additive theorems already imply the linear case; an equivalent nonlinear application of general local-ring lifting theory may exist in unexamined literature. The cited older additive articles were available in bibliographic/abstract form but their entire texts were not inspected, so no whole-document novelty claim is made about them. There is no independent validation or claim of certified priority.

## References

[1] Baby C. J. and Kamalika Bhattacharjee, *Algebraic Characterization of Reversible First Degree Cellular Automata over \(\mathbb Z_d\)*, arXiv:2603.05253v1 (first publicly posted 2026-03-05), https://arxiv.org/html/2603.05253v1 .

[2] Kamalika Bhattacharjee and Sukanta Das, *On Finite 1-Dimensional Cellular Automata: Reversibility and Semi-reversibility*, arXiv:1903.06011v1, https://arxiv.org/html/1903.06011v1 .

[3] R. A. Dow, *Additive cellular automata and global injectivity*, Physica D (1997), https://doi.org/10.1016/S0167-2789(97)00074-2 .

[4] G. Manzini and L. Margara, *Invertible Linear Cellular Automata over \(\mathbb Z_m\): Algorithmic and Dynamical Aspects*, Journal of Computer and System Sciences (1998), https://doi.org/10.1006/jcss.1997.1535 .
