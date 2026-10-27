# An optimal four-cell polygonal generator for a nonsplit neutral toral endomorphism

## Finding
Let \(T:\mathbb T^2\to\mathbb T^2\) be the Haar-preserving toral endomorphism
\[
 T(x,y)=(x+y,3y)\pmod1,
\]
represented by the integer matrix \(\left(\begin{smallmatrix}1&1\\0&3\end{smallmatrix}\right)\). With canonical representatives \(0\le x,y<1\), define the four polygonal atoms
\[
\begin{aligned}
 C_0&=\{0\le y<1/3,\ 0\le x<3y\},\\
 C_1&=\{0\le y<1/3,\ 3y\le x<1\},\\
 C_2&=\{1/3\le y<2/3\},\\
 C_3&=\{2/3\le y<1\}.
\end{aligned}
\]
Unspecified \(x\) in the last two atoms is unrestricted in \([0,1)\). This partition is a one-sided generator modulo Haar-null sets: its complete forward name determines almost every point. Moreover **no partition into at most three measurable atoms** is a one-sided generator. Consequently the least cardinality of a measurable generator and that of a polygonal generator are both \(4\). This is an explicit optimal geometric coding of the smallest nonsplit triangular neutral–expanding integral example.

## Assumptions and scope
The torus is \(\mathbb R^2/\mathbb Z^2\), equipped with normalized Haar (Lebesgue) measure. The half-open convention makes the displayed atoms a genuine Borel partition; their boundaries consist of finitely many line segments in a square fundamental domain, with Haar measure zero. One-sided generation means that the itineraries \((C(T^n(x,y)))_{n\ge0}\) are injective on a measurable set of full Haar measure. No Markov/Rokhlin or everywhere-injective assertion is made. The matrix has eigenvalues \(1,3\), with primitive integral eigenvectors \((1,0),(1,2)\) of determinant \(2\); thus it is not integrally conjugate to \(\operatorname{diag}(1,3)\).

## Proof
**1. The expanding coordinate is reconstructed.** Merge the symbols \(0,1\) into ternary digit \(0\); relabel \(2\) as digit \(1\), and \(3\) as digit \(2\). The resulting itinerary is \(d_n=\lfloor3y_n\rfloor\) for \(y_n=3^ny\pmod1\). Therefore
\[
 y=\sum_{n\ge0}d_n3^{-n-1}
\]
with the usual greedy half-open convention. Once \(y\) is known, so is the entire sequence \((y_n)\).

**2. A two-sheet lift provides an exact orbit identity.** Put \(z=\{x-y/2\}\), with braces denoting fractional part, and \(v_n=3^ny\pmod2\in[0,2)\). Summing the first-coordinate recurrence modulo \(1\) gives
\[
 x_n\equiv x+\frac{3^n-1}{2}y
      \equiv z+\frac{v_n}{2}\pmod1,
 \qquad y_n=\{v_n\}.
\]
The map \(v\mapsto3v\pmod2\) is conjugate by division by \(2\) to the standard tripling map of the circle. It is ergodic for normalized Lebesgue measure. Hence for Lebesgue-almost every starting \(y\in[0,1)\), the sequence \((v_n)\) is equidistributed in \([0,2)\). Fix such a \(y\); in particular the visits \(v_n=j+t\), for each \(j\in\{0,1\}\), are dense throughout \(t\in(0,1/3)\). These are exactly the visits to the ternary-zero strip. At these times, the label \(0\) records the inequality
\[
  \left\{s_j+\frac t2\right\}<3t,
 \qquad s_0=z,\quad s_1=\{z+1/2\}.
\]
Both the return values \(j,t\) and the label are known from \(y\) and the original forward name.

**3. Each return family determines a threshold.** For \(0\le s<1\) and \(0<t<1/3\) **away from the single threshold equality**, direct resolution of the inequality, including its single possible wrap modulo \(1\), gives
\[
 \left\{s+\frac t2\right\}<3t
 \quad\Longleftrightarrow\quad
 t>\tau(s),\qquad
 \tau(s)=\min\left\{\frac{2s}{5},\ 2(1-s)\right\}.
\]
The two affine terms cross at \(s=5/6\). At equality \(t=\tau(s)\), the label convention depends on whether the crossing is through a strict inequality or a modular wrap; this single value is irrelevant to dense-return reconstruction. By density of the return values, the observed labels for each \(j\) determine \(\tau(s_j)\) as the infimum of the \(t\) associated to label \(0\), **taking the value \(1/3\) when no such labels occur**, with equality conventions irrelevant at a single threshold. Thus the forward name determines
\[
 \Phi(z)=\bigl(\tau(z),\tau(\{z+1/2\})\bigr).
\]

