# Sharp step-ratio resonance for two-period optimistic gradient on a bilinear saddle

## Finding
Consider the **naively step-scaled optimistic gradient update**
\[
 z_{k+1}=z_k-h_k\bigl(2F(z_k)-F(z_{k-1})\bigr),
 \qquad F(x,y)=(-y,x),\quad z_k=(x_k,y_k)\in\mathbb R^2.
\]
This is the operator for the unconstrained convex-concave bilinear game \(\min_x\max_y(-xy)\). Suppose \(h_{2j}=u\) and \(h_{2j+1}=v\), with \(u,v>0\). Define \(r=uv\), \(s=u+v\), and
\[
 \Delta(u,v)=3uv(2-5uv)(1+uv)^2-(u+v)^2(1-uv)^2.
\]
Then **every** initialization \((z_{-1},z_0)\) converges to the saddle \(0\) geometrically if and only if
\[
 \boxed{uv<1\quad\text{and}\quad\Delta(u,v)>0.}
\]
When \(uv<1\) and \(\Delta(u,v)<0\), the two-period map has a multiplier of modulus strictly greater than one, so an open dense set of real initial pairs diverges geometrically along even subsequences. Equality \(\Delta=0\), \(uv<1\), is a neutral spectral boundary and does not yield convergence from every initialization.

For a constant step \(u=v=h\), this criterion reduces exactly to \(0<h<1/\sqrt3\). Despite this, the two individually stable steps \(u=1/100\) and \(v=1/10\) give \(\Delta=-1215767223/200000000000<0\) and hence exponential divergence for generic initial states.

For every fixed \(a,b>0\), put \(u=at\), \(v=bt\) and let \(t\downarrow0\). The alternating method is geometrically convergent for all sufficiently small positive \(t\) **if and only if**
\[
 \boxed{2-\sqrt3\ \le\ a/b\ \le\ 2+\sqrt3.}
\]
Outside this closed ratio interval it diverges for generic initialization at *every sufficiently small* positive scale. This is a sharp relative-step requirement that cannot be replaced by any bound on the absolute maximum step alone.

## Assumptions and scope
All statements concern exact arithmetic, the fixed bilinear operator \(F(x,y)=(-y,x)\), positive deterministic two-period steps \(u,v\), and the explicitly specified **naive** extension that multiplies the entire historical-gradient combination by the current step. This algorithm is *not* the adaptive golden-ratio algorithm or a validated variable-step OGDA modification. “Converges from every initialization” concerns the full two-step state \((z_k,z_{k-1})\); “generic divergence” means an open dense set of initial full states excites an expansive mode. The frequency of the bilinear coupling is normalized to one; a coupling of size \(L>0\) is covered by replacing both \(u,v\) by \(Lu,Lv\).

## Proof
Identify \(\mathbb R^2\) with \(\mathbb C\) by \(w=x+iy\). The operator \(F\) becomes multiplication by \(i\), so the iteration is
\[
 w_{k+1}=(1-2ih_k)w_k+ih_kw_{k-1},\qquad
 T(h)=\begin{pmatrix}1-2ih&ih\\1&0\end{pmatrix}.
\]
For successive steps \(u,v\), the exact two-step matrix is \(M=T(v)T(u)\), with
\[
 \operatorname{tr}M=1-4uv-i(u+v),\qquad\det M=-uv.
\]
Thus the multipliers are the two roots of
\[
 p(\lambda)=\lambda^2-\bigl(1-4r-is\bigr)\lambda-r.
\]
For clarity, the degree-two Schur criterion used here is also derived. If \(p(z)=z^2+Az+B\) with \(|B|<1\), its reciprocal is \(p^*(z)=\overline Bz^2+\overline Az+1\). Since \(|p(z)|=|p^*(z)|\) on the unit circle, Rouché's theorem applied to \(p-Bp^*\) (initially excluding roots on the circle, then by continuity) gives the equivalence
\[
 \text{both roots of }p\text{ lie in }|z|<1
 \iff |B|<1\ \text{and}\ |A-B\overline A|<1-|B|^2.
\]
Indeed, \(p-Bp^*=z[(1-|B|^2)z+A-B\overline A]\). Its two roots lie inside precisely under that inequality, and on the strict domain the Rouché root count agrees with that of \(p\). Applying this criterion with \(A=-(1-4r-is)\), \(B=-r\), we obtain \(r<1\) and
\[
 \big|(1+r)(1-4r)-is(1-r)\big|<1-r^2.
\]
Squaring and subtracting yields the exact positive margin
\[
 (1-r^2)^2-(1+r)^2(1-4r)^2-s^2(1-r)^2
 =3r(2-5r)(1+r)^2-s^2(1-r)^2
 =\Delta(u,v).
\]
The real two-step map is the realification of the complex matrix \(M\), hence the same spectral conditions determine geometric convergence and instability over real initial data. A simple multiplier outside the unit circle has a proper real invariant complement of initial states that do not excite it; all other states diverge geometrically along even times. At \(r<1\) and \(\Delta=0\), the Schur boundary contains a unit-modulus multiplier and therefore precludes convergence for every initial pair.

