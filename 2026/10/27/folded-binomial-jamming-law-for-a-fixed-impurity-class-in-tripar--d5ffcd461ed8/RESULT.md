# Folded-binomial jamming law for a fixed impurity class in tripartite dimer adsorption

## Finding
Let \(r\ge2\) be fixed. On the complete tripartite graph \(K_{n,n,r}\), initially every vertex is vacant. Each edge independently attempts irreversible dimer adsorption at equal positive Poisson rate; an attempt is accepted precisely when both endpoints are vacant. Let \(U_{n,r}\) be the number of vertices still vacant when no admissible edge remains. For a binomial random variable \(B_r\sim\operatorname{Binomial}(r,1/2)\), put \(V_r=|2B_r-r|\).

For all integers \(n\ge 2r+2\), the total-variation distance satisfies
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(U_{n,r}),\mathcal L(V_r)\bigr)
 \le \frac{r^2}{2}\left[\frac1n+\frac{n+2H_n}{(n+1)(n+2)}\right]
 +\frac{r(r+2)(r+3)}{(n+1)(n+2)},
\]
where \(H_n=\sum_{j=1}^n 1/j\). In particular, for every fixed integer \(r\ge2\),
\[
 d_{\mathrm{TV}}\bigl(\mathcal L(U_{n,r}),\mathcal L(V_r)\bigr)=O_r(n^{-1}).
\]
Consequently, for every allowed integer \(u\) with \(0\le u\le r\) and \(u\equiv r\pmod2\),
\[
 \lim_{n\to\infty}\Pr(U_{n,r}=u)
 =2^{-r}\sum_{k=0}^{r}\binom rk\mathbf1_{\{|2k-r|=u\}}.
\]
The limiting expected number of vacancies is \(r\,2^{1-r}\binom{r-1}{\lfloor(r-1)/2\rfloor}\), with finite-size error \(O_r(n^{-1})\). In particular, for \(r=2\), the probability of a perfect jammed matching tends to \(1/2\), and the probability of exactly two vacant sites also tends to \(1/2\). For \(r=3\), the limiting probabilities of one and three vacancies are \(3/4\) and \(1/4\), respectively.

## Assumptions and scope
The three vertex classes \(A,B,C\) have respective sizes \(n,n,r\). Every interclass edge is permitted and every intraclass edge forbidden. Each deposited dimer permanently occupies its two vertices and blocks subsequent overlapping dimers. All permitted edges have identical positive attempt rates, and there is no desorption. The positive rate rescales physical time and does not affect the terminal law. The asymptotic theorem holds with \(r\) fixed as \(n\to\infty\), not with an arbitrary simultaneous growth of \(r\). Total variation is \(d_{\mathrm{TV}}(P,Q)=\frac12\sum_x|P(x)-Q(x)|\).

## Proof
**Step 1: an exact count-state process.** When \(a,b,c\) vertices remain vacant in the respective classes, available edges of types \(AB,AC,BC\) number \(ab,ac,bc\). Exponential memorylessness means the next accepted edge is selected uniformly from these \(ab+ac+bc\) possibilities, whenever this number is nonzero. It removes one vertex from each of the two incident classes. This gives a finite exact Markov recurrence for the complete distribution. At terminal time at most one class can contain vacancies. Since exactly \(2n+r\) vertices were originally present, the terminal vacancy count has the same parity as \(r\) and is at most \(r\) whenever \(n\ge r\).

**Step 2: a marked-impurity survival bound.** Label the \(r\) initial vertices in \(C\), and fix one vertex \(i\). Write \(j=n-m\), where \(m\) is the number of accepted \(AB\) dimers so far. At stage \(j\), if \(x\) impurity dimers have used an \(A\)-vertex and \(y\) have used a \(B\)-vertex, then the currently vacant base-class sizes are \(a=j-x\) and \(b=j-y\), where \(x+y\le r\). Thus \(a,b\le j\) and, for \(j\ge r+1\), \(a,b>0\).

