# Sharp Radau IIA positivity and reentry on balanced multipartite diffusion networks

## Finding
Let \(G_{r,m}=K_{m,\ldots,m}\) be the unweighted complete \(r\)-partite graph with \(r\ge3\) parts, each of size \(m\ge2\), and let \(L\) be its combinatorial Laplacian. The two-stage, third-order Radau IIA completed diffusion step is
\[
T_{r,m}(h)=(6I-2hL)(6I+4hL+h^2L^2)^{-1},\qquad h\ge0.
\]
Entrywise nonnegativity at **every** timestep holds exactly for
\[
\boxed{(r,m)\in\{(3,2),(3,3),(4,2),(5,2)\}.}
\]
For every other admissible pair, there are **exactly two** positive thresholds \(0<h_-<h_+\), and the complete positivity set is
\[
\boxed{\{h\ge0:T_{r,m}(h)\ge0\text{ entrywise}\}=[0,h_-]\cup[h_+,\infty).}
\]
In particular, a positive intermediate-timestep window is unsafe, whereas both sufficiently small and sufficiently large timesteps are positive. The two thresholds are exactly the positive roots of a specified quartic, divided by \(m\), and only diagonal entries can ever be negative.

## Assumptions and scope
All graphs are finite, simple, unweighted, undirected; \(r\ge3\) and \(m\ge2\) are integers; each part has the same size \(m\). The graph has \(N=rm\) vertices. For \(z=mh\), put
\[
D_a=(r-1)^2z^2+4(r-1)z+6,\quad D_b=r^2z^2+4rz+6
\]
and
\[
\begin{aligned}
C_{r,m}(z)={}&r(r-1)^2z^4+2(r-1)\bigl(3(2r-1)-mr^2\bigr)z^3\\
&+\bigl(2mr(4-r)+18(r-1)\bigr)z^2\\
&+12m(r+1)z+36m.
\end{aligned}
\]
The thresholds are \(h_-=z_-/m\) and \(h_+=z_+/m\), where \(z_-<z_+\) are the two positive real zeros of \(C_{r,m}\); this definition applies only outside the four unconditional families. No assertion is made about unequal part sizes or other numerical methods.

## Proof
**Spectral reduction.** Write \(J=\mathbf1\mathbf1^\mathsf{T}\), let \(J_m\) be the \(m\)-by-\(m\) all-ones matrix, let \(E=\operatorname{diag}(J_m/m,\ldots,J_m/m)\), and set \(N=rm\). The orthogonal spectral projectors of \(L\) are \(J/N\) (eigenvalue 0), \(I-E\) (eigenvalue \((r-1)m\)), and \(E-J/N\) (eigenvalue \(rm\)). Let
\[
R(x)=\frac{6-2x}{x^2+4x+6},\quad a=R((r-1)z),\quad b=R(rz).
\]
Functional calculus gives \(T=J/N+a(I-E)+b(E-J/N)\). Consequently its three distinct entry types are exactly
\[
\begin{aligned}
T_{uu}&=\frac{C_{r,m}(z)}{mD_aD_b},\\
T_{uv}\quad(u\ne v\text{ in one part})&=\frac{(r-1)z^2\bigl(r(r-1)z^2+(12r-6)z+18\bigr)}{mD_aD_b},\\
T_{uv}\quad(u,v\text{ in distinct parts})&=\frac{z(rz+6)}{mD_b}.
\end{aligned}
\]
All denominators are positive. Both off-diagonal types are strictly positive for \(z>0\); their values at \(z=0\) are zero. Hence all positivity decisions are exactly the sign of \(C_{r,m}(z)\).

**The four safe families.** The following finite table is an exact, all-real positive-polynomial certificate; each \(P\) is a strictly positive rational multiple of \(C_{r,m}\), so has the same sign:

| \((r,m)\) | \(P(z)\) | split point \(c\) | coefficients, descending, of \((1+t)^4P(ct/(1+t))\) | coefficients, descending, of \(P(c+t)\) |
|---|---|---|---|---|
| \((3,3)\) | \(2z^4-8z^3+9z^2+24z+18\) | 2 | 70, 224, 288, 120, 18 | 2, 8, 9, 28, 70 |
| \((4,2)\) | \(6z^4-11z^3+9z^2+20z+12\) | 1 | 36, 115, 141, 68, 12 | 6, 13, 12, 29, 36 |
| \((5,2)\) | \(20z^4-46z^3+13z^2+36z+18\) | 2 | 94, 24, 376, 144, 18 | 20, 114, 217, 176, 94 |

