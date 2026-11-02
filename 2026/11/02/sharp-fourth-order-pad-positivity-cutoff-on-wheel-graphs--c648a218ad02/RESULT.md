# Sharp fourth-order Padé positivity cutoff on wheel graphs

## Finding
Let \(W_m=K_1\vee C_m\), with \(m\ge3\), denote a wheel with one hub and \(m\) rim vertices. Assign the same edge conductance \(c>0\) to every spoke and rim edge. Let \(L_m\) be the corresponding symmetric Laplacian and let
\[
P_m(h)=\left(I+\frac h2L_m+\frac{h^2}{12}L_m^2\right)^{-1}
\left(I-\frac h2L_m+\frac{h^2}{12}L_m^2\right).
\]
For every \(h\ge0\), \(P_m(h)\) is symmetric, has row sums one and is positive definite. Its **entrywise nonnegativity holds for every timestep** if and only if \(3\le m\le5\). In fact, for these three values every matrix entry is strictly positive when \(h>0\). For every \(m\ge6\), the transition coefficient between adjacent rim vertices is negative for all sufficiently large \(h\).

The first failing wheel \(W_6\) (seven vertices) has an exact, contiguous positivity interval. Put \(t=ch\), and let \(\tau\) denote the **unique positive root** of
\[
230t^6-1440t^5-6921t^4-10440t^3-7668t^2-2808t-432=0.
\]
Then \(P_6(h)\) is entrywise nonnegative **exactly when** \(0\le ch\le\tau\), where \(9.82<\tau<9.84\). At \(ch=\tau\), precisely the adjacent-rim off-diagonal class first reaches zero; all other off-diagonal classes remain positive.

A quantitative obstruction for all \(m\ge6\) is the adjacent-rim asymptotic formula
\[
P_m(h)_{0,1}=-\frac{12}{ch}\left[
\frac{\rho+\rho^{m-1}}{\sqrt5(1-\rho^m)}-\frac{m+2}{(m+1)^2}
\right]+O((ch)^{-2}),\qquad \rho=\frac{3-\sqrt5}{2}.
\]
The bracket is strictly positive for every integer \(m\ge6\), with lower bound \((147\sqrt5-325)/490>0\).

## Assumptions and scope
The graph is finite, simple and undirected, with exactly one hub joined to every vertex of a simple \(m\)-cycle. The common edge conductance \(c\) is strictly positive and fixed. Timesteps range over all \(h\ge0\). At \(m=3\), the wheel is \(K_4\). Rim vertices are indexed by \(0,\ldots,m-1\), and the hub is indexed by \(m\). This theorem does not assert a positivity-interval classification for \(m\ge7\), and does not cover unequal spoke/rim conductances or directed generators.

## Proof
**1. Spectral and diagonal facts.** Scale to unit conductances by setting \(t=ch\), and write \(L\) for the unweighted wheel Laplacian. The eigenvalues are \(0\), \(m+1\), and \(3-2\cos(2\pi k/m)\) for \(1\le k<m\). This follows by decomposing into the constants, the one-dimensional hub-versus-rim mode, and the Fourier modes of mean zero on the rim. The scalar Padé multiplier is
\[
r(z)=\frac{z^2-6z+12}{z^2+6z+12}.
\]
For all real \(z\ge0\), its numerator and denominator are strictly positive, so \(P_m(h)=r(tL)\) is positive definite. Since \(r(0)=1\), it has row sums one. Every diagonal entry is therefore strictly positive. Only off-diagonal entries require a sign check.

**2. Exact finite positive cases.** By cyclic and reflection symmetries, the off-diagonal classes are hub-to-rim and rim-to-rim at distances \(1\le d\le\lfloor m/2\rfloor\). Writing \(p_{d}^{(m)}(t)\) for a rim pair at cyclic distance \(d\) and \(u^{(m)}(t)\) for a rim-to-hub entry, exact matrix inversion gives the following complete formulas:

For \(m=3\), \(u^{(3)}=p_1^{(3)}=3t/(4t^2+6t+3)\).

For \(m=4\),
\[
u^{(4)}=p_1^{(4)}=\frac{12t}{25t^2+30t+12},\qquad
p_2^{(4)}=\frac{24t^2(4t+3)}{(3t^2+6t+4)(25t^2+30t+12)}.
\]
For \(m=5\), set \(D_5=(3t^2+3t+1)(121t^4+462t^3+720t^2+504t+144)\). Then
\[
u^{(5)}=\frac{t}{3t^2+3t+1},
\]
\[
p_1^{(5)}=\frac{t(55t^4+462t^3+876t^2+576t+144)}{D_5},
\quad
p_2^{(5)}=\frac{t^2(451t^3+858t^2+576t+144)}{D_5}.
\]
Every displayed numerator and denominator is positive for \(t>0\). Therefore \(P_m(h)\) is entrywise strictly positive for all positive steps when \(m\in\{3,4,5\}\); at zero step it is the identity. These rational identities can be independently recomputed by inverting \(I+tL/2+t^2L^2/12\); the accompanying exact-arithmetic verifier performs all such checks.