**4. The pair of thresholds uniquely determines almost every \(z\).** The function \(\tau\) increases strictly on \([0,5/6]\) and decreases strictly on \([5/6,1)\). If distinct \(z<z'\) have \(\tau(z)=\tau(z')\), necessarily \(z<5/6<z'\) and \(z'=1-z/5\). For \(0<z<1/3\), comparison of the second thresholds becomes \(z+1/2=z'-1/2\), impossible; for \(1/3\le z<1/2\), it becomes \(1-2z=(1-2z/5)/5\), giving exactly \(z=5/12\) and \(z'=11/12\). For \(1/2\le z<5/6\), the second-threshold equality yields \(z=5/6\), contradicting distinctness. The endpoint \(z=0\) corresponds only to the identified circle seam. Thus \(\Phi\) has precisely one nontrivial double fiber, \(\{5/12,11/12\}\), and is injective elsewhere. Excluding the Haar-null set of starting points with either exceptional \(z\) value, the label sequence recovers \(z\), then \(x=\{z+y/2\}\). Therefore the displayed four polygonal atoms generate one-sidedly.

**5. Four atoms are necessary even without boundary restrictions.** The linear factor map
\[
 P(x,y)=(2x-y,y)\pmod1
\]
is a two-to-one toral covering satisfying \(P\circ T=(\operatorname{id}\times D_3)\circ P\), where \(D_3(y)=3y\pmod1\). A finite-to-one extension has the same measure entropy as its factor: given the entire factor orbit, the remaining initial ambiguity is a single two-valued sheet, which contributes at most \(\log2\) total information, not per-step entropy. Hence \(h_\mathrm{Haar}(T)=\log3\). If a generating partition had \(k\le3\) atoms, entropy forces \(k=3\) and entropy rate \(\log3\). For a stationary three-letter process, attaining maximal entropy rate implies every finite name block is uniformly distributed: for every \(n\), its Shannon entropy is bounded above by \(n\log3\), and bounded below by \(n\) times the entropy rate. Thus the name process would be uniform i.i.d., hence ergodic. Generation would make \(T\) itself ergodic. But the nonconstant invariant \(\theta=2x-y\pmod1\) shows \(T\) is not ergodic. Therefore \(k\ge4\), completing the proof.

## Verification
The exact orbit identity and threshold reduction were checked on rational grids by the standalone script `verify_generator.py`, yielding `EXACT_THRESHOLD_TESTS_PASS 11663` and `EXACT_SKEW_ORBIT_IDENTITIES_PASS 4536`. An exact rational collision check gives \(\tau(5/12)=\tau(11/12)=1/6\). The infinite-time conclusions use the analytical ergodic and entropy arguments above, **not** these finite tests. The verification script uses only Python's standard library and exact rational arithmetic; run with `python verify_generator.py`.

## Relationship to prior work
Leuridan, *Linear toral endomorphisms, exactness, Bernoulliness and generators* (arXiv:2610.01642v1, publicly submitted 2026-10-01), proves a boundary obstruction for eigenvalues of modulus **strictly below** one. Its splitting results also explain a measurable product structure, but not the existence of a **minimal polygonal** one-sided generator in the original nonsplit integral coordinates. Prior explicit work on \(\operatorname{diag}(1,m)\) proves an optimal \(m+1\)-atom polygonal generator for a diagonal neutral product, while work on \((\theta,y)\mapsto(\theta+\alpha,my)\) handles irrational translation. The former pulled back through \(P\) does not separate the two points in each fiber \(\{(x,y),(x+1/2,y)\}\), and the latter has a different moving-phase base. Thus neither result logically provides the present four-cell polygonal generator. The general measurable minimum is consistent with known product isomorphisms; **the new assertion is the optimal geometric realization in a genuinely nonsplit model**. Hughes and de Jong (arXiv:2604.00257) investigate the stronger Markov requirement for fully expanding maps, not ordinary generators for neutral skew maps.

## Limitations
The claim is only for the explicit nonsplit matrix \(\left(\begin{smallmatrix}1&1\\0&3\end{smallmatrix}\right)\), Haar measure, and almost-everywhere one-sided generation. No Markov property, pointwise exceptional-set classification beyond the decoder, general triangular-family formula, or smooth conjugacy classification is established. Earlier general geometric-coding constructions could potentially subsume this exact four-atom partition; the accessible literature comparisons do not constitute an exhaustive priority guarantee.

## References
1. C. Leuridan, *Linear toral endomorphisms, exactness, Bernoulliness and generators*, arXiv:2610.01642v1, public date 2026-10-01. https://arxiv.org/pdf/2610.01642 .
2. *Sharp \(m+1\) polyhedral generators for neutral–expanding toral products* (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-m-1-polyhedral-generators-for-neutral-expanding-toral-prod--b8dc89e947a7 .
3. *Optimal \(m+1\)-cell polygonal generators for quasiperiodic–expanding toral maps* (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-optimal-m-1-cell-polygonal-generators-for-quasiperiodic-expandin--4edb0ee2c3e2 .
4. C. Hughes and H. de Jong, *Smoothness of Markov Partitions for Expanding Toral Endomorphisms*, arXiv:2604.00257v2 (2026). https://arxiv.org/abs/2604.00257 .
5. W. Krieger, *On entropy and generators of measure-preserving transformations*, Trans. AMS 149 (1970), 453–464. https://doi.org/10.1090/S0002-9947-1970-0259068-3 .
