# Finite-volume clock-factor aliasing in traveling affine cellular automata

## Finding
For integers \(q\ge2\), \(L\ge1\), and \(r\ne0\), put \(A=\mathbb Z/q\mathbb Z\) and define the invertible periodic-ring map
\[
 (F_L x)_i=x_{i+r}+1\pmod q,\qquad i\in\mathbb Z/L\mathbb Z.
\]
A **scalar clock factor** means a surjective map \(h_L:A^L\to A\) with \(h_L(F_Lx)=h_L(x)+1\). Every map on this finite discrete space is continuous.

The fixed-point count for every \(n\ge1\), with \(d=\gcd(L,rn)\), is
\[
 \#\operatorname{Fix}(F_L^n)=\begin{cases}q^d,&q\mid nL/d,\\0,&q\nmid nL/d.\end{cases}
\]
Moreover, a scalar clock factor exists **if and only if**
\[
  v_p(L)<v_p(|r|)+v_p(q)\quad\text{for every prime }p\mid q. \tag{1}
\]
Here \(v_p\) is the usual nonnegative \(p\)-adic valuation of a positive integer. The same local rule on \(A^{\mathbb Z}\) has a fixed configuration and hence has **no** scalar clock factor, although its constant configurations all have exact time period \(q\).

There are arbitrarily large \(L\) for which \(\gcd(L,rq)=1\). For **every** such \(L\), scalar clock factors exist, but every scalar clock factor depends essentially on **all** \(L\) coordinates. This lower bound is attained by the normalized global sum
\[
 h_L(x)=L^{-1}\sum_{i\bmod L} x_i\pmod q.
\]
Thus finite periodic approximants can possess genuine global scalar clock observations absent from the infinite system, and their required observation support grows without bound.

## Assumptions and scope
The group \(A=\mathbb Z/q\mathbb Z\) is additive; \(q\) need not be prime. Index shifts are interpreted modulo \(L\), even when \(|r|>L\). All results hold for every integer \(r\ne0\) and all \(L\ge1\), including composite \(q\), without asymptotic assumptions. For the infinite full shift, the topology is the product topology; a scalar clock factor is a continuous surjection to the discrete cyclic system \(a\mapsto a+1\). This scalar factor is **not** a claim of surjectivity onto the entire configuration space of a radius-zero clock cellular automaton.

A coordinate \(i\) is **essential** for a function \(h_L:A^L\to A\) if two configurations agreeing at every other coordinate yield different outputs. The support of \(h_L\) is the set of its essential coordinates.

## Proof
**Iterates and fixed-point counts.** Direct induction gives \((F_L^n x)_i=x_{i+rn}+n\pmod q\). A rotation by \(rn\) of a ring of length \(L\) splits its coordinates into exactly \(d=\gcd(L,rn)\) cycles of common length \(\ell=L/d\). The equation \(F_L^n x=x\) forces successive values along each such spatial cycle to decrease by \(n\). Closing the cycle is possible precisely when \(q\mid n\ell\). If possible, its first value may be chosen arbitrarily from \(A\), independently for each of the \(d\) cycles. This proves the exact count, including the cases \(L=1\) and \(r<0\).

**A factor criterion for a finite permutation.** For any permutation \(P\) of a finite set, a surjective map \(h\) satisfying \(h(Px)=h(x)+1\pmod q\) exists exactly when **each** cycle length of \(P\) is divisible by \(q\). Necessity follows by going once around an orbit. For sufficiency, choose a starting label in \(A\) separately on each orbit, and propagate it by adding one; divisibility makes this unambiguous, and each nonempty orbit then surjects onto \(A\).

