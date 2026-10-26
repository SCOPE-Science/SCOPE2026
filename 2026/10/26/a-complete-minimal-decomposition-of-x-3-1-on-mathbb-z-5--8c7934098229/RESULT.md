# A complete minimal decomposition of \(x^3+1\) on \(\mathbb Z_5\)

## Finding

Let \(f:\mathbb Z_5\to\mathbb Z_5\) be \(f(x)=x^3+1\), where \(\mathbb Z_5\) is the ring of 5-adic integers and \(\nu_5\) is its normalized valuation. The full dynamical decomposition is as follows.

1. The four residue classes \(0,1,2,4\pmod5\) form the basin of a unique attracting 4-cycle lifting \(0\mapsto1\mapsto2\mapsto4\mapsto0\). This basin has normalized Haar measure \(4/5\).
2. The ball \(B=3+5\mathbb Z_5\) is invariant and contains a unique fixed point \(\alpha\), the unique root of \(x^3-x+1=0\) in \(B\).
3. For each integer \(k\ge1\), the shell \(S_k=\alpha+5^k\mathbb Z_5^\times\) is a clopen invariant minimal set. These shells are pairwise disjoint, exhaust \(B\setminus\{\alpha\}\), and have Haar measure \(4/5^{k+1}\).
4. For every \(n>k\), the action on the finite quotient of \(S_k\) modulo \(5^n\) is one cycle of exact length \(4\cdot5^{n-k-1}\). Hence the only periodic orbits in \(\mathbb Z_5\) are the attracting 4-cycle and the fixed point \(\alpha\).

The statement is specific to \(f(x)=x^3+1\) on \(\mathbb Z_5\); it makes no claim about other primes or other polynomials.

## Assumptions and scope

All arithmetic is in \(\mathbb Z_5\). A shell \(S_k\) is defined using the 5-adic unit group \(\mathbb Z_5^\times\). “Minimal” means that every forward orbit in the invariant compact set is dense in that set. Haar measure is normalized by \(\mu(\mathbb Z_5)=1\). The finite-level formula concerns the induced map on residue classes represented by \(S_k\) modulo \(5^n\), with \(n>k\); it does not assert a single cycle on all of \(\mathbb Z_5/5^n\mathbb Z_5\).

## Proof

**1. Residue dynamics and the attracting cycle.** Modulo 5,
\[
0\mapsto1\mapsto2\mapsto4\mapsto0,\qquad 3\mapsto3.
\]
Write \(C=\{0,1,2,4\}\). For each \(a\in C\), the map \(g=f^4\) sends the ball \(a+5\mathbb Z_5\) into itself. Along the four-step residue itinerary, one iterate is congruent to 0, so the derivative
\[
g'(x)=\prod_{j=0}^{3}3\bigl(f^j(x)\bigr)^2
\]
is divisible by 5 throughout each such ball. For points \(x,y\) in the same ball, the difference quotient \((g(x)-g(y))/(x-y)\) is therefore divisible by 5; hence \(g\) is a strict contraction there. Banach’s fixed-point theorem gives exactly one fixed point of \(g\) in each of the four balls. The four fixed points are permuted by \(f\), forming a unique attracting 4-cycle. Every point in the four balls converges to that cycle under iteration of \(f\). Their union has Haar measure \(4/5\).

