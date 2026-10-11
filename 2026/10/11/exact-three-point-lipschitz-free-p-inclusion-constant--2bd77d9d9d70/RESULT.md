# Exact three-point Lipschitz-free \(p\)-inclusion constant

## Finding
Fix \(0<p<1\). For every inclusion of pointed real \(p\)-metric spaces \(N\subset M\) with exactly three points in \(N\), write \(L[N,M;p]:\mathcal F_p(N)\to\mathcal F_p(M)\) for the canonical linearization of inclusion. Set
\[
K_p=\sup_{\substack{N\subset M\\|N|=3}}\|L[N,M;p]^{-1}\|,
\]
where the norm is measured on the image. The exact universal value is
\[
\boxed{K_p=\left(\frac{4}{4-2^{p+1}+2^{2p}}\right)^{1/p}.}
\]
The bound holds for infinite as well as finite superspaces; the supremum is attained in a four-point weighted-star metric. In the notation of Cúth and Raunig, \(K_p=\mathfrak{aa}_p(2)\). The contribution is the matching universal **upper** bound: their Proposition 3.24 already supplied the corresponding lower witness.

## Assumptions and scope
All vector spaces and free spaces use **real scalars**. The exponent is any real \(0<p<1\). A pointed \(p\)-metric space \((M,d,0)\) means that \(\rho(s,t)=d(s,t)^p\) is an ordinary metric. The free \(p\)-space \(\mathcal F_p(M)\) is the universal real \(p\)-Banach linearization of the pointed metric, with \(\delta(0)=0\) and molecules \(\delta(s)-\delta(t)\) of \(p\)-norm \(d(s,t)\). The canonical inclusion is contractive. Inverse norms are understood only for the finite-dimensional image of \(\mathcal F_p(N)\). The theorem concerns a **three-point subset**, or equivalently a two-dimensional free \(p\)-space; no ambient compactness or cardinality bound is imposed.

## Proof
**1. Three-terminal weighted-median identity.** Let \(t_0,t_1,t_2\) be distinct points of any pointed \(p\)-metric space, and let real coefficients \(m_0+m_1+m_2=0\). Write \(a_i=|m_i|^p\). Then
\[
\left\|\sum_{i=0}^{2}m_i\delta(t_i)\right\|_{\mathcal F_p(M)}^p
 =\inf_{z\in M}\sum_{i=0}^{2}a_i\rho(t_i,z).\tag{1}
\]
For finite \(M\), apply the spanning-tree norm formula of Cúth--Raunig, Theorem 2.2 [2]. Remove every zero-flow edge: all its discarded components have zero net mass. Each remaining leaf must be a terminal with nonzero mass. Suppress every zero-mass degree-two vertex, using the triangle inequality for \(\rho\) to replace each pair of adjacent edges by their shortcut without increasing cost; the flow magnitudes on both edges coincide. With at most three terminal leaves, the reduced tree is a path or a three-arm star, whose unique central vertex \(z\) is in \(M\). Each remaining arm carries the total mass \(m_i\) of its terminal, so its cost is the right-hand expression at \(z\) (if the center is a terminal, that arm has zero length). Conversely, the three-molecule star representation about any \(z\in M\) proves the reverse inequality through the \(p\)-triangle inequality. For arbitrary \(M\), use the finite-subset infimum formula [2, Fact 1.1] and take the infimum over finite subsets containing all terminals, establishing (1).

For the intrinsic space \(N=\{t_0,t_1,t_2\}\), this specializes to
\[
\|\mu\|_{\mathcal F_p(N)}^p
=\min_{i=0,1,2}\sum_{j\ne i}a_j\rho(t_j,t_i).\tag{2}
\]
If one coefficient vanishes, \(\mu\) is one molecule and its free norm is unchanged by any inclusion. Hence assume all three coefficients are nonzero.

**2. A uniform comparison at an arbitrary center.** Fix any \(z\in M\), write \(r_i=\rho(t_i,z)\), \(A=a_0+a_1+a_2\), and \(S=\sum_i a_i r_i\). Define \(b_i=A-2a_i\). Since each \(m_i\) is the sum of the other two coefficients with opposite sign, the scalar \(p\)-triangle inequality ensures \(b_i>0\) for \(0<p<1\) when all coefficients are nonzero. The metric triangle inequality and (2) imply
\[
\|\mu\|_{\mathcal F_p(N)}^p
\le \min_i\bigl(S+b_i r_i\bigr)
=S+\min_i b_i r_i.\tag{3}
\]
Set \(h=\min_i b_i r_i\) and \(F=\sum_i a_i/b_i\). Because \(r_i\ge h/b_i\), one has \(S\ge hF\). Thus, also for \(h=0\),
\[
\|\mu\|_{\mathcal F_p(N)}^p\le(1+F^{-1})S.\tag{4}
\]