Setting \(u=v=h\) and factoring yields
\[
 \Delta(h,h)=-h^2(h^2+2)(3h^2-1)(5h^2+1).
\]
This is positive precisely for \(0<h<1/\sqrt3\). The explicit rational witness follows by direct substitution into \(\Delta\).

For the small-step classification, put \(p=ab t^2\) and \(c=(a+b)^2/(ab)\). Then \(s^2=cp\) and
\[
 \Delta(at,bt)
 =p\left[3(2-5p)(1+p)^2-c(1-p)^2\right].
\]
If \(c<6\), the bracket is eventually positive; if \(c>6\), eventually negative. The exceptional boundary \(c=6\) is also stable for sufficiently small positive \(p\), because the exact bracket reduces to \(3p(3-10p-5p^2)>0\) near zero. Finally \(c\le6\) is equivalent to \((a-b)^2\le2ab\), or \(2-\sqrt3\le a/b\le2+\sqrt3\). This completes all quantifiers, including the equality cases.

## Verification
The self-contained `verify_ogda.py` computes the exact characteristic trace and determinant and checks the sign of the Schur margin against direct complex eigenvalues on a finite grid; it also verifies the rational instability witness, constant-step factorization, and representative small-scale ratios. Run `python3 verify_ogda.py` with Python 3 and no external dependencies. These checks are finite corroboration; the proof above establishes the infinite-horizon statement for all positive steps.

## Relationship to prior work
Anagnostides and Penna (2020, arXiv:2010.03211, Theorem 3.1) establish the sharp constant-step OGDA stability limit \(1/\sqrt3\) on bilinear games. De Montbrun and Renault (2022, arXiv:2208.03085, Section 2) analyze constant-step OGDA and its rates. Alacaoglu, Böhm, and Malitsky (2022, arXiv:2212.13955; JMLR 2023, Sections 2 and 4) connect **fixed-step** OGDA with the golden-ratio algorithm and separately study a genuinely adaptive algorithm with different state variables and a safeguarded stepsize rule. The present result does not challenge those existing convergence guarantees: it concerns the specifically defined naive variable-step substitution, and supplies its exact two-period Floquet region and a sharp vanishing-step ratio boundary.

The root criterion is classical Schur stability; novelty, if any, is the exact algebraic application and the qualitative consequence for this particular variable-step optimizer. Earlier time-varying-gradient or multistep stability results could provide an equivalent special case; this has not been independently ruled out.

## Limitations
The conclusion neither applies to arbitrary nonperiodic schedules nor demonstrates failure of the authors' adaptive GRAAL method, step-history-aware optimism, extragradient, or other safeguarded updates. There is no claim about stochastic gradients, nonlinear games, constrained problems, finite precision, or all variable-step methods. The equality boundary is nonasymptotically neutral and is **not** geometric convergence for all initial states. Originality remains a best-knowledge comparison rather than independent priority certification.

## References
1. I. Anagnostides and P. Penna, *A Robust Framework for Analyzing Gradient-Based Dynamics in Bilinear Games*, arXiv:2010.03211 (first public version 2020-10-07), Sections 2–3 and Theorem 3.1. https://arxiv.org/abs/2010.03211
2. É. de Montbrun and J. Renault, *Optimistic Gradient Descent Ascent in Zero-Sum and General-Sum Bilinear Games*, arXiv:2208.03085 (first public version 2022-08-05), Section 2. https://arxiv.org/abs/2208.03085
3. A. Alacaoglu, A. Böhm, and Y. Malitsky, *Beyond the Golden Ratio for Variational Inequality Algorithms*, arXiv:2212.13955 (first public version 2022-12-28), JMLR 24 (2023), Sections 2 and 4. https://arxiv.org/abs/2212.13955