**2. The invariant ball and its fixed point.** Since \(f(3)\equiv3\pmod5\), the ball \(B=3+5\mathbb Z_5\) is invariant. The fixed-point equation is \(F(x)=x^3-x+1=0\). Modulo 5, \(F\) has the unique root 3, and \(F'(3)=26\not\equiv0\pmod5\). Hensel’s lemma gives a unique root \(\alpha\in B\); also \(\alpha\equiv3\pmod{25}\). For \(x,y\in B\),
\[
f(x)-f(y)=(x-y)(x^2+xy+y^2),
\]
and the second factor is congruent to \(27\equiv2\pmod5\). Thus \(f\) is an isometry on \(B\), and in particular
\[
\nu_5(f(x)-\alpha)=\nu_5(x-\alpha).
\]
It follows that each shell \(S_k=\{x:\nu_5(x-\alpha)=k\}\), \(k\ge1\), is invariant and clopen.

**3. The fourth return map near \(\alpha\).** Put \(\lambda=f'(\alpha)=3\alpha^2\) and \(g=f^4\). Because \(\alpha\equiv3\pmod{25}\), one has \(\lambda\equiv2\pmod{25}\), so
\[
g'(\alpha)=\lambda^4\equiv16\pmod{25},\qquad \nu_5(g'(\alpha)-1)=1.
\]
We also need the second derivative. Modulo 5, \(f'(\alpha)\equiv2\) and \(f''(\alpha)\equiv3\). If \(D_j=(f^j)'(\alpha)\) and \(E_j=(f^j)''(\alpha)\), then \(D_j\equiv2^j\pmod5\) and
\[
E_{j+1}\equiv3D_j^2+2E_j\pmod5,\qquad E_1\equiv3\pmod5.
\]
This gives \(E_2\equiv3\), \(E_3\equiv4\), and \(E_4\equiv0\pmod5\), hence \(g''(\alpha)\equiv0\pmod5\). Taylor expansion about \(\alpha\) now shows that for \(x\in S_k\), with \(k=\nu_5(x-\alpha)\ge1\),
\[
\nu_5(g(x)-x)=k+1.
\]
Indeed, the linear term has valuation exactly \(k+1\); the quadratic coefficient is divisible by 5, and every term of degree at least three has valuation at least \(3k\ge k+2\). The same expansion gives, throughout \(B\), \(g'(x)\equiv1\pmod5\) and \(g''(x)\equiv0\pmod5\).

**4. Exact period lifting.** We use the following elementary 5-adic lifting fact. If an analytic map \(h\) on a 5-adic ball satisfies \(h'(y)\equiv1\pmod5\) and \(h''(y)\equiv0\pmod5\) throughout the ball, and \(\nu_5(h(x)-x)=s\ge2\), Taylor expansion of five successive displacements yields
\[
h^5(x)-x\equiv5\bigl(h(x)-x\bigr)\pmod{5^{s+2}}.
\]
Thus \(\nu_5(h^5(x)-x)=s+1\). The derivative and second-derivative congruences persist for \(h^5\), so induction gives \(\nu_5(h^{5^j}(x)-x)=s+j\) for every \(j\ge0\). For an exponent coprime to 5, the valuation remains \(s\), because the displacement sum is that exponent times \(h(x)-x\) modulo \(5^{s+1}\). Applying this to \(h=g\) and \(s=k+1\) proves
\[
\nu_5\!\left(f^{4\cdot5^j}(x)-x\right)=k+1+j.
\]
Modulo \(5^{k+1}\), the first nonzero digit of \(x-\alpha\) is multiplied by 2 under \(f\), so its exact period is 4. Combining these two facts, for every \(n>k\) the least period of \(x\) modulo \(5^n\) is \(4\cdot5^{n-k-1}\).

The shell \(S_k\) contains exactly \(5^{n-k}-5^{n-k-1}=4\cdot5^{n-k-1}\) residue classes modulo \(5^n\). Since every point has that least period, the whole shell quotient is one cycle. This proves minimality of \(S_k\): the orbit meets every relative residue class at every finer level, so it is dense in \(S_k\). Every point of \(B\setminus\{\alpha\}\) belongs to exactly one shell, so there are no other periodic orbits in \(B\). Together with Step 1, this gives the full decomposition. Finally, \(\mu(S_k)=5^{-k}-5^{-(k+1)}=4/5^{k+1}\), and \(\sum_{k\ge1}\mu(S_k)=1/5\), matching the measure of \(B\).

## Verification

The included script `verify_x3_plus1_z5.py` enumerates the exact functional graphs modulo \(5^n\) for \(1\le n\le5\). It checks the predicted cycle lengths in \(B\), the unique 4-cycle in the other four residue classes, and eventual entry into that 4-cycle for every residue outside \(B\). The script prints `VERIFY_OK`. These finite checks are consistency checks only; the all-\(n\) conclusion follows from the valuation and period-lifting proof above, not from extrapolation of the finite census.

## Relationship to prior work

Fan and Liao’s general minimal-decomposition theorem for polynomial maps on \(\mathbb Z_p\) gives the qualitative framework of periodic orbits, minimal clopen components, and attracting basins; their odometer theorem explains the form of the minimal components. Their explicit classification paper on the square map treats \(x\mapsto x^2\), not the cubic \(x\mapsto x^3+1\). The result here is a map-specific decomposition: it identifies the exceptional residue class, the unique fixed point, every minimal shell, the attracting basin, the exact Haar measures, and the precise period at every finite level. It is consistent with the general framework but is not stated by those general results.

## Limitations

The finite verifier checks only \(n\le5\); it is not used as an infinite proof. The all-level claim depends on the displayed derivative congruences and period-lifting lemma. No classification is claimed for \(x^3+1\) over \(\mathbb Z_p\) when \(p\ne5\), or for other cubic polynomials. A bibliographic search cannot exclude every unindexed or unpublished treatment of this exact example.

## References

1. A.-H. Fan and L. Liao, “On minimal decomposition of \(p\)-adic polynomial dynamical systems,” *Advances in Mathematics* 228 (2011), 2116–2144; first preprint version, arXiv:1010.5583v1 (2010-10-27). Theorems A–C and the period classification provide the general framework.
2. S. Fan and L. Liao, “Dynamics of the square mapping on the ring of \(p\)-adic integers,” arXiv:1408.4574v1 (2014-08-20). This classifies the square map and serves as a comparison, not as a source for the cubic-specific claim.
