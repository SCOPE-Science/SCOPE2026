# Exact modal-failure polynomial and uniform rare-defect law for distributed knowledge

## Finding

For each integer \(n\geq 1\) and integer \(r\geq 3\), let \(W=[n]\) be a labelled world set. Choose \(r\) independent, uniformly random equivalence relations \(E_1,\ldots,E_r\) on \(W\), and independently choose the truth set \(V(p)\subseteq W\) uniformly. Interpret the distributed-knowledge modality \(D\) using \(E=\bigcap_{i=1}^r E_i\). Define the *failure count*
\[
Y=\bigl|\{w\in W:\ w\models p\text{ and }w\not\models Dp\}\bigr|.
\]
For a positive integer \(k\), let \(B_k\) denote the Bell number, \(s(k,j)\) the **signed** Stirling number of the first kind, and
\[
T_{r,k}=\sum_{j=0}^k s(k,j)B_j^r.
\]
For an integer \(m\geq1\), set \(\Phi_m(z)=1+(1+z)^m-z^m\). Then the *complete finite probability generating polynomial* of the logical failure count is
\[
\boxed{\mathbb E[z^Y]=\frac{1}{2^n B_n^r}\sum_{\pi\in\Pi_n}T_{r,|\pi|}\prod_{C\in\pi}\Phi_{|C|}(z).}
\]
Here \(\Pi_n\) is the set of all set partitions of \(W\). The coefficient at \(z^j\) is exactly the probability of precisely \(j\) worlds falsifying \(p\to Dp\). The polynomial is finite, explicit, and valid without an asymptotic qualification.

Write \(N=\binom n2\), \(a_n=B_{n-1}/B_n\), and \(b_n=B_{n-2}/B_n\) when \(n\ge2\). Let \(F\) be the event that the frame does **not** validate \(p\to Dp\) under all valuations, and let \(L\) be the event \(Y>0\) for the sampled valuation. The following nonasymptotic bounds hold for all \(n\ge2\) and \(r\ge3\):
\[
\boxed{Na_n^r-\binom N2 b_n^r\ \leq\ \Pr(F)\ \leq\ Na_n^r,}
\]
\[
\boxed{\frac{Na_n^r}{2}-\frac14\binom N2 b_n^r\ \leq\ \Pr(L)\ \leq\ \frac{Na_n^r}{2}.}
\]
The frame has a uniquely determined exceptional two-world information cell, with all other cells singleton, conditional on \(F\) with probability tending to one **uniformly over every choice of \(r=r(n)\ge3\)**. Conditional on \(L\), asymptotically one and only one world falsifies the implication, also uniformly over \(r\ge3\). In that typical exceptional frame exactly half of all truth assignments to \(p\) detect the defect.

More quantitatively, with \(\rho_n=W_0(n)\) (the positive solution of \(\rho_n e^{\rho_n}=n\)), the relative errors in the two displayed leading terms and the conditional exceptional-shape errors are \(O(\rho_n^3/n)\), with an absolute implied constant for all integers \(r\ge3\). In particular, for each **fixed** integer \(r\ge3\),
\[
\boxed{\Pr(F)\sim\frac{\rho_n^r}{2n^{r-2}},\qquad
\Pr(L)\sim\frac{\rho_n^r}{4n^{r-2}}.}
\]
In the three-agent case the leading rates are respectively \(\rho_n^3/(2n)\) and \(\rho_n^3/(4n)\). For growing \(r\), use the exact Bell-ratio leading factors rather than substituting the fixed-\(r\) asymptotics.

## Assumptions and scope

The sampling is uniform on the \(B_n\) labelled partitions of \(W\), independently for each named agent. This differs from sampling partitions via independent random functions or by uniform block-count. The independent valuation assigns each world truth or falsity with probability one half, and is not required to be constant on information cells. The modal operator is the **ordinary, initial-history** distributed-knowledge operator; asynchronous history updates are not considered. Frame validity means truth at all worlds under every valuation. The formula \(p\to Dp\) is a single modal schema, not an assertion about every modal formula.

For \(n=1\), the displayed generating polynomial equals \(1\), and both failure probabilities vanish. For \(n\ge2\), all Bell ratios are well-defined. The asymptotic constants apply as \(n\to\infty\). The uniform assertion covers arbitrary integer-valued sequences \(r(n)\ge3\), whereas the explicit \(\rho_n^r\)-formula is stated only for fixed \(r\).

