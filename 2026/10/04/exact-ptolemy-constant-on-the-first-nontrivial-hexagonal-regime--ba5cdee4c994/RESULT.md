# Exact Ptolemy constant on the first nontrivial hexagonal regime
## Finding
For the real hexagonal plane \(X_\gamma=(\mathbb R^2,N_\gamma)\), \(N_\gamma(x,y)=\max\{|y|,\ |x|+(1-\gamma)|y|\}\), one has \(C_{\mathrm{Pt}}(X_\gamma)=2/(1+\gamma)\) for every \(0<\gamma<1/2\).

The Ptolemy constant is
\[
C_{\mathrm{Pt}}(X)
=
\sup
\frac{\|x-y\|\,\|z\|}
{\|x-z\|\,\|y\|+\|z-y\|\,\|x\|},
\]
where the supremum runs over nonzero pairwise distinct \(x,y,z\in X\).

## Assumptions and scope
The scalar field is real and \(0<\gamma<1/2\). The norm is
\[
N_\gamma(x,y)=\max\left\{|y|,\ |x|+(1-\gamma)|y|\right\}.
\]
The source family is the hexagonal family whose unit ball has extreme points
\[
\pm(1,0),\qquad \pm(\gamma,1),\qquad \pm(\gamma,-1).
\]
No exact claim is made here for \(\gamma\ge 1/2\). The excluded endpoints are not needed for the stated result.

## Proof
Define the Hilbert norm
\[
H_\gamma(x,y)=\sqrt{x^2+(1-\gamma^2)y^2}.
\]
Every extreme point of the \(N_\gamma\)-unit ball has \(H_\gamma\)-norm one:
\[
H_\gamma(1,0)=1,\qquad
H_\gamma(\gamma,\pm1)=1.
\]
Since the \(N_\gamma\)-unit ball is the convex hull of these six points and the \(H_\gamma\)-unit ball is convex, the inclusion of unit balls gives
\[
H_\gamma(v)\le N_\gamma(v)
\]
for every \(v\in\mathbb R^2\).

For the reverse comparison, weighted Cauchy--Schwarz gives
\[
|x|+(1-\gamma)|y|
\le
\sqrt{1+\frac{(1-\gamma)^2}{1-\gamma^2}}\,
H_\gamma(x,y)
=
\sqrt{\frac{2}{1+\gamma}}\,
H_\gamma(x,y).
\]
Also
\[
|y|\le \frac{1}{\sqrt{1-\gamma^2}}H_\gamma(x,y).
\]
For \(0<\gamma<1/2\),
\[
\frac{1}{1-\gamma^2}<\frac{2}{1+\gamma},
\]
so both branches of \(N_\gamma\) satisfy
\[
N_\gamma(v)\le
c_\gamma H_\gamma(v),
\qquad
c_\gamma=\sqrt{\frac{2}{1+\gamma}}.
\]

Now fix nonzero pairwise distinct \(x,y,z\). By the norm comparison and the Hilbert-space Ptolemy inequality,
\[
N_\gamma(x-y)N_\gamma(z)
\le
c_\gamma^2 H_\gamma(x-y)H_\gamma(z)
\]
and
\[
H_\gamma(x-y)H_\gamma(z)
\le
H_\gamma(x-z)H_\gamma(y)+H_\gamma(z-y)H_\gamma(x).
\]
Because \(H_\gamma\le N_\gamma\), the last expression is at most the Ptolemy denominator formed with \(N_\gamma\). Therefore
\[
C_{\mathrm{Pt}}(X_\gamma)
\le
c_\gamma^2
=
\frac{2}{1+\gamma}.
\]

For equality, take
\[
x=(-1,0),\qquad
y=(\gamma,1),\qquad
z=(-(1+\gamma),1).
\]
A direct evaluation gives
\[
N_\gamma(x-y)=2,\qquad N_\gamma(z)=2,
\]
while
\[
N_\gamma(x-z)=N_\gamma(y)=N_\gamma(x)=1,
\qquad
N_\gamma(z-y)=1+2\gamma.
\]
Hence the Ptolemy ratio is
\[
\frac{4}{1+(1+2\gamma)}=\frac{2}{1+\gamma},
\]
which matches the upper bound.

