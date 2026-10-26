# Sharp periodic idempotent census for characteristic-two cycle evolution algebras

## Finding

For integers \(n\ge3\) and \(m\ge1\), let \(k=\mathbb F_{2^m}\). The **undirected-cycle evolution algebra** \(E(C_n,k)\) has natural basis \(e_0,\ldots,e_{n-1}\), with indices modulo \(n\), and multiplication
\[
e_i e_j=0\quad(i\ne j),\qquad e_i^2=e_{i-1}+e_{i+1}.
\]
Let \(I_{n,m}\) be the number of elements \(z\in E(C_n,k)\) satisfying \(z^2=z\), **including zero**. In \(\mathbb F_2[X]\), put
\[
P_m(X)=(X^2+1)^m+X^m.
\]
Then the complete two-parameter count is
\[
\boxed{I_{n,m}=2^{\deg\gcd(X^n-1,P_m(X))}.}
\]
In particular, the count is always a power of two, and it obeys the sharp, dimension-independent bound
\[
\boxed{1\le I_{n,m}\le 2^{2m}=|k|^2.}
\]
The bound is attained for infinitely many cycle lengths at every fixed \(m\).

There is an exact arithmetic description of all maximizing lengths and of the least period of \(n\mapsto I_{n,m}\). Write \(m=2^s r\) with \(r\) odd, and let \(o_r\) be the multiplicative order of the residue class of \(X\) in the finite ring \(\mathbb F_2[X]/(P_r(X))\). This is well-defined and odd. Define \(N_m=2^s o_r\). Then
\[
\boxed{I_{n,m}=2^{2m}\quad\Longleftrightarrow\quad N_m\mid n,}
\]
and \(N_m\) is the **least positive period** of the counting sequence as \(n\) varies through integers at least three. In particular, maximal counts recur with exact period \(N_m\), not merely with some unspecified finite-state period.

The first extension degrees exhibit two distinct kinds of arithmetic resonance:
\[
I_{n,1}=\begin{cases}4,&3\mid n,\\1,&3\nmid n,\end{cases}
\qquad
I_{n,2}=\begin{cases}16,&6\mid n,\\4,&3\mid n\text{ and }2\nmid n,\\1,&3\nmid n,\end{cases}
\]
and
\[
\boxed{I_{n,3}=2^{2\mathbf 1_{3\mid n}+4\mathbf 1_{5\mid n}}.}
\]
Here the indicator equals one if the indicated divisibility condition holds and zero otherwise. Thus the extension from \(\mathbb F_2\) to \(\mathbb F_8\) introduces a five-cycle resonance: for \(m=3\), all \(n\) divisible by five but not three have exactly 16 idempotents, while all \(n\) divisible by fifteen attain the maximum 64.

## Assumptions and scope

The ground field is exactly \(\mathbb F_{2^m}\), the structure constants are the binary adjacency entries of an **undirected simple** cycle with \(n\ge3\), and idempotents are elements \(z\) with \(z^2=z\). This must not be confused with the term *idempotent evolution algebra*, which often means a perfect algebra satisfying \(E^2=E\); indeed these characteristic-two cycle algebras are not perfect, because the all-ones vector is killed by their adjacency matrix. No weighting of edges, orientation, or characteristic other than two is asserted.

## Proof

