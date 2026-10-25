# Exact first-hit depth distribution for the cubic Dickson map modulo powers of three

## Finding
For an integer \(k\ge1\), let \(R_k=\mathbb Z/3^k\mathbb Z\) and \(f(x)=x^3-3x\). If \(\rho(x)\in\{0,2,-2\}\) is the unique integer congruent to \(x\pmod3\), set
\[
H_k(x)=\min\{t\ge0:f^{\circ t}(x)\equiv\rho(x)\pmod{3^k}\}.
\]
Then \(H_k(x)\) is finite for every \(x\in R_k\), and \(0,2,-2\) are the only periodic points. For \(k\ge2\), the maximum \(H_k\) on the basins of \(0,2,-2\) is respectively \(k-1,\lfloor k/2\rfloor,\lfloor k/2\rfloor\).

Let \(\nu_{3,k}(y)=\min\{k,\nu_3(y)\}\), interpreted on residues. For \(x\equiv0\pmod3\),
\[
H_k(x)=k-\nu_{3,k}(x).
\]
For \(\rho=\pm2\) and \(x\equiv\rho\pmod3\), write \(a=\nu_{3,k}(x-\rho)\) and \(b=\nu_{3,k}(x+\rho/2)\). Then
\[
H_k(x)=\begin{cases}0,&a=k,\\1+\max\bigl\{0,\lceil(k-a-2b)/2\rceil\bigr\},&a<k.\end{cases}
\]

The exact depth polynomial is \(P_k(u)=\sum_{x\in R_k}u^{H_k(x)}\). In particular, \(P_1(u)=3\). For \(k\ge2\), put
\[
\begin{aligned}
c_k&=1+\max\{0,\lceil(k-3)/2\rceil\},\\
A_k(a)&=1+\max\{0,\lceil(k-a-2)/2\rceil\},\\
B_k(b)&=1+\max\{0,\lceil(k-1-2b)/2\rceil\}.
\end{aligned}
\]
Then
\[
\boxed{\begin{aligned}
P_k(u)={}&1+\sum_{a=1}^{k-1}2\cdot3^{k-a-1}u^{k-a}\\
&+2\Bigl(1+u+3^{k-2}u^{c_k}
+\sum_{a=2}^{k-1}2\cdot3^{k-a-1}u^{A_k(a)}
+\sum_{b=2}^{k-1}2\cdot3^{k-b-1}u^{B_k(b)}\Bigr).
\end{aligned}}
\]
Every sum with lower limit exceeding its upper limit is zero. The identity counts all \(3^k\) residues, including exactly three fixed points.

## Assumptions and scope
Only the polynomial \(f(x)=x^3-3x=D_3(x,1)=2T_3(x/2)\), the prime \(3\), and all positive integer precisions \(k\) are considered. Division by two is legitimate modulo \(3^k\). A first-hit time includes time zero for a fixed point. Valuations are capped at the precision, so the expressions depend only on residue classes. Basins are indexed by reduction modulo three, not by the sign of a chosen representative.

## Proof
Modulo three, \(f(x)\equiv x^3\equiv x\), hence every orbit remains in one residue class. The three displayed numbers are fixed in every quotient. For the basin of zero, factor
\[
f(x)=x(x^2-3).
\]
If \(3\mid x\) and \(x\not\equiv0\pmod{3^k}\), then \(\nu_3(x^2-3)=1\). The valuation therefore increases by exactly one at every step until it reaches \(k\), proving \(H_k=k-\nu_{3,k}(x)\).

For either nonzero basin, with \(\rho\in\{2,-2\}\), the exact integer identity is
\[
f(x)-\rho=(x-\rho)(x+\rho/2)^2.
\]
The two factors on the right differ by \(3\rho/2\), whose \(3\)-adic valuation is exactly one. Thus, for a nonfixed point, \(a,b\ge1\), \(\min(a,b)=1\), and after one iteration the distance from \(\rho\) has valuation \(\min(k,a+2b)\), at least three before truncation. Every subsequent nonterminal iterate \(y\) satisfies \(y\equiv\rho\pmod{27}\) at untruncated precision and consequently \(\nu_3(y+\rho/2)=1\). Its distance valuation therefore increases by exactly two per further step. Solving the resulting threshold inequality yields the displayed formula for \(H_k(x)\). This also proves that every orbit enters its designated fixed point and that no other periodic point exists.

