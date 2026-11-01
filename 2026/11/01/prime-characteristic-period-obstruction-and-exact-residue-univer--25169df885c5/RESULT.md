# Prime-characteristic period obstruction and exact residue-universal cycles on multipartite networks

## Finding

Let \(p\ge3\) be prime, \(r\ge2\), and \(G=K_{n_1,\ldots,n_r}\) a labelled complete multipartite simple graph with positive integer part sizes and \(N=\sum_i n_i\). On \(\mathbb F_p^N\) apply the synchronous neighbour-sum update
\[
 (Fx)_v=\sum_{w\sim v}x_w\pmod p.
\]
Put \(L_p=\operatorname{lcm}_{1\le j\le p-1}(p^j-1)\) and \(C_p=pL_p\). For **arbitrary** part sizes, every configuration is periodic after at most \(p+2\) steps, every least period divides \(C_p\), and no least period is divisible by \(p^2\). Equivalently,
\[
 F^{p+2+C_p}=F^{p+2}.
\]
This is uniform in the vertex count and the number of parts.

There is an exact joint transient/period census whenever all part sizes have a common residue \(a\in\mathbb F_p\). Write \(T(x)\) for the smallest nonnegative time at which the trajectory is periodic, and \(\ell(x)\) for its eventual least period. If \(a=0\), put
\[
 \delta=r-\mathbf1_{\{r\equiv1\pmod p\}}.
\]
All eventual periods equal one, and the counts at \(T=0,1,2\) are, respectively,
\[
 1,\qquad p^{N-\delta}-1,\qquad p^N-p^{N-\delta}.
\]
In particular, two steps are necessary for some initial states.

If \(a\ne0\), let \(d=\operatorname{ord}_{\mathbb F_p^\times}(-a)\), and, when \(r\not\equiv0,1\pmod p\), also let \(e=\operatorname{ord}_{\mathbb F_p^\times}(a(r-1))\) and \(h=\operatorname{lcm}(d,e)\). Define a finite list of pairs \((k,w_k)\), with \(k\) a period and \(w_k\) a number of periodic *points*, by the following cases:
\[
\begin{array}{c|l}
\text{condition}&(k,w_k)\text{ pairs}\\\hline
r\equiv0\pmod p&(1,1),\ (d,p^{r-1}-1),\ (pd,p^r-p^{r-1})\\
r\equiv1\pmod p&(1,1),\ (d,p^{r-1}-1)\\
r\not\equiv0,1\pmod p&(1,1),\ (d,p^{r-1}-1),\ (e,p-1),\ (h,(p^{r-1}-1)(p-1))
\end{array}
\]
**Add weights when two displayed periods coincide**, obtaining \(m_k\), and put \(b=r-1\) if \(r\equiv1\pmod p\), otherwise \(b=r\). The *complete* joint distribution is
\[
\#\{x:T(x)=0,\ \ell(x)=k\}=m_k,\qquad
\#\{x:T(x)=1,\ \ell(x)=k\}=(p^{N-b}-1)m_k.
\]
All other joint counts vanish. The number of distinct primitive \(k\)-cycle orbits is \(m_k/k\), and the exact Artin--Mazur zeta function is
\[
 \zeta_F(z)=\prod_{k:m_k>0}(1-z^k)^{-m_k/k}.
\]
A least period divisible by the characteristic \(p\) occurs in the congruent-part family **if and only if** \(a\ne0\) and \(r\equiv0\pmod p\); its characteristic-divisible period is precisely \(pd\).

For example, on \(K_{1,1,1}\) over \(\mathbb F_3\), there are one fixed state, eight period-two states and eighteen period-six states. On \(K_{2,2,2}\) over \(\mathbb F_3\), there are nine fixed states and eighteen period-three states, while the other 702 configurations enter a cycle after exactly one update.

## Assumptions and scope

The graph is loopless, undirected, complete between distinct nonempty parts and empty within each part. The update is simultaneous and *excludes* the present vertex's own state. A state at time zero may already be periodic. The finite-field modulus is a prime, not a prime power, and the formulas apply to labelled configurations. The general uniform bound allows arbitrary residues of the part sizes; only the exact joint census assumes congruence of their residues. \(\operatorname{ord}\) denotes multiplicative order in \(\mathbb F_p^\times\). Orbit counts are time-orbits, not graph-isomorphism classes.

