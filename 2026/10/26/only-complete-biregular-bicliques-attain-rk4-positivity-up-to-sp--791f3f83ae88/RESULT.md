# Only complete biregular bicliques attain RK4 positivity up to spectral stability

## Finding

Let \(G\) be a finite, connected, simple, unweighted biregular bipartite graph. If its two vertex classes have degrees \(a\geq1\) and \(b\geq1\), set \(s=a+b\), let \(L\) be the combinatorial Laplacian, and define the completed classical fourth-order Runge--Kutta diffusion step
\[
T(h)=R_4(-hL),\qquad R_4(z)=\sum_{j=0}^{4}\frac{z^j}{j!},\qquad h\geq0.
\]
Let \(\rho\) be the unique positive root of \(24-12z+4z^2-z^3=0\), approximately \(2.78529356340528\).

**Theorem (sharp complete-versus-incomplete dichotomy).** For every such graph,
\[
T(h)\geq0\text{ entrywise}\quad\Longleftrightarrow\quad
\begin{cases}
0\leq h\leq\rho/s,&G\text{ is complete bipartite},\\
0\leq h\leq2/s,&G\text{ is not complete bipartite}.
\end{cases}
\]
In every case the exact Euclidean spectral-stability interval is
\[
\|T(h)\|_{2\to2}\leq1\quad\Longleftrightarrow\quad0\leq h\leq\rho/s.
\]
Hence the spectral-stability-to-positivity timestep ratio equals \(1\) on complete bipartite graphs and the **same universal value \(\rho/2>1\)** on every connected incomplete biregular bipartite graph. Beyond the stated positivity cutoff, negative transition entries persist for every larger positive timestep: positivity never returns.

## Assumptions and scope

A biregular bipartite graph has a fixed bipartition \(U\sqcup V\), no loops or parallel edges, all vertices in \(U\) of degree \(a\), and all vertices in \(V\) of degree \(b\). The graph is assumed finite, nonempty, and connected; the degrees and edge weights are exactly as specified. The endpoint matrix \(T(h)\) acts on arbitrary initially nonnegative vertex values. Entrywise nonnegativity, not stagewise Runge--Kutta nonnegativity, is the criterion. The complete case includes stars and the single-edge graph.

## Proof

**1. Exact block identities.** Write \(B\) for the \(|U|\)-by-\(|V|\) zero--one bipartite incidence block. Thus \(B\mathbf1=a\mathbf1\), \(B^{\mathsf T}\mathbf1=b\mathbf1\), and
\[
L=\begin{pmatrix}aI&-B\\-B^{\mathsf T}&bI\end{pmatrix}.
\]
Direct multiplication gives the left--right blocks
\[
\begin{aligned}
(L)_{UV}&=-B,\\
(L^2)_{UV}&=-sB,\\
(L^3)_{UV}&=-(a^2+ab+b^2)B-BB^{\mathsf T}B,\\
(L^4)_{UV}&=-(a^3+a^2b+ab^2+b^3)B-2sBB^{\mathsf T}B.
\end{aligned}
\]
Consequently
\[
T(h)_{UV}=hF_{a,b}(h)B+\frac{h^3}{6}\left(1-\frac{sh}{2}\right)BB^{\mathsf T}B,
\]
where
\[
F_{a,b}(h)=1-\frac{sh}{2}+\frac{a^2+ab+b^2}{6}h^2-\frac{a^3+a^2b+ab^2+b^3}{24}h^3.
\]
For distinct vertices in \(U\), the entry equals
\[
\frac{h^2}{24}\left[12-4(2a+b)h+(3a^2+2ab+b^2)h^2\right](BB^{\mathsf T})_{uv}
+\frac{h^4}{24}((BB^{\mathsf T})^2)_{uv}.
\]
The corresponding \(V\)-class identity exchanges \(a\) with \(b\) and \(BB^{\mathsf T}\) with \(B^{\mathsf T}B\).

**2. Signs and the universal lower interval.** Every entry of \(B\), \(BB^{\mathsf T}B\), \(BB^{\mathsf T}\), and their relevant powers is nonnegative. The quadratic in brackets has discriminant
\[
-16(5a^2+2ab+2b^2)<0
\]
and strictly positive leading coefficient, so every same-class off-diagonal transition is nonnegative for all \(h\geq0\).

For the cross-class edge coefficient, set \(t=sh/2\) and \(\eta=ab/s^2\), where \(0<\eta\leq1/4\). The exact identity
\[
F_{a,b}(h)=1-t+\frac{t^2}{3}+\frac{(1-2\eta)t^2(1-t)}{3}
\]
shows that \(F_{a,b}(h)>0\) whenever \(0\leq t\leq1\). The three-walk coefficient is nonnegative on the same interval. Thus all off-diagonal entries are nonnegative for \(0\leq h\leq2/s\).

Diagonal entries are strictly positive for **all** \(h\geq0\): since \(L\) is symmetric and positive semidefinite, its spectral expansion evaluates \(R_4(-h\lambda)\) at nonnegative eigenvalues; the exact identity
\[
24R_4(-x)=(x^2-2x+2)^2+4((x-2)^2+1)>0\qquad(x\geq0)
\]
proves the required strict positivity.

