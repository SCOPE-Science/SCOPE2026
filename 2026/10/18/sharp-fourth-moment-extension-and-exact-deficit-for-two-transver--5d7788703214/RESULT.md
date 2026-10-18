# Sharp fourth-moment extension and exact deficit for two transverse finite-group axes

## Finding
Let \(A\) be an arbitrary finite abelian group of order \(N\ge4\). Put
\[
S=(A\times\{0\})\cup(\{0\}\times A)\subset A^2,\qquad L=|S|=2N-1.
\]
For every function \(f:S\to\mathbb C\), define its Fourier extension on the dual group by
\[
\mathcal E f(\chi,\eta)=\frac1L\sum_{(x,y)\in S}f(x,y)\chi(x)\eta(y),
\qquad (\chi,\eta)\in\widehat A^2.
\]
Give \(S\) normalized counting measure and \(\widehat A^2\) unnormalized counting measure. Then the **exact sharp inequality** is
\[
\boxed{\|\mathcal E f\|_{\ell^4(\widehat A^2)}^4
\le\frac{N^3}{(2N-1)^2}\|f\|_{L^2(S)}^4.}
\]
Every nonzero equality case is a nonzero scalar multiple of a single character supported on exactly one complete axis: for some \(c\ne0\) and \(\chi_0\in\widehat A\), either
\[
f(x,0)=c\chi_0(x)\ (x\in A),\qquad f(0,y)=0\ (y\ne0),
\]
or the transposed vertical counterpart. Conversely, all such functions are extremizers.

Beyond the optimal constant, the theorem provides the exact eight-term nonnegative deficit below, which quantifies departures from convolution extremality. In particular, the sharp equality geometry changes between group orders three and four.

## Assumptions and scope
The abelian group \(A\) is any finite abelian group of order \(N\ge4\), without assumptions about primality, exponent or parity. Its identity is \(0\) and all sums are taken in \(A\). The Fourier characters are unit-modulus homomorphisms into the complex circle. All norms and convolutions use the counting measure conventions stated above. The theorem is uniform over all complex-valued functions on the two-axis set.

Write \(a=f(0,0)\), \(u(x)=f(x,0)\), \(v(y)=f(0,y)\), so \(u(0)=v(0)=a\), and introduce
\[
\lambda=|a|^2,\quad G=\sum_{x\ne0}|u(x)|^2,\quad H=\sum_{y\ne0}|v(y)|^2,
\quad M=\lambda+G+H=\sum_{s\in S}|f(s)|^2.
\]
Also set
\[
B_u=\sum_{x\ne0}u(x)u(-x),\quad
B_v=\sum_{y\ne0}v(y)v(-y),\quad b=|B_u|,\quad c=|B_v|,
\]
\[
R_u=\sum_{x\ne0}|u(x)|^2|u(-x)|^2,\qquad
R_v=\sum_{y\ne0}|v(y)|^2|v(-y)|^2.
\]
Let \(*\) denote unnormalized additive convolution on \(A\) or \(A^2\), as appropriate. Set
\[
\Delta_u=\sum_{s\ne0}\left(N\sum_{t\in A}|u(t)u(s-t)|^2-|\sum_{t\in A}u(t)u(s-t)|^2\right),
\]
and define \(\Delta_v\) analogously. By Cauchy--Schwarz every term in either sum is nonnegative.

## Proof
**Step 1: exact convolution fibers.** Let \(F=f*f\) be convolution in \(A^2\), regarding \(f\) as zero outside \(S\). For any \(s,t\ne0\), the only ways to express \((s,t)\) as a sum of two points of \(S\) are the two ordered cross-axis pairs, hence \(F(s,t)=2u(s)v(t)\). At the origin \(F(0,0)=a^2+B_u+B_v\). On the nonzero horizontal and vertical axes we have \(F(s,0)=(u*u)(s)\) and \(F(0,t)=(v*v)(t)\), respectively. Thus the exact convolution energy \(Q=\sum_{z\in A^2}|F(z)|^2\) is
\[
Q=|a^2+B_u+B_v|^2+
\sum_{s\ne0}|(u*u)(s)|^2+
\sum_{t\ne0}|(v*v)(t)|^2+4GH.
\tag{1}
\]

**Step 2: axis Cauchy deficits.** Expanding the definition of \(\Delta_u\), and partitioning the product-square sum by \(s=x+y\), gives
\[
\sum_{s\ne0}|(u*u)(s)|^2
=N\big((\lambda+G)^2-\lambda^2-R_u\big)-\Delta_u
=N(2\lambda G+G^2-R_u)-\Delta_u.
\tag{2}
\]
The identical formula holds for \(v\). Substituting (2) into (1) and simplifying yields the exact preliminary identity
\[
NM^2-Q=\Delta_u+\Delta_v+N(R_u+R_v)
+(2N-4)GH+N\lambda^2-|a^2+B_u+B_v|^2.
\tag{3}
\]

**Step 3: manifestly nonnegative eight-term deficit.** Let \(\theta_N=2N-6-2/(N-1)\). Rearranging (3) gives the following **identity**, with no inequalities discarded:
\[
\begin{aligned}
NM^2-Q={}&\Delta_u+\Delta_v
+N\left(R_u-\frac{b^2}{N-1}\right)
+N\left(R_v-\frac{c^2}{N-1}\right)\\
&+\frac{\big((N-1)\lambda-b-c\big)^2}{N-1}
+\theta_Nbc
+(2N-4)(GH-bc)\\
&+(\lambda+b+c)^2-|a^2+B_u+B_v|^2.
\end{aligned}
\tag{4}
\]
Every displayed summand is nonnegative: \(\Delta_u,\Delta_v\ge0\) follow from Cauchy--Schwarz; \(b^2\le(N-1)R_u\) and \(c^2\le(N-1)R_v\) are another Cauchy--Schwarz application; \(b\le G\), \(c\le H\) follow by pairing \(x\) with \(-x\) and using \(2|zw|\le|z|^2+|w|^2\); and \(|a^2+B_u+B_v|\le\lambda+b+c\) is the triangle inequality. For \(N\ge4\), \(\theta_N\ge4/3>0\), while \(2N-4>0\). Hence \(Q\le NM^2\).

