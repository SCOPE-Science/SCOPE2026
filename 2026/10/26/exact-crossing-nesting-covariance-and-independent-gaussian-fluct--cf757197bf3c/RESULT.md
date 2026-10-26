# Exact crossing–nesting covariance and independent Gaussian fluctuations in uniform random matchings

## Finding

Let \(M_n\) be uniformly distributed over the \((2n-1)!!\) perfect matchings on \(\{1,\dots,2n\}\), for an integer \(n\ge2\). Among unordered pairs of distinct edges, let \(C_n\), \(N_n\), and \(A_n\) count crossing, nesting, and alignment configurations, respectively. Their common mean is \(m_n=n(n-1)/6\). The exact covariance matrix is

\[
\operatorname{Cov}(C_n,N_n,A_n)=\frac{n(n-1)}{90}
\begin{pmatrix}
2(n+3)&-5&-(2n+1)\\
-5&2(n+3)&-(2n+1)\\
-(2n+1)&-(2n+1)&2(2n+1)
\end{pmatrix}.
\]

Consequently the numbers of crossings and nestings are negatively correlated at every finite size, with the exact Pearson correlation

\[
\operatorname{Corr}(C_n,N_n)=-\frac5{2(n+3)}.
\]

The principal distributional conclusion is their *asymptotic independence*: as \(n\to\infty\),

\[
\frac1{n^{3/2}}(C_n-m_n,N_n-m_n,A_n-m_n)
\xrightarrow{d}(Z_C,Z_N,-Z_C-Z_N),
\quad Z_C,Z_N\ \text{independent }N(0,1/45).
\]

The explicit finite covariance and its simplification are derived evaluations of an already studied joint generating distribution; the asymptotic independence and its structural explanation by orthogonal first projections constitute the additional result established here.

## Assumptions and scope

A matching is a partition of the ordered endpoint set \(\{1,\ldots,2n\}\) into \(n\) two-element blocks, with all perfect matchings equally likely. For four endpoints \(a<b<c<d\), the edge pair \(\{(a,c),(b,d)\}\) is a *crossing*, \(\{(a,d),(b,c)\}\) is a *nesting*, and \(\{(a,b),(c,d)\}\) is an *alignment*. Every unordered pair of distinct edges has exactly one of these types, hence \(C_n+N_n+A_n=\binom n2\) deterministically. All assertions concern that uniform model. The stated central limit theorem is for the joint law as the number of chords \(n\) tends to infinity.

## Proof

**Independent-chord representation.** Let \(X_i=(U_i,V_i)\), for \(1\le i\le n\), have mutually independent uniform \([0,1]\) coordinates, independent over \(i\). Sort their \(2n\) coordinates and pair the two ranks originating from the same index. Every matching on the ranks has exactly \(2^n n!\) equally likely originating coordinate assignments, so its law is uniform. Let \(h_C(X_i,X_j)\) and \(h_N(X_i,X_j)\) denote the crossing and nesting indicators. These are bounded symmetric order-two kernels, each with expectation \(1/3\), because three pairings of four distinct coordinates are equiprobable.

**Conditional expectations.** Condition on the first chord with sorted coordinates \(0<u<v<1\), and put \(\ell=v-u\). The second chord crosses it precisely if one of its endpoints is in \((u,v)\) and the other is outside. It nests with it precisely if both second endpoints lie inside \((u,v)\), or if one lies before \(u\) and the other after \(v\). Therefore

\[
f_C(u,v)=2\ell(1-\ell),\qquad
f_N(u,v)=\ell^2+2u(1-v).
\]

Define the centered first projections \(g_C=f_C-1/3\) and \(g_N=f_N-1/3\). The sorted first chord has density \(2\) on \(0<u<v<1\). Direct integration of the displayed polynomials gives

\[
2\int_0^1\int_u^1 f_C(u,v)\,dv\,du
=2\int_0^1\int_u^1 f_N(u,v)\,dv\,du=\frac13,
\]
\[
2\int_0^1\int_u^1
\begin{pmatrix}g_C^2&g_Cg_N\\g_Cg_N&g_N^2\end{pmatrix}
\,dv\,du
=\frac1{45}\begin{pmatrix}1&0\\0&1\end{pmatrix}.
\]

Thus the two first projections are *orthogonal* and each has variance \(1/45\).

**Exact second moments.** For \(J\in\{C,N\}\), define

\[
r_J(x,y)=h_J(x,y)-\frac13-g_J(x)-g_J(y).
\]

By conditional centering, \(\mathbb E[r_J(X_1,X_2)\mid X_1]=0\) and likewise conditioning on \(X_2\). Because crossing and nesting are mutually exclusive for the same edge pair, \(\operatorname{Cov}(h_C,h_N)=-1/9\); either indicator alone has variance \(2/9\). Orthogonality of Hoeffding components therefore gives

\[
\begin{pmatrix}
\operatorname{Var}(r_C)&\operatorname{Cov}(r_C,r_N)\\
\operatorname{Cov}(r_N,r_C)&\operatorname{Var}(r_N)
\end{pmatrix}
=\begin{pmatrix}8/45&-1/9\\-1/9&8/45\end{pmatrix}.
\]

For each \(J\), the exact order-two Hoeffding decomposition is

