# Exact coexistence on star–clique epidemic overlays

## Finding

**Theorem.** Fix an integer \(m\ge 2\). Consider a deterministic, mutually exclusive two-virus SIS model on \(m+1\) vertices, with Virus 1 transmitted on the star \(K_{1,m}\) and Virus 2 on the complete graph \(K_{m+1}\). Let the strictly positive effective infection-to-recovery ratios be \(a\) and \(b\), respectively. Set

\[
r=\frac ab,\qquad R_m=\frac{m-1+\sqrt{(m-1)^2+4}}2,\qquad H_m(r)=\frac{mr^2-(m-1)r-m}{mr[1+(m-1)r-r^2]}.
\]

There exists a **strictly positive coexistence equilibrium** (both strains present at every vertex with strictly positive susceptibility) if and only if

\[
\boxed{\sqrt m<r<R_m\quad\text{and}\quad b>H_m(r).}
\]

Whenever it exists, that equilibrium is **unique**, is invariant under all permutations of the \(m\) leaves, and has the following explicit rational coordinates. Because both graphs are connected, this also classifies every equilibrium in which each virus has nonzero total population: such an equilibrium necessarily has both virus fractions positive at every vertex. Write subscripts \(C\) and \(L\) for the center and each leaf, and define susceptible fractions \(s_C\), \(s_L\):

\[
s_L=\frac{a^2-b^2}{a^2b(m-1)},\qquad
s_C=\frac{b(m-1)}{m(a^2-b^2)},\qquad
u=a s_L,\quad v=mb s_C.
\]

Then

\[
x_C=\frac{(1-s_C)-v(1-s_L)}{1-b/a},\qquad
x_L=\nu x_C,\qquad
y_L=\frac{(1-s_L)-\nu(1-s_C)}{1-b/a},\qquad
y_C=v y_L.
\]

In particular, the three-vertex instance (Virus 1 on a path of length two and Virus 2 on a triangle) can support coexistence only for the sharp ratio window \(\sqrt2<a/b<(1+\sqrt5)/2\), with the additional sharp strength bound \(b>H_2(a/b)\).

## Assumptions and scope

Vertices are indexed by \(0,1,\ldots,m\), with vertex \(0\) the star center. The two layer adjacencies \(A\) and \(B\) are the simple, unweighted adjacency matrices of \(K_{1,m}\) and \(K_{m+1}\), with **no self-loops**. For \(i=0,\ldots,m\), \(x_i\) and \(y_i\) are the respective virus fractions and \(s_i=1-x_i-y_i\) is the susceptible fraction. The continuous-time dynamics are

\[
\dot x_i=\delta_1[-x_i+a s_i(Ax)_i],\qquad
\dot y_i=\delta_2[-y_i+b s_i(By)_i],
\]

where \(a=\beta_1/\delta_1>0\), \(b=\beta_2/\delta_2>0\), and recovery rates \(\delta_1,\delta_2>0\). Only equilibria are studied, so the two recovery scales do not enter the formulas. The admissible state space is \(x_i\ge0\), \(y_i\ge0\), \(x_i+y_i\le1\). “Strictly positive coexistence” requires \(x_i>0\), \(y_i>0\), and \(s_i>0\) for every vertex. The theorem does not classify boundary equilibria or convergence basins.

## Proof

**1. Interior positivity and a symmetry reduction without assuming leaf symmetry.** At any equilibrium, \(s_i=0\) would force \(x_i=y_i=0\) by both stationary equations, contradicting \(s_i=1-x_i-y_i=0\). Thus all susceptibles are strictly positive. If one virus has positive population at any vertex, its stationary equation and connectivity of its infection graph propagate strict positivity to every vertex. Hence any equilibrium with both total virus populations positive is automatically strictly positive at every vertex. We may now assume \(x_i,y_i,s_i>0\) without additional restrictions. Put \(Y=\sum_{j=0}^m y_j>0\). For every leaf \(i\), the first stationary equation gives \(x_i=a s_i x_0\); the second, because Virus 2 uses a clique with no self-edge, gives