**Step 1: Frobenius fixed-point lemma.** Let \(B\in M_d(\mathbb F_2)\), and for \(v\in\mathbb F_{2^m}^d\) write \(v^{[2]}\) for coordinatewise squaring. Then
\[
\#\{v:Bv^{[2]}=v\}=2^{\dim_{\mathbb F_2}\ker(B^m-I_d)}.\tag{1}
\]
Indeed, choose a normal basis \(\theta,\theta^2,\ldots,\theta^{2^{m-1}}\) of \(\mathbb F_{2^m}\) over \(\mathbb F_2\). Every \(v\) has a **unique** expansion \(v=\sum_{j=0}^{m-1}\theta^{2^j}u_j\) with \(u_j\in\mathbb F_2^d\). Squaring cyclically shifts the normal-basis indices, while \(B\) commutes with those scalar Frobenius shifts. Therefore \(Bv^{[2]}=v\) is equivalent to \(u_j=B u_{j-1}\) for all \(j\) modulo \(m\). Choose \(u_0\) arbitrarily subject to \(B^m u_0=u_0\); this uniquely determines every other \(u_j\). Thus the solution set is in bijection with the binary kernel in (1), without any invertibility assumption on \(B\).

**Step 2: The cycle polynomial.** With respect to the natural basis, the squaring map of \(E(C_n,k)\) is \(v\mapsto Av^{[2]}\), where \(A=S+S^{-1}\) and \(S\) is the cyclic coordinate shift. Under the identification
\[
\mathbb F_2^n\cong R_n:=\mathbb F_2[X]/(X^n-1),
\]
\(S\) acts by multiplication by \(X\). The element \(X\) is a unit in \(R_n\). Hence multiplication by \(A^m-I_n\) is multiplication by the unit \(X^{-m}\) times
\[
(X^2+1)^m+X^m=P_m(X).
\]
Write \(D=X^n-1\) and \(g=\gcd(D,P_m)\). In \(\mathbb F_2[X]/(D)\), the kernel of multiplication by \(P_m\) consists exactly of the residues divisible by \(D/g\). Indeed, \(D\mid P_m f\) holds if and only if \(D/g\mid f\), because \(D/g\) and \(P_m/g\) are coprime. This kernel is an \(\mathbb F_2\)-space of dimension \(\deg g\). Applying (1) proves the main formula.

**Step 3: Sharp bound.** The polynomial \(P_m\) has leading term \(X^{2m}\) and constant coefficient one; consequently \(\deg P_m=2m\). Therefore \(\deg\gcd(D,P_m)\le2m\), proving the bound. Its attainability, and the exact maximizing lengths, follow in Step 4.

**Step 4: Saturation and least period.** Decompose \(m=2^s r\) with \(r\) odd. Frobenius in characteristic two gives \(P_m=P_r^{2^s}\). Moreover,
\[
P_r'(X)=X^{r-1},\qquad P_r(0)=1,
\]
so \(P_r\) is squarefree and has no zero root. The finite quotient \(\mathbb F_2[X]/(P_r)\) is therefore a product of finite fields; its unit \(\bar X\) has finite **odd** order \(o_r\). Writing \(n=2^t u\) with \(u\) odd, we have \(X^n-1=(X^u-1)^{2^t}\), where \(X^u-1\) is squarefree. Consequently
\[
P_m\mid X^n-1\quad\Longleftrightarrow\quad t\ge s\text{ and }P_r\mid X^u-1
\quad\Longleftrightarrow\quad 2^s o_r\mid n.
\]
Because the main count is maximal precisely when \(P_m\mid X^n-1\), this proves the saturation criterion and supplies infinitely many maximizing \(n\).

Further, \(P_m\mid X^{N_m}-1\), so \(X^{n+N_m}-1\equiv X^n-1\pmod{P_m}\). Taking gcd with \(P_m\) shows \(I_{n+N_m,m}=I_{n,m}\) for all \(n\ge3\). If \(T>0\) were any period, take a sufficiently large multiple \(n\ge3\) of \(N_m\); then both \(n\) and \(n+T\) give the maximum \(2^{2m}\). The saturation criterion forces \(N_m\mid n+T\), hence \(N_m\mid T\). Therefore \(N_m\) is the least positive period.