While marked vertex \(i\) remains available, the total rate of its incident edges is proportional to \(a+b\); the competing \(AB\) rate is proportional to \(ab\). Ignore for the moment the edges from other impurity vertices. The chance of an \(AB\) edge winning this two-type race is
\[
 q(a,b)=\frac{ab}{ab+a+b}\le\frac{j}{j+2}.
\]
The inequality follows because \(q\) is increasing in both nonnegative arguments and \(a,b\le j\). Allowing other impurity vertices to be matched before either competing event can only lower \(a\) or \(b\), hence can only decrease the chance that \(AB\) wins before the marked vertex is matched. Formally, writing \(p_i(a,b,c)\) for that chance when \(c\) includes the marked vertex, first-step analysis gives \[p_i(a,b,c)=\frac{ab}{W}+\frac{(c-1)a}{W}p_i(a-1,b,c-1)+\frac{(c-1)b}{W}p_i(a,b-1,c-1),\qquad W=ab+c(a+b).\] For \(c=1\), \(p_i=q\). If the smaller-\(c\) probabilities are bounded by \(q\), monotonicity gives \(p_i(a,b,c)\le [ab+(c-1)(a+b)q(a,b)]/W=q(a,b)\). This proves the needed comparison inductively even with intervening impurity edges.

Let \(J_i\) be the value of \(j\) at which marked vertex \(i\) is eventually matched, and define \(J_i=0\) if it remains unmatched. For any integer \(r+1\le k\le n\), the event \(\{J_i\le k\}\) implies that the marked vertex survives until the process has made \(n-k\) accepted \(AB\) matches. Since both base classes remain nonempty at every intervening stage \(j\ge r+1\), multiplication of the conditional race bounds gives
\[
 \Pr(J_i\le k)\le\prod_{j=k+1}^{n}\frac{j}{j+2}
 =\frac{(k+1)(k+2)}{(n+1)(n+2)}.
 \tag{1}
\]
This is a uniform finite-size estimate, not an asymptotic approximation.

**Step 3: summable orientation bias.** Whenever vertex \(i\) is matched while \(j\ge r+1\), the conditional probability that its partner is in \(A\), rather than \(B\), equals \(a/(a+b)\). Since \(|a-b|\le r\) and \(a+b\ge2j-r\),
\[
 \left|\frac{a}{a+b}-\frac12\right|
 \le\frac{r}{2(2j-r)}\le\frac{r}{2j}.
 \tag{2}
\]
Put \(\widetilde J_i=\max\{r+1,J_i\}\). From (1) and summation by parts for the decreasing function \(j\mapsto1/j\),
\[
 \begin{aligned}
 \mathbb E\frac1{\widetilde J_i}
 &=\frac1n+\sum_{k=r+1}^{n-1}\left(\frac1k-\frac1{k+1}\right)\Pr(\widetilde J_i\le k)\\
 &\le \frac1n+\frac1{(n+1)(n+2)}\sum_{k=r+1}^{n-1}\frac{k+2}{k}\\
 &\le\frac1n+\frac{n+2H_n}{(n+1)(n+2)}.
 \end{aligned}
 \tag{3}
\]
Equation (1) also bounds the probability that marked vertex \(i\) is not matched before stage \(r+1\):
\[
 \Pr(J_i\le r)\le\frac{(r+2)(r+3)}{(n+1)(n+2)}.
 \tag{4}
\]

**Step 4: coupling and identification of the terminal count.** Give the \(r\) initially labeled impurity vertices independent uniform random numbers. At the moment a particular impurity vertex is matched, use its own uniform number to choose its partner's base class with threshold \(a/(a+b)\); compare this choice with an ideal fair bit from the threshold \(1/2\). This coupling preserves the exact process because the identity of the next impurity vertex and its choice of base class can be generated separately. Conditional on a matching stage \(J_i\ge r+1\), the mismatch probability is bounded by (2). Treat \(J_i\le r\), which includes a potentially unpaired impurity vertex, as an exceptional event. A union bound over all \(r\) vertices, followed by (3) and (4), shows that all actual impurity choices agree with the independent fair bits and every impurity is matched, except on an event of probability at most
\[
 \varepsilon_{n,r}=\frac{r^2}{2}\left[\frac1n+\frac{n+2H_n}{(n+1)(n+2)}\right]
 +\frac{r(r+2)(r+3)}{(n+1)(n+2)}.
\]

