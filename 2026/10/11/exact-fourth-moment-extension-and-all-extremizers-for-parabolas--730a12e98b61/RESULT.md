# Exact fourth-moment extension and all extremizers for parabolas over odd prime-power rings

## Finding

For every odd prime \(p\), integer \(k\geq 1\), and \(q=p^k\), let \(R=\mathbb Z/q\mathbb Z\) and
\[
\mathcal E_q f(u,v)=\frac1q\sum_{x\in R}f(x)\exp\!\left(\frac{2\pi i(ux+v x^2)}q\right),\qquad (u,v)\in R^2.
\]
The **exact best fourth-power extension constant** is
\[
\boxed{\sup_{f\ne0}\frac{\displaystyle\sum_{u,v\in R}|\mathcal E_q f(u,v)|^4}{\displaystyle\bigl(q^{-1}\sum_{x\in R}|f(x)|^2\bigr)^2}
=\mathsf C_{p,k}=\begin{cases}
p^{k/2},&k\text{ even},\\
(2-1/p)p^{(k-1)/2},&k\text{ odd}.
\end{cases}}
\]
Thus the operator norm, with the displayed norms, is \(\mathsf C_{p,k}^{1/4}\). The following describes **all** nonzero equality cases, with \(a\in R\) arbitrary, \(\lambda\in\mathbb C\setminus\{0\}\), and zero values outside the indicated coset.

For \(k=2m\), equality holds precisely on a coset \(a+p^m R\), with
\[
f(a+p^m h)=\lambda\chi(h)\qquad (h\in\mathbb Z/p^m\mathbb Z),
\]
where \(\chi\) is any additive character of \(\mathbb Z/p^m\mathbb Z\).

For \(k=2m+1\), including \(m=0\), equality holds precisely on a coset \(a+p^m R\). Its elements have unique representations \(a+p^m r+p^{m+1}h\), with \(0\le r<p\) and \(h\in\mathbb Z/p^m\mathbb Z\), and
\[
f(a+p^m r+p^{m+1}h)=\lambda\eta_r\chi(h),\quad
|\eta_r|=1,
\]
for a **single common** additive character \(\chi\) and arbitrary unimodular phases \(\eta_0,\dots,\eta_{p-1}\). For \(m=0\), the character is trivial and this is exactly the family of constant-modulus functions on \(R\).

## Assumptions and scope

The ring has *odd-prime* order \(p^k\); no assertion is made for the prime \(2\) or for non-prime-power moduli. All sums use unnormalized counting measure except for the factors explicitly displayed. Powers, congruences, and additive characters are taken in the indicated quotient rings. The result includes both the sharp norm and the entire equality family for every \(k\ge1\).

## Proof