**The arithmetic condition.** All cycles of \(F_L\) have lengths divisible by \(q\) precisely when \(F_L^n\) has no fixed points for every positive integer \(n\) with \(q\nmid n\). For any prime \(p\mid q\), writing \(a=v_p(q)\), \(b=v_p(L)\), and \(c=v_p(|r|)\), observe that
\[
 v_p\!\left(\frac{nL}{\gcd(L,rn)}\right)
 =v_p(n)+b-\min\{b,c+v_p(n)\}
 =\max\{v_p(n),b-c\}.\tag{2}
\]
Suppose (1) holds. For \(q\nmid n\), choose a prime \(p\mid q\) with \(v_p(n)<v_p(q)=a\). Then both arguments of the maximum in (2) are strictly below \(a\), so \(q\nmid nL/\gcd(L,rn)\), ruling out fixed points. Conversely, if (1) fails for some \(p\), so \(b-c\ge a\), choose \(n=q/p\). The maximum in (2) is at least \(a\) for this prime and for any other \(p'\mid q\), \(v_{p'}(n)=v_{p'}(q)\). Thus \(q\mid nL/\gcd(L,rn)\). Because \(q\nmid n\), the fixed-point formula supplies an orbit whose length does not divide the clock congruence, contradicting the existence of a clock factor. Hence (1) is necessary and sufficient.

**Infinite-versus-finite difference.** On \(A^{\mathbb Z}\), choose any bi-infinite configuration satisfying \(x_{i+r}=x_i-1\) for all \(i\). This is possible by choosing one value in each residue class modulo \(|r|\) and propagating in both directions. It satisfies \(F_\infty x=x\). Equivariance into the scalar clock would imply \(h(x)=h(x)+1\pmod q\), impossible. By contrast, every constant configuration evolves via \(a\mapsto a+1\), so all constant-configuration periods equal \(q\). This shows that the constant-cycle divisibility obstruction is inconclusive here.

**Forced delocalization.** Choose any \(L\) coprime to \(rq\); there are arbitrarily many such sizes. Since \(L\) is invertible modulo \(q\), the displayed global-sum map satisfies \(h_L(F_Lx)=h_L(x)+1\) and is surjective. If \(h\) is *any* scalar clock factor, then \(h\circ F_L^q=h\). But \(F_L^q\) is spatial translation by \(rq\) positions, which generates **all** cyclic translations when \(\gcd(L,rq)=1\). Consequently \(h\) is invariant under every one-step rotation of coordinates. The essential-coordinate support of a rotation-invariant function is invariant under this transitive coordinate permutation group. Since \(h\) is surjective it is nonconstant, so its support is nonempty and therefore includes all \(L\) sites. The global sum uses each site essentially, attaining the bound.

## Verification
The standalone `verify.py` exhaustively enumerates all configurations for \(2\le q\le6\), \(1\le L\le5\), and \(r\in\{-3,-2,-1,1,2,3\}\). It independently checks the fixed-point formula at every iterate through the exact permutation order; computes all permutation-orbit lengths and compares their common clock divisibility with the prime-valuation condition; and tests the explicit global sum and essential-coordinate support where applicable. Run `python3 verify.py` with only the Python standard library. The script reports 59,926 successful finite assertions. All universal claims are proved above, not inferred from finite tests.

## Relationship to prior work
Gwóźdź's 2026 theorem proves that a weak factor from an infinite-lattice cellular automaton onto a radius-zero clock cellular automaton requires all source periodic point periods, including constant-configuration periods, to be divisible by the clock length. The current result is an exact **finite-ring scalar-clock factor criterion** for a natural reversible affine family, combined with a global observation-support lower bound and an explicit infinite-volume countercontrast. The original theorem supplies the motivating necessary obstruction but neither the prime-valuation classification for periodic rings nor the support result. The distinction between scalar factors and full spatial clock factors is essential.

Hudcová and Krásenský study intrinsic simulation and affine cellular automata by local-algebra transformations; their simulation preorder is not the non-shift-equivariant scalar factor relation considered here. The fixed-point enumeration uses classical cyclic-orbit arithmetic rather than claiming a new counting technique.

## Limitations
The scalar finite-ring clock factor must not be confused with a surjective factor onto the entire finite spatial clock automaton. The theorem treats one traveling affine rule with uniform increment, not arbitrary affine or nonlinear cellular automata. For ring sizes meeting (1) but not coprime to \(rq\), it establishes factor existence but makes no universal minimum-support claim. There is residual bibliographic risk of an equivalent formula in earlier finite-ring literature. Numerical checks do not certify statements for unbounded \(L\) or \(q\).

## References
- M. Gwóźdź, *No weakly factor-universal cellular automaton*, arXiv:2603.23570v1 (first public 2026-03-24), https://arxiv.org/abs/2603.23570.
- B. Hudcová and J. Krásenský, *Simulation Limitations of Affine Cellular Automata*, arXiv:2311.14477v2 (2024), https://arxiv.org/abs/2311.14477.

