# Corrected equilibria and local spectrum of the Cui–Li four-dimensional flow

## Finding
Consider the four-dimensional autonomous system
\[
\dot u=a(v-u)+evw,\qquad
\dot v=cu+dv-uw+mp,\qquad
\dot w=-bw+uv,\qquad
\dot p=-k(u+v),
\]
with \(a,b,e,m,k>0\) and \(c,d\in\mathbb R\). Its equilibria are exactly
\[
E_0=(0,0,0,0),
\]
and
\[
E_\sigma=\left(\sigma r,-\sigma r,-\frac{2a}{e},\frac{\sigma r(de-ce-2a)}{em}\right),
\qquad
r=\sqrt{\frac{2ab}{e}},
\qquad
\sigma\in\{-1,1\}.
\]
At either nonzero equilibrium the characteristic polynomial of the Jacobian is
\[
\chi(\lambda)=\lambda^4+(a+b-d)\lambda^3
+\left(km-ab+ac-ad-bd+\frac{2a(a+b)}{e}\right)\lambda^2
+\left(b(3ac+ad+km)+\frac{10a^2b}{e}\right)\lambda
-4abkm.
\]
The introducing paper's displayed nonzero equilibrium coordinate contains \(de-ce-2ad\) where direct stationarity gives \(de-ce-2a\). Its displayed nonzero characteristic polynomial likewise has extra factors. The printed nonzero points are generally not equilibria: substituting their fourth coordinate into the second stationarity equation leaves the residual
\[
\frac{2au(1-d)}{e},
\]
which vanishes on the nonzero branch only when \(d=1\).

For the paper's numerical parameters
\[
(a,b,c,d,e,m,k)=(15,43,1,16,5,5,2),
\]
the corrected pair is
\[
E_\sigma=\left(\sigma\sqrt{258},-\sigma\sqrt{258},-6,\frac{9\sigma}{5}\sqrt{258}\right),
\]
so the fourth coordinate has magnitude about \(28.9122811\), not about \(260.210\). The exact characteristic polynomial becomes
\[
\lambda^4+42\lambda^3-1200\lambda^2+32035\lambda-25800.
\]
Its Routh first column is
\[
1,\quad 42,\quad -\frac{82435}{42},\quad \frac{519058805}{16487},\quad -25800,
\]
which has three sign changes. Hence each corrected nonzero equilibrium has exactly three eigenvalues in the open right half-plane and one in the open left half-plane.

## Assumptions and scope
The proof uses only \(a,b,e,m,k>0\), so that the square root is real and the eliminations divide only by nonzero parameters; \(c\) and \(d\) may be arbitrary real numbers. The baseline specialization uses exactly the parameter values stated in the source. The claim concerns the equilibrium set and the linearization at the nonzero equilibria. It does not classify global attractors, prove or disprove hyperchaos on non-equilibrium invariant sets, or validate numerical Lyapunov-exponent computations in the source.

## Proof
At an equilibrium, \(\dot p=0\) and \(k>0\) give \(v=-u\). Then \(\dot w=0\) and \(b>0\) give
\[
w=-\frac{u^2}{b}.
\]
Substitution into \(\dot u=0\) gives the exact factorization
\[
u\left(-2a+\frac{eu^2}{b}\right)=0.
\]
If \(u=0\), then \(v=w=0\), and \(\dot v=mp=0\) gives \(p=0\). Otherwise
\[
u^2=\frac{2ab}{e},\qquad w=-\frac{2a}{e},\qquad v=-u.
\]
Finally \(\dot v=0\) gives
\[
p=-\frac{u(c-d+2a/e)}{m}=\frac{u(de-ce-2a)}{em},
\]
which proves the exhaustive equilibrium formula.

The Jacobian is
\[
J=\begin{pmatrix}
-a & a+ew & ev & 0\\
c-w & d & -u & m\\
v & u & -b & 0\\
-k & -k & 0 & 0
\end{pmatrix}.
\]
Substituting \(v=-u\), \(w=-2a/e\), and \(u^2=2ab/e\) into \(\det(\lambda I-J)\) and collecting powers of \(\lambda\) gives the polynomial stated above. Its constant term is \(-4abkm<0\), which already guarantees at least one positive real eigenvalue and therefore preserves the source's qualitative instability conclusion.

For the source parameters, direct substitution produces the displayed quartic. The standard Routh array has the exact first column displayed above. None of those entries vanishes, so the Routh criterion applies without a singular case; three sign changes give exactly three roots in the open right half-plane.

## Verification
The companion file `verify.py` reconstructs the equilibrium elimination symbolically, recomputes \(\det(\lambda I-J)\), specializes the result to the published parameter values, and checks the exact rational Routh entries. Executing

`python3 verify.py`

returns `VERIFY_OK`. The verification uses exact symbolic and rational arithmetic for every asserted algebraic identity and sign count; decimal values are reported only for orientation.

## Relationship to prior work
Cui and Li introduce the system, state the same seven-parameter vector field, and in their equilibrium analysis display the two nonzero points with a fourth coordinate proportional to \(de-ce-2ad\). In the following local-stability calculation they also display a nonzero characteristic polynomial whose cubic coefficient and two lower coefficients contain extra factors relative to the determinant of the published Jacobian. Their negative constant term correctly implies instability, but it does not repair the coordinates or determine the unstable dimension.

Searches by DOI, exact title, the displayed equilibrium factor, the vector-field equations, and Qi-system aliases did not locate a published correction of these formulas. Earlier Qi-derived four-dimensional hyperchaotic systems use different controller constructions and do not imply the corrected stationary equations above. The present statement is therefore a correction and sharpening of the local equilibrium geometry of this specific published flow, not a claim that the underlying Qi-system lineage is new.

## Limitations
The originality search cannot exclude an unindexed correction, private communication, or later commentary not returned by the searched literature services. Two earlier Qi-hyperchaos papers were compared through their indexed abstracts and bibliographic descriptions rather than complete full text; they are recorded as residual literature risk because they concern the same model lineage but different controller constructions. The result is local: it gives exact equilibria and their tangent spectra, not the global invariant-set structure.

## References
1. Ning Cui and Junhong Li, “A new 4D hyperchaotic system and its control,” *AIMS Mathematics* 8(1), 905–923, DOI 10.3934/math.2023044. Published 13 October 2022. The defining system is Eq. (1.2); the equilibrium and linear-stability formulas are in Section 2.3.
2. “Hyperchaos generated from Qi system and its observer,” DOI 10.1142/S021798490901920X. Indexed 2009; inspected as prior Qi-derived four-dimensional context.
3. “Hyperchaos Qi system,” DOI 10.1142/S0217979210055895. Indexed 2010; inspected as prior Qi-derived four-dimensional context.