**Step 5: Explicit extension degrees.** Direct polynomial arithmetic over \(\mathbb F_2\) gives
\[
P_1=X^2+X+1,\quad P_2=(X^2+X+1)^2,
\]
and
\[
P_3=(X^2+X+1)(X^4+X^3+X^2+X+1).
\]
The two factors of \(P_3\) are squarefree, irreducible, and have root orders three and five respectively. Therefore the gcd-degree formula yields exactly the three displayed cases. The minimum saturation periods are \(N_1=3\), \(N_2=6\), \(N_3=15\).

## Verification

A standalone Python 3 standard-library checker, `check_idempotents.py`, is embedded in this package. Execute `python3 check_idempotents.py` from the directory containing it. It compares the gcd formula against independently computed binary matrix nullities in 480 parameter pairs, directly enumerates idempotent coordinates over \(\mathbb F_2,\mathbb F_4,\mathbb F_8,\mathbb F_{16}\) in 19 finite cases, and tests the predicted least-period and saturation criteria in 642 additional parameter pairs (extension degrees one, two, three, four, six, and eight). It also tests the explicit formulas for all \(3\le n<80\). Expected terminal line: `CYCLE_EVOLUTION_IDEMPOTENTS_OK 480 matrix_pairs 19 direct_enumerations 642 period_tests`. These finite checks are diagnostic; Steps 1–5 prove the universal assertions.

## Relationship to prior work

Khudoyberdiyev–Omirov–Qaralleh (2013) study idempotents and cycle decompositions of **permutation** evolution algebras, whose squares contain one basis term. Elduque–Labra (2013) supply the graph–evolution-algebra framework, discussing nilpotency and automorphism groups. Neither of these inspected works states the two-neighbor cycle census here. Sriwongsa–Zou (2022) use graph adjacency matrices to study automorphism groups of perfect evolution algebras, not counts of idempotent **elements** in the present nonperfect cycle algebras. Kaygorodov–Martín González–Viruel (2026), Sections 1.4.3 and 2.1.4–2.1.5, discuss the general idempotent-equation system and the degree-\(2^n\) scheme for perfect algebras; this does not give the sharp \(2^{2m}\) cycle bound, the gcd distribution, or the least-length-period criterion.

The Frobenius normal-basis mechanism is standard and **not** claimed as new. Dempwolff–Fisher–Herman (2000) establish semilinear normal forms and invertible Frobenius-map fixed-space results; their proof explicitly uses invertibility. Here the binary adjacency matrix is singular and the particular cycle-polynomial arithmetic determines every finite-field idempotent count and exact saturation period. No absolute publication-priority or independence claim is made.

## Limitations

The formulas do not cover weighted or directed cycles, general graph algebras with arbitrary structure constants, or odd-characteristic fields. The least-period formula defines an effective arithmetic invariant \(o_r\) but does not present a simple closed formula in \(r\) for every odd \(r\). It counts labeled algebra elements, not isomorphism classes of algebras or automorphism orbits of idempotents. Previously unlocated algebraic-dynamical literature could contain an equivalent general reduction; independent mathematical assessment and full priority verification remain outstanding.

## References

1. A. Kh. Khudoyberdiyev, B. A. Omirov, I. Qaralleh, *Few remarks on evolution algebras*, arXiv:1307.0993v1, first public 2013-07-03. https://arxiv.org/abs/1307.0993
2. A. Elduque, A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1, first public 2013-12-17. https://arxiv.org/abs/1312.4685
3. S. Sriwongsa, Y. M. Zou, *On Automorphism Groups of Idempotent Evolution Algebras*, arXiv:2202.01333v2. https://arxiv.org/html/2202.01333v2
4. I. Kaygorodov, C. Martín González, A. Viruel, *Evolution algebras: a survey of results and a list of open problems*, arXiv:2610.22248v1, 2026-10-15. https://arxiv.org/html/2610.22248v1
5. U. Dempwolff, J. C. Fisher, A. Herman, *Semilinear transformations over finite fields are Frobenius maps*, Glasgow Mathematical Journal 42 (2000), 289–295. DOI: 10.1017/S0017089500020164.
