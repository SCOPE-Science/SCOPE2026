# No nontrivial positive cycles for the \(\{2,3\}\)-arithmetic subderivative

## Finding
For a positive integer \(n\), define the arithmetic subderivative with respect to \(S=\{2,3\}\) by
\[
D_{\{2,3\}}(n)
=n\left(\frac{\nu_2(n)}2+\frac{\nu_3(n)}3\right).
\]
If there is an integer \(L\ge1\) such that
\[
D_{\{2,3\}}^L(n)=n,
\]
then in fact
\[
D_{\{2,3\}}(n)=n.
\]
Thus there are no positive cycles of length greater than one.

The positive periodic points are exactly
\[
n=4m
\]
or
\[
n=27m,
\]
where
\[
\gcd(m,6)=1.
\]

## Assumptions and scope
The domain is the positive integers. The notation \(\nu_p(n)\) denotes the exponent of the prime \(p\) in \(n\), and \(D_{\{2,3\}}^L\) denotes \(L\)-fold functional iteration.

The theorem is specific to the two-prime set \(\{2,3\}\). It does not classify periodic points for arbitrary finite prime sets. If the map is extended to \(0\) in the standard way, then \(0\) is an additional fixed point; the theorem here concerns positive integers only.

## Proof
Suppose a positive orbit is periodic with period dividing \(L\). Write its terms as
\[
x_j=c_j2^{a_j}3^{b_j},
\qquad
\gcd(c_j,6)=1,
\]
for \(j\) taken modulo \(L\). Because all orbit terms are positive, at each step at least one of \(a_j,b_j\) is positive. Set
\[
m_j=3a_j+2b_j>0.
\]
Then
\[
D_{\{2,3\}}(x_j)
=c_j2^{a_j-1}3^{b_j-1}m_j.
\]
Factor
\[
m_j=2^{r_j}3^{s_j}u_j,
\qquad
\gcd(u_j,6)=1.
\]
The next term therefore has
\[
c_{j+1}=c_ju_j,
\]
\[
a_{j+1}=a_j-1+r_j,
\qquad
b_{j+1}=b_j-1+s_j.
\]

Since the orbit is periodic,
\[
c_L=c_0.
\]
Every \(u_j\) is a positive integer, so
\[
\prod_{j=0}^{L-1}u_j=1
\]
forces
\[
u_j=1
\]
for every \(j\). Hence each \(m_j\) is \(3\)-smooth:
\[
m_j=2^{r_j}3^{s_j}.
\]
Summing the exponent recurrences around the cycle gives
\[
\sum_{j=0}^{L-1}r_j=L,
\qquad
\sum_{j=0}^{L-1}s_j=L.
\]
Consequently
\[
\prod_{j=0}^{L-1}m_j
=2^L3^L
=6^L.
\]

We now show that no \(m_j<6\) can occur on a positive periodic orbit. Since
\[
m_j=3a_j+2b_j
\]
with nonnegative integers \(a_j,b_j\), the positive values below \(6\) are \(2,3,4,5\).

If \(m_j=2\), then \((a_j,b_j)=(0,1)\), so
\[
x_j=3c_j,
\qquad
D_{\{2,3\}}(x_j)=c_j,
\]
and the next derivative is \(0\). This cannot lie on a positive periodic orbit.

If \(m_j=3\), then \((a_j,b_j)=(1,0)\), so
\[
x_j=2c_j,
\qquad
D_{\{2,3\}}(x_j)=c_j,
\]
and again the next derivative is \(0\).

If \(m_j=4\), then \((a_j,b_j)=(0,2)\). The next exponent pair is
\[
(a_{j+1},b_{j+1})=(1,1),
\]
so
\[
m_{j+1}=5.
\]
But \(5\) has coprime factor \(u_{j+1}=5\), contradicting the already proved condition \(u_{j+1}=1\).

