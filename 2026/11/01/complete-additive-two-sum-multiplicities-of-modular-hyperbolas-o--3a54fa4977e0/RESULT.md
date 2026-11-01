# Complete additive two-sum multiplicities of modular hyperbolas over odd finite chain rings

## Finding

Let \(R\) be a finite commutative chain ring with maximal ideal \(\mathfrak m=(\pi)\), odd residue-field cardinality \(q=|R/\mathfrak m|\), and nilpotency length \(k\geq1\). Thus \(\mathfrak m^k=0\), \(\mathfrak m^{k-1}\ne0\), and \(|R|=q^k\). Define the multiplicative hyperbola, viewed as a subset of the **additive** group \(R^2\), by

\[
H=\{(x,x^{-1}):x\in R^\times\}.
\]

Write \(r(s,t)=(\mathbf1_H*\mathbf1_H)(s,t)\) for its ordered two-sum representation function, and put \(U=(q-1)q^{k-1}=|R^\times|\). Define \(v(0)=k\) and \(v(z)=a\) when \(z\in\mathfrak m^a\setminus\mathfrak m^{a+1}\). Write \(\chi\) for the quadratic character of \(R/\mathfrak m\), extended by \(\chi(0)=0\).

**Theorem (full pointwise classification).** Every ordered two-sum count is determined as follows:

1. \(r(0,0)=U\). If \(v(s)\ne v(t)\), then \(r(s,t)=0\).
2. If \(v(s)=v(t)=a\) with \(1\le a<k\), choose unit factors \(s=\pi^a s_a\), \(t=\pi^a t_a\). Then
   \[
   r(s,t)=\begin{cases}2q^a,&\chi(-\overline{s_a}/\overline{t_a})=1,\\0,&\text{otherwise}.\end{cases}
   \]
   The reduced quotient is independent of the choices of unit factors.
3. If \(s,t\in R^\times\), set \(D=s^2-4s/t\). Then
   \[
   r(s,t)=\begin{cases}
   q^{\lfloor k/2\rfloor},&D=0,\\
   2q^j,&v(D)=2j<k\ \text{and}\ \chi(\overline{D/\pi^{2j}})=1,\\
   0,&\text{otherwise}.
   \end{cases}
   \]
   In the second line, \(D/\pi^{2j}\) means any unit factor and its residue-class square character is well defined.

These cases exhaust \(R^2\). In particular, this determines the complete two-sum support, including all singular valuation strata, for every finite commutative chain ring of odd residue-field order. The values and their multiplicities depend only on \((q,k)\), not on the ring's characteristic or presentation.

**Theorem (disjoint multiplicity strata).** Put \(J=\lfloor(k-1)/2\rfloor\). The nonzero entries of the function \(r\) comprise the following disjoint **families of positions**:

| Position family | Number of positions | Value of \(r\) |
|---|---:|---:|
| \((s,t)=(0,0)\) | \(1\) | \(U\) |
| Unit \(s,t\), \(D=0\) | \(U\) | \(q^{\lfloor k/2\rfloor}\) |
| Unit \(s,t\), \(v(D)=0\), square residue | \(U(q-3)q^{k-1}/2\) | \(2\) |
| Unit \(s,t\), \(v(D)=2j\), square unit part, \(1\le j\le J\) | \(U(q-1)q^{k-2j-1}/2\) | \(2q^j\) |
| \(v(s)=v(t)=a\), square condition, \(1\le a<k\) | \((q-1)^2q^{2(k-a-1)}/2\) | \(2q^a\) |

All unlisted positions have value zero. Families are disjoint, but their **values** can coincide; the multiplicities of equal values must be added. A family with empty index range contributes nothing, and the \(q=3\) unit-square family of value \(2\) is empty.

Consequently the exact additive energy is
\[
\boxed{\sum_{(s,t)\in R^2}r(s,t)^2
=3(q-1)q^{2k-2}\bigl(k(q-1)-1\bigr).}
\]
With the unnormalized additive Fourier transform, this is equivalent to the exact fourth-moment identity
\[
\boxed{\sum_{\gamma\in\widehat{R^2}}|\widehat{\mathbf1_H}(\gamma)|^4
=q^{2k}\,3(q-1)q^{2k-2}\bigl(k(q-1)-1\bigr).}
\]

