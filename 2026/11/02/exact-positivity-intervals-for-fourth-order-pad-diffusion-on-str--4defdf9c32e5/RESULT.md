# Exact positivity intervals for fourth-order Padé diffusion on strongly regular graphs

## Finding

Let \(G\) be a finite, connected, noncomplete, simple strongly regular graph with parameters \((v,k,\lambda,\mu)\), so \(v\ge4\), \(0<k<v-1\), \(\mu>0\), adjacent vertices have exactly \(\lambda\) common neighbors, and nonadjacent vertices have exactly \(\mu\) common neighbors. Give every edge the same conductance \(c>0\), let \(L=c(kI-A)\), and define the fourth-order diagonal Padé (two-stage Gauss–Legendre) one-step diffusion map

\[
P(h)=\left(I+\tfrac h2L+\tfrac{h^2}{12}L^2\right)^{-1}\left(I-\tfrac h2L+\tfrac{h^2}{12}L^2\right),\qquad h\ge0.
\]

Put \(S=2k-\lambda+\mu\), \(\Delta=v-S\), and \(t=ch\). The **exact set** of timesteps for which \(P(h)\) is entrywise nonnegative is

\[
\boxed{\{h\ge0:P(h)\ge0\}=\begin{cases}
[0,\infty),&\Delta\le0,\\
[0,H],&\Delta>0.
\end{cases}}
\qquad H=\frac{3}{c\Delta}\left(1+\sqrt{1+\frac{4\Delta}{3\mu}}\right)\quad(\Delta>0).
\]

For every \(h>0\), each nonadjacent off-diagonal entry is **strictly positive**; all diagonal entries are strictly positive. In the finite-horizon case, precisely the entries corresponding to graph edges become negative for \(h>H\); they vanish at \(h=H\). Therefore there are no separated positivity windows. This claim concerns only the **end-step map**, not internal Runge–Kutta stage positivity.

Explicitly, if \(q_1<q_2\) are the two positive nonzero Laplacian eigenvalues for unit conductance and \(d(z)=1+z/2+z^2/12\), then \(q_1+q_2=S\), \(q_1q_2=\mu v\), and the off-diagonal entries are

\[
\begin{aligned}
P(h)_{ij}&=\frac{t\left(1+\mu t/2-\mu\Delta t^2/12\right)}{d(tq_1)d(tq_2)}&&\text{when }i\sim j,\\
P(h)_{ij}&=\frac{\mu t^2\left(1/2+St/12\right)}{d(tq_1)d(tq_2)}&&\text{when }i\not\sim j,\ i\ne j.
\end{aligned}
\]

At the equality boundary \(\Delta=0\), the adjacent coefficient obeys \(P(h)_{ij}=72/(\mu v^2t^2)+O(t^{-3})\) as \(t\to\infty\). For \(\Delta>0\), it equals \(-12\Delta/(\mu v^2t)+O(t^{-2})\). These formulas give exact sharp time and large-step sign information, not merely asymptotic necessary conditions.

## Assumptions and scope

All statements refer to real symmetric **combinatorial** graph Laplacians, uniform edge conductance \(c>0\), the rational end-step \(P(h)\) as defined above, and finite simple connected noncomplete strongly regular graphs with \(\mu>0\). The graph may be imprimitive (e.g. a balanced complete multipartite graph); no connectivity condition on its complement is needed for the main theorem. Both nonzero eigenvalues \(q_1,q_2\) are positive and distinct because such a strongly regular graph is connected and noncomplete. Matrix inequality \(P(h)\ge0\) means entrywise nonnegativity, not merely positive semidefiniteness. Time \(h\) and conductance \(c\) are real; the sharp endpoint is included.

For a **primitive** strongly regular graph (both \(G\) and its complement connected), the elementary complement parameter identity gives \(S(\overline G)=2v-S(G)\). Consequently at least one of the two complementary diffusion problems is unconditionally positive; both are unconditionally positive when \(S=v\). These complement-side parameter statements parallel the known Moore–Penrose inverse \(M\)-property duality [3]; their graph-side classification is not claimed as new.

