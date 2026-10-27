# Arithmetic onset and exact birth counts of wrapped fixed points on discrete Huygens paths

## Finding
Let \(m\ge2\) and \(N=m-1\). For the unit-weight \(m\)-oscillator path, consider the reduced map on \(\mathbb T^N=(\mathbb R/2\pi\mathbb Z)^N\)
\[
G_h(z)=z+hK_N\sin z\pmod{2\pi},\qquad h>0,
\]
where \(K_N\) is tridiagonal with diagonal entries \(2\) and immediate off-diagonal entries \(-1\). A *wrapped* fixed point means \(G_h(z)=z\) but \(\sin z\ne0\); equivalently its real-lift displacement is a nonzero vector in \(2\pi\mathbb Z^N\). Every nonwrapped fixed point is one of the \(2^N\) configurations \(z_i\in\{0,\pi\}\).

Let \(p\) be the smallest odd prime factor of \(m\), when one exists. Set
\[
 h_*(m)=\begin{cases}
 \pi(1-1/p),&\text{if }m\text{ has an odd prime factor }p,\\
 \pi,&\text{if }m\text{ is a power of two}.
 \end{cases}
\]
Then **no wrapped fixed point exists for \(0<h<h_*(m)\)**, and **wrapped fixed points exist already at \(h=h_*(m)\)**. The exact additional fixed-point counts at the threshold are
\[
 \#\operatorname{Fix}_{\rm wrap}(G_{h_*})=
 \begin{cases}
 (p-1)2^{N-2m/p},&p\text{ exists},\\
 (m-1)2^N,&m\text{ is a power of two}.
 \end{cases}
\]
For each fixed \(m\), there exists \(\varepsilon_m>0\) such that the count is constant throughout \(h_*<h<h_*+\varepsilon_m\) and equals
\[
 \#\operatorname{Fix}_{\rm wrap}(G_h)=
 \begin{cases}
 (p-1)2^N,&p\text{ exists},\\
 2^N\displaystyle\sum_{\substack{d\mid m\\d\ge2}}\varphi(d)2^{m/d},&m\text{ is a power of two}.
 \end{cases}
\]
Here \(\varphi\) denotes Euler's totient function. These counts are geometric fixed points on the torus, not counts of lift labels or orbits. For example, three oscillators have \(h_*=2\pi/3\) and gain exactly two fixed points at onset, then eight immediately above it; four oscillators have \(h_*=\pi\) and gain 24, then 64.

## Assumptions and scope
The underlying interaction is the repulsive sine law with all edge weights equal to one; the map uses edge-difference coordinates, with a single positive step \(h\). Integers \(m\ge2\) are arbitrary and fixed before choosing \(\varepsilon_m\). A wrapped fixed point is defined relative to the displayed real lift; it is never a critical point of the cosine potential. Statements concern fixed-point **existence and multiplicity**, not their stability, attraction, or absence of higher-period cycles. At \(h=h_*\), some of the new solutions have coordinates where \(\lvert\sin z_i\rvert=1\), so no unproved hyperbolicity assertion is made.

