# Exact Ptolemy constant \(C_{\mathrm{Pt}}=\lambda\) on the first Banaś–Frączek regime
## Finding
For the real Banaś–Frączek plane \(R_\lambda^2=(\mathbb R^2,N_\lambda)\), \(N_\lambda(x_1,x_2)=\max\{\lambda|x_1|,\sqrt{x_1^2+x_2^2}\}\), the Ptolemy constant satisfies \(C_{\mathrm{Pt}}(R_\lambda^2)=\lambda\) for every \(1<\lambda\le\sqrt2\).

Here the Ptolemy constant is
\[
C_{\mathrm{Pt}}(X)
=
\sup
\frac{\|x-y\|\,\|z\|}
{\|x-z\|\,\|y\|+\|z-y\|\,\|x\|},
\]
where the supremum ranges over nonzero pairwise distinct \(x,y,z\in X\).

## Assumptions and scope
The scalar field is real. The parameter range is \(1<\lambda\le\sqrt2\). No claim is made here about the exact value for \(\lambda>\sqrt2\).

The space is the classical two-dimensional Banaś–Frączek deformation, with
\[
N_\lambda(v)=\max\{E(v),F(v)\},\qquad
E(v)=\sqrt{v_1^2+v_2^2},\qquad
F(v)=\lambda|v_1|.
\]

## Proof
Fix nonzero pairwise distinct \(x,y,z\). In the numerator
\[
N_\lambda(x-y)N_\lambda(z),
\]
choose for each factor an active branch \(E\) or \(F\).

If both active branches are \(E\), Euclidean Ptolemy gives
\[
E(x-y)E(z)
\le E(x-z)E(y)+E(z-y)E(x)
\le N_\lambda(x-z)N_\lambda(y)+N_\lambda(z-y)N_\lambda(x).
\]

If both active branches are \(F\), the ordinary one-dimensional Ptolemy inequality applied to the first coordinate gives
\[
F(x-y)F(z)
\le F(x-z)F(y)+F(z-y)F(x),
\]
and the right-hand side is again bounded by the denominator formed with \(N_\lambda\).

In either mixed case, use \(F(v)\le\lambda E(v)\). For example,
\[
E(x-y)F(z)
\le \lambda E(x-y)E(z)
\le \lambda\!\left(E(x-z)E(y)+E(z-y)E(x)\right),
\]
so the Ptolemy ratio is at most \(\lambda\). The other mixed case is identical. Therefore
\[
C_{\mathrm{Pt}}(R_\lambda^2)\le\lambda
\]
for every \(\lambda>1\).

For the reverse inequality in the stated range, take
\[
x=\left(\frac12,\frac12\right),\qquad
y=\left(\frac12,-\frac12\right),\qquad
z=(1,0).
\]
Then
\[
N_\lambda(x-y)=1,\qquad N_\lambda(z)=\lambda.
\]
Moreover,
\[
N_\lambda(x)
=
N_\lambda(y)
=
N_\lambda(x-z)
=
N_\lambda(z-y)
=
\max\left\{\frac{\lambda}{2},\frac1{\sqrt2}\right\}.
\]
When \(1<\lambda\le\sqrt2\), all four of these terms equal \(1/\sqrt2\). Hence the denominator is
\[
\frac12+\frac12=1,
\]
and the displayed triple has Ptolemy ratio exactly \(\lambda\). Thus
\[
C_{\mathrm{Pt}}(R_\lambda^2)=\lambda
\]
throughout \(1<\lambda\le\sqrt2\).

## Verification
The upper bound exhausts all four active-branch combinations of the two numerator factors. The \(F\)-branch is the pullback of the absolute-value metric on \(\mathbb R\), multiplied by \(\lambda\), so its Ptolemy inequality is exact even though \(F\) is a seminorm on the plane.

The lower-bound triple is nonzero and pairwise distinct. The condition \(\lambda\le\sqrt2\) is used exactly once: it makes each of the four denominator-side norms choose the Euclidean branch. At \(\lambda=\sqrt2\) the two branches tie, so the endpoint is included.