Finally, \(m_j=5\) itself has \(u_j=5\), again impossible. Therefore
\[
m_j\ge6
\]
for every \(j\). Since their product is exactly \(6^L\), every factor must equal \(6\):
\[
m_j=6.
\]
The nonnegative solutions of
\[
3a+2b=6
\]
are exactly
\[
(a,b)=(2,0)
\]
and
\[
(a,b)=(0,3).
\]
Each is fixed by the exponent update, and the coprime coefficient is unchanged. Thus every positive periodic point is fixed.

For completeness, the fixed-point equation itself is
\[
\frac{a}{2}+\frac{b}{3}=1,
\]
whose nonnegative solutions are the same two pairs. Hence the positive periodic points are precisely \(4m\) and \(27m\) with \(\gcd(m,6)=1\).

## Verification
The accompanying `verify.py` implements \(D_{\{2,3\}}\) directly from integer valuations and independently implements the exponent-pair transition used in the proof.

It checks all exponent pairs
\[
0\le a,b\le200
\]
for agreement between the symbolic transition and direct integer evaluation on several coprime coefficients. It then searches the finite transition graph in that box for closed trajectories whose coprime multiplier returns to its starting value and confirms that the only such positive closed states are
\[
(2,0)
\]
and
\[
(0,3).
\]
It also verifies the fixed-point formula for every positive integer up to \(200000\).

These finite checks are regression evidence only. The exclusion of all nontrivial positive cycles is proved symbolically above.

## Relationship to prior work
Merikoski, Haukkanen, and Tossavainen introduced arithmetic subderivatives in 2019. Emmons and Xiao later studied the one-prime arithmetic partial derivative and explicitly described finite-set arithmetic subderivatives as a natural next step for the dynamical questions arising from arithmetic differentiation.

A 2026 paper of Talukdar and Saikia studies iterates of generalized subderivatives, proves criteria for vanishing, and determines fixed points. Its fixed-point theorem already covers the two fixed families \(4m\) and \(27m\) appearing above. The new content here is not that fixed-point classification; it is the proof that for \(S=\{2,3\}\) there are no additional positive periodic cycles of any length.

The inspected 2025 generalized-subderivative paper concerns algebraic properties, while the inspected 2026 eigenpoint paper concerns integer eigenpoints. Targeted searches for periodic points, cycles, and the special set \(\{2,3\}\) did not locate a prior theorem excluding nontrivial cycles.

## Limitations
The argument uses the special small-smooth structure of
\[
3a+2b
\]
and the fact that the product identity forces an average multiplicative size exactly \(6\). It does not immediately extend to arbitrary two-prime sets \(\{p,q\}\) or to larger finite sets.

The literature search cannot exclude an equivalent result in an unindexed source. The fixed-point portion of the conclusion is prior-covered and is included only to state the complete periodic set; originality is claimed only for the exclusion of nontrivial positive cycles for \(S=\{2,3\}\).

## References
1. Jorma K. Merikoski, Pentti Haukkanen, Timo Tossavainen, “Arithmetic Subderivatives and Leibniz-Additive Functions,” arXiv:1901.02216v1, first public 8 January 2019; Annales Mathematicae et Informaticae 50 (2019), 145–157; primary MSC \(11A25\).
2. Brad Emmons, Xiao Xiao, “The Arithmetic Partial Derivative,” arXiv:2201.12453v1, first public 28 January 2022; Journal of Integer Sequences 25 (2022).
3. Champak Talukdar, Helen K. Saikia, “Arithmetic Subderivatives Relative to Subsets of Primes,” Communications in Mathematics and Applications 16 (2025).
4. Champak Talukdar, Helen K. Saikia, “Arithmetic Differential Equations Defined by Generalized Subderivatives,” International Journal of Mathematics Trends and Technology 72 (2026), 21–27, DOI:10.14445/22315373/IJMTT-V72I1P104.
5. Champak Talukdar, Helen K. Saikia, “Prime-Supported Leibniz-Additive Functions and Integer Eigenpoints of Generalized Arithmetic Subderivatives,” Far East Journal of Mathematical Sciences 143 (2026), 1057–1071.
