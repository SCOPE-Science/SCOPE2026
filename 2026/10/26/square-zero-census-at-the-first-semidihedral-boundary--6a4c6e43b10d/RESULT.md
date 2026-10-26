# Square-zero census at the first semidihedral boundary

## Finding
Let \(q\) be an arbitrary power of \(2\). Consider the following three groups of order \(16\), defined uniformly by
\[
G(r,c)=\langle a,b\mid a^8=1,\ b^2=a^c,\ bab^{-1}=a^r\rangle:
\quad D_{16}=G(7,0),\quad SD_{16}=G(3,0),\quad Q_{16}=G(7,4).
\]
Let \(A_G=\mathbb F_q[G]\). The number of elements \(x\in A_G\) satisfying \(x^2=0\) is exactly
\[
\begin{array}{c|c}
G & \#\{x\in A_G:x^2=0\}\\\hline
D_{16}&q^8(4q-3)\\
SD_{16}&q^8(3q-2)\\
Q_{16}&q^8(2q-1).
\end{array}
\]
At the smallest field, \(q=2\), the complete regular-rank generating polynomials, with \(\rho(x)=\dim_{\mathbb F_2}(xA_G)\), are respectively
\[
\begin{aligned}
F_D(z)&=1+z+6z^2+16z^3+72z^4+288z^6+896z^8,\\
F_S(z)&=1+z+6z^2+16z^3+72z^4+288z^6+640z^8,\\
F_Q(z)&=1+z+6z^2+16z^3+72z^4+288z^6+384z^8.
\end{aligned}
\]
Thus the three nonisomorphic order-16 maximal-class nonabelian \(2\)-groups have identical binary square-zero multiplication-rank multiplicities below \(8\), but different acyclic multiplicities at rank \(8\).

## Assumptions and scope
All algebras and linear ranks are over the stated finite field. In the generating polynomials, \(z\) is formal, each coefficient counts **elements** rather than similarity orbits, and multiplication acts on the left of the \(16\)-dimensional regular module. Group notation is fixed by the presentations above. The finite-field total-count theorem covers every \(2\)-power \(q\); the complete rank refinement asserted here is restricted to \(q=2\). No claim is made for odd characteristic, larger groups, or infinite fields with nonperfect Frobenius.

## Proof
**Algebraic reduction for the all-field totals.** Put \(t=a+1\) and \(R=\mathbb F_q[t]/(t^8)\). Then \(A_G=R\oplus Rb\), with \(bu=\sigma_r(u)b\), \(\sigma_r(a)=a^r\), and \(b^2=\delta_c\), where \(\delta_0=1\) and \(\delta_4=1+t^4\). A general \(x=u+vb\) has square zero precisely when
\[
u^2+\delta_c v\sigma_r(v)=0,\qquad v(u+\sigma_r(u))=0.
\tag{1}\]
For \(r=7\), substitution sends \(t\) to \(t+t^2+\cdots+t^7\); for \(r=3\), it sends \(t\) to \(t+t^2+t^3\). Write \(v=\sum_{i=0}^7 v_i t^i\). Because the finite-field Frobenius is an automorphism, a polynomial \(h\in R\) has a square root if and only if its coefficients of \(t,t^3,t^5,t^7\) vanish; each such \(h\) has exactly \(q^4\) roots.

If \(v\) has odd \(t\)-adic valuation \(1\) or \(3\), the coefficient of \(t^{2s+1}\) in \(v\sigma_r(v)\), after the preceding even terms, is \(v_s^2\ne0\), so (1) has no solution. If \(v\in t^4R\), then \(v\sigma_r(v)=0\), \(u\in t^4R\), and the second equation holds because \(u+\sigma_r(u)\in t^6R\). There are exactly \(q^8\) pairs in this stratum.

If \(v\) has valuation \(2\), odd-power coefficient comparison gives the single condition \(v_3(v_2+v_3)=0\). There are \(2(q-1)q^4\) admissible \(v\) (\(v_2\ne0\), \(v_3=0\) or \(v_2\), and four free higher coefficients). The square-root equation forces \(u_0=u_1=0\) and \(u_2=u_3=v_2\), leaving \(u_4,u_5,u_6,u_7\) free. All \(q^4\) roots satisfy the second equation of (1). This contributes \(2(q-1)q^8\) pairs independently of \((r,c)\).

Finally suppose \(v_0\ne0\). The odd coefficients of \(v\sigma_r(v)\) give \(v_1(v_0+v_1)=0\) and a further equation which fixes \(v_5\) uniquely after choosing \(v_0\ne0\), \(v_1\in\{0,v_0\}\), and arbitrary \(v_2,v_3,v_4,v_6,v_7\). Thus there are \(2(q-1)q^5\) such \(v\). As \(v\) is a unit, (1) also requires \(u=\sigma_r(u)\). For \(r=7\) this forces \(u_1=0\), \(u_2=u_3=u_5\), with \(u_4,u_6,u_7\) free; for \(r=3\) it forces \(u_1=0\), \(u_2=u_3\), \(u_5=0\), with the same three free coefficients. In both cases \(u_1^2=v_1(v_0+v_1)=0\).

