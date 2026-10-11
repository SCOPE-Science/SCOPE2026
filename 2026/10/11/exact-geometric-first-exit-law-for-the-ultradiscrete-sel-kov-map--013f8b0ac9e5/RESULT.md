# Exact geometric first-exit law for the ultradiscrete Sel'kov map

## Finding

For each real \(B>0\), consider the piecewise-affine dynamical system
\[
F_B(X,Y)=\bigl(Y+\max(0,2X),\ B-\max(0,2X)\bigr).
\]
Its expanding-branch fixed point is \(p_B=(B,-B)\). Define the **strict positive-branch survivor set**, for an integer \(n\geq0\), by
\[
S_n(B)=\{z\in\mathbb R^2:(F_B^j(z))_1>0\text{ for every }0\le j\le n\}.
\]
Here \((z)_1\) denotes the first coordinate. The theorem is that **for every \(B>0\) and every integer \(n\ge6\)**,
\[
S_{n+1}(B)-p_B=A^{-1}(S_n(B)-p_B),\qquad
\operatorname{area}(S_n(B))=\frac{79B^2}{2^{n+1}},
\qquad A=\begin{pmatrix}2&1\\-2&0\end{pmatrix}.
\]
In particular, \(S_6(B)\) is the interior of a heptagon, and its closure, shifted by \(p_B\), has the following vertices in cyclic order, scaled by \(B\):
\[
\left(-1,\tfrac98\right),\left(-1,1\right),
\left(-\tfrac12,0\right),\left(0,-\tfrac12\right),
\left(\tfrac14,-\tfrac12\right),\left(\tfrac14,-\tfrac14\right),
\left(\tfrac18,0\right).
\]
For initial conditions sampled uniformly by planar Lebesgue measure on the bounded open set \(S_6(B)\), the first nonpositive-first-coordinate time
\[
\tau(z)=\min\{j\ge0:(F_B^j(z))_1\le0\}
\]
has the **exact geometric distribution**, for every integer \(k\ge0\):
\[
\Pr\{\tau>6+k\}=2^{-k},\qquad
\Pr\{\tau=7+k\}=2^{-k-1},\qquad
\mathbb E[\tau]=8.
\]
Moreover, the unique orbit remaining in the strict positive branch forever is the fixed point \(p_B\).

## Assumptions and scope

The parameter is an arbitrary real \(B>0\); the phase space is all \(\mathbb R^2\), not a single Poincaré section or a neighborhood. Branch membership is strict (\(X>0\)); first exit is defined by \(X\le0\). Planar area is ordinary Lebesgue measure and is finite for all \(n\ge6\). The results concern first escape **from the expanding branch**, not ultimate absorption into the attracting seven-cycle, nor stochastic perturbations of the map. No claims about the detailed polygon formula for \(n<6\) are needed.

## Proof

**1. Exact affine dynamics while surviving.** The positive branch is \(F_B(z)=Az+(0,B)\). Direct substitution gives \(F_B(p_B)=p_B\). Put \(u=z-p_B\) and \(r_j=(1,0)A^j\). For every orbit whose first coordinate stays positive up through time \(n\), induction gives \(F_B^j(z)=p_B+A^ju\) for \(0\le j\le n\). Conversely, if \(B+r_j u>0\) for \(0\le j\le n\), the same induction verifies that the actual piecewise map follows this affine formula through time \(n\). Consequently, with no branch substitution made outside its validity,
\[
S_n(B)-p_B=\{u\in\mathbb R^2:r_j u>-B\text{ for }0\le j\le n\}.
\]
This is an equivalence for every \(n\ge0\).

**2. The sharp renewal-onset survival polygon.** Exact integer matrix multiplication yields
\[
(r_0,r_1,\ldots,r_7)=
((1,0),(2,1),(2,2),(0,2),(-4,0),(-8,-4),(-8,-8),(0,-8)).
\]
The seven inequalities \(r_j u\ge-B\), \(0\le j\le6\), enclose a bounded convex polygon. For \(B=1\), intersection of the supporting pairs of lines, with the other inequalities imposed, gives exactly the seven vertices listed in the finding. Every listed point satisfies all seven weak inequalities, and every intersection of two supporting lines that satisfies the entire system is in this list; equivalently, checking the seven consecutive supporting edges establishes their complete enclosing polygon. Scaling by \(B\) gives the general case. The shoelace formula, in the cyclic order written above, gives
\[
2\operatorname{area}(S_6(1))
=\tfrac18+\tfrac12+\tfrac14+\tfrac18
+\tfrac1{16}+\tfrac1{32}+\tfrac9{64}=\tfrac{79}{64}.
\]
Therefore \(\operatorname{area}(S_6(B))=79B^2/128\). Strict versus weak inequalities affect only the polygon boundary, a null set. The preceding set \(S_5(B)\) is also bounded: its closure, centered at \(p_B\) and divided by \(B\), is the hexagon with cyclic vertices \((-1,9/4)\), \((-1,1)\), \((-1/2,0)\), \((0,-1/2)\), \((1/4,-1/2)\), and \((1/4,-1/4)\). Intersecting the first six halfplanes and applying the same shoelace formula gives its area \(5B^2/4\); hence the first area ratio from \(n=5\) to \(n=6\) is \(79/160\), not \(1/2\). The one-step renewal law starts sharply at \(n=6\).

