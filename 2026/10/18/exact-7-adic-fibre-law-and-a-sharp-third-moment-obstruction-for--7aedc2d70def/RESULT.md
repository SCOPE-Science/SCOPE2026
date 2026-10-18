# Exact 7-adic fibre law and a sharp third-moment obstruction for sums of two cubes

## Finding
For each integer \(n\ge1\) and residue \(a\pmod{7^n}\), put
\[
R_n(a)=\#\{(x,y)\in(\mathbb Z/7^n\mathbb Z)^2:x^3+y^3\equiv a\pmod{7^n}\}.
\]
Let \(T\) be Haar-uniform on \(\mathbb Z_7\), and set \(F_n(T)=7^{-n}R_n(T\bmod7^n)\). Then \(F_n\) converges almost surely and in \(L^2(\mathbb Z_7)\) to a nonnegative function \(F\). Its **complete distributional recursion** is
\[
F(T)=\begin{cases}
6/7,&T\bmod7\in\{1,6\},\\
9/7,&T\bmod7\in\{2,5\},\\
0,&T\bmod7\in\{3,4\},\\
18/7,&7\mid T,\ 343\nmid T,\\
18/7+7F(T/343),&343\mid T,
\end{cases}
\]
where the last branch recurs on the Haar-uniform quotient conditional on divisibility by \(343\). In particular,
\[
\mathbb EF=1,\qquad \mathbb EF^2=\frac{99}{49},\qquad
\operatorname{Var}(F)=\frac{50}{49},
\]
and, for every real \(s>0\),
\[
F\in L^s(\mathbb Z_7)\quad\Longleftrightarrow\quad 0<s<3.
\]
Equivalently, the normalized four-variable cube-collision count has the exact limit
\[
\lim_{n\to\infty}7^{-3n}\#\{(x,y,u,v)\bmod7^n:x^3+y^3\equiv u^3+v^3\pmod{7^n}\}=\frac{99}{49}.
\]
All variables in the finite congruences range independently over the complete indicated residue rings. No assertion about positive-integer representations is needed.

## Assumptions and scope
The valuation \(\nu_7(t)\) of a nonzero 7-adic integer \(t\) is its order of divisibility by \(7\); \(\nu_7(0)=\infty\). All probability and \(L^s\) statements use normalized additive Haar measure on \(\mathbb Z_7\). Define \(F_0\equiv1\) only to simplify the finite recurrence. The displayed recursion and the pointwise limit are asserted outside a Haar-null set; at \(T=0\), the normalized counts grow without bound. A conditional quotient \(T/343\) belongs to \(\mathbb Z_7\) precisely on the indicated branch.

## Proof
**1. Exact local counts.** Modulo \(7\), the cube residues are \(0\) once, \(1\) three times, and \(-1\) three times. Thus the vector \(R_1(a)\), indexed by \(a=0,1,\ldots,6\), is
\[
(19,6,9,0,0,9,6).
\]
If \(7\nmid a\), each solution modulo \(7\) has a unit coordinate and at least one of the two partial derivatives \(3x^2,3y^2\) is a unit. At each lifting step there are exactly seven lifts of each such pair for the prescribed lifted right-hand side. Therefore, for every \(n\ge1\),
\[
R_n(a)=7^{n-1}R_1(a\bmod7)\qquad(7\nmid a).
\]
For \(7\mid a\), exactly 18 of the 19 pairs modulo \(7\) representing zero have a unit coordinate. They contribute \(18\cdot7^{n-1}\) at every level. Remaining solutions have both coordinates divisible by seven. For \(n\ge3\), writing \(x=7u,y=7v\) gives \(7^3(u^3+v^3)\equiv a\pmod{7^n}\), possible exactly when \(343\mid a\). Each pair modulo \(7^{n-3}\) has \(7^2\) choices for \(u\) modulo \(7^{n-1}\), and likewise for \(v\), hence \(7^4\) lifts. With \(R_0=1\), the exact recurrence is
\[
R_n(a)=18\cdot7^{n-1}+\mathbf1_{343\mid a}\,7^4R_{n-3}(a/343)
\quad(n\ge3,\ 7\mid a).
\]
At level \(n=2\), the same count gives \(R_2(a)=126+49\mathbf1_{49\mid a}\) when \(7\mid a\). These formulas also fix all boundary cases of the finite argument.

**2. Limiting law and convergence.** Let \(t\ne0\) be any 7-adic integer, and write \(\nu_7(t)=3j+d\) with \(j\ge0\) and \(d\in\{0,1,2\}\). Repeated use of the recurrence shows that \(F_n(t)\) eventually stabilizes. If \(d=0\) and \(u=t/7^{3j}\) is a unit, its limiting value is
\[
F(t)=\frac{18}{7}\sum_{i=0}^{j-1}7^i+7^j\frac{R_1(u\bmod7)}7.
\]
If \(d\in\{1,2\}\), its value is
\[
F(t)=\frac{18}{7}\sum_{i=0}^{j}7^i.
\]
These formulas yield the stated recursive law, including all unit, nonunit, and zero-representation classes. The exceptional point \(t=0\) has Haar measure zero.