**1. Orthogonality and pair fibers.** Put \(S=\sum_x|f(x)|^2\) and, for \((s,t)\in R^2\), define the pair-sum fiber
\[
\mathcal F(s,t)=\{(x,y)\in R^2:x+y=s,\;x^2+y^2=t\},\quad
F(s,t)=\sum_{(x,y)\in\mathcal F(s,t)}f(x)f(y).
\]
Orthogonality in each of the two Fourier variables gives the **exact** identity
\[
\sum_{u,v\in R}|\mathcal E_q f(u,v)|^4=q^{-2}\sum_{s,t\in R}|F(s,t)|^2.
\]
Writing \(n(s,t)=|\mathcal F(s,t)|\), Cauchy–Schwarz on each fiber yields
\[
\sum_{s,t}|F(s,t)|^2\le\sum_{x,y\in R}n(x+y,x^2+y^2)|f(x)|^2|f(y)|^2.
\tag{1}
\]
Because \(2\) is invertible, fixing \((s,t)\) amounts to fixing the square of the half-difference \(z=(x-y)/2\). Let \(w(x-y)\) be the number of solutions \(z'\in R\) of \(z'^2=((x-y)/2)^2\). If \(r\) is the truncated \(p\)-adic valuation of \(x-y\), with \(r=k\) when \(x=y\), then
\[
\boxed{w(x-y)=\begin{cases}2p^r,&2r<k,\\p^{\lfloor k/2\rfloor},&2r\ge k.\end{cases}}
\tag{2}
\]
Indeed, if \(2r<k\), divide the congruence by \(p^{2r}\); the remaining unit equation has precisely the two roots \(\pm u\) modulo \(p^{k-2r}\), each with \(p^r\) lifts to a root in \(R\). If \(2r\ge k\), the equation is \(z'^2\equiv0\pmod{p^k}\), with \(p^{\lfloor k/2\rfloor}\) solutions. Thus the ratio of the two sides of the claimed extension estimate is at most
\[
B(\mu)=\sum_{x,y\in R}w(x-y)\mu_x\mu_y,\qquad \mu_x=|f(x)|^2/S.
\tag{3}
\]

**2. Even exponent.** Let \(k=2m\). Formula (2) implies \(w(x-y)\le p^m\), with equality precisely when \(x\equiv y\pmod{p^m}\): for \(r<m\), \(2p^r\le2p^{m-1}<p^m\) since \(p\ge3\). Therefore \(B(\mu)\le p^m\), and equality forces \(\mu\) to be supported inside exactly one residue class \(a+p^mR\).

**3. Odd exponent.** Let \(k=2m+1\) and first \(m\ge1\). For each residue class \(a\pmod{p^m}\), denote its total probability by \(U_a\); for the \(p\) daughter classes modulo \(p^{m+1}\), denote the probabilities by \(V_{a,r}\), so \(\sum_r V_{a,r}=U_a\). Formula (2) gives weights bounded by \(2p^{m-1}\) for different parents, exactly \(2p^m\) for two different daughters in the same parent, and exactly \(p^m\) within a daughter. Hence
\[
\begin{aligned}
B(\mu)&\le2p^{m-1}(1-\sum_aU_a^2)+p^m\sum_a(2U_a^2-\sum_rV_{a,r}^2)\\
&\le2p^{m-1}+\bigl((2-1/p)p^m-2p^{m-1}\bigr)\sum_aU_a^2\\
&\le(2-1/p)p^m.
\end{aligned}
\tag{4}
\]
The second inequality uses \(\sum_r V_{a,r}^2\ge U_a^2/p\); the third uses \(\sum_aU_a^2\le1\). Both inequalities are strict unless precisely **one parent** has probability \(1\) and its \(p\) daughters each have probability \(1/p\). If \(m=0\), all distinct points have weight \(2\) and diagonal pairs weight \(1\), so \(B(\mu)=2-\sum_x\mu_x^2\le2-1/p\), with equality precisely at the uniform distribution. This proves the upper bound in all cases.

**4. Attainment and all equality phases.** For any nonzero \(f\) attaining the upper bound, (1), (3), and the strict probability conditions above are all equalities. Equality in fiberwise Cauchy–Schwarz means that every product \(f(x)f(y)\) is **constant across its complete fiber**, including points where a product might otherwise vanish.

In the even case, take a nonzero diagonal pair in the winning coset \(C=a+p^mR\). Its fiber contains all \(p^m\) pairs within \(C\) with that same sum, so equality forces every element of \(C\) to belong to the nonzero support. Inside \(C\), the parabola is affine in the coset coordinate: \((a+p^mh)^2\equiv a^2+2ap^mh\pmod{p^{2m}}\). Consequently its pair fibers are exactly the fixed-sum pairs in the coset. The constant-product condition gives \(f(a+p^mh)f(a+p^mj)=f(a)f(a+p^m(h+j))\), hence \(h\mapsto f(a+p^mh)/f(a)\) is a character of the finite cyclic additive group. Conversely every such character makes every complete pair-fiber product constant and reaches (1), proving sufficiency.

In the odd case, every daughter class has positive mass. Within a daughter \(C_r=a+p^mr+p^{m+1}R\), the quadratic map is affine in \(h\) modulo \(p^{2m+1}\), so diagonal fibers imply its entire \(p^m\)-point daughter is nonzero, and the fiber equality forces the restriction to be a scalar times an additive character \(\chi_r(h)\). For distinct daughters \(r\ne s\), each cross-daughter pair fiber consists of the \(2p^m\) ordered pairs obtained from the two opposite half-difference root classes. The constant-product condition, at fixed sum, gives \(\chi_r(h)\chi_s(j)=\chi_r(h+1)\chi_s(j-1)\), which forces \(\chi_r=\chi_s\). Since every daughter has probability mass \(1/p\), its constant modulus must coincide with all the others. Conversely a common character and arbitrary daughter phases make **all** the diagonal and cross-daughter fiber products constant. Hence these, and only these, attain (4). For \(m=0\) each fiber contains at most the two swapped ordered pairs, which always have equal products; the sole condition is equal absolute values. This completes the proof.

## Verification

The included dependency-free `checker.py` implements the integer fiber formula, verifies (2) for all differences in eleven representative rings, and tests the sharp ratio with exact Gaussian-integer arithmetic on random inputs and explicit equality constructions. It also verifies direct complex Fourier orthogonality in selected small moduli. Execution using `python3 checker.py` returned `EXACT_CHECKS_PASSED 85388`. These checks sample finitely many rings and inputs; the proof above, not this test count, establishes all prime powers and all equality cases.

## Relationship to prior work

Hickman and Wright establish the Fourier restriction framework on \(\mathbb Z/N\mathbb Z\), including paraboloid estimates, prime-power scaling, and exponent thresholds [1]. Their results do not state the exact \(L^2\)-to-\(L^4\) norm or classify its equality cases at each odd prime power. González-Riquelme and Oliveira e Silva establish sharp *finite-field* extension results [2]; their one-dimensional parabola endpoint is \(L^2\to L^6\), while the displayed \(L^2\to L^4\) theorem concerns a two-dimensional paraboloid. Kingsbury-Neuschotz analyzes the one-dimensional parabola over **squarefree moduli** [3], rather than repeated odd prime powers; the paper's pair-congruence approach is related. The present exact ratio and rigidity result address the prime-power degeneracy and classify every equality configuration. These comparisons are based on the inspected statements and relevant proofs, not on an assertion that an exhaustive literature search can establish uniqueness.

## Limitations

The result does not cover modulus divisible by \(2\), mixed-prime moduli, other polynomial graphs, or extension exponents other than \(4\). The proof is algebraic and does not certify independence or absence of equivalent formulations in uncatalogued literature. No independent validation has been performed.

## References

[1] J. Hickman and J. Wright, *The Fourier Restriction and Kakeya Problems over Rings of Integers Modulo N*, Discrete Analysis 2018:11, arXiv:1801.03176, first posted 2018-01-09.

[2] C. González-Riquelme and D. Oliveira e Silva, *Sharp extension inequalities on finite fields*, arXiv:2405.16647, first posted 2024-05-26.

[3] N. Kingsbury-Neuschotz, *On a Restriction Problem of Hickman and Wright for the Parabola over Z/NZ for Squarefree N*, arXiv:2509.09885, first posted 2025-09-11 (comparison only).