**3. All larger wheels eventually fail.** In the same unit-conductance normalization, the hub-indexed block of \(L\) is \(m\), and the rim-indexed principal block is the positive-definite circulant \(B=3I-A(C_m)\), satisfying \(B\mathbf{1}=\mathbf{1}\). Resolve the wheel space into rim vectors orthogonal to \(\mathbf{1}\) and the hub-versus-rim eigenvector. The rim block of the Moore–Penrose inverse is exactly
\[
(L^+)_{\mathrm{rim},\mathrm{rim}}=B^{-1}-\frac{m+2}{(m+1)^2}\mathbf{1}\mathbf{1}^\mathsf T.
\]
Indeed, on zero-mean rim vectors \(L\) acts as \(B\); the zero-mean inverse is \(B^{-1}-\mathbf{1}\mathbf{1}^\mathsf T/m\), while the hub-versus-rim eigenprojector contributes \(\mathbf{1}\mathbf{1}^\mathsf T/[m(m+1)^2]\). Combining coefficients yields the formula.

The cyclic difference equation for \(B^{-1}\) has characteristic roots \(\rho\) and \(\rho^{-1}\), where \(\rho=(3-\sqrt5)/2\). The cyclic Green kernel at distance \(d\) is
\[
(B^{-1})_{0,d}=\frac{\rho^d+\rho^{m-d}}{\sqrt5(1-\rho^m)},\quad 0\le d<m.
\]
It follows that
\[
(L^+)_{0,1}\ge\frac{\rho}{\sqrt5}-\frac{m+2}{(m+1)^2}
\ge\frac{3\sqrt5-5}{10}-\frac8{49}
=\frac{147\sqrt5-325}{490}>0
\]
for every \(m\ge6\). The second inequality uses monotonic decrease of \((m+2)/(m+1)^2\). The strict final inequality is equivalent to \(147\sqrt5>325\), verified by squaring the positive sides. Since \(r(z)=1-12/z+O(z^{-2})\) as \(z\to\infty\), the spectral expansion on the orthogonal complement of constants gives, for distinct vertices,
\[
[r(tL)]_{ij}=-\frac{12}{t}(L^+)_{ij}+O(t^{-2}).
\]
The adjacent rim coefficient is therefore negative for all sufficiently large \(t\), proving necessity.

**4. First failing wheel: an exact horizon.** On \(W_6\), put
\[
D_6=(t^2+3t+3)(4t^2+6t+3)(25t^2+30t+12)(49t^2+42t+12).
\]
For rim distances \(1,2,3\), direct Fourier inversion (or exact matrix inversion) yields
\[
p_1^{(6)}(t)=-\frac{3t(230t^6-1440t^5-6921t^4-10440t^3-7668t^2-2808t-432)}{D_6},
\]
\[
p_2^{(6)}(t)=\frac{3t^2(1730t^5+6060t^4+9039t^3+6876t^2+2664t+432)}{D_6},
\]
\[
p_3^{(6)}(t)=\frac{18t^2(370t^5+1080t^4+1257t^3+768t^2+252t+36)}{D_6},
\]
whereas the hub-to-rim entry is \(u^{(6)}(t)=12t/(49t^2+42t+12)\). All denominators and all off-diagonal entries except \(p_1^{(6)}\) are positive for \(t>0\). The degree-six polynomial in \(p_1^{(6)}\) has exactly one sign change in descending coefficient order, is negative at \(t=0\), and tends to positive infinity. Descartes' rule of signs together with continuity gives exactly one positive root \(\tau\), and its sign changes there. Hence the complete positivity set is \(0\le t\le\tau\). Exact substitution gives a negative polynomial value at \(t=491/50=9.82\) and a positive value at \(t=246/25=9.84\), locating the root. This proves the theorem.

## Verification
The included `verify.py` uses SymPy rational arithmetic to reconstruct the unweighted Laplacians, verify every closed-form off-diagonal entry at \(m=3,4,5,6\), check the wheel pseudoinverse block identity for additional finite sizes, confirm the unique positive-root certificate for \(W_6\), and perform finite large-step consistency tests. Exact checks support algebraic formulas; the all-\(m\) assertion follows from the analytic Green-kernel bound, not from finite testing. Run with `python verify.py` in an environment containing SymPy.

## Relationship to prior work
Zappavigna, Colaneri, Kirkland and Shorten (2010, 2012) established important general facts and sufficient conditions for positivity of Padé-discretized positive systems, including failures in other Metzler settings. Their inspected positivity sections neither give an unconditional wheel classification nor an exact seven-vertex wheel timestep root. Mednykh's 2015 lecture notes record the wheel Laplacian eigenvalues used here; the spectrum alone does not settle entrywise positivity of its rational matrix function. Closely related published investigations concern other geometries (uniform paths and cycles) or directed Markov generators. They do not directly imply the wheel claim because adding the hub changes the generator, spectral projectors and matrix-function entries.

## Limitations
The conclusion requires all edge conductances to be identical, including spokes and rim edges. It does not determine all positivity windows when \(m\ge7\), prove an optimal step-length bound for arbitrary wheels, or address higher-order Padé approximants. The proof is an exact mathematical argument; finite computations are corroborative, not an exhaustive proof for unbounded \(m\). Specialized earlier results not located in the literature search may still cover parts of the claim. Independent audit has not been performed.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010. Public author copy and repository deposit dated 2010-10-15: https://mural.maynoothuniversity.ie/id/eprint/2195/ .
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, Linear Algebra and its Applications 436 (2012), 3425–3442. Author PDF: https://www.hamilton.ie/skirkland/pade_paper_final_end.pdf .
3. A. Mednykh, *Laplacians of Graphs, Spectra and Laplacian Polynomials*, 2015 lecture notes, Exercise 1.6 (wheel spectrum): https://conferences.matheo.si/event/10/attachments/79/161/Lecture_1_Laplacian_Mednykh_Rogla_2015.pdf .
