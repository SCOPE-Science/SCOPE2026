# Sharp quartet–triple law for Nash welfare in four-role enemy-averse games

## Finding

Let four role classes have sizes \(a\ge b\ge c\ge d\ge0\), with \(n=a+b+c+d\ge2\). Agents in distinct classes are mutual friends of valuation \(+1\), and distinct agents in the same class are mutual enemies of valuation \(-n\). Consider individually rational coalition partitions, with Nash welfare the geometric mean of individual coalition utilities.

If \(a>b+c+d\), the maximum Nash welfare is \(0\). Otherwise, put
\[
 k=b+c+d-a,\qquad q_*=\min\!\left\{d,\left\lfloor\frac{k}{2}\right\rfloor\right\}.
\]
Let \(T\) be the smaller of \(k-2q_*\) and \(\lfloor(n-4q_*)/3\rfloor\), and let \(t_*\) be the largest nonnegative integer no greater than \(T\) with the same parity as \(n\). Set \(p_*=(n-3t_*-4q_*)/2\). These are nonnegative integers. The maximum Nash welfare is exactly
\[
 \boxed{\mathcal{NW}^*=(81^{q_*}8^{t_*})^{1/n}.}
\]
Every maximizing partition consists of precisely \(p_*\) pairs, \(t_*\) triples, and \(q_*\) four-person coalitions, each meeting every role class at most once; conversely every partition of that kind is optimal. Its number of labeled realizations is exactly
\[
 \boxed{\frac{a!b!c!d!}{p_*!t_*!q_*!}
 [x_1^a x_2^b x_3^c x_4^d]
 e_2(x_1,x_2,x_3,x_4)^{p_*}
 e_3(x_1,x_2,x_3,x_4)^{t_*}
 e_4(x_1,x_2,x_3,x_4)^{q_*}.}
\]
Here \(e_j\) is the degree-\(j\) elementary symmetric polynomial, and bracket notation means coefficient extraction. The coefficient can be computed by a polynomial-time dynamic program in the population \(n\). No count is asserted for the zero-optimum regime.

## Assumptions and scope

All agents are labeled, all coalitions are nonempty, and the four classes partition the agent set. A class may be empty, but the genuinely new four-role case has \(d>0\). Each person's coalition utility is the sum of valuations for their other coalition members, and only nonnegative-utility (individually rational) partitions enter the Nash objective. An individually rational coalition of size \(s\) is necessarily a transversal clique, and all its members then receive utility \(s-1\). Therefore its Nash-product factor is \((s-1)^s\); the factors for pairs, triples, and quartets are respectively \(1\), \(8\), and \(81\). A singleton contributes zero to the product. In the positive-optimum regime, the only permissible sizes are \(2,3,4\).

## Proof

**1. Characterization of realizable size spectra.** A coalition containing two members of the same role gives these agents utility at most \((s-2)-n<0\); thus every individually rational coalition is role-transversal. Conversely every transversal coalition is individually rational. A strictly positive product therefore corresponds to a partition into transversal coalitions of sizes \(2,3,4\). Let \(p,t,q\) be their counts and put \(C=p+t+q\). The size equation is
\[
 2p+3t+4q=n,\qquad C=\frac{n-t-2q}{2}.
\]
Regard the role classes as four row vertices of a bipartite incidence graph, and the \(C\) prospective coalitions as column vertices with degrees \(2\), \(3\), or \(4\). Row degrees are \((a,b,c,d)\). The Gale–Ryser inequalities for rows \(j=1,2,3,4\) become
\[
 a\le C,\qquad a+b\le2C,\qquad a+b+c\le n-q,\qquad n=n.
\]
The middle inequality is automatic when \(a\le C\), and the third is equivalent to \(q\le d\). Thus a nonnegative integer spectrum \((p,t,q)\) is realizable **if and only if**
\[
 2p+3t+4q=n,\qquad q\le d,\qquad t+2q\le k=n-2a.
\tag{1}
\]
The standard constructive proof of Gale–Ryser (or bipartite Havel–Hakimi) realizes the actual coalitions from these inequalities.

If \(a>n-a\), equation (1) is impossible and every individually rational partition includes a singleton. Conversely, if \(a\le n-a\), take \(q=0\), \(t=0\) for even \(n\) or \(t=1\) for odd \(n\), and \(p=(n-3t)/2\). Then (1) holds; this proves the positive-welfare threshold.

**2. A strict improvement whenever the quartet count is not maximal.** Every realizable spectrum obeys \(q\le d\) and \(2q\le k\), so \(q\le q_*\). Suppose \(q<q_*\), giving \(q+1\le d\) and \(C-a=(k-t-2q)/2\ge0\). If \(t\ge2\), replace the size spectrum by
\[
 (p,t,q)\longmapsto(p+1,t-2,q+1).
\]
This preserves \(C\), obeys (1), and increases the product by the strict factor \(81/64\), since two triples yield factor \(8^2=64\) while a pair and a quartet yield \(1\cdot81\).