**3. A sharp negative witness in every incomplete graph.** If \(G\) is not complete bipartite, connectivity and a shortest path between a nonadjacent opposite-class pair produce opposite-class vertices \(u,v\) at graph distance exactly three. Thus \(B_{uv}=0\) but \((BB^{\mathsf T}B)_{uv}\geq1\). The cross-class identity gives
\[
T(h)_{uv}=\frac{h^3}{6}\left(1-\frac{sh}{2}\right)(BB^{\mathsf T}B)_{uv}<0
\quad\text{for every }h>2/s.
\]
Therefore \(2/s\) is the exact cutoff, and there is no later positivity window.

**4. Complete bipartite exception.** If \(G\) is complete bipartite, \(BB^{\mathsf T}B=abB\). Substitution simplifies **every** cross-class entry to
\[
T(h)_{uv}=\frac{h}{24}[24-12sh+4s^2h^2-s^3h^3].
\]
The cubic \(Q(z)=24-12z+4z^2-z^3\) has \(Q'(z)=-12+8z-3z^2<0\) everywhere, so it has one positive root \(\rho\), positive entries before it, zero at it, and negative entries thereafter. Step 2 handles all remaining entries, proving the complete-case cutoff.

**5. Sharp spectral interval.** For every edge \(uv\) with \(u\in U\), \(v\in V\),
\[
(x_u-x_v)^2\leq s\left(\frac{x_u^2}{a}+\frac{x_v^2}{b}\right),
\]
with nonnegative difference equal to \((\sqrt{b/a}\,x_u+\sqrt{a/b}\,x_v)^2\). Summing over edges yields \(x^{\mathsf T}Lx\leq s\|x\|_2^2\). Equality is achieved by the vector taking value \(a\) on \(U\) and \(-b\) on \(V\), so \(\lambda_{\max}(L)=s\). For \(0\leq z\leq\rho\), the positive real scalar polynomial \(R_4(-z)\leq1\), because \(R_4(-z)-1=-zQ(z)/24\). For \(z>\rho\) it is greater than one. Since the spectrum of \(L\) lies in \([0,s]\) and contains \(s\), exactly \(0\leq h\leq\rho/s\) is Euclidean nonexpansive. All statements follow.

## Verification

The standalone `verify.py` requires `sympy` as specified in `requirements.txt` and can be run with `python verify.py` in the extracted package directory. It calculates full rational Laplacian powers directly for connected complete, cycle, crown, incidence and circulant bipartite examples; compares all cross-class and same-class polynomial formulas with exact matrix entries; tests both sides of incomplete-graph cutoffs; and checks a rational enclosure \(11/4<\rho<14/5\) on complete bipartite cases. Symbolic identities independently check the positive-coefficient and discriminant certificates. These finite tests corroborate the algebra; the all-graph proof is Steps 1--5 above.

## Relationship to prior work

Classical strong-stability-preserving theory studies positivity and monotonicity certificates uniform over classes of initial-value problems. In particular, Horváth (1998, Theorem 5 and Example 1) determines that classical RK4 has zero **method-wide** positivity/absolute-monotonicity radius; Horváth (2005, Theorems 4 and 17) gives general positivity thresholds and smaller invariant-cone alternatives. Neither theorem asserts a zero threshold on each fixed graph Laplacian: the graph-specific endpoint requirement here is weaker and its positive sharp cutoff must be determined separately. Hadjimichael and collaborators (2012, Sections 1--2) study SSP coefficients and effective-order construction rather than fixed graph families.

Previously recorded graph-specific special cases include complete multipartite graphs, crown graphs, maximum-degree-two graphs and edge-subdivided regular graphs. Their relevant results follow as proper restrictions of the theorem above; **those special cases are not claimed as new**. The new conclusion is the complete structural characterization for every connected unweighted biregular bipartite network, including irregular biregular incidence networks, together with the exact universal gap between positivity and spectral stability. No covering result was found in the inspected literature, but that observation does not constitute a completeness proof of the literature search.

## Limitations

The result does not treat weighted, directed, disconnected or non-biregular networks, nor positivity at internal RK4 stages. At equality a graph can retain zero entries for distant vertex pairs; the theorem asserts entrywise nonnegativity rather than strict positivity. A literature-search residual risk remains: a specialized graph-diffusion source not located or indexed in the inspected records could cover the same characterization. The verification code is finite corroboration, not an exhaustive graph census or an independent audit.

## References

1. Z. Horváth, “Positivity of Runge--Kutta and diagonally split Runge--Kutta methods,” *Applied Numerical Mathematics* 28 (1998), 309--326, DOI: 10.1016/S0168-9274(98)00050-6.
2. Z. Horváth, “On the positivity step size threshold of Runge--Kutta methods,” *Applied Numerical Mathematics* 53 (2005), 341--356, DOI: 10.1016/j.apnum.2004.08.026. First available online 27 October 2004.
3. Y. Hadjimichael, C. B. Macdonald, D. I. Ketcheson and J. H. Verner, “Strong stability preserving explicit Runge--Kutta methods of maximal effective order,” arXiv:1207.2902, initial public posting 12 July 2012.
