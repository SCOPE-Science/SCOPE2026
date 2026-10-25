# Eventual prefix Abelian powers at every Tribonacci substitution length

## Finding
Let \(\tau(0)=01\), \(\tau(1)=02\), and \(\tau(2)=0\), let \(t=\tau^\omega(0)\), and set \(U_m=\tau^m(0)\) and \(L_m=|U_m|\). For **every integer \(k\ge 2\)** there exists an effectively computable integer \(M(k)\) such that for **every** \(m\ge M(k)\) and **every** \(j\in\{0,1,\ldots,k\}\),
\[
\Psi(t[0:jL_m])=j\Psi(U_m).
\]
Here \(t[0:n]\) is the prefix of length \(n\), and \(\Psi\) is the three-coordinate Parikh vector. Hence the first \(kL_m\) symbols split into \(k\) successive blocks, each of length \(L_m\) and each having Parikh vector \(\Psi(U_m)\). In particular, **every sufficiently large Tribonacci substitution length is the order of a prefix Abelian \(k\)-power**, and therefore of an additive \(k\)-power.

The constructive threshold uses greedy base-\(\beta\) expansions of the integers \(1,\ldots,k\), where \(\beta>1\) is the real root of \(X^3-X^2-X-1\). Write the finite expansion of \(j\) as \(j=\sum_{r\in E_j}\beta^r\) with \(E_j\subset\mathbb Z\) finite, and set
\[
M(k)=\max\bigl(0,\max_{1\le j\le k}[-\min E_j]\bigr).
\]
The finiteness property of this Pisot base makes the algorithm terminate. Verified examples of sufficient (not claimed minimal) thresholds are \(M(3)=3\), \(M(4)=6\), \(M(10)=9\), \(M(20)=9\), \(M(50)=14\), \(M(100)=15\), and \(M(200)=17\). In particular, for each \(m\ge6\) the prefix of length \(4L_m\) is an Abelian fourth power; the order \(L_6=44\) has each block's Parikh vector \((24,13,7)\).

## Assumptions and scope
Indices start at zero. \(U_0=0\), \(U_1=01\), \(U_2=0102\), with the exact concatenation law \(U_{m+3}=U_{m+2}U_{m+1}U_m\). Thus \(L_0=1\), \(L_1=2\), \(L_2=4\), and both \(L_m\) and each coordinate of \(P_m=\Psi(U_m)\) satisfy the order-three Tribonacci recurrence. An Abelian \(k\)-power means \(k\) consecutive equal-length blocks with identical Parikh vectors. The result is about **prefixes**, not a classification of every factor or every admissible order. It uses the known finiteness theorem for base \(\beta\), not an assumed conjecture.

## Proof
**1. Exact prefix numeration.** For every finite binary digit string \(d_s\cdots d_0\) avoiding `111`, define \(N=\sum_{i=0}^s d_iL_i\) and \(W_d=U_s^{d_s}U_{s-1}^{d_{s-1}}\cdots U_0^{d_0}\). Then \(W_d=t[0:N]\). Proof by induction on \(s\): \(W_d\) is a prefix of \(U_{s+1}\). If \(d_s=0\), apply induction to the remaining string to get a prefix of \(U_s\). If \(d_s=1,d_{s-1}=0\), the remaining factors (indices at most \(s-2\)) form a prefix of \(U_{s-1}\); hence \(W_d\) is a prefix of \(U_sU_{s-1}\). If \(d_s=d_{s-1}=1\), avoidance of `111` forces \(d_{s-2}=0\); the remaining factors form a prefix of \(U_{s-2}\), so \(W_d\) is a prefix of \(U_sU_{s-1}U_{s-2}=U_{s+1}\). The cases \(s=0,1,2\) are verified directly. Since \(U_{s+1}\) is a prefix of \(t\), the lemma follows. Taking Parikh vectors gives
\[
\Psi(t[0:N])=\sum_{i=0}^s d_iP_i.
\]

**2. Finite expansions of ordinary integers.** The real Tribonacci root \(\beta\) has a finite greedy expansion of \(1\) with fractional digits `111` and satisfies the Frougny–Solomyak finiteness condition (F): every nonnegative element of \(\mathbb Z[\beta^{-1}]\) has a finite base-\(\beta\) expansion. Specifically their theorem applies to the positive root of \(X^3-a_1X^2-a_2X-a_3\) with \(a_1\ge a_2\ge a_3>0\); here all three coefficients are \(1\). Every positive integer \(j\) thus has a finite greedy expansion \(j=\sum_{r\in E_j}\beta^r\). Since \(1<\beta<2\), digits lie in \(\{0,1\}\). Greediness excludes three consecutive ones: a block \(111\) at positions \(r-1,r-2,r-3\) equals the single digit at position \(r\), because \(\beta^3=\beta^2+\beta+1\).