For \((r,c)=(7,0)\), the odd-coefficient equation fixing \(v_5\) is exactly the condition that the even coefficients of degrees \(4\) and \(6\) of \(v\sigma_r(v)\) agree, so \(u_2=u_3\) always. Each admissible \(v\) yields \(q^3\) solutions, contributing \(2(q-1)q^8\). For \((r,c)=(3,0)\), these two even coefficients differ by \(v_1^2\) after imposing the odd-coefficient equations. Exactly the \(v_1=0\) half contributes, yielding \((q-1)q^8\) pairs. For \((r,c)=(7,4)\), multiplication by \(1+t^4\) adds \(v_0^2\ne0\) to the degree-four even coefficient but not to degree six; hence the required equality is impossible. Summing the three valuation strata gives the three displayed total-count formulas. These coefficient identities follow by expanding \(\sigma_r(t)\) modulo \(t^8\); no interpolation from small fields is used.

**Exact binary rank refinement.** Identify \(g_{i,j}=a^ib^j\), \(0\le i<8\), \(j\in\{0,1\}\), with index \(i+8j\). For each parameter pair \((r,c)\), group multiplication is
\[
g_{i,j}g_{k,\ell}=g_{\,i+r^jk+cj\ell\pmod 8,\;j+\ell\pmod2}.
\tag{2}\]
For each binary coordinate vector \((x_0,\ldots,x_{15})\), the coefficient of \(g_w\) in \(x^2\) is the parity of \(\sum_{i,j:\,g_ig_j=g_w}x_ix_j\). The column indexed by \(g_j\) in the matrix of left multiplication is \(\sum_{i:x_i=1}e_{g_i g_j}\). Applying these *exact* formulas to all \(2^{16}=65,536\) vectors and computing their binary Gaussian ranks yields the three coefficient lists stated above. The standalone `verify_binary.c` contains the complete finite proof by exhaustive case analysis: its loops range over every coordinate vector, every group product, and every matrix column. This is an exhaustive **finite** computation, not an extrapolation to arbitrary fields.

For \(x^2=0\), \(\operatorname{im}L_x\subseteq\ker L_x\); hence \(\rho(x)\le8\) and the homology \(\ker L_x/\operatorname{im}L_x\) vanishes precisely for rank \(8\). This justifies the acyclicity interpretation.

## Verification
Compile `verify_binary.c` with `cc -std=c99 -O2 -Wall -Wextra verify_binary.c -o verify_binary` and run it. It verifies every one of the \(65,536\) binary elements independently in each of the three group algebras. `verify_ring_lift.c`, compiled analogously, enumerates the pairs \((u,v)\) through the distinct \(R\oplus Rb\) presentation, verifies the same binary ranks, and additionally checks the all-field total formulas at \(q=4\) as \(851,968\), \(655,360\), and \(458,752\), respectively. The latter finite checks do not substitute for the general valuation proof.

## Relationship to prior work
Semidihedral, dihedral and generalized quaternion groups are the three maximal-class nonabelian \(2\)-group types; their modular group algebras occupy a central place in the theory of tame blocks. Holm and Zimmermann (2008) distinguish algebras of dihedral and semidihedral type by generalized Reynolds ideals and derived invariants. Their analyzed theorems and semidihedral sections do not supply this square-zero-element or regular-multiplication-rank census. The present invariant is not asserted to be a derived-equivalence invariant.

Earlier square-zero spectra for groups \(D_{8m}\) and dicyclic groups of order \(8m\) with **odd** \(m\) have different, explicitly restricted domains: none includes these order-\(16\) groups. In particular, a similar-looking product formula from those families cannot be substituted for the counts here. The coefficient-wise common low-rank spectrum and separation only at maximal rank are new comparison claims, subject to the originality limitations below.

## Limitations
The q-uniform result counts square-zero elements only, not all their rank multiplicities. The rank-refined statement concerns precisely \(q=2\). The proof does not classify conjugacy classes, higher-order nilpotents, or larger maximal-class groups. The scientific literature search cannot certify absolute publication priority; indirect consequences of broader classification or modular algebra enumeration may exist. Independent mathematical audit has not been performed.

## References
1. T. Holm and A. Zimmermann, *Generalized Reynolds ideals and derived equivalences for algebras of dihedral and semidihedral type*, arXiv:0807.0688v1, first public 2008-07-04, https://arxiv.org/abs/0807.0688.
2. GroupNames, *SD16*, https://people.maths.bris.ac.uk/~matyd/GroupNames/1/SD16.html (group identification reference).
