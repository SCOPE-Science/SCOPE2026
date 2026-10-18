# Exact finite-level collision moments and p-adic fibres for sums of two cubes

## Finding
For every prime \(p\ge5\) and integer \(n\ge1\), put
\[
R_{p,n}(a)=\#\{(x,y)\in(\mathbb Z/p^n\mathbb Z)^2:x^3+y^3\equiv a\pmod{p^n}\},\qquad
M_{p,n}=p^{-3n}\sum_{a\bmod p^n}R_{p,n}(a)^2.
\]
Set \(M_{p,0}=1\), a formal normalization for the one-element ring. Define \(\gamma_p=7\) when \(p\equiv1\pmod3\) and \(\gamma_p=1\) when \(p\equiv2\pmod3\). The exact infinite-level constant is
\[
L_p=1+\frac{\gamma_p}{p}+\frac1{p^2}.
\]
The initial values are
\[
M_{p,1}=\begin{cases}1+6/p-6/p^2,&p\equiv1\pmod3,\\1,&p\equiv2\pmod3,\end{cases}
\qquad
M_{p,2}=\begin{cases}1+6/p-5/p^2-1/p^3,&p\equiv1\pmod3,\\1+(p-1)/p^3,&p\equiv2\pmod3.\end{cases}
\]
Then, for every \(n\ge0\), including all three residue classes of \(n\) modulo three,
\[
\boxed{M_{p,n}=L_p+p^{-\lfloor n/3\rfloor}(M_{p,n\bmod3}-L_p).}
\]
In particular, the normalized number of ordered quadruples satisfying \(x^3+y^3\equiv u^3+v^3\pmod{p^n}\) is exactly \(M_{p,n}\) and converges to \(L_p\) at a fully explicit three-periodic geometric rate.

There is also an exact limiting fibre distribution. Equip \(\mathbb Z_p\) with Haar probability measure, let \(T\) be Haar distributed, and put \(F_{p,n}(T)=p^{-n}R_{p,n}(T\bmod p^n)\). Define \(g_p=\gcd(3,p-1)\) and \(c_p=g_p(p-1)/p\). For any nonzero \(T\in\mathbb Z_p\), write \(v_p(T)=3k+r\) with \(k\ge0\), \(r\in\{0,1,2\}\), and \(U=T/p^{3k}\). Let
\[
B_p(U)=\begin{cases}p^{-1}R_{p,1}(U\bmod p),&r=0,\\ c_p,&r=1\text{ or }2.\end{cases}
\]
Then \(F_{p,n}(T)\) eventually stabilizes to
\[
\boxed{F_p(T)=c_p\frac{p^k-1}{p-1}+p^k B_p(U).}
\]
Consequently \(F_{p,n}\to F_p\) almost surely and in \(L^s(\mathbb Z_p)\) for every real \(0<s<3\), with
\[
\mathbb EF_p=1,\qquad \mathbb EF_p^2=L_p,\qquad
F_p\in L^s(\mathbb Z_p)\iff0<s<3.
\]
The nonintegrable endpoint is sharp at exponent three.

The unit-fibre values in this formula are fully explicit. If \(p\equiv2\pmod3\), then \(R_{p,1}(a)=p\) for every \(a\). If \(p\equiv1\pmod3\), choose either nontrivial cubic multiplicative character \(\chi\) of \(\mathbb F_p\), extended by zero, and put \(J=\sum_{z\in\mathbb F_p}\chi(z)\chi(1-z)\). For \(a\ne0\),
\[
R_{p,1}(a)=p-2+J\chi(a)^2+\overline J\chi(a),\qquad |J|^2=p;
\]
for \(a=0\) in either congruence class, \(R_{p,1}(0)=g_p(p-1)+1\).

## Assumptions and scope
All four congruence variables are ordered complete residue systems, not restricted to positive integers or primitive solutions. The prime is at least five; no assertion for primes two or three is made. All prime-adic expectations are Haar-probability expectations. The point \(T=0\) is excluded only from the pointwise limiting formula and has measure zero. For arbitrary finite \(n\), the formula gives an exact identity, not a numerical asymptotic.

## Proof
**Step 1: residues modulo a prime.** If \(p\equiv2\pmod3\), cubing permutes \(\mathbb F_p\), so each target has exactly \(p\) ordered cubic-sum representations. Otherwise choose \(\chi\) as above. The number of cube roots of \(z\in\mathbb F_p\) is \(1+\chi(z)+\overline\chi(z)\), also at zero. Convolving this identity and using \(\chi(-1)=1\), \(J(\chi,\overline\chi)=-1\), and character orthogonality gives the stated expression for \(R_{p,1}(a)\) when \(a\ne0\). The standard Jacobi-sum identity gives \(|J|^2=p\). Thus
\[
S_p:=\sum_{a=1}^{p-1}R_{p,1}(a)^2
=\begin{cases}(p-1)(p^2-2p+4),&p\equiv1\pmod3,\\(p-1)p^2,&p\equiv2\pmod3.\end{cases}
\]
Also \(x^3+y^3=0\) over \(\mathbb F_p\) has \(g_p(p-1)+1\) solutions, precisely one of which is singular, \((0,0)\).