**3. Exact scalar bound.** Permuting and scaling the three masses, write \((m_0,m_1,m_2)=(-1,u,1-u)\) with \(0<u<1\). Put \(a=u^p\), \(b=(1-u)^p\), \(t=a+b\), and \(v=2^{1-p}\). Then \(1<t\le v<2\). Put \(s=a-b\). The three denominators \(b_i\) are \(t-1\), \(1-s\), and \(1+s\), so exactly
\[
F=\frac{1}{t-1}+\frac{a}{1-s}+\frac{b}{1+s}
=\frac{1}{t-1}+\frac{t+s^2}{1-s^2}
\ge\frac{1}{t-1}+t
\ge\frac{1}{v-1}+v.\tag{5}
\]
The final inequality uses that \(t+1/(t-1)\) decreases on \((1,2)\). Hence
\[
1+F^{-1}\le1+\frac{v-1}{v^2-v+1}
=\frac{v^2}{v^2-v+1}
=\frac4{4-2^{p+1}+2^{2p}}.\tag{6}
\]
Combine (4)--(6), take \(\inf_{z\in M}\) and use (1). For every \(\mu\in\mathcal F_p(N)\), this proves the universal upper bound on the inverse norm. The space \(\mathcal F_p(N)\) is two-dimensional; its coefficients are unique, and the lower estimate yields injectivity for any \(M\).

**4. Attainment.** Set \(q=2^p\in(1,2)\). Construct four points \(M=\{0,x,y,z\}\) with center \(z\), and make \(\rho=d^p\) the shortest-path metric of the star with lengths
\[
\rho(z,x)=\rho(z,y)=q^{-1},\qquad \rho(z,0)=(2-q)^{-1}.\tag{7}
\]
Let \(N=\{0,x,y\}\) and \(\mu=\delta(x)+\delta(y)\); its signed masses are \((-2,1,1)\). By (1) the ambient \(p\)-norm satisfies
\[
\|L\mu\|_{\mathcal F_p(M)}^p=S:=\frac2q+\frac{q}{2-q},\tag{8}
\]
since every terminal hub adds one unit to the center cost. By (2), its intrinsic norm is
\[
\|\mu\|_{\mathcal F_p(N)}^p=S+1.\tag{9}
\]
Indeed the hub \(x\) and hub \(y\) both cost \(S+1\), and the hub \(0\) also costs \(S+1\). Directly
\[
\frac{S+1}{S}=\frac4{4-2q+q^2}
=\frac4{4-2^{p+1}+2^{2p}},\tag{10}
\]
so (6) is sharp. This completes the proof.

## Verification
The analytic proof uses the cited finite tree-norm identity and elementary scalar inequalities, not the numerical checks. The supplied standalone standard-library program `three_terminal_median_check.py` enumerates labelled spanning trees for small finite metric spaces; verifies the three-terminal median formula against all tree costs for several real exponents and signed measures; checks (5)--(6) on deterministic samples; and checks the equality star both numerically and by a rational algebraic identity. Run `python3 three_terminal_median_check.py`; expected terminal line: `THREE_TERMINAL_P_FREE_MEDIAN_AND_SHARP_CONSTANT_CHECK_OK`. These **finite tests are supplementary**: the proof above, together with [2, Theorem 2.2 and Fact 1.1], establishes the universal statement.

## Relationship to prior work
Cúth and Raunig [2, Sections 2 and 3.3, Proposition 3.24] established the spanning-tree norm formula, studied three-point embeddings, and gave exactly the lower-bound value \(\bigl(4/(4-2^{p+1}+2^{2p})\bigr)^{1/p}\) as an attained witness, without the matching universal upper bound. The present finding is the **upper bound**, with a three-terminal median reduction and a scalar inequality (5) that forces their witness to be globally sharp. Albiac and Ansorena [1, Theorem 3.5] recently proved a uniform embedding estimate for every pointed \(p\)-metric subspace, with a much larger, cardinality-independent constant; their theorem does not determine this sharp three-point value. Related published geometric work on classical Lipschitz-free spaces concerns distinct invariants (octahedrality, quantitative Schur properties, or numerical index), not this nonlocally convex canonical-inclusion norm. Literature identification remains subject to an unindexed-equivalence risk.

## Limitations
Only **real** \(\mathcal F_p\) spaces with \(0<p<1\), pointed three-point subsets, and ambient **\(p\)-metrics** are covered. No sharp bound is asserted for larger terminal subsets, for a distinct ambient exponent \(q>p\), or for complex coefficients. The median identity uses the established tree-norm formula [2] as an external theorem; it is not proved from the universal property alone here. An independent audit has not been performed. No claim of priority against inaccessible or unindexed literature is implied by search nonhits.

## References
[1] Fernando Albiac and José L. Ansorena, *Lipschitz extensions into \(p\)-Banach spaces, and canonical embeddings of Lipschitz-free \(p\)-spaces for \(0<p<1\)*, arXiv:2603.28193v1 (first publicly posted 2026-03-30), Sections 1--3, especially Theorem 3.5. https://arxiv.org/html/2603.28193v1

[2] Marek Cúth and Tomáš Raunig, *Canonical embedding of Lipschitz-free \(p\)-spaces*, arXiv:2311.02920v1 (first publicly posted 2023-11-06), Fact 1.1, Theorem 2.2, Corollary 2.7, Definition 3.1, Theorem 3.9, Proposition 3.24. https://arxiv.org/html/2311.02920v1
