# Wild-prime fibre laws and collision growth for sums of two prime powers

## Finding

For every prime \(p\ge5\), integer \(n\ge0\), and residue \(a\bmod p^n\), define
\[
R_{p,n}(a)=\#\{(x,y)\bmod p^n:x^p+y^p\equiv a\pmod{p^n}\},\qquad F_{p,n}(a)=p^{-n}R_{p,n}(a).
\]
Here \(R_{p,0}(0)=F_{p,0}(0)=1\). Define the finite Teichmüller set and its additive-convolution counts by
\[
H_p=\{u^p\bmod p^2:1\le u<p\},\qquad
m_p(c)=\#\{(h,k)\in H_p^2:h+k\equiv c\pmod{p^2}\},
\]
\[
g_p(c)=m_p(c)+2\mathbf1_{H_p}(c),\qquad G_p=p^{-2}\sum_{c\bmod p^2}g_p(c)^2.
\]
The set \(H_p\) consists of the \(p-1\) Teichmüller unit representatives modulo \(p^2\), and \(g_p(0)=p-1\).

**Exact finite-depth fibre theorem.** The following are identities for every residue \(a\) of the specified modulus:
\[
F_{p,1}(a)=1;
\]
\[
F_{p,n}(a)=g_p(a\bmod p^2)+p^{n-2}\mathbf1_{p^n\mid a},\qquad 2\le n\le p;
\]
\[
F_{p,n}(a)=g_p(a\bmod p^2)+p^{p-2}\mathbf1_{p^p\mid a}
F_{p,n-p}(a/p^p\bmod p^{n-p}),\qquad n\ge p.
\]
At the common boundary \(n=p\), the two displays agree.

**Exact normalized collision theorem.** Put
\[
M_{p,n}=p^{-3n}\#\{(x,y,u,v)\bmod p^n:x^p+y^p\equiv u^p+v^p\pmod{p^n}\}
=p^{-n}\sum_{a\bmod p^n}F_{p,n}(a)^2.
\]
Then
\[
M_{p,0}=M_{p,1}=1,
\]
\[
M_{p,n}=G_p+\frac{2(p-1)}{p^2}+p^{n-4},\qquad 2\le n\le p,
\]
\[
\boxed{M_{p,n}=G_p+\frac{2(p-1)}{p^2}+p^{p-4}M_{p,n-p}\qquad(n\ge p).}
\]
In particular, \(M_{p,n}\asymp_p p^{(p-4)n/p}\) and therefore tends to infinity for every prime \(p\ge5\).

**Limiting law.** The pushforward of normalized Haar measure on \(\mathbb Z_p^2\) under \((x,y)\mapsto x^p+y^p\) is absolutely continuous with respect to normalized Haar measure on \(\mathbb Z_p\). Its density \(F_p\) satisfies, for all nonzero \(t\in\mathbb Z_p\),
\[
F_p(t)=g_p(t\bmod p^2)+p^{p-2}\mathbf1_{t\in p^p\mathbb Z_p}F_p(t/p^p).
\]
The finite-level functions \(F_{p,n}(t\bmod p^n)\) converge almost everywhere and in \(L^s\) whenever \(0<s<p/(p-2)\). The exact moment threshold is
\[
\boxed{F_p\in L^s(\mathbb Z_p)\quad\Longleftrightarrow\quad 0<s<\frac{p}{p-2}.}
\]
Thus \(\int_{\mathbb Z_p}F_p\,dt=1\), while \(\int F_p^2\,dt=+\infty\) for every prime in the stated range.

For the concrete wild prime \(p=5\), \(H_5=\{1,7,18,24\}\), \(G_5=52/25\), and the collision law becomes \(M_{5,n}=12/5+5M_{5,n-5}\) for \(n\ge5\); for example \(M_{5,5}=M_{5,6}=37/5\) and \(M_{5,7}=73/5\). Exactly 13 residue classes modulo 25 occur in the support of the Haar density, hence the support has Haar measure \(13/25\).

## Assumptions and scope

All variables in finite congruences range independently over complete residue systems, and the prime \(p\) is the same as the exponent. All measures are normalized additive Haar measures on \(\mathbb Z_p\); a density is a real-valued Radon–Nikodym derivative, not a \(p\)-adic-valued distribution. The density is defined up to a null set; its value at \(t=0\) is immaterial and may be assigned arbitrarily. The exponent range is \(p\ge5\), not arbitrary fixed exponents or primes different from the exponent.

## Proof

