# Sharp rare-event law for Minkowski decomposability of Bernoulli Boolean polytopes

## Finding
Fix a retention probability \(p\in(0,1)\), set \(q=1-p\), and independently keep each vertex of \(\{0,1\}^n\) with probability \(p\). Write \(V_n\) for the resulting set, \(P_n=\operatorname{conv}(V_n)\) when nonempty, \(F_n=\{\dim P_n=n\}\), and \(D_n\) for nontrivial Minkowski decomposability of \(P_n\). The principal assertion is the **sharp prefactor and exponent**
\[
\Pr(D_n\mid F_n)
=n\bigl(p^2+(1-p)^2\bigr)^{2^{n-1}}
\bigl(1+O_p(e^{-c_p2^n})\bigr)
\qquad(n\to\infty),
\]
where some \(c_p>0\) exists for every fixed \(p\in(0,1)\). The same expression applies to \(\Pr(D_n\cap F_n)\).

Conditionally on \(D_n\cap F_n\), with probability tending to one the **unique prime Minkowski decomposition** consists of exactly one one-dimensional unit segment in a coordinate direction and one indecomposable full-dimensional Boolean polytope on the other \(n-1\) coordinates. In particular, the dominant mechanism is a complete equality between the two opposite vertex-retention slices along precisely one coordinate.

For the explicit event \(E_i\) that the retained indicators match across every cube edge in coordinate \(i\), let \(b=p^2+q^2\). There is also the exact finite-dimensional identity
\[
\Pr\Bigl(\bigcup_{i=1}^n E_i\Bigr)
=\sum_{j=1}^{n}(-1)^{j+1}\binom nj
\bigl(p^{2^j}+q^{2^j}\bigr)^{2^{n-j}}.
\]
This identity concerns the coordinate-prism event, not the whole decomposability event at finite \(n\).

## Assumptions and scope
The limit takes integer \(n\to\infty\) with **fixed** \(p\in(0,1)\); the implicit constants may depend on \(p\). Conditioning on full affine dimension avoids ambiguity from lower-dimensional sampled polytopes. A proper Minkowski decomposition means \(P=Q+R\) where neither summand is a positive homothetic copy of \(P\). Empty samples do not satisfy \(F_n\). The claim is not uniform as \(p\) approaches either endpoint or varies with \(n\).

Every sampled binary vertex is actually a vertex of the convex hull: its signed-coordinate linear functional, positive on its ones and negative on its zeros, uniquely maximizes there among cube vertices. Hence the sampled set coincides with the exact vertex set of \(P_n\). We invoke the deterministic Cartesian-product theorem of Higashitani–Padrol–Sanyal for Boolean polytopes: a full-dimensional decomposable Boolean polytope has a coordinate-split Cartesian product decomposition into nontrivial Boolean polytopes. The original theorem, not a newly claimed result, supplies this reduction.

## Proof
Write \(N=2^n\). For each coordinate \(i\), let \(X_v\) be the independent Bernoulli retention indicators and define
\[
E_i=\{X_v=X_{v\oplus e_i}\text{ for every }v\in\{0,1\}^n\}.
\]
The \(N/2\) unordered pairs across coordinate \(i\) are disjoint. Both indicators in a pair agree with probability \(b=p^2+q^2\). Consequently
\[
\Pr(E_i)=b^{N/2}.
\]
For two distinct coordinates, the cube splits into \(N/4\) four-vertex faces, and agreement in both coordinates forces all four indicators on each face to match. With \(c=p^4+q^4\),
\[
\Pr(E_i\cap E_j)=c^{N/4},\qquad c<b^2.
\]
Bonferroni therefore gives
\[
n b^{N/2}-\binom n2c^{N/4}
\leq \Pr(\cup_iE_i)\leq n b^{N/2}.
\]
More generally, for any specified \(j\) distinct directions, the indicators must be constant on each of the \(2^{n-j}\) subcubes of order \(2^j\), giving the exact inclusion–exclusion formula in the finding.

It remains to show that products with no singleton coordinate factor are exponentially less probable. Choose a coordinate split \(I\sqcup J=[n]\) with \(k=|I|\), \(2\leq k\leq\lfloor n/2\rfloor\), and set \(M=2^k\). If \(V_n=A\times B\) is full-dimensional, then \(A\subseteq\{0,1\}^I\) has at least two elements. Fix any nonempty \(A\) of size \(a\geq2\). For each of the \(N/M\) independent \(J\)-columns, the retained pattern must equal either the empty set or exactly \(A\). Its probability is
\[
f_M(a)=q^M+p^aq^{M-a}.
\]
For \(p\geq q\), monotonicity of the finite \(\ell^r\)-norm implies
\[
f_M(a)\leq p^M+q^M
\leq(p^4+q^4)^{M/4}.
\]
For \(p<q\), since \(a\geq2\),
\[
f_M(a)\leq q^{M-2}(p^2+q^2)
\leq\bigl(q^2(p^2+q^2)\bigr)^{M/4}.
\]
The last inequality holds for every power of two \(M\geq4\), because \(q^2<b\). Define
\[
\rho_p=\begin{cases}
(p^4+q^4)^{1/4},&p\geq q,\\
(q^2b)^{1/4},&p<q.
\end{cases}
\]
Both cases give \(\rho_p<\sqrt b\). The independence of columns and the at most \(2^M\) choices of \(A\) bound the probability for this split by \(2^M\rho_p^N\). Summing over all splits with smaller side at least two gives
\[
\Pr(\exists\text{ such a product split})
\leq 2^n2^{2^{n/2}}\rho_p^N
=o\bigl(b^{N/2}e^{-\eta_pN}\bigr)
\]
for some \(\eta_p>0\) small enough, since \(n+2^{n/2}=o(2^n)\).

