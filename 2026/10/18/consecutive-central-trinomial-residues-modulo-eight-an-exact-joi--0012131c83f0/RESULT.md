# Consecutive central trinomial residues modulo eight: an exact joint law and sharp dyadic discrepancy

## Finding
Let \(T_n=[z^0](z^{-1}+1+z)^n\) for every integer \(n\geq0\). For any odd residues \(a,b\in\{1,3,5,7\}\), put
\[
D_{a,b}(N)=\#\{0\leq n<N:T_n\equiv a\pmod8,\ T_{n+1}\equiv b\pmod8\}.
\]
Then, simultaneously for all sixteen pairs,
\[
D_{a,b}(N)=\begin{cases}N/12+O(\sqrt N),&a\equiv b\pmod4,\\N/24+O(\sqrt N),&a\not\equiv b\pmod4.\end{cases}
\]
The constants are absolute. Thus all sixteen consecutive pairs occur with positive natural density; individual residues each have density \(1/4\), but equality modulo four between neighbors has limiting probability \(2/3\). The exponent \(1/2\) cannot be improved uniformly: for every integer \(m\geq1\),
\[
\#\{0\leq n<2^{8m}:T_n\equiv1\pmod8\}=2^{8m-2}+2^{4m-1}.
\]
Consequently, at least one of the four joint classes with first coordinate \(1\) has discrepancy of order \(\sqrt N\) along an infinite sequence.

## Assumptions and scope
The definitions use the integer constant term of a Laurent polynomial; \(T_0=T_1=1\). All counting ranges begin at \(n=0\), and \(N\) ranges over positive integers. No assumption of periodicity of the sequence or independence of neighboring residues is made. The statement concerns precisely modulus eight, not all prime powers.

## Proof
**Binary recurrences.** Put \(P=z^{-1}+1+z\); then \(P^2=P(z^2)+2P\). Expanding \(P^{2n}\) and \(P^{2n+1}\) by this identity, terms containing three factors \(2P\) vanish modulo eight. Constant-term extraction gives, for \(n\geq1\),
\[
T_{2n}\equiv T_n+2n^2T_{n-1}\pmod8,\qquad
T_{2n+1}\equiv(2n+1)T_n+2n(n+1)T_{n-1}\pmod8.
\]
The case \(n=0\) is immediate. These identities show inductively that every \(T_n\) is odd. Modulo four, \(T_{2j}\equiv T_{2j+1}\equiv T_j\), so whenever \(n\) is odd, \(T_{n-1}\equiv T_n\pmod4\). Since \(2n(n+1)\) is divisible by four and \(T_{n-1}\) is odd, the displayed congruences simplify for all \(n\geq0\) to
\[
T_{2n}\equiv f(p,T_n),\quad T_{2n+1}\equiv g(p,T_n)\pmod8,
\]
where \(p=n\bmod2\), \(f(0,x)=x\), \(f(1,x)=3x\), \(g(0,x)=x\), and \(g(1,x)=-x\), all reduced modulo eight.

**Pair-state system.** Set \(s_n=(n\bmod2,T_n\bmod8,T_{n+1}\bmod8)\). Appending a binary digit \(d\in\{0,1\}\) to the right of the representation of \(n\) sends a state \((p,a,b)\) to
\[
F_0(p,a,b)=(0,f(p,a),g(p,a)),\qquad
F_1(p,a,b)=(1,g(p,a),f(1-p,b)).
\]
The initial state is \((0,1,1)\). The reachable set \(S\) has exactly 24 elements: eight states with \(p=0\), odd \(a,b\), and \(a\equiv b\pmod4\), together with all sixteen states with \(p=1\) and odd \(a,b\). Direct use of these explicit transitions proves closure, reachability, and mutual communication; all 24 paths can also be checked by `VERIFY.py`.

