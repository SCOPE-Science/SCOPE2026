# Explicit positive gamma enumerators for weighted-bond Möbius polynomials of cycles

## Finding

Let \(C_n\) be the simple cycle on \(n\ge3\) vertices, and let \(\mu_{C_n}(t)\) be the weighted-bond-poset Möbius polynomial introduced by González D'León and Wachs [1]. Define its sign-adjusted polynomial by \(c_n(t)=(-1)^{n-1}\mu_{C_n}(t)\). The complete gamma vector of every such cycle is determined by one algebraic generating function.

Let \(T=T(z,u)\) be the unique formal series of zero constant term satisfying
\[
T=z(1+T+uT^2).
\]
Then, for all \(n\ge3\),
\[
c_n(t)=\sum_{j=0}^{\lfloor(n-1)/2\rfloor}\gamma_{n,j}t^j(1+t)^{n-1-2j},\qquad
\gamma_{n,j}=[z^n u^j]\frac{T^2(1+uT)}{1-uT^2}.
\]
Every displayed gamma coefficient is a **strictly positive integer**. In fact, for every \(n\ge3\), \(\gamma_{n,0}=n-1\). Equivalently, the whole positive coefficient array has the exact Lagrange-inversion formula
\[
\begin{aligned}
\gamma_{n,j}={}&\frac1n\sum_{r=0}^{j}(2r+2)
\binom{n}{j-r,\ n-2j-2,\ j+r+2}\\
&+\frac1n\sum_{r=0}^{j-1}(2r+3)
\binom{n}{j-r-1,\ n-2j-1,\ j+r+2},
\end{aligned}
\]
where a multinomial coefficient is understood to vanish when an entry is negative, and an empty sum is zero. This is an exact all-orders enumeration, not merely a positivity test.

For example, the gamma vectors at lengths \(3,4,5,6,7\) are \((2,1)\), \((3,6)\), \((4,18,4)\), \((5,40,30)\), and \((6,75,120,15)\).

## Assumptions and scope

All graphs are finite and simple. The invariant \(\mu_G(t)\) is the polynomial of [1] obtained by summing the Möbius values from the least weighted connected-partition element to each maximal one-block element, with weight parameter \(t\). For a connected graph \(G\) of order greater than one it is characterized by the published bond-partition recursion
\[
\mu_G(t)=-\sum_{\substack{\pi\text{ a connected-block partition of }V(G)\\|\pi|\ge2}}[|\pi|]_t\prod_{B\in\pi}\mu_{G[B]}(t),\qquad
[k]_t=1+t+\cdots+t^{k-1},
\]
with \(\mu_{K_1}(t)=1\); for disconnected induced blocks, use the product over connected components. For simple cycles only the one-block value and proper path blocks enter this formula.

The auxiliary formal term at degree two below is a bookkeeping device for cyclic compositions; it does not assert the existence of a simple two-vertex cycle. The theorem begins at \(n=3\). The formal variables \(z,u,t\) commute, and rational expressions are interpreted in formal-power-series rings, not as analytic identities requiring convergence.

## Proof

**Step 1: the path series.** Put \(a_m(t)=(-1)^{m-1}\mu_{P_m}(t)\) for the path on \(m\ge1\) vertices. Theorem 3.2 of [1] proves \(a_m(t)\) is the Narayana polynomial, with generating series
\[
P(x,t)=\sum_{m\ge1}a_m(t)x^m=x(1+P(x,t))(1+tP(x,t)).
\]
In particular, every proper connected induced block in a cycle is a path whose sign-adjusted polynomial contributes the corresponding coefficient of \(P\).

**Step 2: cyclic connected partitions.** A partition of the vertices of \(C_n\) into \(k\ge2\) connected nonempty blocks is a cyclic composition into \(k\) consecutive proper paths. For each ordered list of \(k\) positive block lengths summing to \(n\), placing its initial marked boundary at one of the \(n\) cycle vertices and forgetting the choice of which of the \(k\) blocks was marked counts each partition exactly \(k\) times. Thus the cycle recursion from [1], including the block-sign factors, gives
\[
\sum_{n\ge2}c_n(t)x^n
=x\frac{\partial}{\partial x}\sum_{k\ge2}\frac{(-1)^k[k]_t}{k}P(x,t)^k.
\]
The coefficient at \(n=2\) is the formal value \(1+t\) and is not used as a graph invariant.

**Step 3: summation.** The elementary formal identity
\[
\sum_{k\ge1}(-1)^k[k]_tP^{k-1}=-\frac1{(1+P)(1+tP)}
\]
and differentiation of \(P=x(1+P)(1+tP)\) give
\[
x\frac{\partial P}{\partial x}=\frac{P(1+P)(1+tP)}{1-tP^2}.
\]
Subtracting the \(k=1\) summand in the first identity yields the closed ordinary generating function
\[
\sum_{n\ge2}c_n(t)x^n=\frac{P^2(1+t+tP)}{1-tP^2}.
\]