## Proof

**1. Quotient enumeration.** The meet \(E\) of the chosen equivalence relations is itself an equivalence relation. Fix a partition \(\pi\in\Pi_n\) having \(k\) blocks. Any tuple \((E_1,\ldots,E_r)\) with meet exactly \(\pi\) consists of relations coarser than \(\pi\); passing to the \(k\) quotient blocks produces \(r\) partitions whose meet is discrete. Conversely any such quotient tuple lifts uniquely. Thus the number of tuples with meet exactly \(\pi\) equals \(T_{r,k}\), independent of the sizes of the blocks. The standard partition-lattice Möbius inversion gives
\[
T_{r,k}=\sum_{\sigma\in\Pi_k}\mu(\hat0,\sigma)B_{|\sigma|}^r
=\sum_{j=0}^k s(k,j)B_j^r.
\]
The second equality follows by grouping permutations by their number of cycles: the sum of \(\prod_{C\in\sigma}(-1)^{|C|-1}(|C|-1)!\) over partitions with \(j\) blocks is \(s(k,j)\). This exact enumeration is classical and is not claimed as new.

**2. Truth-set marking.** On an \(E\)-cell \(C\) of size \(m\), suppose exactly \(t\) worlds satisfy \(p\). If \(t=m\), then \(Dp\) holds throughout \(C\) and no world fails. If \(t<m\), the modality fails throughout \(C\), so exactly \(t\) worlds falsify \(p\to Dp\). The \(2^m\) truth assignments therefore contribute
\[
2+\sum_{t=1}^{m-1}\binom mt z^t
=1+(1+z)^m-z^m=\Phi_m(z).
\]
Different cells have independent valuation choices, yielding the product of their polynomials. Summing over meet partitions and dividing by \(2^n B_n^r\) proves the generating-polynomial identity. At \(z=1\), each factor equals \(2^{|C|}\), so the coefficients sum to one.

**3. Two-event geometry.** For an unordered pair \(e=\{u,v\}\), let \(A_e\) be the event that all \(r\) agents identify the pair. A single uniformly random partition identifies the pair in exactly \(B_{n-1}\) of the \(B_n\) possibilities, by collapsing it; hence \(\Pr(A_e)=a_n^r\). For two distinct unordered pairs \(e,f\), the two equality constraints reduce the number of quotient elements by exactly two, whether the pairs intersect or not. Therefore \(\Pr(A_e\cap A_f)=b_n^r\). The frame fails \(p\to Dp\) under some valuation exactly when \(\bigcup_e A_e\) occurs: if a distinct pair lies in one cell, a valuation true only at one of those worlds falsifies the implication, while a discrete meet makes \(Dp=p\) everywhere. The first two Bonferroni inequalities give the displayed enclosure of \(\Pr(F)\).