**Step 4: complete equality classification.** If \(NM^2-Q=0\), positivity of the \(bc\) and \(GH-bc\) summands in (4) forces \(bc=0\) and \(GH=bc=0\). Therefore at least one of \(G,H\) vanishes, so \(f\) is supported on exactly one of the two axes (unless \(f=0\), which is excluded in the equality classification). Suppose it is the horizontal axis, identified with \(A\), and write its full-axis signal as \(u\). Then \(Q=\sum_s|(u*u)(s)|^2\). By unnormalized Fourier transform and Plancherel on \(A\),
\[
Q=\frac1N\sum_{\chi\in\widehat A}|\widehat u(\chi)|^4
\le\frac1N\left(\sum_{\chi\in\widehat A}|\widehat u(\chi)|^2\right)^2
=N\left(\sum_{x\in A}|u(x)|^2\right)^2.
\]
Equality for nonzero \(u\) holds precisely if \(\widehat u\) has exactly one nonzero coefficient, equivalently if \(u\) is a nonzero complex scalar multiple of a character of \(A\). The vertical case is identical, and every such character indeed gives equality.

**Step 5: Fourier norm normalization.** Finite-group character orthogonality applied to the square of the Fourier transform gives
\[
\sum_{\chi,\eta\in\widehat A}|\mathcal E f(\chi,\eta)|^4
=\frac{N^2}{L^4}Q,
\qquad \|f\|_{L^2(S)}^4=\frac{M^2}{L^2}.
\]
Combining these expressions with \(Q\le NM^2\) proves the stated sharp constant and equality classification.

**Boundary behavior.** The hypothesis \(N\ge4\) cannot be weakened to \(N=3\). For \(A=\mathbb Z_3\), the function \(f(0,0)=6/5\), \(f(s)=1\) at the four other axis points has \(Q/M^2=14349/4624>3\), contradicting the putative \(Q\le3M^2\). This exact counterexample also illustrates that the positive \(\theta_N\) condition represents a real transition.

## Verification
A self-contained Python 3 checker is supplied as `verify_axes.py`. It independently constructs the additive convolution on eight groups (\(\mathbb Z_3\), \(\mathbb Z_4\), \(\mathbb Z_5\), \(\mathbb Z_6\), \(\mathbb Z_7\), \(\mathbb Z_2^2\), \(\mathbb Z_2\times\mathbb Z_4\), \(\mathbb Z_3^2\)). It compares both sides of the **exact** identity (4) on 65 deterministic complex inputs per group, checks positivity in the claimed range, tests actual character extremizers and direct Fourier normalization, and confirms that order three is exceptional. The checker reports `VERIFY_OK groups=8 complex_inputs=562 exact_deficit_identity=PASS axes_extremizers=PASS fourier_normalization=PASS exceptional_order_three=PASS`.

The computation checks finite examples only. The unrestricted assertion for every finite abelian group with \(N\ge4\) follows from the algebra and equality arguments in Steps 1--5, not from an enumeration.

## Relationship to prior work
Koh and Shen, arXiv:1003.4240, establish a qualitative finite-field extension criterion for planar algebraic curves requiring the defining polynomial to have no linear factor. The present reducible curve \(xy=0\) falls outside that uniform-boundedness regime. The cited theorem does not give the sharp finite-size \(L^2\to\ell^4\) constant, the exact deficit, or the equality classification proved here. Iosevich and Koh, arXiv:0804.4505, treat nondegenerate quadratic level surfaces and do not cover this union of two subgroups. González-Riquelme and Oliveira e Silva, arXiv:2405.16647, develop sharp extension inequalities for other finite-field surfaces; the two-line sets appearing as auxiliary fibers in their calculations are not the support of the same extension problem. Searches of related published mathematical records uncovered results for other curves, Fourier uncertainty, and finite spectral sets, but no theorem implying this exact statement.

The smallest odd-field split cone \(\mathbb F_3\) has a distinct, mixed-axis extremizer, consistent with the exact counterexample in Step 5; that result does not imply the order-four-and-above theorem. This is a claim-to-claim comparison, not a priority guarantee. A previously unlocated general inequality for unions of finite subgroups could still subsume this theorem.

## Limitations
The group must be finite and abelian, and its order at least four. The proof does not treat more than two intersecting subgroups, arbitrary translate arrangements, or an optimal operator on nonabelian groups. The sharp constant grows with \(N\) under the stated counting normalization; no uniform-in-field extension bound is claimed. The supplied numerical verifier is finite evidence and does not certify the general proof. Novelty has not been independently audited against every historical source.

## References
1. A. Iosevich and D. Koh, *Extension theorems for Fourier transform associated with non-degenerate quadratic surfaces in vector spaces over finite fields*, arXiv:0804.4505 (first public posting 2008-04-28). https://arxiv.org/abs/0804.4505
2. D. Koh and C.-Y. Shen, *Sharp extension theorems and Falconer distance problems for algebraic curves in two dimensional vector spaces over finite fields*, arXiv:1003.4240 (first public posting 2010-03-22). https://arxiv.org/abs/1003.4240
3. A. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647 (2024). https://arxiv.org/abs/2405.16647
