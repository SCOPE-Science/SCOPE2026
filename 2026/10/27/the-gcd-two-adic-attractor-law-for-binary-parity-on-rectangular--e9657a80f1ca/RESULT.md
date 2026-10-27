# The gcd–two-adic attractor law for binary parity on rectangular tori

## Finding

Consider the nearest-neighbour parity update on the rectangular torus \(C_m\square C_n\), for every pair of integers \(m,n\ge3\). Define
\[
k=2^{\nu_2(m)},\qquad \ell=2^{\nu_2(n)},\qquad g=\gcd(m/k,n/\ell).
\]
The number of configurations lying on periodic orbits is precisely
\[
R(m,n)=2^{mn-k\ell(2g-1)}.
\]
Let \(\tau(z)\) be the least nonnegative number of updates needed for a configuration \(z\) to become periodic. Its exact maximum over all configurations is
\[
T(m,n)=\begin{cases}
\max(k,\ell),&g>1,\\
\max(1,k/2,\ell/2),&g=1.
\end{cases}
\]
For every recurrent phase \(p\), the set of initial configurations satisfying \(F^{T(m,n)}(z)=p\) has size exactly \(2^{k\ell(2g-1)}\). Thus every attractor cycle of length \(r\) has precisely \(r\cdot2^{k\ell(2g-1)}\) initial states attracted to that *cycle*.

When \(g>1\) and \(M=\max(k,\ell)>1\), the fraction of initial configurations having \(\tau(z)=M\) is exactly
\[
1-2^{-2(g-1)\min(k,\ell)}.
\]
When \(g>1\) and \(k=\ell=1\), the corresponding fraction is \(1-2^{-(2g-1)}\). If both \(m\) and \(n\) are powers of two, the all-zero state is the unique recurrent configuration and the sharp extinction time is \(\max(m,n)/2\).

## Assumptions and scope

The vertex set is \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\) with four *distinct* neighbours (guaranteed by \(m,n\ge3\)). Configurations take values in \(\mathbb F_2\); each vertex's new bit is the sum modulo two of its north, south, east and west neighbours. Updates are synchronous and have no stochastic component, memory term, or self-loop. A state is recurrent precisely if it lies on a finite periodic orbit. For a periodic state, \(\tau=0\). A basin over an entire cycle is distinguished above from the fibre of its individual periodic phases.

## Proof

**Polynomial representation.** Work first over \(\mathbb F_2\), identify the configuration space with the group algebra
\[
A=\mathbb F_2[x^{\pm1},y^{\pm1}]/(x^m-1,y^n-1).
\]
Under this identification the update is multiplication by
\[
f=x+x^{-1}+y+y^{-1}=\frac{(x+y)(1+xy)}{xy}.
\]
Its orientation relative to the chosen indexing is immaterial, because the four shifts occur in symmetric inverse pairs. Extend scalars to an algebraic closure \(K\) of \(\mathbb F_2\), which preserves all matrix ranks and nilpotency indices.

**Local decomposition and recurrent count.** Write \(m=km_0\) and \(n=\ell n_0\), where \(m_0,n_0\) are odd and \(k,\ell\) are powers of two. Characteristic two gives
\[
x^m-1=(x^{m_0}-1)^k,\qquad y^n-1=(y^{n_0}-1)^\ell.
\]
The two odd-degree root equations have distinct roots. The Chinese remainder theorem decomposes \(A\otimes K\) into \(m_0n_0\) local summands, each isomorphic to \(K[u,v]/(u^k,v^\ell)\), indexed by \(\alpha^{m_0}=1\) and \(\beta^{n_0}=1\). Multiplication by \(f\) is a unit on a summand if \(f(\alpha,\beta)\ne0\). Otherwise it acts nilpotently, because the constant term vanishes and the remaining polynomial belongs to the nilpotent maximal ideal.

The displayed factorisation of \(f\) shows that it vanishes exactly when \(\alpha=\beta\) or \(\alpha\beta=1\). Each equation has \(g=\gcd(m_0,n_0)\) solutions. Their intersection is only \((1,1)\): two simultaneous equations require \(\alpha^2=1\), whose only solution in characteristic two is \(1\). Thus exactly \(2g-1\) local summands, each of dimension \(k\ell\), are nilpotent. Every other local summand is invertible. By finite-dimensional Fitting decomposition the periodic points are precisely the stable image of the update map and have \(\mathbb F_2\)-dimension \(mn-k\ell(2g-1)\). This proves the recurrent-state count and the uniform size \(2^{k\ell(2g-1)}\) of each fibre of the stabilized update \(F^T\).

**Sharp transient index.** At \((\alpha,\beta)=(1,1)\), write \(x=1+u\), \(y=1+v\). The local expression is
\[
f=\frac{u^2}{1+u}+\frac{v^2}{1+v}.
\]
Since \(k\) and \(\ell\) are powers of two, the Frobenius identity gives the nilpotency upper bound \(T_0=\max(1,k/2,\ell/2)\). It is attained whenever \(T_0>1\): specializing one coordinate to zero leaves a power of \(u^2/(1+u)\) or \(v^2/(1+v)\) which is nonzero at exponent \(T_0-1\). If \(T_0=1\), the local zero operator itself has nilpotency index one.