**3. Polynomial transfer to the substitution lengths and Parikh vectors.** The polynomial \(g(X)=X^3-X^2-X-1\) is irreducible over \(\mathbb Q\): neither possible rational root \(\pm1\) vanishes. Thus for each \(j\), the Laurent polynomial \(q_j(X)=j-\sum_{r\in E_j}X^r\), which vanishes at \(\beta\), is divisible by \(g(X)\) in \(\mathbb Q[X,X^{-1}]\). The sequences \((L_m)\) and \((P_m)\) satisfy \(g(S)=0\), with forward shift \(S\). Consequently, for every \(m\) for which each \(m+r\ge0\),
\[
jL_m=\sum_{r\in E_j}L_{m+r},\qquad jP_m=\sum_{r\in E_j}P_{m+r}.
\]
The recurrence can be applied without crossing a negative index because the lowest exponent of \(q_j\) also bounds the lowest exponent in its quotient by \(g\) (whose constant term is nonzero).

**4. Shift back into the Tribonacci word.** Fix \(k\), and select \(M(k)\) as in the finding. For any \(m\ge M(k)\), shift each finite expansion of \(j\le k\) upward by \(m\). Its digit pattern still avoids `111` and uses only nonnegative indices. By Step 3 it represents the integer \(jL_m\), and by Step 1 its prefix Parikh vector is \(\sum_{r\in E_j}P_{m+r}=jP_m\). This also holds at \(j=0\), with both sides zero. Subtract the prefix identities for consecutive \(j\) to conclude that every length-\(L_m\) block in the first \(kL_m\) positions has Parikh vector \(P_m\). This proves all quantifiers of the theorem.

## Verification
Run `python3 verify.py`. It evaluates exact powers of \(\beta\) inside the cubic ring \(\mathbb Z[\beta]\), uses high-precision decimal comparisons only to choose greedy digits, and subsequently checks every resulting identity by exact integer-triple arithmetic. It reproduces finite expansions for integers \(1\) through \(200\), confirms admissibility, algebraic length/Parikh identities at several substitution levels, checks the first \(10{,}000\) canonical prefix decompositions against directly generated words, and checks five explicit prefix-power examples. The final line is `TRIB_PREFIX_ABELIAN_PASS beta_expansions=200 canonical_prefix_tests=10000 parikh_examples=5`. These are finite reproducibility checks. The **arbitrary-\(k\)** conclusion comes from the published finiteness theorem and the recurrence proof, not from extrapolating the 200 tests.

## Relationship to prior work
Popoli, Shallit and Stipulanti (arXiv:2410.02409, first posted October 3, 2024) study additive powers in the Tribonacci word. Their Section 5, Theorems 35–36 and Problem 37 address existence, automata for cubes, and the open task of characterizing allowed additive-power orders. Their results do not explicitly assert the eventual **prefix Abelian powers at every Tribonacci substitution length for every fixed exponent** proved here. Their Theorem 35, that Abelian squares occur at every order somewhere in the word, is stronger than the present order coverage for \(k=2\), but does not imply the present prefix identity. The existence of additive powers of every exponent, already known from bounded complexity, also does not imply a cofinal prescribed family of orders or prefix locations.

Frougny and Solomyak (1992) supply the finiteness property of the Tribonacci base as an indispensable previously published premise, not as a new result. Shallit (2020) and Couvreur et al. (2025) investigate Tribonacci Parikh synchronization and (generalized) Abelian complexity. These provide broader algorithmic background but their inspected statements do not yield the specific prefix-power conclusion without additional argument. Existing Sturmian/Fibonacci Abelian-power classifications have a different binary fixed point and cannot by themselves establish a ternary Tribonacci prefix theorem.

## Limitations
This does **not** characterize all orders of additive or Abelian \(k\)-powers; \(M(k)\) need not be minimal. The proof uses the previously published finiteness property (F), whose original publisher full text was not accessible in this review; its precise standard formulation is corroborated by a separate mathematical exposition, and the finite examples are independently exact-checked. The available literature searches do not rule out an unindexed equivalent. No independent mathematical audit has been performed.

## References
- P. Popoli, J. Shallit, M. Stipulanti, *Additive word complexity and Walnut*, arXiv:2410.02409v1 (October 3, 2024), especially Section 5, Problem 37, https://arxiv.org/abs/2410.02409.
- C. Frougny, B. Solomyak, *Finite beta-expansions*, Ergodic Theory and Dynamical Systems 12 (1992), 713–723, doi:10.1017/S0143385700007057.
- M. R. Iacò, *Finite beta-expansions and bounded remainder sets*, exposition of the Frougny–Solomyak finiteness criterion, https://www.irif.fr/~fan/uploads/Main/Admont.pdf.
- J. Shallit, *Abelian Complexity and Synchronization*, arXiv:2011.00453 (2020).
- J.-M. Couvreur et al., *Effective Computation of Generalized Abelian Complexity for Pisot Type Substitutive Sequences*, arXiv:2504.13584 (2025), Sections 1, 3–4.