\[
J_n-m_n=(n-1)\sum_{i=1}^n g_J(X_i)
+\sum_{1\le i<j\le n}r_J(X_i,X_j).
\]

The projected and canonical sums are orthogonal; terms from distinct unordered pairs in the canonical sum are also orthogonal (including pairs sharing one index). Hence

\[
\operatorname{Var}(C_n)=\operatorname{Var}(N_n)
=\frac{n(n-1)^2}{45}+\binom n2\frac8{45}
=\frac{n(n-1)(n+3)}{45},
\]
\[
\operatorname{Cov}(C_n,N_n)
=(n-1)^2n\cdot0+\binom n2\left(-\frac19\right)
=-\frac{n(n-1)}{18}.
\]

Because \(A_n=\binom n2-C_n-N_n\), its covariances and variance follow by bilinearity; the resulting matrix is precisely the one stated above. Dividing the mixed covariance by the common marginal variance proves the correlation formula.

**Joint limit.** Let \(R_n\) denote the bivariate canonical remainder in the displayed decompositions. The exact variance formula gives \(\mathbb E\|R_n\|^2=8n(n-1)/45=O(n^2)\). Therefore \(n^{-3/2}R_n\to0\) in \(L^2\). The leading term, after division by \(n^{3/2}\), differs by a factor tending to one from the normalized sum \(n^{-1/2}\sum_i(g_C(X_i),g_N(X_i))\). The summands are i.i.d., bounded, centered, and have covariance matrix \(I_2/45\). The ordinary multivariate i.i.d. central limit theorem gives independent normal coordinates with the stated variance. Slutsky's theorem yields the bivariate limit, and the deterministic identity for \(A_n\) yields the trivariate limit. This proves the result for all claimed parameters, without extrapolating finite enumerations.

## Verification

The accompanying `check.py` independently enumerates all uniform matchings for every \(2\le n\le7\), compares every entry of the exact \(3\times3\) covariance matrix as a rational number, and verifies all classification and mean identities. It separately uses exact symbolic polynomial integration to verify the two conditional expectations, projection variances, projection orthogonality, and the canonical second-order kernel covariance. The complete delivered program passes 146,683 individually counted exact assertions plus all seven symbolic checks (the latter included in the total). Execute with `python check.py` in a Python environment with SymPy installed. The asymptotic limit is justified by the analytic proof above, not the enumeration.

## Relationship to prior work

Kasraoui and Zeng (2006, Proposition 3.8) provide a continued fraction for the full bivariate crossing–nesting generating polynomial, while Klazar (2005) establishes its interchange symmetry. Therefore finite mixed moments are *in principle extractable from that stronger generating function*; the explicit covariance entries are reported here as transparent derived evaluations, not claimed to supersede those earlier distributional formulas. Khare, Lorentz, and Yan (2017) also provide general machinery for matching-statistic moments and record marginal second moments. Féray (2018) and Paguyo (2021), followed by Arenas-Velilla, Arizmendi, and Paguyo (2023), establish central limit theorems for the single crossing-count statistic. The latter work is the dated motivating source for this joint-fluctuation question. None of the inspected cited results states the nondegenerate bivariate limit with *independent* crossing and nesting Gaussian coordinates or identifies the orthogonality of their first projections. General iid U-statistic central limit theory is a standard methodological ingredient and is not claimed as novel.

A different family of papers studying maximal crossing and maximal nesting *sizes* uses different statistics and different fluctuation scales; those maximal-size results cannot be substituted for the total pair-count result here.

## Limitations

The result is specific to uniform fixed-size perfect matchings. It does not assert independence at finite \(n\), where the correlation is strictly negative, nor independent fluctuations for arbitrary nonuniform matchings, general set partitions, or maximal crossing/nesting sizes. The third Gaussian coordinate is a deterministic negative sum of the first two, so the trivariate limit is necessarily singular. The already-known full joint generating function could permit another derivation of the finite covariance or the limit; historical priority of the explicit joint limit is not independently established.

## References

1. S. Arenas-Velilla, O. Arizmendi, and J. E. Paguyo, *Central limit theorem for crossings in randomly embedded graphs*, arXiv:2308.11570 (first public version 2023-08-22), https://arxiv.org/abs/2308.11570.
2. J. E. Paguyo, *Convergence rates of limit theorems in random chord diagrams*, arXiv:2104.01134, https://arxiv.org/abs/2104.01134.
3. A. Kasraoui and J. Zeng, *Distribution of crossings, nestings and alignments of two edges in matchings and partitions*, arXiv:math/0601081, https://arxiv.org/abs/math/0601081.
4. M. Klazar, *On identities concerning the numbers of crossings and nestings of two edges in matchings*, 2005, https://iti.mff.cuni.cz/series/2005/251.pdf.
5. N. Khare, R. Lorentz, and C. H. Yan, *Moments of matching statistics*, Journal of Combinatorics **8** (2017), 1–27.
6. V. Féray, *Weighted dependency graphs*, arXiv:1605.03836, https://arxiv.org/abs/1605.03836.
7. W. Y. C. Chen, E. Y. P. Deng, R. R. X. Du, R. P. Stanley, and C. H. Yan, *Crossings and nestings of matchings and partitions*, arXiv:math/0501230, https://arxiv.org/abs/math/0501230.