The two-sum support cardinality is also exact:
\[
\begin{split}
|H+H|={}&1+U\left(1+\frac{(q-3)q^{k-1}}2
+\frac{q-1}{2}\sum_{j=1}^{\lfloor(k-1)/2\rfloor}q^{k-2j-1}\right)\\
&+\frac{(q-1)^2}{2}\sum_{a=1}^{k-1}q^{2(k-a-1)}.
\end{split}
\]
For any fixed odd prime power \(q\), this has the limiting density
\[
\boxed{\lim_{k\to\infty}\frac{|H+H|}{|R|^2}
=\frac{q-1}{2q^2}\left(q-3+\frac2{q+1}\right).}
\]
Thus this density is \(1/18\) for residue-field size three, whereas for residue-field size five it is \(14/75\). The exceptional behavior at three is caused by the disappearance of the unit, nonzero-square-discriminant family.

## Assumptions and scope

The ring is commutative, finite, local, principal with linearly ordered ideals, and its residue-field characteristic is odd. No assumption of cyclic additive group, unramifiedness, or equal characteristic is made. The convolution is on the full additive group \(R^2\); it is not coordinate summation of the two entries of one point of the hyperbola. The Fourier transform is unnormalized, and the two-sum count uses **ordered pairs**, including repetitions.

## Proof

**1. Reduction to a quadratic congruence.** Each point of \(H\) has a unique parameter \(x\in R^\times\). For a representation of \((s,t)\), write its parameters as \(x,y\in R^\times\). Then
\[
s=x+y,\qquad t=x^{-1}+y^{-1}=s/(xy).
\]
Because \(xy\) is a unit, \(v(s)=v(t)\); moreover \(s=0\) if and only if \(t=0\). In that case \(y=-x\) and there are \(U\) ordered representations.

Assume \(v(s)=v(t)=a<k\), and choose unit factors \(s=\pi^a s_a\), \(t=\pi^a t_a\). The relation \(t x(s-x)=s\) is equivalent to
\[
x^2-sx+s_a/t_a=0\pmod{\pi^{k-a}}.
\]
The quotient \(s_a/t_a\) in \(R/\pi^{k-a}R\) is independent of the choice of factors. Every root is a unit because its constant term is a unit; then \(y=s-x\) is also a unit since it has unit product with \(x\). Each root modulo \(\pi^{k-a}\) lifts to exactly \(q^a\) possibilities for \(x\in R\). Completing the square (\(2\) is invertible) gives discriminant
\[
D_a=s^2-4s_a/t_a\pmod{\pi^{k-a}}.
\]

**2. Nonunit and unit strata.** If \(a\ge1\), then \(D_a\) is a unit and its residue class equals \(-4\overline{s_a}/\overline{t_a}\). The derivative of the square map is invertible at every unit root in odd residue characteristic; Hensel lifting therefore gives precisely two roots when the reduced discriminant is square, and none otherwise. Incorporating the \(q^a\) lifts gives the second pointwise case.

If \(a=0\), we work directly in \(R\) with \(D=s^2-4s/t\). For \(D=0\), solutions to \(z^2=0\) are exactly \(z\in\mathfrak m^{\lceil k/2\rceil}\), giving \(q^{\lfloor k/2\rfloor}\) roots. If \(D\ne0\), the valuation of a square is even. Writing \(D=\pi^{2j}u\), with \(2j<k\), the equation \(z^2=D\) forces \(z\in\mathfrak m^j\setminus\mathfrak m^{j+1}\), and division by \(\pi^{2j}\) leaves the unit-square congruence modulo \(\pi^{k-2j}\). It has two Hensel roots if and only if \(\chi(\bar u)=1\), each with \(q^j\) lifts, for a total \(2q^j\). This proves the complete pointwise classification.

**3. Counting all nonzero values.** The number of elements of valuation exactly \(a<k\) is \(N_a=(q-1)q^{k-a-1}\). For each fixed \(s\) of valuation \(a\ge1\), precisely half of the \(N_a\) eligible \(t\)'s pass the square-class test, producing \(N_a^2/2\) positions with value \(2q^a\).

For fixed unit \(s\), the map \(t\mapsto D=s^2-4s/t\) bijects the units \(t\) with elements \(D\in R\) whose residues are **not** \(\bar s^2\). Exactly one has \(D=0\). Of the \(q\) residue classes, \((q-3)/2\) are nonzero squares other than \(\bar s^2\), and each has \(q^{k-1}\) lifts. For \(1\le j\le J\), exactly \((q-1)q^{k-2j-1}/2\) such \(D\)'s have valuation \(2j\) and square unit part. Multiply by the \(U\) choices of unit \(s\). These disjoint counts prove the table. Summing value times multiplicity recovers \(U^2\), as required for a convolution square.

