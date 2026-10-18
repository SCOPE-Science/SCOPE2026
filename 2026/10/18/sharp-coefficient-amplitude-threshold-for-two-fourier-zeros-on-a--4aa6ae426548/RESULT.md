# Sharp coefficient-amplitude threshold for two Fourier zeros on a prime parabola

## Finding
Fix a prime \(p\ge5\), three distinct elements \(x_1,x_2,x_3\in\mathbb F_p\), and nonzero complex coefficients \(c_1,c_2,c_3\). With \(\omega=\exp(2\pi i/p)\), let
\[
F(a,b)=\sum_{j=1}^{3}c_j\omega^{a x_j^2+b x_j},\qquad(a,b)\in\mathbb F_p^2.
\]
The number of zeros of \(F\) is at most two, and the following **sharp quantitative characterization of two-zero signals** holds. Set \(q=\lfloor p/3\rfloor\) and
\[
R_p=\frac{\sin(\pi(q+1)/p)}{\sin(\pi q/p)}.
\]
If \(F\) has two distinct zeros, then
\[
\boxed{\frac{\max_j|c_j|}{\min_j|c_j|}\ge R_p>1.}
\]
For every fixed ordered support triple, equality is attained. When \(p\ge7\), equality holds **if and only if**, writing the two zeros as \(v_0,v_1\), the three roots
\[
u_j=\omega^{(v_1-v_0)\cdot(x_j^2,x_j)},\qquad j=1,2,3,
\]
have successive positive cyclic gaps, in some order, \((q,q,q+1)\) if \(p=3q+1\), or \((q,q+1,q+1)\) if \(p=3q+2\). At \(p=5\), every three-element subset of the fifth roots of unity gives equality. The coefficient ray associated with an unordered zero pair is uniquely determined by the two linear zero equations.

The number of projective coefficient rays with exactly two zeros and **minimum possible amplitude ratio** is therefore exactly
\[
\boxed{\begin{cases}6p^2,&p=5,\\3p^2,&p\ge7.\end{cases}}
\]
Furthermore \(R_p=1+\pi/(\sqrt3\,p)+O(p^{-2})\) along primes. The statement concerns actual amplitude imbalance, not the already known equal-amplitude one-zero theorem.

## Assumptions and scope
All finite-field calculations use the prime field \(\mathbb F_p\), \(p\ge5\). The Fourier sum is unnormalized; multiplying it by any nonzero scalar changes neither its zeros nor its coefficient dynamic range. A coefficient ray is \([c_1:c_2:c_3]\in\mathbb{CP}^2\) with all coordinates nonzero. Only exact zeros are counted. The given support consists of three **distinct** elements, so the corresponding parabola points are affinely independent. Cyclic gaps of three different \(p\)-th roots mean the positive integer arc lengths in cyclic order, summing to \(p\). The origin and orientation of the frequency difference do not affect the gap multiset.

## Proof
**Step 1 (full root-grid coordinates and at most two zeros).** Put \(P_j=(x_j^2,x_j)\). For any \(v=(a,b)\) the two differences \(v\cdot(P_2-P_1)\), \(v\cdot(P_3-P_1)\) give an invertible linear change of coordinates on \(\mathbb F_p^2\), since its determinant is, up to sign,
\[
(x_2-x_1)(x_3-x_1)(x_3-x_2)\ne0.
\]
Consequently the zero-count problem reduces, up to a harmless nonzero character factor, to \(C_1+C_2\omega^r+C_3\omega^s=0\) over all \((r,s)\in\mathbb F_p^2\), with all \(C_j\ne0\). For a solution, \(|C_1+C_2\omega^r|=|C_3|\). Squaring gives a fixed real affine-line condition on the unit-circle point \(\omega^r\), because \(C_1\overline C_2\ne0\). A line meets the circle in at most two points, and for each such \(r\) there is at most one \(s\). Thus there are at most two zeros. This standard upper bound is prior mathematical knowledge, not a new part of the result.

**Step 2 (two-zero null vector).** Suppose \(v_0\ne v_1\) are zeros. Define
\[
d_j=c_j\omega^{v_0\cdot P_j},\quad u_j=\omega^{(v_1-v_0)\cdot P_j}.
\]
The zero equations are \(\sum_jd_j=\sum_j u_jd_j=0\). If precisely two \(u_j\) coincide, subtracting a multiple of the first equation from the second forces the third \(d_j\) to vanish, impossible. If all coincide, the quadratic polynomial \((v_1-v_0)\cdot(x^2,x)\) is constant at three distinct \(x_j\); its difference from that constant has three roots, so it is identically zero and \(v_1=v_0\), also impossible. Hence \(u_1,u_2,u_3\) are pairwise distinct. The two independent zero equations have a one-dimensional kernel, whose projective generator is
\[
(d_1,d_2,d_3)=(u_2-u_3,\;u_3-u_1,\;u_1-u_2).
\]
Therefore the three coefficient magnitudes are exactly the three chord lengths joining the root triple \(\{u_1,u_2,u_3\}\), up to one common factor.

