# Affine rigidity and a zero–one law for Gaussian norm values

## Finding
Let \(\mathcal S_2=\{x^2+y^2:x,y\in\mathbb Z\}\), including \(0\), and for integers \(a\ge1\), \(b\ge0\), \(H\ge0\) define
\[
G_{a,b}(H)=\#\{(x,y)\in\{0,\ldots,H\}^2: a(x^2+y^2)+b\in\mathcal S_2\}.
\]
Then the **zero–one law** is
\[
\boxed{\lim_{H\to\infty}\frac{G_{a,b}(H)}{(H+1)^2}=
\begin{cases}1,&b=0\text{ and }a\in\mathcal S_2,\\0,&\text{otherwise.}\end{cases}}
\]
In particular, this completely classifies affine self-maps of the two-square set:
\[
\boxed{a\mathcal S_2+b\subseteq\mathcal S_2\quad\Longleftrightarrow\quad b=0\text{ and }a\in\mathcal S_2.}
\]
The local statement is exact: whenever \(b>0\) and \(q\equiv3\pmod4\) is prime with \(q\nmid ab\), exactly
\[
\boxed{q(q^2-1)}
\]
ordered residue pairs \((x,y)\pmod{q^2}\) make \(q\) divide \(a(x^2+y^2)+b\) to exponent exactly one. Thus their proportion is \(q^{-1}-q^{-3}\), independent of \(a,b\). For every finite set \(Q\) of such primes,
\[
\limsup_{H\to\infty}\frac{G_{a,b}(H)}{(H+1)^2}
\le\prod_{q\in Q}\left(1-\frac1q+\frac1{q^3}\right).
\]

## Assumptions and scope
Integers \(a\ge1\), \(b\ge0\) are fixed as \(H\to\infty\). The coordinates \(x,y\) range independently and uniformly over the integer square \(\{0,\ldots,H\}^2\); the statement is **not** a conditional density among distinct representable integers. Zero coordinates and the zero norm are allowed. For a positive integer \(m\), \(v_q(m)\) is its \(q\)-adic valuation. All local valuation conditions concern strictly positive \(m\), ensured when \(b>0\).

## Proof
**Step 1: Exactly count one inert-prime obstruction.** Choose any prime \(q\equiv3\pmod4\) with \(q\nmid ab\). The residue \(c\equiv-b a^{-1}\pmod q\) is nonzero. Since \(-1\) is nonsquare modulo \(q\), the quadratic extension \(\mathbb F_{q^2}=\mathbb F_q[i]\) has a surjective norm map from its cyclic multiplicative group to \(\mathbb F_q^\times\). The norm kernel has \(q+1\) elements, so the equation
\[
x^2+y^2\equiv c\pmod q
\]
has exactly \(q+1\) ordered residue solutions. Each has \((x,y)\not\equiv(0,0)\pmod q\). Its \(q^2\) lifts modulo \(q^2\) can be written \((x+qu,y+qv)\), where \(u,v\pmod q\). Divisibility of \(a((x+qu)^2+(y+qv)^2)+b\) by \(q^2\) is one nontrivial affine linear condition on \((u,v)\), because the gradient \((2ax,2ay)\) is nonzero modulo \(q\). Exactly \(q\) of the \(q^2\) lifts satisfy it, and the other \(q^2-q\) lifts have valuation exactly one. Hence the number of forbidden residue pairs is
\[
(q+1)(q^2-q)=q(q^2-1),
\]
proving the stated local density after division by \(q^4\). This proof includes the smallest admissible prime \(q=3\).