Three examples follow by inserting classical strongly regular parameters: (i) every conference graph, including every undirected Paley graph, has \(\Delta=0\); (ii) the triangular graph \(T_m=L(K_m)\) for \(m\ge4\) has \(\Delta=(m^2-7m+4)/2\), so unconditional Padé positivity holds for exactly \(m=4,5,6\); (iii) the square rook graph \(K_m\square K_m\) for \(m\ge3\) has \(\Delta=m(m-3)\), so it is unconditional exactly at \(m=3\). These parameter classifications for the Moore–Penrose \(M\)-property, including the triangular-graph cutoff, are already in [3]; the precise Padé temporal conclusions are obtained here. For the Petersen graph \((v,k,\lambda,\mu)=(10,3,0,1)\), one obtains the particularly simple sharp horizon \(H=(1+\sqrt5)/c\), whereas its complement (the triangular graph \(T_5\)) is unconditionally positive.

## Proof

**1. Strong-regularity algebra.** Let \(A\) be the adjacency matrix, \(J\) the all-ones matrix, and \(L_0=kI-A\). Counting common neighbors gives

\[
A^2=(k-\mu)I+(\lambda-\mu)A+\mu J.
\]

Because \(G\) is connected and \(k\)-regular, the zero eigenspace of \(L_0\) is the span of the all-ones vector. Expanding the displayed identity yields

\[
L_0^2-SL_0+\mu v\left(I-\tfrac1vJ\right)=0,
\qquad S=2k-\lambda+\mu.
\]

Thus the restriction of \(L_0\) to the orthogonal complement of constants has exactly two distinct positive eigenvalues \(q_1<q_2\), with \(q_1+q_2=S\) and \(q_1q_2=\mu v\). Positivity and distinctness follow from connected noncomplete strong regularity (the two adjacency roots are distinct, because their discriminant is \((\lambda-\mu)^2+4(k-\mu)>0\) for the nontrivial strongly regular parameters).

**2. Rational functional calculus.** Set \(t=ch\) and \(d(z)=1+z/2+z^2/12\). Since \(d(z)>0\) for real \(z\ge0\), the step is defined for every \(t\ge0\). The exact identity

\[
\frac{1-z/2+z^2/12}{1+z/2+z^2/12}=1-\frac{z}{d(z)}
\]

implies \(P(h)=I-tL_0d(tL_0)^{-1}\). Interpolate the scalar function \(x\mapsto x/d(tx)\) at \(0,q_1,q_2\); its matrix value equals \(aL_0+bL_0^2\) with

\[
b=\frac{d(tq_2)^{-1}-d(tq_1)^{-1}}{q_2-q_1},\qquad a=d(tq_1)^{-1}-q_1b.
\]

For adjacent vertices, \((L_0)_{ij}=-1\) and \((L_0^2)_{ij}=\lambda-2k\). For distinct nonadjacent vertices, \((L_0)_{ij}=0\) and \((L_0^2)_{ij}=\mu\). Hence

\[
P(h)_{ij}=t[a+b(2k-\lambda)]\quad(i\sim j),\qquad
P(h)_{ij}=-t\mu b\quad(i\not\sim j).
\]

Substitute \(2k-\lambda=S-\mu=q_1+q_2-\mu\), bring both expressions to the common positive denominator \(d(tq_1)d(tq_2)\), and simplify with \(q_1q_2=\mu v\). This gives the two rational formulas asserted under **Finding**. In particular, \(b<0\) for \(t>0\), proving strict positivity for nonedges.

**3. Exhaustive sign analysis and boundaries.** For \(t>0\), the only potentially nonpositive off-diagonal entries are edges. Their common sign is exactly the sign of

\[
F(t)=1+\frac{\mu t}{2}-\frac{\mu\Delta t^2}{12}.
\]

If \(\Delta\le0\), all terms of \(F\) are nonnegative, with constant term positive. If \(\Delta>0\), \(F\) is a concave quadratic with one negative and one positive real root (the product of roots is negative); the unique positive root is

\[
t_* = \frac{3}{\Delta}\left(1+\sqrt{1+\frac{4\Delta}{3\mu}}\right).
\]

Thus \(F(t)\ge0\) for precisely \(0\le t\le t_*\), and \(F(t)<0\) thereafter. Each matrix \(P(h)\) is symmetric and has row sums one, since \(L\mathbf1=0\). Every diagonal is strictly positive: the scalar Padé multiplier has positive numerator \(1-z/2+z^2/12=((z-3)^2+3)/12>0\) and positive denominator for \(z\ge0\), so \(P(h)\) is symmetric positive definite. This accounts for **every** matrix entry and proves the sharp interval without numerical extrapolation.

