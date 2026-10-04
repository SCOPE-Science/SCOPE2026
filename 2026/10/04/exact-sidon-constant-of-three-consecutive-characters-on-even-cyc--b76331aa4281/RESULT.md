# Exact Sidon constant of three consecutive characters on even cyclic groups
## Finding
For every even integer \(N\ge 4\), write \(\zeta=e^{2\pi i/N}\). The Sidon constant of the character set \(E=\{0,1,2\}\subset \widehat{\mathbb Z_N}\),
\[
S_N(E)=\sup_{(c_0,c_1,c_2)\ne0}\frac{|c_0|+|c_1|+|c_2|}{\max_{k\in\mathbb Z_N}|c_0+c_1\zeta^k+c_2\zeta^{2k}|},
\]
is exactly
\[
S_N(E)=\sqrt{1+\sec^2(\pi/N)}.
\]
In particular \(S_4(E)=\sqrt3\), while \(S_N(E)>\sqrt2\) for every finite even \(N\) and \(S_N(E)\downarrow\sqrt2\) as \(N\to\infty\).

## Assumptions and scope
The group is the finite cyclic group \(\mathbb Z_N\) with even \(N\ge4\), and the three characters are the residue classes \(0,1,2\). The result concerns the complex Sidon constant defined by the displayed coefficient \(\ell^1\)-to-supremum ratio. The case \(N=2\) is excluded because the three displayed frequencies are not distinct. No claim is made here for odd \(N\) or for other three-point frequency sets.

## Proof
Let
\[
M=\max_{k\in\mathbb Z_N}|c_0+c_1\zeta^k+c_2\zeta^{2k}|,
\]
and put \(a=|c_0|\), \(b=|c_1|\), and \(c=|c_2|\). Because \(N\) is even, replacing \(k\) by \(k+N/2\) changes the sign of \(\zeta^k\) but not of \(\zeta^{2k}\). With
\[
A_k=c_0+c_2\zeta^{2k},\qquad B_k=c_1\zeta^k,
\]
the parallelogram identity gives
\[
\max\{|A_k+B_k|^2,|A_k-B_k|^2\}\ge |A_k|^2+|B_k|^2.
\]
Hence
\[
M^2\ge b^2+\max_{0\le k<N/2}|c_0+c_2\zeta^{2k}|^2.
\]
The numbers \(\zeta^{2k}\), for \(0\le k<N/2\), are the \(N/2\)-th roots of unity. Whatever the relative phase of \(c_0\) and \(c_2\), one of those roots lies within angular distance \(2\pi/N\) of perfect alignment. Therefore
\[
\max_{0\le k<N/2}|c_0+c_2\zeta^{2k}|^2\ge a^2+c^2+2ac\cos(2\pi/N).
\]
Set \(q=\cos^2(\pi/N)\). Since \(\cos(2\pi/N)=2q-1\),
\[
a^2+c^2+2ac\cos(2\pi/N)-q(a+c)^2=(1-q)(a-c)^2\ge0.
\]
Thus, with \(u=a+c\),
\[
M^2\ge b^2+q u^2.
\]
Weighted Cauchy--Schwarz now yields
\[
(u+b)^2\le (1+q^{-1})(qu^2+b^2),
\]
so
\[
\frac{a+b+c}{M}\le\sqrt{1+q^{-1}}=\sqrt{1+\sec^2(\pi/N)}.
\]

It remains to attain the bound. Put \(\alpha=\pi/N\), \(q=\cos^2\alpha\), and choose
\[
c_0=1,\qquad c_2=e^{2i\alpha},\qquad c_1=2q\,e^{i(\alpha+\pi/2)}.
\]
For \(z=e^{it}\),
\[
c_0+c_2z^2=2e^{i(t+\alpha)}\cos(t+\alpha),
\]
while \(c_1z=2q e^{i(t+\alpha+\pi/2)}\); these two summands are orthogonal for every \(t\). On the grid \(t=2\pi k/N\), the largest value of \(|\cos(t+\alpha)|\) is \(\cos\alpha\). Consequently
\[
M^2=4q+4q^2=4q(1+q),
\]
whereas
\[
|c_0|+|c_1|+|c_2|=2(1+q).
\]
Their ratio is \(\sqrt{(1+q)/q}=\sqrt{1+\sec^2\alpha}\), proving sharpness.

## Verification
The proof is algebraic and trigonometric and does not depend on finite enumeration. The accompanying `artifacts/verify.py` independently evaluates the displayed extremizer for every even \(N\) from \(4\) through \(200\), checks the claimed ratio numerically, and stress-tests the upper bound on random complex coefficient triples. It prints `VERIFY_OK` on success. These numerical checks are regression tests only; the infinite statement is established by the proof above.

## Relationship to prior work
Neuwirth determined the exact Sidon constant of every three-element subset of integer frequencies in \(C(\mathbb T)\). For \(\{0,1,2\}\) his result is \(\sqrt2\); his proof uses the supremum over the entire circle rather than the supremum over the finite set of \(N\)-th roots of unity. The formula above quantifies the exact sampling penalty for every even cyclic order and tends to Neuwirth's constant in the limit.

Graham's 1978 result computes the Sidon/Helson constant of a whole finite abelian group, not that of a prescribed three-character subset. Later work on extremal Sidon sets studies the special value equal to the square root of the set cardinality. The present family has that extremal value only at \(N=4\); for every even \(N\ge6\) the constant lies strictly between \(\sqrt2\) and \(\sqrt3\).

## Limitations
Odd cyclic orders are not treated. The result is specific to the consecutive three-character set \(\{0,1,2\}\); affine images under cyclic-group automorphisms inherit the same constant, but arbitrary three-point subsets can behave differently. The literature search found no statement equivalent to the even-order formula, but differently indexed finite-group interpolation literature remains a residual originality risk.

## References
1. Stefan Neuwirth, *The Sidon constant of sets with three elements*, arXiv:math/0102145, first submitted 2001-02-19; MSC 42A05.
2. C. C. Graham, *The Sidon constant of a finite abelian group*, Proceedings of the American Mathematical Society 68 (1978), 83--84, DOI: 10.1090/S0002-9939-1978-0458059-X.
3. Colin C. Graham, *A beastiary of sets having extremal Sidon constant, or, there must be more than one theorem somewhere here*, arXiv:1910.00924.