**Step 2: Local obstructions have zero-density complement.** Fermat–Euler's two-square criterion says that a positive integer is a sum of two squares only if its valuation at every prime \(q\equiv3\pmod4\) is even. Let \(Q\) be any finite set of primes as in Step 1. For every \((x,y)\) counted by \(G_{a,b}(H)\), the coordinates modulo \(q^2\) avoid the forbidden residues, for all \(q\in Q\). By the Chinese remainder theorem, these conditions are independent for uniformly distributed coordinate residues modulo \(\prod_{q\in Q}q^2\), and the surviving fraction is exactly
\[
\prod_{q\in Q}\left(1-\frac1q+\frac1{q^3}\right).
\]
For a **fixed** modulus, uniform lattice boxes converge to uniform residue frequencies, yielding the displayed upper bound. The standard divergence \(\sum_{q\equiv3\ (4)}q^{-1}=\infty\), unaffected by omission of the finitely many prime factors of \(ab\), forces this finite Euler product to tend to zero as \(Q\) increases. This proves the zero-density statement for every \(b>0\), without exchanging an infinite sieve limit with the box limit.

**Step 3: Zero-intercept classification and exact preservation.** If \(b=0\) and \(a\in\mathcal S_2\), the two-square multiplication identity
\[
(u^2+v^2)(x^2+y^2)=(ux-vy)^2+(uy+vx)^2
\]
shows that every pair is counted, so the density equals one and the affine map preserves the whole set. If \(b=0\) and \(a\notin\mathcal S_2\), the two-square criterion supplies a prime \(q\equiv3\pmod4\) with odd \(v_q(a)\). Every nonzero \(x^2+y^2\) has even \(v_q\); hence their product with \(a\) has odd valuation and fails the criterion. The origin is the sole successful pair, so \(G_{a,0}(H)=1\). Finally, if \(b>0\), Step 1 supplies explicit forbidden residue pairs for every available \(q\), hence a concrete nonnegative two-square input whose affine image is not two-square representable. This proves both implications of the preservation classification.

## Verification
The companion standalone `verify_affine_norms.py` uses exact integers. It verifies the complete local count \(q(q^2-1)\) for \(q=3,7,11,19\) and fourteen admissible \((a,b,q)\) parameter cases; independently checks Chinese-remainder independence for all \(441^2=194481\) coordinate pairs modulo \(3^2\cdot7^2\); and checks the positive and negative zero-intercept patterns plus direct affine counterexamples. Running `python3 verify_affine_norms.py` prints `VERIFY_OK`. Finite checks do not prove the unrestricted statement; Steps 1–3 do.

## Relationship to prior work
Radomskii's *On sums of two squares and a basis of order 2* (first posted 2026-04-22) studies long intervals in which \(n\) and \(an+b\) cannot both be **primitive** sums of two squares; its Theorem 1.1 assumes \(a\nmid b\). That restriction, the integer-progressions counting domain, and its gap conclusion differ from the present exact affine-preserver classification and **lattice-point** zero–one law for all sums of two squares. Harrington, Jones, and Lamarche analyze representability modulo general integers and state the classical multiplicative closure and prime-exponent criterion; their modular-solvability classifications do not supply this exact local lift count tied to an affine shift or the global lattice density. The classical two-square criterion, finite-field norms, the multiplication identity, and divergence of reciprocal primes in the class \(3\pmod4\) are used as established ingredients, not asserted as new discoveries.

## Limitations
The law gives a zero or one **limit**, not a quantitative rate or exact asymptotic for the number of surviving lattice pairs when \(b>0\). It concerns nonnegative integer coefficients and unrestricted Gaussian norms, not primitive norms, arbitrary quadratic forms, relative density among distinct values, or general polynomial maps. The local count requires \(q\nmid ab\); such primes nevertheless exist infinitely often when \(b>0\). An earlier formulation via more general polynomial sieves or norm-form value distributions could subsume aspects of the density conclusion; independent priority assessment remains necessary.

## References
1. A. Radomskii, *On sums of two squares and a basis of order 2*, arXiv:2604.20653v1, publicly posted 2026-04-22, https://arxiv.org/abs/2604.20653.
2. J. Harrington, L. Jones, and A. Lamarche, *Representing Integers as the Sum of Two Squares in the Ring Z_n*, arXiv:1404.0187v1, publicly posted 2014-04-01, https://arxiv.org/abs/1404.0187.
3. Fermat–Euler two-square theorem; Brahmagupta–Fibonacci product identity; finite-field norm surjectivity; divergence of reciprocal primes \(3\pmod4\) (classical results).