**Step 2: exact lifting, including the singular branch.** Since \(p\ge5\), the gradient \((3x^2,3y^2)\) vanishes modulo \(p\) exactly when both variables vanish. Each nonsingular solution for a fixed target modulo \(p\) has exactly \(p^{n-1}\) lifts to a specified target modulo \(p^n\). If \(a\) is a unit, all solutions are nonsingular. If \(p\mid a\), the nonsingular base solutions number \(g_p(p-1)\), contributing \(c_p p^n\) solutions at every level. For \(n\ge3\), the singular solutions have both \(x\) and \(y\) divisible by \(p\), and exist only if \(p^3\mid a\). Writing \(x=px'\), \(y=py'\), and counting the redundant last two digits gives exactly \(p^4R_{p,n-3}(a/p^3)\) additional solutions, where \(R_{p,0}(0)=1\). Therefore
\[
F_{p,n}(T)=\begin{cases}
R_{p,1}(T\bmod p)/p,&p\nmid T,\\
c_p,&p\mid T,\ p^3\nmid T,\\
c_p+pF_{p,n-3}(T/p^3),&p^3\mid T,
\end{cases}\qquad n\ge3,
\]
where the quotients in the last case are taken modulo \(p^{n-3}\). At the two initial levels the singular residue contributes \(1/p\) to \(F_{p,1}(0)\), and contributes \(1\) to \(F_{p,2}(0)\); all other divisible-by-\(p\) targets at level two have value \(c_p\).

**Step 3: exact collision moments.** Since the finite distribution has mean one, the two initial moments from Steps 1--2 are
\[
M_{p,1}=(S_p+[g_p(p-1)+1]^2)/p^3,\qquad
M_{p,2}=S_p/p^3+c_p^2/p+(2c_p+1)/p^2.
\]
They simplify to the stated piecewise rational expressions. Partition targets at level \(n\ge3\) by whether their valuation is zero, one or two, or at least three. Using the preceding fibre recursion, independence of the remaining Haar digits, and \(\mathbb E F_{p,n-3}=1\), gives
\[
M_{p,n}=S_p/p^3+c_p^2/p+2c_p/p^2+M_{p,n-3}/p.
\]
Direct substitution of the two values for \(S_p\), together with \(c_p=g_p(p-1)/p\), shows that the constant term equals \((1-1/p)L_p\). Hence
\[
M_{p,n}-L_p=p^{-1}(M_{p,n-3}-L_p),
\]
which iterates to the boxed formula for every \(n\ge0\).

**Step 4: limiting fibres and the sharp moment boundary.** For \(T\ne0\), write its finite valuation as \(3k+r\). Iterating the recursion exactly \(k\) times leaves either a unit target or a target of valuation one or two, where the value is independent of all sufficiently large levels. This proves the displayed closed formula for \(F_p(T)\) and eventual pointwise stabilization. Uniformly over \(n\), its size on the valuation shell \(v_p(T)=3k+r\) is bounded by a constant depending only on \(p\), times \(p^k\); the same bound, with a harmless factor depending on \(p\), also holds at levels smaller than the valuation. The shell has Haar mass \((1-1/p)p^{-3k-r}\). Therefore \(\sup_n\mathbb E|F_{p,n}|^s<\infty\) for each \(s<3\), and shell-wise domination proves \(L^s\) convergence. Since every shell with \(r=1\) satisfies \(F_p(T)\ge c_pp^k\), the third and all higher moments diverge by the geometric series \(\sum_{k\ge0}p^{k(s-3)}\). The first two expectations follow from \(L^2\) convergence and the exact finite moments. Finally, the quadruple count equals \(\sum_aR_{p,n}(a)^2\) by fixing the common target, proving its stated normalization.

## Verification
Run `python3 verify.py` using Python's standard library. It enumerates complete cube-value distributions and convolutions for eight primes \(5,7,11,13,17,19,31,37\) at all tested levels with modulus at most \(2500\). It compares each residue fibre with the nonsingular/singular lifting formula and every exact collision moment against the closed formula; 22 complete distributions pass. The code does not certify the statements for unbounded primes or exponents: these follow from Steps 1--4.

## Relationship to prior work
Brüdern and Vaughan (2021) study variances of positive two-cube representations in arithmetic progressions, introducing the modular counts \(\rho(q,a)\); that work does not state the all-prime exact finite-depth collision sequence or the prime-adic fibre law here. The classical point counts of smooth Fermat cubic surfaces, presented for example in Massarenti (2026, Corollary 8.3), produce the values \(p^2+7p+1\) or \(p^2+p+1\) and already provide the geometric limit of the collision energy. **That limiting numerical constant by itself is not claimed as new.** The present statements instead specify every finite depth, all residue targets' limiting densities, and the sharp integrability transition simultaneously for all primes at least five. An isolated prime-seven fibre computation is consistent with, and is contained in, the general theorem. Classical Jacobi-sum orthogonality and smooth lifting are used without any claim of priority.

## Limitations
No assertion is made for \(p=2\) or \(p=3\), for global positive-integer counts, or for analytic error terms over growing moduli. Standard homogeneous-form local-zeta or Poincaré-series machinery may implicitly give the collision recurrence; establishing whether a specific earlier result subsumes the full joint theorem would require further bibliographic verification. The proof is mathematical and computationally checked at finite sample moduli, but no independent audit has been performed.

## References
- J. Brüdern and R. C. Vaughan, *A Montgomery--Hooley Theorem for sums of two cubes*, European Journal of Mathematics **7** (2021), 1616--1644, https://doi.org/10.1007/s40879-021-00495-4 (publicly released 20 September 2021).
- A. Massarenti, *Rational points on even-dimensional Fermat cubics*, Transactions of the London Mathematical Society (2026), Corollary 8.3, https://doi.org/10.1112/tlm3.70028 (finite-field geometric point-count comparison).
- P. Swinnerton-Dyer, *Cubic surfaces over finite fields*, Mathematical Proceedings of the Cambridge Philosophical Society **149** (2010), 385--388, https://doi.org/10.1017/S0305004110000320 (background on cubic-surface point counts; full text not examined here).