**1. Prime-power images of units.** The multiplicative decomposition \(\mathbb Z_p^\times\cong\mu_{p-1}\times(1+p\mathbb Z_p)\) is valid for odd \(p\). Raising to the \(p\)th power fixes the Teichmüller root-of-unity component and takes the principal-unit group bijectively onto \(1+p^2\mathbb Z_p\) (for instance via the convergent logarithm). Consequently, if \(X\) is Haar-uniform on \(\mathbb Z_p\), the subprobability law of \(X^p\) on the unit-input event has density
\[
u_U(t)=p\,\mathbf1_{H_p+p^2\mathbb Z_p}(t).
\]
Each of the \(p-1\) unit-image cosets has mass \(1/p\). In particular \(|H_p|=p-1\), \(H_p\cap p\mathbb Z_p=\varnothing\), and \(H_p\) is closed under negation, implying \(m_p(0)=p-1\).

On the event \(X\in p\mathbb Z_p\), which has probability \(1/p\), write \(X=pX'\). Then \(X'\) is Haar-uniform and \(X^p=p^p(X')^p\). Writing \(\nu\) for the full distribution of \(X^p\), this proves an exact decomposition as finite measures:
\[
\nu=\nu_U+\frac1p(S_p)_*\nu,\qquad S_p(t)=p^pt.
\]

**2. Convolution and normalization.** The law \(\mu=\nu*\nu\) of \(X^p+Y^p\) decomposes into unit/unit, the two mixed parity-of-divisibility cases, and nonunit/nonunit. In unit/unit, there are \(m_p(c)\) ordered Teichmüller pairs whose sum lies in \(c+p^2\mathbb Z_p\); its density is precisely \(m_p(t\bmod p^2)\). In a mixed case, adding the \(p^p\)-divisible input to a unit-image coset does not change its uniform distribution, giving density \(\mathbf1_{H_p+p^2\mathbb Z_p}\) in each of the two cases. Finally, nonunit/nonunit has total mass \(p^{-2}\) and conditional output \(p^p\) times an independent copy of \(X^p+Y^p\). Thus
\[
\mu=g_p(t\bmod p^2)\,dt+\frac1{p^2}(S_p)_*\mu.
\]
Note that \(\int g_p\,dt=(p-1)^2/p^2+2(p-1)/p^2=1-p^{-2}\). After \(k\) iterations, the residual nonnegative measure has total mass \(p^{-2k}\to0\), so the geometric expansion proves absolute continuity and the almost-everywhere density recursion, with no hidden atom at zero.

**3. Finite levels.** The normalized count \(F_{p,n}(a)\) is the density of the finite-output law relative to uniform counting measure modulo \(p^n\). At depth one, Fermat's little theorem makes the outputs of two independent inputs uniform modulo \(p\), so \(F_{p,1}=1\). For \(2\le n\le p\), both nonunit inputs contribute only the residue zero; their combined probability \(p^{-2}\) has normalized density \(p^{n-2}\) at zero. The unit-containing cases have density \(g_p\), giving the finite base formula. For \(n\ge p\), division of the nonunit/nonunit target by \(p^p\) gives exactly the indicated lower-depth fibre, including \(n=p\) with depth-zero normalization one. This proves every finite-depth formula without invoking an asymptotic lifting argument.

**4. Collision recurrence.** Square the finite-level density and average over \(a\bmod p^n\). The square of the nonsingular part contributes \(G_p\). The extra term lies only on \(p^p\mid a\), where \(g_p(a\bmod p^2)=g_p(0)=p-1\). The cross term is therefore
\[
2p^{p-2}p^{-p}(p-1)\,\mathbb E(F_{p,n-p})=\frac{2(p-1)}{p^2},
\]
because each normalized finite-level density has mean one. The square of the singular term is \(p^{2p-4}p^{-p}M_{p,n-p}=p^{p-4}M_{p,n-p}\). For depths \(2\le n\le p\), the identical calculation with the delta-at-zero term gives \(G_p+2(p-1)/p^2+p^{n-4}\). Repeated application along the residue classes of \(n\bmod p\), with strictly positive initial values and multiplier \(p^{p-4}>1\), proves the two-sided exponential-growth estimate.

**5. Sharp moment integrability.** Put \(B_p=\max_{c\bmod p^2}g_p(c)\). For \(t\ne0\) with \(v_p(t)=pk+r\), \(0\le r<p\), iteration stops after at most \(k+1\) contributions, yielding \(0\le F_p(t)\le B_p\sum_{j=0}^k p^{j(p-2)}\ll_p p^{k(p-2)}\). The Haar measure of the shell \(v_p(t)=pk+r\) is \((1-p^{-1})p^{-pk-r}\). Summing shell upper bounds gives convergence of the \(s\)th moment whenever \(s(p-2)<p\).

For the reverse direction choose, for each \(k\ge0\), the pairwise-disjoint set \(E_k=p^{pk}(H_p+p^2\mathbb Z_p)\). This set has Haar mass \((p-1)p^{-pk-2}\) and consists of numbers of valuation exactly \(pk\). The nonnegative recursive expansion gives \(F_p(t)\ge 2p^{k(p-2)}\) there (the last-stage term includes \(2\mathbf1_{H_p}\)). The integral of \(F_p^s\) is therefore at least a positive constant times \(\sum_{k\ge0}p^{k(s(p-2)-p)}\), which diverges exactly for \(s\ge p/(p-2)\).

**6. Convergence.** The finite densities \(F_{p,n}\), pulled back to \(\mathbb Z_p\), are conditional expectations of \(F_p\) with respect to the residue-class sigma fields. Since \(F_p\in L^1\), they converge almost surely and in \(L^1\). For \(1<s<p/(p-2)\), \(F_p\in L^s\) and conditional-expectation convergence holds in \(L^s\). For \(0<s<1\), \(L^1\) convergence implies \(L^s\) convergence by concavity/Jensen. The full theorem follows.

## Verification

Run `python3 verify.py` from the extracted package. It forms the residues of prime powers by direct modular exponentiation, builds the exact output multiplicity distribution by integer pair-convolution of those residues, divides by the required normalization, and compares each target with the independently derived recurrence. It also recomputes the collision moment using exact rational arithmetic. Checks cover all target residues for primes 5 through depth 6, 7 through depth 4, and 11 through depth 3, totaling 23,793 target comparisons, as well as exact fifth-power constants and larger-depth moment recurrences. These computations test finite identities but do not substitute for the preceding infinite proof.

## Relationship to prior work

Brüdern and Vaughan (2021) study the distribution and variance of *positive integer sums of two cubes* in arithmetic progressions; their congruence counts concern degree three and global asymptotic variance, rather than the wild prime-as-exponent family here. Ramanujam (1963) considers Waring-type *existence and bounded numbers of summands* in \(p\)-adic rings, without giving these two-input target-fibre distributions or all-level collision recurrences. Skinner (2020) addresses solvability of diagonal systems with large variable counts, not this two-variable density. Bories' explicit Newton-polyhedron zeta-function theorem requires nondegeneracy over the residue field; for \(x^p+y^p-a\) every derivative with respect to the variables vanishes modulo \(p\), invalidating that assumption in the wild-degree setting.

The algebraic description of principal units and the existence of general rationality theorems for local congruence series are classical. The new claim is the combined explicit **target-by-target, every-level** recursion, sharp collision-growth law, and moment spectrum in the wild-prime two-variable family, not a claim to have invented \(p\)-adic integration or the prime-power unit decomposition.

## Limitations

The result does not address unequal exponents, primes different from the exponent, or diagonal forms with more than two summands. The constants \(G_p\) are expressed as exact finite sums modulo \(p^2\), not simplified uniformly into an elementary function of \(p\); additive coincidences within \(H_p\) vary with the prime. Almost-everywhere density values at zero are not canonical. A more general specialized local-zeta or singular-density theorem could subsume some statements; the inspected literature does not establish absolute publication priority. Independent mathematical audit has not been performed.

## References

1. J. Brüdern and R. C. Vaughan, “A Montgomery–Hooley Theorem for sums of two cubes,” *European Journal of Mathematics* **7** (2021), 1616–1644, first public date September 20, 2021. DOI: 10.1007/s40879-021-00495-4.
2. C. P. Ramanujam, “Sums of m-th powers in p-adic rings,” *Mathematika* **10** (1963), 137–146. DOI: 10.1112/S002557930000406X.
3. C. Skinner, “Solvability of systems of diagonal equations over p-adic local fields,” *Proceedings of the London Mathematical Society* **122** (2021), 207–228; first published May 4, 2020. DOI: 10.1112/plms.12318.
4. B. Bories, “Igusa's p-adic local zeta function associated to a polynomial mapping and a polynomial integration measure,” arXiv:1012.5087, §§1, 5, especially Definitions 1.4–1.5 and Theorem 5.6.
