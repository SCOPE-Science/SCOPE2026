# Exact \(p\)-adic closures and residue densities of arithmetic partial-derivative orbits

## Finding
For every prime \(p\) and integer \(x\), the closure in the \(p\)-adic integers of the forward orbit of the arithmetic partial derivative \(D_p\) is either finite or a finite set of isolated transient points joined to an explicitly computable, disjoint union of open-and-closed \(p\)-adic balls. In the second case its Haar measure is positive and equals the limiting density of the orbit among residue classes modulo growing powers of \(p\). Furthermore the number of attained residue classes is given by an exact formula at all sufficiently large precisions.

## Assumptions and scope
Fix a rational prime \(p\). Define \(D_p(0)=0\) and, for any nonzero integer \(x\),
\[
D_p(x)=\frac{x\nu_p(x)}p,
\]
where \(\nu_p(x)\) is the exponent of \(p\) in \(|x|\). This map sends integers to integers. Set \(x_n=D_p^n(x)\) for \(n\ge0\). Haar measure on \(\mathbb Z_p\) is normalized to give \(\mathbb Z_p\) measure one.

If \(x=0\), the orbit is \(\{0\}\). If \(x\ne0\) and \(a_0=\nu_p(x)<p\), then \(x_{a_0+1}=0\), so the closure is the finite orbit. Otherwise, the valuation recurrence
\[
a_{n+1}=f_p(a_n):=a_n-1+\nu_p(a_n)
\]
remains positive; it is eventually periodic by Emmons–Xiao [1, Theorem 8]. Let \(t\) be its *least* preperiod and \(\ell\) its *least* positive period. Put \(b_j=a_{t+j}\) and \(z_j=x_{t+j}\), for \(0\le j<\ell\), and define
\[
\Lambda=\prod_{j=0}^{\ell-1}\frac{b_j}{p}=p^{-\ell}\prod_{j=0}^{\ell-1}b_j.
\]
This product is a positive integer not divisible by \(p\), since summing the valuation recurrence around the cycle gives \(\sum_j\nu_p(b_j)=\ell\). In particular, \(x_{t+j+q\ell}=z_j\Lambda^q\) for all \(q\ge0\).

If \(\Lambda=1\), the orbit is finite, consisting of its first \(t+\ell\) terms. Otherwise, define
\[
e=\begin{cases}\operatorname{ord}_{p}(\Lambda),&p\text{ odd},\\
\operatorname{ord}_{4}(\Lambda),&p=2,
\end{cases}\qquad c=\nu_p(\Lambda^e-1).
\]
Thus \(c\ge1\) for odd \(p\), while \(c\ge2\) for \(p=2\), and \(e\) divides \(p-1\) for odd \(p\) while \(e\in\{1,2\}\) for \(p=2\).

**Exact closure theorem.** Whenever \(\Lambda>1\),
\[
\boxed{\overline{\{x_n:n\ge0\}}=\{x_0,\ldots,x_{t-1}\}\;\sqcup\;
\bigsqcup_{j=0}^{\ell-1}\bigsqcup_{r=0}^{e-1}
\bigl(z_j\Lambda^r+p^{b_j+c}\mathbb Z_p\bigr).}
\]
All displayed balls and transient points are pairwise disjoint. Accordingly,
\[
\boxed{\mu\bigl(\overline{\{x_n\}}\bigr)=e\sum_{j=0}^{\ell-1}p^{-(b_j+c)}>0.}
\]
For any integer \(N\ge\max_j(b_j+c)\) that also satisfies \(N>\max_{0\le i<t}a_i\) (the second condition is vacuous if \(t=0\)), the *exact* number \(C_N\) of residues modulo \(p^N\) hit by the orbit is
\[
\boxed{C_N=t+e\sum_{j=0}^{\ell-1}p^{N-b_j-c}.}
\]
Consequently \(\lim_{N\to\infty}C_N/p^N=\mu\bigl(\overline{\{x_n\}}\bigr)\). These statements also apply when \(x\) is negative.

## Proof
**1. Valuation and multiplier.** For \(x_n\ne0\) with positive valuation \(a_n\), the derivative is \(x_{n+1}=x_n a_n/p\), hence \(a_{n+1}=a_n-1+\nu_p(a_n)\). If \(a_0<p\), repeated steps decrease the valuation by one until valuation zero; the next derivative vanishes. If \(a_0\ge p\), positive valuations persist: \(f_p(p)=p\) and \(f_p(a)\ge p\) whenever \(a>p\). The eventual cycle is the previously established valuation-periodicity theorem [1], or equivalently it can be located by iterating \(f_p\) using that theorem as a termination guarantee. Summing \(a_{n+1}-a_n=-1+\nu_p(a_n)\) over a period gives \(\sum_j\nu_p(b_j)=\ell\). Thus \(\Lambda\in\mathbb Z_{>0}\) is a \(p\)-adic unit, and the displayed geometric subsequence identity follows by multiplying the \(\ell\) derivative multipliers.