On the complementary event, let \(K\) be the number of impurity vertices whose partner lies in \(A\). Once all impurity vertices have been matched, the numbers of vacant \(A\)- and \(B\)-vertices differ by \(r-2K\), because accepted \(AB\) edges have always reduced both counts equally. The remaining complete bipartite graph matches until its smaller side is exhausted; hence its terminal vacancy count is \(|r-2K|\). Under the coupled ideal choices, \(K=B_r\) is binomial with parameters \(r\) and \(1/2\). The coupling inequality yields the claimed total-variation bound. Since \(H_n=O(\log n)\), that bound is \(O_r(n^{-1})\). Finally the limiting expected absolute symmetric-binomial displacement has the stated binomial-coefficient expression, obtained by pairing adjacent binomial coefficients or the standard simple-random-walk identity. Because both vacancy counts are bounded by \(r\), the expectation error is also \(O_r(n^{-1})\). This completes the proof.

## Verification
Run `python verify_tripartite.py` with Python 3.9 or later; no third-party dependencies are needed. The program computes exact rational finite-state laws using two structurally different representations: a three-part-size Markov chain, and the full labeled-vertex bitmask process with explicit edge enumeration. It compares both representations on six finite graphs, checks parity/support and the displayed total-variation inequality on twenty additional parameter pairs, and computes larger finite examples. The program reports 117 passing assertions, with representative output at \(n=100\). All finite computations are checks of the formulas, not a substitute for the preceding proof for all \(n\).

## Relationship to prior work
Random sequential adsorption and irreversible edge exclusion are classical statistical-mechanical models. Pippenger's study of adsorption on graphs includes edge-based occupation with nearest-edge blocking and develops asymptotics in sparse or high-girth regimes, but the accessible abstract does not determine the present dense tripartite fixed-impurity vacancy distribution. Erban and Chapman analyze how RSA attempts relate to physical time in a diffusive adsorption model, rather than this terminal graph distribution. Dhara, van Leeuwaarden, and Mukherjee study vertex-activation RSA on Erdős–Rényi graphs and limiting coverage fractions, not edge-dimer deposition on a deterministic tripartite graph. Glock and collaborators study much broader random greedy hypergraph matchings in approximately regular settings but do not supply the stated fixed-class microscopic residue distribution.

A related analysis of complete tripartite adsorption in a **different scaling regime** assumes one part much larger than two linearly growing parts and derives a Poisson law for dimers joining those minority parts. Its hypotheses do not include two equally large parts and a fixed third part; its Poisson count does not determine this folded-binomial terminal vacancy distribution. These comparisons are statements of inspected scope, not claims of exhaustive historical uniqueness. The 1989 graph-adsorption paper's full text remained inaccessible, so a residual priority risk is retained.

## Limitations
The theorem assumes identical positive rates on all available interclass edges, a complete tripartite graph, fixed impurity count \(r\), and no desorption. It does not address nonuniform rates, arbitrary forbidden-edge patterns, the regime \(r\to\infty\), the distribution of the adsorption completion time, or a higher-order asymptotic expansion beyond the proved \(O_r(n^{-1})\) total-variation bound. Although a finite exact Markov recurrence is given, no closed form for the full finite-size distribution is asserted. The self-review is not an independent audit.

## References
1. N. Pippenger, *Random Sequential Adsorption on Graphs*, SIAM Journal on Discrete Mathematics 2 (1989), 393–401; DOI: 10.1137/0402034. Original publication month August 1989; publicly available abstract examined, full text not obtained.
2. R. Erban and S. J. Chapman, *What is the Time Scale of Random Sequential Adsorption?*, arXiv:physics/0611252, first public posting 2006-11-27; published in Physical Review E 75 (2007), 041116.
3. S. Dhara, J. S. H. van Leeuwaarden, and D. Mukherjee, *Generalized Random Sequential Adsorption on Erdős–Rényi Random Graphs*, arXiv:1604.03918, first public posting 2016-04-13; Journal of Statistical Physics 164 (2016), 1217–1232.
4. S. Glock, F. Joos, J. Kim, M. Kühn, and L. Lichev, *Conflict-free hypergraph matchings*, Journal of the London Mathematical Society 109 (2024), e12899; DOI: 10.1112/jlms.12899.