\[
y_i=b s_i(Y-y_i),\qquad\text{hence}\qquad y_i=\frac{bY s_i}{1+b s_i}.
\]

Therefore every leaf susceptible value \(s_i\) satisfies

\[
1=s_i+a x_0s_i+\frac{bY s_i}{1+b s_i}.
\]

The right side is strictly increasing on nonnegative \(s_i\), with derivative \(1+a x_0+bY/(1+b s_i)^2>0\). It follows that all leaves share the same \(s_L,x_L,y_L\); write center values \(s_C,x_C,y_C\). This proves leaf symmetry for **every** positive equilibrium, including any equilibrium not initially supposed symmetric.

**2. Necessary susceptibility coordinates.** The four stationary equations become

\[
x_L=a s_Lx_C,\quad x_C=ma s_Cx_L,\quad
y_L=b s_L[(m-1)y_L+y_C],\quad y_C=mb s_Cy_L.
\]

Since all infected fractions are positive, the first pair implies \(s_Ls_C=1/(ma^2)\). The second pair gives

\[
1=b(m-1)s_L+mb^2s_Ls_C=b(m-1)s_L+\frac{b^2}{a^2}.
\]

Consequently \(s_L=(a^2-b^2)/(a^2b(m-1))\), forcing \(a>b\), and \(s_C=b(m-1)/(m(a^2-b^2))\). Set \(u=a s_L\) and \(v=mb s_C\). The susceptible identities now read

\[
\begin{pmatrix}1&v\\u&1\end{pmatrix}
\begin{pmatrix}x_C\\y_L\end{pmatrix}=
\begin{pmatrix}1-s_C\\1-s_L\end{pmatrix}.
\]

Because \(uv=mab s_Ls_C=b/a<1\), this linear system is nonsingular, and inversion gives the displayed coordinates, including \(x_L=u x_C\) and \(y_C=v y_L\). Thus no more than one strictly positive coexistence equilibrium exists.

**3. Sharp existence conditions.** Write \(r=a/b>1\), \(F=1+(m-1)r-r^2\), and \(Q=mr^2-(m-1)r-m\). Direct simplification gives

\[
x_C=\frac{(r^2-m)(bmr^2+1)}{bmr(r-1)^2(r+1)},\qquad
y_L=\frac{bmrF-Q}{bmr(m-1)(r-1)}.
\]