**Step 4: gamma transformation.** Set \(z=(1+t)x\), \(u=t/(1+t)^2\), and \(T=(1+t)P\). The path equation becomes exactly \(T=z(1+T+uT^2)\). Multiplying the last displayed cycle generating function by \(1+t\) now yields
\[
\sum_{n\ge2}(1+t)c_n(t)x^n
=\frac{T^2(1+uT)}{1-uT^2}.
\]
The right-hand side is a formal series in \(z,u\) with nonnegative integer coefficients, because \(T\) counts plane rooted trees having zero, one, or two ordered children, weighted by \(u\) for each binary node. Explicitly,
\[
\frac{T^2(1+uT)}{1-uT^2}
=\sum_{r\ge0}u^rT^{2r+2}+\sum_{r\ge0}u^{r+1}T^{2r+3}.
\]
Thus its \(z^nu^j\) coefficient counts ordered forests of \(2r+2\) such trees with \(r\) additional marks or ordered forests of \(2r+3\) trees with \(r+1\) marks, where the number of binary nodes supplies the remaining exponent of \(u\). This is a coefficientwise positive combinatorial model for the whole cycle gamma array.

Extracting coefficients gives the claimed gamma expansion and simultaneously proves palindromicity in degree \(n-1\). Lagrange inversion applied to each \(T^k\), namely
\[
[z^n]T^k=\frac{k}{n}[v^{n-k}](1+v+uv^2)^n,
\]
gives exactly the two stated multinomial sums. Their rational summands add to positive integers because they count actual forests. For every \(0\le j\le\lfloor(n-1)/2\rfloor\), positivity follows without cancellation: if \(n\ge2j+2\), choose \(r=j\) in the first forest sum; if \(n=2j+1\), choose \(r=j-1\) in the second. In each case there is at least one admissible term. Finally, setting \(u=0\) gives \(T=z/(1-z)\), so the constant gamma coefficient is \([z^n]T^2=n-1\). This proves all parts. \(\square\)

## Verification

The standalone `cycle_verify.py` independently implements the source bond-partition recursion by generating all set partitions of path and cycle vertex sets, testing connectedness directly, and computing integer-polynomial products. It compares the resulting cycle polynomials for every order \(3\le n\le9\) with the **separately implemented** Lagrange-multinomial gamma formula and its reconstruction of \(c_n(t)\). It also checks strict positivity and the first-gamma-coefficient formula for \(3\le n\le80\). Execute `python3 cycle_verify.py` in a directory containing that file, with no third-party packages. The finite tests are corroboration; the displayed formal derivation is the unrestricted proof.

## Relationship to prior work

The invariant, bond-partition recurrence (Theorem 3.1) and Narayana path specialization (Theorem 3.2) are from González D'León and Wachs [1]. Their Conjecture 4.12 asks for gamma positivity for all graphs; their discussion explicitly acknowledges earlier work establishing real-rootedness for the **cycle case**, which already implies gamma positivity there. **Neither cycle real-rootedness nor bare gamma positivity is claimed as new.** The present claim is narrower and constructive: an explicit positive two-variable generating function, all individual gamma coefficients by multinomial sums, and a plane unary–binary forest model.

The distinct nestohedron \(h\)-polynomial recurrences of Ávila Ramírez, Carrillo, and González D'León [2] are relevant but are not recurrences for the weighted-bond polynomial of a cycle. Earlier work on the cyclohedron's \(h\)-polynomial likewise does not identify it with \(\mu_{C_n}(t)\). In particular the first coefficient of the signless cycle polynomial is \(n-1\), not the constant coefficient one of an \(h\)-polynomial. The first source's cited 2022 thesis [3], which contains earlier cycle results, was not accessible in full and may contain a related exact formula; priority remains subject to that comparison.

## Limitations

This finding applies only to simple cycles of order at least three and supplies a gamma-coefficient enumeration; it does not prove the graph-wide positivity conjecture, deduce new real-rootedness, or classify weighted-bond polynomials of general cactus graphs. An earlier unpublished or difficult-to-access formula might supersede the enumerator. The independent mathematical verification and final bibliographic priority assessment have not been performed.

## References

1. R. S. González D'León and M. L. Wachs, *Weighted bond posets and a new chromatic symmetric function*, arXiv:2608.08692v1, first posted 2026-08-09, Sections 3.1, 3.2 and 4.3. https://arxiv.org/abs/2608.08692
2. N. Ávila Ramírez, S. A. Carrillo, and R. S. González D'León, *A Möbius function computing h-polynomials of nestohedra*, arXiv:2609.15784v1, 2026-09-14. https://arxiv.org/abs/2609.15784
3. N. Ávila Ramírez, *The μ-polynomials of graph associahedra*, undergraduate thesis, Universidad Sergio Arboleda, 2022; repository record: https://repository.usergioarboleda.edu.co/handle/11232/1821 (complete text unavailable for comparison).