To control full dimensionality, consider any independent Bernoulli-\(r\) subset of the vertices of a \(d\)-cube, with fixed \(r\in(0,1)\). A proper affine hyperplane contains at most \(2^{d-1}\) cube vertices: fix all coordinates except one with nonzero normal coefficient. Every affinely deficient selected subset lies in a hyperplane spanned by \(d\) cube vertices. There are at most \(2^{d^2}\) ordered tuples determining such hyperplanes, so
\[
\Pr(\text{not full dimensional})
\leq 2^{d^2}(1-r)^{2^{d-1}}.
\]
Unconditionally take \(d=n\), \(r=p\); this establishes \(\Pr(F_n)=1-o(1)\). Conditional on \(E_i\), the \(N/2\) matching pairs collapse to independent indicators of retention probability \(r=p^2/b\). Their support is a random subset of an \((n-1)\)-cube, and \(P_n\) is a unit segment times its convex hull. Thus \(\Pr(F_n\mid E_i)=1-O_p(e^{-\gamma_pN})\) for some \(\gamma_p>0\).

The deterministic Boolean-polytope decomposition theorem says that on \(F_n\), any nontrivial Minkowski decomposition yields a split \(V_n=A\times B\) along two nonempty coordinate groups. A one-coordinate group must contribute both binary endpoints (full dimension), hence yields some \(E_i\). Every remaining split is in the exponentially negligible group just bounded. Combining this observation with Bonferroni, the conditional dimension estimate, and \(\Pr(F_n)=1-o(1)\) proves the stated sharp law with exponential relative error.

Finally, the relative probability of two distinct singleton factors is at most \(\binom n2c^{N/4}/(nb^{N/2})\to0\), and the relative probability of any other product split is exponentially small. If exactly one singleton factor occurs and the other factor decomposed, then the full polytope would possess either a second singleton factor or a non-singleton split. Thus its other factor is indecomposable with conditional probability tending to one, proving the prime-factor assertion.

## Verification
The accompanying standard-library script `verify.py` checks the strict rate gaps at five rational retention probabilities for all tested block sizes from four to 128. It also exhaustively enumerates all retained vertex sets in dimensions three and four, computes exact affine ranks, and independently compares the coordinate-product and coordinate-prism events. For dimension four, the number of full-dimensional subsets is 60879, of which 625 are Cartesian products and 577 possess a coordinate-prism factor; the remaining 48 exhibit a non-prism product split. These finite calculations confirm that the non-prism error is real at small dimensions and must be bounded rather than suppressed. They do not establish the infinite-dimensional limit, which follows from the preceding inequalities.

Run the standalone script using Python 3: `python verify.py`. No third-party packages or external files are required.

## Relationship to prior work
Higashitani, Padrol, and Sanyal (arXiv:2605.22594, first posted May 21, 2026) prove unique coordinate Cartesian decomposition for Boolean polytopes; their deterministic theorem is the geometric premise, not part of the priority claim. Ferber, Krivelevich, Sales, and Samotij (arXiv:2509.09831, first posted September 11, 2025) study edge expansion under the same random vertex-retention model. Guo and Tomon (arXiv:2604.09520, first posted April 10, 2026) sharpen that random-polytope expansion analysis. The present theorem concerns the exact rare-event probability and conditional decomposition mechanism, neither the deterministic existence of prime factors nor graph expansion. Searches for equivalent random Boolean-function conjunction factorization and Cartesian-product enumeration did not locate a source deriving this full-dimensional geometric law. The possibility of older results under Boolean-function terminology remains a priority risk.

## Limitations
Only fixed \(p\in(0,1)\) is covered; sparse, density-dependent regimes are not characterized. The conclusion is asymptotic and provides no exact finite-\(n\) formula for the entire decomposability event. The exact alternating sum applies only to the union of coordinate-prism events. The proof depends on the cited deterministic Boolean-polytope product theorem, whose relevant statement and coordinate proof were inspected. Neither independent specialist audit nor exhaustive bibliographic priority certification has been performed.

## References
- Akihiro Higashitani, Arnau Padrol, Raman Sanyal, *Indecomposability of 0/1-polytopes*, arXiv:2605.22594 (2026), https://arxiv.org/abs/2605.22594.
- He Guo, István Tomon, *Random 0/1-polytopes expand rapidly*, arXiv:2604.09520 (2026), https://arxiv.org/abs/2604.09520.
- Asaf Ferber, Michael Krivelevich, Marcelo Sales, Wojciech Samotij, *On the edge expansion of random polytopes*, arXiv:2509.09831 (2025), https://arxiv.org/abs/2509.09831.
