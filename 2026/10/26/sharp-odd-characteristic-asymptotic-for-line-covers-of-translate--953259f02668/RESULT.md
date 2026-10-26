# Sharp odd-characteristic asymptotic for line covers of translated-conic unions

## Finding
Fix an integer \(\ell\ge2\). For every odd prime power \(q\) and pairwise distinct constants \(c_1,\ldots,c_\ell\in\mathbb F_q\), let \(C\subset\mathbb P^2_{\mathbb F_q}\) be the reduced union of the smooth conics
\[
C_i:\quad YZ=X^2+c_iZ^2\qquad(1\le i\le\ell).
\]
Let \(\operatorname{cov}(C)\) be the minimum number of \(\mathbb F_q\)-projective lines covering all \(\mathbb F_q\)-points of \(C\). **For every** \(\varepsilon>0\), **there exists** \(Q(\ell,\varepsilon)\) such that for every odd prime power \(q\ge Q(\ell,\varepsilon)\) and *every* choice of the distinct constants,
\[
\frac q2\le\operatorname{cov}(C)\le\left(\frac12+\varepsilon\right)q.
\]
Thus \(\operatorname{cov}(C)/q\to1/2\) as \(q\to\infty\) through odd prime powers, uniformly in the distinct translates for fixed \(\ell\). The assertion is asymptotic: it does not give exact finite-field cover numbers or a numerical effective threshold.

## Assumptions and scope
The ground field has odd characteristic. The component number \(\ell\) is fixed independently of \(q\). A line may contain points of multiple components and the singular common point \(P_\infty=[0:1:0]\). Each \(C_i\) has exactly the \(q\) affine points \((a,a^2+c_i)\) and \(P_\infty\). Because the \(c_i\) are distinct, their affine point sets are disjoint; therefore \(C(\mathbb F_q)\) has exactly \(\ell q+1\) elements.

## Proof
**1. Lower bound.** Every projective line meets a component conic in at most two distinct geometric points unless the line is a component (impossible since the components are nonsingular conics). Thus every line contains at most \(2\ell\) points of \(C(\mathbb F_q)\). Covering \(\ell q+1\) points requires at least \(\lceil(\ell q+1)/(2\ell)\rceil\) lines, hence at least \(q/2\).

**2. A uniform full-secant degree estimate.** Put \(m=\ell-1\). Call a rational line *full* if it meets each component in precisely two distinct rational affine points. Fix a vertex \(P=(a,a^2+c_i)\) on the affine part of \(C_i\). Every candidate full line through \(P\) is nonvertical and has equation \(y=ux+b\), with \(b=a^2+c_i-ua\). Set \(t=u-2a\). On component \(C_j\) the intersection equation is quadratic, with discriminant
\[
\Delta_j(t)=t^2+4(c_i-c_j).
\]
In odd characteristic the line is full if and only if \(t\ne0\) and each of the \(m\) values \(\Delta_j(t)\), for \(j\ne i\), is a nonzero square. Let \(\chi\) be the quadratic character with \(\chi(0)=0\). The \(m\) offsets \(4(c_i-c_j)\), \(j\ne i\), are nonzero and pairwise different. Accordingly, for any nonempty subset \(S\) of these indices, the polynomial
\[
F_S(t)=\prod_{j\in S}\bigl(t^2+4(c_i-c_j)\bigr)
\]
is squarefree of degree \(2|S|\) over the algebraic closure: each factor has two simple roots, and distinct factors have disjoint root sets. The classical Weil quadratic-character bound therefore gives
\[
\left|\sum_{t\in\mathbb F_q}\chi(F_S(t))\right|\le(2|S|-1)\sqrt q.
\]
Outside at most \(2m\) roots of the discriminants, the indicator of all \(m\) nonzero-square conditions equals
\[
2^{-m}\prod_{j\ne i}(1+\chi(\Delta_j(t))).
\]
Removing those exceptional values and the possible tangent value \(t=0\) changes the resulting character-expanded sum by at most \(2m+1\). Summing over all nonempty subsets and using the binomial identity \(2^{-m}\sum_{s=1}^{m}\binom ms(2s-1)=m-1+2^{-m}\), the number \(d(P)\) of full lines through \(P\) obeys the completely uniform estimate
\[
\left|d(P)-\frac{q}{2^m}\right|\le\left(m-1+2^{-m}\right)\sqrt q+2m+1.
\]
This argument applies identically to every component, every affine point, and every choice of pairwise distinct constants.