Index \(S\) in lexicographic order, and let \(A\) be its integer transition matrix, where \(A_{t,s}\) is the number of bits carrying \(s\) to \(t\). The column sums are two. Define \(w_s=3\) for \(p=0\), \(w_s=1\) for \(p=1\) and \(a\equiv b\pmod4\), and \(w_s=2\) for the remaining \(p=1\) states. Checking the 48 explicitly specified transitions gives
\[
\sum_{s\in S}w_s=48,\qquad Aw=2w.
\]
A second exact calculation, reproducible from the fully specified transitions, gives the **matrix identity**
\[
A^3(A-I)(A+I)(A-2I)(A^2-2I)(A^2-2A+2I)=0.
\]
Every root of the annihilating polynomial except two has modulus at most \(\sqrt2\); the root two is simple and its eigenprojection is \(w\mathbf 1^\mathsf T/48\), since the reachable directed graph is strongly connected. The nonzero roots of the annihilator are simple. Hence, for each starting state \(s\),
\[
A^j e_s=2^j w/48+O((\sqrt2)^j)
\]
coordinatewise, uniformly in \(s\), with only a harmless fixed adjustment for \(j<3\). A dyadically aligned integer block of length \(2^j\) is represented by one starting state followed by all \(j\)-bit suffixes. Decomposing \([0,N)\) into at most one aligned block of each dyadic length and summing the errors proves the asserted \(O(\sqrt N)\) asymptotic. Summing \(w_s/48\) over states whose final coordinates are \((a,b)\) yields \((3+1)/48=1/12\) for congruent residues modulo four and \(2/48=1/24\) otherwise.

**Sharpness.** Let \(e\) be the coordinate vector at \((0,1,1)\), and let \(L\) sum coordinates for which the second state coordinate is \(1\). The number of such \(n\) below \(2^j\) is \(LA^j e\). From the annihilator, the eigenvalues of \(A^8\) on the surviving space after the first iteration are \(256,16,1\); its zero eigenpart has already vanished. Therefore \(c_m=LA^{8m}e\), for \(m\ge1\), satisfies the third-order recurrence with characteristic polynomial \((X-256)(X-16)(X-1)\). Exact computation by the transitions gives \(c_1=72,c_2=16512,c_3=4196352\). The unique solution is \(c_m=256^m/4+16^m/2\), which is the displayed identity. Since the marginal discrepancy is the sum of four joint discrepancies, the dyadic \(\sqrt N\) scale is attained by at least one joint class infinitely often.

## Verification
Run `python3 VERIFY.py` with only Python's standard library. The checker reconstructs \(T_n\) via the exact recurrence \((n+1)T_{n+1}=(2n+1)T_n+3nT_{n-1}\), checks 4096 binary-state instances, enumerates the 24-state reachable automaton, verifies strong connectivity, stationary weights, all sixteen joint densities, the integer matrix annihilator, and the three sharpness anchors. Expected terminal line starts `VERIFY_OK`. The infinite assertions follow from the displayed finite matrix identity and the proof, rather than extrapolation of sampled data.

## Relationship to prior work
Z.-W. Sun, *Congruences involving generalized central trinomial coefficients* (arXiv:1008.3887, first posted August 23, 2010) studies generalized central trinomial congruences, not neighbor-pair densities. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions* (arXiv:1310.8635, first posted October 31, 2013), Section 4.2, develop automata for central trinomial coefficients modulo four and general automaticity machinery. C. Krattenthaler and T. W. Müller, *Motzkin numbers and related sequences modulo powers of 2* (arXiv:1608.05657, first posted August 19, 2016), Theorem 17, **already give pointwise central trinomial residues modulo eight** through binary digit statistics. Thus pointwise modulo-eight determination is established prior work, not claimed here. The stated joint natural densities, non-independent neighbor correlation, quantitative discrepancy and sharpness identity require additional transfer-matrix analysis and were not identified in the inspected results. A general automated derivation from earlier automata remains possible; novelty is asserted only for the explicit correlation and sharp asymptotics.

## Limitations
Only two adjacent terms modulo eight are treated. The explicit numerical constant in \(O(\sqrt N)\) is not optimized. The result does not imply any analogous distribution at modulus sixteen, any asymptotic independence, or independence from all earlier number-theoretic literature. A stronger unlocated theorem on binary-automatic cylinder frequencies could cover the claim; independent literature review remains necessary.

## References
1. Z.-W. Sun, *Congruences involving generalized central trinomial coefficients*, arXiv:1008.3887 (2010), https://arxiv.org/abs/1008.3887.
2. E. Rowland and R. Yassawi, *Automatic congruences for diagonals of rational functions*, arXiv:1310.8635 (2013), https://arxiv.org/html/1310.8635v2, Section 4.2.
3. C. Krattenthaler and T. W. Müller, *Motzkin numbers and related sequences modulo powers of 2*, arXiv:1608.05657 (2016), https://arxiv.org/html/1608.05657v3, Theorem 17.