No numerical experiment or finite search is used in the proof.

## Relationship to prior work
Banaś and Frączek introduced the plane \(R_\lambda^2\) with the same norm while studying convexity, smoothness, and deformation. Their article contains no Ptolemy calculation. A later paper by Yang and Yang studies the generalized family
\[
\|x\|_{\lambda,p}=\max\{\lambda|x_1|,\|x\|_p\}
\]
and computes James-type and von Neumann--Jordan constants; its \(p=2\) case is the present space, and the inspected full text contains no Ptolemy result.

Zuo's 2012 paper develops exact Ptolemy criteria for absolute normalized norms and computes, among other examples, the different symmetric norm
\[
\max\{\|x\|_2,\mu\|x\|_\infty\}.
\]
The present norm becomes absolute normalized after the linear isometry
\[
(u,v)=(\lambda x_1,x_2),
\qquad
M_\lambda(u,v)=\max\left\{|u|,\sqrt{u^2/\lambda^2+v^2}\right\}.
\]
Its associated function is
\[
\psi_\lambda(t)
=
\max\left\{1-t,\sqrt{(1-t)^2/\lambda^2+t^2}\right\}.
\]
Let \(s=\sqrt{1-\lambda^{-2}}\) and \(t_\lambda=s/(1+s)\), where the two branches meet. For the Euclidean comparison function \(\psi_2\),
\[
\left(\frac{\psi_2(t_\lambda)}{\psi_\lambda(t_\lambda)}\right)^2
=
2-\lambda^{-2},
\]
whereas
\[
\left(\frac{\psi_2(1/2)}{\psi_\lambda(1/2)}\right)^2
=
\frac{2\lambda^2}{\lambda^2+1}.
\]
Their difference is
\[
\frac{\lambda^2-1}{\lambda^2(\lambda^2+1)}>0.
\]
Thus the midpoint-maximizer hypothesis in the relevant 2012 exact criterion does not hold for this transformed norm.

Zuo's 2018 comparison results likewise include midpoint-extremum criteria, while the more general off-midpoint theorem inspected there assumes symmetry of the associated function about \(1/2\). The function \(\psi_\lambda\) above is not symmetric for \(\lambda>1\), and the inspected 2018 paper contains no Banaś–Frączek instance.

## Limitations
The result gives the exact value only on \(1<\lambda\le\sqrt2\). The same branch argument gives the upper bound \(C_{\mathrm{Pt}}(R_\lambda^2)\le\lambda\) beyond that interval, but the lower witness used here ceases to attain it when \(\lambda>\sqrt2\).

A 2015 article on additional sufficient conditions for Ptolemy constants of absolute normalized norms is a plausible comparison source. Its abstract and bibliography were inspected, but a readable full text was not obtained through bounded lawful access attempts. This is retained as a residual originality risk rather than treated as evidence of noncoverage.

The original 1993 print article is older than its exact day-level online availability record. The day-level date used in metadata is the verified public availability date reported by the DML-CZ record, not an invented print day.

## References
1. J. Banaś and K. Frączek, “Deformation of Banach spaces,” Commentationes Mathematicae Universitatis Carolinae 34 (1993), 47–53. Stable record: DML-CZ 118554.
2. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” Journal of Inequalities and Applications 2012, 107 (2012). DOI: 10.1186/1029-242X-2012-107.
3. Z. Zuo, “A Reconsideration on the Ptolemy Constant of Absolute Normalized Norms,” Acta Mathematica Sinica, Chinese Series 58 (2015), 337–344. DOI: 10.12386/A2015sxxb0033.
4. C. Yang and X. Yang, “On the James type constant and von Neumann-Jordan constant for a class of Banaś-Fraczieck type spaces,” Journal of Mathematical Inequalities 10 (2016), 551–558. DOI: 10.7153/jmi-10-43.
5. Z.-F. Zuo, “On the Ptolemy constant of some concrete Banach spaces,” Mathematical Inequalities & Applications 21 (2018), 945–956. DOI: 10.7153/mia-2018-21-64.