Therefore \(x_C>0\) is equivalent to \(r>\sqrt m\). For \(r>\sqrt m\) one has \(Q>0\): at \(r=\sqrt m\), \(Q=(m-1)(m-\sqrt m)>0\), and \(Q' =2mr-(m-1)>0\) thereafter. Hence \(y_L>0\) forces \(F>0\) and \(b>Q/(mrF)=H_m(r)\). The inequality \(F>0\), given \(r>1\), is equivalent to \(r<R_m\). These conditions are necessary.

They are also sufficient: throughout \(\sqrt m<r<R_m\), let \(D=(r^2-m)(mr^2-1)>0\). Algebra yields

\[
H_m(r)-\frac{r^2-1}{r^2(m-1)}=\frac{D}{mr^2(m-1)F}>0,
\]

\[
H_m(r)-\frac{m-1}{m(r^2-1)}=\frac{D}{mr(r^2-1)F}>0.
\]

The two subtracted bounds are precisely the thresholds for \(s_L<1\) and \(s_C<1\), respectively. Thus \(b>H_m(r)\) implies \(0<s_L,s_C<1\). The displayed formulas give \(x_C>0\), \(y_L>0\), hence \(x_L>0\), \(y_C>0\). The linear susceptibility identities ensure \(x_C+y_C=1-s_C\) and \(x_L+y_L=1-s_L\), so all state constraints hold strictly. Substitution into the four stationary equations proves existence. Uniqueness was already established in step 2.

**4. Boundaries.** Equality in any of the three strict conditions cannot produce a strictly positive coexistence state: \(r=\sqrt m\) forces \(x_C=0\), \(r=R_m\) forces \(F=0\) and makes \(y_L\le0\), and \(b=H_m(r)\) forces \(y_L=0\). The theorem concerns open positive-coexistence parameter regions; no claim about boundary equilibria is needed.

## Verification

The standalone reproducibility program `verify.py` symbolically confirms the inversion, the two susceptibility bounds, and all four *original* stationary equations, without using numerical root fitting. It then evaluates \(25,872\) exact-rational parameter instances across \(m=2,\ldots,12\) and compares positivity of the candidate coordinates with the sharp inequalities, confirming zero original-system residual for every instance. Of these, \(2,208\) lie in the positive coexistence region. Run `python verify.py` with Python 3 and SymPy.

For independent hand checks, at \(m=3\), \(a=2\), \(b=1\) the formula yields

\[
(s_L,s_C,x_C,x_L,y_L,y_C)=\left(\frac38,\frac29,\frac{13}{18},\frac{13}{24},\frac1{12},\frac1{18}\right),
\]

and at \(m=2\), \(a=3\), \(b=2\) it yields \((5/18,1/5,2/3,5/9,1/6,2/15)\). Both satisfy every original equilibrium equation exactly. The infinite theorem follows from the proof, not finite checking.

## Relationship to prior work

The 2014 Sahneh–Scoglio paper establishes general competition/survival thresholds on arbitrary overlaid layers, and the 2021 Doshi–Mallick–Eun paper establishes broad qualitative global convergence and coexistence criteria. Their general existence criteria can, in principle, be specialized to this topology; the existence *of a coexistence region itself* is not claimed as new. The 2022 Doshi–Hu–Eun work derives quantitative upper bounds for general graphs, and explicitly lists star/line topologies as directions for future quantitative analysis. The present theorem goes beyond general bounds by solving **each infection coordinate exactly**, eliminating the implicit network equilibrium, and making the entire positive-equilibrium parameter region elementary and sharp on one natural infinite family of overlaid graphs.

The 2019 Liu–Paré–Nedić–Tang–Beck–Başar analysis discusses star, clique, and other structures in same-layer computational examples, rather than the star-versus-clique exact solution. The 2022/2023 Anderson–Ye work studies general equilibrium counts and stability and does not give these star–clique coordinates. Earlier work may still contain an equivalent under different notation; this is a residual bibliographic risk, not evidence of mathematical independence.

## Limitations

This is an **equilibrium**, not a full-dynamics, theorem: stability, attraction basins, finite-population stochastic extinction, and transient time scales have not been established here. Results do not transfer without proof to two arbitrary graphs, directed layers, unequal vertexwise rates, or graph modifications. The theorem's uniqueness quantifier is for strictly positive coexistence states, not all boundary or healthy equilibria. The symbolic and finite-rational checks are supporting evidence; exact analytic derivation supplies the universal proof. Originality comparisons depend on accessible literature and do not imply uniqueness in all unpublished work.

## References

1. V. Doshi, J. Hu, D. Y. Eun, *Bi-SIS Epidemics on Graphs—Quantitative Analysis of Coexistence Equilibria*, arXiv:2209.07304 (first public 2022-09-15), https://arxiv.org/abs/2209.07304.
2. V. Doshi, S. Mallick, D. Y. Eun, *Competing Epidemics on Graphs—Global Convergence and Coexistence*, arXiv:2104.10872 (2021), https://arxiv.org/abs/2104.10872.
3. F. D. Sahneh and C. Scoglio, *Competitive epidemic spreading over arbitrary multilayer networks*, Physical Review E **89**, 062817 (2014), https://doi.org/10.1103/PhysRevE.89.062817.
4. J. Liu, P. E. Paré, A. Nedić, C. Y. Tang, C. L. Beck, T. Başar, *Analysis and Control of a Continuous-Time Bi-Virus Model*, arXiv:1901.00765 (2019), https://arxiv.org/abs/1901.00765.
5. B. D. O. Anderson and M. Ye, *Equilibria analysis of a networked bivirus epidemic model using Poincaré–Hopf and Manifold Theory*, arXiv:2210.11044 (2022), https://arxiv.org/abs/2210.11044.