**3. An exact one-step renormalization.** Matrix multiplication also gives
\[
A^4=-4I,\qquad A^8=16I,\qquad \det A=2.
\]
For any integer \(n\ge6\), the set \(A^{-1}(S_n(B)-p_B)\) consists of the points satisfying precisely the inequalities with indices \(j=1,2,\ldots,n+1\). In that system, the \(j=7\) inequality gives \(u_2<B/8\), whereas the \(j=1\) inequality gives \(2u_1+u_2>-B\). Combining them yields \(u_1> -9B/16>-B\), which implies the missing \(j=0\) inequality. Thus the omitted condition is redundant, and the remaining conditions are exactly those defining \(S_{n+1}(B)-p_B\). This proves the stated set identity, not merely an equality of areas. This onset is sharp: for \(B=1\), the displacement \(u=(-11/10,121/100)\) satisfies all inequalities with indices \(j=1,\ldots,6\), but violates \(u_1>-1\). Rescaling gives the same obstruction for every \(B>0\) and every \(n\le5\). In particular,
\[
S_n(B)-p_B=A^{-(n-6)}(S_6(B)-p_B),\qquad n\ge6.
\]
The area formula follows by induction because \(|\det A^{-1}|=1/2\). Every \(S_n(B)\) is a homothetic image after each eighth step because \(A^{-8}=I/16\), while intermediate shapes are affinely transformed.

**4. Exact first-exit law and uniqueness.** For any \(z\in S_6(B)\), \(\tau(z)\ge7\). Since \(\{z\in S_6(B):\tau(z)>6+k\}=S_{6+k}(B)\), the ratio of the two area formulas gives \(\Pr\{\tau>6+k\}=2^{-k}\). Differencing successive survival probabilities gives \(\Pr\{\tau=7+k\}=2^{-k-1}\), a proper geometric law of total mass one and mean \(7+1=8\). Finally, \(A^8=16I\) and boundedness of \(S_6(B)\) imply that \(A^{-(n-6)}S_6(B)\) contracts to the origin as \(n\to\infty\), so their intersection is \(\{0\}\), corresponding to the surviving fixed point \(p_B\).

## Verification

The standalone standard-library Python script `verification/check.py` uses exact rational fractions, not floating point. It checks \(A^8=16I\), the seven supporting inequalities, complete half-plane vertex enumeration, all seven heptagon vertices, the exact shoelace area, the one-step inverse-polygon identity for \(6\le n\le18\), area formulas for those \(n\), and scaling for three positive rational \(B\)-values. Its expected final line is `EXACT_SELVKOV_SURVIVOR_CERTIFICATE_OK`. These finite checks are reproducibility aids; the all-\(n\) theorem and infinite survivor assertion depend on the analytic induction proved above, not on finite enumerations.

## Relationship to prior work

Ohmori and Yamazaki first derive this max-plus map from a tropically discretized Sel'kov model (arXiv:2107.02435, equations (13)–(14)). Their follow-up study of two seven-cycles develops a Poincaré return map, stability, and the singular backward-basin curves for the repelling cycle (arXiv:2204.00745, Sections 3–4; and *JSIAM Letters* 14 (2022), 127–130). The heptagon introduced in their integrable-mapping analysis is a distinct invariant-cycle polygon in other coordinates; it is not the planar strict-first-escape survivor heptagon quantified here. Their later generalized max-plus model (arXiv:2402.06230) studies parameter-dependent cycles and return maps; its positive-region dynamics provides context but not the present exact Lebesgue-area or first-exit distribution statement. The present theorem concerns the entire two-dimensional initial-condition set for each number of consecutive expanding-branch visits.

## Limitations

The theorem is a deterministic result for the specific two-dimensional max-plus map and \(B>0\). The normalized area coefficient \(79/128\) pertains to the natural, exact cutoff after seven tested branch coordinates and is not asserted to be universal for other max-plus systems. Uniform sampling is with respect to normalized Lebesgue measure on \(S_6(B)\), not an invariant probability of the full map. The result does not characterize what happens after the first branch exit, or the distribution under other initial sampling laws. No independent mathematical validation has been performed.

## References

1. S. Ohmori and Y. Yamazaki, *Dynamical properties of max-plus equations obtained from tropically discretized Sel'kov model*, arXiv:2107.02435 (first posted 2021-07-06), https://arxiv.org/abs/2107.02435.
2. S. Ohmori and Y. Yamazaki, *Poincaré Map Method for Limit Cycles in a Max-Plus Dynamical System*, arXiv:2204.00745 (first posted 2022-04-02), https://arxiv.org/abs/2204.00745.
3. S. Ohmori and Y. Yamazaki, *Poincaré map approach to limit cycles of a simplified ultradiscrete Sel'kov model*, *JSIAM Letters* **14** (2022), 127–130, DOI:10.14495/jsiaml.14.127.
4. S. Ohmori and Y. Yamazaki, *A Generalization for Ultradiscrete Limit Cycles in a Certain Type of Max-Plus Dynamical Systems*, arXiv:2402.06230 (first posted 2024-02-09), https://arxiv.org/abs/2402.06230.