**4. Large-time and complement statements.** Use \(d(tq_1)d(tq_2)=\mu^2v^2t^4/144+O(t^3)\). Substitution proves the two stated adjacent-entry expansions. For a primitive graph, the standard complement SRG parameters imply \(S(\overline G)=2v-S(G)\), and the already-proved sign criterion applies to both connected complements. This finishes the theorem.

## Verification

The deterministic exact-rational finite-instance checker `verify_srg_pade.py` uses only Python 3's standard library. It constructs ten named strongly regular graphs or complements, independently checks the \((v,k,\lambda,\mu)\) common-neighbor definitions, computes the exact matrix rational function by rational Gaussian elimination for five positive rational timesteps, and compares every off-diagonal entry against the two stated formulas. It also checks positivity of all diagonals, row sums, and the sign polynomial.

Executing `python3 verify_srg_pade.py` yielded `VERIFY_OK 10 graph instances; 50 exact rational matrices; 8740 entry comparisons`. Verified families include the Petersen graph, Paley graphs of orders \(5\) and \(13\), triangular graphs through \(T_7\), two square rook graphs, and the complement of \(T_7\). Finite checks are **not** substitutes for the argument in **Proof**, which applies to every graph meeting the hypotheses and to the continuum of real steps.

## Relationship to prior work

The 2010 study of Zappavigna–Colaneri–Kirkland–Shorten [1] and their expanded 2012 paper [2] develop Padé positivity and sufficient timestep conditions for Metzler/Hurwitz matrices, but do not give the exact family-wide Padé sign formulas or positivity horizon above. Their general sufficient test is not a sharp characterization of this conservative graph-Laplacian setting; nonedges with \((L_0^2)_{ij}=\mu>0\) render its off-diagonal ratio test uninformative.

**Important prior coverage:** Bendito–Carmona–Encinas–Mitjana [3] already completely characterize when the Moore–Penrose inverse of the Laplacian of a strongly regular graph has nonpositive off-diagonals (their \(M\)-property). In their notation the condition is \(\mu\ge k-k^2/(v-1)\), which is **algebraically equivalent** to \(S\ge v\). They also establish the primitive complement duality, conference-graph equality, and triangular-graph cutoff. None of those graph-theoretic classifications is claimed here as new. The present finding is the **exact time-dependent Padé positivity theorem**, including strict signs for nonedges, a single sharp interval, an explicit endpoint if finite, and critical large-time decay; these dynamic conclusions require the additional rational matrix-function computation in **Proof** and are not stated in the inspected portions of [3]. The adjacency-algebra facts used in the proof are standard; see van Dam–Omidi [4].

## Limitations

The theorem is for noncomplete connected strongly regular graphs with uniform conductance, a symmetric conservative generator, and one fixed fourth-order \([2/2]\) Padé end-step. It does not cover arbitrary weighted graphs, general directed generators, other rational integrators, or intermediate internal stage values. Published work [3] covers the equivalent **static** Moore–Penrose inverse parameter condition; novelty claims are therefore restricted to the finite-step Padé dynamics and the exact horizon. Although targeted literature and research-record searches did not identify an earlier identical dynamic theorem, specialized historical coverage remains possible. Independent expert review has not been performed.

## References

1. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010, repository record and author PDF: https://mural.maynoothuniversity.ie/id/eprint/2195/ (deposited 2010-10-15).
2. A. Zappavigna, P. Colaneri, S. Kirkland, R. Shorten, *Essentially Negative News About Positive Systems*, preprint, 2012, repository PDF: https://mural.maynoothuniversity.ie/id/eprint/3761/ (deposited 2012-06-19); journal DOI: 10.1016/j.laa.2011.12.021.
3. E. Bendito, Á. Carmona, A. M. Encinas, M. Mitjana, *Distance-regular graphs having the M-property*, Linear and Multilinear Algebra **60** (2012), 225–240, DOI: 10.1080/03081087.2011.589047 (first online 2011-08-25); primary 2011 lecture material: https://mapthe.upc.edu/en/congresses/docs/congresses_2011_the-m-property-for-distance-regular-graphs.pdf.
4. E. R. van Dam, G. R. Omidi, *Strongly walk-regular graphs*, Journal of Combinatorial Theory A **120** (2013), 803–810; arXiv:1208.3067 (first posted 2012-08-15).