## Verification
The argument is symbolic and covers every real \(0<\gamma<1/2\); no finite enumeration is used as evidence for the quantified claim. The upper bound follows from a global norm comparison, not from a presumed orientation of an optimizing configuration.

The critical inequality
\[
(1-\gamma^2)^{-1}<2/(1+\gamma)
\]
is equivalent to \(\gamma<1/2\), so the parameter threshold is intrinsic to the proof. The lower-bound triple is nonzero and pairwise distinct throughout the stated interval, and all six displayed norms were recomputed directly from the defining maximum.

## Relationship to prior work
Chica and Merí's dated 2014 preprint studies exactly this hexagonal family and computes its rank-one numerical index. Its full text defines the norm and extreme points above and contains no Ptolemy calculation.

Llorens-Fuster, Mazcuñán-Navarro, and Reich study Ptolemy constants and compute a single space called the hexagon space. The accessible article preview describes one fixed norm, not the parameterized Chica--Merí family, so it does not state the interval formula proved here. Its full text was not lawfully readable in the bounded comparison and is retained as a residual risk.

Zuo's 2012 framework treats absolute normalized norms by comparison with the Euclidean associated function. For the present family the associated function is
\[
\psi_\gamma(t)=\max\{t,1-\gamma t\}.
\]
For \(0<\gamma<1/2\), \(\psi_\gamma\) lies above the Euclidean comparison function near \(t=0\) but below it near \(t=1\); thus the global one-sided comparison hypotheses used by the relevant exact criteria do not apply. The 2012 article contains no occurrence of either “hexagon” or the Martín--Merí family.

Zuo's 2018 comparison theorems include midpoint-extremum criteria and, for the more flexible off-midpoint results, a symmetry hypothesis on the associated function. The function \(\psi_\gamma\) is not symmetric about \(1/2\) for \(0<\gamma<1/2\), so those inspected exact mechanisms do not imply the claim.

## Limitations
The result is restricted to the nontrivial interior regime \(0<\gamma<1/2\). The same proof gives the corresponding endpoint inequalities, but endpoints are omitted from the final claim because fixed endpoint spaces already occur in earlier Ptolemy literature.

A 2015 reconsideration of Ptolemy constants for absolute normalized norms announces additional sufficient conditions. Its abstract and bibliographic material were inspected, but a readable full text was not obtained in bounded lawful access attempts. Likewise, the 2010 fixed-hexagon paper was available only through its detailed article preview. These are recorded originality risks, not proof dependencies.

The source date used for cohort classification is the date printed on the publicly available author preprint, June 8, 2014; the later journal publication date is not used.

## References
1. M. Chica and J. Merí, “Rank-1 numerical index of some families of norms on the plane,” author preprint dated June 8, 2014; later published in Linear and Multilinear Algebra 63 (2015), 1817–1828. DOI: 10.1080/03081087.2014.975670.
2. E. Llorens-Fuster, E. M. Mazcuñán-Navarro, and S. Reich, “The Ptolemy and Zbăganu constants of normed spaces,” Nonlinear Analysis 72 (2010), 3984–3993. DOI: 10.1016/j.na.2010.01.030.
3. Z. Zuo, “The Ptolemy constant of absolute normalized norms on \(\mathbb R^2\),” Journal of Inequalities and Applications 2012, 107. DOI: 10.1186/1029-242X-2012-107.
4. Z. Zuo, “A Reconsideration on the Ptolemy Constant of Absolute Normalized Norms,” Acta Mathematica Sinica, Chinese Series 58 (2015), 337–344. DOI: 10.12386/A2015sxxb0033.
5. Z.-F. Zuo, “On the Ptolemy constant of some concrete Banach spaces,” Mathematical Inequalities & Applications 21 (2018), 945–956. DOI: 10.7153/mia-2018-21-64.