Because all coefficients in both transforms are positive, \(P(z)>0\) on \([0,c]\) and \([c,\infty)\) respectively. The remaining safe case \((3,2)\) follows by reducing \(m\) from 3: if \(a<0\) then \(1+r(m-1)a+(r-1)b\) strictly increases as \(m\) decreases; if \(a\ge0\), the elementary identity
\[
R(x)+\frac1{10}=\frac{(x-8)^2+2}{10(x^2+4x+6)}>0
\]
shows \(1+r(m-1)a+(r-1)b>1-(r-1)/10>0\), for \(r\le5\). This monotonicity also covers all smaller admissible \(m\) in the displayed safe cases.

**All other families fail.** For \((r,m)=(3,4),(4,3),(5,3)\), respectively, use \(z=4,2,2\). The exact values of \(1+r(m-1)a+(r-1)b\) are \(-12/187,-4/187,-1355/3723\). At each witness \(a<0\), so every larger \(m\) for that fixed \(r\) fails too. For every \(r\ge6\), set \(z=6/(r-1)\). Then \(a=R(6)=-1/11\), while \(6<rz\le36/5<3+3\sqrt3\), and \(R\) is strictly decreasing on this interval; thus \(b<-1/11\). Since \(rm\ge12\),
\[
1+r(m-1)a+(r-1)b<1-\frac{rm-1}{11}\le0.
\]
This covers all remaining integer parameters.

**Exactly one unsafe interval.** The leading and constant coefficients of \(C_{r,m}\) are positive; its coefficient of \(z^3\) is strictly negative for \(r\ge3,m\ge2\) because at \(m=2\) it equals \(-2(r-1)(2r^2-6r+3)<0\) and decreases with \(m\). The coefficient of \(z^2\) has arbitrary sign, while both linear and constant coefficients are positive. Thus the descending sign sequence has **exactly two sign changes**, whether the quadratic coefficient is positive, zero or negative. Descartes' rule gives at most two positive zeros counted with multiplicity. Every failing case has a negative value between \(C(0)>0\) and \(C(z)\to+\infty\) as \(z\to\infty\), so the intermediate value theorem gives two distinct positive roots. They are the only positive roots, and the sign is negative exactly between them. The endpoints belong to the positivity set because nonnegativity is inclusive.

## Verification
Run `python verify.py` with SymPy installed (`requirements.txt`). The standalone checker establishes all symbolic kernel identities, checks the complete positive-coefficient certificates, verifies strict rational witnesses, verifies the analytic sign identities, and compares exact rational direct inverses of Radau matrices with the three projector formulas in seven finite examples. It prints `VERIFY_OK all exact sign, symbolic, and direct rational identities`. Those finite tests are corroboration; the unbounded-parameter assertions are proved by the displayed algebra, monotonicity and Descartes argument.

## Relationship to prior work
Zappavigna, Colaneri, Kirkland and Shorten study positive systems and diagonal Padé discretizations and give general sufficient tests and counterexamples. These do **not** yield the exact Radau IIA threshold classification on equal-part complete multipartite graphs with at least three parts. Hairer and Wanner supply the classical Radau IIA numerical-method setting, not an entrywise-positivity classification on this graph family. The Laplacian spectrum and its projectors are standard background; their use alone is not claimed as new. Exact Radau positivity on complete bipartite graphs has also been separately studied and is outside this claim's \(r\ge3\) scope. Related fourth-order Gauss classifications for complete multipartite graphs involve a different stability function and do not imply these third-order Radau thresholds. No absolute claim of novelty follows merely from absence in a search; specialized unindexed literature could contain equivalent statements.

## Limitations
This is a structural result only for balanced multipartite graphs with \(r\ge3,m\ge2\). It does not characterize unbalanced multipartite graphs, arbitrary Markov generators, or stagewise positivity. The method's spectral stability is not the same as entrywise nonnegativity. Thresholds for general failing pairs are specified exactly as polynomial roots rather than radicals. A primary-literature search cannot rule out an unindexed equivalent graph-specific result. Independent mathematical validation has not been performed.

## References
1. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *On the preservation of co-positive Lyapunov functions under Padé discretization for positive systems*, MTNS 2010, open archive item 2195, https://mural.maynoothuniversity.ie/id/eprint/2195/1/SK-pade_MTNS10_long.pdf (public archive deposit 2010-10-15).
2. A. Zappavigna, P. Colaneri, S. Kirkland and R. Shorten, *Essentially Negative News About Positive Systems*, open archive preprint, 2012, https://mural.maynoothuniversity.ie/id/eprint/3761/1/SK_Essentially_Negative.pdf.
3. E. Hairer and G. Wanner, *Stiff differential equations solved by Radau methods*, https://www.unige.ch/~hairer/preprints/coimbra.pdf.
4. S. Klee and M. T. Stamps, *Eigenvalues of graph Laplacians via rank-one perturbations*, arXiv:2008.01669 (2020), https://arxiv.org/abs/2008.01669.