**2. Closure of a cyclic unit group.** Suppose \(\Lambda>1\). For odd \(p\), let \(e\) be its order modulo \(p\), and for \(p=2\) its order modulo \(4\). Put \(u=\Lambda^e\) and \(c=\nu_p(u-1)\). We have \(c\ge1\) for odd \(p\), and \(c\ge2\) for \(p=2\). The standard binomial lifting argument gives
\[
\nu_p(u^{p^m}-1)=c+m\quad(m\ge0),
\]
and, more generally, \(\nu_p(u^q-1)=c+\nu_p(q)\) for all positive integers \(q\). Therefore \(u\) has precise order \(p^{N-c}\) modulo \(p^N\) whenever \(N>c\). This equals the cardinality of the principal-unit subgroup \(1+p^c\mathbb Z/p^N\mathbb Z\), so every residue in that subgroup is a power of \(u\). Passing to compatible inverse limits gives
\[
\overline{\{\Lambda^q:q\ge0\}}=\bigsqcup_{r=0}^{e-1}\Lambda^r(1+p^c\mathbb Z_p).
\]
The use of positive powers rather than all integer powers makes no difference in a compact profinite group, since all their finite reductions are cyclic groups.

**3. Pullback to the derivative orbit.** Multiplication by \(z_j=p^{b_j}v_j\), with \(v_j\) a \(p\)-adic unit, maps a principal-unit coset to the additive ball
\[
z_j\Lambda^r(1+p^c\mathbb Z_p)=z_j\Lambda^r+p^{b_j+c}\mathbb Z_p.
\]
Different \(j\) have distinct valuations \(b_j\) because \(\ell\) is the least period of the deterministic valuation recurrence; hence their balls are disjoint. For fixed \(j\), the \(e\) centers have distinct reductions modulo \(p^{b_j+c}\): distinct powers \(\Lambda^r\) are distinct modulo \(p\) for odd \(p\), or modulo \(4\) when \(p=2\) and \(e=2\). No transient valuation can equal a cycle valuation (otherwise eventual periodicity would begin earlier), and all transient valuations are mutually distinct; thus those points are outside the balls and outside each other. Taking the closure of a finite union of geometric subsequences proves the claimed decomposition.

**4. Measure and exact modular counts.** Each additive ball modulo \(p^{b_j+c}\) has normalized measure \(p^{-(b_j+c)}\). Disjointness proves the Haar-measure formula. For any \(N\ge b_j+c\), that ball has exactly \(p^{N-b_j-c}\) residues modulo \(p^N\). If additionally \(N\) strictly exceeds every transient valuation, distinct transient valuations remain distinct modulo \(p^N\) and cannot lie in the images of the balls. The \(t\) transient points therefore contribute exactly \(t\) further residue classes, proving the formula for \(C_N\) and the limiting density.

**5. Example.** For \(p=2\) and \(x=16\), valuations alternate \(4,5\). Here \(t=0\), \(\ell=2\), \(\Lambda=5\), \(e=1\), \(c=2\). The exact closure is
\[
(16+64\mathbb Z_2)\sqcup(32+128\mathbb Z_2),
\]
with Haar measure \(1/64+1/128=3/128\), and \(C_N=3\cdot2^{N-7}\) for \(N\ge7\).

## Verification
The bundled `verify.py` independently implements modular dynamics using the pair consisting of the valuation and the unit factor, and separately builds the predicted coset residues from the theorem. Executing `python3 verify.py` succeeded for 6,399 test profiles, prime parameters \(2,3,5,7\), 8,480 accumulated attained-residue instances, and 187 checked valuation cycles. The finite computation checks representative modular cases only; the general closure and Haar-measure conclusions are proved in Sections 1–4 above.

## Relationship to prior work
Emmons and Xiao [1, Theorem 8] prove the eventual periodicity and effective segment structure of integer valuation orbits; that result is a required premise here, not a new claim. Their [1, Theorem 10] concerns ordinary real divergence, vanishing and eventual fixed points. Their later study [2, Sections 2 and 5] extends partial derivatives to local fields and studies valuation dynamics and continuity. The present result instead classifies *the values of entire integer forward orbits* as subsets of \(\mathbb Z_p\): their exact topological closures, disjoint additive balls, Haar measures and modular residue counts. The unit-subgroup lifting lemma is standard; the contribution is its complete uniform application to the derivative's valuation cycles and resulting measurable orbit geometry. No claim is made that valuation periodicity or principal-unit lifting is new.

## Limitations
The classification concerns integer-starting orbits in \(\mathbb Z_p\), not all starting elements of \(\mathbb Q_p\) or extensions. The finite verifier cannot replace the proof of the infinite statement. Originality has been checked against the identified foundational papers, mathematical searches, and accessible related records; full historical exhaustiveness and independent scientific validation are not claimed. The exact modular formula requires the explicit stated lower bound on \(N\); finite orbits must be handled separately.

## References
[1] B. Emmons and X. Xiao, "The Arithmetic Partial Derivative," *Journal of Integer Sequences* **25** (2022), Article 22.4.7; first posted 2022-01-28, arXiv:2201.12453. https://arxiv.org/abs/2201.12453 ; full text: https://cs.uwaterloo.ca/journals/JIS/VOL25/Xiao/xiao3.pdf.

[2] B. Emmons and X. Xiao, "A Generalization of Arithmetic Derivative to \(p\)-adic Fields and Number Fields," arXiv:2307.04912 (first posted 2023-07-10). https://arxiv.org/abs/2307.04912.
