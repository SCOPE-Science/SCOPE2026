# A rational counterexample to the density-two conjecture for mixing skew tent maps

## Finding

Conjecture 3.5 of Alsedà, Misiurewicz and Pérez (2020) asserts that the invariant probability density of every topologically mixing expanding skew tent map is at most \(2\). This is false. For the explicit mixing skew tent map
\[
f(x)=\begin{cases}
\frac{21}{20}x+\frac{19}{40},&0\le x\le\frac12,\\
2(1-x),&\frac12\le x\le1,
\end{cases}
\]
its unique absolutely continuous invariant probability measure has a density \(\rho\) obeying
\[
\rho(y)\ge\frac{170333841}{67511439}>\frac52
\quad\text{for almost every }y\in\left(\frac{779}{800},1\right).
\]
The set where this strict violation occurs has positive Lebesgue length \(21/800\). Moreover, the same density bound above \(5/2\) persists for all skew tent slope pairs in some open neighborhood of \((21/20,2)\) within the mixing class.

## Assumptions and scope

The skew tent family is normalized by \(f(c)=1\), \(f(1)=0\), and \(c=1-1/t\), where the left and right slopes are \(s>1\) and \(-t<-1\), respectively. The stated parameters are \(s=21/20\), \(t=2\), \(c=1/2\). The inequalities
\[
1<\frac1s+\frac1t=\frac{61}{42}<2=t
\]
put this map in the topologically mixing expanding class \(\mathfrak X\) in the cited source (Section 2). In that class the absolutely continuous invariant probability measure exists and is unique. The assertion concerns its normalized density, not an arbitrary scalar multiple of an invariant density.

## Proof

We use the exact density representation recorded as Theorem 3.1 in Alsedà–Misiurewicz–Pérez (2020), originally due to Ito–Tanaka–Nakada (1979). Define \(z_0=0\), \(w_0=1\), and recursively
\[
z_{n+1}=f(z_n),\qquad w_{n+1}=\frac{w_n}{f'(z_n)}.
\]
Then \(\widehat\rho(y)=\sum_{n\ge0}w_n\mathbf1_{[z_n,1]}(y)\) is an invariant density, and
\[
Z=\int_0^1\widehat\rho(y)\,dy
=\sum_{n\ge0}w_n(1-z_n)>0,
\qquad \rho=\widehat\rho/Z.
\]
These series converge absolutely because every branch derivative has modulus at least \(21/20\). None of the first seventeen orbit points is the turning point, so their derivatives are unambiguous.

For \(0\le n\le16\), exact iteration using only rational arithmetic gives
\[
\max_{0\le n\le16}z_n=\frac{779}{800},\quad
H=\sum_{n=0}^{16}w_n=\frac{171583841}{85766121},
\]
\[
I=\sum_{n=0}^{16}w_n(1-z_n)=\frac{66261439}{85766121},
\qquad w_{16}=\frac{62500}{85766121}.
\]
The attached executable `CHECK.py` recomputes these fractions, together with all intermediate orbit points, without numerical rounding.

Every later derivative has modulus at least \(21/20\). Therefore both the remaining absolute total weight and the remaining absolute contribution to the normalization are at most
\[
R=\frac{|w_{16}|}{(21/20)-1}=\frac{1250000}{85766121},
\qquad
\sum_{n\ge17}|w_n|\le R,\qquad
\left|\sum_{n\ge17}w_n(1-z_n)\right|\le R.
\]
In particular \(Z\in[I-R,I+R]\), where \(I-R>0\). For \(779/800<y<1\), all seventeen initial indicators are one. Thus \(\widehat\rho(y)\ge H-R>0\) and
\[
\rho(y)\ge\frac{H-R}{I+R}
=\frac{171583841-1250000}{66261439+1250000}
=\frac{170333841}{67511439}>\frac52.
\]
The last inequality is strict because
\[
2\cdot170333841-5\cdot67511439=3110487>0.
\]
This proves the positive-measure counterexample.

For robustness, the first seventeen branches and orbit positions vary continuously with the two slopes whenever the finite orbit avoids the turning point. They do so at this parameter pair. The parameter inequalities defining the mixing class, the inequality \(\max_{n\le16}z_n<1\), positivity of \(I-R\), and the strict lower-bound inequality are all open conditions. Repeating the preceding finite-tail argument therefore yields a nonempty open set of counterexamples. This continuity argument does not require any asserted uniform continuity of the entire invariant density.

## Verification

Run `python CHECK.py` under Python 3. The script uses exact `fractions.Fraction` arithmetic, checks that the map belongs to the mixing parameter regime, builds seventeen orbit-and-weight terms, reconstructs \(H\), \(I\) and \(R\), and checks that the bound exceeds \(5/2\) on an interval of length \(21/800\). This is a finite certificate for the inequalities needed in the proof; the infinite tail is controlled separately by the geometric derivative estimate. The established invariant-density formula is explicitly credited, not re-proved here.

## Relationship to prior work

Alsedà, Misiurewicz and Pérez (2020, arXiv:2004.01813v1), Theorem 3.1, cite Ito, Tanaka and Nakada (1979) for the signed orbit-jump representation; their Conjecture 3.5 explicitly proposes the universal bound \(\rho\le2\) for mixing expanding skew tent maps. The present counterexample retains that exact representation and contradicts the proposed universal bound. Their separate Conjecture 3.4, asking for *some* universal finite upper bound, is not addressed.

Billings and Bollt (2001) and Mackey and Tyran-Kamińska (2008) study invariant densities in skew tent families, including exact formulas on selected Markov parameter sets. These general density methods do not by themselves give the explicit seventeen-step inequality above. The full text of Billings–Bollt was not accessible for an exhaustive comparison, so the possibility of prior unrecognized examples remains a publication-priority risk. No claim of inventing the orbit-jump representation or of fully settling density bounds is made.

## Limitations

The result invalidates only the numerical ceiling \(2\) in Conjecture 3.5. It does not disprove the existence of any finite universal ceiling or determine the largest density over all mixing skew tent maps. It does not give the exact essential supremum for the displayed map. The bound is not a symbolic closed form for the full invariant density. The existence of an open neighborhood is qualitative, with no explicit neighborhood radius. A further comprehensive independent publication-priority audit remains to be performed.

## References

1. L. Alsedà, M. Misiurewicz and R. A. Pérez, *Flexibility of entropies for piecewise expanding unimodal maps*, arXiv:2004.01813v1, first public 3 April 2020. Sections 2–4, especially Theorem 3.1 and Conjectures 3.4–3.5. https://arxiv.org/html/2004.01813v1
2. S. Ito, S. Tanaka and H. Nakada, *On unimodal linear transformations and chaos II*, Tokyo Journal of Mathematics 2 (1979), 241–259. Cited as the source of the invariant-density formula in reference 1.
3. L. Billings and E. M. Bollt, *Probability density functions of some skew tent maps*, Chaos, Solitons & Fractals 12 (2001), 365–376. https://doi.org/10.1016/S0960-0779(99)00204-0
4. M. C. Mackey and M. Tyran-Kamińska, *Central limit theorem behavior in the skew tent map*, Chaos, Solitons & Fractals 38 (2008), 789–805. https://www.mcgill.ca/mathematical-physiology-lab/files/mathematical-physiology-lab/2008jan_mcm_tyran_kaminska_cltbehaviour_skewtentmap.pdf