Define \(A'_e=A_e\cap\{p(u)\ne p(v)\}\). The event \(L\) equals \(\bigcup_e A'_e\), since a nonconstant valuation on a cell makes the implication fail at some true world. A uniform binary valuation separates any given pair with probability \(1/2\), and simultaneously separates any **two distinct** pairs with probability \(1/4\), including two pairs meeting at a vertex (their two binary inequality constraints are independent). Thus \(\Pr(A'_e)=a_n^r/2\) and \(\Pr(A'_e\cap A'_f)=b_n^r/4\). Bonferroni gives the second enclosure.

**4. Uniform rare-defect estimate.** Put \(\mu=Na_n^r\) and \(\eta=\binom N2 b_n^r\). Since \(B_{n-2}<B_{n-1}\) for \(n\ge3\), for all \(r\ge3\),
\[
\frac{\eta}{\mu}=\frac{N-1}{2}\left(\frac{B_{n-2}}{B_{n-1}}\right)^r
\leq \frac{N-1}{2}\left(\frac{B_{n-2}}{B_{n-1}}\right)^3.
\]
The standard Bell-ratio asymptotics are \(B_{n-1}/B_n\sim\rho_n/n\) and \(B_{n-2}/B_{n-1}\sim\rho_n/n\). Therefore the right side is \(O(\rho_n^3/n)=o(1)\), *uniformly in the number of agents*. The two Bonferroni enclosures give the claimed uniform relative errors and, for fixed \(r\), the stated leading coefficients.

Let \(X\) count unordered pairs lying in one meet cell. If \(X\ge2\), at least two events \(A_e\) occur, so \(\Pr(X\ge2)\le\eta\). But \(\Pr(X\ge1)\ge\mu-\eta\); hence conditional on a bad frame, \(X=1\) with probability \(1-O(\rho_n^3/n)\). Exactly one coalesced pair means one doubleton cell and every other cell singleton. The analogous estimate using \(A'_e\) shows that conditional on a violation under the sampled valuation exactly one separating pair is present with probability \(1-O(\rho_n^3/n)\). On the single-doubleton event, only the unique true world of that pair falsifies \(p\to Dp\). Exchangeability makes its label uniform on \(W\). This finishes the proof.

## Verification

The accompanying standalone `checker.py` independently enumerates labelled partitions, all tuples for the listed small sizes, and all binary valuations. It compares the histogram of failing-world counts against the signed-Stirling/quotient generating polynomial, checks the two Bonferroni enclosures, and verifies the exact single-doubleton quotient count. Its runs for \((n,r)=(2,3),(3,3),(4,3),(5,3),(3,4),(4,4)\) completed with `ALL_CHECKS_OK`. For example, at \((n,r)=(3,3)\), the unnormalised polynomial is \(910+87z+3z^2\), with denominator \(1000\); at \((4,3)\), it is \(48454+5284z+258z^2+4z^3\), with denominator \(54000\). These are finite cross-checks only; the proof of the infinite claims is symbolic.

To reproduce: run `python checker.py` with a standard Python 3 interpreter. It uses only the standard library. No network or precomputed tables are needed.

## Relationship to prior work

Balbiani, van Ditmarsch, and Lerouvillois (2026) motivate distributed knowledge as an intersection of agents' indistinguishability relations, as well as subsequent resolution dynamics. This finding treats only the initial synchronous intersection operator, not their history-based asynchronous semantics.

Pittel (2000) proved exact enumeration of ordered tuples of partitions with discrete meet, established that the probability of discrete meet tends to one for every fixed \(r\ge3\), and described the large-number-of-doubletons regime for \(r=2\). Canfield (2001), Theorem 1, gave generating functions for precisely these discrete-meet counts and their complements, while Theorem 4 explicitly decomposed unrestricted tuples by meet intervals. In particular, the present quotient coefficient \(T_{r,k}\) and the general unmarked meet-enumeration principle are established results, **not** newly discovered enumerative identities. OEIS A059849 records the two-partition discrete-meet counts. The additional assertions assessed here are the full **valuation-marked modal-failure polynomial**, the sharp \(\rho_n^r/(4n^{r-2})\) rate for a failing sampled valuation, the uniform-in-\(r\) first-defect error, and the conditional one-world modal-failure shape. The result therefore complements rather than replaces Pittel's broad partition theory. It is possible that a general existing marked-partition sieve yields these formulas as an unstated corollary; historical priority is not established by a failed search.

## Limitations

The model assumes independent uniform Bell partitions, labelled worlds, and independent fair atomic valuations. The rate can change under nonuniform partition laws, correlated agents, valuations respecting agent information, or asynchronous resolution histories. The displayed fixed-\(r\) asymptotic cannot be asserted uniformly for unbounded \(r\) by replacing Bell ratios individually. For \(r=2\), the rare-defect regime fails and Pittel's different Poisson result is appropriate. No independent mathematical audit or exhaustive historical-priority certification has been conducted.

## References

1. P. Balbiani, H. van Ditmarsch, C. Lerouvillois, *Resolving Asynchronous Distributed Knowledge*, arXiv:2606.31855, publicly submitted 2026-06-30. https://arxiv.org/abs/2606.31855
2. B. Pittel, *Where the Typical Set Partitions Meet and Join*, Electronic Journal of Combinatorics **7** (2000), R5, published 2000-01-15. https://doi.org/10.37236/1483
3. Stanford Encyclopedia of Philosophy, *Epistemic Logic*, discussion of distributed knowledge as relation intersection. https://plato.stanford.edu/entries/logic-epistemic/
4. E. R. Canfield, *Meet and Join within the Lattice of Set Partitions*, Electronic Journal of Combinatorics **8** (2001), R15. https://doi.org/10.37236/1559
5. OEIS Foundation, *A059849: Number of pairs of set partitions with discrete meet*. https://oeis.org/A059849