If \(t\le1\), then \(C-a\ge1\): the integer \(k-t-2q\) is even and strictly positive because \(q<\lfloor k/2\rfloor\) and \(t\equiv k\pmod2\). We also have \(p\ge2\). Indeed, otherwise \(n=4q+3t+2p\), together with \(d\ge q+1\) and consequently \(n\ge4q+4\), forces \(p=t=1\) and \(n=4q+5\). The sorted role sizes then must be \((q+2,q+1,q+1,q+1)\), whence \(k=2q+1\), contradicting \(q<\lfloor k/2\rfloor\). We can therefore replace the spectrum by
\[
 (p,t,q)\longmapsto(p-2,t,q+1).
\]
Its number of coalitions drops by one, but \(C-1\ge a\), and (1) still holds; the product increases by \(81\). Hence no optimizer has fewer than \(q_*\) quartets. Starting from the baseline feasible spectrum above and repeatedly applying these changes proves that \(q_*\) is attainable.

**3. Optimal triples at fixed quartet count.** Set \(q=q_*\). By (1), feasibility is equivalent to
\[
 0\le t\le \min\!\left\{k-2q_*,\left\lfloor\frac{n-4q_*}{3}\right\rfloor\right\},\qquad t\equiv n\pmod2.
\]
For fixed \(q\), the product is \(81^q8^t\), strictly increasing with \(t\). Therefore the feasible largest \(t\) is exactly \(t_*\), and \(p_*= (n-3t_*-4q_*)/2\). This proves the unique optimum size spectrum and the Nash-welfare formula.

**4. Exact labeled count.** The polynomial \(e_s(x_1,x_2,x_3,x_4)\) records the choice of the \(s\) distinct role classes present in one size-\(s\) coalition. The specified coefficient in \(e_2^{p_*}e_3^{t_*}e_4^{q_*}\) counts role patterns across temporarily ordered coalition slots. For each pattern, the agents of a class of size \(r\) can be assigned to its \(r\) appearances in \(r!\) ways. Forgetting the order of slots of the same size divides by \(p_*!t_*!q_*!\). The displayed coefficient formula follows. A dynamic program tracking four exponents while multiplying at most \(n\) elementary-symmetric factors uses \(O(n^5)\) arithmetic operations, and the counts have polynomially bounded bit length.

## Verification

The standalone file `verify.py` uses only the Python standard library and exact integer arithmetic. Running `python verify.py` checks the product formula against exhaustive recursion for \(730\) ordered class-size profiles with \(n\le24\), compares the labeled counting coefficient with a separate brute-force coalition recursion for \(30\) profiles with \(n\le9\), constructs \(2000\) seeded larger feasible instances, and tests explicit exchange and boundary examples. The run succeeded on the embedded file. Finite checks corroborate the proof but do not establish it for all populations.

For example, at role sizes \((a,b,c,d)=(5,4,4,1)\), the unique optimal size spectrum is \((p_*,t_*,q_*)=(2,2,1)\). Its Nash product is \(81\cdot8^2=5184\) and there are exactly \(34560\) labeled optimal partitions. A feasible no-quartet spectrum has product \(8^4=4096\), demonstrating a genuine quartet–triple tradeoff. At \((3,3,3,3)\), the optimum is three quartets with Nash product \(81^3\) and exactly \(216\) labeled maximizers.

## Relationship to prior work

Pagano and Schlenga (arXiv:2605.19030v1, first public 18 May 2026) introduce the Nash-welfare objective in additively separable hedonic games, show general enemy-averse hardness and approximation guarantees, and establish the clique characterization of individually rational partitions. Their Section 3 gives a local example contrasting two triples with a quartet and a pair. The present statement is **not** a new clique characterization or the first observation that a quartet can beat two triples; its advance is the exact all-size formula, forced maximizing size spectrum, constructive realizability, and labeled optimum count for every complete four-role friendship graph. The source's examined treatment does not give that complete four-role classification.

Bullinger, Chatziafratis and Shahkar (arXiv:2503.06017v1) analyze **utilitarian** rather than Nash welfare and stochastic multipartite enemy-aversion models; their results do not imply the above exact deterministic Nash formula. The three-role case \(d=0\) has a separate exact treatment and is included for boundary consistency, not claimed as new. The structural content requiring four nonempty classes is the quartet cap and its interaction with the triple count.

## Limitations

The result is confined to four role classes, constant friend value \(+1\), enemy value \(-n\), complete cross-class friendship, additive utilities, individual rationality, and the geometric-mean Nash objective. It makes no claim for general graphs, asymmetrical valuations, role-dependent weights, or other welfare measures. It does not count maximizers when their optimum is zero. Earlier equivalent unindexed work remains possible; no independent scientific audit has been performed.

## References

- Marta Pagano and Alexander Schlenga, *Nash Welfare in Additively Separable Hedonic Games*, arXiv:2605.19030v1, first posted 18 May 2026. https://arxiv.org/html/2605.19030v1
- Martin Bullinger, Vaggos Chatziafratis and Parnian Shahkar, *Welfare Approximation in Additively Separable Hedonic Games*, arXiv:2503.06017v1, first posted 8 March 2025. https://arxiv.org/html/2503.06017v1
- D. Gale, *A theorem on flows in networks*, Pacific Journal of Mathematics 7 (1957); H. J. Ryser, *Combinatorial properties of matrices of zeros and ones*, Canadian Journal of Mathematics 9 (1957). (Classical bipartite incidence-sequence criterion.)