**4. Energy, Fourier moment, and support density.** Squaring each table value and summing, including coincidences between rows, gives
\[
\begin{split}
\sum r^2={}&U^2+Uq^{2\lfloor k/2\rfloor}
+2U(q-3)q^{k-1}\\
&+2\lfloor(k-1)/2\rfloor U(q-1)q^{k-1}
+2(k-1)(q-1)^2q^{2k-2}.
\end{split}
\]
For odd and even \(k\) separately, simplifying yields \(3(q-1)q^{2k-2}(k(q-1)-1)\). The Fourier fourth moment follows from Parseval applied to \(\widehat r=\widehat{\mathbf1_H}^{\,2}\), with group cardinality \(q^{2k}\).

Counting the positions in the nonzero table gives the displayed support formula. After division by \(q^{2k}\), the finite geometric sums for the two valuation families both tend to \((q-1)/(2q^2(q+1))\); the unit nonzero-square term contributes \((q-1)(q-3)/(2q^2)\), while the zero-discriminant and zero-sum single strata vanish in density. This proves the limit.

## Verification

A standalone, dependency-free script, `check_exact.py`, computes all ordered pairs of points and compares the **complete histogram of output multiplicities**, including zero positions, with the theorem. It also separately checks total mass and energy. The following instances were executed exactly:

- Cyclic rings \(\mathbb Z/p^k\mathbb Z\): \((p,k)=(3,1),(3,2),(3,3),(3,4),(5,1),(5,2),(5,3),(7,2)\).
- Equal-characteristic noncyclic rings \(\mathbb F_3[\epsilon]/(\epsilon^2)\) and \(\mathbb F_5[\epsilon]/(\epsilon^2)\).
- A residue-field extension, \(\mathbb F_9[\epsilon]/(\epsilon^2)\), with \(\mathbb F_9=\mathbb F_3[u]/(u^2+1)\).

Every test passed. Representative support sizes are \(9\) at \((q,k)=(3,2)\), \(129\) at \((5,2)\), and \(2049\) at \((9,2)\). The script verifies finite examples, not the quantified theorem; the proof above establishes all cases.

## Relationship to prior work

Kowalski's 2010 discussion of the fourth moment of finite-field Kloosterman sums explicitly uses the two symmetric quantities \(x+y\) and \(x^{-1}+y^{-1}\), and identifies the opposite-pair collision at zero. That gives the **field-level** core of the present classification; no originality is claimed for it. Gong–Veys–Wan (first circulated 2013) derive moment formulas for classical Kloosterman sums over prime-power cyclic rings, including their treatment of singular contributions. The aggregate fourth-moment formula for cyclic rings should therefore not be read as an independent priority claim. Bower–Evans–Luo–Miller (first circulated 2012) count **coordinate** sumsets \(\{x+y:(x,y)\in H\}\) for modular hyperbolas, which are different from the planar Minkowski sum \(H+H\).

The assessed contribution is the **complete pointwise and stratified distribution of the planar twofold convolution across all odd finite commutative chain rings**, including noncyclic rings, plus its explicit ring-universal support counts and limiting density. The existing moment and coordinate-sum theorems do not by themselves specify this distribution. Possible equivalent descriptions in wider local-congruence or harmonic-analysis literature remain a priority risk.

## Limitations

No even-residue-characteristic case is claimed. The result classifies **twofold** additive convolution and its constant-input Fourier fourth moment; it does not give sharp weighted \(L^2\to L^4\) extension constants, arbitrary higher-fold convolutions, or the full Kloosterman eigenvalue distribution. The characterization is proved for commutative chain rings, not arbitrary finite local rings. Priority has been evaluated through accessible sources and is not independently established.

## References

1. E. Kowalski, *The fourth moment of Kloosterman sums*, public exposition dated 2010-02-26, https://blogs.ethz.ch/kowalski/2010/02/26/the-fourth-moment-of-kloosterman-sums/.
2. A. Bower, R. Evans, V. Luo, S. J. Miller, *Coordinate sum and difference sets of d-dimensional modular hyperbolas*, arXiv:1212.2930, first posted 2012-12-12, https://arxiv.org/abs/1212.2930.
3. K. Gong, W. Veys, D. Wan, *Power moments of Kloosterman sums*, arXiv:1306.4104, first posted 2013-06-18, https://arxiv.org/abs/1306.4104.