At any other zero pair, necessarily \(\alpha,\beta\ne1\). The formal derivative of \(h(x)=x+x^{-1}\) is \(h'(x)=1+x^{-2}\), nonzero at \(\alpha\ne1\). Hence \(X=h(x)-h(\alpha)\) and \(Y=h(y)-h(\beta)\) are independent local coordinates with \(X^k=Y^\ell=0\). Because the constant terms sum to zero, \(f=X+Y\). Frobenius shows \(f^M=0\) for \(M=\max(k,\ell)\). This bound is attained: substituting the smaller coordinate equal to zero gives a nonzero \((M-1)\)-st power in the longer truncated coordinate. Such noncentral zero pairs exist if and only if \(g>1\). Combining these blocks proves both cases of the stated global sharp \(T(m,n)\).

**Exact proportion at maximum depth.** Suppose \(g>1\) and \(M=\max(k,\ell)>1\). Each noncentral zero block has nilpotency index \(M\), whereas the central block has smaller index. If \(k\ge\ell\), the invertible coordinate change \(W=X+Y\) identifies the block with \(K[W,Y]/(W^k,Y^\ell)\), since \(Y^k=0\). Multiplication by \(W^{k-1}\) therefore has rank \(\ell=\min(k,\ell)\). The same argument with the coordinates reversed handles \(\ell\ge k\). There are exactly \(2(g-1)\) noncentral zero blocks, giving
\[
\operatorname{rank}(F^{M-1})-\operatorname{rank}(F^M)=2(g-1)\min(k,\ell).
\]
An initial state has transient at most \(M-1\) precisely when its nilpotent component is killed by \(F^{M-1}\). Uniform counting in the nilpotent Fitting space gives the fraction \(2^{-2(g-1)\min(k,\ell)}\), proving the stated complement. If \(k=\ell=1\), every one of the \(2g-1\) zero blocks is one-dimensional and is killed in one update, so the fraction needing one update is \(1-2^{-(2g-1)}\).

Finally, when \(m=k\) and \(n=\ell\), \(g=1\) and the whole algebra is the central nilpotent summand, so the zero state alone is recurrent and the sharp extinction time is \(\max(m,n)/2\) (both dimensions are at least four under the graph-size assumption).

## Verification

The supplied `VERIFIER.py` constructs the update operator directly from graph neighbours and independently computes ranks of successive powers over \(\mathbb F_2\). It compared the predicted stable rank, sharp transient index and, where applicable, the maximum-depth rank decrement on **144 parameter pairs**, all \(3\le m,n\le14\). It enumerated every initial state for \((m,n)=(3,3),(3,4),(4,3),(4,4)\), totalling **74,240 configurations**, and checked the cardinality of the stabilized image. Independently, an exhaustive transient-depth census of all 262,144 configurations on \(C_3\square C_6\) yielded depths 0, 1 and 2 with populations 256, 16,128 and 245,760 respectively, confirming the predicted 15/16 maximum-depth proportion. `verification.log` records the completed checks. Finite computations corroborate, but do not replace, the arbitrary-size algebraic proof above. One can run `python3 VERIFIER.py` with the Python standard library.

## Relationship to prior work

Nearest-neighbour additive cellular automata and their polynomial description are classical. Martin, Odlyzko and Wolfram (1984) give a general algebraic framework for finite additive automata. Barua and Ramakrishnan (1996, §5) explicitly study the four-neighbour sigma-game on tori, including its global noninvertibility; their treatment does not give the recurrent-count, sharp depth or maximum-depth fraction stated here. Kawahara and collaborators (1992 preprint; 1995 journal article) work with the four-neighbour rule on rectangular lattices with *zero* boundary conditions rather than toroidal identification, so their quantitative statements do not directly transfer. Ekhad, Sloane and Zeilberger (2015) study odd-rule neighbourhoods on the infinite square lattice using a single seed and count occupied sites, not the full finite-torus state space. General state-transition methods in Guan and He (1986) may overlap conceptually; the exact implication of that work was not completely resolved from accessible text.

The specific assertions established here are the closed gcd/two-adic recurrent dimension, the sharp dimension-dependent nilpotent index, and the exact peak-transient proportion. This is not a claim of novelty of XOR updates, polynomial models, or uniform attraction-basin trees in general.

## Limitations

No closed formula for each individual primitive-cycle period or its multiplicity is claimed. The formula for the fraction with maximum transient is asserted in the stated cases \(g>1\); only the maximum transient and total recurrent count are asserted for \(g=1\). The graph restriction \(m,n\ge3\) is essential for the four neighbours to be distinct. General literature may contain an equivalent specialization; in particular, the full text of Guan and He (1986) was inaccessible during the comparison and remains a historical overlap risk. The calculations are an internal verification of a mathematical proof, not independent external validation.

## References

1. O. Martin, A. M. Odlyzko, and S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. DOI: 10.1007/BF01223745.
2. R. Barua and S. Ramakrishnan, *The sigma-game, sigma+-game, and two-dimensional additive cellular automata*, Theoretical Computer Science **154** (1996), 349–366. DOI: 10.1016/0304-3975(95)00091-7.
3. Y. Kawahara et al., *Period lengths of cellular automata on square lattices with rule 90*, RIFIS Technical Report 54 (March 1992); Journal of Mathematical Physics **36** (1995), 1435–1456. Repository: https://hdl.handle.net/2324/3062. DOI: 10.1063/1.531132.
4. S. B. Ekhad, N. J. A. Sloane, and D. Zeilberger, *Odd-Rule Cellular Automata on the Square Grid*, arXiv:1503.04249 (2015); author's preprint webpage dated March 12, 2015: https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/3x3.html.
5. P.-H. Guan and Y. He, *Exact results for deterministic cellular automata with additive rules*, Journal of Statistical Physics **43** (1986). DOI: 10.1007/BF01020648.