For completeness, \((F_n)\) is a nonnegative martingale for the 7-adic residue filtration: every pair modulo \(7^n\) has 49 lifts to pairs modulo \(7^{n+1}\), distributed among the seven possible lifted sums, and consequently
\[
\frac17\sum_{b\equiv a\ (7^n)}\frac{R_{n+1}(b)}{7^{n+1}}
=\frac{R_n(a)}{7^n}.
\]
The moment computation below bounds \(\sup_n\mathbb EF_n^2\), so this martingale converges in \(L^2\) as well as almost surely, to the explicitly identified function \(F\).

**3. Exact moments and collision energy.** The first moment is \(\mathbb EF_n=1\), since \(\sum_{a\bmod7^n}R_n(a)=7^{2n}\). The recursion partitions Haar measure into six unit classes, a \(48/343\)-mass set with \(7\mid T\), \(343\nmid T\), and a \(1/343\)-mass set with \(343\mid T\). On the last set the quotient is Haar-uniform. Writing \(H_n=\mathbb EF_n^2\) and using \(\mathbb EF_{n-3}=1\) yields, for \(n\ge3\),
\[
H_n=\frac27\left[\left(\frac67\right)^2+\left(\frac97\right)^2\right]
+\frac{48}{343}\left(\frac{18}{7}\right)^2
+\frac1{343}\left[\left(\frac{18}{7}\right)^2+36+49H_{n-3}\right]
=\frac{594}{343}+\frac{H_{n-3}}7.
\]
The finite starting values are \(H_0=1\), \(H_1=85/49\), and \(H_2=601/343\). Each of the three subsequences converges to the unique fixed point
\[
H_\infty=\frac{594/343}{1-1/7}=\frac{99}{49}.
\]
The first and second moments converge to those of \(F\) by \(L^2\) convergence. Counting pairs of pairs with equal sums gives \(\sum_aR_n(a)^2\), so \(H_n=7^{-3n}\sum_aR_n(a)^2\) proves the collision limit.

**4. Sharp moment cutoff.** The set of 7-adic integers with valuation \(3j+d\) has Haar mass \(6\cdot7^{-(3j+d+1)}\). The explicit shell formulas from step 2 show \(F(t)=O(7^j)\) on each of the three shells with that \(j\); hence
\[
\int_{\mathbb Z_7}|F(t)|^s\,dt
\ll_s1+\sum_{j\ge0}7^{j(s-3)},
\]
which converges for \(0<s<3\). Conversely, on the valuation-\(3j+1\) shell the same formula gives \(F(t)\ge(18/7)7^j\) and shell measure \(6\cdot7^{-(3j+2)}\). The \(s\)-moment therefore dominates a positive constant times \(\sum_{j\ge0}7^{j(s-3)}\), which diverges for \(s\ge3\). This proves the sharp cutoff.

## Verification
Run `python3 verify.py` using a standard Python installation. It independently builds cube-residue multiplicities and their convolutions for every modulus \(7^n\) with \(1\le n\le4\), checks all residue classes against the exact count formulas, checks total masses and rational second moments, and tests the 7-adic valuation-shell formulas. It uses only Python's standard library and finishes without network access. A finite check is not the proof of the limiting or infinite moment statements; those follow from the recurrence, martingale estimate, and complete valuation-shell argument above.

## Relationship to prior work
Brüdern and Vaughan [1] introduce the two-cube local congruence multiplicity \(\rho(q,a)\) as part of a Montgomery–Hooley variance analysis. Broughan [2] and Avoyan–Tsirekidze [3] characterize representable residue classes modulo general integers, in particular the two excluded classes modulo seven. Those representability results determine **support**, not normalized fibre multiplicities, their complete 7-adic distribution, the exact second collision moment, or the sharp \(L^3\) boundary. The proof here specializes local counts to the singular prime seven and evaluates the distribution, moments, and full moment threshold. The arguments do not invoke any claim of independent priority.

## Limitations
This is a local theorem for ordered residue-class pairs modulo powers of seven, not an asymptotic for the number of positive integer solutions of \(x^3+y^3=N\), nor a theorem for other primes or composite moduli. The limiting fibre density may diverge at \(T=0\), which has measure zero. Existing general results on local zeta functions or \(p\)-adic fibre densities could conceivably imply the moment boundary after specialization; a complete literature-exhaustiveness guarantee is not claimed. No independent mathematical audit is claimed.

## References
[1] J. Brüdern and R. C. Vaughan, *A Montgomery–Hooley Theorem for sums of two cubes*, European Journal of Mathematics 7 (2021), 1616–1644, first available online September 20, 2021; https://doi.org/10.1007/s40879-021-00495-4.

[2] K. A. Broughan, *Characterizing the Sum of Two Cubes*, Journal of Integer Sequences 6 (2003), Article 03.4.6.

[3] A. Avoyan and D. Tsirekidze, *Decomposition of an integer as the sum of two cubes to a fixed modulus*, arXiv:1109.0451 (September 2, 2011); https://arxiv.org/abs/1109.0451; Matematički Vesnik 65 (2013), 383–386.