**3. Nearly regular hypergraph.** Define \(H\) to have the \(n=\ell q\) affine rational points as vertices. Its edges are the sets of \(2\ell\) vertices lying on a full line. A full line determines exactly one edge, and every edge has cardinality \(r=2\ell\). By Step 2 all degrees satisfy \(d(P)=D+O_\ell(\sqrt q)\), where \(D=q/2^{\ell-1}\); for all sufficiently large \(q\), these degrees are positive and satisfy the near-regularity and \(d(P)<2D\) hypotheses of the Pippenger–Spencer hypergraph covering theorem with parameters \(r=2\ell\) and \(k=2\). Two distinct affine points determine one projective line, hence their edge codegree is at most \(1\), whereas \(D\to\infty\). Thus the theorem's codegree hypothesis also holds, uniformly in the constants.

For any prescribed \(\alpha>0\), that theorem supplies a cover of all \(\ell q\) affine vertices by at most
\[
(1+\alpha)\frac{\ell q}{2\ell}=\frac{(1+\alpha)q}{2}
\]
full lines, once \(q\) is large enough in terms of \(\ell,\alpha\). Add one vertical rational line to cover \(P_\infty\). It follows that
\[
\operatorname{cov}(C)\le\frac{(1+\alpha)q}{2}+1.
\]
Take \(\alpha=\varepsilon\) and additionally \(q\ge2/\varepsilon\). This gives the asserted \((1/2+\varepsilon)q\) bound. All threshold choices depend only on \(\ell\) and \(\varepsilon\), which proves the uniform quantifiers.

## Verification
The self-contained `verify_degrees.py` enumerates nonvertical slopes and their exact affine intersections for sample prime fields, checking the discriminant characterization and the explicit character-sum degree bound point-by-point. Running it returns `FULL_SECANT_DEGREES_OK`. This finite test validates the local algebra in examples only; the assertion for all sufficiently large odd prime powers follows from the stated Weil bound and the hypergraph covering theorem. Neither theorem is replaced by finite enumeration.

## Relationship to prior work
Asgarli, Dassarma, Ghioca, MacLean, and Stokdyk (2026), Remark 1.4, introduce this *same reducible family* to demonstrate failure of their degree-dependent asymptotic bound for irreducible curves; they establish the counting lower bound but not an asymptotic upper bound for these unions. Their Theorem 1.2 excludes reducible curves, and their Theorem 3.1 quotes the Pippenger–Spencer covering theorem, which is used here with a different, explicitly character-sum-controlled hypergraph. The missing component of the analysis is the uniform simultaneous splitting count for quadratic intersections across every distinct translate, proved in Step 2. General hypergraph covering results alone do not furnish the geometric degree estimate, and prior lower bounds or small-field covering computations do not entail the uniform odd-characteristic asymptotic upper bound.

## Limitations
The proof is existential and does not provide an algorithm to find a minimum line cover. No explicit numerical value of \(Q(\ell,\varepsilon)\) follows without quantitative constants for the hypergraph theorem. The parameter \(\ell\) must be fixed, rather than growing arbitrarily with \(q\). The claim is restricted to odd characteristic; it makes no assertion about characteristic two. It does not determine lower-order terms or exact minimal covers, and it does not imply the \(q/(2\ell)\) asymptotic that fails for these reducible curves. Possible unindexed equivalent finite-geometric covering arguments remain a bibliographic priority risk.

## References
1. S. Asgarli, S. Dassarma, D. Ghioca, S. MacLean, E. Stokdyk, *Covering plane curves over finite fields with lines*, arXiv:2610.13042v1 (9 October 2026), especially Remark 1.4 and Section 3, https://arxiv.org/html/2610.13042v1.
2. N. Pippenger and J. Spencer, *Asymptotic behavior of the chromatic index for hypergraphs*, Journal of Combinatorial Theory, Series A 51 (1989), 24–42; covering consequence as reproduced in reference 1, Theorem 3.1.
3. N. Alon and J. H. Spencer, *The Probabilistic Method*, 4th ed., Theorem 4.7.1 (covering form quoted in reference 1).
4. Classical Weil bound for multiplicative-character sums of squarefree polynomials, used here for quadratic characters.
