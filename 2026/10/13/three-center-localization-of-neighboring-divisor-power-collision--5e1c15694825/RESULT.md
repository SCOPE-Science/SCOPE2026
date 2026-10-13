# Three-center localization of neighboring divisor-power collisions

## Finding
For an integer exponent \(d\ge2\), set \(\sigma_d(n)=\sum_{a\mid n}a^d\). The following result is proved for **every even** \(d\ge6\), with no bound on \(n\): if
\[\sigma_d(n)=\sigma_d(n+1),\]
then \(n\) is even. Set
\[\alpha(n)=\mathbf 1_{3\mid n}-\mathbf 1_{3\mid n+1}\in\{-1,0,1\}.\]
Then
\[\boxed{\left|n-d2^d+\alpha(n)d(4/3)^d\right|<5d.}\]
In particular the collision index must lie in one of three intervals of radius \(5d\), whose centers are \(d2^d\) and \(d2^d\pm d(4/3)^d\). Its residue modulo \(3\) uniquely selects the center. For each fixed exponent this leaves at most \(30d+O(1)\) integers to test, independent of any height cutoff.

## Assumptions and scope
All divisors are positive. The exponent \(d\) is an **even integer at least \(6\)**. The start \(n\) is any positive integer. No unproved distribution theorem is used. Nothing here asserts that a collision exists. The proof in fact gives the same localization for all integer exponents \(d\ge6\), although the new statement is restricted to the even-exponent case.

## Proof
**Parity direction.** Write \(R_d(m)=\sigma_d(m)/m^d=\sum_{a\mid m}a^{-d}\). For odd \(m\) and \(d\ge2\),
\[R_d(m)\le1+\sum_{j\ge3,\ j\text{ odd}}j^{-d}<1+2^{-d}.\]
The final inequality follows by comparing the summands \( (2/j)^d\le(2/j)^2\) and the strict bound \(\sum_{j\ge3,\ j\text{ odd}}j^{-2}<1/4\). The latter follows by the midpoint integral estimate for the positive decreasing convex function \((2t+1)^{-2}\) on \(t\ge1/2\). For even \(m\), \(R_d(m)\ge1+2^{-d}\). Therefore if \(n\) were odd, the larger even integer \(n+1\) would have strictly larger \(\sigma_d\), contradicting equality. Hence \(n\) is even.

**Uniform reciprocal-divisor approximation.** Put \(u=2^{-d}\), \(v=3^{-d}\), \(A=R_d(n)\), and \(B=R_d(n+1)\). Let \(\delta_m=\mathbf1_{3\mid m}\). Because \(n\) is even and \(n+1\) odd,
\[A=1+u+\delta_n v+E_n,\qquad B=1+\delta_{n+1}v+E_{n+1},\]
where \(0\le E_m\le\sum_{j=4}^\infty j^{-d}\le4^{-d}(1+4/(d-1))\le1.8u^2\) for every \(d\ge6\). Also \(v/u=(2/3)^d\le(2/3)^6<0.088\), and \(u\le1/64\). Thus \(0\le A-1<1.117u\) and \(0\le B-1<0.117u\). Using \(0\le t-\log(1+t)\le t^2/2\) for \(t\ge0\), and \(\alpha=\delta_n-\delta_{n+1}\), gives
\[D:=\log(A/B)=u+\alpha v+\eta,\qquad |\eta|<3u^2.\]
Indeed, the residual from \(E_n-E_{n+1}\) is at most \(1.8u^2\), and the two logarithmic errors total less than \(0.5(1.117^2+0.117^2)u^2<0.64u^2\).

**Inverting the equality.** The assumed equality implies \(A/B=((n+1)/n)^d\), hence \(D=d\log(1+1/n)>0\). Set \(q=v/u=(2/3)^d\) and \(t=\alpha q+\eta/u\). Then \(D=u(1+t)\), where \(|t|<q+3u<0.135\). We use the elementary inequality
\[0<\frac1y-\frac1{e^y-1}<1\qquad(y>0),\]
so, taking \(y=D/d\),
\[\left|n-\frac dD\right|<1.\]
The identity \(1/(1+t)=1-t+t^2/(1+t)\) now yields
\[\left|n-\frac d u(1-\alpha q)\right|
<1+\frac du\left(3u+\frac{(q+3u)^2}{1-q-3u}\right).\]
For \(d\ge6\), \(q^2/u=(8/9)^d<0.5\), \(6q<0.528\), \(9u\le9/64<0.141\), and \(1-q-3u>0.865\). It follows that the right side is less than
\[1+d\left(3+\frac{0.5+0.528+0.141}{0.865}\right)<5d.\]
Finally, \(d/u=d2^d\) and \((d/u)q=d(4/3)^d\), proving the theorem. The \(30d+O(1)\) count follows by intersecting the three real intervals of radius \(5d\) with the integers, without assuming that they are disjoint.

## Verification
The proof is symbolic and unrestricted. The standalone standard-library program `verify.py` checks the elementary analytic inequalities numerically at many exponents, computes exact power-divisor sums for consecutive small integers, and checks whether every observed equality satisfies the stated strict bound. Computations are sanity checks only: they do not establish the all-exponents/all-integers theorem.

## Relationship to prior work
Lebowitz-Lockard and Saunders (arXiv:2402.06832, initially submitted 2024-02-09), Remark 1, explicitly explain a method for **odd** divisor-power exponents and its failure for **even** ones; their bound concerns maximal constant-string lengths, not localization of neighboring even-power equalities. Lebowitz-Lockard and Vandehey (J. Integer Sequences 26, article 23.8.4, 2023) study constant strings for other arithmetic functions. The classical square-power adjacent equality \(\sigma_2(6)=\sigma_2(7)=50\), with no others, is recorded in ProofWiki and OEIS A372114. These results neither state nor imply the three-center uniform \(O(d)\)-width localization for all even \(d\ge6\). This is a relative literature assessment, not a claim of exhaustive bibliographic novelty.

## Limitations
The result is necessary, not sufficient. It does not determine whether any equal neighboring values occur for any given exponent \(d\ge6\), nor does it classify exponents \(d=2,4\). The three windows are uniform coarse intervals; their centers may have no solutions. Some relevant older literature may not be indexed.

## References
1. N. Lebowitz-Lockard and J. C. Saunders, *Arithmetic functions that remain constant on strings of integers*, arXiv:2402.06832, v1 dated 2024-02-09, especially Remark 1. https://arxiv.org/html/2402.06832v4
2. N. Lebowitz-Lockard and J. Vandehey, *Arithmetic Functions that Remain Constant on Runs of Consecutive Integers*, Journal of Integer Sequences 26 (2023), 23.8.4. https://cs.uwaterloo.ca/journals/JIS/VOL26/Lebowitz/lebo10.html
3. *Consecutive Integers whose Sums of Squares of Divisors are Equal*, ProofWiki. https://proofwiki.org/wiki/Consecutive_Integers_whose_Sums_of_Squares_of_Divisors_are_Equal
4. OEIS A372114 (square-divisor sums at a two-unit separation). https://oeis.org/A372114