**Step 3 (sharp polygon chord lemma).** Let \(n_1,n_2,n_3\) be the positive cyclic gaps of three distinct \(p\)-th roots, with sum \(p\). Their chord lengths are \(2\sin(\pi n_i/p)\). If one gap exceeds \(p/2\), let \(k\) be the sum of the other two. Since their smaller gap is at most \(k/2\), the ratio of longest to shortest chord is at least
\[
\frac{\sin(\pi k/p)}{\sin(\pi k/(2p))}=2\cos\left(\frac{\pi k}{2p}\right)>\sqrt2.
\]
For primes \(p\ge11\) the balanced gap triple has chord ratio strictly less than \((q+1)/q\le4/3<\sqrt2\), using the strict decrease of \(\sin t/t\) on \((0,\pi)\). For \(p=7\), the balanced ratio is \(\sin(3\pi/7)/\sin(2\pi/7)<\sqrt2\), since \(\sin(2\pi/7)>1/\sqrt2\). Thus an optimal triple for \(p\ge7\) has all its gaps below \(p/2\), where the sine is strictly increasing. Whenever the largest and smallest gaps differ by at least two, moving one unit from a largest to a smallest gap strictly decreases the largest-to-smallest sine ratio: its numerator cannot increase, its denominator cannot decrease, and at least one changes strictly. Iterating proves the unique minimizing gap multiset is balanced, as stated, and its exact ratio is \(R_p\). Since a prime \(p\ge5\) is not divisible by three, \(R_p>1\). For \(p=5\), direct enumeration of positive partitions of five into three parts gives the two multisets \((1,1,3)\) and \((1,2,2)\), both with chord ratio \(\sin(2\pi/5)/\sin(\pi/5)=R_5\), exhausting every triple.

**Step 4 (realizability on every support).** For any ordered root triple \((u_1,u_2,u_3)\) considered modulo a common root-of-unity factor, the invertible difference-coordinate map of Step 1 supplies a unique nonzero displacement \(v_1-v_0\) realizing its two root ratios. Fix any \(v_0\) and select coefficients by undoing the phases \(\omega^{v_0\cdot P_j}\) in the cofactor vector of Step 2. These coefficients are all nonzero and vanish at both prescribed frequencies. Step 1 rules out a third zero. Hence the sharp ratio and every equality type occur for every fixed support.

**Step 5 (exact equality-ray count).** For \(p\ge7\), the balanced three-vertex subsets of a labeled regular \(p\)-gon number exactly \(p\): the single exceptional-length gap uniquely marks their cyclic origin. Thus precisely three balanced subsets contain the vertex \(1\), and ordering the other two vertices gives six possible ordered root ratios \((u_2/u_1,u_3/u_1)\). Via Step 1 there are exactly six admissible nonzero frequency displacements. At \(p=5\), all \(\binom42=6\) rooted triples work, giving twelve ordered root ratios and displacements. Each of the \(p^2\) choices of first zero and each admissible displacement specify one projective coefficient ray. Each ray has exactly two zeros by Step 1, hence is counted exactly twice by the ordered zero pairs. Dividing by two gives \(3p^2\) or \(6p^2\) as stated. Finally, Taylor's theorem at \(\pi/3\) yields \(R_p=1+\pi/(\sqrt3 p)+O(p^{-2})\).

## Verification
Run `python verify.py` using Python 3's standard library. The script checks every nonzero frequency displacement with three distinct phases for each of 23 primes from 5 to 97, compares the resulting chord ratio to \(R_p\), and checks that precisely 12 displacements attain equality at \(p=5\) and precisely 6 do so at every other tested prime. It constructs the cofactor coefficients and checks the two prescribed zeros and equality ratio. At primes 5, 7, 11, and 13 it additionally tests the entire finite frequency grid of each equality construction for exactly two zeros. All checks are numerical with explicit tolerances; they support but do not replace the analytic infinite-prime proof.

## Relationship to prior work
Dongwei Li proved the sharp upper bound of two zeros for three-point finite-parabola Fourier sums with arbitrary nonzero complex coefficients (arXiv:2609.16030, Theorem 4.4). A published exact three-sparse Fourier-support-spectrum classification over elementary Abelian odd-prime groups also establishes the two-zero possibility on noncollinear three-point supports. Both results concern zero **counts** and do not bound the relative magnitudes necessary to attain two zeros. A previously published phase-only theorem on finite parabolas proves at most one zero for equal-magnitude coefficients and counts its equality rays; neither the phase-only result nor its separate nonzero-frequency gap is claimed again here. The current result quantifies the exact amplitude transition from one to two zeros, completely classifies equality, and counts its coefficient rays.

A published sharp Riesz-conditioning theorem for three cyclic sampling sites independently identifies the same balanced **gap geometry** as the optimum of a different spectral condition-number functional. The geometry of balanced root triples is therefore not asserted as a new standalone phenomenon. That spectral theorem does not imply the ratio of magnitudes in the cofactor kernel of two parabolic Fourier zero equations, or the exact number of corresponding coefficient rays. The present proof makes that connection explicitly, including the exceptional fifth-root count.

## Limitations
The result assumes a three-point parabola support over a prime field, nonzero complex coefficients, and exact zero constraints. It does not address approximate Fourier zeros, larger supports, composite rings, or the smallest Euclidean perturbation of a given coefficient vector. The exact counting is modulo arbitrary nonzero complex scalar. The finite computations are supplementary. Earlier geometric chord-ratio formulations outside the searched literature may exist, so absolute historical priority is not certified; independent mathematical audit has not been performed.

## References
1. Dongwei Li, *Parity-Sensitive Fourier Uncertainty and Zero-Set Rigidity on the Finite Parabola*, arXiv:2609.16030, first posted 2026-09-11, https://arxiv.org/abs/2609.16030 .
2. *Exact three-sparse Fourier support spectra on elementary Abelian odd-prime groups*, public research record, 2026-10-04, identifier `ca0d22e76a34`.
3. *Fourier-zero rigidity for unimodular three-point signals on cyclic groups*, public research record, 2026-10-04, identifier `a8ba65401394`.
4. *Sharp Riesz conditioning for consecutive triples on finite cycles*, public research record, 2026-10-11, identifier `1200745c9cae`.