For \(k\ge2\), the zero basin contains one fixed point and, for each \(1\le a<k\), exactly \(2\cdot3^{k-a-1}\) points with \(\nu_3(x)=a\). Each nonzero basin has the following disjoint partition: one fixed point \(a=k\); one exact critical preimage \(b=k\), mapping to the fixed point in one step; \(3^{k-2}\) points with \(a=b=1\); for each \(2\le a<k\), exactly \(2\cdot3^{k-a-1}\) points with \(a\) fixed and \(b=1\); for each \(2\le b<k\), exactly \(2\cdot3^{k-b-1}\) points with \(a=1\) and \(b\) fixed. These counts follow from the distinct congruence roots \(x=\rho\) and \(x=-\rho/2\) modulo \(9\), followed by geometric counts for exact valuations. The first-hit formula gives the exponents \(c_k,A_k(a),B_k(b)\) for those groups. Both nonzero basins have the same polynomial because \(f\) is odd; addition of all three basins yields \(P_k(u)\). Its sum of coefficients is \(3^k\).

For \(k\ge2\), \(x=3\) (read modulo \(3^k\)) attains depth \(k-1\) in the zero basin. In a nonzero basin, \(a+2b\ge3\) whenever \(x\) is not fixed, so the first-hit formula gives at most \(\lfloor k/2\rfloor\). The branch \(a=b=1\) exists for each \(k\ge2\), and attains that bound. At \(k=1\), all three residues are fixed.

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. It iterates every residue modulo \(3^k\) independently for \(1\le k\le8\), identifies the fixed point using its residue class, compares all actual first-hit times to the capped-valuation formula, and compares independently accumulated histograms with the finite-sum formula. It also checks normalization and all three sharp heights. A successful run prints `VERIFY_OK`. The resulting 9,840 finite checks are not substituted for the universal proof.

## Relationship to prior work
Gassert's *Chebyshev Action on Finite Fields* (arXiv:1209.4396v1, Sections 2.1 and Theorems 2.3–2.4) classifies finite-**field** functional graphs and their preperiod counts; its main graph analysis explicitly assumes the characteristic is different from the polynomial degree. It does not imply the residue-**ring** histogram at the ramified pair \((p,d)=(3,3)\). Diarra and Sylla's *p-Adic Dynamical Systems of Chebyshev Polynomials* (dated 2013-03-21, Theorem 13 and Proposition 11) determines attracting basins and limiting fixed points over \(p\)-adic domains. That basin classification does not determine each finite-modulus first-hit time or its histogram. Panraksa and Tangboonduangjit's *Fixed-point lifting and ghost periodic points for Chebyshev polynomials modulo odd prime powers* (arXiv:2605.04417, Corollaries 7.14 and 12.1) proves that the Chebyshev–Fermat case has precisely \(p\) fixed points and no other periodic points; its stated enumerations concern periodic points rather than the first-hit distribution of the remaining \(p^k-p\) vertices. Lu, Dai, and Li's *Graph Structure of Chebyshev Permutation Polynomials over Binary and Ternary Adic Rings* (arXiv:2605.21819) studies permutation-polynomial degrees, whereas the present degree is divisible by the modulus prime and is nonpermuting. The new contribution asserted here is the exact transient first-hit profile and branch-specific height asymmetry, not the previously known attractor set or fixed-point count.

## Limitations
The result does not treat other degrees, other primes, or arbitrary Chebyshev maps. The exact histogram is a finite-sum formula depending on the precision; no single rational bivariate generating function is asserted. An equivalent transient-depth result could exist in unlocated literature, and the present checks do not establish absolute priority. Independent validation is not claimed.

## References
1. T. Alden Gassert, *Chebyshev Action on Finite Fields*, arXiv:1209.4396v1 (first public date 2012-09-20), https://arxiv.org/abs/1209.4396 .
2. Bertin Diarra and Djeidi Sylla, *p-Adic Dynamical Systems of Chebyshev Polynomials*, manuscript dated 2013-03-21, https://padic2013.mi-ras.ru/Diarra.pdf ; journal version, *p-Adic Numbers, Ultrametric Analysis and Applications* 6 (2014), 21–32.
3. Chatchawan Panraksa and Aram Tangboonduangjit, *Fixed-point lifting and ghost periodic points for Chebyshev polynomials modulo odd prime powers*, arXiv:2605.04417v1, https://arxiv.org/abs/2605.04417 .
4. Xiaoxiong Lu, Yuling Dai, and Chengqing Li, *Graph Structure of Chebyshev Permutation Polynomials over Binary and Ternary Adic Rings*, arXiv:2605.21819v1, https://arxiv.org/abs/2605.21819 .