## Proof

**1. Factor the graph update.** Let \(S:\mathbb F_p^N\to\mathbb F_p^r\) take part sums, and \(E:\mathbb F_p^r\to\mathbb F_p^N\) repeat each part coordinate at every vertex in that part. The former is surjective and the latter injective. If \(J\) is the all-ones \(r\)-square matrix and \(D=\operatorname{diag}(a_1,\ldots,a_r)\), with \(a_i=n_i\pmod p\), then
\[
 F=E(J-I)S,\quad SE=D,\quad FE=EB,\quad B=(J-I)D=\mathbf1(a_1,\ldots,a_r)-D.
\]
Thus \(U=\operatorname{im}E\) is invariant and the update on it is conjugate to \(B\); the induced update on \(\mathbb F_p^N/U\) is zero.

**2. A uniform characteristic-period obstruction.** Group indices having the same part-size residue \(a\in\mathbb F_p\). Let \(s\le p\) be the number of residues actually present. For each group let \(H_a\) consist of coordinate vectors supported in that group whose coordinate sum is zero. The direct sum \(H=\bigoplus_a H_a\) is invariant under \(B\), and \(B\) acts as the scalar \(-a\) on \(H_a\). Hence \(B|_H\) is semisimple, and \(\dim(\mathbb F_p^r/H)=s\). Writing \(m_a\) for the number of parts of residue \(a\), the quotient on group sums \(X_a\) is
\[
 X'_b=m_b\sum_a aX_a-bX_b.
\]
Its dimension is \(s\). If \(s=p\), the residue-zero group is present, and the column indexed by zero is identically zero; in particular, the quotient has a zero eigenvalue. Therefore every **nonzero** eigenvalue of the quotient has algebraic degree at most \(p-1\) over \(\mathbb F_p\), and its total generalized-eigenspace dimension is at most \(p-1\). If \(s<p\), these bounds follow immediately from \(s\le p-1\). Eigenvalues on \(H\) lie in \(\mathbb F_p\).

For a nonzero eigenvalue \(\lambda\), a Jordan chain in \(B\) can exceed the corresponding maximum chain length in the quotient by **at most one**: a sufficiently high power of \(B-\lambda I\) sends the generalized eigenspace into the invariant semisimple subspace \(H\), where one further application kills it. Therefore every nonzero Jordan block of \(B\) has length at most \(p\), and every zero block has length at most \(s+1\le p+1\). Since \(F\) acts as zero on the quotient by \(U\), its nonzero Jordan blocks have the same sizes as those of \(B\), while its zero blocks have length at most \(p+2\). Every nonzero eigenvalue lies in some \(\mathbb F_{p^j}\) with \(1\le j\le p-1\), so its multiplicative order divides \(L_p\). In characteristic \(p\), a nonzero Jordan block of length at most \(p\) becomes scalar after its \(p\)-th power, because \((I+N)^p=I+N^p=I\). The invertible restriction of \(F\) therefore has order dividing \(pL_p\). The zero-primary restriction vanishes after \(p+2\) steps. This proves the global iterate identity and excludes \(p^2\)-divisible least periods.

**3. Congruent part residues: exact cycles.** If all \(a_i=a\), then \(B=a(J-I)\). If \(a=0\), \(F^2=0\), and \(\operatorname{rank}F=\operatorname{rank}(J-I)=\delta\). The kernel has \(p^{N-\delta}\) elements. Exactly one state is periodic; nonzero kernel states enter zero in one step and all remaining states in two, giving the stated counts.

Suppose \(a\ne0\). Put \(W=\{u\in\mathbb F_p^r:\sum_i u_i=0\}\). If \(r\equiv1\pmod p\), then \(\operatorname{im}(J-I)=W\), with dimension \(r-1\), and \(B|_W=-aI\), yielding \(1\) zero state and \(p^{r-1}-1\) nonzero period-\(d\) states. If \(r\equiv0\pmod p\), then \(J^2=rJ=0\), so
\[
 B^t=(-a)^t(I-tJ).
\]
Vectors of sum zero (\(p^{r-1}\) of them) have period one when zero, otherwise \(d\); each vector of nonzero sum has least period \(pd\), since return requires both \((-a)^t=1\) and \(t=0\pmod p\). Finally, if \(r\not\equiv0,1\pmod p\), the direct decomposition \(\mathbb F_p^r=W\oplus\langle\mathbf1\rangle\) has scalar eigenvalues \(-a\) and \(a(r-1)\). There are \(p^{r-1}-1\) vectors with only a nonzero \(W\)-component, \(p-1\) with only a nonzero constant component, and their product in number with both components nonzero. Their periods are \(d\), \(e\), and \(\operatorname{lcm}(d,e)\), respectively. This derives the displayed weighted lists.