## Proof
**1. Convert fixed points to a lattice problem.** A torus fixed point has an integer lift vector \(w\in\mathbb Z^N\) satisfying
\[
 hK_N\sin z=2\pi w.
\]
Put \(u=h\sin z/(2\pi)\), and write \(t=h/(2\pi)\). Then \(u\in K_N^{-1}\mathbb Z^N\) and \(\lVert u\rVert_\infty\le t\). Conversely, every such \(u\) gives exactly
\[
 2^{\#\{i:\lvert u_i\rvert<t\}}
\]
distinct torus solutions, because each unsaturated sine value has two angular preimages and each saturated value has exactly one. Since \(K_N\) is positive definite, \(w=0\) gives \(u=0\), hence exactly the \(2^N\) unwrapped configurations.

**2. Classify lattice residues.** Append boundary coordinates \(u_0=u_m=0\). The condition \(K_Nu\in\mathbb Z^N\) reads
\[
 2u_i-u_{i-1}-u_{i+1}\in\mathbb Z\quad(1\le i<m).
\]
Successive increments \(u_i-u_{i-1}\) are equal modulo integers. Therefore there is a unique residue \(k\in\{0,\ldots,m-1\}\) such that
\[
 u_i\equiv\frac{ik}{m}\pmod1\quad(1\le i<m).
\]
The endpoint \(u_m=0\) forces exactly this cyclic classification, and every choice of integer representatives of these residues does give an integer vector \(K_Nu\). If \(k=0\) and \(u\ne0\), then \(\lVert u\rVert_\infty\ge1\). For \(k\ne0\), let \(d=m/\gcd(k,m)>1\). The displayed fractions cycle through the nonzero residues of denominator \(d\), each repeated \(m/d\) times. Taking each coordinate to its nearest integer representative minimizes the max norm in that class, yielding
\[
 q(d)=\frac{\lfloor d/2\rfloor}{d}=
 \begin{cases}\frac12-\frac1{2d},&d\text{ odd},\\\frac12,&d\text{ even}.\end{cases}
\]
When a residue equals \(1/2\), there are two equally nearest representatives; otherwise there is exactly one. Thus the smallest norm of a nonzero lattice vector is \((p-1)/(2p)\) when \(m\) has an odd divisor (its smallest possible odd divisor is its smallest odd prime \(p\)), and \(1/2\) when all divisors of \(m\) are powers of two. These minimal norms are strictly below one, so the zero residue class contributes no competitor. Multiplication by \(2\pi\) gives \(h_*\), and simultaneously proves both the lower exclusion and attainment.

**3. Count the first wrapped points for odd \(p\).** The minimizing residue classes are precisely those with order \(p\); there are \(\varphi(p)=p-1\). Each has a unique minimax lattice representative, with exactly \(2m/p\) saturated coordinates at the two extreme nonzero fractions \((p-1)/(2p)\) and \((p+1)/(2p)\). Its sine-inverse multiplicity at \(t=(p-1)/(2p)\) is therefore \(2^{N-2m/p}\). Multiplying by \(p-1\) gives the threshold count. Just above threshold, each of these representatives has \(2^N\) nonsaturated sine inverses.

**4. Count the first wrapped points for powers of two.** If \(m=2^s\), every nonzero residue class of order \(d\mid m\) has exactly \(m/d\) half-integer coordinates. There are \(\varphi(d)\) such classes. Each has \(2^{m/d}\) minimax lattice representatives (independent choices of \(+1/2\) or \(-1/2\)), each with \(2^{N-m/d}\) threshold sine inverses. Hence each nonzero residue class contributes \(2^N\) threshold fixed points, and summing the \(m-1\) classes gives \((m-1)2^N\). Immediately above threshold every minimizing representative has \(2^N\) angular choices; grouping classes by \(d\) gives the totient sum.

**5. Prove the open interval count.** The lattice \(K_N^{-1}\mathbb Z^N\) is discrete. Consequently, after removing its finitely many minimal nonzero vectors, the remaining nonzero lattice vectors have a strictly larger infinity norm. Choose \(\varepsilon_m>0\) smaller than the corresponding positive norm gap multiplied by \(2\pi\), and small enough to keep \(h<2\pi\), excluding nonzero vectors from the integral residue class. Exactly the enumerated minimal representatives contribute for all \(h_*<h<h_*+\varepsilon_m\). All their sine coordinates are then strictly interior, completing the counts and proof.

## Verification
The self-contained Python 3 standard-library program `verify_winding.py` uses rational arithmetic to enumerate, for each path length \(2\le m\le16\), all minimizing representatives of every nonzero residue class. It independently verifies that the second-difference vector \(K_Nu\) is integral, checks uniqueness of lift labels, and compares the computed smallest norms, saturated-coordinate counts, and strict-above counts with the theorem. Run `python3 verify_winding.py` from the directory containing the embedded file. All fifteen tests pass. These finite calculations **do not prove** the assertion for arbitrary \(m\); the proof is the residue argument above.

## Relationship to prior work
Buescu, D'Aniello and Oliveira (arXiv:2610.10993v1), Section 5.2 and Corollary 5.4, introduce precisely the path map and prove Morse–Smale dynamics with only the \(2^N\) critical fixed points for \(0<h<[2+2\cos(\pi/m)]^{-1}\). Their Proposition 3.4 gives fixed-point exclusion through the strict-Lyapunov regime. The present result is at **much larger** coupling \(h\ge 2\pi/3\): it establishes the first noncritical torus fixed points, arithmetic dependence on the smallest odd prime divisor of \(m\), and exact birth multiplicities. Other known small-step fold and flip calculations concern inverse preimages or temporal two-cycles, not these large-step torus fixed points.

## Limitations
The theorem is an exact family-specific statement; it does not describe other graphs, weighted paths, or general interaction laws. The new points may be degenerate at onset. It does not exclude other phenomena at smaller steps (e.g. periodic cycles). The comparison of mathematical records and inspected source text did not uncover equivalent fixed-point counting results, but historical priority under alternative terminology for modulo-angle wrapping remains a risk. No independent validation has been performed.

## References
1. J. Buescu, E. D'Aniello and H. M. Oliveira, *Morse–Smale dynamics in discrete Huygens networks*, arXiv:2610.10993v1, October 7, 2026, https://arxiv.org/html/2610.10993v1 (Sections 2–5, especially Corollary 5.4).
2. `verify_winding.py` (included with this result), standalone exact-rational checks of the fixed-point onset formulas.