**4. Joint transients and orbit numbers.** If \(a\ne0\), the image of \(F\) is exactly \(E\operatorname{im}(J-I)\), of dimension \(b\). The restriction of \(F\) to this image is bijective by the three cases in Step 3. Thus this image is precisely the periodic set. Each periodic point has \(p^{N-b}\) total preimages, exactly one of which is itself periodic. All others enter its cycle in exactly one step. Consequently the same multiplicative fibre factor applies to every eventual period, proving the joint distribution. Dividing periodic point counts by their least period counts distinct time-orbits, and the Euler-product definition gives the stated zeta function.

## Verification

Run `python verification/verify.py` using Python 3 and the standard library to enumerate all configurations in 14 labelled examples, including unequal part sizes with congruent residues. It compares exact first-periodic-entry times and least periods against every term of the joint distribution: 87,400 configurations checked. Separately run `python verification/verify_uniform.py`: this exhaustively enumerates all residual core matrices on two through five parts over \(\mathbb F_3\), and two through four parts over \(\mathbb F_5\). It checks 1,135 residue patterns and 473,295 initial core vectors against the uniform tail and period divisibility bounds. Both scripts' saved output accompanies this result. These finite checks guard formulas and indexing, while Steps 1--4 prove the general infinite families.

## Relationship to prior work

Moreno, Bollman and Aviño-Diaz (2006, full text §§2--4) establish finite-field representations and the general linear-state-diagram framework, including determination of cycles through elementary divisors. Hernández Toledo (2005) gives an earlier general Fitting-decomposition treatment of linear finite dynamical systems. These general results supply theory but do not, in the material accessible for this comparison, supply the present complete-multipartite residue-group Jordan bound or its exact joint law. Aledo, Martínez and Valverde (2015) survey parallel graph systems, not these explicit counts.

The published *Sharp period-four census for complete multipartite parity automata* treats the binary field \(\mathbb F_2\) and two XOR rules, including a zeta function and uniform small period cutoff. Its full RESULT text is a relevant established **binary** counterpart, and the present result does not re-claim the binary census. The characteristic-\(p\) absence of periods divisible by \(p^2\) for arbitrary part sizes and the residue-congruence classification for all odd primes are distinct statements. The general linear-map results are acknowledged rather than represented as newly proved principles.

## Limitations

The uniform period bound is not asserted sharp for each prime. Exact cycle and transient formulas require equal part-size residues modulo \(p\); the uniform \(p^2\) obstruction does not. The result makes no claims for prime powers, asynchronous updates, nonlinear thresholds, arbitrary graph families, or self-inclusive update rules. The full original article of Hernández Toledo (2005) was not available during the comparison, so a previously unnoticed special graph example there or in other unindexed historical material remains a specific originality risk. Finite checks alone do not establish the universal identities.

## References

1. O. Moreno, D. Bollman and M. A. Aviño-Diaz, *Finite Dynamical Systems, Linear Automata, and Finite Fields*, arXiv:math/0604534v1, first submitted 25 April 2006, especially §§2--4.
2. R. A. Hernández Toledo, *Linear Finite Dynamical Systems*, Communications in Algebra **33** (2005), 2977--2989, DOI:10.1081/AGB-200066211.
3. J. A. Aledo, S. Martínez and J. C. Valverde, *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), Article 594294, DOI:10.1155/2015/594294.
4. *Sharp period-four census for complete multipartite parity automata*, published mathematical record (11 October 2026), `2026/10/11/SCOPE-sharp-period-four-census-for-complete-multipartite-parity-automa--acea41c73be7`.
5. J. Kantic, C. Qureshi, D. Panario and F. Legl, *On the Dynamics of Linear Finite Dynamical Systems Over Galois Rings*, arXiv:2604.01548v1 (2026), especially §§2--5.
